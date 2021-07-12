import asyncio
import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response

from models.models import Shipment
from shipment.serializer import ShipmentSerializer, ShipmentUpdateSerializer
from shipment.services.EmailService import send_email_delivery_shipmet, send_email_send_shipmet


class ShipmentsCreateViewSet(generics.CreateAPIView):
    """
        Creacion de un shipment
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


class ShipmentsSendViewSet(generics.RetrieveAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        shipment = self.get_object()
        shipment.send_date = datetime.date.today()
        shipment.save()
        response = send_email_send_shipmet(shipment=shipment)
        status_response = status.HTTP_200_OK if response["status"]=="OK" else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(response,status_response)


class ShipmentsDeliveryViewSet(generics.RetrieveAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()
    lookup_field= 'id'

    def retrieve(self, request, *args, **kwargs):
        shipment = self.get_object()
        shipment.delivery_date = datetime.date.today()
        shipment.save()
        response = send_email_delivery_shipmet(shipment)
        status_response = status.HTTP_200_OK if response["status"] == "OK" else status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(response, status_response)
