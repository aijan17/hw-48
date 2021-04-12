from django import forms
from django.forms import Textarea

from webapp.models import Product, Order


class DateInput(forms.DateTimeInput):
    input_type = 'date'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'remainder', 'price')
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 10}),

        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('goods','username','telephone','adress',)
        widgets = {
            'datetimes': DateInput(),
        }

