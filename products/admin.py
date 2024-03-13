from django.contrib import admin
from products.models import Category, Product, Basket


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
    list_display_links = ["id", "name"]
    fields = ["id", "name", "description"]
    readonly_fields = [
        "id",
    ]
    ordering = [
        "name",
    ]
    search_fields = [
        "name",
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category", "price", "quantity"]
    list_display_links = ["id", "name"]
    fields = ["id", "name", "description", "category", "price", "quantity", "image"]
    readonly_fields = [
        "id",
    ]
    ordering = ["name", "category"]
    search_fields = ["name", "category"]


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = [
        "product",
        "quantity",
        "time_stamp",
    ]
    readonly_fields = [
        "time_stamp",
    ]
    extra = 1
