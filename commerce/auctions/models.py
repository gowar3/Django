from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=CASCADE)
    comment = models.CharField(max_length=128)

    def __str__(self):

        return f"{self.user.username}: {self.comment}"

class Listing(models.Model):

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    price = models.IntegerField()
    comments = models.ManyToManyField(Comment, blank=True)

    def __str__(self):

        return f"{self.title} {self.description} {self.price}"

class Bid(models.Model):

    owner = models.CharField(max_length=64)
    offer = models.IntegerField()

    def __str__(self):

        return f"{self.owner} {self.offer}"
