from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from models.models import Product
from product.serializer import ProductSerializer


def create_enviroment() :
    Product.objects.create(id=777, name="test", price=2000)


class ProductTest(APITestCase):

    def test_create(self):
        url = reverse("productos:products_create")

        payload = {
            "id": 999,
            "name": "test",
            "price": 2000
        }

        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.filter(id=999).get().name, "test")

    def test_notfound_product_by_id(self):
        url = reverse("productos:products_get_delete", args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_product_by_id(self):
        create_enviroment()
        url = reverse("productos:products_get_delete", args=[777])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product = Product(**ProductSerializer(response.data).data)
        self.assertEqual(product.name, "test")

    def test_update(self):
        create_enviroment()
        url = reverse("productos:products_update", args=[777])

        payload = {
            "name": "test_updated",
            "price": 3000
        }

        response = self.client.put(url , payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse("productos:products_get_delete", args=[777])
        response = self.client.get(url)
        product = Product(**ProductSerializer(response.data).data)
        self.assertEqual(product.name, "test_updated")

