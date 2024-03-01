import pytest

from django.conf import settings
from django.core.cache import caches

from django.urls import reverse


@pytest.mark.django_db
def test_session_cache(client):
    """
    Test if the session cache works as expected.
    """
    cache = caches[settings.SESSION_CACHE_ALIAS]
    r = client.get(reverse("tests:test-session"))
    assert r.status_code == 200

    session_id = r.cookies.get("sessionid").value
    assert session_id is not None
    cache_key = f"django.contrib.sessions.cache{session_id}"
    cached = cache.get(cache_key)
    assert cached.get("id") is not None


@pytest.mark.django_db
def test_session_id_changes_on_post(client):
    cache = caches[settings.SESSION_CACHE_ALIAS]
    r = client.get(reverse("tests:test-session"))
    assert r.status_code == 200
    session_id = r.cookies.get("sessionid").value
    cache_key = f"django.contrib.sessions.cache{session_id}"
    cached = cache.get(cache_key)
    current_id = cached.get("id")

    r = client.get(reverse("tests:test-session"))
    assert r.status_code == 200
    session_id = r.cookies.get("sessionid").value
    cache_key = f"django.contrib.sessions.cache{session_id}"
    cached = cache.get(cache_key)
    next_id = cached.get("id")
    assert current_id == next_id, "The id should not have changed yet."

    r = client.post(reverse("tests:test-session-new-id"))
    assert r.status_code == 200
    r = client.get(reverse("tests:test-session"))
    assert r.status_code == 200
    session_id = r.cookies.get("sessionid").value
    cache_key = f"django.contrib.sessions.cache{session_id}"
    cached = cache.get(cache_key)
    changed_id = cached.get("id")
    assert current_id != changed_id, "The id should have changed."
    assert next_id != changed_id, "The id should have changed."
