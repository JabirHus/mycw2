# Generated by Django 5.1.1 on 2024-11-08 00:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                ("contact_info", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="PatientTreatment",
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
                ("treatment_date", models.DateField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.patient"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Treatment",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "patients",
                    models.ManyToManyField(
                        through="api.PatientTreatment", to="api.patient"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Computer",
        ),
        migrations.AddField(
            model_name="patienttreatment",
            name="treatment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.treatment"
            ),
        ),
    ]