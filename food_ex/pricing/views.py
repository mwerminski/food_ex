from .models import Price, PriceCalculation
from orders.models import Order
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response

from .serializers import PriceSerializer, CalculatedPriceSerializer, CalculatedPricePartialSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class CalculatedPriceViewSet(viewsets.ModelViewSet):
    queryset = PriceCalculation.objects.all()
    serializer_class = CalculatedPriceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def calculate_total_price(request, format=None):
    serializer = CalculatedPricePartialSerializer(data=request.data)
    errors = None
    if serializer.is_valid():
        try:
            order_id = request.query_params.get('order_id')
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        magic_value = 21.37 #advanced algorithm that will make me rich
        total_price = sum(price_obj.base_price for price_obj in order.prices)
        total_price += magic_value * order.distnace
        
        response_serializer = CalculatedPriceSerializer({'order_id' : order_id, 'calculated_price': total_price})
        
        if request.method == 'GET':
                if response_serializer.is_valid(): 
                    return Response(response_serializer.data)
            
        if request.method == 'PUT':
                if response_serializer.is_valid():
                    response_serializer.save()
                    return Response(response_serializer.data)
                
        errors = response_serializer.errors

    return Response(errors, status=status.HTTP_400_BAD_REQUEST)