"""
comp_desc_sensitivity -- NFRA_TOOLUNIFY PRESENCE-IS-NOT-TRUTH, Phase 1 (LEAF).

WHAT THIS MEASURES
    For each unit in infra/system/scope_contract.json: does the `desc`'s CLAIM STRENGTH
    exceed the `check`'s ACTUAL SENSITIVITY? A check whose desc promises more than it
    tests is the defect, and it is invisible from either side alone.

WHAT THIS INSTRUMENT CAN AND CANNOT DO -- read before citing any number it prints.
    THE CLAIM CLASSIFIER IS LEXICAL. It matches WORDS, not meaning. It cannot read a
    desc and understand it. Specifically it CANNOT detect:
      - a desc that over-claims using vocabulary not in CLAIM_TRUTH below;
      - a desc that is literally accurate but MISLEADING in context;
      - whether the DOC the check points at is itself TRUE (that is the content plane,
        and no check in this register touches it -- see LIMITS, item 3);
      - the AGGREGATE over-claim (Phase 2): honest leaves rolling up into a verdict that
        asserts more than their conjunction supports.
    So a HONEST verdict from this tool means "no LEXICAL over-claim detected", NEVER
    "this unit's claim is true". That distinction is the entire subject of this build,
    and an instrument that blurred it would be the next instance of the class.

    Every run prints its own denominator, its own classifier basis, and this limit.
    If it ever stops doing that, it has become the thing it measures.

DESIGN CONSTRAINT (self-application, CTO~Z dispatch item 4)
    This module's own docstring is written to the standard it enforces: it states what
    the instrument DETECTS, not what it would like to be true. `desc_sensitivity` is a
    LEXICAL SCREEN, and it says so in-band on every run.

Author: 0.8.0_AE_CloudComp~B, 2026-07-25. Dispatch 1.0.0_SA_CTO~Z 20260725T171405Z.
Scope ruling 20260725T174332Z: Phase 1 (leaf) proceeds; Phase 2 (aggregate) needs
CTO~Z ratification before landing.
"""
from __future__ import annotations


import json
import os
import re
from typing import Any, Dict, List, Optional, Tuple

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CONTRACT = os.path.join(REPO, "infra", "system", "scope_contract.json")

# ---------------------------------------------------------------------------
# CHECK SENSITIVITY MODEL -- what each check type can ACTUALLY detect.
# Grounded in infra/system/system_parity.py run_check() at HEAD, read not assumed.
# Tier ordering is what the comparison uses; the prose is what a reader needs.
# ---------------------------------------------------------------------------
PRESENCE = "PRESENCE"   # existence of a file or a string. Content unexamined.
DERIVED = "DERIVED"     # a value computed at run time and compared to a source.

CHECK_SENSITIVITY: Dict[str, Tuple[str, str]] = {
    "file_exists": (
        PRESENCE,
        "existence at the active vintage ONLY -- an EMPTY file passes (exercised); "
        "no content is read",
    ),
    "grep_present": (
        PRESENCE,
        "one regex matched in >=1 of N named files; everything the pattern does not "
        "span is unexamined",
    ),
    "grep_absent": (
        PRESENCE,
        "a regex NOT found in N named files -- absence of a counter-string, which is "
        "NOT proof of the positive property",
    ),
    "glob_count_ge": (
        DERIVED,
        "a file COUNT at run time vs a floor; a floor is a regression detector, not "
        "validated coverage",
    ),
    "version_pin": (
        DERIVED,
        "a version DERIVED from source at run time vs its representation; sensitivity "
        "to ADD-without-bump is BORROWED from source discipline",
    ),
    "derived_count": (
        DERIVED,
        "a count DERIVED from source at run time vs its representation",
    ),
    "metric_current": (
        DERIVED,
        "live managed metrics compared for drift; non-numeric drift not observable",
    ),
    "system_current": (
        DERIVED,
        "compiler-generated snapshot staleness vs HEAD/TTL",
    ),
}

# ---------------------------------------------------------------------------
# CLAIM CLASSIFIER -- LEXICAL. The word lists ARE the instrument; they are exposed
# here rather than buried so a reader can audit what it actually keys on.
#
# CLAIM_PRESENCE: the desc claims something EXISTS / IS WRITTEN DOWN.
# CLAIM_TRUTH:    the desc claims something IS SO -- current, correct, in force,
#                 faithfully representing. A presence check cannot support these.
# ---------------------------------------------------------------------------
CLAIM_PRESENCE = [
    "present", "exists", "documented", "described", "referenced", "appears",
    "carries", "declared", "reachable", "named", "listed",
]
CLAIM_TRUTH = [
    "current", "not stale", "not drifted", "faithfully", "correct",
    "in sync", "is true", "represents", "represented",
    "enforced", "verified", "guaranteed",
]

# MEASURED FALSE-POSITIVE HISTORY (kept in-source; it is the instrument's calibration).
#
# The FIRST version of this classifier used bare substring matching and reported
# 5 OVER-CLAIM on the live register. HAND-ADJUDICATION FOUND 3 OF THE 5 WERE FALSE:
#   - "bound"  matched inside the ROLE NAME `BoundedDeriveReadOnly`  (inf-intraday-iam)
#   - "bound"  matched inside the compound `Opal-bound`              (ct-tenant-neutral-caveat)
#   - "live "  matched inside the phrase  `derive live`              (ont-archetypes-in-system)
# A 60% false-positive rate, on the instrument built to detect instruments that
# over-claim their own sensitivity. Recorded rather than quietly corrected, because
# a calibration history that is deleted once it is fixed teaches nobody.
#
# FIXES APPLIED: word-boundary matching (kills the `Bounded` class), and the removal of
# "derived"/"live"/"bound"/"actually"/"at run time" as TRUTH terms -- they occur too often
# as incidental parenthetical detail inside an otherwise honest desc to carry a verdict.
# RESIDUAL, NOT CLAIMED CLOSED: a lexical screen still cannot tell a desc's MAIN claim
# from a subordinate clause. Verdicts here are SCREENING OUTPUT FOR HUMAN ADJUDICATION,
# never a finished finding.
_WORD_RE = {w: re.compile(r"\b" + re.escape(w).replace(r"\ ", r"\s+") + r"\b", re.I)
            for w in CLAIM_PRESENCE + CLAIM_TRUTH}


def _classify_desc(desc: str) -> Tuple[str, List[str]]:
    """LEXICAL claim classification. Returns (class, matched_terms).

    WORD-BOUNDARY matched, not substring -- see the calibration note above for the
    measured false positives that forced this.

    TRUTH wins ties: a desc asserting both existence AND currency makes the stronger
    claim, and the stronger claim is the one a presence check fails to support.
    """
    truth_hits = [w for w in CLAIM_TRUTH if _WORD_RE[w].search(desc)]
    pres_hits = [w for w in CLAIM_PRESENCE if _WORD_RE[w].search(desc)]
    if truth_hits:
        return "TRUTH", truth_hits
    if pres_hits:
        return "PRESENCE", pres_hits
    return "UNCLASSIFIED", []


def load_units(path: Optional[str] = None) -> List[Dict[str, Any]]:
    """Every object carrying both an id and a check, at any nesting depth."""
    with open(path or CONTRACT, encoding="utf-8") as fh:
        doc = json.load(fh)

    out: List[Dict[str, Any]] = []

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            if "id" in node and "check" in node:
                out.append(node)
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(doc)
    return out


def assess(unit: Dict[str, Any]) -> Dict[str, Any]:
    """Score ONE unit. Verdict vocabulary is deliberately narrow.

    OVER-CLAIM  desc makes a TRUTH claim; the check only tests PRESENCE.
    ALIGNED     desc's claim class is supported by the check's sensitivity.
    UNDER-CLAIM desc says 'present' while the check actually DERIVES -- benign, and
                per the dispatch the MORE accurate direction. Reported, never a defect.
    UNKNOWN     unrecognised check type, or a desc the lexical screen cannot classify.
                FIRST-CLASS, never silently folded into ALIGNED.
    """
    ctype = unit.get("check", {}).get("type", "<none>")
    desc = unit.get("desc", "") or ""
    sens, sens_note = CHECK_SENSITIVITY.get(ctype, ("UNKNOWN", "unmodelled check type"))
    claim, hits = _classify_desc(desc)

    if sens == "UNKNOWN" or claim == "UNCLASSIFIED":
        verdict = "UNKNOWN"
    elif claim == "TRUTH" and sens == PRESENCE:
        verdict = "OVER-CLAIM"
    elif claim == "PRESENCE" and sens == DERIVED:
        verdict = "UNDER-CLAIM"
    else:
        verdict = "ALIGNED"

    return {
        "id": unit.get("id", "<no-id>"),
        "check_type": ctype,
        "check_sensitivity": sens,
        "sensitivity_note": sens_note,
        "desc": desc,
        "claim_class": claim,
        "claim_terms": hits,
        "verdict": verdict,
    }


def report(path: Optional[str] = None) -> Dict[str, Any]:
    units = load_units(path)
    rows = [assess(u) for u in units]
    counts: Dict[str, int] = {}
    for row in rows:
        counts[row["verdict"]] = counts.get(row["verdict"], 0) + 1
    presence_n = sum(1 for r in rows if r["check_sensitivity"] == PRESENCE)
    return {
        "denominator": len(rows),
        "presence_shaped": presence_n,
        "derived_shaped": sum(1 for r in rows if r["check_sensitivity"] == DERIVED),
        "counts": counts,
        "rows": rows,
    }


def render(res: Dict[str, Any]) -> str:
    n = res["denominator"]
    out: List[str] = []
    out.append("comp-desc-sensitivity -- LEAF desc-vs-check screen (NFRA_TOOLUNIFY Phase 1)")
    out.append("")
    out.append("  DENOMINATOR: %d unit(s) carrying a check in scope_contract.json" % n)
    out.append("  CHECK SHAPE: %d presence-shaped / %d derived-shaped"
               % (res["presence_shaped"], res["derived_shaped"]))
    order = ["OVER-CLAIM", "UNDER-CLAIM", "UNKNOWN", "ALIGNED"]
    tally = ", ".join("%s=%d" % (k, res["counts"].get(k, 0)) for k in order)
    out.append("  VERDICTS:    %s" % tally)
    out.append("")
    for row in sorted(res["rows"], key=lambda r: (order.index(r["verdict"])
                                                  if r["verdict"] in order else 99,
                                                  r["id"])):
        if row["verdict"] == "ALIGNED":
            continue
        out.append("  [%s] %s  (%s -> %s)"
                   % (row["verdict"], row["id"], row["check_type"], row["check_sensitivity"]))
        out.append("        desc:  %s" % row["desc"][:150])
        out.append("        claim: %s %s" % (row["claim_class"], row["claim_terms"][:4]))
        out.append("        check: %s" % row["sensitivity_note"])
    out.append("")
    out.append("  WHAT THIS RUN DID *NOT* MEASURE -- do not read past these:")
    out.append("    1. THE CLAIM CLASSIFIER IS LEXICAL. It matches words, not meaning. An")
    out.append("       ALIGNED verdict means NO LEXICAL OVER-CLAIM WAS DETECTED -- it does")
    out.append("       NOT mean the unit's claim is true.")
    out.append("    2. Classifier basis, auditable: %d presence terms / %d truth terms,"
               % (len(CLAIM_PRESENCE), len(CLAIM_TRUTH)))
    out.append("       WORD-BOUNDARY matched. Its own first version scored a MEASURED 60%")
    out.append("       false-positive rate by substring-matching inside proper nouns; see")
    out.append("       the calibration note in-source. VERDICTS HERE ARE SCREENING OUTPUT")
    out.append("       FOR HUMAN ADJUDICATION, never a finished finding.")
    out.append("    3. THE CONTENT PLANE IS UNTOUCHED. No check in this register tests")
    out.append("       whether the DOC it points at is TRUE. A doc can be present, its desc")
    out.append("       honest, this screen ALIGNED, and its content still false.")
    out.append("    4. THE AGGREGATE PLANE IS OUT OF SCOPE HERE (Phase 2, ratification-gated):")
    out.append("       honest leaves can still roll up into an over-claiming verdict.")
    return "\n".join(out)


def main(argv: Optional[List[str]] = None) -> int:
    import argparse
    ap = argparse.ArgumentParser(description="desc-vs-check sensitivity screen (LEXICAL)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--contract", default=None, help="path to scope_contract.json")
    args = ap.parse_args(argv)
    res = report(args.contract)
    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(render(res))
    # rc: 2 when a leaf over-claim is present, else 0. NOT a gate -- a report.
    return 2 if res["counts"].get("OVER-CLAIM", 0) else 0


if __name__ == "__main__":
    raise SystemExit(main())
