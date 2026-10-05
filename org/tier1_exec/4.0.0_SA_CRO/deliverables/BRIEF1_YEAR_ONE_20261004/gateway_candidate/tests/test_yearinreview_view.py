"""Year in review (/yearinreview) -- machine-checkable ACs for app/yearinreview_view.py.

Runnable standalone (`python tests/test_yearinreview_view.py`) or under pytest. Each AC carries both arms. The
identity wall itself is the ALB + identity.py (exercised live through the ALB), as for /sprint; here the handler is
driven with a stubbed identity to prove the 401 arm, the page arm, the trailing-slash redirect and the path
predicate GuardMiddleware keys on.
"""
from __future__ import annotations

import asyncio
import os
import sys

_GW_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _GW_ROOT not in sys.path:
    sys.path.insert(0, _GW_ROOT)

os.environ.setdefault("MOCK_GRAPH", "1")

from starlette.requests import Request          # noqa: E402

from app import yearinreview_view as yv         # noqa: E402


def _req(path: str = "/yearinreview", query: str = "") -> Request:
    scope = {"type": "http", "method": "GET", "path": path, "raw_path": path.encode(), "headers": [],
             "query_string": query.encode(), "server": ("test", 80), "scheme": "http", "root_path": ""}
    return Request(scope)


def test_path_predicate_both_arms() -> None:
    # AC1: exactly /yearinreview or a subpath -- never a loose prefix.
    assert yv.is_yearinreview_path("/yearinreview")
    assert yv.is_yearinreview_path("/yearinreview/")
    for bad in ("/yearinreviewx", "/year", "/sprint", "/", "/YearInReview"):
        assert not yv.is_yearinreview_path(bad), bad


def test_bundled_page_present_and_capped() -> None:
    # AC2: the release carries the page, under the cap, ASCII-only, with the page's own title.
    raw = yv.PAGE_FILE.read_bytes()
    assert 10_000 < len(raw) <= yv.MAX_BYTES
    assert all(b < 128 for b in raw)
    assert b"<title>Opal Year One Review</title>" in raw


def test_no_identity_is_401() -> None:
    # AC3: no verified email -> 401, never the page.
    yv._viewer = lambda request: ""            # type: ignore[assignment]
    resp = asyncio.run(yv.yearinreview_page(_req()))
    assert resp.status_code == 401


def test_identity_serves_page_with_frame_policy() -> None:
    # AC4: a verified viewer gets the page, no-store, framed only by self and Teams/Office hosts.
    yv._viewer = lambda request: "viewer@opalinvest.com"   # type: ignore[assignment]
    yv.audit.log_call = lambda *a, **k: None                # type: ignore[assignment]
    resp = asyncio.run(yv.yearinreview_page(_req()))
    assert resp.status_code == 200
    assert b"Opal Year One Review" in resp.body
    assert resp.headers["cache-control"] == "private, no-store"
    assert "frame-ancestors 'self' https://teams.microsoft.com" in resp.headers["content-security-policy"]


def test_trailing_slash_redirects() -> None:
    # AC5: /yearinreview/ -> 307 /yearinreview, query string kept; no query -> no '?'.
    r1 = asyncio.run(yv.yearinreview_redirect(_req("/yearinreview/", "v=mobile")))
    assert r1.status_code == 307 and r1.headers["location"] == "/yearinreview?v=mobile"
    r2 = asyncio.run(yv.yearinreview_redirect(_req("/yearinreview/")))
    assert r2.headers["location"] == "/yearinreview"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("PASS", name)
