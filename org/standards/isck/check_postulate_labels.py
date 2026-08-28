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
    """Return (records, unparsed_headers, header_count) for section 3.

    records          [(enum_name, body)] -- one per parseable record
    unparsed_headers [header_line]       -- every "### 3.N" subsection whose name the record
                                            regex could NOT capture. NEVER silently dropped.
    header_count     int                 -- the census of "### 3.N" subsections, taken BEFORE
                                            any name pattern is applied: the denominator that
                                            cannot shrink when a name is unusual.

    TWO SHAPES ARE ACCEPTED, because the doctrine changed shape between v0 and v0.1 and a parser
    that returns 0 on a renamed heading emits a FALSE ZERO -- byte-identical to a document with
    no records at all:
      v0.1   "### 3.N `enum_name` - values"    one subsection per record
      v0     "- **`enum_name`** values"        one bullet per record

    R3-CTO-1 (2026-08-28, 1.0.0_SA_CTO~X self-found): the v0.1 name capture was `[a-z_.]+`, so a
    record named `source_frontier.entries[].availability` matched nothing, findall skipped the
    whole subsection, and the gate printed 22 of 22 COMPLETE while the document held 23 -- a
    record ABSENT FROM THE DENOMINATOR with a clean pass on top. The remedy is structural, not a
    wider character class: census the headers first, then any header the name capture cannot
    parse is returned by name and the caller FAILS on it. A wider class alone would move the
    blind spot to the next unusual name.
    """
    m = re.search(r"\n## 3\.[^\n]*\n", text)
    if not m:
        return [], [], 0, []
    sec = text[m.end():]
    nxt = re.search(r"\n## 4\.", sec)
    if nxt:
        sec = sec[:nxt.start()]

    # Census FIRST: every subsection, with its body, before any name pattern is applied.
    subsections = re.findall(r"\n(### 3\.\d+[^\n]*)(.*?)(?=\n### 3\.\d+|\Z)", sec, re.S)
    header_count = len(subsections)

    if subsections:
        parsed, unparsed, non_record = [], [], []
        for header, body in subsections:
            nm = re.match(r"### 3\.\d+\s+`([^`\n]+)`", header)
            if nm and body.strip():
                parsed.append((nm.group(1), body))
                continue
            # No backticked name. Two things look like this and they must not be conflated:
            #   a RECORD the parser cannot name  -> its body carries postulate labels -> UNPARSED
            #   an explanatory subsection        -> no labels at all                 -> NON-RECORD
            # Only the first is the R3-CTO-1 class. Both are printed; only the first fails.
            if any(re.search(pat, body, re.IGNORECASE) for _, pat in POSTULATES):
                unparsed.append(header)
            else:
                non_record.append(header)
        return parsed, unparsed, header_count, non_record

    bullets = re.findall(r"\n- \*\*`([^`\n]+)`\*\*(.*?)(?=\n- \*\*|\Z)", sec, re.S)
    return bullets, [], len(bullets), []


def _ascii(s):
    """Gate output stays ASCII (CLAUDE.md sec 4) even when a header carries an em-dash."""
    return s.encode("ascii", "replace").decode("ascii")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DOC
    if not os.path.exists(path):
        print("ERROR: contract doc not found: %s" % path)
        return 2
    with open(path, "r", encoding="utf-8") as fh:
        records, unparsed, header_count, non_record = parse_records(fh.read())

    if not records:
        # A zero here is byte-identical to "the section was renamed". Never report it as a result.
        print("ERROR: parsed 0 enum records -- section 3 missing or restructured, NOT a clean run")
        return 2

    print("FOUR-POSTULATE LABEL GATE -- %s" % os.path.basename(path))
    print(LIMIT)
    print("")
    print("HEADER CENSUS: %d '### 3.N' subsections = %d record(s) PARSED + %d NON-RECORD"
          " (no labels, listed) + %d UNPARSED (labels present, name not captured)"
          % (header_count, len(records), len(non_record), len(unparsed)))
    for h in non_record:
        print("INFO: non-record subsection (carries no postulate label; not counted): %s" % _ascii(h))
    for h in unparsed:
        print("WARN: header NOT PARSED -> a RECORD absent from every count below: %s" % _ascii(h))
    if unparsed:
        # An unparsed record is the uncheckable case this gate exists to refuse. Fail on it
        # BEFORE scoring, so the table below is never read as covering the document.
        print("GATE FAILED: %d section-3 header(s) could not be parsed into a record -- the"
              " denominator below UNDERSTATES the document. Rename or fix the header, or widen"
              " the parser WITH a self-test arm for the new shape." % len(unparsed))
        return 1
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


def _self_test():
    """Both directions, on synthetic documents. Every arm prints its observation beside its
    expectation; the run exits 0 only when all arms hold. The arms are transcribed from the
    R3-CTO-1 finding, not from this implementation: (1) a bracketed name is COUNTED and NAMED,
    never dropped; (2) a clean document still parses every header; (3) the count is DERIVED
    from the header census, never from the name pattern; (4) the v0 bullet shape still parses."""
    rec = "\nDOMAIN: x\nMECE: y\ngrain: z\nintent: w\nstate-coherence: v\n"
    clean = "\n## 3. Records\n" + "".join("\n### 3.%d `rec_%d` - values%s" % (i, i, rec) for i in (1, 2, 3)) + "\n## 4. Next\n"
    bracketed = clean.replace("### 3.2 `rec_2`", "### 3.2 `source_frontier.entries[].availability`")
    v0 = "\n## 3. Records\n" + "".join("\n- **`rec_%d`** values%s" % (i, rec) for i in (1, 2)) + "\n## 4. Next\n"

    arms = []
    r, u, h, nr = parse_records(clean)
    arms.append(("clean doc: 3 headers, 3 parsed, 0 unparsed, 0 non-record", (h, len(r), len(u), len(nr)), (3, 3, 0, 0)))
    r, u, h, nr = parse_records(bracketed)
    arms.append(("bracketed name: header census still 3 (derived, not name-pattern)", h, 3))
    arms.append(("bracketed name: parsed as a record (wide capture), not dropped", len(r), 3))
    arms.append(("bracketed name: 0 unparsed under the wide capture", len(u), 0))
    hostile = clean.replace("### 3.2 `rec_2`", "### 3.2 rec_2_no_backticks")
    r, u, h, nr = parse_records(hostile)
    arms.append(("un-backticked RECORD (labels in body): census 3, parsed 2, UNPARSED 1 -- NAMED not dropped", (h, len(r), len(u)), (3, 2, 1)))
    arms.append(("un-backticked RECORD: the WARN carries the header text", "rec_2_no_backticks" in (u[0] if u else ""), True))
    prose = clean.replace("\n### 3.2 `rec_2` - values" + rec, "\n### 3.2 The five axes (explanatory prose)\nNo labels live here.\n")
    r, u, h, nr = parse_records(prose)
    arms.append(("NON-RECORD subsection (no labels): census 3, parsed 2, unparsed 0, non-record 1", (h, len(r), len(u), len(nr)), (3, 2, 0, 1)))
    arms.append(("NON-RECORD subsection is NAMED in the census, not dropped", "explanatory prose" in (nr[0] if nr else ""), True))
    r, u, h, nr = parse_records(v0)
    arms.append(("v0 bullet shape still parses: 2 records", (len(r), len(u)), (2, 0)))
    r, u, h, nr = parse_records("\n## 2. Nothing here\n")
    arms.append(("no section 3: (0 records, 0 unparsed, 0 headers)", (len(r), len(u), h), (0, 0, 0)))

    bad = 0
    for label, got, want in arms:
        ok = got == want
        bad += 0 if ok else 1
        print("  [%s] %s: %r (expect %r)" % ("OK" if ok else "FAIL", label, got, want))
    print("SELF-TEST: %d of %d arms hold" % (len(arms) - bad, len(arms)))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        raise SystemExit(_self_test())
    raise SystemExit(main())
