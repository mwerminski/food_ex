from .models import Price
from rest_framework import permissions, viewsets

from .serializers import PriceSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]