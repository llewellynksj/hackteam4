from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views import View, generic
from django.urls import reverse_lazy
from .models import Task, Shopping, Bin, Bins
from .forms import AddTaskForm, AddShoppingForm, AddBinDetailsForm, AddToDoForm


def display_household(request):
    return render(request, 'hh/household.html', {})

class BaseTaskView(View):
    template_name = None
    form_class = AddTaskForm
    category = None
    
    def get_queryset(self):
        return Task.objects.filter(category=self.category)
    
    def get_context_data(self, **kwargs):
        context = {}
        context['queryset'] = self.get_queryset()
        context['task_form'] = self.form_class()
        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(**kwargs))
    
    def post(self, request, *args, **kwargs):
        task_form = self.form_class(data=request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            task.category = self.category
            task.save()
            return redirect(request.path)
        return render(request, self.template_name, self.get_context_data(**kwargs))

class FoodTaskView(BaseTaskView):
    template_name = "hh/food.html"
    category = "food"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopping_form'] = AddShoppingForm()
        context['shopping_list'] = Shopping.objects.filter(user=self.request.user)
        context['active_tab'] = 'food' 
        return context
    
    def post(self, request, *args, **kwargs):
        if 'task_submit' in request.POST:
            return super().post(request, *args, **kwargs)
        elif 'shopping_submit' in request.POST:
            shopping_form = AddShoppingForm(data=request.POST)
            if shopping_form.is_valid():
                shopping = shopping_form.save(commit=False)
                shopping.user = request.user
                shopping.save()
                return redirect(request.path)
        return render(request, self.template_name, self.get_context_data(**kwargs))

class LaundryTaskView(BaseTaskView):
    template_name = "hh/laundry.html"
    category = "laundry"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_form'] = AddToDoForm()
        context['active_tab'] = 'laundry'  
        return context


    def post(self, request, *args, **kwargs):
        todo_form = AddToDoForm(data=request.POST)
        if todo_form.is_valid():
            todo = todo_form.save(commit=False)
            todo.user = request.user
            todo.category = self.category
            todo.save()
            return redirect(request.path)
        return render(request, self.template_name, self.get_context_data(**kwargs))

class KitchenTaskView(BaseTaskView):
    template_name = "hh/kitchen.html"
    category = "kitchen"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_form'] = AddToDoForm()
        context['active_tab'] = 'kitchen' 
        return context
    
    def post(self, request, *args, **kwargs):
        todo_form = AddToDoForm(data=request.POST)
        if todo_form.is_valid():
            todo = todo_form.save(commit=False)
            todo.user = request.user
            todo.category = self.category
            todo.save()
            return redirect(request.path)
        return render(request, self.template_name, self.get_context_data(**kwargs))

class BinsTaskView(BaseTaskView):
    template_name = "hh/bins.html"
    category = "bins"

    def get_queryset(self):
        # Filter bins by the current user
        return Bins.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bins_form'] = AddBinDetailsForm()
        # Pass the queryset of bins to the template context
        context['queryset'] = self.get_queryset()
        context['active_tab'] = 'bins' 
        return context

    def post(self, request, *args, **kwargs):
        bins_form = AddBinDetailsForm(data=request.POST)
        if bins_form.is_valid():
            bins_data = bins_form.cleaned_data
            bins_data['user'] = request.user
            existing_bin_details = Bins.objects.filter(user=request.user).first()
            if existing_bin_details:
                # If bin details exist, update them
                existing_bin_details.bins_collected.set(bins_data['bins_collected'])
                existing_bin_details.bins_next_collected.set(bins_data['bins_next_collected'])
                existing_bin_details.next_collection_date = bins_data['next_collection_date']
                existing_bin_details.save()
            else:
                # Otherwise, create a new record
                bins = bins_form.save(commit=False)
                bins.user = request.user
                bins.save()
            return redirect(request.path)
        return render(request, self.template_name, self.get_context_data(**kwargs))

class GeneralTaskView(BaseTaskView):
    template_name = "hh/general.html"
    category = "other"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_form'] = AddToDoForm()
        context['active_tab'] = 'general' 
        return context

    def post(self, request, *args, **kwargs):
        todo_form = AddToDoForm(data=request.POST)
        if todo_form.is_valid():
            todo = todo_form.save(commit=False)
            todo.user = request.user
            todo.category = self.category
            todo.save()
            return redirect(request.path)
        return render(request, self.template_name, self.get_context_data(**kwargs))

# Edit and Delete Views
class DeleteTask(generic.DeleteView):
    model = Task
    template_name = 'hh/delete_task.html'
    success_url = reverse_lazy('household')  # Default URL, change as needed

    def delete(self, request, *args, **kwargs):
        previous_url = request.POST.get('previous_url')

        self.object = self.get_object()
        self.object.delete()

        if previous_url:
            return HttpResponseRedirect(previous_url)
        else:
            return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        previous_url = self.request.META.get('HTTP_REFERER', '/')
        context['previous_url'] = previous_url
        return context


class DeleteShoppingItem(generic.DeleteView):
    model = Shopping
    template_name = 'hh/delete_shopping_item.html'
    success_url = reverse_lazy('food')
