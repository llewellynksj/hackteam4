from django.shortcuts import render
from django.views import generic
from .models import Child


def display_family(request):
  
  return render(request, 'family.html', {})
