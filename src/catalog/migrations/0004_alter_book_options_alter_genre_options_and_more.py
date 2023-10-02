# Generated by Django 4.2.5 on 2023-10-02 18:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_remove_genre_book_remove_writer_book_book_publish"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={
                "ordering": ("-publish",),
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
            },
        ),
        migrations.AlterModelOptions(
            name="genre",
            options={
                "ordering": ("name",),
                "verbose_name": "Жанр",
                "verbose_name_plural": "Жанры",
            },
        ),
        migrations.AlterModelOptions(
            name="publishinghouse",
            options={
                "ordering": ("name",),
                "verbose_name": "Издательство",
                "verbose_name_plural": "Издательства",
            },
        ),
        migrations.AlterModelOptions(
            name="serie",
            options={
                "ordering": ("name",),
                "verbose_name": "Серия",
                "verbose_name_plural": "Серии",
            },
        ),
        migrations.AlterModelOptions(
            name="writer",
            options={
                "ordering": ("last_name",),
                "verbose_name": "Автор",
                "verbose_name_plural": "Авторы",
            },
        ),
        migrations.AlterField(
            model_name="book",
            name="active",
            field=models.CharField(
                choices=[("Да", "ДА"), ("Нет", "НЕТ")],
                default="Да",
                max_length=3,
                verbose_name="Доступен для заказа",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="genre",
            field=models.ManyToManyField(
                related_name="book_of_writer", to="catalog.genre", verbose_name="Жанр"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="publish",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                verbose_name="Дата внесения в каталог",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="writer",
            field=models.ManyToManyField(
                related_name="book_of_writer", to="catalog.writer", verbose_name="Автор"
            ),
        ),
        migrations.AlterField(
            model_name="genre",
            name="discription",
            field=models.TextField(max_length=300, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="publishinghouse",
            name="discription",
            field=models.TextField(max_length=300, verbose_name="Описание"),
        ),
    ]
