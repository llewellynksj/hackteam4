from django.urls import path

from .views import FamilyListView

app_name = 'family'

urlpatterns = [
    path('', FamilyListView.as_view(), name='family'),
]
