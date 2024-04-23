from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Child(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=100)
    birth_date = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['user', 'child_name']

    def __str__(self):
        return f'Parent: {self.user} of {self.child_name}'
