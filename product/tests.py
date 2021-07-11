from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

from models.models import Product
from product.serializer import ProductSerializer


class ProductTest(APITestCase):

    def test_create(self):
        url = reversed("ecommerce-api:Productos")

        product = Product.objects.create(id=999, name="test", price=1200)
        serializer = ProductSerializer(product)

        response = self.client.post(url, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.filter(id=999).get().name, product.name)