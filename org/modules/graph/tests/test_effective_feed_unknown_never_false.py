"""NFRA_TOOLHEALTH TH-A seam: the --effective-feed load path must obey the CANNOT-EVALUATE-vs-FAIL law.

The TH-A probe emits a TRISTATE effective ("yes"|"no"|"unknown"). The seam (_effective_to_bool +
load_effective_feed) MUST map: yes->True (PROMOTE) / no->False (RETIRE) / unknown|off-vocab|ABSENT->None
(HOLD, pending_effective kept -- classify_full:132 fires only on `is True`, :134 only on `is False`,
None falls through to the pending HOLD).

THE ONE SILENT-HONESTY FAILURE (CVO~B handshake 20260712T162037Z, probe owner): unknown->False would
silently RETIRE a tool the probe NEVER measured -- collapsing "could-not-measure" into "measured-not-
effective". "no" = MEASURED-not-effective (may retire); "unknown" = COULD-NOT-MEASURE (must hold). This
test LOCKS that mapping so a future edit cannot regress it (the seam was verified correct at HEAD but
carried NO regression guard on the load/string path -- only the classify/decide taxonomy was tested).

Pure-function test -- hermetic, bd-safe (no corpus/routing/AWS; only a temp JSON file).

# rail-checked: assurance oracle for the comp-tool-health --effective-feed seam under test (NFRA_TOOLHEALTH TH-A)
Author: 0.8.0_AE_CloudComp.
"""
from __future__ import annotations

import importlib.util
import json
import os
import tempfile

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, "org", "modules", "graph", "comp_tool_health.py")

_spec = importlib.util.spec_from_file_location("comp_tool_health_undertest", _MODULE)
th = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(th)


def test_effective_to_bool_resolves_yes_no_and_legacy_bools():
    # Only "yes"/"no" (case-insensitive) and bare bools RESOLVE.
    assert th._effective_to_bool("yes") is True
    assert th._effective_to_bool("YES") is True
    assert th._effective_to_bool("no") is False
    assert th._effective_to_bool("No") is False
    assert th._effective_to_bool(True) is True     # legacy bare bool
    assert th._effective_to_bool(False) is False   # legacy bare bool -- MEASURED not-effective


def test_unknown_and_offvocab_map_to_None_never_False():
    # THE invariant: unknown / VOID / off-vocab / null -> None (pending HOLD), NEVER False.
    # A False here would silently RETIRE a tool the probe never measured.
    for x in ("unknown", "VOID", "", "maybe", "true", "false", None, 1, 0):
        got = th._effective_to_bool(x)
        assert got is None, f"{x!r} must map to None (HOLD), got {got!r} -- a silent RETIRE of an unmeasured tool"


def test_load_effective_feed_holds_unknown_resolves_yes_no():
    feed = {
        "comp-blast": {"effective": "yes"},
        "comp-drift": {"effective": "no"},
        "comp-trace": {"effective": "unknown"},
        "comp-xref": {"effective": "VOID"},
        "comp-diff": True,
        "comp-build": False,
    }
    fd, p = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    try:
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(feed, fh)
        loaded = th.load_effective_feed(p)
    finally:
        os.unlink(p)
    # yes/no (and legacy bools) resolve...
    assert loaded.get("comp-blast") is True and loaded.get("comp-diff") is True
    assert loaded.get("comp-drift") is False and loaded.get("comp-build") is False
    # ...unknown/VOID are ABSENT -> classify reads None -> HOLD (never a silent False)
    assert "comp-trace" not in loaded, "unknown MUST be absent (->None->HOLD), not a silent False"
    assert "comp-xref" not in loaded, "VOID MUST be absent (->None->HOLD), not a silent False"


def test_CANNOT_EVALUATE_is_distinct_from_FAIL_nonvacuous():
    # The mutation guard: "no" (measured-not-effective, may retire) and "unknown" (could-not-measure,
    # must hold) MUST map DIFFERENTLY. If a future edit collapses unknown->False these become identical
    # and the honesty is silently gone -- this arm fails first.
    no_v = th._effective_to_bool("no")
    unk_v = th._effective_to_bool("unknown")
    assert no_v is False, "no = MEASURED-not-effective (False, may retire)"
    assert unk_v is None, "unknown = COULD-NOT-MEASURE (None, must hold)"
    assert no_v is not unk_v, "no (FAIL) and unknown (CANNOT-EVALUATE) must NOT collapse -- the law"
