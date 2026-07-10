"""AC1 go-red proof for NFRA_TOOLGRAPH.TO-1's declared-vs-actual coupling diff, + AC6 class-agnostic.

The coupling diff is the load-bearing move, and TOOLGRAPH's AC1 is that it be SHOWN ABLE TO GO RED --
a diff that is merely green on the live tree has not been proven. These tests seed a KNOWN undeclared
edge and assert the diff flags it (go-red), with a NEGATIVE control (a declared edge is NOT flagged)
and an R6 impossible-value check (an all-declared input yields exactly zero findings -- the value the
diff must produce if it is measuring the intended quantity). Together the two directions bracket the
correct behaviour, so a mutation that blinds the diff (always [] ) fails go-red and a mutation that
over-flags (returns everything) fails the negative control -- a mutant-kill pair.

Run: python -m pytest org/modules/graph/tests/test_tool_graph_coupling_diff.py
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import comp_toolgraph as tg  # noqa: E402  (path set above so the sibling backend imports)

_DECLARED = {frozenset({"comp-aws", "comp-iam"}): ["IAM"]}


def _pairs(edges):
    return {frozenset({e["a"], e["b"]}) for e in edges}


def test_ac1_go_red_flags_seeded_undeclared_edge():
    """A seeded undeclared shared-backend edge MUST appear in the diff (the go-red proof)."""
    actual = [{"a": "comp-seedX", "b": "comp-seedY", "shared": ["seed_backend"]}]
    out = tg.coupling_diff(actual, _DECLARED)
    assert frozenset({"comp-seedX", "comp-seedY"}) in _pairs(out)


def test_ac1_negative_control_declared_not_flagged():
    """A DECLARED overlap edge MUST NOT be flagged as undeclared (the negative control)."""
    actual = [{"a": "comp-aws", "b": "comp-iam", "shared": ["iam_lib"]}]
    assert tg.coupling_diff(actual, _DECLARED) == []


def test_r6_impossible_value_all_declared_is_empty():
    """R6 on the diff: an all-declared input must yield ZERO findings -- the value the diff must
    never exceed if it is measuring undeclared coupling and not something else."""
    actual = [
        {"a": "comp-aws", "b": "comp-iam", "shared": ["iam_lib"]},
    ]
    assert tg.coupling_diff(actual, _DECLARED) == []


def test_ac1_mixed_flags_only_the_undeclared():
    """Given one declared + one undeclared edge, the diff flags exactly the undeclared one."""
    actual = [
        {"a": "comp-aws", "b": "comp-iam", "shared": ["iam_lib"]},          # declared
        {"a": "comp-seedX", "b": "comp-seedY", "shared": ["seed_backend"]},  # undeclared
    ]
    out = _pairs(tg.coupling_diff(actual, _DECLARED))
    assert out == {frozenset({"comp-seedX", "comp-seedY"})}


def test_ac6_non_comp_node_admits_no_schema_fork():
    """The node/edge model admits a NON-comp scanner (a future org recognizer) with no schema fork:
    two foreign scanners sharing a substrate produce a SHARES_SUBSTRATE edge via the same code."""
    a = {"tool": "org-recognizer-X", "substrate": ["org_recognizer_lib"]}
    b = {"tool": "org-recognizer-Y", "substrate": ["org_recognizer_lib"]}
    edges = tg.shares_substrate_edges([a, b])
    assert len(edges) == 1 and edges[0]["shared"] == ["org_recognizer_lib"]


def test_embedded_self_test_passes():
    """The tool's own --self-test (AC1 + AC6) passes end-to-end."""
    ok, checks = tg._self_test()
    assert ok, [c for c in checks if not c["pass"]]


def test_live_coupling_diff_is_total_and_pure():
    """Sanity on the live tree: run() returns the expected shape and the diff is a partition
    (covered + undeclared == actual). Does not assert a specific count (the tree changes)."""
    res = tg.run_coupling_diff()
    assert res["actual_substrate_edges"] == len(res["covered"]) + len(res["undeclared"])
    for e in res["undeclared"]:
        assert frozenset({e["a"], e["b"]}) not in tg.declared_coupling()
