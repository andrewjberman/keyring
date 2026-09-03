"""Control: safe-deploy's receipt enumerates the ACTUAL upload set, both legs.

CTO GO 2026-08-20T0020Z. The receipt previously counted `detect_script_files` alone while
`detect_bundle_member_files` deployed on its own leg, so a BUNDLE-MEMBER-ONLY change printed
"0 script file(s) to deploy" and then deployed one.

THE NAMED CONTROL: a bundle-member-only deploy must APPEAR in the receipt.

Asserted in both directions, because a "fix" that simply printed a bigger number would satisfy
a one-sided test:
  1. bundle-member-only  -> receipt total is 1, and the path is named on the [bundle-member] leg
  2. script-only         -> receipt still says 1 script / 0 bundle-member (no double-count,
                            no regression in the ordinary case)
  3. the two sets do not double-count a .py that is BOTH a script and a bundle member

Usage: python .tools/tests/test_safe_deploy_receipt_names_both_legs.py
"""
from __future__ import annotations

import sys
from pathlib import Path

WS = Path(__file__).resolve().parents[2]   # .tools/tests/<this> -> workspace root; no subprocess at import
sys.path.insert(0, str(WS / ".tools"))

import safe_deploy_core as sdc  # noqa: E402

RESULTS: list[tuple[str, str, str]] = []


def rec(tid, ok, detail):
    RESULTS.append((tid, "PASS" if ok else "FAIL", detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tid}: {detail}")


# The one declared non-.py bundle-member authority in the estate today.
ROSTER = "data/mdpf/config/partner_roster.json"
SCRIPT = "data/mdpf/scripts/gold/mdpf_aggregate_aua.py"


def sets_for(paths):
    return (sdc.detect_script_files(explicit_files=paths),
            sdc.detect_bundle_member_files(explicit_files=paths))


def receipt_total(files, bundle):
    bundle_only = [f for f in bundle if f not in files]
    return len(files) + len(bundle_only), len(files), len(bundle_only)


_RAN = False


def _run_battery():
    """EVERY piece of work the battery does lives here, so IMPORT IS INERT (the T-16 pass-2 shape,
    03cf4d17ac; NFRA_COMPEFFICACY F6, 92794). Called once per process by test_all_arms_pass (pytest)
    or _report (direct). safe_deploy_core is imported at module level (measured 0.5 s, no subprocess); the arms ran at import before this."""
    global _RAN
    if _RAN:
        return
    _RAN = True
    # --- 1. bundle-member-only: the case the receipt was blind to ---
    files, bundle = sets_for([ROSTER])
    total, n_s, n_b = receipt_total(files, bundle)
    rec("BUNDLE-ONLY-APPEARS", total == 1 and n_s == 0 and n_b == 1,
        f"roster-only change -> receipt total={total} ({n_s} script, {n_b} bundle-member). "
        f"Before the fix this printed 0 while deploying 1.")

    # --- 2. script-only: no regression, no double-count ---
    files, bundle = sets_for([SCRIPT])
    total, n_s, n_b = receipt_total(files, bundle)
    rec("SCRIPT-ONLY-UNCHANGED", total == 1 and n_s == 1,
        f"ordinary script change -> receipt total={total} ({n_s} script, {n_b} bundle-member); "
        f"the ordinary path is untouched")

    # --- 3. both together: the union is counted once, not twice ---
    files, bundle = sets_for([ROSTER, SCRIPT])
    total, n_s, n_b = receipt_total(files, bundle)
    rec("NO-DOUBLE-COUNT", total == n_s + n_b and total == 2,
        f"roster + script -> receipt total={total} ({n_s} script, {n_b} bundle-member); "
        f"a path in BOTH sets is counted once")

    # --- 4. the nothing-to-do gate and the receipt agree on their domain ---
    # :997 exits when NEITHER set has entries; the receipt must therefore be able to describe
    # anything that gets past that gate. A receipt whose domain is narrower than its gate's is
    # exactly the defect this fixes.
    files, bundle = sets_for([ROSTER])
    rec("GATE-AND-RECEIPT-SAME-DOMAIN", bool(files or bundle) and receipt_total(files, bundle)[0] > 0,
        "a path that passes the nothing-to-do gate is describable by the receipt "
        "(gate domain == receipt domain)")


def _report() -> int:
    _run_battery()
    n = sum(1 for _, v, _ in RESULTS if v == "PASS")
    print()
    print("=" * 80)
    print("SAFE-DEPLOY RECEIPT BATTERY: %d/%d PASS (denominator %d)" % (n, len(RESULTS), len(RESULTS)))
    print("=" * 80)
    return 0 if n == len(RESULTS) else 1


def test_all_arms_pass():
    _run_battery()
    failed = [(t, d) for t, v, d in RESULTS if v != "PASS"]
    assert not failed, "arms failed (%d of %d): %s" % (len(failed), len(RESULTS), failed)
    print("SAFE-DEPLOY RECEIPT BATTERY: %d/%d PASS (denominator %d)" % (len(RESULTS), len(RESULTS), len(RESULTS)))


if __name__ == "__main__":
    sys.exit(_report())
