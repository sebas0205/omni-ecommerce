import asyncio
import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from ecommerce.services.EmailService import send_email_send_shipmet, send_email_delivery_shipmet
from models.models import Shipment
from shipment.serializer import ShipmentSerializer, ShipmentUpdateSerializer


class ShipmentsCreateViewSet(generics.CreateAPIView):
    """
        Creacion de un shipmento
    """
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()


class ShipmentsListViewSet(generics.ListAPIView):
    """
        Listar shipmentos
    """
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()


class ShipmentsRetrieveOrDestroyViewSet(generics.RetrieveDestroyAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        """
            Obtiene produto by id
        """
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
            Elimina shipmento by id
        """
        return self.destroy(request, *args, **kwargs)


class ShipmentsUpdateView(generics.UpdateAPIView):
    """
        Actualziar  shipmentos
    """
    serializer_class = ShipmentUpdateSerializer
    queryset = Shipment.objects.all()
    lookup_field = 'id'


class ShipmentsSendViewSet(generics.UpdateAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()

    def retrieve(self, request, *args, **kwargs):
        shipment = self.get_object()
        shipment.send_date = datetime.today()
        shipment.save()
        asyncio.run(send_email_send_shipmet(shipment))


class ShipmentsDeliveryViewSet(generics.UpdateAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()

    def retrieve(self, request, *args, **kwargs):
        shipment = self.get_object()
        shipment.delivery_date = datetime.today()
        shipment.save()
        asyncio.run(send_email_delivery_shipmet(shipment))
