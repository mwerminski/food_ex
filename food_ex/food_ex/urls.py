from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('users.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('pricing.urls')),
    path('api/', include('product_repository.urls')),
]
