from django.shortcuts import render
from django.views import View
from .models import Task
from .forms import AddMealIdeaForm

class BaseTaskView(View):
    template_name = "household.html"
    form_class = None
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
        return render(request, self.template_name, self.get_context_data(**kwargs))

class FoodTaskView(BaseTaskView):
    form_class = AddMealIdeaForm
    category = "food"

class LaundryTaskView(BaseTaskView):
    form_class = AddLaundryTaskForm
    category = "laundry"
