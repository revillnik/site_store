from django.shortcuts import render
from common.views import TitleMixin
from django.views.generic import  CreateView

class OrderCreate(CreateView):
   template_name = "orders/order-create.html"
