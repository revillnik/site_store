from django.shortcuts import render, redirect
from users.forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {"form": form}
    return render(request, "users/login.html", context)


def register(request):
    return render(request, "users/register.html")
