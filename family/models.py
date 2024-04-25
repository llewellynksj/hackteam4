from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Child(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['child_name']

    def __str__(self):
        return f'Parent: {self.user} of {self.child_name}'


class ChildTasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=100)
    daily_tasks = models.CharField(max_length=100)
    important_dates = models.DateField(default=date.today)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['child_name']

    def __str__(self):
        return f'Child: {self.child_name} of {self.user}'


class Tabs(models.Model):
    """
    Tabs model to get track of currently working tab
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tab_name = models.CharField(max_length=100, default="")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return f'Tab: {self.tab_name} of {self.user}'
