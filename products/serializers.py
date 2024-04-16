from rest_framework import serializers
from rest_framework import fields
from products.models import Product, Category, Basket

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "quantity", "image", "category"]

class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    sum = fields.FloatField()
    total_sum = fields.SerializerMethodField()
    total_quantity = fields.SerializerMethodField()

    class Meta:
        model = Basket
        fields = [
            "id",
            "product",
            "quantity",
            "sum",
            "time_stamp",
            "total_sum",
            "total_quantity",
        ]
        read_only_fields = ["time_stamp", ]

    def get_total_sum(self, obj):
        return Basket.objects.filter(user=obj.user.id).total_sum()

    def get_total_quantity(self, obj):
        return Basket.objects.filter(user=obj.user.id).total_quantity()
