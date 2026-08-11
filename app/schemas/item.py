from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    price: float = Field(ge=0)
    active: bool = True


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    price: Optional[float] = Field(default=None, ge=0)
    active: Optional[bool] = None


class Item(ItemCreate):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
