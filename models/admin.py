from django.contrib import admin

# Register your models here.
from models.models import  Product, Order, Payment


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Payment)
