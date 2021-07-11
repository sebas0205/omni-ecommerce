from django.urls import path

from payments import views

app_name = "payments"

urlpatterns = [
    path("", views.PaymentsListViewSet.as_view(), name="payments"),
    path("<id>", views.PaymentsRetrieveOrDestroyViewSet.as_view(), name="Payments_get_delete"),
    path("create/", views.PaymentsCreateViewSet.as_view(), name="Payments_create"),
    path("update/<id>" , views.PaymentsUpdateView.as_view(), name="Payments_update")
]

