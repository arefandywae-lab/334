from django import forms
from .models import Product

CATEGORIES = [
    ('Accessories', 'Accessories'),
    ('Audio', 'Audio'),
    ('Electronics', 'Electronics'),
    ('Furniture', 'Furniture'),
    ('Office', 'Office'),
]


class ProductForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORIES)

    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'category']
