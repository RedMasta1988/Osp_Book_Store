# Generated by Django 4.2.5 on 2023-10-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="productincart",
            name="price",
            field=models.DecimalField(
                decimal_places=2, default=1, max_digits=6, verbose_name="Price"
            ),
            preserve_default=False,
        ),
    ]