# ads/forms.py
from django import forms
from .models import Ad, Category

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'image', 'contact', 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
