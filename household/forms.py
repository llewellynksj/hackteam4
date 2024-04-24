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
    
    # bins_collected = forms.ModelMultipleChoiceField(queryset=Bin.objects.all(), widget=forms.CheckboxSelectMultiple)
    # bins_next_collected = forms.ModelMultipleChoiceField(queryset=Bin.objects.all(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default value for next_collection_date
        today = date.today()
        self.fields['next_collection_date'].initial = today.strftime('%Y-%m-%d')
    
    widgets = {
      'frequency': forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
      'bins_collected': forms.CheckboxSelectMultiple(),
      'bins_next_collected': forms.CheckboxSelectMultiple(),
      'next_collection_date': forms.widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    labels = {
      'different_collections_each_week': 'Do you have different bins collected on different weeks?',
      'bins_collected': 'Select all bins being collected in your next collection',
      'bins_next_collected': 'If you have different bins collected each week, select all bins being collected in the collection AFTER your next collection',
    }
