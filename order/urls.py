from django.urls import path

from order import views

app_name = "ordenes"

urlpatterns = [
    path("user/<user_id>", views.OrdersByUserViewSet.as_view(), name="orders_by_user"),
    path("", views.OrdersListViewSet.as_view(), name="orders"),
    path("<id>", views.OrdersRetrieveOrDestroyViewSet.as_view(), name="Orders_get_delete"),
    path("create/", views.OrdersCreateViewSet.as_view(), name="Orders_create"),
    path("update/<id>", views.OrdersUpdateView.as_view(), name="Orders_update")
]