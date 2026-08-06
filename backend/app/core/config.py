import os
from datetime import timedelta


def _build_cors_origins():
    configured = [
        origin.strip()
        for origin in os.getenv("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",")
        if origin.strip()
    ]
    local_dev_defaults = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ]

    deduped = []
    for origin in [*configured, *local_dev_defaults]:
        if origin not in deduped:
            deduped.append(origin)
    return deduped


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "bhargava-secret-key-1234-socioneed-main")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///../instance/socioneed.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "bhargava-jwt-secret-key-1234-socioneed")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)
    CORS_ORIGINS = _build_cors_origins()
