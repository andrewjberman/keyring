"""/yearinreview -- the Year One Operating Review page (Brief #1, 4.0.0_SA_CRO~2026).

Andrew-direct 2026-10-04: "id publish it at mcp.opalinvest.dev/yearinreview". Record:
org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261004_194xZ_BRIEF1_WHERE_WEVE_BEEN_ONE_YEAR_SCALE_ONE_PAGER.md

A THIN viewer, modelled on sprint_view.py / rivalfunds_view.py, with one difference: the page is ONE static,
self-contained HTML file that ships INSIDE the release (app/static/yearinreview/index.html), so there is no S3 read,
no new IAM grant and no new storage address. A rebuilt page reaches viewers with the next gateway release.
Source of the page: org/tier1_exec/4.0.0_SA_CRO/deliverables/BRIEF1_YEAR_ONE_20261004/build_year_one.py.

Paths (behind the ALB's authenticate-oidc DEFAULT action; GuardMiddleware verifies identity exactly as for /sprint):
  GET /yearinreview     the page
  GET /yearinreview/    307 -> /yearinreview
Viewers: any signed-in account (the /sprint wall).
"""
from __future__ import annotations

import pathlib
from typing import Optional

from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse, RedirectResponse, Response

from . import audit

PAGE_FILE = pathlib.Path(__file__).resolve().parent / "static" / "yearinreview" / "index.html"
MAX_BYTES = 2 * 1024 * 1024          # the page is ~70 KB; 2 MB is a generous ceiling

# Same serving policy as /sprint: the page may be framed by Teams (website tab) and nothing else.
_HEADERS = {
    "Cache-Control": "private, no-store",
    "Content-Security-Policy": (
        "frame-ancestors 'self' https://teams.microsoft.com https://*.teams.microsoft.com "
        "https://*.cloud.microsoft https://*.office.com https://*.sharepoint.com"
    ),
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "no-referrer",
}

_page: Optional[str] = None


def is_yearinreview_path(path: str) -> bool:
    # Exactly /yearinreview or a /yearinreview/ subpath -- NOT a loose prefix (/yearinreviewx is not ours).
    return path == "/yearinreview" or path.startswith("/yearinreview/")


def load_page() -> str:
    """Read the bundled page once, capped; a missing or oversize file raises (the handler names it)."""
    global _page
    if _page is None:
        raw = PAGE_FILE.read_bytes()
        if len(raw) > MAX_BYTES:
            raise ValueError("yearinreview page over the size cap")
        _page = raw.decode("utf-8")
    return _page


def _viewer(request: Request) -> str:
    from .identity import IdentityError, get_user_email
    try:
        return get_user_email(request)
    except IdentityError:
        return ""


async def yearinreview_page(request: Request) -> Response:
    email = _viewer(request)
    if not email:
        return JSONResponse({"error": "identity required"}, status_code=401, headers=_HEADERS)
    try:
        body = load_page()
    except Exception as e:  # noqa: BLE001 -- name the class, never a bare 500
        audit.log_call(email, "yearinreview_view", {"verdict": "PAGE-ERROR"}, "error", type(e).__name__)
        return HTMLResponse("<h3>Year in review temporarily unavailable.</h3>", status_code=502, headers=_HEADERS)
    audit.log_call(email, "yearinreview_view", {}, "ok")
    return HTMLResponse(body, headers=_HEADERS)


async def yearinreview_redirect(request: Request) -> Response:
    """/yearinreview/ (trailing slash) -> /yearinreview, preserving the query string."""
    qs = request.url.query
    return RedirectResponse("/yearinreview" + (f"?{qs}" if qs else ""), status_code=307)
