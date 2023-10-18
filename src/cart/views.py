from django.shortcuts import render
from proj.settings import AUTH_USER_MODEL
from cart.models import Cart, ProductCart
from catalog.models import Book

# Create your views here.
def view_cart(request):

    return render(request, 'cart/cart.html')