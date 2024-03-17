from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (EmailVerificationView, ProfileView, RegisterView,
                         UserLoginView)

app_name = "users"

urlpatterns = [
    path("login", UserLoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("profile/<int:pk>", login_required(ProfileView.as_view()), name="profile"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("EmailVerification/<str:email>/<uuid:code>/", EmailVerificationView.as_view(), name="EmailVerification"),
]
