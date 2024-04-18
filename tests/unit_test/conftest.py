import pytest
from typing import Any, Callable, Generator
from app.database import Base, Database
from fastapi.testclient import TestClient
from pytest import fixture

from contextlib import AbstractContextManager
from sqlalchemy.orm import Session

from app.main import app


SQLALCHEMY_DATABASE_URL = "sqlite://"


@pytest.fixture
def db_session_factory() -> (
    Generator[Callable[..., AbstractContextManager[Session]], None, None]
):
    db = Database(SQLALCHEMY_DATABASE_URL)
    db.create_database()
    yield db.session

    db.close()


@fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client
