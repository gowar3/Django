from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    price = models.IntegerField()

    def __str__(self):

        return f"{self.title} {self.description} {self.price}"


class Comment(models.Model):

    poster = models.CharField(max_length=64, default="Anonymous")
    comment = models.CharField(max_length=128)
    listings = models.ManyToManyField(Listing, blank=True, related_name= "comments")

    def __str__(self):

        return f"{self.poster}: {self.comment}"

class Bid(models.Model):

    owner = models.CharField(max_length=64, default="Anonymous")
    offer = models.IntegerField()
    bids = models.ManyToManyField(Listing, blank=True, related_name= "bids")

    def __str__(self):

        return f"{self.owner}: {self.offer}"
