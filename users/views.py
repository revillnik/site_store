from django.shortcuts import render, redirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from products.models import Basket
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from users.models import User

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse("index"))
    else:
        form = UserLoginForm()
    context = {"form": form}
    return render(request, "users/login.html", context)

class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registration"
        return context


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

class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Profile"
        context["basket"] = Basket.objects.filter(user=self.request.user)
        return context
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


def logout(request):
    auth.logout(request)
    return redirect(reverse("index"))
