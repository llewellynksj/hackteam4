from django.shortcuts import render
from django.views import generic
from .models import Task


def display_household(request):
  task_list = Task.objects.all()

  context = {
    'task_list': task_list,
  }

  return render(request, 'household.html', context)


