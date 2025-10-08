from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description',
            'thumbnail',
            'category',
            'stock',
            'size',
            'color',
            'rating',
            'is_featured'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-[#0B3954] rounded-md px-3 py-2'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full border border-[#0B3954] rounded-md px-3 py-2'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border border-[#0B3954] rounded-md px-3 py-2 h-28'
            }),
            'thumbnail': forms.URLInput(attrs={
                'class': 'w-full border border-[#0B3954] rounded-md px-3 py-2',
                'placeholder': 'https://example.com/image.jpg'
            }),
            'rating': forms.NumberInput(attrs={
                'min': 1, 'max': 5,
                'class': 'w-full border border-[#0B3954] rounded-md px-3 py-2'
            }),
            'size': forms.TextInput(attrs={
                'class': 'w-full border border-[#0B3954] rounded-md px-3 py-2'
            }),
            'color': forms.TextInput(attrs={
                'class': 'w-full border border-[#0B3954] rounded-md px-3 py-2'
            }),
        }
