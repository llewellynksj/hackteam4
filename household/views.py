from django.shortcuts import render, redirect
from django.views import View, generic
from django.urls import reverse_lazy
from .models import Task, Shopping, Bin, Bins
from .forms import AddTaskForm, AddShoppingForm, AddBinDetailsForm


def display_household(request):
    return render(request, 'household.html', {})

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
    template_name = "food.html"
    category = "food"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopping_form'] = AddShoppingForm()
        context['shopping_list'] = Shopping.objects.filter(user=self.request.user)
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
    template_name = "laundry.html"
    category = "laundry"

class KitchenTaskView(BaseTaskView):
    template_name = "kitchen.html"
    category = "kitchen"

class BinsTaskView(BaseTaskView):
    template_name = "bins.html"
    category = "bins"

    def get_queryset(self):
        # Filter bins by the current user
        return Bins.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bins_form'] = AddBinDetailsForm()
        # Pass the queryset of bins to the template context
        context['queryset'] = self.get_queryset()
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
    template_name = "general.html"
    category = "other"


# Edit and Delete Views
class DeleteTask(generic.DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('food')

class EditTask(generic.UpdateView):
    model = Task
    form_class = AddTaskForm
    template_name = edit_task.html
    success_url = reverse_lazy('food')