from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):

    name = models.CharField(max_length=64)
    price = models.IntegerField()

    def __str__(self):

        return f"{self.id}: {self.name} to {self.price}"
