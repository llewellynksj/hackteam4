from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
  """
  Model to store task information
  """
  TASK_AREAS = [
      ('kitchen', 'Kitchen'),
      ('food', 'Food'),
      ('shop', 'Shop'),
      ('laundry', 'Laundry'),
      ('bins', 'Bins'),
      ('other', 'Other'),
  ]

  user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  description = models.TextField(blank=True)
  category = models.CharField(max_length=20, choices=TASK_AREAS, default='other')

  def __str__(self):
    return f'User:{self.user} - {self.category} : {self.description}'


class Shopping(models.Model):
  user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  item = models.TextField(blank=True)

  def __str__(self):
    return f'User:{self.user} - Shopping item: {self.item}'
