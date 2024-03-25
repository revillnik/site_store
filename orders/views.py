from django.shortcuts import render
from common.views import TitleMixin
from django.views.generic import CreateView
from orders.forms import OrderCreateForm
from django.urls import reverse_lazy
from common.views import TitleMixin


class OrderCreate(TitleMixin, CreateView):
    template_name = "orders/order-create.html"
    form_class = OrderCreateForm
    success_url = reverse_lazy("orders:order_create")
    title = 'order_create'
    def form_valid(self, form):
       form.instance.initiator = self.request.user
       return super(OrderCreate, self).form_valid(form)
	 
