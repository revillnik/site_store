from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic import ListView, TemplateView

from common.views import TitleMixin
from products.models import Basket, Category, Product


class IndexView(TitleMixin, TemplateView):
    template_name = "products/index.html"
    title = "Store"


# def index(request):
# 	return render(request, "products/index.html")


class PorductsListView(TitleMixin, ListView):
    model = Product
    template_name = "products/products.html"
    paginate_by = 3
    title = "Products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #  работа с кешем при помощи redis (решил сделать через коммент, т.к. работаю на винде, запарно устанавливать редис)
        # categories = cache.get("categories")
        # if not categories:
        #    context["categories"] = Category.objects.filter( name__in=Product.objects.values("category__name"))
        #    categories = cache.set("categories", context["categories"], 30)
        # else:
        #    context["categories"] = categories
        context["categories"] = Category.objects.filter(
            name__in=Product.objects.values("category__name")
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get("category_id")
        return (
            Product.objects.filter(category_id=category_id) if category_id else queryset
        )


# def products(request, category_id=None, page_number=1):
#     products = (
#         Product.objects.filter(category__id=category_id)
#         if category_id
#         else Product.objects.all()
#     )
#     per_page = 3
#     paginator = Paginator(products, per_page)
#     products_paginator = paginator.page(page_number)
#     context = {
#         "products": products_paginator,
#         "categories": Category.objects.filter(
#             name__in=Product.objects.values("category__name")
#         ),
#     }
#     return render(request, "products/products.html", context)


@login_required
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


@login_required
def basket_delete(request, basket_id):
    product_delete = Basket.objects.get(user=request.user, id=basket_id)
    product_delete.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
