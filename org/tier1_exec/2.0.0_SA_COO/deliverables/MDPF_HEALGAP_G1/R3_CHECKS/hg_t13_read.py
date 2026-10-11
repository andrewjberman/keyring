"""MDPF_HEALGAP round 3, HG-t-13 (row MDPF_HEALGAP-S1): the read-only answer on the mdpf-daily-runner's dispatch list.

Reads org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~10/MDAILY_RUNNER_SLICE_READ.md and requires, each on its own line:
  DENOMINATOR: <n> dispatch entries read          (n >= 1)
  VERDICT: RUNS-SLICE | NO-SLICE
  NOOP: YES | NO | UNKNOWN because <reason>       (UNKNOWN needs a reason; YES/NO are bare)
  GROUNDING: <repo path>:<line>[, <repo path>:<line> ...]   (each cites path:digits and the path exists in the tree)
Last line: READ-OK verdict=<v> noop=<x>, or READ-BAD <reasons>. A verdict of NO-SLICE needs NOOP: YES (nothing to no-op) or
UNKNOWN; RUNS-SLICE needs YES, NO or UNKNOWN with its grounding.
"""
from __future__ import annotations

import os
import re
import sys

DOC = os.environ.get("HG_T13_DOC") or os.path.join(
    "org", "missions", "D8", "MDPF", "MDPF_HEALGAP", "deliverables", "0.9.0_WK_MDPF_HEALGAP~10", "MDAILY_RUNNER_SLICE_READ.md")


def main() -> int:
    if not os.path.isfile(DOC):
        print("READ-BAD no file " + DOC)
        return 1
    t = open(DOC, encoding="utf-8").read()
    bad = []
    m = re.search(r"^DENOMINATOR:\s*(\d+) dispatch entries read", t, re.M)
    if not m or int(m.group(1)) < 1:
        bad.append("no 'DENOMINATOR: <n> dispatch entries read' line with n >= 1")
    v = re.search(r"^VERDICT:\s*(RUNS-SLICE|NO-SLICE)\s*$", t, re.M)
    if not v:
        bad.append("no 'VERDICT: RUNS-SLICE|NO-SLICE' line")
    n = re.search(r"^NOOP:\s*(YES|NO|UNKNOWN because \S.*)\s*$", t, re.M)
    if not n:
        bad.append("no 'NOOP: YES|NO|UNKNOWN because <reason>' line")
    g = re.search(r"^GROUNDING:\s*(.+)$", t, re.M)
    if not g:
        bad.append("no GROUNDING line")
    else:
        cites = re.findall(r"([\w./~-]+):(\d+)", g.group(1))
        if not cites:
            bad.append("GROUNDING cites no path:line")
        for path, _ in cites:
            if not os.path.exists(path):
                bad.append("GROUNDING path does not exist: " + path)
    if bad:
        print("READ-BAD " + "; ".join(bad))
        return 1
    print("READ-OK verdict=%s noop=%s" % (v.group(1), n.group(1).split()[0]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
