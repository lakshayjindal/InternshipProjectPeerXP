from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=140)
    dateOfExpense = models.DateField()
    category = models.CharField(max_length=140)
    description = models.TextField()
    amount = models.PositiveIntegerField()
    created_by = models.CharField(max_length=150)
    created_at = datetime.now()
    updated_at = datetime.now()
    
    def __str__(self):
        return self.name
