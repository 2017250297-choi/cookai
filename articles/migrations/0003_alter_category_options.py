# Generated by Django 4.2.2 on 2023-06-22 03:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]