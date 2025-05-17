from django.urls import include, path
from rest_framework import routers

from pricing import views

router = routers.SimpleRouter()
router.register(r'prices', views.PriceViewSet)
router.register(r'calculated-prices', views.CalculatedPriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('prices/calculate-price', views.calculate_total_price)
]