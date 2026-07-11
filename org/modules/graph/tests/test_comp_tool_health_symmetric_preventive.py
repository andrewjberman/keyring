"""NFRA_TOOLPASS: comp-tool-health classify_full was ASYMMETRIC on the preventive axis (CVO finding,
CTO-accepted as a real LOW-severity honesty gap).

is_preventive_tool tempered the USED + low-EFFECTIVE branch out of FIX -> KEEP (:152: a preventive
gate's value = drift silently PREVENTED, which usage cannot observe), but the NOT-used + EFFECTIVE-
pending branch (:136) emitted a bare RETIRE? for a preventive gate too -- resting only on the
'?'+pending honesty, not the guard. A preventive gate showing NO usage is exactly the case usage
cannot measure. FIX (stopgap-until-EFFECTIVE): the not-used branch now HOLDs a preventive gate
(RETIRE?-PREVENTIVE, do-not-retire pending EFFECTIVE/TH-A) instead of a bare RETIRE?.

Pure-function test of classify_full -- hermetic, bd-safe (no corpus/routing/AWS).

# rail-checked: assurance oracle for comp-tool-health under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B.
"""

import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_MODULE = os.path.join(_WS, "org", "modules", "graph", "comp_tool_health.py")

_spec = importlib.util.spec_from_file_location("comp_tool_health_undertest", _MODULE)
th = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(th)


def test_not_used_preventive_gate_is_HELD_not_bare_retired():
    # not used + EFFECTIVE pending + PREVENTIVE -> RETIRE? but a preventive HOLD, symmetric with :152.
    verdict, pending, reason = th.classify_full(used=False, rail_consistent=None, effective=None, preventive=True)
    assert verdict == "RETIRE", f"token must stay RETIRE (preserves --verdict/counts/rank); got {verdict}"
    assert pending is True, "must remain EFFECTIVE-pending (the '?' -- resolves via TH-A)"
    assert "PREVENTIVE" in reason and "HOLD" in reason, f"preventive HOLD not surfaced: {reason!r}"
    assert "stopgap-until-EFFECTIVE" in reason, f"stopgap marker missing (CTO directive): {reason!r}"


def test_not_used_non_preventive_is_the_bare_retire_NONVACUOUS():
    # SAME axes, preventive=False -> the ORIGINAL bare RETIRE? reason. The guard must CHANGE the reason
    # (else the preventive branch is vacuous).
    _, _, reason_plain = th.classify_full(used=False, rail_consistent=None, effective=None, preventive=False)
    _, _, reason_prev = th.classify_full(used=False, rail_consistent=None, effective=None, preventive=True)
    assert "HOLD" not in reason_plain and "PREVENTIVE" not in reason_plain, \
        f"a NON-preventive not-used tool must keep the bare RETIRE rationale: {reason_plain!r}"
    assert reason_plain != reason_prev, "the preventive guard must bite (distinct reason) -- non-vacuous"


def test_used_branch_preventive_symmetry_preserved():
    # the pre-existing USED + low-EFFECTIVE preventive temper (:152) must still hold -> KEEP not FIX,
    # confirming the two branches are now symmetric on the preventive axis.
    v_prev, _, _ = th.classify_full(used=True, rail_consistent=True, effective=False, preventive=True)
    v_plain, _, _ = th.classify_full(used=True, rail_consistent=True, effective=False, preventive=False)
    assert v_prev == "KEEP", f"used + low-effective + preventive must be KEEP (:152); got {v_prev}"
    assert v_plain == "FIX", f"used + low-effective + NON-preventive must be the load-bearing FIX; got {v_plain}"


if __name__ == "__main__":
    test_not_used_preventive_gate_is_HELD_not_bare_retired()
    print("PASS: not-used preventive gate -> RETIRE?-PREVENTIVE HOLD (not a bare RETIRE?)")
    test_not_used_non_preventive_is_the_bare_retire_NONVACUOUS()
    print("PASS: non-preventive not-used keeps the bare RETIRE rationale (guard is non-vacuous)")
    test_used_branch_preventive_symmetry_preserved()
    print("PASS: used-branch preventive temper (:152) preserved -- the axis is now symmetric")
    print("=== comp-tool-health symmetric-preventive guard: ALL PASS ===")
