from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse

from .form import ChildForm, DailyTaskForm, TabsForm
from .models import Child, ChildTasks, Tabs


# Create your views here.

# create
class FamilyCreateView(LoginRequiredMixin, CreateView):
    model = Child
    form_class = ChildForm
    message = 'You have successfully created a family.'

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse('family:family')

    def form_invalid(self, form):
        messages.error(self.request, self.message)
        return reverse('family:family')

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = self.request.user
            # return self.get_success_url()
        return super().form_valid(form)


class DailyTaskCreateView(LoginRequiredMixin, CreateView):
    """
    Creates new daily tasks for child
    """

    model = ChildTasks
    form_class = DailyTaskForm
    message = 'You have successfully created a daily task.'

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse('family:family')

    def form_valid(self, form):
        if form.is_valid():
            # gets child name from an url path
            child_name = self.request.path.split('/')[3]

            instance = form.save(commit=False)
            instance.user = self.request.user
            instance.child_name = child_name
        return super().form_valid(form)


class TabsCreateView(LoginRequiredMixin, CreateView):
    """
    Creates new tabs for child
    """

    model = Tabs
    form_class = TabsForm

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = self.request.user
        return super().form_valid(form)


# read
class FamilyListView(LoginRequiredMixin, FormView):
    # template to be used
    template_name = 'family/index.html'
    # Child model
    model = Child
    # form taken from form.py file
    form_class = ChildForm
    # fetches current date of computer
    current_date = datetime.now().date()

    def get_age(self, birth_date):
        """
        The Method is used not to return the age of the child in days.
        """

        # convert to correct format
        start_date = datetime(self.current_date.year, self.current_date.month, self.current_date.day)
        end_date = datetime(birth_date.year, birth_date.month, birth_date.day)

        # difference between two dates
        delta = start_date - end_date

        # Calculate years and remaining days
        years = delta.days // 365
        remaining_days = delta.days % 365

        # Calculate months and remaining days
        months = remaining_days // 30
        remaining_days %= 30

        # subtracts current date from birthdate and returns amount of days
        return years, months, remaining_days

    def get_queryset(self):
        """
        Built in method used to fetch data from a database
        """

        # fetches children from db based on logged-in username
        data = self.model.objects.filter(user=self.request.user).values()
        tasks = ChildTasks.objects.filter(user=self.request.user, ).values()

        # empty list used to return only the data that I want
        context = []

        # for loop used to iterate over data, and return only name and age
        for d in data:
            # dictionary literal to append to for fetching name and age from data
            obj = {'name': d['child_name'], 'age': self.get_age(d['birth_date']),
                   'tasks': [i for i in tasks if i['child_name'] == d['child_name']]}

            # once gathered correct data append to a context list
            context.append(obj)

        return context

    def get_context_data(self, **kwargs):
        """
        Built in method used to send data to template
        """

        context = super(FamilyListView, self).get_context_data(**kwargs)

        # store data from queryset to context object
        context['queryset'] = self.get_queryset()

        return {'context': context, 'form': self.form_class(), 'daily_tasks_form': DailyTaskForm}


class DailyTaskDeleteView(LoginRequiredMixin, DeleteView):
    model = ChildTasks
    template_name = 'family/index.html'
    success_message = 'You have successfully deleted a daily task.'
    success_url = "/family"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
