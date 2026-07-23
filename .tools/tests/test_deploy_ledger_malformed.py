"""test_deploy_ledger_malformed.py -- the MALFORMED-IS-A-VERDICT-NOT-A-CRASH guard.

CTO gate-integrity dispatch 2026-07-23T205615Z: `deploy_ledger.py check --red` died with
KeyError 'legs' partway through the Layer-1 sentinel sweep. The blast radius was NOT one entry --
Layer 1 aborts before Layer 2 ever runs, so the ENTIRE gate-bypass scan was unreachable: the live
run after the fix surfaced 7 unindexed open ledgers that the crash had been hiding.

A crashed red-scan cannot assert "0 stranded" -- it fails WITHOUT rendering a verdict, which is the
instrument-that-cannot-fail class inverted. Same law as the R1R3 appender: UNKNOWN IS NOT A VERDICT.

These fixtures are DELIBERATELY MALFORMED and live in the committed set so the crash class cannot
return silently: every one must yield a REASON STRING (a verdict the caller renders loud), never an
exception.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

_WS = Path(__file__).resolve().parents[2]
_MOD = _WS / ".tools" / "deploy_ledger.py"

_spec = importlib.util.spec_from_file_location("deploy_ledger_undertest", _MOD)
dl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dl)


def _write(tmp_path, name, payload):
    p = tmp_path / name
    p.write_text(payload if isinstance(payload, str) else json.dumps(payload), encoding="utf-8")
    return p


def test_wellformed_sentinel_parses(tmp_path):
    """A writer-shaped sentinel returns the dict (not a reason string)."""
    p = _write(tmp_path, "ok.json", {
        "slug": "x", "opened_at": "2026-07-23T11:02:00", "legs": [{"id": "L1", "proof": "sha"}]})
    got = dl._read_sentinel(p)
    assert isinstance(got, dict) and got["slug"] == "x"


# --- THE PRODUCTION REGRESSION: the exact shape that crashed the sweep -------------------------
def test_production_malformed_shape_returns_reason_not_crash(tmp_path):
    """The real 2026-07-23 offender: a hand-authored CLOSED-deploy record in the sentinel dir,
    carrying a foreign schema (deploy_id/mechanism/result/rollback) with NO slug and NO legs.
    Must render a reason, never raise -- this is the exact KeyError 'legs' that blinded the gate."""
    p = _write(tmp_path, "ws1-lever-a-age-bound-20260723.json", {
        "deploy_id": "ws1-lever-a-age-bound-20260723",
        "opened_at": "2026-07-23T11:02Z",
        "agent": "0.6.2_AE_PartnerETL~A",
        "scope": "cot-pipeline ...", "mechanism": "build-and-upload -> ...",
        "status": "CLOSED", "rollback": "revert ...", "closed_at": "2026-07-23T11:12Z",
        "result": "Apply complete 0/1/0 ...",
    })
    reason = dl._read_sentinel(p)
    assert isinstance(reason, str)
    assert "missing required key(s)" in reason
    assert "slug" in reason and "legs" in reason


@pytest.mark.parametrize("name,payload,expect", [
    ("no_legs.json",     {"slug": "a", "opened_at": "2026-07-23T11:02:00"},              "missing required key(s)"),
    ("no_slug.json",     {"opened_at": "2026-07-23T11:02:00", "legs": []},               "missing required key(s)"),
    ("no_opened.json",   {"slug": "a", "legs": []},                                      "missing required key(s)"),
    ("legs_not_list.json", {"slug": "a", "opened_at": "2026-07-23T11:02:00", "legs": {}}, "'legs' is dict"),
    ("bad_opened.json",  {"slug": "a", "opened_at": "not-a-date", "legs": []},           "unparseable"),
    ("not_json.json",    "{ this is not json",                                            "UNPARSEABLE JSON"),
    ("not_object.json",  [1, 2, 3],                                                       "not a JSON object"),
])
def test_malformed_variants_yield_reason_never_raise(tmp_path, name, payload, expect):
    """Every malformed shape is a VERDICT (reason string), never an exception."""
    p = _write(tmp_path, name, payload)
    reason = dl._read_sentinel(p)  # must not raise
    assert isinstance(reason, str), f"{name} returned {type(reason).__name__}, expected a reason string"
    assert expect in reason, f"{name}: reason {reason!r} lacks {expect!r}"


def test_required_keys_are_exactly_what_the_scan_dereferences():
    """The required set must cover the keys the Layer-1 scan dereferences UNGUARDED -- if the scan
    grows a new unguarded key, this test is the reminder to add it here too."""
    assert set(dl.REQUIRED_SENTINEL_KEYS) == {"slug", "opened_at", "legs"}


def test_reason_names_the_writer_contract(tmp_path):
    """The loud line must tell the operator what a real sentinel looks like (repair guidance),
    not just that something is wrong."""
    p = _write(tmp_path, "x.json", {"opened_at": "2026-07-23T11:02:00"})
    reason = dl._read_sentinel(p)
    assert "writer emits" in reason


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
