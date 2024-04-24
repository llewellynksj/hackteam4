from django.contrib.auth.models import User
from django import forms
from .models import Task


class AddMealIdeaForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = (
      'description',
    )
    widgets = {
      'description': forms.TextInput(
        attrs={'class': 'form-control'}),
    }