"""comp-lambdamap Phase-1 `check` regression tests.

Day-1 fixture = the live source-map drift state as of 2026-06-01 (CVO manual audit
359375d87 + the seeking-alpha TF-source_dir bug the tool found). These assert the
tool's *detection contract* (which classes it must catch + which it must NOT
false-positive), not exact counts, so they survive legit map fixes (e.g. when
derive --write resolves the 7 MISLOCATED, those assertions are updated then).
"""
from __future__ import annotations

import os
import sys

import pytest

GRAPH_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if GRAPH_DIR not in sys.path:
    sys.path.insert(0, GRAPH_DIR)

import lambdamap_cli as lm  # noqa: E402

ROOT = lm.workspace_root()


@pytest.fixture(scope="module")
def findings():
    f, _stats = lm.compute_findings(ROOT)
    return f


def _by_class(findings, cls):
    return {name for c, name, _ in findings if c == cls}


def test_runs_and_returns_structured(findings):
    # every finding is (class, name, detail) with a known class
    for c, name, detail in findings:
        assert c in lm.CLASS_ORDER, f"unknown class {c}"
        assert name and isinstance(detail, str)


def test_external_sentinel_not_flagged(findings):
    # source_dir == "EXTERNAL" entries must NOT be WRONG_SOURCE_DIR/ORPHAN (intentional sentinel)
    wrong = _by_class(findings, "WRONG_SOURCE_DIR") | _by_class(findings, "ORPHAN_ENTRY")
    sm = lm.load_srcmap(ROOT)
    external = {k for k, v in sm.get("functions", {}).items()
                if isinstance(v, dict) and v.get("source_dir") == "EXTERNAL"}
    assert external, "expected some EXTERNAL-sentinel entries in the fixture"
    assert not (external & wrong), f"EXTERNAL entries false-flagged: {external & wrong}"


def test_detects_mislocated_top_level(findings):
    # the 7 top-level (outside functions{}) entries must be caught
    mis = _by_class(findings, "MISLOCATED")
    for expected in ("bd-incrparity-trigger", "inf-client-detail", "inf-gold-trigger",
                     "inf-bronze-trigger", "inf-otp-relay", "inf-portal-publisher",
                     "inf-portal-advisor-publisher"):
        assert expected in mis, f"MISLOCATED missed {expected}"


def test_detects_missing_entry_blindspots(findings):
    # TF-backed lambdas with no functions{} entry (the real CI blind spots)
    missing = _by_class(findings, "MISSING_ENTRY")
    for expected in ("inf-client-detail", "inf-portal-publisher", "bd-incrparity-trigger"):
        assert expected in missing, f"MISSING_ENTRY missed {expected}"


def test_detects_seeking_alpha_tf_sourcedir_bug(findings):
    # the bonus bug the tool found: TF source_dir -> absent dir (real dirs are analysis-*)
    wrong = _by_class(findings, "WRONG_SOURCE_DIR")
    assert "seeking-alpha-analysis-scraper" in wrong, \
        "WRONG_SOURCE_DIR missed the seeking-alpha TF source_dir bug"


# --- Phase 2: sha-vs-live CodeSha256 (compute_sha_findings is pure -> unit-testable) ---

_GOOD = "0" * 43 + "="          # well-formed 44-char base64 sha shape
_GOOD2 = "1" * 43 + "="
_PATHLEAK = "C:/Program Files/Git/abc123"   # the real record-terraform-deploy MSYS path-leak class


def test_sha_findings_classifies_all_buckets():
    funcs = {
        "match_fn":   {"artifact_sha256": _GOOD},
        "drift_fn":   {"artifact_sha256": _GOOD},
        "notlive_fn": {"artifact_sha256": _GOOD2},
        "norec_fn":   {},                                  # no artifact_sha256
        "corrupt_fn": {"artifact_sha256": _PATHLEAK},      # non-base64 -> CORRUPT_RECORD
    }
    live = {"match_fn": _GOOD, "drift_fn": _GOOD2}         # match equal; drift differs; notlive absent
    r = lm.compute_sha_findings(funcs, live)
    assert r["match"] == 1
    assert [d[0] for d in r["drift"]] == ["drift_fn"]
    assert r["not_live"] == ["notlive_fn"]
    assert r["no_record"] == 1
    assert [c[0] for c in r["corrupt"]] == ["corrupt_fn"]


def test_sha_corrupt_record_not_miscounted_as_drift():
    # a path-leaked sha must be CORRUPT_RECORD, never SHA_DRIFT (different fix path)
    funcs = {"x": {"artifact_sha256": _PATHLEAK}}
    r = lm.compute_sha_findings(funcs, {"x": _GOOD})
    assert not r["drift"], "path-leak corrupt record must not be reported as deploy-drift"
    assert r["corrupt"] and r["corrupt"][0][0] == "x"


def test_sha_dispositioned_note_suppresses_drift():
    # an entry whose _note documents an intentional divergence is DISPOSITIONED, not SHA_DRIFT
    funcs = {"vf": {"artifact_sha256": _GOOD, "_note": "S3 artifact is a stale re-zip NOT to apply; TF ignore_changes; intentional-leave"}}
    r = lm.compute_sha_findings(funcs, {"vf": _GOOD2})   # recorded != live, but dispositioned
    assert not r["drift"], "dispositioned divergence must not be SHA_DRIFT"
    assert [d[0] for d in r["dispositioned"]] == ["vf"]


def test_sha_plain_note_does_not_suppress_real_drift():
    # FALSE-NEGATIVE GUARD: a generic _note WITHOUT a disposition marker must NOT suppress real drift
    funcs = {"y": {"artifact_sha256": _GOOD, "_note": "just a normal description, deployed by the daily job"}}
    r = lm.compute_sha_findings(funcs, {"y": _GOOD2})   # recorded != live, no disposition marker
    assert [d[0] for d in r["drift"]] == ["y"], "a plain _note must not disposition-away real drift"
    assert not r["dispositioned"]
