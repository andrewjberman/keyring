"""Round 8 (~M1) check for SC-e-40 (criterion SC8-e40-AC3): the FWD-4 census's denominator carries every surface.

Reads org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/FWD4_CENSUS_20261007.json (written by the census
instrument R10_CHECKS/fwd4_copy_census.py) and the PRD's surface manifest, and passes when:
  1. the JSON has `denominator_files` > 0 and a `copies` list whose every entry names `path`, `line` and `surface`;
  2. its `surfaces` object holds every REQUIRED surface id with `scanned: true` and a non-empty `paths` list, where
     REQUIRED = every manifest row of org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md whose outcomes name
     FWD-4, plus S22, S23, S24, S25 and S26 (PRD v0.12 addendum);
  3. every path the JSON lists under a surface exists in the repo, or under portal/ in the portal checkout.

Prints `FWD4-SURFACES ok=True required=<n> ...` or `FWD4-SURFACES ok=False ...`. Edits nothing.
"""
import json
import os
import re
import subprocess
import sys

M = "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M"
CENSUS = M + "/FWD4_CENSUS_20261007.json"
PRD = "org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md"
ADDED = {"S22", "S23", "S24", "S25", "S26"}


def root():
    here = os.path.abspath(os.path.dirname(__file__))
    return subprocess.run(["git", "-C", here, "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=False).stdout.strip()


def required(rt):
    req = set(ADDED)
    with open(os.path.join(rt, PRD), encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"\|\s*(S\d\d)\s*\|\s*([^|]*)\|", line)
            if m and "FWD-4" in m.group(2):
                req.add(m.group(1))
    return req


def main():
    rt = root()
    path = os.path.join(rt, CENSUS)
    if not os.path.exists(path):
        print(f"FWD4-SURFACES ok=False reason=census-json-absent path={CENSUS}")
        return 1
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    req = required(rt)
    surfaces = data.get("surfaces") or {}
    missing = sorted(s for s in req if not (surfaces.get(s) or {}).get("scanned") or not (surfaces.get(s) or {}).get("paths"))
    gone = []
    for entry in surfaces.values():
        for p in (entry or {}).get("paths", []):
            if not os.path.exists(os.path.join(rt, p)):
                gone.append(p)
    copies = data.get("copies")
    copies_ok = isinstance(copies, list) and all(isinstance(c, dict) and {"path", "line", "surface"} <= set(c) for c in copies)
    denom = data.get("denominator_files") or 0
    ok = not missing and not gone and copies_ok and denom > 0
    print(f'FWD4-SURFACES ok={ok!s} required={len(req)} missing={",".join(missing) or "-"!s} paths_gone={len(gone)} copies={len(copies) if isinstance(copies, list) else "BAD"!s} denominator_files={denom!s}')
    for p in gone[:10]:
        print(f"  GONE {p}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
