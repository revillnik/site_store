from django.shortcuts import render
from products.models import Category, Product


def index(request):
    return render(request, "products/index.html")


def products(request):
    context = {"products": Product.objects.all(), "categories": Category.objects.all()}
    return render(request, "products/products.html", context)
