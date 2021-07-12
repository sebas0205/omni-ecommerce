from rest_framework import serializers

from models.models import Order
from product.serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'user', 'purchase_date', 'products']


class OrderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['products']
