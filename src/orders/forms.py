from django import forms
from . import models



class CreateOrderForm(forms.Form):
    delivery_adress = forms.CharField(
        required=True,
        widget =forms.Textarea
    )
    phone = forms.CharField(
        required=True
    )

class OrderModelForm(forms.ModelForm):
    class Meta: 
        model = models.Order
        fields = ['delivery_adress',"phone"]

class OrderDetailForm(forms.ModelForm):
    class Meta: 
        model = models.Order
        fields = ('delivery_adress', "phone", 'cart')