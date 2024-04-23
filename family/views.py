from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .form import ChildForm
from .models import Child


# Create your views here.
class FamilyListView(LoginRequiredMixin, FormView):
    template_name = 'family/index.html'
    model = Child
    form_class = ChildForm

    def get_context_data(self, **kwargs):
        context = super(FamilyListView, self).get_context_data(**kwargs)

        context['name'] = ['family']

        return {'context': context, 'form': self.form_class()}
