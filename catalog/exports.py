"""CSV export helpers used by the storefront's reporting views."""
from __future__ import annotations

import csv
import io

from .models import MOCK_PRODUCTS


def export_products_csv() -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["id", "name", "price_cents", "in_stock"])
    for product in sorted(MOCK_PRODUCTS, key=lambda p: p.id):
        writer.writerow([product.id, product.name, product.price_cents, product.in_stock])
    return buffer.getvalue()
