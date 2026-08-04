#!/usr/bin/env python3
"""prd-delta-report.py -- text lens over a persisted /prd-delta Workflow result.

Reads the JSON the /prd-delta skill writes after its Workflow fan-out completes
(default org/mcp/prd_delta_results/latest.json) and prints the sorted ASCII report,
worst-completeness first. Presentation-only -- this script does NOT run the
assessment itself (that requires the Workflow tool's agent fan-out, outside a plain
script's reach); same engine/presentation split as its /registry-check, /to-check,
/activity-check siblings.

Usage:
  python .tools/prd-delta-report.py                # default path
  python .tools/prd-delta-report.py --path PATH.json
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
DEFAULT_PATH = WORKSPACE / "org" / "mcp" / "prd_delta_results" / "latest.json"

_ASCII = {
    "—": "--", "–": "-", "…": "...", "→": "->",
    "‘": "'", "’": "'", "“": '"', "”": '"',
}


def to_ascii(t: str) -> str:
    for u, a in _ASCII.items():
        t = t.replace(u, a)
    return t.encode("ascii", "replace").decode("ascii")


def bar(pct, width: int = 20) -> str:
    if pct is None:
        return "[" + ("?" * width) + "]  N/A"
    filled = round(width * pct / 100)
    return "[" + ("#" * filled) + ("." * (width - filled)) + f"] {pct:3d}%"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default=str(DEFAULT_PATH))
    args = ap.parse_args()

    p = Path(args.path)
    if not p.exists():
        sys.stderr.write(f"ERROR: no results file at {p} -- run /prd-delta first "
                          "(the Workflow fan-out writes this file when it completes).\n")
        sys.exit(1)
    d = json.loads(p.read_text(encoding="utf-8-sig", errors="replace"))
    results = d.get("results", [])
    generated = d.get("generated_scope", len(results))
    with_prd = d.get("with_prd", sum(1 for r in results if r.get("completeness_label") != "NO-PRD"))
    no_prd = d.get("no_prd", sum(1 for r in results if r.get("completeness_label") == "NO-PRD"))

    mtime = datetime.datetime.fromtimestamp(p.stat().st_mtime, tz=datetime.timezone.utc)
    print(f"PRD-DELTA  {mtime.strftime('%Y-%m-%dT%H:%MZ')}  |  {generated} project(s) assessed  "
          f"|  {with_prd} with PRD  |  {no_prd} no PRD")
    print("  (sorted worst-completeness first; NO-PRD projects sort to the front -- "
          "an unwritten spec is its own finding)")
    print()

    results_sorted = sorted(results, key=lambda r: (r.get("completeness_pct") is not None,
                                                      r.get("completeness_pct") or 0))

    pcts = [r["completeness_pct"] for r in results if r.get("completeness_pct") is not None]
    mismatches = [r for r in results if r.get("registry_mismatch")]

    for i, r in enumerate(results_sorted, 1):
        code = r.get("code", "?")
        label = r.get("completeness_label", "?")
        pct = r.get("completeness_pct")
        print(f"#: {i}")
        print(f"Project: {code}")
        print(f"Completeness: {bar(pct)}  ({label})")
        rm = r.get("registry_mismatch")
        if rm:
            print(f"REGISTRY MISMATCH: {to_ascii(str(rm))}")
        missing = r.get("missing") or []
        if missing:
            print("Missing:")
            for m in missing:
                print(f"  - {to_ascii(str(m))}")
        else:
            print("Missing: (none -- fully accounted for)")
        undoc = r.get("undocumented_activity") or []
        if undoc:
            print("Undocumented activity (not traceable to a PRD item):")
            for u in undoc:
                print(f"  * {to_ascii(str(u))}")
        print("-" * 56)

    avg = round(sum(pcts) / len(pcts)) if pcts else None
    print()
    print(f"SUMMARY: avg completeness {avg if avg is not None else 'N/A'}% "
          f"| {no_prd} with no PRD | {len(mismatches)} registry-mismatch(es) "
          f"| {sum(1 for r in results if r.get('completeness_pct') == 100)} fully complete")
    print(f"PRD-DELTA-RESULT total={len(results)} no_prd={no_prd} "
          f"mismatches={len(mismatches)} avg_pct={avg if avg is not None else -1}")


if __name__ == "__main__":
    main()
