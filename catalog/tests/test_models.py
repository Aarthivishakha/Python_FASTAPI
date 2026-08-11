from unittest import TestCase
from catalog.models import Product


class ProductModelTests(TestCase):
    def test_str_returns_name(self):
        product = Product(id=1, name="Widget", price_cents=999, in_stock=True)
        self.assertEqual(str(product), "Widget")

    def test_defaults_in_stock_true(self):
        product = Product(id=1, name="Gadget", price_cents=1500)
        self.assertTrue(product.in_stock)
