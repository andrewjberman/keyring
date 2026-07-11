#!/usr/bin/env python3
"""comp-which routing-quality SCORECARD -- the reproducible TO-8 measurement instrument.

NOT a pytest test (no test_ prefix -> not collected): it MEASURES, it doesn't assert. Run it to
reproduce the N=12 catalog-label scorecard (the number that took comp-which from 4/12 to 10/12 rank-1
on 2026-07-10, NFRA_TOOLPASS) + the raw-engine baseline that is TO-8's real target.

  python org/modules/graph/tests/compwhich_routing_scorecard.py

METHOD (TO-8 law, from the TO-7 finding 34f835110):
  - N=12 situations lifted VERBATIM from CLAUDE.md's situation->command table -- a human-authored
    catalog that does NOT share comp_route's scoring predicate (two instruments sharing a predicate
    are one instrument).
  - Routes are read from the launcher's --json output (exact, no human-text regex; --route-only so a
    grep fallback never shells out).
  - The route-ASSERTION harness (pass/fail, CI-enforced) is the sibling test_compwhich_toolpass_rules.py;
    THIS file is the measurement (PICK / SURFACED / ABSENT counts) for tracking the engine over time.

THE ENGINE FINDING (TO-8's real work, not more curated patches): the curated rules carry ALL the hits;
the raw fuzzy/posterior backstop is ~0/12 top-1 on catalog vocabulary. A per-label curated allowlist
always lags the catalog -- the structural fix is the engine's scoring, tracked here.

Read-only, bd-clean. Author: 3.0.0_SA_CVO (NFRA_TOOLPASS comp-which, 2026-07-10).
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

_WS = Path(__file__).resolve().parents[4]
_CW = str(_WS / ".tools" / "comp-which")
_ROUTE = str(_WS / "org" / "modules" / "graph" / "comp_route.py")

# 12 catalog labels (VERBATIM from CLAUDE.md :62-73) -> canonical TOOL(s).
CATALOG = [
    ("Need to grep/find the repo",           {"comp-grep", "comp-glob"}),
    ("What's in the market pipeline?",        {"pipescript"}),
    ("Editing a gold script",                 {"comp-pipescript"}),
    ("Running a gold script",                 {"comp-pipescript"}),
    ("Ad-hoc non-dispatch run",               {"comp-pipescript"}),   # known phrasing artifact (label has "dispatch")
    ("Cross-layer graph question",            {"comp-kuzu"}),
    ("Touching MP/benchmarks/ADVI backend",   {"comp-surface-check"}),
    ("Gold run done, signaling AE",           {"comp-validate"}),
    ("What breaks if I change X?",            {"comp-blast"}),
    ("Modifying a portal component",          {"comp-transform"}),
    ("4xx / HTML-response debugging",         {"comp-routes"}),
    ("New boto3 call / iam.tf change",        {"comp-iam"}),
]


def _launcher_route(q):
    """The AGENT-FACING route: launcher --json --route-only (curated + posterior). (kind, [tools])."""
    out = subprocess.run([sys.executable, _CW, "--json", "--route-only", q],
                         capture_output=True, text=True, timeout=60).stdout
    try:
        o = json.loads(out)
    except Exception:
        return ("parse-error", [])
    tools = [r["tool"] for r in o.get("routed", [])]
    if o.get("kind") == "fallback" and o.get("fallback"):
        tools = [o["fallback"].split()[0]]
    return (o.get("kind", "?"), tools)


def _raw_engine_ranking(q):
    """The raw posterior engine ALONE (the fuzzy backstop, no launcher curated layer) -- TO-8's target.
    Ordered tool list from comp_route.py's 'full ranking' block."""
    out = subprocess.run([sys.executable, _ROUTE, q], capture_output=True, text=True, timeout=60).stdout
    tools, in_block = [], False
    for ln in out.splitlines():
        if "full ranking" in ln:
            in_block = True
            continue
        if in_block:
            s = ln.strip()
            if not s:
                break
            tok = s.split()[0]
            if tok.startswith("comp-") or tok == "pipescript":
                tools.append(tok)
    return tools


def main():
    print("=== comp-which routing scorecard (N=%d catalog labels) ===\n" % len(CATALOG))
    pick = surf = absent = 0
    raw_top1 = raw_top2 = 0
    for q, canon in CATALOG:
        _, tools = _launcher_route(q)
        raw = _raw_engine_ranking(q)
        if tools and tools[0] in canon:
            v = "PICK"
            pick += 1
        elif any(t in canon for t in tools):
            v = "SURFACED"
            surf += 1
        else:
            v = "ABSENT"
            absent += 1
        if raw and raw[0] in canon:
            raw_top1 += 1
        elif any(t in canon for t in raw[:2]):
            raw_top2 += 1
        print("  [%-8s] %-42s -> %-18s (raw#1=%s)" % (v, q[:42], (tools[0] if tools else "-"),
                                                      (raw[0] if raw else "-")))
    N = len(CATALOG)
    print("\n  AGENT-FACING (launcher): PICK %d/%d (%d%%) | +SURFACED %d/%d | ABSENT %d"
          % (pick, N, 100 * pick // N, pick + surf, N, absent))
    print("  RAW ENGINE (fuzzy backstop alone -- TO-8 target): top-1 %d/%d | top-2 %d/%d"
          % (raw_top1, N, raw_top1 + raw_top2, N))
    print("\n  The gap between the two rows = what the curated layer carries and the engine does not.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
