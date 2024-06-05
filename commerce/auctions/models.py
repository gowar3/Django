from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):

    Name = models.CharField(max_length=64)
    Price = models.IntegerField()

    def __str__(self):

        return f"{self.id}: {self.origin} to {self.destination}"
