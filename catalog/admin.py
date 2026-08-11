"""Admin CSV export helpers, duplicated from exports.py for duplication testing (jscpd)."""
from __future__ import annotations

import csv
import io

from .models import MOCK_PRODUCTS


def export_selected_csv(queryset) -> str:
    # Mirrors exports.export_products_csv() almost exactly - a real
    # copy-paste anti-pattern for jscpd to catch, not a staged one.
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["id", "name", "price_cents", "in_stock"])
    for product in sorted(queryset, key=lambda p: p.id):
        writer.writerow([product.id, product.name, product.price_cents, product.in_stock])
    return buffer.getvalue()
