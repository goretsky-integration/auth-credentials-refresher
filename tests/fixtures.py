import httpx
import pytest

from dodo_is_auth import DodoISAuthService


@pytest.fixture
def http_client():
    with httpx.Client(base_url='http://localhost:8000') as http_client:
        yield http_client


@pytest.fixture
def dodo_is_auth(http_client):
    return DodoISAuthService(http_client)
