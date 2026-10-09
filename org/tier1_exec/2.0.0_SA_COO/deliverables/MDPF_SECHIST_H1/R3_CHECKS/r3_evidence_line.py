"""MDPF_SECHIST round 3: read one evidence file and grade its summary line against a floor.

Usage: python r3_evidence_line.py <LABEL> <evidence file, repo-relative> <regex with named groups> <group>=<min> [...]
The regex must match exactly one line; each named integer group must be >= its floor.

Last line: <LABEL>-EVIDENCE-OK <the matched line>   or   <LABEL>-EVIDENCE-BAD <reason>.
"""
from __future__ import annotations

import os
import re
import sys


def main(argv: list[str]) -> int:
    if len(argv) < 4:
        print("usage: r3_evidence_line.py LABEL FILE REGEX [GROUP=MIN ...]")
        return 2
    label, path, rx = argv[1], argv[2], re.compile(argv[3])
    floors = dict(a.split("=", 1) for a in argv[4:])
    if not os.path.isfile(path):
        print(f"{label}-EVIDENCE-BAD missing-file={path}")
        return 1
    with open(path, encoding="utf-8") as fh:
        hits = [(ln.rstrip("\n"), m) for ln in fh for m in [rx.search(ln)] if m]
    if len(hits) != 1:
        print(f"{label}-EVIDENCE-BAD summary-lines={len(hits)} (want 1)")
        return 1
    line, m = hits[0]
    for g, lo in floors.items():
        v = int(m.group(g))
        if v < int(lo):
            print(f"{label}-EVIDENCE-BAD {g}={v} below {lo}")
            return 1
    print(f"{label}-EVIDENCE-OK {line.strip()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
