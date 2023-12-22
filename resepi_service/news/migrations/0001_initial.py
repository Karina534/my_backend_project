# Generated by Django 4.2.8 on 2023-12-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Articl",
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
                (
                    "title",
                    models.CharField(
                        default="None", max_length=50, verbose_name="Название"
                    ),
                ),
                (
                    "anons",
                    models.CharField(
                        default="None", max_length=250, verbose_name="Анонс"
                    ),
                ),
                ("full_text", models.TextField(verbose_name="Статья")),
                ("data", models.DateTimeField(verbose_name="Дата публикации")),
            ],
        ),
    ]
