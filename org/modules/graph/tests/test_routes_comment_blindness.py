"""Bundle item 2 -- the FALSE-PRESENCE resolver defect (DE @7a2805d4e).

comp-routes/comp-platinum resolved getAccountDistribution to a commented-out
/api/private TODO instead of the live /api/general call: the extractors scanned
RAW source and the dead call preceded the live one. Control = instrument
selection (dead code never reaches the resolver), NOT resolution-time liveness
(COO 220729Z: CVO III-c does not cover this class).
"""
from __future__ import annotations

import sys
from pathlib import Path

WS = Path(__file__).resolve().parents[4]
if str(WS) not in sys.path:
    sys.path.insert(0, str(WS))

from org.modules.graph.extract_ts_source import strip_comments  # noqa: E402
from org.modules.graph.extract_routes import _parse_frontend_endpoints  # noqa: E402


# ---------------------------------------------------------------- stripper unit
def test_line_comment_blanked():
    assert "dead" not in strip_comments("live()\n// dead()\n")


def test_block_comment_blanked():
    s = strip_comments("a /* dead1\n dead2 */ b")
    assert "dead1" not in s and "dead2" not in s
    assert "a" in s and "b" in s


def test_double_slash_inside_string_preserved():
    # The classic hazard: a naive line-strip truncates every absolute URL.
    src = 'const u = "https://example.com/x"; // real comment\n'
    out = strip_comments(src)
    assert '"https://example.com/x"' in out
    assert "real comment" not in out


def test_template_literal_preserved_and_offsets_stable():
    src = "const t = `//not-a-comment ${x}`\n// comment\nlive()"
    out = strip_comments(src)
    assert "`//not-a-comment ${x}`" in out
    assert "comment" not in out.replace("//not-a-comment", "")
    # Whitespace replacement keeps length + line structure identical.
    assert len(out) == len(src)
    assert out.count("\n") == src.count("\n")


def test_escaped_quote_does_not_end_string():
    src = 'const s = "a\\" // still-string"; // real\nx()'
    out = strip_comments(src)
    assert "still-string" in out
    assert "real" not in out


# ------------------------------------------------- the regression pin (live file)
def test_getAccountDistribution_resolves_to_live_general_url():
    """CTO's exact ask: a regression case pinning this endpoint. The live call is
    /api/general/...; the commented-out /api/private TODO must never win again."""
    endpoints = _parse_frontend_endpoints(WS)
    ep = endpoints.get("getAccountDistribution")
    assert ep is not None, "getAccountDistribution not parsed at all"
    assert ep.url_template == "/api/general/portfolios/account-distribution.json", \
        f"resolved to {ep.url_template!r} -- the false-presence defect is back"


# ------------------------------------------------------- negative control (synth)
def test_commented_only_call_yields_unresolved_not_phantom(tmp_path, monkeypatch):
    """A function whose ONLY apiRequest is commented out must parse as
    URL-unresolved (honest empty), never as the dead URL -- absence reported
    loud beats presence fabricated."""
    api_dir = tmp_path / "portal" / "src" / "api" / "endpoints"
    api_dir.mkdir(parents=True)
    (api_dir / "synth.ts").write_text(
        "export async function getSynthDead(): Promise<X> {\n"
        "  // const d = await apiRequest<X>('/api/private/dead.json')\n"
        "  return null as any\n"
        "}\n"
        "export async function getSynthLive(): Promise<X> {\n"
        "  /* old: await apiRequest<X>('/api/private/older.json') */\n"
        "  return await apiRequest<X>('/api/general/live.json')\n"
        "}\n",
        encoding="utf-8",
    )
    endpoints = _parse_frontend_endpoints(tmp_path)
    dead = endpoints.get("getSynthDead")
    live = endpoints.get("getSynthLive")
    assert dead is not None and dead.url_template == "", \
        f"dead-only function resolved to {dead.url_template!r} (false presence)"
    assert live is not None and live.url_template == "/api/general/live.json", \
        f"live call lost: {live.url_template!r} (over-stripping)"
