import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from models.models import Payment, Product, Order, Shipment


def create_enviroment():
    user = get_user_model().objects.create_user(email="sebas0205@gmail.com", password="123")
    product1 = Product.objects.create(id=1, name="product1", price=2000)
    product2 = Product.objects.create(id=2, name="product2", price=2000)
    product3 = Product.objects.create(id=3, name="product3", price=2000)

    order1 = Order.objects.create(user=user)
    order1.products.add(product1)

    order2 = Order.objects.create(user=user)
    order2.products.add(product2)
    order2.products.add(product3)

    shipment = Shipment.objects.create(order=order1)
    shipment.products.add(product1)



class PaymentTest(APITestCase):

    def test_create(self):
        url = reverse("shipment:shipments_create")

        payload = {
            "order": 2,
            "products": [
                2
            ]
        }

        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        shipment = Shipment.objects.filter(id=response.data["id"]).first()

        self.assertEqual(shipment.order.id, 2)

    def test_notfound_shipment_by_id(self):
        url = reverse("shipment:shipments_get_delete", args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_shipment_by_id(self):
        create_enviroment()
        url = reverse("shipment:shipments_get_delete", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)

    def test_update(self):
        create_enviroment()
        url = reverse("shipment:shipments_update", args=[1])

        payload = {
            "order": 2,
            "products": [
                2, 3
            ]
        }

        response = self.client.put(url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse("shipment:shipments_get_delete", args=[1])
        response = self.client.get(url)
        shipment = Shipment.objects.filter(id=response.data["id"]).first()

        self.assertEqual(shipment.order.id, 2)

    def test_send_shipment(self):
        create_enviroment()
        url = reverse("shipment:shipments_send", args=[1])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse("shipment:shipments_get_delete", args=[1])
        response = self.client.get(url)
        shipment = Shipment.objects.filter(id=response.data["id"]).first()

        self.assertEqual(shipment.send_date, datetime.date.today())

    def test_delivery_shipment(self):
        create_enviroment()
        url = reverse("shipment:shipments_delivery", args=[1])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse("shipment:shipments_get_delete", args=[1])
        response = self.client.get(url)
        shipment = Shipment.objects.filter(id=response.data["id"]).first()

        self.assertEqual(shipment.delivery_date, datetime.date.today())
