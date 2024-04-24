from django.urls import path
from . import views

urlpatterns = [
  path('', views.display_household, name='household'),
  path('food/', views.FoodTaskView.as_view(), name='food'),
  path('laundry/', views.LaundryTaskView.as_view(), name='laundry'),
  path('kitchen/', views.KitchenTaskView.as_view(), name='kitchen'),
  path('bins/', views.BinsTaskView.as_view(), name='bins'),
  path('general/', views.GeneralTaskView.as_view(), name='general'),
]