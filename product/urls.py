from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "productos"

urlpatterns = [
    path("create", views.ProductsCreateViewSet.as_view(), name="products_create"),
    path("list/", views.ProductsListViewSet.as_view(), name="products"),
    path("list/<id>", views.ProductsRetrieveOrDestroyViewSet.as_view(), name="products_get_delete"),
    path("update/<id>", views.ProductsUpdateView.as_view(), name="products_update")
]
