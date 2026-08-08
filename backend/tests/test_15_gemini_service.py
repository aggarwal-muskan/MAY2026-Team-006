"""Unit tests for the Gemini service latency optimizations (client stubbed)."""

import pytest

import app.services.gemini_service as gs
from app.services.gemini_service import GeminiServiceError


class _FakeModels:
    def __init__(self, text='{"ok": true}'):
        self.calls = 0
        self.last_config = None
        self.last_model = None
        self._text = text

    def generate_content(self, model=None, contents=None, config=None):
        self.calls += 1
        self.last_config = config
        self.last_model = model
        return type("Resp", (), {"text": self._text})()


class _FakeClient:
    def __init__(self, text='{"ok": true}'):
        self.models = _FakeModels(text)


@pytest.fixture()
def fake_client(app, monkeypatch):
    """Stub the cached genai client so no network call happens."""
    client = _FakeClient()
    monkeypatch.setattr(gs, "_client", lambda: client)
    gs.clear_response_cache()
    return client


def test_generate_json_parses_and_uses_json_config(app, fake_client):
    with app.app_context():
        result = gs.generate_json("do something", system="sys")
    assert result == {"ok": True}
    # JSON mode should request strict JSON output for speed + reliability.
    assert fake_client.models.last_config.response_mime_type == "application/json"
    assert fake_client.models.last_config.max_output_tokens == 2048


def test_response_cache_avoids_second_call(app, fake_client):
    with app.app_context():
        gs.generate_json("same prompt", system="sys")
        gs.generate_json("same prompt", system="sys")
    # Second identical call is served from cache → underlying model hit once.
    assert fake_client.models.calls == 1


def test_cache_clear_forces_new_call(app, fake_client):
    with app.app_context():
        gs.generate_json("prompt A")
        gs.clear_response_cache()
        gs.generate_json("prompt A")
    assert fake_client.models.calls == 2


def test_thinking_disabled_for_2_5_models(app, fake_client):
    app.config["GEMINI_MODEL"] = "gemini-2.5-flash"
    with app.app_context():
        gs.generate_json("hello")
    cfg = fake_client.models.last_config
    assert cfg.thinking_config is not None
    assert cfg.thinking_config.thinking_budget == 0


def test_no_thinking_config_for_non_2_5_models(app, fake_client):
    app.config["GEMINI_MODEL"] = "gemini-2.0-flash"
    with app.app_context():
        gs.generate_json("hello")
    assert fake_client.models.last_config.thinking_config is None


def test_empty_response_raises(app, monkeypatch):
    client = _FakeClient(text="")
    monkeypatch.setattr(gs, "_client", lambda: client)
    gs.clear_response_cache()
    with app.app_context():
        with pytest.raises(GeminiServiceError):
            gs.generate_text("x", use_cache=False)


def test_missing_api_key_raises(app):
    app.config["GEMINI_API_KEY"] = ""
    # Bypass the stub so the real _client() key check runs.
    with app.app_context():
        with pytest.raises(GeminiServiceError):
            gs.generate_text("x", use_cache=False)
