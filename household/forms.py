from django.contrib.auth.models import User
from django import forms
from .models import Task, Shopping, Bin, Bins
from datetime import date


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


class AddBinDetailsForm(forms.ModelForm):
  class Meta:
    model = Bins
    fields = (
      'next_collection_date',  
      'bins_collected', 
      'bins_next_collected',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default value for next_collection_date
        today = date.today()
        self.fields['next_collection_date'].initial = today.strftime('%Y-%m-%d')
    
    widgets = {
      'bins_collected': forms.CheckboxSelectMultiple(),
      'bins_next_collected': forms.CheckboxSelectMultiple(),
      'next_collection_date': forms.widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    labels = {
      'bins_collected': 'Select all bins being collected in your next collection',
      'bins_next_collected': 'If you have different bins collected each week, select all bins being collected in the collection AFTER your next collection',
    }


class AddToDoForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = (
      'description',
      'priority',
      'due_date',
    )
    widgets = {
      'description': forms.TextInput(
        attrs={'class': 'form-control'}),
      'priority': forms.CheckboxInput(),
      'due_date': forms.DateInput(
        attrs={'type': 'date'}),
    }
    labels = {
            'description': False, 
            'due_date': 'Due by'
        }