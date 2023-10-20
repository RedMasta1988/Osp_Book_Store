# Generated by Django 4.2.5 on 2023-10-21 00:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("guide", "0005_delete_onetomany"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genre",
            name="discription",
            field=models.TextField(
                blank=True, max_length=3000, null=True, verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Жанр"),
        ),
        migrations.AlterField(
            model_name="publishinghouse",
            name="discription",
            field=models.TextField(
                blank=True, max_length=3000, null=True, verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="publishinghouse",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Издательство"),
        ),
        migrations.AlterField(
            model_name="serie",
            name="discription",
            field=models.TextField(
                blank=True, max_length=3000, null=True, verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="serie",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Серия"),
        ),
        migrations.AlterField(
            model_name="writer",
            name="discription",
            field=models.TextField(
                blank=True, max_length=3000, null=True, verbose_name="Описание"
            ),
        ),
    ]
