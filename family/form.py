import datetime

from django import forms
from .models import Child, ChildTasks


class ChildForm(forms.ModelForm):
    """
    Form for creating and updating child objects
    """

    class Meta:
        model = Child
        fields = ['child_name', 'birth_date']
        widgets = {'birth_date': forms.widgets.DateTimeInput(attrs={'type': 'date'})}

    def __init__(self, *args, **kwargs):
        super(ChildForm, self).__init__(*args, **kwargs)

        self.fields['child_name'].required = True

        self.fields['birth_date'].required = True
        self.fields['birth_date'].widget.attrs['class'] = 'datepicker'
        self.fields['birth_date'].widget.attrs['max'] = datetime.date.today().strftime(
            '%Y-%m-%d')


class DailyTaskForm(forms.ModelForm):
    """
    Form for creating daily tasks
    """

    class Meta:
        model = ChildTasks
        fields = ['daily_tasks']

    def __init__(self, *args, **kwargs):
        super(DailyTaskForm, self).__init__(*args, **kwargs)

        self.fields['daily_tasks'].required = True
        self.fields['daily_tasks'].label = ''
