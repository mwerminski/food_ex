from .models import Price
from rest_framework import serializers


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = ['product', 'base_price']

    