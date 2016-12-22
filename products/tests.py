from django.test import TestCase
from products.models import Product
from django.utils import timezone
from django.core.urlresolvers import reverse


# Create your tests here.
class WhateverTest(TestCase):

    def create_Product(self, name="only a test", description="yes, this is only a test",price="only a test"):
        return Product.objects.create(name=name, description=description,price=price, created_at=timezone.now())

    # def test_whatever_creation(self):
    #     w = self.create_whatever()
    #     self.assertTrue(isinstance(w, Whatever))
    #     self.assertEqual(w.__unicode__(), w.title)