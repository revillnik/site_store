from django.urls import path, include
from products.views import PorductsListView, basket_add, basket_delete, IndexView

app_name = "products"

urlpatterns = [
    path("", PorductsListView.as_view(), name="index"),
    path("category/<int:category_id>", PorductsListView.as_view(), name="category"),
    path("basket_add/<int:product_id>", basket_add, name="basket_add"),
    path("basket_delete/<int:basket_id>", basket_delete, name="basket_delete"),
]
