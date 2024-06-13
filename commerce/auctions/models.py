from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    price = models.IntegerField()
    comments = models.ManyToManyField(Comment, blank=True, related_name="Listings")

    def __str__(self):

        return f"{self.title} {self.description} {self.price}"

class Bid(models.Model):

    owner = models.CharField(max_length=64)
    offer = models.IntegerField()

    def __str__(self):

        return f"{self.owner} {self.offer}"

class Comment(models.Model):

    user = models.CharField(max_length=64)
    comment = models.CharField(max_length=128)

    def __str__(self):

        return f"{self.user}: {self.comment}"
