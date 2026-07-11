#!/usr/bin/env python3
"""comp-pii: a security tool must verify the mechanism it audits is REACHABLE, else it reports on a
corpse (CTO ruling 2026-07-11). The serve-time pseudonymizer was RETIRED 2026-04-15 (Andrew):
needs_pseudonymization() returns False, so _transform_field is dead code. comp-pii used to parse
_transform_field's hash-map and report those fields "pseudonymized=True / protected" -- FALSE ASSURANCE
(a security tool reporting cleartext PII as hashed is the worst failure mode it has).

This locks the fix + proves it BITES both ways:
  RETIRED source  -> MASKING_RETIRED True, 0 pseudonymized fields (honest cleartext posture).
  LIVE source     -> MASKING_RETIRED False, the hashed fields ARE reported (no over-correction).
  MUTANT (pretend the gate is always live) -> the retired posture is LOST -> proves the reachability
    check is LOAD-BEARING, not decorative.

Synthetic pseudonymizer sources in a temp tree -- bd-clean, no real PII, no served read.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_WS = Path(__file__).resolve().parents[4]
_PII = _WS / "org" / "modules" / "graph" / "pii_cli.py"
spec = importlib.util.spec_from_file_location("pii_cli_under_test", str(_PII))
P = importlib.util.module_from_spec(spec)
sys.modules["pii_cli_under_test"] = P
spec.loader.exec_module(P)

# Snapshot the hardcoded field list BEFORE any _ensure mutates the module globals.
_ORIG_FIELDS = list(P.PII_FIELDS)

_RETIRED_SRC = (
    "def needs_pseudonymization(user_role):\n"
    "    return False\n"
    "\n"
    "def _transform_field(key, value, firm_id, user_role):\n"
    "    if key == 'account_id':\n"
    "        return _hash(firm_id, value, 'Acct')\n"
    "    if key in ('relationship_id', 'client_key'):\n"
    "        return _hash(firm_id, value, 'id')\n"
    "    return value\n"
)
_LIVE_SRC = (
    "def needs_pseudonymization(user_role):\n"
    "    if user_role == 'admin':\n"
    "        return False\n"
    "    return True\n"
    "\n"
    "def _transform_field(key, value, firm_id, user_role):\n"
    "    if key == 'account_id':\n"
    "        return _hash(firm_id, value, 'Acct')\n"
    "    if key in ('relationship_id', 'client_key'):\n"
    "        return _hash(firm_id, value, 'id')\n"
    "    return value\n"
)


def _write_pseudonymizer(tmp_path: Path, src: str) -> Path:
    d = tmp_path / "infra" / "aws" / "lambda" / "v2_portal" / "opal-partners-data"
    d.mkdir(parents=True, exist_ok=True)
    (d / "pseudonymizer.py").write_text(src, encoding="utf-8")
    return tmp_path


@pytest.fixture(autouse=True)
def _reset_module_state(monkeypatch):
    """Each test starts from the pristine hardcoded list + unloaded runtime flag."""
    monkeypatch.setattr(P, "PII_FIELDS", list(_ORIG_FIELDS))
    monkeypatch.setattr(P, "PSEUDONYMIZED_FIELDS", {f.name for f in _ORIG_FIELDS if f.hash_prefix})
    monkeypatch.setattr(P, "_RUNTIME_PII_LOADED", False)
    monkeypatch.setattr(P, "MASKING_RETIRED", False)
    yield


# ---- the reachability predicate (pure) ----

def test_reachability_predicate():
    assert P._serve_time_masking_reachable(_RETIRED_SRC) is False   # every return is False
    assert P._serve_time_masking_reachable(_LIVE_SRC) is True        # a return True path exists
    assert P._serve_time_masking_reachable("def other(): return 1") is None   # gate absent
    assert P._serve_time_masking_reachable("!!! not python") is None          # unparseable -> None (fail-safe)


# ---- end-to-end: RETIRED source -> honest cleartext posture ----

def test_retired_source_reports_zero_pseudonymized(tmp_path, monkeypatch):
    monkeypatch.setattr(P, "_WORKSPACE", _write_pseudonymizer(tmp_path, _RETIRED_SRC))
    P._ensure_runtime_pii_truth(verbose=False)
    assert P.MASKING_RETIRED is True
    assert P.PSEUDONYMIZED_FIELDS == set(), "retired -> nothing is hashed; must report 0 pseudonymized"
    # the fields the dead _transform_field 'would' hash must NOT be reported as protected
    assert "account_id" not in P.PSEUDONYMIZED_FIELDS
    assert "client_key" not in P.PSEUDONYMIZED_FIELDS


# ---- end-to-end: LIVE source -> the hashed fields ARE reported (no over-correction) ----

def test_live_source_reports_hashed_fields(tmp_path, monkeypatch):
    monkeypatch.setattr(P, "_WORKSPACE", _write_pseudonymizer(tmp_path, _LIVE_SRC))
    P._ensure_runtime_pii_truth(verbose=False)
    assert P.MASKING_RETIRED is False
    assert {"account_id", "relationship_id", "client_key"} <= P.PSEUDONYMIZED_FIELDS, \
        "live gate -> _transform_field's keys ARE hashed and must be reported protected"


# ---- MUTANT-KILL: pretend the gate is always live -> the retired posture is LOST ----

def test_MUTANT_pretend_gate_live_loses_the_retired_posture(tmp_path, monkeypatch):
    """If the reachability check is neutered to always-live, the RETIRED source wrongly reports the
    dead hash-map as pseudonymized (the false assurance returns). Proves the check is load-bearing."""
    monkeypatch.setattr(P, "_serve_time_masking_reachable", lambda text: True)  # MUTANT
    monkeypatch.setattr(P, "_WORKSPACE", _write_pseudonymizer(tmp_path, _RETIRED_SRC))
    P._ensure_runtime_pii_truth(verbose=False)
    assert P.MASKING_RETIRED is False, "mutant forces live -> retirement not detected"
    assert "account_id" in P.PSEUDONYMIZED_FIELDS, \
        "with the check neutered the dead hash-map is reported protected -- the false assurance the fix removes"


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
