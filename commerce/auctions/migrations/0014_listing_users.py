# Generated by Django 5.0.4 on 2024-06-18 06:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0013_alter_bid_listing_alter_comment_listing_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="users",
            field=models.ManyToManyField(
                blank=True, related_name="wishlist", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
