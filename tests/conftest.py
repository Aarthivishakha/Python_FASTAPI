import pytest
from starlette.testclient import TestClient

from app.main import app
from app.services.item_service import item_service


@pytest.fixture
def client() -> TestClient:
    item_service.reset()
    with TestClient(app) as test_client:
        yield test_client
