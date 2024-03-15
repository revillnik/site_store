from django.urls import path, include
from users.views import login, RegisterView, ProfileView, logout


app_name = "users"

urlpatterns = [
    path("login", login, name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
    path("logout", logout, name="logout"),
]
