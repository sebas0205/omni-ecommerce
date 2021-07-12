from django.urls import path

from shipment import views

app_name = "shipment"

urlpatterns = [
    path("", views.ShipmentsListViewSet.as_view(), name="shipments"),
    path("<id>", views.ShipmentsRetrieveOrDestroyViewSet.as_view(), name="shipments_get_delete"),
    path("create/", views.ShipmentsCreateViewSet.as_view(), name="shipments_create"),
    path("update/<id>", views.ShipmentsUpdateView.as_view(), name="shipments_update"),
    path("send_to_user/<id>", views.ShipmentsSendViewSet.as_view() , name="shipments_send"),
    path("delivery_to_user/<id>", views.ShipmentsDeliveryViewSet.as_view() , name="shipments_delivery")
]

