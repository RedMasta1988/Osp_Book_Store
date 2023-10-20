from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    name = models.CharField(_("Автор отзыва"), max_length=100)
    comment = models.TextField(_("Отзыв"), max_length=3000, blank=False, null=False)
    publish = models.DateTimeField(_("Дата внесения"), default=timezone.now)
    def __str__(self):
        return f"Автор комментария:({self.name}), Комментарий:{self.comment}"