# Generated by Django 4.1.2 on 2022-10-30 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0003_patient_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="slug",
            field=models.SlugField(blank="True"),
        ),
    ]
