from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView, FormView, TemplateView, UpdateView
from typing import Any, Dict, Optional
from django.shortcuts import get_object_or_404
from catalog.models import Book
from .models import Cart, ProductInCart, Order

from django.db import models
from . import forms
from account.models import User

# Create your views here.

class CartDetailView(DetailView):
    template_name="orders/cart.html"
    model=Cart  
     
       
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont =super().get_context_data(**kwargs)
        if self.request.session.get("cart_id"):
            cart_pk = self.request.session.get("cart_id")
            cont["total_quantity_in_cart"] = Cart.objects.get(pk=cart_pk).total_quantity
        return cont

    def get_object(self, *args, **kwargs):
        # cart_id
        cart_pk = self.request.session.get("cart_id") # int / None
        customer = self.request.user # User / AnonimousUser -> User / None
        if customer.is_anonymous:
            customer = None
        cart, created = Cart.objects.get_or_create(
            pk=cart_pk,
            defaults={
                "customer": customer
            }
        )
        # cart
        product_id = self.request.GET.get("product")
        quantity = self.request.GET.get("quantity")
        if product_id and quantity:
            quantity = int(quantity)
            product = Book.objects.get(pk=int(product_id))
            price = Book.objects.get(pk=int(product_id)).price
            product_in_cart, product_in_cart_created = ProductInCart.objects.get_or_create(
                cart=cart,
                product=product,
                defaults={
                    "quantity":quantity,
                    "price": price * quantity
                }
            )
            if not product_in_cart_created:
                product_in_cart.quantity = product_in_cart.quantity + quantity
                product_in_cart.price = product_in_cart.price + price*quantity
                product_in_cart.save()
            if created:
                self.request.session['cart_id'] = cart.pk
        return cart
      


class CartAddDeleteItemView(DetailView):
    template_name = "orders/cart.html"
    model = Cart

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
            cont =super().get_context_data(**kwargs)
            if self.request.session.get("cart_id"):
                cart_pk = self.request.session.get("cart_id")
                cont["total_quantity_in_cart"] = Cart.objects.get(pk=cart_pk).total_quantity
            return cont

    def get_object(self, *args, **kwargs):
        # cart_id
        
        cart_pk = self.request.session.get("cart_id") # int / None
        customer = self.request.user # User / AnonimousUser -> User / None
        if customer.is_anonymous:
            customer = None
        cart, created = Cart.objects.get_or_create(
            pk=cart_pk,
            defaults={
                "customer": customer
            }
        )
        # cart
        product_id = self.request.GET.get("product")
        action = self.request.GET.get("action")
        if product_id and action and action in ['add', 'delete']:
            product = Book.objects.get(pk=int(product_id))
            price = Book.objects.get(pk=int(product_id)).price
            product_in_cart = get_object_or_404(
                ProductInCart,
                cart__pk=cart.pk,
                product__pk=product.pk,
            )
            if action == "add":
                addition = 1
            else:
                if product_in_cart.quantity <= 1:
                    product_in_cart.delete()
                    return cart
                addition = -1
            product_in_cart.quantity = product_in_cart.quantity + addition
            product_in_cart.price = product_in_cart.quantity * price
            product_in_cart.save()
        return cart


class OrderCreateView(FormView):
    form_class = forms.CreateOrderForm
    template_name = "orders/create_order.html"
    success_url = reverse_lazy("orders:done_order")

    def form_valid(self, form):
        delivery_adress = form.cleaned_data.get('delivery_adress')

        
        cart_pk = self.request.session.get("cart_id")
        # updating the USER when forming an order 
        customer_login = Cart.objects.get(pk=cart_pk)
        customer_login.customer=self.request.user
        customer_login.save(update_fields=["customer"])
        #
        cart = get_object_or_404(
           Cart, 
           pk=cart_pk,
        
        ) 
        obj = Order.objects.create(
            delivery_adress = delivery_adress,
             cart= cart
        )
      
        del self.request.session['cart_id']
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont =super().get_context_data(**kwargs)
        if self.request.session.get("cart_id"):
            cart_pk = self.request.session.get('cart_id')
            cont["total_quantity_in_cart"] = Cart.objects.get(pk=cart_pk).total_quantity
            cont["object"] = Cart.objects.get(pk=cart_pk)
            
        return cont
    
class OrderSuccess(TemplateView):
    template_name = "orders/done_order.html"

#Update   
class OrderUpdateView(UpdateView):
    model= Order
    form_class= forms.OrderModelForm
    template_name = "orders/order_update.html"
    success_url = "/"
    # def get_success_url(self):
    #     success_url=reverse_lazy("HomePage")
    #     if self.request.user.is_superuser or self.request.user.is_staff:
    #         success_url=reverse_lazy("person:UsersListView")
    #     return success_url

 

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont =super().get_context_data(**kwargs)
        cont["object_cart"] = ProductInCart.objects.all()
        return cont

#Detail    
class OrderDetailView(DetailView):
    model= Order
    template_name = 'orders/detail_order.html'
    success_url = '/'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont =super().get_context_data(**kwargs)
        cont["object_cart"] = ProductInCart.objects.all()
        return cont
    
