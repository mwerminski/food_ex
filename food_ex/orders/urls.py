from django.urls import include, path
from rest_framework import routers

from orders import views

router = routers.SimpleRouter()
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]