from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_id = models.IntegerField()
    user_email = models.EmailField()
    user_phone_number = models.IntegerField()
    user_address = models.CharField(max_length=100)
