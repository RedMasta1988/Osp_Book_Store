from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models import Sum
from catalog.models import Book

User = get_user_model()
STATUSES = (
        ('Новый', "NEW"),
        ('Оформлен', "OFORMLEN"),
        ('В работе', "IN_WORK"),
        ('Выдан', "VYDAN"),
        ('Отменен', "CLOSED")
    )

# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        verbose_name=_("Покупатель"),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Корзина({self.pk}): {self.customer}"

    @property
    def total_quantity(self):
        total_quantity=0
        for item  in self.products.all():
            total_quantity += item.quantity
        return total_quantity
    
    @property
    def total_price(self):
        total_price = 0
        for item in self.products.all():
            total_price += item.total_price
        return total_price

    class Meta:
        verbose_name = "Корзину"
        verbose_name_plural = "Корзины"


class ProductInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name=_("Корзина"),
        on_delete=models.CASCADE,
        related_name="products",
    )
    product = models.ForeignKey(
        Book, verbose_name=_("Товар"), on_delete=models.PROTECT, related_name="carts"
    )
    quantity = models.PositiveIntegerField(_("Количество"), default=1)
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=6,
        decimal_places=2
        )
    created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name='updated',
        auto_now_add=False,
        auto_now=True
    )

    def __str__(self):
        return f"Товар({self.pk}): {self.product.title_of_the_book} - Количество:{self.quantity}"


    @property
    def total_price(self):
        return self.product.price * self.quantity

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"



class Order(models.Model):
    delivery_adress = models.TextField(_("Адрес"))
    phone = models.CharField(
        _("Телефон"),
        max_length=13
    ) 
    cart = models.OneToOneField(Cart, verbose_name=_("Корзина"), on_delete=models.PROTECT)


    created = models.DateTimeField(_("Создан"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("Обновлен"), auto_now=True, auto_now_add=False)
