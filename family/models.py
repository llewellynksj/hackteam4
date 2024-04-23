from django.db import models
from datetime import date

class Child(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
      return self.name
    
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
    
