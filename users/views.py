from django.contrib.auth.views import LoginView
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User


class UserLoginView(TitleMixin, LoginView):
    model = User
    form_class = UserLoginForm
    template_name = "users/login.html"
    title = "Login"


# def login(request):
#     if request.method == "POST":
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST["username"]
#             password = request.POST["password"]
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return redirect(reverse("index"))
#     else:
#         form = UserLoginForm()
#     context = {"form": form}
#     return render(request, "users/login.html", context)


class RegisterView(TitleMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")
    title = "Registration"


# def register(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Вы успешно зарегистрировались!")
#             return redirect(reverse("users:login"))
#     else:
#         form = UserRegistrationForm()
#     context = {"form": form}
#     return render(request, "users/register.html", context)


class ProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile.html"
    title = "Profile"

    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.request.user.id,))


# @login_required
# def profile(request):
#     if request.method == "POST":
#         form = UserProfileForm(
#             instance=request.user, data=request.POST, files=request.FILES
#         )
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("users:profile"))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)
#     context = {
#         "title": "Store - профиль",
#         "form": form,
#         "basket": Basket.objects.filter(user=request.user),
#     }
#     return render(request, "users/profile.html", context)


# def logout(request):
#     auth.logout(request)
#     return redirect(reverse("index"))


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = "users/email_verification.html"
    title = "email verification"

    def get(self, request, *args, **kwargs):
        code = self.kwargs["code"]
        user = User.objects.get(email=self.kwargs["email"])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists():
            user.is_verified_email = True
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return redirect(reverse("index"))
