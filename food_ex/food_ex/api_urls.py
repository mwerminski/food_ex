from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('orders.urls')),
    path('', include('pricing.urls')),
    path('', include('product_repository.urls')),
]
