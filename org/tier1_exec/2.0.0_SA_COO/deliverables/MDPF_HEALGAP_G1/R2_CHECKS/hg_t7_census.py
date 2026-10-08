"""MDPF_HEALGAP round 2, HG-t-7 (FWD-6) criterion AC1: the census of scheduled pulls that lean on a login kept alive
by something else, as a written answer.

Reads `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~6/FWD6_SESSION_DEPENDENT_PULLS_CENSUS.md`
and requires:
  - a line `DENOMINATOR: <n> scheduled pulls read` (the population swept) and `<n>` >= the table's row count;
  - a markdown table whose header names the columns `pull`, `schedule`, `login kept alive by`, `answer`, `grounding`;
  - every row's `answer` is `RECOVERS` or `NOT-EXPOSED because ...` (a non-empty reason), never blank;
  - a row for the 49F login chain, listed FIRST, and a row for the Cottonwood Rebalancer runner (`cot-rebalancer-runner`);
  - every row's `grounding` cell is non-empty.
CENSUS-OK with the row count; else CENSUS-BAD <reason>. Completeness of the population is a JUDGMENT the CVO grades.
"""
from __future__ import annotations

import os
import re
import sys

DOC = os.path.join("org", "missions", "D8", "MDPF", "MDPF_HEALGAP", "deliverables", "0.9.0_WK_MDPF_HEALGAP~6",
                   "FWD6_SESSION_DEPENDENT_PULLS_CENSUS.md")
COLS = ["pull", "schedule", "login kept alive by", "answer", "grounding"]


def main() -> int:
    if not os.path.isfile(DOC):
        print("CENSUS-BAD no file " + DOC)
        return 1
    with open(DOC, encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"^DENOMINATOR:\s*(\d+) scheduled pulls read", text, re.M)
    if not m:
        print("CENSUS-BAD no 'DENOMINATOR: <n> scheduled pulls read' line")
        return 1
    denom = int(m.group(1))
    lines = [ln for ln in text.splitlines() if ln.strip().startswith("|")]
    hdr_i = next((i for i, ln in enumerate(lines) if all(c in ln.lower() for c in COLS)), None)
    if hdr_i is None:
        print("CENSUS-BAD no table header naming " + ", ".join(COLS))
        return 1
    hdr = [c.strip().lower() for c in lines[hdr_i].strip().strip("|").split("|")]
    idx = {c: next(i for i, h in enumerate(hdr) if c in h) for c in COLS}
    rows = []
    for ln in lines[hdr_i + 1:]:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if set("".join(cells)) <= set("-: "):
            continue
        rows.append(cells)
    if not rows:
        print("CENSUS-BAD table has no rows")
        return 1
    bad = []
    for r in rows:
        if len(r) < len(hdr):
            bad.append("short row %r" % r[:1])
            continue
        ans = r[idx["answer"]]
        if not (ans == "RECOVERS" or re.match(r"NOT-EXPOSED because \S", ans)):
            bad.append("row %r answer %r" % (r[idx["pull"]][:40], ans[:40]))
        if not r[idx["grounding"]]:
            bad.append("row %r has no grounding" % r[idx["pull"]][:40])
    if "49f" not in rows[0][idx["pull"]].lower() and "49f" not in rows[0][idx["login kept alive by"]].lower():
        bad.append("first row is not the 49F login chain")
    if not any("cot-rebalancer-runner" in r[idx["pull"]] for r in rows):
        bad.append("no cot-rebalancer-runner row")
    if denom < len(rows):
        bad.append("denominator %d < rows %d" % (denom, len(rows)))
    if bad:
        print("CENSUS-BAD " + "; ".join(bad))
        return 1
    print("CENSUS-OK rows=%d denominator=%d" % (len(rows), denom))
    return 0


if __name__ == "__main__":
    sys.exit(main())
