from django.db import models


# Create your models here.
class Bank(models.Model):
    bank_name = models.CharField(max_length=80)
    bank_branch = models.CharField(max_length=100)
    bank_services = models.TextField()
    is_islamic_bank = models.BooleanField()
