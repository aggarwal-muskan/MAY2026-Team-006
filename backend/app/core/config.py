import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "bhargava-secret-key-1234-socioneed-main")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///../instance/socioneed.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "bhargava-jwt-secret-key-1234-socioneed")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)
    CORS_ORIGINS = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",") if origin.strip()]
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-latest")
    # AI latency tuning (all optional; sensible defaults applied in gemini_service).
    # AI_CACHE_TTL: seconds to cache identical AI responses (0 disables caching).
    AI_CACHE_TTL = int(os.getenv("AI_CACHE_TTL", "300"))
    # AI_MAX_OUTPUT_TOKENS: cap on generated tokens (smaller = faster).
    AI_MAX_OUTPUT_TOKENS = int(os.getenv("AI_MAX_OUTPUT_TOKENS", "2048"))
