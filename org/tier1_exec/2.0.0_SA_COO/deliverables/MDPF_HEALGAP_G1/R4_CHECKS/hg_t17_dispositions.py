"""MDPF_HEALGAP round 4, HG-t-17: the seven EXPOSED-MANUAL pulls each get a disposition document check. Read-only; no AWS call.

  python hg_t17_dispositions.py [DOC]

DOC (default org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md) must carry
exactly SEVEN disposition rows, one per pull named in FWD6_CENSUS_RESWEEP_R3.md section 4's EXPOSED-MANUAL list, in a markdown
table whose first cell is the pull's key (the names below). Each row must have:
  - a disposition token, exactly one of RE-ATTEMPT-BUILT, RE-ATTEMPT-DESIGNED, NAMED-REASON;
  - a `because` clause of at least 40 characters (the third-or-later cell, not the token or the key);
  - at least one `path:line` citation that resolves in the repo (the file exists and the line number is within it), and
    for a NAMED-REASON row, the person's act and the place it is listed are named (the words `person` and `listed`).
  No row may read TBD or TODO, and RE-ATTEMPT-BUILT is allowed only for bd-asset-dim-pipeline-trigger (its re-attempt is the
  HG-t-11 rule, live since 2026-10-11).
Last line: DISP-OK <n> rows, or DISP-BAD <reasons>. At the base (no file) this is DISP-BAD.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

DOC = "org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md"
KEYS = [
    "outlook-global-transcripts-pull-daily",
    "teams-global-transcripts-pull-hourly",
    "schwab-canonical-si2-08403355-pull-daily",
    "canonical-schwab-si2-08242234-daily-pull",
    "canonical-schwab-si2-08335338-daily-pull",
    "astn-wsjft-3am-run",
    "bd-asset-dim-pipeline-trigger",
]
TOKENS = ("RE-ATTEMPT-BUILT", "RE-ATTEMPT-DESIGNED", "NAMED-REASON")
CITE = re.compile(r"([A-Za-z0-9_./\-]+\.[A-Za-z0-9]+):(\d+)")


def main(path: str) -> int:
    p = Path(path)
    if not p.is_file():
        print(f"DISP-BAD no document at {path}")
        return 1
    text = p.read_text(encoding="utf-8")
    rows = {}
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if cells and cells[0] in KEYS:
            if cells[0] in rows:
                print(f"DISP-BAD pull {cells[0]} has two rows")
                return 1
            rows[cells[0]] = cells
    bad = []
    missing = [k for k in KEYS if k not in rows]
    if missing:
        bad.append("missing rows: " + ", ".join(missing))
    root = Path(".")
    for k, cells in rows.items():
        body = " | ".join(cells[1:])
        toks = [t for t in TOKENS if t in body]
        if len(toks) != 1:
            bad.append(f"{k}: disposition tokens found {toks}, want exactly one of {TOKENS}")
            continue
        tok = toks[0]
        if re.search(r"\b(TBD|TODO)\b", body):
            bad.append(f"{k}: reads TBD/TODO")
        if tok == "RE-ATTEMPT-BUILT" and k != "bd-asset-dim-pipeline-trigger":
            bad.append(f"{k}: RE-ATTEMPT-BUILT is allowed only for bd-asset-dim-pipeline-trigger")
        because = CITE.sub("", " ".join(c for c in cells[1:] if tok not in c)).strip()
        if len(because) < 40:
            bad.append(f"{k}: the because clause is {len(because)} characters, want at least 40")
        cites = CITE.findall(body)
        ok = 0
        for f, ln in cites:
            fp = root / f
            if fp.is_file():
                try:
                    n = sum(1 for _ in fp.open(encoding="utf-8", errors="replace"))
                except OSError:
                    n = 0
                if 1 <= int(ln) <= n:
                    ok += 1
        if ok < 1:
            bad.append(f"{k}: no path:line citation resolves in the repo (cites {cites[:3]})")
        if tok == "NAMED-REASON" and not (re.search(r"\bperson", body, re.I) and re.search(r"\blisted\b", body, re.I)):
            bad.append(f"{k}: a NAMED-REASON row must name the person's act and where it is listed")
    if bad:
        print("DISP-BAD " + "; ".join(bad))
        return 1
    print(f"DISP-OK {len(rows)} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else DOC))
