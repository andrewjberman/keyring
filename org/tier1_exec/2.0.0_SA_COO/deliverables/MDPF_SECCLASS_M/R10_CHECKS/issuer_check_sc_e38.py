#!/usr/bin/env python3
"""issuer_check_sc_e38.py -- MDPF_SECCLASS round 8 issuer check for cell SC-e-38 (FWD-5: who reads the old list).

Reads the newest M/OLD_LIST_READER_TRACE_*.md and prints SC-E38-TRACE ok=True|False. It passes only when the trace
carries one section per reader -- a heading line starting '## READER:' -- with at least the three named readers
(Advisor Intelligence's screens, `infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py` (S22),
`data/black_diamond/scripts/classification/resolve_tickers.py` (S25)), each section holding one 'READS:' line, one
'EVIDENCE:' line naming a file path that exists at HEAD (path:line) and one 'VERDICT:' line whose value is one of
NEEDS-OLD-LIST | REPOINTABLE | DEAD-READ | NOT-A-READER; and a 'DENOMINATOR:' line (files or call sites swept).
Run from the repo root.
"""
import glob
import os
import re
import sys

M = os.path.join("org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M")
VERDICTS = {"NEEDS-OLD-LIST", "REPOINTABLE", "DEAD-READ", "NOT-A-READER"}
REQUIRED = ("semantic-news-layer3-curation", "resolve_tickers.py", "advisor")


def main():
    hits = sorted(glob.glob(os.path.join(M, "OLD_LIST_READER_TRACE_*.md")))
    if not hits:
        print("SC-E38-TRACE ok=False no OLD_LIST_READER_TRACE_*.md")
        return 1
    with open(hits[-1], encoding="utf-8") as fh:
        text = fh.read()
    if not re.search(r"^DENOMINATOR:\s*\S", text, re.MULTILINE):
        print("SC-E38-TRACE ok=False no DENOMINATOR line")
        return 1
    sections = re.split(r"^## READER:", text, flags=re.MULTILINE)[1:]
    if len(sections) < 3:
        print(f"SC-E38-TRACE ok=False {len(sections)} reader sections, need >= 3")
        return 1
    heads = " ".join(s.splitlines()[0].lower() for s in sections)
    for r in REQUIRED:
        if r not in heads:
            print(f"SC-E38-TRACE ok=False required reader '{r}' has no section")
            return 1
    for s in sections:
        head = s.splitlines()[0].strip()
        for tag in ("READS:", "EVIDENCE:", "VERDICT:"):
            if len(re.findall(r"^" + tag, s, re.MULTILINE)) != 1:
                print(f"SC-E38-TRACE ok=False section '{head}' needs exactly one {tag} line")
                return 1
        verdict = re.search(r"^VERDICT:\s*(\S+)", s, re.MULTILINE).group(1)
        if verdict not in VERDICTS:
            print(f"SC-E38-TRACE ok=False section '{head}' verdict {verdict} not in {sorted(VERDICTS)}")
            return 1
        ev = re.search(r"^EVIDENCE:\s*`?([^\s`:]+)", s, re.MULTILINE).group(1)
        if not os.path.exists(ev):
            print(f"SC-E38-TRACE ok=False section '{head}' evidence path {ev} absent")
            return 1
    print(f"SC-E38-TRACE ok=True readers={len(sections)} file={os.path.basename(hits[-1])!s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
