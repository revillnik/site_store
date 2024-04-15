from django.contrib import admin
from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):	
    list_display = ["__str__", "id"]
    fields = [
        "id",
        ("created", "status"),
        ("first_name", "last_name"),
        "email",
        "adress",
        "basket_history",
        "initiator",
    ]
    readonly_fields = ["id", "created"]
