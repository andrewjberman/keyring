"""
Tests for comp-learns-score -- the NFRA_COMPLEARN value-anchored scorer (P2).

Locks the load-bearing Goodhart-honesty invariants (the CTO-owned gate): the scorer ranks on VALUE
(escapes-prevented / friction-averted), NEVER on raw usage count, and reuses the COMPROUTE L3
outcome-weighting (one signal, two consumers).

Author: 0.8.0_AE_CloudComp~E (NFRA_COMPLEARN P2). 2026-07-01.
"""

from __future__ import annotations

import sys
from pathlib import Path

_WORKSPACE = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.comp_learns_score import (  # noqa: E402
    _self_test,
    build_gap_candidates,
    build_merge_retire_candidates,
    escape_severity,
    is_preventive_tool,
    outcome_value,
)


def test_self_test_all_pass():
    ok, checks = _self_test()
    assert ok, f"failing: {[c['check'] for c in checks if not c['pass']]}"


def test_severity_is_friction_not_usage():
    """found-nothing (unmet need) > went-raw-and-found > bare listing; two identical successful runs
    add no severity (this is friction, not usage)."""
    assert escape_severity({"action": "RUN-GREP", "matches": 0}) == 1.0
    assert escape_severity({"action": "RUN-GREP", "matches": 20}) == 0.6
    assert escape_severity({"action": "RUN-LS"}) == 0.3
    assert escape_severity({"action": "ROUTE"}) == 0.0


def test_severity_matters_at_equal_volume():
    """At EQUAL event count, a higher-severity unmet need outranks a milder one."""
    n = 12
    unmet = [{"action": "RUN-GREP", "term": "gap", "target_path": "infra/aws", "matches": 0}] * n
    mild = [{"action": "RUN-LS", "term": "ls", "target_path": "org/tmp", "matches": 3}] * n
    vals = {c["candidate"]: c["value_score"] for c in build_gap_candidates(unmet + mild)}
    assert max(v for k, v in vals.items() if "infra" in k) > max(v for k, v in vals.items() if "tmp" in k)


def test_deny_names_no_gap_and_is_not_a_candidate():
    """DENY rows carry no term/target -> they name no gap and must never become a build-next candidate
    (the rail working != an unmet capability need)."""
    assert build_gap_candidates([{"action": "DENY", "tool": "Bash"}] * 100) == []


def test_high_usage_low_value_tool_is_a_retire_candidate():
    """Usage never protects a tool: a high-invocation low-outcome tool surfaces to retire; a
    low-invocation high-outcome tool does not."""
    rolling = ([{"tool": "noisy", "result": "FAIL"}] * 25 + [{"tool": "noisy", "result": "DENY"}] * 25
               + [{"tool": "solid", "result": "PASS"}] * 4)
    retire = {c["candidate"].split()[0] for c in build_merge_retire_candidates(rolling)}
    assert "noisy" in retire and "solid" not in retire


def test_every_gap_candidate_cites_value_evidence():
    """No evidence-free rank -- each item carries its value metric + evidence (a Goodhart leak otherwise)."""
    rows = [{"action": "RUN-GREP", "term": "iam policy gap check", "target_path": "infra/aws", "matches": 0}] * 3
    for c in build_gap_candidates(rows):
        assert c["value_metric"]["escapes_prevented"] > 0
        assert c["value_evidence"]["top_terms"]


def test_preventive_gate_retire_score_is_tempered_and_flagged():
    """CTO caveat: a preventive/enforcement GATE (e.g. comp-manifest-check) with a low value-per-run is
    likely silently SUCCEEDING (drift prevented = unobservable), not low-value. Its retire score is
    tempered vs a plain tool with the identical low outcome, and it is flagged for human judgment."""
    assert is_preventive_tool("comp-manifest-check") and is_preventive_tool("ds-commit-gate")
    assert not is_preventive_tool("comp-lambdamap") and not is_preventive_tool("comp-constants")
    rolling = [{"tool": "comp-manifest-check", "result": "FAIL"}] * 20 + [{"tool": "plain-tool", "result": "FAIL"}] * 20
    cands = {c["candidate"].split()[0]: c for c in build_merge_retire_candidates(rolling)}
    gate, plain = cands["comp-manifest-check"], cands["plain-tool"]
    assert gate["preventive_gate"] is True and plain["preventive_gate"] is False
    assert gate["value_score"] < plain["value_score"]   # tempered


def test_reuses_comproute_l3_outcome_weighting():
    """One signal, two consumers: the imported outcome_value is COMPROUTE L3's, consistent."""
    assert outcome_value({"result": "PASS"}) == 1.0
    assert outcome_value({"result": "FAIL"}) == 0.0
    assert outcome_value({"result": "PASS", "gap_text": "found"}) == 1.0   # capped at 1.0
