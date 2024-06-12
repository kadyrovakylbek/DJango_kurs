from django.urls import path
from .views import home, ad_detail, category_ads, create_ad, create_category

urlpatterns = [
    path('', home, name='home'),
    path('ad/<int:pk>/', ad_detail, name='ad_detail'),
    path('category/<int:pk>/', category_ads, name='category_ads'),
    path('create_ad/', create_ad, name='create_ad'),
    path('create_category/', create_category, name='create_category'),
]