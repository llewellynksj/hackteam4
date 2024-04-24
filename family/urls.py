from django.urls import path

from .views import FamilyListView, FamilyCreateView

app_name = 'family'

urlpatterns = [
    path('', FamilyListView.as_view(), name='family'),
    path('create/', FamilyCreateView.as_view(), name='family_create'),
]
