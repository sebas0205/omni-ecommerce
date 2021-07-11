from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics

from models.models import Payment
from payments.serializer import PaymentSerializer, PaymentUpdateSerializer


class PaymentsCreateViewSet(generics.CreateAPIView):
    """
        Creacion de un pago
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentsListViewSet(generics.ListAPIView):
    """
        Listar Pagos realizados
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentsRetrieveOrDestroyViewSet(generics.RetrieveDestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        """
            Obtiene un pago   by id
        """
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
            Elimina pago by id
        """
        return self.destroy(request, *args, **kwargs)


class PaymentsUpdateView(generics.UpdateAPIView):
    """
        Actualziar  Pagos
    """
    serializer_class = PaymentUpdateSerializer
    queryset = Payment.objects.all()
    lookup_field = 'id'
