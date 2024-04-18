from typing import Generator
from fastapi.testclient import TestClient
from pytest import fixture


from app.main import app


@fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client
