#!/usr/bin/env python3
"""issuer_check_sc_e41.py -- MDPF_SECCLASS round 9 issuer check for cell SC-e-41 (FWD-5, row W25-S5): the widened reader census.

Reads the newest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_READER_TRACE_BD_*.md. It passes only when:
- a 'DENOMINATOR:' line is present;
- the census is computed HERE at run time -- git grep -l -E "bd-securities|BD_SECURITIES_TABLE" over data/black_diamond/ minus test
  files (13 files at the round-9 base) -- and EVERY file it returns has a '## READER:' section whose heading contains its repo path;
- one section's heading contains 'runtime' (the run-time-assembled table names via the naming registry) and one section's heading
  contains 'role' (role-level grants that reach the table without naming it in code);
- every section carries exactly one 'READS:', 'EVIDENCE:' (a path that exists at HEAD, path:line) and 'VERDICT:' line, VERDICT one of
  NEEDS-OLD-LIST | REPOINTABLE | DEAD-READ | NOT-A-READER; every section whose VERDICT is not NOT-A-READER carries exactly one
  'MISSING-ROW:', 'SERVED-NEW:' and 'CANONICAL-PRODUCER:' line.
Prints SC-E41-TRACE ok=True|False with the census denominator. Run from the repo root. Read-only.
"""
import glob
import os
import re
import subprocess
import sys

M = os.path.join("org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M")
VERDICTS = {"NEEDS-OLD-LIST", "REPOINTABLE", "DEAD-READ", "NOT-A-READER"}


def census():
    r = subprocess.run(["git", "grep", "-l", "-E", "bd-securities|BD_SECURITIES_TABLE", "--", "data/black_diamond/"],
                       capture_output=True, text=True, timeout=60, check=False)
    return [f for f in r.stdout.splitlines() if "/tests/" not in f and "/test_" not in f]


def check_section(s):
    head = s.splitlines()[0].strip()
    for tag in ("READS:", "EVIDENCE:", "VERDICT:"):
        if len(re.findall(r"^" + tag, s, re.MULTILINE)) != 1:
            return f"section '{head}' needs exactly one {tag} line"
    verdict = re.search(r"^VERDICT:\s*(\S+)", s, re.MULTILINE).group(1)
    if verdict not in VERDICTS:
        return f"section '{head}' verdict {verdict}"
    ev = re.search(r"^EVIDENCE:\s*`?([^\s`:]+)", s, re.MULTILINE).group(1)
    if not os.path.exists(ev):
        return f"section '{head}' evidence path {ev} absent"
    if verdict != "NOT-A-READER":
        for tag in ("MISSING-ROW:", "SERVED-NEW:", "CANONICAL-PRODUCER:"):
            if len(re.findall(r"^" + tag, s, re.MULTILINE)) != 1:
                return f"section '{head}' needs exactly one {tag} line"
    return None


def main():
    hits = sorted(glob.glob(os.path.join(M, "OLD_LIST_READER_TRACE_BD_*.md")))
    if not hits:
        print("SC-E41-TRACE ok=False no OLD_LIST_READER_TRACE_BD_*.md")
        return 1
    with open(hits[-1], encoding="utf-8") as fh:
        text = fh.read()
    if not re.search(r"^DENOMINATOR:\s*\S", text, re.MULTILINE):
        print("SC-E41-TRACE ok=False no DENOMINATOR line")
        return 1
    sections = re.split(r"^## READER:", text, flags=re.MULTILINE)[1:]
    heads = [s.splitlines()[0].lower() for s in sections]
    files = census()
    missing = [f for f in files if not any(f.lower() in h for h in heads)]
    if missing:
        print(f"SC-E41-TRACE ok=False census={len(files)} uncovered={len(missing)} first={missing[:3]}")
        return 1
    for need in ("runtime", "role"):
        if not any(need in h for h in heads):
            print(f"SC-E41-TRACE ok=False no section heading names '{need}'")
            return 1
    for s in sections:
        why = check_section(s)
        if why:
            print(f"SC-E41-TRACE ok=False {why}")
            return 1
    print(f"SC-E41-TRACE ok=True sections={len(sections)} census={len(files)} file={os.path.basename(hits[-1])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
