from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Task
from .forms import AddMealIdeaForm

class TaskView(View):

    def get(self, request, *args, **kwargs):
        queryset = Task.objects.filter(category="food")
        return render(
            request,
            "household.html",
            {
                "queryset": queryset,
                "add_meal_idea_form": AddMealIdeaForm(),
            },
        )
    
    def post(self, request, *args, **kwargs):
        queryset = Task.objects.filter(category="food")
        add_meal_idea_form = AddMealIdeaForm(data=request.POST)
        if add_meal_idea_form.is_valid():
            task = add_meal_idea_form.save(commit=False)
            task.user = request.user
            task.category = "food"
            task.save()
        else:
            add_meal_idea_form = AddMealIdeaForm()
            
        return render(
            request,
            "household.html",
            {
                "queryset": queryset,
                "add_meal_idea_form": add_meal_idea_form,
            },
        )
