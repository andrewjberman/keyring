#!/usr/bin/env python3
"""MDPF_SECCLASS round 8, cell SC-e-24 (criterion SC8-e24-AC1): the screen-group census and its mapping, as data.

READ-ONLY. Reads the newest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/SCREEN_GROUP_MAPPING_<yyyymmdd>.json
and grades its SHAPE and its COVERAGE (never whether a mapping is wise: that is the CVO's).

Required shape:
  {
    "denominator": {"files_scanned": <int > 0>, "how": "<the census command or rule>"},
    "six_classes": ["cash", "fixed_income", "equity", "structured", "alternatives", "commodities"],
    "screens": [
      {"screen": "<name a person sees>", "files": ["<repo path>", ...], "groups": ["<group shown>", ...],
       "mapping": {"<each of the six>": "<one of groups>"}, "basis": "measured|inferred"}
    ],
    "geography": {"source": "<repo path>:<line>", "values": ["..."], "placed": "<where S26's list belongs, or OPEN>"}
  }

ok=True only when: denominator.files_scanned > 0; six_classes is exactly the six; screens >= 1; every screen whose
`groups` has fewer than six entries carries a mapping with all six keys, each value one of that screen's groups; every
screen's `files` exist in this tree; geography.source names yang-generate-positioning and geography.values is non-empty.

Prints: SCREEN-GROUP-MAPPING ok=<bool> file=<name> screens=<n> fewer_than_six=<n> mapped=<n> problems=<n>
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
HOME = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M"
SIX = ["cash", "fixed_income", "equity", "structured", "alternatives", "commodities"]


def main():
    files = sorted(HOME.glob("SCREEN_GROUP_MAPPING_*.json"))
    if not files:
        print("SCREEN-GROUP-MAPPING ok=False file=ABSENT screens=0 fewer_than_six=0 mapped=0 problems=1")
        return 1
    path = files[-1]
    problems = []
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:  # a malformed file is a finding, printed
        print(f"PROBLEM unreadable json: {exc}")
        print(f"SCREEN-GROUP-MAPPING ok=False file={path.name} screens=0 fewer_than_six=0 mapped=0 problems=1")
        return 1
    den = (doc.get("denominator") or {}).get("files_scanned")
    if not isinstance(den, int) or den <= 0:
        problems.append("denominator.files_scanned missing or not > 0")
    if doc.get("six_classes") != SIX:
        problems.append(f"six_classes is not exactly {SIX}")
    screens = doc.get("screens") or []
    if not screens:
        problems.append("no screens")
    fewer = mapped = 0
    for s in screens:
        name = s.get("screen", "<unnamed>")
        groups = s.get("groups") or []
        for f in s.get("files") or []:
            if not (ROOT / f).exists():
                problems.append(f"{name}: file not in tree: {f}")
        if not s.get("files"):
            problems.append(f"{name}: no files")
        if len(groups) < 6:
            fewer += 1
            m = s.get("mapping") or {}
            missing = [c for c in SIX if c not in m]
            stray = [c for c, g in m.items() if c in SIX and g not in groups]
            if missing:
                problems.append(f"{name}: mapping lacks {missing}")
            if stray:
                problems.append(f"{name}: mapping targets not among its groups for {stray}")
            if not missing and not stray:
                mapped += 1
    geo = doc.get("geography") or {}
    if "yang-generate-positioning" not in str(geo.get("source", "")) or not geo.get("values"):
        problems.append("geography: source must name yang-generate-positioning and values must be non-empty")
    for p in problems:
        print(f"PROBLEM {p}")
    ok = not problems
    print(f"SCREEN-GROUP-MAPPING ok={ok} file={path.name} screens={len(screens)} fewer_than_six={fewer} "
          f"mapped={mapped} problems={len(problems)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
