from django.urls import include, path
from rest_framework import routers

from product_repository import views

router = routers.SimpleRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]