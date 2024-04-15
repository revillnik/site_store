from rest_framework import serializers

from products.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "quantity", "image", "category"]
