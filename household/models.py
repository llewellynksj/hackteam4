from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
  """
  Model to store task information
  """
  TASK_AREAS = [
      ('kitchen', 'Kitchen'),
      ('food', 'Food'),
      ('laundry', 'Laundry'),
      ('bins', 'Bins'),
      ('other', 'Other'),
  ]

  user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  description = models.TextField(blank=True)
  category = models.CharField(max_length=20, choices=TASK_AREAS, default='other')

  def __str__(self):
    return self.description


