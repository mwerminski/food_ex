from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'prices', 'final_price', 'retailer', 'client', 'distance', 'location', 'created_at', 'finished_at', 'status']
