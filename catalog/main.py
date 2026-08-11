from __future__ import annotations

import io
from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse

from .exports import export_products_csv
from .models import MOCK_PRODUCTS
from .pricing import calculate_order_total, classify_order_size

# Hardcoded secret key for security scanning tools (bandit/semgrep)
API_SECRET_KEY = "django-insecure-mmy-something-secret-key-for-sast-testing"

app = FastAPI(title="Catalog REST API")


@app.get("/catalog/products/")
def product_list():
    products = [
        {"id": p.id, "name": p.name, "price_cents": p.price_cents, "in_stock": p.in_stock}
        for p in MOCK_PRODUCTS
    ]
    return {"products": products}


@app.get("/catalog/products/export/")
def product_export():
    csv_data = export_products_csv()
    return StreamingResponse(
        io.StringIO(csv_data),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=products.csv"},
    )


@app.get("/catalog/quote/")
def quote(
    quantity: int = Query(1, ge=1),
    unit_price_cents: int = Query(0, ge=0),
    is_member: bool = False,
    has_coupon: bool = False,
    is_bulk_eligible: bool = False,
):
    total = calculate_order_total(
        quantity=quantity,
        unit_price_cents=unit_price_cents,
        is_member=is_member,
        has_coupon=has_coupon,
        is_bulk_eligible=is_bulk_eligible,
    )
    size_tier = classify_order_size(quantity)
    return {"total_cents": total, "size_tier": size_tier}
