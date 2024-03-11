from django.shortcuts import render, HttpResponseRedirect
from products.models import Category, Product, Basket


def index(request):
    return render(request, "products/index.html")


def products(request):
    context = {"products": Product.objects.all(), "categories": Category.objects.all()}
    return render(request, "products/products.html", context)


def basket_add(request, product_id):
    product_add = Product.objects.get(id=product_id)
    basket_user = Basket.objects.filter(user=request.user, product=product_add)
    if not basket_user.exists():
        Basket.objects.create(user=request.user, product=product_add, quantity=1)
    else:
        product_basket = Basket.objects.get(user=request.user, product=product_add)
        product_basket.quantity += 1
        product_basket.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def basket_delete(request, basket_id):
    product_delete = Basket.objects.get(user=request.user, id=basket_id)
    product_delete.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
