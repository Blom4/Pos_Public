from django import forms
from .models import *

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name','price','size','category','quantity']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product','quantity']
