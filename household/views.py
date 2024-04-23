from django.shortcuts import render
from django.views import generic
from .models import Task
from .forms import AddMealIdeaForm


class TaskList(generic.ListView):
    model = Task
    template_name = "household.html"
    context_object_name = "task_list" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddMealIdeaForm()
        context['task_list'] = Task.objects.filter(category="food")
        return context

    def post(self, request, *args, **kwargs):
        form = AddMealIdeaForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.category = "food"
            task.user = request.user  
            task.save()
            return redirect('household')
        else:
            return self.render_to_response(self.get_context_data(form=form))