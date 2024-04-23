from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Child


# Create your views here.
class FamilyListView(LoginRequiredMixin, ListView):
    template_name = 'family/index.html'
    model = Child

    def get_context_data(self, **kwargs):
        context = super(FamilyListView, self).get_context_data(**kwargs)

        context['name'] = ['family']

        return {'context': context}
