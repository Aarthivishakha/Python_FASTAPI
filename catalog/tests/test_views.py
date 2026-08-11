from unittest import TestCase
from fastapi.testclient import TestClient
from catalog.main import app


class ViewTests(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_product_list(self):
        response = self.client.get("/catalog/products/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["products"]), 3)

    def test_product_export_csv(self):
        response = self.client.get("/catalog/products/export/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Laptop", response.text)

    def test_quote(self):
        response = self.client.get("/catalog/quote/?quantity=2&unit_price_cents=500&is_member=true")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["total_cents"], 900)
