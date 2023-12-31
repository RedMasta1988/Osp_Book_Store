# Generated by Django 4.2.5 on 2023-10-21 00:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                    "name",
                    models.CharField(max_length=100, verbose_name="Автор комментария"),
                ),
                ("comment", models.TextField(max_length=3000, verbose_name="Описание")),
            ],
        ),
    ]
