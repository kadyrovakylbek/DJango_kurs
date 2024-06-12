# ads/views.py
from django.shortcuts import render, redirect
from .models import Ad, Category
from .forms import AdForm, CategoryForm

def home(request):
    ads = Ad.objects.all()
    categories = Category.objects.all()
    return render(request, 'ads/home.html', {'ads': ads, 'categories': categories})

def ad_detail(request, pk):
    ad = Ad.objects.get(pk=pk)
    return render(request, 'ads/ad_detail.html', {'ad': ad})

def category_ads(request, pk):
    category = Category.objects.get(pk=pk)
    ads = category.ads.all()
    return render(request, 'ads/category_ads.html', {'category': category, 'ads': ads})

def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AdForm()
    return render(request, 'ads/create_ad.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'ads/create_category.html', {'form': form})
