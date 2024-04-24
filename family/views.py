from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse

from .form import ChildForm
from .models import Child


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
            instance.save()
        return super().form_valid(form)


class FamilyListView(LoginRequiredMixin, FormView):
    template_name = 'family/index.html'
    model = Child
    form_class = ChildForm

    def days_old(self):
        pass

    def get_queryset(self):
        """
        Built in method used to fetch data from a database
        """

        data = self.model.objects.filter(user=self.request.user).values()

        return data

    def get_context_data(self, **kwargs):
        """
        Built in method used to send data to template
        """

        context = super(FamilyListView, self).get_context_data(**kwargs)

        context['queryset'] = self.get_queryset()

        # date_format = '%m/%d/%Y'
        #
        # birth_date = datetime.strptime(context['queryset'][0]['birth_date'].strftime(date_format), date_format)
        #
        # now = datetime.strptime(datetime.today().strftime(date_format), date_format)
        #
        # delta = (now - birth_date).days
        #
        # print('birth_date', birth_date)
        # print('now', now)
        # print('delta', delta)

        return {'context': context, 'form': self.form_class()}
