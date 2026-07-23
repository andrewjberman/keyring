"""test_output_contract.py -- NFRA_MSBEFF.R1R3 / M3 acceptance + the REQUIRED MUTANTS.

An unmutated assertion has never been tested. Condition (b) requires BOTH mutants on the record in the
commit; this suite carries them plus the derivation-faithfulness + no-regression checks.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_WS = Path(__file__).resolve().parents[4]  # tests/ -> graph -> modules -> org -> workspace root
if str(_WS) not in sys.path:
    sys.path.insert(0, str(_WS))

from org.modules.graph import comp_output_contract as oc  # noqa: E402
from org.modules.graph import comp_log_auto as cla  # noqa: E402


# ----------------------------------------------------------------------------------------------------
# Derivation faithfulness + NO REGRESSION vs the retired frozen set
# ----------------------------------------------------------------------------------------------------

# The 14 tools that were in the hand-frozen VERDICT_EXIT_TOOLS set (comp_log_auto.py pre-M3). The
# derivation must still classify each as a verdict tool -- retiring the freeze must not drop coverage.
_FROZEN_14 = {
    "comp-drift", "comp-lambdamap", "comp-xray", "comp-parity", "comp-validate",
    "comp-manifest-check", "comp-surface-check", "comp-honesty", "comp-freshness",
    "comp-iam", "comp-trigger", "comp-pulse", "comp-system", "comp-constants",
}


def test_derivation_covers_the_whole_retired_frozen_set():
    verdict_tools, _ = oc.verdict_exit_map()
    missing = _FROZEN_14 - set(verdict_tools)
    assert not missing, f"derivation DROPPED verdict tools the frozen set had: {sorted(missing)}"


def test_comp_blast_added_by_grounding():
    verdict_tools, refuse = oc.verdict_exit_map()
    assert "comp-blast" in verdict_tools
    assert ("comp-blast", 3) in refuse  # NOT-FOUND is a REFUSE, source-confirmed cli.py:263


def test_comp_iam_rc3_correction_verdict_to_refuse():
    """The derivation's headline correction: rc3 is a documented COVERAGE REFUSAL, not a verdict."""
    assert cla._classify_result("comp-iam", 3) == "REFUSE"
    assert cla._classify_result("comp-iam", 1) == "VERDICT"


@pytest.mark.parametrize("tool,rc,expected", [
    ("comp-blast", 1, "VERDICT"),
    ("comp-blast", 2, "VERDICT"),
    ("comp-blast", 3, "REFUSE"),
    ("comp-blast", 120, "FAIL"),      # declared tool, UNLISTED rc -> FAIL (launcher death, not a verdict)
    ("comp-constants", 3, "REFUSE"),
    ("comp-pulse", 1, "VERDICT"),
    ("comp-system", 2, "VERDICT"),
    ("comp-kuzu", 1, "FAIL"),         # simple tool: DB-missing / Cypher error IS a failure
    ("comp-pipescript", 1, "FAIL"),   # bad script name is an error; STALE/MISSING verdict is in stdout at rc0
])
def test_classify_matrix(tool, rc, expected):
    assert cla._classify_result(tool, rc) == expected


def test_exit_zero_is_pass_for_everything():
    for tool in ["comp-blast", "comp-kuzu", "comp-not-a-real-tool"]:
        assert cla._classify_result(tool, 0) == "PASS"


# ----------------------------------------------------------------------------------------------------
# REQUIRED MUTANT 1 (condition b) -- a tool with NO declared coverage/plane renders UNKNOWN, LOUD:
# never a silent omission, never a false clean, and its nonzero classifies UNKNOWN (never a verdict/FAIL).
# ----------------------------------------------------------------------------------------------------

def test_mutant_undeclared_tool_renders_loud_unknown():
    tool = "comp-deliberately-undeclared-mutant"
    cov = oc.coverage_line(tool)
    plane = oc.plane_header(tool)
    # LOUD: the word UNKNOWN appears; the line is NOT empty; coverage is explicitly NOT asserted.
    assert "UNKNOWN" in cov and "NOT asserted" in cov, f"coverage must LOUDLY disclaim: {cov!r}"
    assert "UNKNOWN" in plane, f"plane must LOUDLY disclaim: {plane!r}"
    assert cov.strip() and plane.strip(), "an undeclared tool must NOT render an empty (silently-omitted) line"


def test_mutant_undeclared_tool_classifies_unknown_not_a_verdict():
    """M3 mutant: a deliberately-undeclared tool's nonzero surfaces as UNKNOWN, not VERDICT and not FAIL."""
    got = cla._classify_result("comp-deliberately-undeclared-mutant", 1)
    assert got == "UNKNOWN", f"undeclared nonzero must be UNKNOWN, got {got!r}"
    assert got not in ("VERDICT", "REFUSE"), "an undeclared tool must not be laundered into a verdict"
    assert got != "FAIL", "condition b: undeclared is UNKNOWN, never a defaulted FAIL"


# ----------------------------------------------------------------------------------------------------
# REQUIRED MUTANT 2 (condition b) -- a tool whose coverage is 0% of the queried target says so LOUD,
# not a confident empty. Modeled on the audit's own named exhibits: the coverage line must NAME the
# structural blind spot rather than return a clean/empty answer.
# ----------------------------------------------------------------------------------------------------

def test_mutant_zero_coverage_of_target_is_loud_not_empty():
    # comp-pipescript against an .sh dispatch script: its coverage is 0% of that target (bd-tree/.py-scoped).
    cov = oc.coverage_line("comp-pipescript")
    assert ".sh" in cov and "UNCOVERED" in cov, f"the .sh dispatch blind spot must be NAMED, not omitted: {cov!r}"
    # comp-iam against an AWS-managed grant: 0% coverage on the DESIRED plane, must say so.
    cov_iam = oc.coverage_line("comp-iam")
    assert "BLIND" in cov_iam and ("AWS-managed" in cov_iam or "managed" in cov_iam), cov_iam
    # comp-blast against a target outside the indexed set: the blind spot must be named.
    cov_blast = oc.coverage_line("comp-blast")
    assert "outside the indexed" in cov_blast, cov_blast


# ----------------------------------------------------------------------------------------------------
# Consumer denominator is RUN-TIME derived, never hand-listed (the TO's own subject applied to itself)
# ----------------------------------------------------------------------------------------------------

def test_consumer_denominator_is_the_live_tools_index():
    import yaml
    man = yaml.safe_load((_WS / "org/modules/graph/graph-call-manifest.yaml").read_text(encoding="utf-8"))
    live = set((man.get("tools_index") or {}).keys())
    assert set(oc.registered_tools()) == live, "registered_tools() must equal the live tools_index, not a copy"


def test_every_registered_tool_is_declared_or_pending():
    """The completeness invariant, asserted in-suite too: no tools_index tool falls through the cracks."""
    reg = set(oc.registered_tools())
    covered = set(oc.declared_tools()) | set(oc.pending_tools())
    missing = sorted(reg - covered)
    assert not missing, f"tools_index tools in NEITHER contracts nor pending: {missing}"


def test_header_block_goes_to_two_lines():
    hb = oc.header_block("comp-iam")
    assert hb.count("\n") == 1 and hb.startswith("COVERAGE:") and "PLANE:" in hb


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
