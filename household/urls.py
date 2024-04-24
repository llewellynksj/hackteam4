from django.urls import path
from . import views

urlpatterns = [
  path('', views.display_household, name='household'),
  path('food/', views.FoodTaskView.as_view(), name='food'),
  path('laundry/', views.LaundryTaskView.as_view(), name='laundry'),
]