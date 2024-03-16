from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiratoin = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username}, {self.user.email}"

    def send_verification_email(self):
        link = reverse("users:EmailVerification", args=(self.user.email, self.code))
        all_url_link = f"http://127.0.0.1:8000/{link}"
        send_mail(
            subject="Verification email",
            message=all_url_link,
            from_email="from revillnik@mail.ru",
            recipient_list=[self.user.email],
        )
