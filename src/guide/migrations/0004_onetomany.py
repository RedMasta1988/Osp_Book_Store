# Generated by Django 4.2.5 on 2023-10-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("guide", "0003_writer_discription"),
    ]

    operations = [
        migrations.CreateModel(
            name="OneToMany",
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
            ],
        ),
    ]
