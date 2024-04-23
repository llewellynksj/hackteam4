from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['name'] = ['title']

        return {'context': context}
