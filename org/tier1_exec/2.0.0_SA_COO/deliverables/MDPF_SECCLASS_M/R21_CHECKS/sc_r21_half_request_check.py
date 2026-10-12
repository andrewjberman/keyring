#!/usr/bin/env python3
"""sc_r21_half_request_check.py -- MDPF_SECCLASS round 21 cell SC-e-91: the never-widen half request for the C_06 retained-date fix exists
and carries the six sections a half must carry. Reads one file; writes nothing.

Usage:  python sc_r21_half_request_check.py <path-to-half-request.md>

Sections (each a heading line containing the words, case-insensitive):
  1 'the act'                   the deploy, by whom, under which ledger, before which fire
  2 'blast radius'              objects the act writes and objects the next fire writes
  3 'writers'                   the writers of the served mix_summary.json counted, N printed, each named by file:line
  4 'both branches'             the expected outcome read from the code's own rule: a holding WITH a NAME:: row moves; one WITHOUT stays, listed
  5 'rollback'                  the prior C_06 object and the prior gold objects, by version
  6 'reach'                     what the act can and cannot move on a retained date: the share of the retained dates' unclassified dollars
                                that sit inside the stored per-date holding lists the revisit reads, MEASURED read-only, with its denominator
plus two signature lines left UNSIGNED: 'COO half' and 'CTO half'.
Prints  HALF-REQUEST ok=<bool> sections=<n>/6 unsigned_halves=<n>/2
"""
import re
import sys
from pathlib import Path


def main(argv) -> int:
    if len(argv) != 2:
        print("HALF-REQUEST ok=False error=usage (path)")
        return 2
    p = Path(argv[1])
    if not p.is_file():
        print("HALF-REQUEST ok=False sections=0/6 unsigned_halves=0/2 error=absent")
        return 1
    text = p.read_text(encoding="utf-8", errors="replace")
    heads = [ln.lower() for ln in text.splitlines() if ln.lstrip().startswith("#") or ln.lstrip().startswith("**")]
    want = ["the act", "blast radius", "writers", "both branches", "rollback", "reach"]
    found = sum(1 for w in want if any(w in h for h in heads))
    unsigned = 0
    for half in ("coo half", "cto half"):
        for ln in text.splitlines():
            low = ln.lower()
            if half in low and re.search(r"unsigned|not signed|pending", low):
                unsigned += 1
                break
    ok = found == 6 and unsigned == 2
    print(f"HALF-REQUEST ok={ok} sections={found}/6 unsigned_halves={unsigned}/2")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
