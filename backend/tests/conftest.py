import pytest

from app import create_app
from app.core.extensions import db


class TestConfig:
    TESTING = True
    SECRET_KEY = "bhargava-test-secret-key-1234"
    JWT_SECRET_KEY = "bhargava-test-jwt-secret-key-1234"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_ORIGINS = ["http://localhost:5173", "http://127.0.0.1:5173"]


@pytest.fixture()
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def _login(client, email, password, role):
    resp = client.post(
        "/api/auth/login",
        json={"email": email, "password": password, "role": role},
    )
    assert resp.status_code == 200
    return resp.get_json()["data"]["token"]


@pytest.fixture()
def admin_token(client):
    return _login(client, "admin@socioneed.com", "123456", "admin")


@pytest.fixture()
def resident_token(client):
    return _login(client, "resident@socioneed.com", "123456", "owner")


@pytest.fixture()
def provider_token(client):
    return _login(client, "provider@socioneed.com", "123456", "service_provider")


@pytest.fixture()
def security_token(client):
    return _login(client, "security@socioneed.com", "123456", "security")
