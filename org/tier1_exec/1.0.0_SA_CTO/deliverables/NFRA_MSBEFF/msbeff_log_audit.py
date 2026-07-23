#!/usr/bin/env python
"""msbeff-log-audit -- NFRA_MSBEFF programmatic pass over org/compiler-tools-log.md.

The audit substrate for the Opal-efficiency case study (Andrew-direct 2026-07-23): every row of the
rolling compiler-tools log, both schema eras, classified and aggregated along the three audit layers:

  MECHANICAL  -- does the tool run fast/reliably?   (FAIL/PARTIAL/WARN clusters, error-note mining)
  SEMANTIC    -- does the right tool get found?      (tool-usage distribution vs the registered
                 surface; never-used tools; comp-which routing share)
  BEHAVIORAL  -- do agents actually reach for them?  (per-agent adoption, rows-per-active-day,
                 no-TO share, N/A-with-reason rows, era drift)

DENOMINATOR DISCIPLINE: every count prints against its denominator; unparseable rows are COUNTED
and listed, never dropped. A row the parser cannot classify is a finding about the LOG, not noise.

Usage:
  python .tools/msbeff-log-audit.py [--since YYYY-MM-DD] [--json OUT.json] [--fails] [--legacy]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

def _find_ws() -> Path:
    # anchor on the workspace root by content, not by directory depth -- the script must run
    # identically from .tools/, a deliverables folder, or anywhere else in the tree
    for base in (Path(__file__).resolve(), Path.cwd().resolve()):
        for p in [base, *base.parents]:
            if (p / "org/compiler-tools-log.md").exists():
                return p
    sys.exit("msbeff-log-audit: workspace root not found (no org/compiler-tools-log.md upward)")


WS = _find_ws()
LOG = WS / "org/compiler-tools-log.md"
TOOLS_DIR = WS / ".tools"

DATE_RE = re.compile(r"^\|?\s*(\d{4}-\d{2}-\d{2})Z?\s*\|")
RESULT_TOKENS = ("PASS", "FAIL", "PARTIAL", "SKIPPED", "WARN", "N/A", "MIXED", "BLOCKED")
# tool-name extraction: canonical comp-* names anywhere in the tool/command cells
TOOL_RE = re.compile(r"\bcomp-([a-z0-9-]+)\b")
NON_TOOL_SUFFIXES = {"tools", "tool"}  # 'comp-tools' prose mentions, not a tool


def registered_tools() -> set[str]:
    names = set()
    for p in TOOLS_DIR.glob("comp-*"):
        n = p.name[len("comp-"):]
        if n.endswith(".py") or n.endswith(".sh"):
            n = n.rsplit(".", 1)[0]
        names.add(n)
    return names


def parse(since: str | None):
    rows, malformed = [], []
    total_lines = 0
    for raw in LOG.read_text(encoding="utf-8", errors="replace").splitlines():
        total_lines += 1
        line = raw.strip()
        if not line or line.startswith(("#", "-", "```", "|--", "|-", "** ", "**F", ">")):
            continue
        if re.match(r"^\|?\s*DATE\s*\|", line, re.IGNORECASE):
            continue
        m = DATE_RE.match(line)
        if not m:
            # a line with a pipe but no leading date, or a date but no pipe = malformed candidate
            if "|" in line and re.search(r"20\d{2}-\d{2}-\d{2}", line):
                malformed.append(line[:160])
            continue
        date = m.group(1)
        if since and date < since:
            continue
        cells = [c.strip() for c in line.split("|")]
        # normalized: '' , date, agent, to, tool, command, result, note...  (structured >= 6 cells)
        # legacy:            date, agent, to, blob[, blob...]               (free prose, 4-5 cells)
        if cells[0] == "":
            cells = cells[1:]
        if len(cells) < 3:
            malformed.append(line[:160])
            continue
        agent = cells[1]
        to = cells[2] if len(cells) > 2 else ""
        rest = " | ".join(cells[3:])
        result = ""
        structured = False
        if len(cells) >= 6:
            cand = cells[5].rstrip(".").upper()
            for t in RESULT_TOKENS:
                if cand.startswith(t):
                    result = t
                    structured = True
                    break
        if not structured:
            up = rest.upper()
            for t in RESULT_TOKENS:
                if re.search(r"\b" + re.escape(t) + r"\b", up):
                    result = t
                    break
        tools = sorted({t for t in TOOL_RE.findall(rest) if t not in NON_TOOL_SUFFIXES})
        command = cells[4] if len(cells) > 4 else ""
        note = " | ".join(cells[6:]) if len(cells) > 6 else ""
        rows.append({
            "date": date, "month": date[:7], "agent": agent, "to": to,
            "tools": tools, "command": command, "note": note,
            "result": result or "UNSTATED",
            "era": "structured" if structured else "legacy",
            "raw": line[:400],
        })
    return rows, malformed, total_lines


def main() -> int:
    ap = argparse.ArgumentParser(prog="msbeff-log-audit")
    ap.add_argument("--since", default=None)
    ap.add_argument("--json", dest="json_out", default=None)
    ap.add_argument("--fails", action="store_true", help="list FAIL/PARTIAL/WARN rows")
    ap.add_argument("--legacy", action="store_true", help="list legacy-era rows")
    args = ap.parse_args()

    rows, malformed, total_lines = parse(args.since)
    reg = registered_tools()

    used = Counter()
    per_agent = Counter()
    per_agent_days = defaultdict(set)
    per_result = Counter()
    per_month = Counter()
    per_tool_result = defaultdict(Counter)
    era = Counter()
    no_to = 0
    for r in rows:
        per_agent[r["agent"]] += 1
        per_agent_days[r["agent"]].add(r["date"])
        per_result[r["result"]] += 1
        per_month[r["month"]] += 1
        era[r["era"]] += 1
        if r["to"] in ("(no-TO)", "", "N/A", "no-TO"):
            no_to += 1
        for t in r["tools"]:
            used[t] += 1
            per_tool_result[t][r["result"]] += 1

    print(f"DENOMINATOR: {total_lines} lines read -> {len(rows)} rows parsed "
          f"({era['structured']} structured / {era['legacy']} legacy-prose) + "
          f"{len(malformed)} malformed (listed at bottom; counted, not dropped)"
          + (f"; window since {args.since}" if args.since else "; full log"))

    print("\n== ROWS BY MONTH (adoption trend / behavioral) ==")
    for mth in sorted(per_month):
        print(f"  {mth}  {per_month[mth]:5d}")

    print(f"\n== RESULTS (mechanical) ==  denominator {len(rows)} rows")
    for res, n in per_result.most_common():
        print(f"  {res:10s} {n:5d}  ({100*n/len(rows):.1f}%)")

    print(f"\n== TOOL USAGE (semantic) ==  {len(used)} distinct tools referenced; "
          f"registered surface = {len(reg)}")
    for t, n in used.most_common():
        fr = per_tool_result[t]
        bad = fr["FAIL"] + fr["PARTIAL"] + fr["WARN"]
        flag = f"  <-- {bad} FAIL/PARTIAL/WARN" if bad else ""
        mark = "" if t in reg else "  [NOT-ON-DISK]"
        print(f"  {t:22s} {n:5d}{mark}{flag}")

    never = sorted(reg - set(used))
    print(f"\n== REGISTERED BUT NEVER IN THE LOG (semantic/behavioral gap) == {len(never)}/{len(reg)}")
    print("  " + " ".join(never) if never else "  (none)")

    print(f"\n== PER AGENT (behavioral) ==  denominator {len(rows)} rows; no-TO rows = {no_to} "
          f"({100*no_to/len(rows):.1f}%)")
    for a, n in per_agent.most_common(25):
        d = len(per_agent_days[a])
        print(f"  {a:38s} {n:5d} rows / {d:3d} active days ({n/d:.1f}/day)")

    if args.fails:
        print("\n== FAIL/PARTIAL/WARN ROWS (mechanical failure corpus) ==")
        for r in rows:
            if r["result"] in ("FAIL", "PARTIAL", "WARN"):
                print(f"  {r['date']} {r['agent']}: {r['raw'][:200]}")
    if args.legacy:
        print("\n== LEGACY-PROSE ROWS ==")
        for r in rows:
            if r["era"] == "legacy":
                print(f"  {r['date']} {r['agent']}: {r['raw'][:200]}")
    if malformed:
        print(f"\n== MALFORMED LINES ({len(malformed)}) ==")
        for line in malformed:
            print(f"  {line}")

    if args.json_out:
        Path(args.json_out).write_text(json.dumps({
            "denominator": {"lines": total_lines, "rows": len(rows),
                            "malformed": len(malformed), "era": dict(era)},
            "per_month": dict(per_month), "per_result": dict(per_result),
            "per_agent": dict(per_agent), "tool_usage": dict(used),
            "per_tool_result": {t: dict(c) for t, c in per_tool_result.items()},
            "never_used": never, "registered": sorted(reg), "no_to_rows": no_to,
            "rows": rows,
        }, indent=1), encoding="utf-8")
        print(f"\nJSON -> {args.json_out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
