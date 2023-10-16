from django.db import models
from django.utils.translation import gettext_lazy as _



# Create your models here.
class Writer(models.Model):
    name = models.CharField(_("Автор"), max_length=100)
    discription = models.TextField(_("Описание"), max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Автора"
        verbose_name_plural = "Авторы"


class Serie(models.Model):
    name = models.CharField(_("Серия"), max_length=50)
    discription = models.TextField(_("Описание"), max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Серию"
        verbose_name_plural = "Серии"


class Genre(models.Model):
    name = models.CharField(_("Жанр"), max_length=50)
    discription = models.TextField(_("Описание"), max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class PublishingHouse(models.Model):
    name = models.CharField(_("Издательство"), max_length=50)
    discription = models.TextField(_("Описание"), max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"


