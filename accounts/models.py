from django.db import models


# Create your models here.
class Account(models.Model):
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=15)
    account_amount = models.IntegerField()
