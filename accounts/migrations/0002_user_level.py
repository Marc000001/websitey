# Generated by Django 4.1.2 on 2022-10-24 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="level",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]