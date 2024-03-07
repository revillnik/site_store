from django.contrib import admin
from django.urls import path, include
from products.views import index, products
from django.conf.urls.static import static
from django.conf import settings

app_name = "products"

urlpatterns = [
    path("", products, name="index"),
]
