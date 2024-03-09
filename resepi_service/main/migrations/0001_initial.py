# Generated by Django 4.2.8 on 2024-03-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("Name", models.CharField(max_length=30)),
                ("Sername", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254)),
                ("content", models.TextField(blank=True)),
                ("photo", models.ImageField(upload_to="photos/%Y/%m/%d/")),
                ("time_create", models.DateTimeField(auto_now_add=True)),
                ("is_published", models.BooleanField(default=True)),
            ],
        ),
    ]
