from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# Create your models here.
from authentication.models import User


class Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.BigIntegerField(default=0)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    purchase_date = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField('Product')

    class Meta:
        db_table = "order"

    def __str__(self):
        return f"Orden : {self.id}"


class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.BigIntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    orders = models.ManyToManyField('Order')

    class Meta:
        db_table = "payment"

    def __str__(self):
        return f"Pagos : {self.id}"


class Shipment(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.OneToOneField(Order, verbose_name='id', on_delete=models.PROTECT)
    products = models.ManyToManyField(Product)
    send_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "shipment"

    def __str__(self):
        return f"Envio numero : {self.id}"
