from django.urls import path
from . import views

urlpatterns = [
  path('food/', views.FoodTaskView.as_view(), name='household'),
  # path('laundry/', views.LaundryTaskView.as_view(), name='laundry_tasks'),
]