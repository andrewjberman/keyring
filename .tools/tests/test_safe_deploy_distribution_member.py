"""Control: a bundle member flagged DISTRIBUTION keeps its own loose leg AND re-mints its bundle.

R-45 (1.0.0_SA_CTO @57bc083d45; cell IRPT_BCKEND.TO-IB-rtc-2). The X-iii routing puts every bundle
member in `triggered` and takes it OUT of `loose` ("loose leg frozen"). That is right for a file the
bundle owns outright, and wrong for a file another pipeline serves on its own per-file leg: declaring
it would freeze that firm's served module while the push reads green. The DISTRIBUTION flag marks the
second kind: the member routes to BOTH legs.

Asserted in both directions, so a routing that simply sent everything everywhere fails:
  1. a FLAGGED member        -> its bundle is triggered AND the path stays in the loose leg
  2. an UNFLAGGED member     -> its bundle is triggered and the path is NOT in the loose leg (X-iii,
                                unchanged)
  3. a NON-member script     -> loose leg only, nothing triggered
  4. a non-.py CONFIG member -> its bundle is triggered via the bundle-member detector, no loose leg
  5. the DECLARATION         -> every flagged member has a real per-file target (a flag on a file with
                                no loose leg would be a claim with nothing behind it), and the
                                investor_reporting bundle carries exactly the three per-firm
                                runner_common.py as its flagged members
  6. the MUTANT              -> the same routing on a copy of CODE_TREES with the flag REMOVED puts the
                                member back to X-iii's bundle-only leg; so arm 1 is caused by the flag
                                and is not a constant

Nothing here touches S3: `route_bundle_members` is the routing half of main(), with no upload in it.

Usage: python .tools/tests/test_safe_deploy_distribution_member.py
"""
from __future__ import annotations

import contextlib
import copy
import io
import sys
from pathlib import Path

WS = Path(__file__).resolve().parents[2]   # .tools/tests/<this> -> workspace root; no subprocess at import
sys.path.insert(0, str(WS / ".tools"))

import safe_deploy_core as sdc  # noqa: E402

RESULTS: list[tuple[str, str, str]] = []

BUNDLE = "investor_reporting"
FLAGGED = [
    "data/assets/scripts/gold/runners_49f/runner_common.py",
    "data/inf/scripts/gold/runners_inf/runner_common.py",
    "data/cot/scripts/gold/runners_cot/runner_common.py",
]
UNFLAGGED = "data/assets/scripts/gold/investor_reporting/directory_runner.py"
NON_MEMBER = "data/mdpf/scripts/gold/mdpf_aggregate_aua.py"
CONFIG = "data/firm_registry.json"


def rec(tid, ok, detail):
    RESULTS.append((tid, "PASS" if ok else "FAIL", detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tid}: {detail}")


def route(paths):
    """Run the guard's own routing on `paths` exactly as main() feeds it; stdout captured."""
    files = sdc.detect_script_files(explicit_files=paths)
    bundle_files = sdc.detect_bundle_member_files(explicit_files=paths)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        triggered, loose = sdc.route_bundle_members(files, bundle_files)
    return sorted(triggered), loose, buf.getvalue()


_RAN = False


def _run_battery():
    """Import is inert; every arm runs here, once per process."""
    global _RAN
    if _RAN:
        return
    _RAN = True

    # --- 1. a flagged member routes to BOTH legs ---
    for p in FLAGGED:
        trig, loose, out = route([p])
        rec("FLAGGED-BOTH-LEGS " + p.split("/")[1], trig == [BUNDLE] and loose == [p],
            f"{p} -> triggered={trig} loose={loose}; line: "
            f"{[ln for ln in out.splitlines() if 'BUNDLE-ROUTED' in ln][:1]}")

    # --- 2. an unflagged member routes as X-iii always has ---
    trig, loose, out = route([UNFLAGGED])
    rec("UNFLAGGED-BUNDLE-ONLY", trig == [BUNDLE] and loose == [],
        f"{UNFLAGGED} -> triggered={trig} loose={loose} (loose leg frozen, X-iii, unchanged)")

    # --- 3. a non-member script: loose only ---
    trig, loose, _ = route([NON_MEMBER])
    rec("NON-MEMBER-LOOSE-ONLY", trig == [] and loose == [NON_MEMBER],
        f"{NON_MEMBER} -> triggered={trig} loose={loose}")

    # --- 4. a non-.py config member: bundle only, through the member detector ---
    trig, loose, _ = route([CONFIG])
    rec("CONFIG-MEMBER-BUNDLE-ONLY", trig == [BUNDLE] and loose == [],
        f"{CONFIG} -> triggered={trig} loose={loose}")

    # --- 5. the declaration: exactly the three, each with a real loose target ---
    hit = sdc.find_bundle(BUNDLE)
    members = hit[2]["members"] if hit else {}
    flagged = sorted(m["repo_path"] for m in members.values() if sdc.is_distribution_spec(m))
    targets = {p: sdc.file_to_s3_target(p) for p in flagged}
    rec("DECLARED-FLAG-SET", flagged == sorted(FLAGGED) and all(targets.values()),
        f"{len(flagged)} flagged of {len(members)} members: {flagged}; "
        f"per-file targets: {[(t[0], t[1]) if t else None for t in targets.values()]}")
    every = [(bn, m["repo_path"]) for t in sdc.CODE_TREES.values()
             for bn, b in t.get("bundles", {}).items() for m in b["members"].values()
             if sdc.is_distribution_spec(m)]
    orphan = [x for x in every if sdc.file_to_s3_target(x[1]) is None]
    rec("NO-FLAG-WITHOUT-A-LOOSE-LEG", every != [] and orphan == [],
        f"{len(every)} flagged member(s) estate-wide, {len(orphan)} without a per-file target {orphan}")

    # --- 6. the mutant: remove the flag on a copy, the member falls back to bundle-only ---
    saved = sdc.CODE_TREES
    try:
        mutant = copy.deepcopy(saved)
        for t in mutant.values():
            for b in t.get("bundles", {}).values():
                for m in b["members"].values():
                    m.pop("distribution", None)
        sdc.CODE_TREES = mutant
        trig, loose, _ = route([FLAGGED[2]])
    finally:
        sdc.CODE_TREES = saved
    rec("MUTANT-FLAG-REMOVED-FREEZES", trig == [BUNDLE] and loose == [],
        f"flag removed on a copy -> triggered={trig} loose={loose}: the member is frozen out of its "
        f"loose leg again, so arm 1's result is caused by the flag")


def _report() -> int:
    _run_battery()
    n = sum(1 for _, v, _ in RESULTS if v == "PASS")
    print()
    print("=" * 80)
    print("SAFE-DEPLOY DISTRIBUTION-MEMBER BATTERY: %d/%d PASS (denominator %d)"
          % (n, len(RESULTS), len(RESULTS)))
    print("=" * 80)
    return 0 if n == len(RESULTS) else 1


def test_all_arms_pass():
    _run_battery()
    failed = [(t, d) for t, v, d in RESULTS if v != "PASS"]
    assert not failed, "arms failed (%d of %d): %s" % (len(failed), len(RESULTS), failed)


if __name__ == "__main__":
    sys.exit(_report())
