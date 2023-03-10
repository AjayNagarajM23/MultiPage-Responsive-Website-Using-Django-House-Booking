# Generated by Django 4.1.4 on 2022-12-29 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PostHouse",
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
                ("name", models.CharField(max_length=30)),
                ("phno", models.TextField()),
                ("housename", models.TextField()),
                ("houseno", models.TextField()),
                ("houseaddr", models.TextField()),
                ("houseimg", models.ImageField(upload_to="pics")),
                ("description", models.TextField()),
            ],
        ),
    ]
