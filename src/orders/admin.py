from django.contrib import admin
from . import models


# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ("customer", "total_quantity", "total_price", "created")


admin.site.register(models.Cart, CartAdmin)


class ProductInCartAdmin(admin.ModelAdmin):
    list_display = (
        "cart",
        "product",
        "quantity",
        "price",
        "total_price",
    )


admin.site.register(models.ProductInCart, ProductInCartAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("delivery_adress", "phone", "cart", "created", "updated")


admin.site.register(models.Order, OrderAdmin)