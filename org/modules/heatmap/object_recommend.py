#!/usr/bin/env python3
"""
O3 -- archive-recommendation layer (NFRA_EXPAND Strand-C, HEATMAP_OBJECT). THE GUARDRAIL LEG.

Takes O2's maximal cold subtrees and decides which are SAFE to RECOMMEND for archive -- behind
the load-bearing verify-BEFORE-recommend chain (inherits NFRA_DEBTSCAN never-auto-delete):

  cold != safe-to-delete. A 100%-cold subtree can still be a LIVE-BUT-QUIET dependency (a rarely
  -touched lambda dir that something still deploys; a config path still read). So BEFORE any
  RECOMMEND, run the inbound-reference checks; ANY inbound signal -> HOLD, never recommend.

The two-check chain per candidate:
  1. NAME-VS-EDGE (automated here, via `git grep`): does any tracked file OUTSIDE the subtree
     reference the subtree's path (import / config path / doc link / deploy script)? Any hit -> HOLD.
  2. GRAPH BLAST (cited as MANDATORY pre-action): `comp-blast <node> --direction up
     --check-consumers` -- confirm zero upstream graph dependents. (Not auto-run here: comp-* are
     bash launchers python can't subprocess on Windows -- banked gotcha; wiring the comp-blast
     python-cli-direct call is a follow-on. Until then O3 EMITS the exact command as a required
     gate per RECOMMEND candidate -- the chain is intact, the graph step is human/CI-run.)

CONSERVATIVE: RECOMMEND only if name-clean. ANY reference OR any error/uncertainty -> HOLD. This
tool NEVER acts -- it emits a ranked ADVISORY report (RECOMMEND with evidence + the mandatory
blast command; HOLD with the reference evidence). A human reviews; nothing is ever auto-archived.

Usage:
    python object_recommend.py [--root .] [--top 40] [--all] [--min-files 5] [--json OUT]
Author: 0.4.0_DS_ClientPlatform (NFRA_EXPAND Strand-C, leg O3 -- the guardrail). 2026-06-25.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heat_map import HeatParams  # noqa: E402
from object_freshness import build  # noqa: E402
from object_locality import aggregate_tree, maximal_cold_subtrees  # noqa: E402


def referenced_by(root: str, subtree_dir: str, limit: int = 5) -> list[str]:
    """Tracked files OUTSIDE subtree_dir that reference its path (name-vs-edge inbound check).
    git grep -F (fixed-string) for the subtree path, excluding the subtree's own files. Any hit
    = the cold subtree is still referenced somewhere -> NOT safe to recommend. (Conservative: a
    noisy/common path that over-matches just yields HOLD, the safe direction.)"""
    try:
        r = subprocess.run(
            ["git", "-C", root, "grep", "-l", "-F", "--", subtree_dir,
             ":(exclude)" + subtree_dir + "/*"],
            capture_output=True, text=True, timeout=60)
    except Exception:
        return ["<grep-error>"]   # uncertainty -> treat as referenced -> HOLD (safe)
    if r.returncode not in (0, 1):
        return ["<grep-error>"]
    return [h for h in r.stdout.splitlines() if h][:limit]


def referenced_index(root: str, subtree_dirs: list[str], limit: int = 5,
                     timeout_s: float | None = 180.0) -> dict[str, list[str]]:
    """name-vs-edge inbound check for ALL candidates in ONE git-grep pass (COO-pointed: a
    reference INDEX, not 225 sequential greps -- the real --all perf fix). One
    `git grep -o -E "<alt of all paths>"` emits `file:matched-path` for every reference; we map
    each matched path -> the EXTERNAL files that mention it. Longest-path-first alternation so a
    parent path doesn't shadow a child. Any error -> HOLD-all (conservative/safe)."""
    refs: dict[str, set] = {d: set() for d in subtree_dirs}
    if not subtree_dirs:
        return {}
    # longest-first: prefer the most specific path when one is a prefix of another
    ordered = sorted(subtree_dirs, key=len, reverse=True)
    alt = "|".join(re.escape(d) for d in ordered)
    valid = set(subtree_dirs)
    try:
        # one pass: `git grep -o` emits `file:matched-path` per reference (-I skips binaries)
        # RULE T (OS-s-16 wire): the bound comes from the CALLER's remaining budget, not from a
        # constant. Default unchanged at 180 s so every existing caller behaves identically.
        r = subprocess.run(["git", "-C", root, "grep", "-I", "-o", "-E", "-e", alt],
                           capture_output=True, text=True, timeout=timeout_s)
    except Exception:
        return {d: ["<grep-error>"] for d in subtree_dirs}   # uncertainty -> HOLD all (safe)
    if r.returncode not in (0, 1):
        return {d: ["<grep-error>"] for d in subtree_dirs}
    for line in r.stdout.splitlines():
        fpath, sep, matched = line.partition(":")
        if not sep or matched not in valid:
            continue
        if not (fpath == matched or fpath.startswith(matched + "/")):   # external reference only
            refs[matched].add(fpath)
    return {d: sorted(v)[:limit] for d, v in refs.items()}


def _blast_node(subtree_dir: str) -> str:
    """The graph query for the mandatory pre-action blast check. comp-blast accepts a file/prefix
    -- the subtree dir is the natural query for 'does anything upstream depend on this?'."""
    return f"comp-blast {subtree_dir} --direction up --check-consumers"


def assess(root: str, candidates: list[dict], timeout_s: float | None = 180.0) -> list[dict]:
    ref_map = referenced_index(root, [c["dir"] for c in candidates],
                               timeout_s=timeout_s)   # ONE git-grep pass
    out: list[dict] = []
    for c in candidates:
        refs = ref_map.get(c["dir"], [])
        recommend = len(refs) == 0
        out.append({
            **c,
            "verdict": "RECOMMEND_ARCHIVE" if recommend else "HOLD_REFERENCED",
            "inbound_refs": refs,                       # evidence (empty => name-clean)
            "mandatory_graph_gate": _blast_node(c["dir"]) if recommend else None,
            "note": ("name-clean; RUN the graph gate before acting"
                     if recommend else f"cold but referenced by {len(refs)} file(s) -- DO NOT archive"),
        })
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="O3 archive-recommendation (verify-before-recommend)")
    ap.add_argument("--root", default=".")
    ap.add_argument("--top", type=int, default=40, help="assess the N largest cold subtrees")
    ap.add_argument("--all", action="store_true", help="assess ALL cold subtrees (slower)")
    ap.add_argument("--cold-threshold", type=float, default=0.9)
    ap.add_argument("--min-files", type=int, default=5)
    ap.add_argument("--half-life", type=float, default=30.0)
    ap.add_argument("--json", default="")
    args = ap.parse_args()
    root = os.path.abspath(args.root)

    scores, _ = build(root, HeatParams(half_life_days=args.half_life), time.time())
    cold = maximal_cold_subtrees(aggregate_tree(scores), args.cold_threshold, args.min_files)
    candidates = cold if args.all else cold[:args.top]
    assessed = assess(root, candidates)

    rec = [a for a in assessed if a["verdict"] == "RECOMMEND_ARCHIVE"]
    hold = [a for a in assessed if a["verdict"] == "HOLD_REFERENCED"]
    print("=== O3 archive recommendations (ADVISORY-ONLY -- never auto-archives) ===")
    print(f"  assessed {len(assessed)} of {len(cold)} cold subtrees  "
          f"(name-vs-edge gate; graph-blast gate cited per RECOMMEND)")
    print(f"  RECOMMEND_ARCHIVE: {len(rec)}   |   HOLD_REFERENCED (cold but load-bearing): {len(hold)}")
    print("  -- RECOMMEND (name-clean; MUST pass the cited graph gate before any action) --")
    for a in rec[:args.top]:
        print(f"    {a['n_cold']:5d} cold  {a['oldest_age_days']:.0f}d  {a['dir']}/")
        print(f"          gate: {a['mandatory_graph_gate']}")
    print("  -- HOLD (cold but REFERENCED -- do NOT archive) --")
    for a in hold[:args.top]:
        print(f"    {a['n_cold']:5d} cold  {a['dir']}/  <- ref'd by: {', '.join(a['inbound_refs'][:3])}")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"generated_ts": int(time.time()), "root": root,
                       "advisory_only": True, "never_auto_archives": True,
                       "recommend": rec, "hold": hold}, fh, indent=2)
        print(f"OK: wrote advisory report -> {args.json} ({len(rec)} recommend / {len(hold)} hold)")
    print("  REMINDER: ADVISORY ONLY. Every RECOMMEND still requires the graph-blast gate + human "
          "review before archive. cold != safe.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
