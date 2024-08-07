# Generated by Django 5.0.4 on 2024-07-11 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0019_category_listing_categories"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="listing",
            name="categories",
        ),
        migrations.AddField(
            model_name="category",
            name="categories",
            field=models.ManyToManyField(
                blank=True, related_name="categories", to="auctions.listing"
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="listing",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="category_listing",
                to="auctions.listing",
            ),
        ),
    ]
