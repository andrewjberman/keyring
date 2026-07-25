"""
comp_aggregate_honesty -- NFRA_TOOLUNIFY PRESENCE-IS-NOT-TRUTH, Phase 2 (AGGREGATE).

*** PROPOSAL ONLY. THIS MODULE LANDS NOTHING. ***
CTO~Z ruling 20260725T182057Z: "You may build a changed roll-up verdict string and put it
in front of me. You may not land it." This module RENDERS the current roll-up phrasing and a
PROPOSED replacement side by side, with each clause's falsifier named. It does NOT modify
system_parity.py and is not wired into any gate.

THE SITE
    Phase 1 measured the leaf: 16/22 checks presence-shaped (73%), but only ~9% of DESCS
    over-claim. Most leaves are honest. The over-claim is at AGGREGATION:

      system_parity.py:13   parity = (units mechanically PRESENT + CURRENT) / (mechanical units)
      system_parity.py:499  "DOMAIN: %s -- parity %s"

    The DEFINITION fuses PRESENT with CURRENT, and the RENDERED WORD is "parity". A reader
    hears "the representation matches the estate." What was measured is "N of M checks passed,
    and most of those checks only asked whether a file or a string exists."

    Nothing at the leaf is lying. The conjunction of honest leaves is being NAMED as something
    stronger than the conjunction supports. That is why an honest desc cannot fix it.

CTO~Z'S BINDING CONSTRAINT ON ANY PROPOSAL
    "The new string must be FALSIFIABLE BY THE REGISTER ITSELF. If the roll-up can say something
    no check in the register can contradict, you have rebuilt the defect at a higher altitude
    with better wording."

    So every clause below names the observation that would falsify it. A clause with no
    falsifier does not ship.

Author: 0.8.0_AE_CloudComp~B, 2026-07-25.
"""
from __future__ import annotations


import os
import sys
from typing import Any, Dict, List

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import comp_desc_sensitivity as ds  # noqa: E402


def measure() -> Dict[str, Any]:
    """Everything the proposed string asserts, derived at run time. No frozen digits."""
    res = ds.report()
    rows = res["rows"]
    content_reading = [r for r in rows if r["check_sensitivity"] not in (ds.PRESENCE, ds.DERIVED)]
    return {
        "total": res["denominator"],
        "presence_only": res["presence_shaped"],
        "derived": res["derived_shaped"],
        "content_reading": len(content_reading),
        "disclosed": res["counts"].get("DISCLOSED", 0),
        "over_claim": res["counts"].get("OVER-CLAIM", 0),
    }


CURRENT = '"DOMAIN: {domain} -- parity {pct}% ({p}/{t} mechanical units)"'

PROPOSED = (
    '"DOMAIN: {domain} -- CHECKS PASSING {p}/{t} ({pct}%); {k} of {t} checks in this\n'
    '   register are PRESENCE-ONLY (file or string existence, content unread).\n'
    '   THIS IS A CHECK-PASS RATE, NOT A MEASUREMENT OF PARITY WITH THE ESTATE."'
)

# Each clause -> the observation that would falsify it, IN THE REGISTER.
FALSIFIERS: List[Dict[str, str]] = [
    {
        "clause": "CHECKS PASSING p/t",
        "falsifier": "recount PASS verdicts over the contract's units; a mismatch falsifies it",
    },
    {
        "clause": "k of t checks are PRESENCE-ONLY",
        "falsifier": "inspect each unit's check.type against the sensitivity model; "
                     "a presence-shaped type counted as derived (or vice versa) falsifies it",
    },
    {
        "clause": "content unread / NOT a measurement of parity",
        "falsifier": "add ANY check type to run_check() that reads document CONTENT and "
                     "compares it to the estate -- this clause becomes FALSE the moment such a "
                     "check exists, and the register itself is where it would appear",
    },
]


def render() -> str:
    m = measure()
    t, k = m["total"], m["presence_only"]
    out: List[str] = []
    out.append("comp-aggregate-honesty -- PHASE 2 PROPOSAL (NOT LANDED, ratification-gated)")
    out.append("")
    out.append("  MEASURED AT RUN TIME (no frozen digits):")
    out.append("    units .................. %d" % t)
    out.append("    presence-only checks ... %d (%.0f%%)" % (k, 100.0 * k / t if t else 0))
    out.append("    derived checks ......... %d" % m["derived"])
    out.append("    content-reading checks . %d   <-- the number that makes 'parity' sayable"
               % m["content_reading"])
    out.append("    descs self-disclosing .. %d" % m["disclosed"])
    out.append("")
    out.append("  CURRENT ROLL-UP STRING (system_parity.py:499):")
    out.append("    " + CURRENT)
    out.append("    READING IT INVITES: 'the representation matches the estate.'")
    out.append("    WHAT IT MEASURED:   'N of M checks passed; %d of %d asked only whether a"
               % (k, t))
    out.append("                         file or string exists.'")
    out.append("")
    out.append("  PROPOSED REPLACEMENT:")
    for line in PROPOSED.split("\n"):
        out.append("    " + line)
    out.append("")
    out.append("  FALSIFIABLE BY THE REGISTER ITSELF (CTO~Z's binding constraint):")
    for f in FALSIFIERS:
        out.append("    - %s" % f["clause"])
        out.append("        falsified by: %s" % f["falsifier"])
    out.append("")
    out.append("  THE LOAD-BEARING CLAUSE is the third one, and it is why this is a proposal")
    out.append("  and not a wording tweak: TODAY content-reading checks = %d. If that stays 0,"
               % m["content_reading"])
    out.append("  the register CANNOT support the word 'parity' at any percentage -- and the")
    out.append("  honest roll-up is a check-pass rate. If someone later adds a content-reading")
    out.append("  check, the clause goes false and the register itself says so. That is the")
    out.append("  difference between a caveat and a falsifiable claim.")
    out.append("")
    out.append("  WHAT THIS PROPOSAL DOES NOT DO:")
    out.append("    - it does not change system_parity.py (ratification-gated, CTO~Z 182057Z);")
    out.append("    - it does not claim the current number is WRONG. The checks that passed")
    out.append("      really did pass. It claims the number is MIS-NAMED;")
    out.append("    - it does not touch the leaf descs (Phase 1, landed @3272197a9).")
    return "\n".join(out)


def main() -> int:
    print(render())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
