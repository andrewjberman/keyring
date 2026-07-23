#!/usr/bin/env python
"""msbeff_phase1 -- NFRA_MSBEFF Phase 1: AUTO-vs-CHOSEN split + FAIL taxonomy.

Consumes the Phase-0 JSON snapshot (re-emit with msbeff_log_audit.py --json first if stale).

AUTO detection is SIGNATURE-GROUNDED, not guessed (sampled live rows 2026-07-23):
  surface-check + "check --mode advisory"  -> safe-commit auto-invoke
  pulse         + command starts "diff "    -> pre-commit risk-reflex auto-invoke
  constants     + "check --file"            -> universal commit-gate auto-invoke
Everything else counts CHOSEN. The split is a floor for AUTO (other gates may hide);
denominators printed so the floor is explicit.

FAIL taxonomy (note+command keyword clusters; first match wins, order = specificity):
  FIXTURE       deliberate test-reds: synthetic/fixture/mutant/control/self-test/probe/exercised
  DETECTION     the gate WORKING -- drift/violation/mismatch/missing-required detected
  STALE-GRAPH   graph/cache vintage: stale, rebuild, "comp-build first", not-in-graph
  BAD-INPUT     name-resolution/user-error: not found, no such, unknown, ambiguous, usage
  TOOL-BROKEN   crash-class: traceback, exception, charmap/unicode, timeout, exit 2, TypeError
  NO-NOTE       FAIL with an empty note cell -- unclassifiable without the session log
  OTHER         note present, no cluster matched (listed for manual pass)
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SNAP = HERE / "log_audit_3mo.json"

AUTO_SIGS = (
    ("surface-check", re.compile(r"check\s+--mode\s+advisory")),
    ("pulse", re.compile(r"^\s*(comp-pulse\s+)?diff\s")),
    ("constants", re.compile(r"check\s+--file\b")),
)

TAXONOMY = [
    ("FIXTURE", re.compile(r"synthetic|fixture|mutant|negative.control|positive.control|self.?test|probe|exercis|drill|expected.(red|fail)|deliberate", re.I)),
    ("DETECTION", re.compile(r"drift detected|violation|mismatch|caught|flagged|missing (required|entry|firm|column)|found \d+ (issue|drift|gap)|correctly (fail|refus)|as designed|working as", re.I)),
    ("STALE-GRAPH", re.compile(r"stale|rebuild|comp-build first|not in (the )?graph|vintage|refresh(ed)? (fixed|resolved)|re-?index", re.I)),
    ("BAD-INPUT", re.compile(r"not found|no such|unknown|unrecognized|ambiguous|usage:|wrong (name|arg)|typo|invalid|no config|NO_CONFIG|bad (script|path)|did not match", re.I)),
    ("TOOL-BROKEN", re.compile(r"traceback|exception|charmap|unicode|codec|timeout|timed out|hang|crash|TypeError|KeyError|AttributeError|exit 2|rc=2|broken|regression|defect in", re.I)),
]


def classify_fail(r) -> str:
    text = (r.get("note", "") + " " + r.get("command", ""))
    if not r.get("note", "").strip():
        # command can still carry fixture markers (e.g. definitely_not_a_thing)
        for name, rx in TAXONOMY[:1]:
            if rx.search(text):
                return name
        if re.search(r"not_a_thing|nonexistent|zzz|dummy", text, re.I):
            return "FIXTURE"
        return "NO-NOTE"
    for name, rx in TAXONOMY:
        if rx.search(text):
            return name
    return "OTHER"


def is_auto(r) -> bool:
    joined = (r.get("command", "") + " " + r.get("raw", ""))
    for tool, rx in AUTO_SIGS:
        if tool in r.get("tools", []) and rx.search(joined):
            return True
    return False


def main() -> int:
    if not SNAP.exists():
        sys.exit("phase1: snapshot missing -- run msbeff_log_audit.py --json first")
    d = json.loads(SNAP.read_text(encoding="utf-8"))
    rows = d["rows"]

    auto, chosen = [], []
    for r in rows:
        (auto if is_auto(r) else chosen).append(r)
    print(f"DENOMINATOR: {len(rows)} rows -> AUTO {len(auto)} ({100*len(auto)/len(rows):.1f}%) / "
          f"CHOSEN {len(chosen)} ({100*len(chosen)/len(rows):.1f}%)  [AUTO is a signature FLOOR]")

    print("\n== CHOSEN rows by month (the real behavioral trend) ==")
    cm = Counter(r["month"] for r in chosen)
    am = Counter(r["month"] for r in auto)
    for mth in sorted(cm):
        print(f"  {mth}  chosen {cm[mth]:5d}   auto {am.get(mth, 0):5d}")

    print("\n== CHOSEN tool usage (top 25; semantic layer on real choices) ==")
    cu = Counter(t for r in chosen for t in r["tools"])
    for t, n in cu.most_common(25):
        print(f"  {t:22s} {n:5d}")

    print("\n== CHOSEN per agent (top 15; behavioral) ==")
    ca = Counter(r["agent"] for r in chosen)
    days = defaultdict(set)
    for r in chosen:
        days[r["agent"]].add(r["date"])
    for a, n in ca.most_common(15):
        print(f"  {a:38s} {n:5d} rows / {len(days[a]):3d} days ({n/len(days[a]):.1f}/day)")

    fails = [r for r in rows if r["result"] == "FAIL"]
    tax = Counter()
    per_tool_tax = defaultdict(Counter)
    buckets = defaultdict(list)
    for r in fails:
        c = classify_fail(r)
        tax[c] += 1
        buckets[c].append(r)
        for t in r["tools"]:
            per_tool_tax[t][c] += 1

    print(f"\n== FAIL TAXONOMY ==  denominator {len(fails)} FAIL rows")
    for c, n in tax.most_common():
        print(f"  {c:12s} {n:5d}  ({100*n/len(fails):.1f}%)")

    print("\n== TAXONOMY x TOP TOOLS (rows>=20 fails) ==")
    for t, cnt in sorted(per_tool_tax.items(), key=lambda kv: -sum(kv[1].values())):
        total = sum(cnt.values())
        if total < 20:
            continue
        parts = " ".join(f"{c}:{n}" for c, n in cnt.most_common())
        print(f"  {t:16s} {total:4d}  {parts}")

    print("\n== SAMPLE per bucket (up to 5 each) ==")
    for c in tax:
        print(f"  -- {c} --")
        for r in buckets[c][:5]:
            note = (r.get('note') or r.get('command') or '')[:130]
            print(f"     {r['date']} {r['agent'][:22]:22s} [{','.join(r['tools'])[:24]:24s}] {note}")

    out = HERE / "phase1_split_and_taxonomy.json"
    out.write_text(json.dumps({
        "auto_chosen": {"auto": len(auto), "chosen": len(chosen),
                        "chosen_by_month": dict(cm), "auto_by_month": dict(am),
                        "chosen_tools": dict(cu), "chosen_agents": dict(ca)},
        "fail_taxonomy": dict(tax),
        "per_tool_taxonomy": {t: dict(c) for t, c in per_tool_tax.items()},
        "fail_rows_bucketed": {c: [r["raw"] for r in rs] for c, rs in buckets.items()},
    }, indent=1), encoding="utf-8")
    print(f"\nJSON -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
