from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from .form import ChildForm
from .models import Child


# Create your views here.
class FamilyCreateView(LoginRequiredMixin, CreateView):
    model = Child
    form_class = ChildForm
    message = 'You have successfully created a child to your family.'

    def form_valid(self, form):
        """
        Once form is valid save to a database
        """

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = self.request.user
            return redirect('family:family')
        return super().form_valid(form)


class FamilyListView(LoginRequiredMixin, FormView):
    template_name = 'family/index.html'
    model = Child
    form_class = ChildForm

    def get_context_data(self, **kwargs):
        context = super(FamilyListView, self).get_context_data(**kwargs)

        context['name'] = ['family']

        return {'context': context, 'form': self.form_class()}
