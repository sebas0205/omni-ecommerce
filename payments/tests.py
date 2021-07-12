from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from models.models import Product, Order, Payment


class PaymentTest(APITestCase):

    def setUp(self) -> None:
        user = get_user_model().objects.create_user(email="email@email.com", password="123")
        product1 = Product.objects.create(id=1, name="product1", price=2000)
        product2 = Product.objects.create(id=2, name="product2", price=2000)
        product3 = Product.objects.create(id=3, name="product3", price=2000)

        order1 = Order.objects.create(user=user)
        order1.products.add(product1)

        order2 = Order.objects.create(user=user)
        order2.products.add(product2)
        order2.products.add(product3)

        payment1 = Payment.objects.create(value=1000)
        payment1.orders.add(order1)

        payment2 = Payment.objects.create(value=3000)
        payment2.orders.add(order2)

    def test_create(self):
        url = reverse("payments:Payments_create")

        payload = {
            "value": 2000,
            "orders": [
                1, 2
            ]
        }

        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        payment = Payment.objects.filter(id=response.data["id"]).first()

        self.assertEqual([o.id for o in payment.orders.all()], [1, 2])

    def test_notfound_payment_by_id(self):
        url = reverse("productos:products_get_delete", args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_payment_by_id(self):
        url = reverse("payments:Payments_get_delete", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)

    def test_update(self):
        url = reverse("payments:Payments_update", args=[1])

        payload = {
            "value": 4000,
            "orders": [
                1, 2
            ]
        }

        response = self.client.put(url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse("ordenes:Orders_get_delete", args=[1])
        response = self.client.get(url)
        payment = Payment.objects.filter(id=response.data["id"]).first()

        self.assertEqual(payment.value, 4000)
