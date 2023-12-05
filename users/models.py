from django.contrib.auth.models import AbstractUser
from django.db import models

from .user_manager import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.IntegerField(null=True)
    address = models.CharField(max_length=100)

    object = CustomUserManager()
