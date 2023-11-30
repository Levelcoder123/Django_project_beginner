from django.db import models

from users.models import User
from banks.models import Bank


# Create your models here.
class Account(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=15)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.type}, {self.number}"
