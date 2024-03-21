from django.test import TestCase
from django.urls import reverse
from users.models import User, EmailVerification
from django.utils.timezone import now
from datetime import timedelta


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            "username": "Nik",
            "first_name": "Никита",
            "last_name": "Иванов",
            "email": "nik@mail.ru",
            "password1": "D2215779638d",
            "password2": "D2215779638d",
        }
        self.path = reverse("users:register")

    def test_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data["title"], "Registration")
        self.assertTemplateUsed(response, "users/register.html")

    def test_post(self):
        username = self.data["username"]
        self.assertFalse(User.objects.filter(username=username))
        response = self.client.post(self.path, self.data)
        # check creation user
        self.assertTrue(User.objects.filter(username=username))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("users:login"), fetch_redirect_response=False
        )
        # check creation send_mail
        send_email = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(send_email.exists())
        self.assertEqual(
            send_email.first().expiratoin.date(), (now() + timedelta(hours=48)).date()
        )

    def test_post_errors(self):
        username = self.data["username"]
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Пользователь с таким именем уже существует.", html=True)
