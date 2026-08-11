from uuid import UUID

from fastapi import APIRouter, Query, Response, status

from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.services.item_service import item_service

router = APIRouter()


@router.get("", response_model=list[Item])
def list_items(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
) -> list[Item]:
    return item_service.list(offset=offset, limit=limit)


@router.post("", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate) -> Item:
    return item_service.create(payload)


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: UUID) -> Item:
    return item_service.get(item_id)


@router.patch("/{item_id}", response_model=Item)
def update_item(item_id: UUID, payload: ItemUpdate) -> Item:
    return item_service.update(item_id, payload)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: UUID) -> Response:
    item_service.delete(item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
