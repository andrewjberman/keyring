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
