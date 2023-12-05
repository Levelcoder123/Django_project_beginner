from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=80)
    branch = models.CharField(max_length=100)
    services = models.TextField()
    is_islamic = models.BooleanField()

    def __str__(self):
        return f"{self.name}, {self.branch}"
