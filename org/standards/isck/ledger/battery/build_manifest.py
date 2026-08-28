#!/usr/bin/env python
"""WP3 AC5 -- GENERATE the battery manifest from the census, EXPANDED and keyed by ARM ID.

GENERATED, NEVER TRANSCRIBED. The manifest is written from arm_census.py's output at a cited
commit, with every template expanded from the design's OWN tables at that same commit. A
hand-copied manifest beside a derived census is the typed-beside-derived defect one file over
(R3-CRO-21 / R3-DT-8).

-- WHY THIS FILE WAS REWRITTEN IN WAVE 2 (issuer 105154Z, on CVO~X's HOLD 105059Z). Wave 1's
manifest carried 190 entries and 126 DISTINCT ids because it stored the design's TEMPLATE STRINGS
verbatim: `L-02-unresolved-<record>.<field>` thirty times, its accept twin thirty times, and
`L-05-<axis>-authored-agrees-accepted` five times. Sixty-one entries, three addressable ids. The
census was right -- it counts ARMS in the TEXT, and `x N` expands to N by the published predicate --
but a manifest's job is IDS, and 61 of them were never minted. The runner addresses arms by id, so
`ran 190 of 190` was unreachable by construction. The generator, not the census, was the defect.

THREE TEMPLATE CLASSES, all expanded here from the design at the pin, none typed:
  1. row 2   `L-02-unresolved-<record>.<field>` / `-resolved-...-accepted` over sec 2d's 30
             (record, field) reference rows, read by TABLE SHAPE from sec 2d at the pin.
  2. row 5   `L-05-<axis>-authored-agrees-accepted` x5 over the five DERIVABLE axes, read from
             row 5's OWN reject ids at the pin (never a typed axis list).
  3. row 5   four reject ids ELIDED in the design with a non-ASCII ellipsis --
             `L-05-entity_binding.status-<ellipsis>` and three siblings. An id ending in an
             elision is not an id, and non-ASCII is banned in production artifacts (CLAUDE.md
             sec 4). The elision's expansion is PROVEN by the first member of its own list,
             `L-05-entity.current_status-authored-vs-derived`, so the suffix is read from that
             member rather than assumed. Found while building the generator, not by a review.

ARM ID IS THE KEY, AND A SHARED ARM IS ONE ARM (issuer 105154Z, on sec 3's published predicate
"a token cited twice is one arm"). Two arms are cited by two rows each --
`L-05-voided-decommission-does-not-retire-accepted` (rows 5, 13) and
`L-04-voided-close-then-replacement-accepted` (rows 4, 13) -- because one test discharges two
responsibilities. They are NOT minted as row-qualified twins: that would fake two tests out of one.
So the manifest carries ARMS (each with the rows it discharges) and reports two different numbers
that must never be conflated: DISTINCT ARMS (what the runner executes) and ROW CITATIONS (how many
row-obligations those arms discharge).

THE CONTROLS, and each can FAIL -- the uniqueness control is the one wave 1 lacked, and its absence
is exactly why a repetition survived where an absence would not have (`--plant-missing` plants an
ABSENCE; this defect was a REPETITION, and no control in wave 1 could see it):
  U1  no arm id is cited twice by the SAME row          (a real duplicate)
  U2  no arm id carries two different kinds             (accept and reject cannot be one arm)
  U3  no arm id still contains a template metacharacter (`<` or `>`) -- an unexpanded template
  U4  every arm id is ASCII                             (CLAUDE.md sec 4)
`--check` re-derives from the census + expansion at the manifest's own commit and reports what it
COUNTED. `--plant-duplicate <id>` injects a same-row repetition to prove U1 discriminates.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CENSUS = os.path.join(HERE, "arm_census.py")
MANIFEST = os.path.join(HERE, "MANIFEST.json")
DESIGN = "org/standards/isck/WP3_LEDGER_DESIGN.md"

BS = chr(92)
ROW_SPLIT = re.compile('(?<!' + re.escape(BS) + ')' + re.escape('|'))
TICKED = re.compile('`([^`]+)`')
REF_TEMPLATE = re.compile(r'^L-02-(unresolved|resolved)-<record>\.<field>')
AXIS_TEMPLATE = "L-05-<axis>-authored-agrees-accepted"
AXIS_FROM_ID = re.compile(r'^L-05-([a-z_]+\.[a-z_]+)-')


def _blob(commit, path):
    return subprocess.check_output(["git", "show", "%s:%s" % (commit, path)],
                                   stderr=subprocess.PIPE).decode("utf-8", "replace")


def census_at(commit):
    out = subprocess.check_output([sys.executable, CENSUS, commit], stderr=subprocess.PIPE)
    return json.loads(out.decode("utf-8", "replace"))


def reference_rows_at(commit):
    """sec 2d's (record, field) pairs, read BY TABLE SHAPE at the pin -- never a typed list.

    A data row is a pipe row whose first two cells are each a single backticked token. That
    excludes the header (`record | field | ...`, unticked) and the separator. Cells are split on
    UNESCAPED pipes only: the target-class column contains `a \\| b \\| c` unions, and a naive
    split shreds them (the R4-DT-4 escaped-pipe class, found in this same document).
    """
    text = _blob(commit, DESIGN)
    body = text.split("## 2d.")[1]
    cut = re.search(r'\n#{2,} ', body)
    body = body[:cut.start()] if cut else body
    pairs = []
    for line in body.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in ROW_SPLIT.split(line)]
        if len(cells) < 4:
            continue
        rec, fld = TICKED.findall(cells[1]), TICKED.findall(cells[2])
        if len(rec) == 1 and len(fld) == 1:
            pairs.append((rec[0], fld[0]))
    return pairs


def derivable_axes(reject_ids):
    """The five derivable axes, read from row 5's OWN reject ids -- not a typed axis list."""
    axes = []
    for i in reject_ids:
        m = AXIS_FROM_ID.match(i)
        if m and m.group(1) not in axes:
            axes.append(m.group(1))
    return axes


def elision_suffix(reject_ids):
    """The suffix the design ELIDES, proven by the one member that spells it out."""
    for i in reject_ids:
        m = AXIS_FROM_ID.match(i)
        if m and i.isascii():
            return i[len(m.group(0)):]
    return None


def expand(census, commit):
    """Every template expanded from the design's own tables at `commit`. Returns citations."""
    refs = reference_rows_at(commit)
    citations, notes = [], {"reference_rows": len(refs), "expansions": {}}
    for row, v in sorted(census["rows"].items(), key=lambda kv: int(kv[0])):
        axes = derivable_axes(v["reject_ids"])
        suffix = elision_suffix(v["reject_ids"])
        for kind in ("reject", "accept"):
            out = []
            for arm in v["%s_ids" % kind]:
                m = REF_TEMPLATE.match(arm)
                if m:
                    if any(a[0] == m.group(1) for a in out):
                        continue                       # the template expands ONCE, not per copy
                    tail = "-accepted" if kind == "accept" else ""
                    out += [(m.group(1), "L-02-%s-%s.%s%s" % (m.group(1), r, f, tail))
                            for r, f in refs]
                    notes["expansions"]["row%s.%s.reference" % (row, kind)] = len(refs)
                elif arm == AXIS_TEMPLATE:
                    if any(a[0] == "axis" for a in out):
                        continue
                    out += [("axis", "L-05-%s-authored-agrees-accepted" % a) for a in axes]
                    notes["expansions"]["row%s.%s.axis" % (row, kind)] = len(axes)
                elif not arm.isascii() and suffix:
                    m2 = AXIS_FROM_ID.match(arm)
                    out.append(("elided", "L-05-%s%s" % (m2.group(1), suffix)))
                    notes["expansions"].setdefault("row%s.%s.elided" % (row, kind), 0)
                    notes["expansions"]["row%s.%s.elided" % (row, kind)] += 1
                else:
                    out.append((None, arm))
            citations += [(arm_id, row, kind) for _src, arm_id in out]
    return citations, notes


def controls(citations):
    """U1-U4. Each returns a list of violations; each can fail."""
    seen_row, kinds, bad = {}, {}, {"U1": [], "U2": [], "U3": [], "U4": []}
    for arm_id, row, kind in citations:
        key = (arm_id, row)
        if key in seen_row:
            bad["U1"].append("%s cited twice by row %s" % (arm_id, row))
        seen_row[key] = True
        if arm_id in kinds and kinds[arm_id] != kind:
            bad["U2"].append("%s is both %s and %s" % (arm_id, kinds[arm_id], kind))
        kinds[arm_id] = kind
        if "<" in arm_id or ">" in arm_id:
            bad["U3"].append(arm_id)
        if not arm_id.isascii():
            bad["U4"].append(arm_id)
    return bad


def assemble(citations):
    arms = {}
    for arm_id, row, kind in citations:
        a = arms.setdefault(arm_id, {"kind": kind, "rows": []})
        if row not in a["rows"]:
            a["rows"].append(row)
    for a in arms.values():
        a["rows"].sort(key=int)
    return arms


def report(citations, notes, label):
    bad = controls(citations)
    arms = assemble(citations)
    shared = {i: a["rows"] for i, a in arms.items() if len(a["rows"]) > 1}
    print("%s -- COUNTED %d distinct arms / %d row citations (%d arms cited by 2 rows)"
          % (label, len(arms), len(citations), len(shared)))
    print("   expansions: sec 2d reference rows %d; %s"
          % (notes["reference_rows"], json.dumps(notes["expansions"], sort_keys=True)))
    for i, rows in sorted(shared.items()):
        print("   SHARED ARM (one test, two responsibilities): %s -> rows %s" % (i, ",".join(rows)))
    ok = True
    for c in ("U1", "U2", "U3", "U4"):
        if bad[c]:
            ok = False
            for v in bad[c]:
                print("   %s VIOLATION: %s" % (c, v))
    print("   controls U1 duplicate-citation, U2 kind-collision, U3 unexpanded-template, "
          "U4 non-ascii: %s" % ("all clear" if ok else "FAILED"))
    return ok, arms


def build(commit):
    census = census_at(commit)
    citations, notes = expand(census, commit)
    ok, arms = report(citations, notes, "BUILD at %s" % commit)
    if not ok:
        print("RESULT: INVALID -- refusing to write a manifest that fails its own controls")
        return False
    doc = {
        "$comment": ("GENERATED by build_manifest.py from arm_census.py plus the design's own "
                     "tables at derived_at. Never hand-edit: re-run it. Keyed by ARM ID; an arm "
                     "cited by two rows is ONE arm (sec 3: 'a token cited twice is one arm'). "
                     "Every count a consumer needs is COUNTED from arms, never stored."),
        "derived_at": commit,
        "source": "%s sec 3 (arms), sec 2d (reference rows), row 5 reject ids (axes)" % DESIGN,
        "predicate": ("every backtick L- token in a row is one arm; `x N` expands to N from the "
                      "design's own table at the pin; a token cited twice is ONE arm carrying "
                      "both rows; rows split on UNESCAPED pipes only"),
        "arms": arms,
    }
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print("WROTE %s" % os.path.relpath(MANIFEST))
    return True


def check(plant_duplicate=None):
    with open(MANIFEST, "r", encoding="utf-8") as fh:
        doc = json.load(fh)
    commit = doc["derived_at"]
    citations, notes = expand(census_at(commit), commit)
    if plant_duplicate:
        row = doc["arms"][plant_duplicate]["rows"][0]
        kind = doc["arms"][plant_duplicate]["kind"]
        citations.append((plant_duplicate, row, kind))
    ok, arms = report(citations, notes, "CHECK at %s" % commit)
    stored = doc["arms"]
    drift = sorted(set(stored) ^ set(arms))
    if drift:
        ok = False
        for i in drift[:10]:
            print("   DRIFT between the stored manifest and a fresh derivation:", i)
    print("   stored arms %d; freshly derived %d; drift %d" % (len(stored), len(arms), len(drift)))
    print("RESULT:", "VALID" if ok else "INVALID")
    return ok


def main():
    if "--check" in sys.argv:
        plant = None
        if "--plant-duplicate" in sys.argv:
            plant = sys.argv[sys.argv.index("--plant-duplicate") + 1]
            print("NEGATIVE CONTROL: citing %r twice from one row -- U1 MUST report INVALID, or "
                  "the uniqueness control cannot discriminate (this is the control wave 1 "
                  "lacked: --plant-missing plants an ABSENCE, and the defect was a REPETITION)."
                  % plant)
        sys.exit(0 if check(plant) else 1)
    sys.exit(0 if build(sys.argv[1]) else 1)


if __name__ == "__main__":
    main()
