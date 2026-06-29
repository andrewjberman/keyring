"""NFRA_COMPAWS.SFN-FIX AC3 -- regression fixture for the recursive ASL walker.

Guards comp_aws_cli._sfn_task_invokes / _walk_asl_states against a silent
recursion regression: a Lambda Task nested in a Parallel branch AND ones nested
in BOTH Map syntaxes (ItemProcessor new-style + Iterator legacy-style), plus the
two resource forms (direct arn + arn:aws:states::: SDK-integration with
Parameters.FunctionName), must all be extracted at any depth.

The SFN-INVOKES-NESTED-GAP (top-level-only extraction -> ~17 under-emitted
SFN->Lambda INVOKES edges) was a comp-aws blast-radius blind spot -- the
destructive-op pre-gate ("0 cross-edges" before a teardown) could read FALSE on
an SFN-orchestrated Lambda. Fixed e13e93391 + certified cee3f6993 (26/26 vs
live); this fixture makes the recursion non-regressable. Author: 0.7.0_AE_CloudOps~B.
"""
from __future__ import annotations

import json
import os
import sys

GRAPH_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if GRAPH_DIR not in sys.path:
    sys.path.insert(0, GRAPH_DIR)

import comp_aws_cli as ca  # noqa: E402

_ACCT = ca.ACCOUNT


def _arn(name):
    return f"arn:aws:lambda:us-east-1:{_ACCT}:function:{name}"


# An ASL def that exercises EVERY nesting + resource form the walker must handle.
_FIXTURE = json.dumps({
    "States": {
        # top-level, direct arn Resource
        "Top": {"Type": "Task", "Resource": _arn("top-fn"), "Next": "Par"},
        # nested in a Parallel branch
        "Par": {"Type": "Parallel", "Next": "MapNew", "Branches": [
            {"States": {"InBranch": {"Type": "Task", "Resource": _arn("parallel-fn"), "End": True}}},
        ]},
        # nested in a Map -- new-style ItemProcessor, SDK-integration + Parameters.FunctionName (arn form)
        "MapNew": {"Type": "Map", "Next": "MapOld", "ItemProcessor": {"States": {
            "InMapNew": {"Type": "Task", "Resource": "arn:aws:states:::lambda:invoke",
                         "Parameters": {"FunctionName": _arn("mapnew-fn")}, "End": True},
        }}},
        # nested in a Map -- legacy Iterator, SDK-integration + Parameters.FunctionName (bare NAME form)
        "MapOld": {"Type": "Map", "Next": "Runtime", "Iterator": {"States": {
            "InMapOld": {"Type": "Task", "Resource": "arn:aws:states:::lambda:invoke",
                         "Parameters": {"FunctionName": "maplegacy-fn"}, "End": True},
        }}},
        # a runtime-reference FunctionName.$ -- NOT statically resolvable, must be SKIPPED (no spurious edge)
        "Runtime": {"Type": "Task", "Resource": "arn:aws:states:::lambda:invoke",
                    "Parameters": {"FunctionName.$": "$.fn"}, "End": True},
    },
})


def test_walker_extracts_every_nested_invoke():
    invokes = ca._sfn_task_invokes(_FIXTURE)
    targets = {arn for _state, arn in invokes}
    # all four nested/top-level invokes extracted, bare-name resolved to arn-form
    assert _arn("top-fn") in targets, "top-level direct-arn invoke missed"
    assert _arn("parallel-fn") in targets, "Parallel.Branches nested invoke missed"
    assert _arn("mapnew-fn") in targets, "Map.ItemProcessor (new-style) nested invoke missed"
    assert _arn("maplegacy-fn") in targets, "Map.Iterator (legacy) nested invoke missed (or name->arn co-key wrong)"


def test_walker_skips_runtime_reference_no_spurious_edge():
    # a FunctionName.$ runtime reference is not statically resolvable -> no edge (no false INVOKES)
    targets = {arn for _s, arn in ca._sfn_task_invokes(_FIXTURE)}
    assert all("$.fn" not in t for t in targets), "runtime-ref FunctionName.$ produced a spurious edge"
    assert len(targets) == 4, f"expected exactly 4 resolvable invokes, got {len(targets)}: {sorted(targets)}"


def test_walk_asl_states_recurses_all_depths():
    # the generator itself must yield the nested state names (the recursion contract)
    defn = json.loads(_FIXTURE)
    names = {n for n, _ in ca._walk_asl_states(defn["States"])}
    for expected in ("Top", "InBranch", "InMapNew", "InMapOld"):
        assert expected in names, f"_walk_asl_states did not recurse to {expected}"
