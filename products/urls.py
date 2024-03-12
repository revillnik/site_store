from django.urls import path, include
from products.views import index, products, basket_add, basket_delete

app_name = "products"

urlpatterns = [
    path("", products, name="index"),
    path("category/<int:category_id>", products, name="category"),
    path("paginator/<int:page_number>", products, name="paginator"),
    path("basket_add/<int:product_id>", basket_add, name="basket_add"),
    path("basket_delete/<int:basket_id>", basket_delete, name="basket_delete"),
]
