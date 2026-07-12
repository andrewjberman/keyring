"""NFRA_LIVELEARN CYCLE B tool -- comp-manifest-check DETECTION discrimination (CTO~D safe re-rank).

Does `check --mode blocking` FLAG a raw-graph-access file (rc!=0) AND CLEAR a canonical-access file (rc0)?
Un-gameable: the runner STAGES synthetic fixtures (raw kuzu.Connection vs a canonical comp-blast call) --
firm-agnostic, no estate. flag-all / flag-none -> no; crash -> VOID (never a silent no). Preventive gate.

Hermetic: injected runner (fake rc keyed on the fixture path); no subprocess, no firm data.

# rail-checked: assurance oracle for the comp-manifest-check detection discrimination (NFRA_LIVELEARN CYCLE B)
Author: 0.8.0_AE_CloudComp.
"""
from __future__ import annotations

import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, "org", "modules", "graph", "compproof", "tool_probe.py")
_spec = importlib.util.spec_from_file_location("tool_probe_mc", _MODULE)
tp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tp)


def _probe():
    return {"probe_id": "comp-manifest-check/noncanonical-detection-discrimination", "tool": "comp-manifest-check",
            "tool_class": "graph-access-lint", "kind": "manifestcheck-discrimination", "fixture": {},
            "usability_timeout_s": 90}


def _run(rc_noncanon, rc_canon):
    def runner(path, to):
        return rc_noncanon if "noncanon" in path else rc_canon
    return tp._run_manifestcheck_discrimination_probe(_probe(), runner=runner)


def test_flags_noncanon_clears_canon_YES():
    assert _run(1, 0)["effective"] == "yes"


def test_flag_none_missed_the_noncanonical_no():
    assert _run(0, 0)["effective"] == "no"


def test_flag_all_false_flags_the_canonical_no():
    assert _run(1, 1)["effective"] == "no"


def test_run_failure_VOIDs_never_silent_no():
    def boom(p, to):
        raise RuntimeError("subprocess died")
    row = tp._run_manifestcheck_discrimination_probe(_probe(), runner=boom)
    assert row["effective"] == "unknown" and "run failed" in row["void_reason"]
