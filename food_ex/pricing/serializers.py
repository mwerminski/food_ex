from .models import Price, PriceCalculation
from rest_framework import serializers


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = ['product', 'base_price']

class CalculatedPriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PriceCalculation
        fields = ['calculated_price', 'order_id']
    
class CalculatedPricePartialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PriceCalculation
        fields = ['order_id']
        
