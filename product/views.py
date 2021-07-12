from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from models.models import Product
from product.serializer import ProductSerializer, ProductUpdateSerializer


class ProductsCreateViewSet(generics.CreateAPIView):
    """
        Creacion de un producto
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductsListViewSet(generics.ListAPIView):
    """
        Listar productos
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductsRetrieveOrDestroyViewSet(generics.RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        """
            Obtiene produto by id
        """
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
            Elimina producto by id
        """
        return self.destroy(request, *args, **kwargs)


class ProductsUpdateView(generics.UpdateAPIView):
    """
        Actualziar  productos
    """
    serializer_class = ProductUpdateSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
