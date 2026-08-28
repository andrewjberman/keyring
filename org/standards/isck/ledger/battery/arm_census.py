#!/usr/bin/env python
"""WP3-1 AC1/AC2 -- the sec-3 arm CENSUS and PAIRING, derived at a CITED COMMIT.

WHY THIS EXISTS AS A FILE RATHER THAN A ONE-OFF: AC5's manifest, AC2's pairing and AC3's carrier
dependency all consume this census. A census error propagates into three criteria, so it is built
once, controlled, and re-run -- not retyped per criterion.

THE PREDICATE (DT~X/CRO~X, agreed at four pins): every backtick `L-...` token in a row is ONE arm;
`x N` after a token expands it to N; a token cited twice in the same row counts ONCE. Column 4 is
the reject set, column 5 the accept set.

-- NO TYPED COUNT ANYWHERE (R3-CRO-21 / R3-DT-8, WP3-mech-3). Every number this file emits is
counted from the parsed rows at run time. It prints what it counted.

-- ROWS ARE SPLIT ON UNESCAPED PIPES ONLY. An escaped pipe inside a cell shifts a naive split and
silently moves arms between columns -- the defect CTO~X hit pre-commit and that this seat and
CTO~X both carried until the fifth design pin. The split pattern is built from chr(92) so no
shell, heredoc or editor can eat the escape on its way here.

-- THE SLICE IS BOUNDED AT THE NEXT HEADING (R4-DT-4). A `## 3.` .. `## 4.` slice SWALLOWS the sec
3b addendum -- 17 extra table rows, one carrying the span's first escaped pipe. This census
survived that only because its row filter is numeric-only while 3b writes `| row 7 |`: a naming
convention in someone else's file, not a property this one guaranteed. The slice now ends at the
first following `## ` heading, and a contamination control FAILS LOUDLY if a non-arm pipe-row
still reaches the parser.

-- READS THE OBJECT DATABASE AT A CITED COMMIT, never the working tree: a working tree is not
atomic and a census taken during another seat's landing samples a torn state.
"""
import json
import re
import subprocess
import sys

BS = chr(92)
ROW_SPLIT = re.compile('(?<!' + re.escape(BS) + ')' + re.escape('|'))
TOKEN = re.compile('`(L-[^`]+)`')
MULT = re.compile(r'\s*(?:x|\*|\xd7)\s*(\d+)')
ARM_ROW = re.compile(r'^\|\s*\d+\s*\|')
SEPARATOR = re.compile(r'^\|[\s:|-]+\|?\s*$')
DESIGN = "org/standards/isck/WP3_LEDGER_DESIGN.md"


def section_3(commit):
    """The sec-3 ARM TABLE at the commit, bounded at the next `## ` heading."""
    blob = subprocess.check_output(["git", "show", "%s:%s" % (commit, DESIGN)],
                                   stderr=subprocess.PIPE).decode("utf-8", "replace")
    after = blob.split("## 3.")[1]
    cut = re.search(r'\n#{2,} ', after)   # ANY heading level: 3b is `### 3b.`
    return after[:cut.start()] if cut else after


def arms_in(cell):
    """Ordered arm ids in one cell, `x N` expanded, a repeated token counted ONCE.

    The dedup clause read 0 double-cited at six consecutive pins, so self_test() drives it
    synthetically -- six clean readings do not test a branch none of them enter.
    """
    out = []
    for m in TOKEN.finditer(cell):
        tok = m.group(1)
        mult = MULT.match(cell[m.end():m.end() + 22])
        n = int(mult.group(1)) if mult else 1
        if tok in out:
            continue
        out.extend([tok] * n if n > 1 else [tok])
    return out


def census(commit):
    s3 = section_3(commit)
    lines = s3.splitlines()
    rows = [ln for ln in lines if ARM_ROW.match(ln)]
    stray = [ln for ln in lines
             if ln.startswith("|") and ln.count("|") > 3
             and not ARM_ROW.match(ln)
             and not SEPARATOR.match(ln)
             and "responsibility" not in ln.lower()]
    if stray:
        raise SystemExit("SLICE CONTAMINATED: %d non-arm pipe-row(s) reached the parser; first: %s"
                         % (len(stray), stray[0][:100]))
    out = {}
    for line in rows:
        cells = ROW_SPLIT.split(line)
        row = cells[1].strip()
        rejects = arms_in(cells[4]) if len(cells) > 4 else []
        accepts = arms_in(cells[5]) if len(cells) > 5 else []
        out[row] = {
            "reject_ids": rejects,
            "accept_ids": accepts,
            "reject_count": len(rejects),
            "accept_count": len(accepts),
            "pairing": "PAIRED" if rejects and accepts else "UNPAIRED",
        }
    return out


def self_test():
    """Both directions per clause. A clause with no failing arm is not controlled."""
    results = []
    plain = "| 6 | resp | reject | `L-06-a`, `L-06-b` | `L-06-a-accepted` |"
    escaped = "| 6 | resp | A " + BS + "| B | `L-06-a`, `L-06-b` | `L-06-a-accepted` |"
    results.append(("SPLIT: unescaped pipes only -- an escaped pipe does NOT add a cell",
                    len(ROW_SPLIT.split(escaped)) == len(plain.split('|')),
                    len(escaped.split('|')) != len(ROW_SPLIT.split(escaped))))
    results.append(("MULT: `x N` expands to N arms",
                    arms_in("`L-01-a` x 5") == ["L-01-a"] * 5,
                    arms_in("`L-01-a`") == ["L-01-a"]))
    results.append(("DEDUP: a token cited TWICE in one cell counts ONCE",
                    arms_in("`L-02-x`, `L-02-x`") == ["L-02-x"],
                    arms_in("`L-02-x`, `L-02-y`") == ["L-02-x", "L-02-y"]))
    results.append(("SLICE: a non-arm pipe-row is REFUSED, not silently discarded (R4-DT-4)",
                    not SEPARATOR.match("| row 7 | a | b |") and not ARM_ROW.match("| row 7 | a | b |"),
                    bool(ARM_ROW.match("| 7 | a | b |"))))
    ok = True
    for label, fires, control in results:
        good = bool(fires) and bool(control)
        ok = ok and good
        print("  [%s] %s (control reachable: %s)" % ("OK: " if good else "FAIL", label, bool(control)))
    return ok


def main():
    if "--self-test" in sys.argv:
        print("ARM CENSUS SELF-TEST -- each clause with an arm that fires and a control")
        sys.exit(0 if self_test() else 1)
    commit = sys.argv[1]
    data = census(commit)
    total = sum(v["reject_count"] + v["accept_count"] for v in data.values())
    distinct = len({t for v in data.values() for t in v["reject_ids"] + v["accept_ids"]})
    unpaired = [r for r, v in data.items() if v["pairing"] != "PAIRED"]
    print(json.dumps({"commit": commit, "rows": data,
                      "counted_rows": len(data), "counted_arms": total,
                      "counted_distinct": distinct,
                      "unpaired_rows": unpaired}, indent=2, sort_keys=True))
    print("COUNTED: %d rows | %d arms | %d distinct | %d UNPAIRED"
          % (len(data), total, distinct, len(unpaired)), file=sys.stderr)


if __name__ == "__main__":
    main()
