from django.urls import path
from orders import views

app_name="orders"

urlpatterns = [
      path('cart/', views.CartDetailView.as_view(), name='cartview'), 
      path('cart-items-edit/', views.CartAddDeleteItemView.as_view(), name='cart-items-edit'), 
      path('create-order/', views.OrderCreateView.as_view(), name='create-order'), 
      path('done_order/', views.OrderSuccess.as_view(), name='done_order'), 
      path('order-update/<int:pk>', views.OrderUpdateView.as_view(), name='order-update'), 
      path('order-detail/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'), 
]