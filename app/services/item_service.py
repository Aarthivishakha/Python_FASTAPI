from datetime import datetime, timezone
from threading import RLock
from uuid import UUID, uuid4

from app.exceptions import ItemNotFoundError
from app.schemas.item import Item, ItemCreate, ItemUpdate


class ItemService:
    """Thread-safe in-memory store; replace behind this interface for persistence."""

    def __init__(self) -> None:
        self._items: dict[UUID, Item] = {}
        self._lock = RLock()

    def reset(self) -> None:
        with self._lock:
            self._items.clear()

    def list(self, offset: int = 0, limit: int = 100) -> list[Item]:
        with self._lock:
            return list(self._items.values())[offset : offset + limit]

    def get(self, item_id: UUID) -> Item:
        with self._lock:
            try:
                return self._items[item_id]
            except KeyError as exc:
                raise ItemNotFoundError(f"Item {item_id} was not found") from exc

    def create(self, data: ItemCreate) -> Item:
        now = datetime.now(timezone.utc)
        item = Item(id=uuid4(), created_at=now, updated_at=now, **data.model_dump())
        with self._lock:
            self._items[item.id] = item
        return item

    def update(self, item_id: UUID, data: ItemUpdate) -> Item:
        current = self.get(item_id)
        changes = data.model_dump(exclude_unset=True)
        updated = current.model_copy(update={**changes, "updated_at": datetime.now(timezone.utc)})
        with self._lock:
            self._items[item_id] = updated
        return updated

    def delete(self, item_id: UUID) -> None:
        self.get(item_id)
        with self._lock:
            del self._items[item_id]


item_service = ItemService()
