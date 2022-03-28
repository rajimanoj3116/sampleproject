from typing import ClassVar
from django.db import models

# Create your models here.
class Expense(models.Model):
    expensename=models.CharField(max_length=500)
    amount=models.IntegerField()
    class Meta:
        db_table='expense'

class Balance(models.Model):
   balance=models.IntegerField()
   class Meta:
       db_table='balance'        