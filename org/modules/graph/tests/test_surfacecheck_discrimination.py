"""NFRA_LIVELEARN CYCLE B tool-1 -- comp-surface-check DETECTION-CORRECTNESS discrimination probe.

CTO~D B2 ruling (2026-07-12): score the EFFECTIVE axis on DETECTION-CORRECTNESS (a regression guard, like
comp-iam/comp-aws) -- does comp-surface-check DISCRIMINATE a registered SEV1 surface (rc!=0 blocking) from
a non-critical file (rc0)? NON-VACUOUS both directions (flag-all AND flag-none both score "no"); VOID (never
a silent "no") on a broken control or a run failure. The mandatory SCOPE annotation (effective=yes attests
DETECTION-CORRECTNESS ONLY, not "surfaces protected" -- LD-0273 is the separate wiring axis) rides every row.

Hermetic: injected runner (fake rc) + registry_reader (fake membership); no subprocess, no estate.

# rail-checked: assurance oracle for the comp-surface-check detection-correctness probe (NFRA_LIVELEARN CYCLE B)
Author: 0.8.0_AE_CloudComp.
"""
from __future__ import annotations

import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, "org", "modules", "graph", "compproof", "tool_probe.py")
_spec = importlib.util.spec_from_file_location("tool_probe_surfacecheck", _MODULE)
tp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tp)


def _probe():
    return {"probe_id": "comp-surface-check/sev1-detection-discrimination", "tool": "comp-surface-check",
            "tool_class": "critical-surface-detection", "kind": "surfacecheck-discrimination",
            "fixture": {"sev1_path": "portal/x.tsx", "noncritical_path": "org/y.py", "registry": "reg.yaml"},
            "usability_timeout_s": 60}


def _run(rc_map, registered):
    return tp._run_surfacecheck_discrimination_probe(
        _probe(), runner=lambda path, to: rc_map[path], registry_reader=lambda reg: set(registered))


def test_discriminates_scores_yes_with_scope():
    row = _run({"portal/x.tsx": 2, "org/y.py": 0}, ["portal/x.tsx"])   # SEV1 flagged, non-critical cleared
    assert row["effective"] == "yes" and row["isolation_ok"] is True
    assert "DETECTION-CORRECTNESS ONLY" in row["effective_evidence"]["scope"], \
        "the mandatory scope annotation MUST ride the evidence (never 'surfaces protected')"
    assert "LD-0273" in row["effective_evidence"]["scope"]


def test_flag_none_is_no():   # missed the SEV1 -> silent false-clean (the worst regression)
    assert _run({"portal/x.tsx": 0, "org/y.py": 0}, ["portal/x.tsx"])["effective"] == "no"


def test_flag_all_is_no():    # false-flags a non-critical -> over-alarm
    assert _run({"portal/x.tsx": 2, "org/y.py": 2}, ["portal/x.tsx"])["effective"] == "no"


def test_inverted_is_no():
    assert _run({"portal/x.tsx": 0, "org/y.py": 2}, ["portal/x.tsx"])["effective"] == "no"


def test_vacuous_positive_control_VOIDs():   # SEV1 path not registered -> the positive control is vacuous
    row = _run({"portal/x.tsx": 2, "org/y.py": 0}, [])
    assert row["effective"] == "unknown" and "VACUOUS" in row["void_reason"], \
        "a non-registered SEV1 control must VOID (unknown), never a silent verdict"


def test_invalid_negative_control_VOIDs():   # the 'non-critical' path IS registered -> control invalid
    row = _run({"portal/x.tsx": 2, "org/y.py": 0}, ["portal/x.tsx", "org/y.py"])
    assert row["effective"] == "unknown" and "INVALID" in row["void_reason"]


def test_run_failure_VOIDs_never_silent_no():
    def boom(path, to):
        raise RuntimeError("subprocess died")
    row = tp._run_surfacecheck_discrimination_probe(
        _probe(), runner=boom, registry_reader=lambda reg: {"portal/x.tsx"})
    assert row["effective"] == "unknown" and "run failed" in row["void_reason"], \
        "a crash/timeout is UNKNOWN (VOID), never a silent 'no' (CANNOT-EVALUATE vs FAIL)"


def test_nonvacuous_yes_and_no_do_not_collapse():
    yes = _run({"portal/x.tsx": 2, "org/y.py": 0}, ["portal/x.tsx"])["effective"]
    no = _run({"portal/x.tsx": 2, "org/y.py": 2}, ["portal/x.tsx"])["effective"]
    assert yes == "yes" and no == "no" and yes != no, "the probe discriminates -- not undiscriminating"
