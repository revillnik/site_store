from django.contrib import admin
from users.models import User, EmailVerification
from products.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
    ]
    inlines = (BasketAdmin,)

@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ["user", "code",]
    fields = [
        "user",
        "created",
        "code",
        "expiratoin",
    ]
    readonly_fields = [
        "created",
    ]
