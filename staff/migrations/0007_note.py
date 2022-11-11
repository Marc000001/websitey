# Generated by Django 4.1.2 on 2022-11-06 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0006_patient_admitted_patient_none_admitted"),
    ]

    operations = [
        migrations.CreateModel(
            name="Note",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_by", models.CharField(max_length=200)),
                ("note", models.TextField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notes",
                        to="staff.patient",
                    ),
                ),
            ],
        ),
    ]
