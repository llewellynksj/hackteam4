from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime


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
  priority = models.BooleanField(default=False)
  due_date = models.DateField(default=date.today)
  completed = models.BooleanField(default=False)
  category = models.CharField(max_length=20, choices=TASK_AREAS, default='other')

  def __str__(self):
    return f'User:{self.user} - {self.category} : {self.description}'


class Shopping(models.Model):
  user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  item = models.TextField(blank=True)

  def __str__(self):
    return f'User:{self.user} - Shopping item: {self.item}'


class Bins(models.Model):
    FREQUENCY_CHOICES = [
        ('week', 'Week'),
        ('fortnight', 'Fortnight'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    next_collection_date = models.DateField(default=date.today)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    different_collections_each_week = models.BooleanField(default=False)
    bins_collected = models.ManyToManyField('Bin', related_name='bins_collected', blank=True)
    bins_next_collected = models.ManyToManyField('Bin', related_name='bins_next_collected', blank=True)

    def __str__(self):
        return f'Bins for {self.user.username}'
    
    def get_next_collection_day(self):
        # Get the day of the week for the next_collection_date
        return self.next_collection_date.strftime("%A")


class Bin(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def populate_bins(cls):
        bin_names = ['General Waste', 'Recycling', 'Food Bin', 'Garden Waste']
        for name in bin_names:
            cls.objects.get_or_create(name=name)


