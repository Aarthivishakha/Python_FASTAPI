from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    name: str
    price_cents: int
    in_stock: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

    def __str__(self) -> str:
        return self.name


# Mock database of products
MOCK_PRODUCTS: list[Product] = [
    Product(id=1, name="Laptop", price_cents=99900, in_stock=True),
    Product(id=2, name="Mouse", price_cents=2500, in_stock=True),
    Product(id=3, name="Keyboard", price_cents=7500, in_stock=False),
]
