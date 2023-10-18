from django.db import models
from django.utils.translation import gettext_lazy as _
from proj.settings import AUTH_USER_MODEL
from django.db.models import Sum
from catalog.models import Book

# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_("Покупатель"), on_delete=models.PROTECT, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Корзина({self.pk}): {self.customer}"
    
    @property
    def all_quantity(self):
        return self.products.aggregate(total=Sum("quantity")).get("total")
  


    @property
    def total_price(self):
        total_price=0
        for item in self.products.all():
            total_price+=item.total_price
        return total_price
    

    class Meta:
        verbose_name = "Корзину"
        verbose_name_plural = "Корзины"

class ProductCart(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_("Корзина"), on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(Book, verbose_name=_("Товар"), on_delete=models.PROTECT, related_name="carts")
    quantity = models.PositiveIntegerField(_("Количество"), default=1)

    def __str__(self):
        return f"Товар({self.pk}): {self.product.title_of_the_book} - Количество:{self.quantity}" 
    @property
    def price(self):
        return self.product.price
    
    @property
    def total_price(self):
        return self.product.price * self.quantity
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"