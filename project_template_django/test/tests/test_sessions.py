import pytest

from django.conf import settings
from django.core.cache import caches
from django.http import HttpResponse
from django.urls import reverse, path

from config.urls.routes import urlpatterns
from core.cypher.tokens import urlsafe_token


if hasattr(settings, "DJANGO_RUNS_IN_TESTMODE"):
    """
    EXAMPLE view using session store below
    """
    from django.views.generic import View

    class TestSession(View):
        def dispatch(self, request, *args, **kwargs):
            self.request.session.set_expiry(60 * 60 * 24)  # 1 day
            _id = self.request.session.get("id")
            # render history elements to the template
            if _id is None:
                _id = urlsafe_token(nbytes=25)
                self.request.session["id"] = _id
            return super().dispatch(request, *args, **kwargs)

        def get(self, request, **kwargs):
            return HttpResponse("<html></html>", status=200)

    class TestRecreateId(View):
        def post(self, request, *args, **kwargs):
            request.session["id"] = urlsafe_token(nbytes=25)
            return HttpResponse("OK", status=200)

    urlpatterns += [
        path("test/session/", TestSession.as_view(), name="test-session"),
        path("test/session-new-id/", TestRecreateId.as_view(), name="test-session-new-id"),
    ]


@pytest.mark.django_db
def test_session_cache(client):
    """
    Test if the session cache works as expected.
    """
    cache = caches[settings.SESSION_CACHE_ALIAS]
    r = client.get(reverse("test-session"))
    assert r.status_code == 200

    session_id = r.cookies.get("sessionid").value
    assert session_id is not None
    cache_key = f"django.contrib.sessions.cache{session_id}"
    cached = cache.get(cache_key)
    assert cached.get("id") is not None


@pytest.mark.django_db
def test_session_id_changes_on_post(client):
    cache = caches[settings.SESSION_CACHE_ALIAS]
    r = client.get(reverse("test-session"))
    assert r.status_code == 200
    session_id = r.cookies.get("sessionid").value
    cache_key = f"django.contrib.sessions.cache{session_id}"
    cached = cache.get(cache_key)
    current_id = cached.get("id")

    r = client.get(reverse("test-session"))
    assert r.status_code == 200
    session_id = r.cookies.get("sessionid").value
    cache_key = f"django.contrib.sessions.cache{session_id}"
    cached = cache.get(cache_key)
    next_id = cached.get("id")
    assert current_id == next_id, "The id should not have changed yet."

    r = client.post(reverse("test-session-new-id"))
    assert r.status_code == 200
    r = client.get(reverse("test-session"))
    assert r.status_code == 200
    session_id = r.cookies.get("sessionid").value
    cache_key = f"django.contrib.sessions.cache{session_id}"
    cached = cache.get(cache_key)
    changed_id = cached.get("id")
    assert current_id != changed_id, "The id should have changed."
    assert next_id != changed_id, "The id should have changed."
