from rest_framework import serializers

from models.models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"


class ShipmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ["order" , "products"]
