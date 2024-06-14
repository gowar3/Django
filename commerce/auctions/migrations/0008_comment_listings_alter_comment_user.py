# Generated by Django 5.0.4 on 2024-06-14 05:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0007_remove_listing_comments"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="listings",
            field=models.ManyToManyField(
                blank=True, related_name="comments", to="auctions.listing"
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]