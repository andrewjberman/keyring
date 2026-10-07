#!/usr/bin/env python3
"""issuer_check_sc_e38.py -- MDPF_SECCLASS round 8 issuer check for cell SC-e-38 (FWD-5: who reads the old list).

Reads the newest M/OLD_LIST_READER_TRACE_*.md and prints SC-E38-TRACE ok=True|False. It passes only when the trace
carries one section per reader -- a heading line starting '## READER:' -- with at least the three named readers
(Advisor Intelligence's screens, `infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py` (S22),
`data/black_diamond/scripts/classification/resolve_tickers.py` (S25)), each section holding one 'READS:' line, one
'EVIDENCE:' line naming a file path that exists at HEAD (path:line) and one 'VERDICT:' line whose value is one of
NEEDS-OLD-LIST | REPOINTABLE | DEAD-READ | NOT-A-READER; and a 'DENOMINATOR:' line (files or call sites swept).

AMENDMENT 1 (2.0.0_SA_COO~M1, on 1.0.0_SA_CTO~DELL1's refusal of the SC-e-35 half, CTO_HALF_MDPF_SECCLASS_SC_e35_...md):
the census is computed HERE, at run time, by the CTO's printed command -- `git grep -l -E "bd-securities|BD_SECURITIES_TABLE"`
over *.py *.ts *.tsx *.tf *.json, excluding data/black_diamond/**, org/** and test files -- and EVERY file it returns must have a
'## READER:' section whose heading contains that file's repo path. Every section whose VERDICT is not NOT-A-READER must also carry
exactly one 'MISSING-ROW:' line (the reader's own rule for a ticker with no bd-securities row, path:line), one 'SERVED-NEW:' line
(what its served output shows for a security first held after the old-list writers stop) and one 'CANONICAL-PRODUCER:' line (the
producer that gives such a security an etf-classifications row before this reader runs, or NONE). Prints the census denominator.
Run from the repo root.
"""
import glob
import os
import re
import subprocess
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
    census = census_files()
    missing = [f for f in census if f.lower() not in heads_full(sections)]
    if missing:
        print(f"SC-E38-TRACE ok=False census={len(census)} uncovered={len(missing)} first={missing[:3]}")
        return 1
    for s in sections:
        head = s.splitlines()[0].strip()
        verdict = re.search(r"^VERDICT:\s*(\S+)", s, re.MULTILINE).group(1)
        if verdict == "NOT-A-READER":
            continue
        for tag in ("MISSING-ROW:", "SERVED-NEW:", "CANONICAL-PRODUCER:"):
            if len(re.findall(r"^" + tag, s, re.MULTILINE)) != 1:
                print(f"SC-E38-TRACE ok=False section '{head}' needs exactly one {tag} line")
                return 1
    print(f"SC-E38-TRACE ok=True readers={len(sections)} census={len(census)} file={os.path.basename(hits[-1])!s}")
    return 0


def census_files():
    r = subprocess.run(["git", "grep", "-l", "-E", "bd-securities|BD_SECURITIES_TABLE", "--", "*.py", "*.ts", "*.tsx", "*.tf", "*.json"],
                       capture_output=True, text=True, timeout=60, check=False)
    out = []
    for f in r.stdout.splitlines():
        low = f.lower()
        if f.startswith(("data/black_diamond/", "org/")) or "/tests/" in low or "/test_" in low or ".test." in low or "__tests__" in low:
            continue
        out.append(f)
    return out


def heads_full(sections):
    return " ".join(s.splitlines()[0].lower() for s in sections)


if __name__ == "__main__":
    sys.exit(main())
