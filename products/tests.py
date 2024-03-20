from django.test import TestCase
from django.urls import reverse
from products.models import Product, Category, Basket
from users.models import User

class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse("index")
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data["title"], "Store")
        self.assertTemplateUsed(response, "products/index.html")


class PorductsListViewTestCase(TestCase):
    fixtures = ["categories.json", "goods.json"]

    def setUp(self):
        self.products = Product.objects.all()

    def test_all_products_list(self):
        path = reverse("products:index")
        response = self.client.get(path)
        self.__common_test(response)
        self.assertEqual(
            list(response.context_data["object_list"]), list(self.products[:3])
        )

    def test_products_category_list(self):
        category = Category.objects.first()
        path = reverse("products:category", kwargs={"category_id": category.id})
        response = self.client.get(path)
        self.__common_test(response)
        self.assertEqual(
            list(response.context_data["object_list"]),
            list(self.products.filter(category=category)[:3]),
        )

    def __common_test(self, response):
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data["title"], "Products")
        self.assertTemplateUsed(response, "products/products.html")


class basket_delete_TestCase(TestCase):
    fixtures = ["categories.json", "goods.json", "Basket.json", "Users.json"]

    def test_basket_delete(self):
        basket = Basket.objects.first()
        user = basket.user
        product_delete = Basket.objects.get(user=user, id=basket.id)
        product_delete.delete()
        try:
            Basket.objects.get(user=user, id=basket.id)
            product_delete = False
        except:
            product_delete = True
        self.assertEqual(product_delete, True)

class basket_add_TestCase(TestCase):
    fixtures = ["categories.json", "goods.json", "Basket.json", "Users.json"]

    def test_basket_add(self):
        product_add1 = Basket.objects.first().product
        user = User.objects.filter(username=Basket.objects.first().user.username).first()
        product_add2 = Product.objects.exclude(name__in=Basket.objects.values("product__name")).first()
        Basket.objects.create(user_id=user.id, product=product_add2, quantity=1)
        self.assertEqual(Basket.objects.get(user=user, product=product_add2).product, product_add2)
        product_basket = Basket.objects.get(user=user, product=product_add1)
        product_basket.quantity += 1
        product_basket.save()
        self.assertEqual(Basket.objects.get(user=user, product=product_add1).product, product_add1)
        self.assertEqual(Basket.objects.get(user=user, product=product_add1).quantity != 1, True)
