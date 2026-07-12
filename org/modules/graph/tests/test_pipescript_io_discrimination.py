"""NFRA_LIVELEARN CYCLE B tool-2 HARDENING -- the comp-pipescript io discrimination regression guard.

CTO~D (2026-07-12, non-blocking follow-up): make the "non-boilerplate" property DURABLE -- assert
io(TARGET) HAS the answer_terms AND io(CONTROL) LACKS them, so a future edit to boilerplate-ish terms is
caught (mirrors comp-surface-check's run-time non-vacuity assert + comp-iam/comp-aws committed controls).

The answer_terms (accounts_dimension_latest.parquet + producer INF_A_00) appear in io(INF_A_04) ONLY because
pipescript traversed INF_A_04's real read chain; they are ABSENT from a control script with no such chain.

Exercises the REAL comp-pipescript backend (subprocess) -- inf scripts only, read-only, sovereign-trivial.

# rail-checked: assurance oracle for the comp-pipescript io discrimination (NFRA_LIVELEARN CYCLE B tool-2)
Author: 0.8.0_AE_CloudComp.
"""
from __future__ import annotations

import os
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_CLI = os.path.join(_WS, "org", "modules", "graph", "pipeline_cli.py")

TARGET = "data/inf/scripts/gold/INF_A_04.client_dimension.py"    # reads accounts_dimension <- INF_A_00
CONTROL = "data/inf/scripts/gold/INF_A_02.fee_rate_history.py"   # no accounts_dimension chain
TERMS = ["accounts_dimension_latest.parquet", "INF_A_00"]        # the probe's discriminating answer_terms


def _io(script: str) -> str:
    r = subprocess.run([sys.executable, _CLI, "io", script], cwd=_WS,
                       capture_output=True, text=True, timeout=90)
    return r.stdout + r.stderr


def test_target_io_surfaces_all_discriminating_terms():
    out = _io(TARGET)
    for t in TERMS:
        assert t in out, f"target io MUST surface the discriminating term {t!r} (a real dependency traversal)"


def test_control_io_lacks_the_terms_proving_nonboilerplate():
    out = _io(CONTROL)
    for t in TERMS:
        assert t not in out, \
            f"control io must NOT contain {t!r} -- if it did, the term is boilerplate, not discriminating"
