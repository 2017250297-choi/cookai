# Generated by Django 4.2.2 on 2023-06-21 06:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("articles", "0003_alter_article_like"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="like_comments", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]