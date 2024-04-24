from django.shortcuts import render, redirect
from django.views import View
from .models import Task, Shopping
from .forms import AddTaskForm, AddShoppingForm


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

class GeneralTaskView(BaseTaskView):
    template_name = "general.html"
    category = "other"
