"""MDPF_STRATID round 1, ST-t-4 criterion AC1: the Eclipse (Inflection) sleeve-name census document exists and carries
its denominator. CENSUS-OK when the file has a `DENOMINATOR:` line with an integer, a `SOURCE:` line naming the read
objects, and a `RESULT:` line; else CENSUS-BAD. Run from the repo (worktree) root.
"""
from __future__ import annotations

import os
import re
import sys

DOC = os.path.join("org", "missions", "D8", "MDPF", "MDPF_STRATID", "deliverables", "0.9.0_WK_MDPF_STRATID~3",
                   "ECLIPSE_SLEEVE_NAME_CENSUS.md")

if __name__ == "__main__":
    if not os.path.isfile(DOC):
        print("CENSUS-BAD no file " + DOC)
        sys.exit(1)
    text = open(DOC, encoding="utf-8").read()
    den = re.search(r"^DENOMINATOR:\s*(\d+)", text, re.M)
    src = re.search(r"^SOURCE:\s*\S+", text, re.M)
    res = re.search(r"^RESULT:\s*\S+", text, re.M)
    if not (den and src and res):
        print("CENSUS-BAD missing line(s): " + ",".join(n for n, m in (("DENOMINATOR", den), ("SOURCE", src),
                                                                       ("RESULT", res)) if not m))
        sys.exit(1)
    print("denominator=%s" % den.group(1))
    print("CENSUS-OK")
    sys.exit(0)
