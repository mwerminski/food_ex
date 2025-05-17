from django.urls import include, path
from rest_framework import routers

from users import views

router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'companies', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]