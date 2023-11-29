from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
