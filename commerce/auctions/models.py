from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    price = models.IntegerField()

    def __str__(self):

        return f"{self.id}: {self.title} to {self.price}"
