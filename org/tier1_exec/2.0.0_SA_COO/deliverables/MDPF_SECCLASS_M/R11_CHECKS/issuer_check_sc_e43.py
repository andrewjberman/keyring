#!/usr/bin/env python3
"""issuer_check_sc_e43.py -- MDPF_SECCLASS round 9 issuer check for cell SC-e-43 (FWD-5): the resolve_tickers gap record.

Reads the newest M/RESOLVE_TICKERS_GAP_*.md the worker writes. It passes only when the file carries one '## ATTRIBUTE:' section for each
of asset_name_raw and name_aliases, each with an integer 'OLD-LIST-ROWS:' line (bd-securities rows carrying it, read-only scan), exactly
one 'CANONICAL:' line (whether etf-classifications carries it) and exactly one 'USED-BY:' line (the resolve_tickers.py method, path:line);
plus one integer 'CANONICAL-FIRST-HITS:' line (held names the switch now resolves from the canonical `name` first, from the worker's
dry run). Prints SC-E43-GAP ok=True|False. Read-only. Run from the repo root.
"""
import glob
import os
import re
import sys

M = os.path.join("org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M")


def main():
    hits = sorted(glob.glob(os.path.join(M, "RESOLVE_TICKERS_GAP_*.md")))
    if not hits:
        print("SC-E43-GAP ok=False no RESOLVE_TICKERS_GAP_*.md")
        return 1
    with open(hits[-1], encoding="utf-8") as fh:
        text = fh.read()
    sections = re.split(r"^## ATTRIBUTE:", text, flags=re.MULTILINE)[1:]
    names = {s.splitlines()[0].strip().strip("`") for s in sections}
    for need in ("asset_name_raw", "name_aliases"):
        if need not in names:
            print(f"SC-E43-GAP ok=False no ATTRIBUTE section for {need}")
            return 1
    for s in sections:
        head = s.splitlines()[0].strip()
        if not re.search(r"^OLD-LIST-ROWS:\s*\d+", s, re.MULTILINE):
            print(f"SC-E43-GAP ok=False section {head} lacks an integer OLD-LIST-ROWS line")
            return 1
        for tag in ("CANONICAL:", "USED-BY:"):
            if len(re.findall(r"^" + tag, s, re.MULTILINE)) != 1:
                print(f"SC-E43-GAP ok=False section {head} needs exactly one {tag} line")
                return 1
    m = re.search(r"^CANONICAL-FIRST-HITS:\s*(\d+)", text, re.MULTILINE)
    if not m:
        print("SC-E43-GAP ok=False no CANONICAL-FIRST-HITS line")
        return 1
    print(f"SC-E43-GAP ok=True attributes={len(sections)} canonical_first_hits={m.group(1)} file={os.path.basename(hits[-1])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
