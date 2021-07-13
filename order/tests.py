from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from models.models import Order, Product
from order.serializer import OrderSerializer


def create_enviroment():
    user = get_user_model().objects.create_user(email="email@email.com", password="123")
    product1 = Product.objects.create(id=1, name="product1", price=2000)
    product2 = Product.objects.create(id=2, name="product2", price=2000)
    product3 = Product.objects.create(id=3, name="product3", price=2000)

    order1 = Order.objects.create(user=user)
    order1.products.add(product1)

    order2 = Order.objects.create(user=user)
    order2.products.add(product2)
    order2.products.add(product3)


class OrderTest(APITestCase):

    def test_create(self):
        url = reverse("ordenes:Orders_create")

        payload = {
            "user": 1,
            "products": [
                3
            ]
        }

        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        order = Order.objects.filter(id=response.data["id"]).first()

        self.assertEqual([o.id for o in order.products.all()], [3])

    def test_notfound_order_by_id(self):
        url = reverse("ordenes:Orders_get_delete", args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_order_by_id(self):
        create_enviroment()
        url = reverse("ordenes:Orders_get_delete", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)

    def test_get_order_by_user(self):
        create_enviroment()
        url = reverse("ordenes:orders_by_user", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)

    def test_update(self):
        create_enviroment()
        url = reverse("ordenes:Orders_update", args=[2])

        payload = {"products": [1, 2, 3]}

        response = self.client.put(url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse("ordenes:Orders_get_delete", args=[2])
        response = self.client.get(url)
        order = Order.objects.filter(id=response.data["id"]).first()

        self.assertEqual([p.id for p in order.products.all()], [1, 2, 3])
