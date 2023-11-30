from django.db import models

from users.models import User
from accounts.models import Account


# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=80)
    branch = models.CharField(max_length=100)
    services = models.TextField()
    is_islamic = models.BooleanField()
    user = models.ManyToManyField(User)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default=True)
