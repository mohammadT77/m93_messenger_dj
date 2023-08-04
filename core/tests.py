from django.test import TestCase
from .models import User, Product

# Create your tests here.
class MyTest(TestCase):

    def test1(self):
        p1 = Product.objects.create(name="p1")
        p2 = Product.objects.create(name="p2")

        print("all before:", Product.objects.all())
        Product.objects.all().delete()
        print("p2.is_deleted:", p2.is_deleted)
        print("Archive:", Product.objects.archive())
        print("All:", Product.objects.all())