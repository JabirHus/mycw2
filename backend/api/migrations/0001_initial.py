# Generated by Django 5.1.1 on 2024-11-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Computer",
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
                ("price", models.FloatField()),
                ("description", models.TextField()),
                (
                    "computer_type",
                    models.CharField(
                        choices=[("MC", "Macintosh"), ("PC", "Personal Computer")],
                        default="PC",
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
