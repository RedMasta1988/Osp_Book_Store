# Generated by Django 4.2.5 on 2023-10-15 16:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("guide", "0004_onetomany"),
    ]

    operations = [
        migrations.DeleteModel(
            name="OneToMany",
        ),
    ]