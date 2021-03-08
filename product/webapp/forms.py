from django import forms
from django.db.models import PositiveSmallIntegerField, DecimalField
from django.forms import Textarea, CharField

from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'remainder', 'price')
        widgets = {
            'description': Textarea(attrs={ 'cols': 50, 'rows': 10}),

        }