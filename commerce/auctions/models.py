from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):

    creator = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    price = models.IntegerField()
    winner = models.CharField(max_length=64, default="")
    status = models.CharField(max_length=64, default="active")
    users = models.ManyToManyField(User, blank=True, related_name= "wishlist")

    def __str__(self):

        return f"{self.title} {self.description} {self.price}"


class Comment(models.Model):

    poster = models.CharField(max_length=64)
    comment = models.CharField(max_length=128)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comment_listing")
    listings = models.ManyToManyField(Listing, blank=True, related_name= "comments")

    def __str__(self):

        return f"{self.poster}: {self.comment}"

class Bid(models.Model):

    owner = models.CharField(max_length=64)
    offer = models.IntegerField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid_listing")
    bids = models.ManyToManyField(Listing, blank=True, related_name= "bids")

    def __str__(self):

        return f"{self.owner}: {self.offer}"
