import datetime

from django import forms
from .models import Child


class ChildForm(forms.ModelForm):
    """
    Form for creating and updating child objects
    """

    class Meta:
        model = Child
        fields = ['child_name', 'birth_date']
        widgets = {'birth_date': forms.widgets.DateTimeInput(attrs={'type': 'date'})}

    # def __init__(self, *args, **kwargs):
    #     super(ChildForm, self).__init__(*args, **kwargs)
    #
    #     # sets validation for time_slots field
    #     self.fields['birth_date'].required = True
    #     # this sets a validation to enter a date more than 1 hour from now
    #     self.fields['birth_date'].widget.attrs['min'] = (
    #             datetime.datetime.now() + datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M')
