# Generated by Django 5.0.4 on 2024-06-13 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0005_listing_comments_alter_comment_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="user",
            field=models.CharField(max_length=64),
        ),
    ]
