from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response

from models.models import Order
from order.serializer import OrderSerializer, OrderUpdateSerializer


class OrdersByUserViewSet(generics.ListAPIView):
    """
        Consultar ordenes por usuario
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get(self, request, user_id):
        queryset = self.get_queryset()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)




class OrdersCreateViewSet(generics.CreateAPIView):
    """
        Creacion de un producto
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrdersListViewSet(generics.ListAPIView):
    """
        Listar Ordernes
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrdersRetrieveOrDestroyViewSet(generics.RetrieveDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        """
            Obtiene orden  by id
        """
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
            Elimina Orden by id
        """
        return self.destroy(request, *args, **kwargs)


class OrdersUpdateView(generics.UpdateAPIView):
    """
        Actualziar  Orderos
    """
    serializer_class = OrderUpdateSerializer
    queryset = Order.objects.all()
    lookup_field = 'id'
