from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
  """
  Model to store task information
  """
  class Task(models.Model):
    TASK_AREAS = [
        ('kitchen', 'Kitchen'),
        ('food', 'Food'),
        ('laundry', 'Laundry'),
        ('bins', 'Bins'),
        ('other', 'Other'),
    ]

    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=TASK_AREAS, default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.description


