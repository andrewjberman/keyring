"""MDPF_DEMQUE round 1, DQ-t-5 (FWD-1 hop 6) criterion AC1: the read-only trace from Cottonwood's canonical prices to
the client's page, as a written answer.

Reads `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~4/FWD1_HOP6_PRICES_TO_PAGE_TRACE.md` and
requires:
  - a markdown table whose header names the columns `hop`, `question`, `answer`, `grounding`;
  - rows for hops Q1..Q5 (the `hop` cell starts `Q1` .. `Q5`), each with a non-empty answer and grounding;
  - a line `VERDICT: <BUILD-NEEDED|NO-BUILD-NEEDED> -- <reason>` naming whether a scheduled run today would carry a new
    Yahoo row in opal-data-cot silver/historical_prices.parquet to the page without a person running anything.
TRACE-OK; else TRACE-BAD <reason>. Correctness of each answer is a JUDGMENT the CVO grades.
"""
from __future__ import annotations

import os
import re
import sys

DOC = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "deliverables", "0.9.0_WK_MDPF_DEMQUE~4",
                   "FWD1_HOP6_PRICES_TO_PAGE_TRACE.md")
COLS = ["hop", "question", "answer", "grounding"]


def main() -> int:
    if not os.path.isfile(DOC):
        print("TRACE-BAD no file " + DOC)
        return 1
    with open(DOC, encoding="utf-8") as f:
        text = f.read()
    if not re.search(r"^VERDICT:\s*(BUILD-NEEDED|NO-BUILD-NEEDED)\s+--\s+\S", text, re.M):
        print("TRACE-BAD no 'VERDICT: BUILD-NEEDED|NO-BUILD-NEEDED -- <reason>' line")
        return 1
    lines = [ln for ln in text.splitlines() if ln.strip().startswith("|")]
    hdr_i = next((i for i, ln in enumerate(lines) if all(c in ln.lower() for c in COLS)), None)
    if hdr_i is None:
        print("TRACE-BAD no table header naming " + ", ".join(COLS))
        return 1
    hdr = [c.strip().lower() for c in lines[hdr_i].strip().strip("|").split("|")]
    idx = {c: next(i for i, h in enumerate(hdr) if c in h) for c in COLS}
    seen = set()
    for ln in lines[hdr_i + 1:]:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if set("".join(cells)) <= set("-: ") or len(cells) < len(hdr):
            continue
        m = re.match(r"Q([1-5])\b", cells[idx["hop"]])
        if not m:
            continue
        if not cells[idx["answer"]] or not cells[idx["grounding"]]:
            print("TRACE-BAD hop Q%s has an empty answer or grounding" % m.group(1))
            return 1
        seen.add(int(m.group(1)))
    missing = sorted({1, 2, 3, 4, 5} - seen)
    if missing:
        print("TRACE-BAD missing hops " + ",".join("Q%d" % q for q in missing))
        return 1
    print("TRACE-OK hops=5")
    return 0


if __name__ == "__main__":
    sys.exit(main())
