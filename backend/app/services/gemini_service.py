"""Thin wrapper around the Gemini API, tuned for low latency.

Latency optimizations applied here benefit every AI feature, since they all
route through generate_text / generate_json:

1. Client reuse   - the genai.Client is created once per API key and cached,
                    instead of rebuilt on every request.
2. Generation cfg - JSON responses use response_mime_type="application/json"
                    (smaller, well-formed output = faster + no repair parsing),
                    a bounded max_output_tokens, and low temperature.
3. Thinking off   - for gemini-2.5-* models, the "thinking" budget is set to 0,
                    which removes a large chunk of response latency.
4. Response cache - identical (model, system, prompt) calls are served from a
                    short-lived in-memory cache, so repeated clicks / refreshes
                    return instantly instead of re-calling the model.
"""

import hashlib
import json
import re
import time
from typing import Any

from flask import current_app
from google import genai
from google.genai import types


class GeminiServiceError(Exception):
    """Raised when Gemini cannot produce a usable response."""


# --- defaults (overridable via app config) ----------------------------------
_DEFAULT_MAX_TOKENS = 2048
_DEFAULT_TEMPERATURE = 0.3
_DEFAULT_CACHE_TTL = 300  # seconds; 0 disables caching
_MAX_CACHE_ENTRIES = 256

# --- module-level caches ----------------------------------------------------
_CLIENT_CACHE: dict[str, "genai.Client"] = {}
_RESPONSE_CACHE: dict[str, tuple[float, str]] = {}


def _client() -> "genai.Client":
    api_key = (current_app.config.get("GEMINI_API_KEY") or "").strip()
    if not api_key:
        raise GeminiServiceError(
            "GEMINI_API_KEY is missing. Add it to backend/.env and restart the server."
        )
    client = _CLIENT_CACHE.get(api_key)
    if client is None:
        client = genai.Client(api_key=api_key)
        _CLIENT_CACHE[api_key] = client
    return client


def _model_name() -> str:
    return current_app.config.get("GEMINI_MODEL") or "gemini-flash-latest"


def _cache_ttl() -> int:
    value = current_app.config.get("AI_CACHE_TTL")
    return int(value) if value is not None else _DEFAULT_CACHE_TTL


def _max_tokens() -> int:
    value = current_app.config.get("AI_MAX_OUTPUT_TOKENS")
    return int(value) if value is not None else _DEFAULT_MAX_TOKENS


def _build_config(as_json: bool, model: str) -> "types.GenerateContentConfig":
    kwargs: dict[str, Any] = {
        "temperature": _DEFAULT_TEMPERATURE,
        "max_output_tokens": _max_tokens(),
    }
    if as_json:
        # Ask the model for strict JSON: smaller output and no fenced-code repair.
        kwargs["response_mime_type"] = "application/json"
    if "2.5" in model:
        # 2.5 models "think" by default, which adds latency. Turn it off.
        kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=0)
    return types.GenerateContentConfig(**kwargs)


def _cache_get(key: str) -> str | None:
    entry = _RESPONSE_CACHE.get(key)
    if not entry:
        return None
    expires_at, value = entry
    if expires_at < time.time():
        _RESPONSE_CACHE.pop(key, None)
        return None
    return value


def _cache_put(key: str, value: str, ttl: int) -> None:
    if ttl <= 0:
        return
    if len(_RESPONSE_CACHE) >= _MAX_CACHE_ENTRIES:
        # Drop the oldest entry to bound memory.
        oldest = min(_RESPONSE_CACHE, key=lambda k: _RESPONSE_CACHE[k][0])
        _RESPONSE_CACHE.pop(oldest, None)
    _RESPONSE_CACHE[key] = (time.time() + ttl, value)


def generate_text(
    prompt: str,
    *,
    system: str | None = None,
    as_json: bool = False,
    use_cache: bool = True,
) -> str:
    model = _model_name()
    contents = f"{system.strip()}\n\n{prompt.strip()}" if system else prompt

    cache_key = None
    ttl = _cache_ttl()
    if use_cache and ttl > 0:
        raw_key = f"{model}|{as_json}|{contents}"
        cache_key = hashlib.sha256(raw_key.encode("utf-8")).hexdigest()
        cached = _cache_get(cache_key)
        if cached is not None:
            return cached

    try:
        response = _client().models.generate_content(
            model=model,
            contents=contents,
            config=_build_config(as_json, model),
        )
    except Exception as error:  # noqa: BLE001 - surface provider errors cleanly
        raise GeminiServiceError(str(error)) from error

    text = getattr(response, "text", None)
    if not text:
        raise GeminiServiceError("Gemini returned an empty response.")
    text = text.strip()

    if cache_key is not None:
        _cache_put(cache_key, text, ttl)
    return text


def generate_json(
    prompt: str,
    *,
    system: str | None = None,
    use_cache: bool = True,
) -> dict[str, Any]:
    text = generate_text(prompt, system=system, as_json=True, use_cache=use_cache)
    return parse_json_object(text)


def parse_json_object(text: str) -> dict[str, Any]:
    cleaned = text.strip()
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", cleaned, flags=re.IGNORECASE)
    if fence:
        cleaned = fence.group(1).strip()

    try:
        data = json.loads(cleaned)
        if isinstance(data, dict):
            return data
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{[\s\S]*\}", cleaned)
    if match:
        data = json.loads(match.group(0))
        if isinstance(data, dict):
            return data

    raise GeminiServiceError("Gemini did not return valid JSON.")


def clear_response_cache() -> None:
    """Clear the in-memory AI response cache (useful in tests/admin tooling)."""
    _RESPONSE_CACHE.clear()
