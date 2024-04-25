from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
class TeamView(TemplateView):
    template_name = 'team/team.html'

    def get_context_data(self, **kwargs):
        context = super(TeamView, self).get_context_data(**kwargs)

        context['name'] = ['title']

        return {'context': context}