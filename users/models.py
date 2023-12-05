from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.IntegerField(null=True)
    address = models.CharField(max_length=100)
