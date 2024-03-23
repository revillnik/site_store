from django.urls import path
from orders.views import OrderCreate


app_name = "orders"

urlpatterns = [
    path("order_create/", OrderCreate.as_view(), name="order_create"),
]
