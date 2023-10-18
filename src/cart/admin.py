from django.contrib import admin
from . import models
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('customer',"all_quantity", "total_price", 'created', 'updated')
admin.site.register(models.Cart, CartAdmin)

class ProductCartAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity',"price","total_price",)
admin.site.register(models.ProductCart, ProductCartAdmin)