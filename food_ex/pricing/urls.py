from django.urls import include, path
from rest_framework import routers

from pricing import views

router = routers.SimpleRouter()
router.register(r'prices', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]