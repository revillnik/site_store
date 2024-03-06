from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2)
    quantity = models.PositiveIntegerField(defailt=0)
    image = models.ImageField(upload_to="products_images")
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    