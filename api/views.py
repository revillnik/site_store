from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from products.models import Product, Basket
from products.serializers import ProductSerializer, BasketSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ["create", "destroy", "update"]:
            self.permission_classes = (IsAdminUser,)
        return super(ProductModelViewSet, self).get_permissions()


class BasketModelViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated, ]
    
    def get_queryset(self):
       queryset = super().get_queryset()
       return queryset.filter(user=self.request.user)
