from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

ACTIVE_CHOICES = (("Да", "ДА"), ("Нет", "НЕТ"))


# Create your models here.
class Book(models.Model):
    title_of_the_book = models.CharField(_("Название книги"), max_length=50)
    cover_foto = models.ImageField(
        verbose_name="Фото обложки", upload_to=None, null=True, blank=True
    )
    price = models.DecimalField(_("Цена(BYN)"), max_digits=5, decimal_places=2)
    writer = models.ManyToManyField(
        "Writer", verbose_name=_("Автор"), related_name="book_of_writer"
    )
    serie = models.ForeignKey(
        "Serie", verbose_name=_("Серия"), on_delete=models.PROTECT
    )
    genre = models.ManyToManyField(
        "Genre", verbose_name=_("Жанр"), related_name="book_of_writer"
    )
    year_of_publication = models.IntegerField(_("Год издания"))
    page = models.IntegerField(_("Количество страниц"))
    binding = models.CharField(_("Переплёт"), max_length=50)
    format = models.CharField(_("Формат"), max_length=50)
    isbn = models.PositiveBigIntegerField(
        _("ISBN"),
        validators=[
            MinValueValidator(1000000000000),
            MaxValueValidator(9999999999999),
        ],
    )
    weight = models.IntegerField(_("Вес(гр)"))
    age = models.IntegerField(_("Возрастные ограничения"))
    publishing_house = models.ForeignKey(
        "PublishingHouse", verbose_name=_("Издательство"), on_delete=models.PROTECT
    )
    availability = models.IntegerField(_("Количество книг в наличии"))
    active = models.CharField(
        _("Доступен для заказа"),
        max_length=3,
        choices=ACTIVE_CHOICES,
        default="Да",
    )
    rating = models.PositiveIntegerField(
        _("Рейтинг(1-10)"),
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    publish = models.DateTimeField(_("Дата внесения в каталог"), default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Book({self.pk}): {self.title_of_the_book}"

    class Meta:
        ordering = ("-publish",)
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"


class Writer(models.Model):
    last_name = models.CharField(_("Фамилия"), max_length=50)
    first_name = models.CharField(_("Имя"), max_length=50)
    patronymic = models.CharField(_("Отчество"), max_length=50, null=True, blank=True)

    def __str__(self):
        return (
            f"Writer({self.pk}): {self.last_name} {self.first_name} {self.patronymic}"
        )

    class Meta:
        ordering = ("last_name",)
        verbose_name = "Автора"
        verbose_name_plural = "Авторы"


class Serie(models.Model):
    name = models.CharField(_("Серия"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Серию"
        verbose_name_plural = "Серии"


class Genre(models.Model):
    name = models.CharField(_("Жанр"), max_length=50)
    discription = models.TextField(_("Описание"), max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class PublishingHouse(models.Model):
    name = models.CharField(_("Издательство"), max_length=50)
    discription = models.TextField(_("Описание"), max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"
