from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
       return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products_images")
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    def __str__(self):
       return self.name
    