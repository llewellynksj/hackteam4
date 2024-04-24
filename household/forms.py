from django.contrib.auth.models import User
from django import forms
from .models import Task, Shopping


class AddTaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = (
      'description',
    )
    widgets = {
      'description': forms.TextInput(
        attrs={'class': 'form-control'}),
    }
    labels = {
            'description': False, 
        }


class AddShoppingForm(forms.ModelForm):
  class Meta:
    model = Shopping
    fields = (
      'item',
    )
    widgets = {
      'item': forms.TextInput(
        attrs={'class': 'form-control'}),
    }
    labels = {
            'item': False, 
        }
