#!/usr/bin/env python3
"""Mutation battery for the substrate_side / side_status split.

WHY THIS EXISTS: on the live graph, `side_status` is 100% RESOLVED, because ZERO nodes currently
carry a null `layer` (measured 2026-08-07). So PARTIAL and UNRESOLVED had NEVER FIRED.

>> A BRANCH THAT HAS NEVER FIRED IS NOT A PROVEN CONTROL -- AND PARTIAL ONLY EVER FIRES THE DAY A
MEMBER'S LAYER GOES MISSING, WHICH IS PRECISELY THE DAY IT HAS TO WORK. <<

The live data cannot exercise it, so synthetic inputs must. Same standard applied to
`3.0.0_SA_CVO~B`'s batteries this session: a control that only demonstrates it can PASS has not been
shown it can FAIL.

Run: python test_substrate_side.py    (exit 0 = all branches discriminate)
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c2_individuate as C  # noqa: E402


def classify(layers):
    """The exact derivation from the emitter, over supplied layers."""
    sides, unres = set(), 0
    for lay in layers:
        s = C.side_of(lay)
        if s:
            sides.add(s)
        else:
            unres += 1
    status = ("RESOLVED" if unres == 0
              else "UNRESOLVED" if unres == len(layers) else "PARTIAL")
    return sorted(sides), status, unres


CASES = [
    # name                       layers                    want_sides                want_status
    ("all backend",              ["aws", "pipeline"],      ["BACKEND"],              "RESOLVED"),
    ("cross-side (serve seam)",  ["aws", "portal"],        ["BACKEND", "FRONTEND"],  "RESOLVED"),
    ("one member unmapped",      ["aws", None],            ["BACKEND"],              "PARTIAL"),
    ("one member semctl",        ["portal", "semctl"],     ["FRONTEND"],             "PARTIAL"),
    ("all unmapped",             [None, None],             [],                       "UNRESOLVED"),
    ("UNKNOWN layer value",      ["aws", "some-new-layer"], ["BACKEND"],             "PARTIAL"),
    ("knowledge plane",          ["ms"],                   ["KNOWLEDGE"],            "RESOLVED"),
]


def main() -> int:
    ok = True
    for name, layers, want_sides, want_status in CASES:
        sides, status, unres = classify(layers)
        good = (sides == want_sides and status == want_status)
        ok = ok and good
        print("  %s  %-24s sides=%-24s status=%-11s unresolved=%d"
              % ("PASS" if good else "FAIL", name, sides, status, unres))
    print()
    if ok:
        print("  ALL THREE STATUS VALUES FIRE -- the two-field split discriminates.")
        print("  Two properties worth naming, both load-bearing:")
        print("   * an UNKNOWN layer -> PARTIAL, never silently BACKEND. A new substrate appearing")
        print("     in the graph cannot be misfiled into an existing side without being counted.")
        print("   * `ms` -> KNOWLEDGE/RESOLVED. KNOWLEDGE is unreachable TODAY (no ms detector), but")
        print("     the mechanism is proven ready: the day an ms detector lands, the side derives")
        print("     correctly with NO code change. Its emptiness is a coverage fact, not a bug.")
    else:
        print("  *** A BRANCH DOES NOT BEHAVE AS SPECIFIED ***")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
