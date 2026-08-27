#!/usr/bin/env python
"""ACCEPTANCE GATE for the four-postulate record remedy (ISCK pass finding F3).

Section 3 of ISCK_CONTRACT.md declares that every enum record carries five things: domain, MECE,
grain, intent, state-coherence. This gate measures whether each record CARRIES ALL FIVE and fails
if any does not.

STOP: READ THIS LIMIT BEFORE QUOTING ANY NUMBER THIS TOOL PRINTS.
    THIS PROBE READS LABELS, NOT REASONING. An author can satisfy a postulate substantively
    without writing its name, so a record scored INCOMPLETE here is NOT proven unconsidered -- it
    is proven UNCHECKABLE BY A REVIEWER, which is the Rule 24 bar: a proposal arrives WITH its
    four-postulate record. The number is a LEGIBILITY count, never a quality count. Reporting it
    as one manufactures the confident-wrong figure this pass exists to catch, so the tool prints
    this limit on every run, above the number.

Origin: 2 of 10 records complete at v0 @8ba18439dd (2.0.0_SA_COO~X, adversarial pass round 1,
finding F3 -- UPHELD; v0.1 remedy gives all records the full five-label form).

Usage:
    check_postulate_labels.py [path/to/ISCK_CONTRACT.md]   exit 0 = every record complete
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DOC = os.path.join(HERE, "ISCK_CONTRACT.md")

# Matched CASE-INSENSITIVELY at the call site. v0 wrote "domain:", v0.1 writes "DOMAIN:".
# A case-sensitive gate reports a fully compliant document as fully non-compliant, and that
# number reads exactly like a real finding. This file's positive control caught precisely that
# during the v0.1 acceptance run -- it refused to publish 0-of-13 and said to suspect the
# pattern set instead. The control is the reason the wrong number was never reported.
POSTULATES = (
    ("domain", r"\bdomain\s*:"),
    ("MECE", r"\bMECE\b"),
    ("grain", r"\bgrain\s*:"),
    ("intent", r"\bintent\s*:"),
    ("state", r"\bstate(?:[-\s]coherence)?\s*:"),
)

LIMIT = (
    "LIMIT: this gate reads LABELS, not reasoning. An INCOMPLETE record is UNCHECKABLE, not\n"
    "       proven unconsidered. The count is a LEGIBILITY count -- never quote it as a quality\n"
    "       count. Rule 24's bar is that a proposal ARRIVES WITH its record."
)


def parse_records(text):
    """Return [(enum_name, body)] for each enum record in section 3.

    TWO SHAPES ARE ACCEPTED, because the doctrine changed shape between v0 and v0.1 and a parser
    that returns 0 on a renamed heading emits a FALSE ZERO -- byte-identical to a document with
    no records at all:
      v0.1   "### 3.N `enum_name` - values"    one subsection per record
      v0     "- **`enum_name`** values"        one bullet per record
    """
    m = re.search(r"\n## 3\.[^\n]*\n", text)
    if not m:
        return []
    sec = text[m.end():]
    nxt = re.search(r"\n## 4\.", sec)
    if nxt:
        sec = sec[:nxt.start()]

    recs = re.findall(r"\n### 3\.\d+\s+`([a-z_.]+)`(.*?)(?=\n### 3\.\d+|\Z)", sec, re.S)
    if recs:
        return [(n, b) for n, b in recs if b.strip()]

    return re.findall(r"\n- \*\*`([a-z_.]+)`\*\*(.*?)(?=\n- \*\*|\Z)", sec, re.S)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DOC
    if not os.path.exists(path):
        print("ERROR: contract doc not found: %s" % path)
        return 2
    with open(path, "r", encoding="utf-8") as fh:
        records = parse_records(fh.read())

    if not records:
        # A zero here is byte-identical to "the section was renamed". Never report it as a result.
        print("ERROR: parsed 0 enum records -- section 3 missing or restructured, NOT a clean run")
        return 2

    print("FOUR-POSTULATE LABEL GATE -- %s" % os.path.basename(path))
    print(LIMIT)
    print("")
    head = "%-30s" % "enum record" + "".join("%8s" % n for n, _ in POSTULATES)
    print(head)
    print("-" * len(head))

    incomplete = []
    for name, body in records:
        cells, missing = [], []
        for label, pat in POSTULATES:
            hit = bool(re.search(pat, body, re.IGNORECASE))
            cells.append("%8s" % ("ok" if hit else "MISS"))
            if not hit:
                missing.append(label)
        print("%-30s%s" % (name, "".join(cells)))
        if missing:
            incomplete.append((name, missing))

    complete = len(records) - len(incomplete)
    print("")
    print("DENOMINATOR: %d enum records parsed from section 3" % len(records))
    print("COMPLETE (all five labels): %d of %d" % (complete, len(records)))

    # POSITIVE CONTROL. If NO record scores all five, the pattern set is likelier broken than
    # every record being defective. A uniform result across a whole set is an instrument
    # signature, not a defect signature -- and a gate that can only say MISS is not a gate.
    if complete == 0:
        print("ERROR: no record scored all five -- suspect the PATTERN SET, not the document.")
        print("       A uniform result across a whole set is an instrument signature.")
        return 2

    if incomplete:
        print("")
        for name, missing in incomplete:
            print("FAIL: %-28s missing label(s): %s" % (name, ", ".join(missing)))
        print("")
        print("GATE FAILED: %d record(s) are not reviewer-checkable." % len(incomplete))
        return 1

    print("OK: every enum record carries all five declared postulate labels.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
