from django.urls import path

from .views import FamilyListView, FamilyCreateView, DailyTaskCreateView, DailyTaskDeleteView

app_name = 'family'

urlpatterns = [
    path('', FamilyListView.as_view(), name='family'),
    path('create/', FamilyCreateView.as_view(), name='family_create'),
    path('daily-tasks/<str:child_name>/', DailyTaskCreateView.as_view(), name='daily_task_create'),
    path('daily-tasks/delete/<int:pk>', DailyTaskDeleteView.as_view(), name='daily_task_delete'),
]
