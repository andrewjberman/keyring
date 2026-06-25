#!/usr/bin/env python3
"""
O2 -- filesystem-locality clustering (NFRA_EXPAND Strand-C, HEATMAP_OBJECT).

A whole COLD SUBTREE is a far stronger archive signal than scattered cold files ("this DIR is
dead" vs "these 3 files are old"). O2 rolls the O1 per-path heat up the DIRECTORY HIERARCHY and
finds the MAXIMAL cold subtrees -- the highest directory whose entire subtree is (near-)uniformly
cold. O3 (recommendation, advisory) consumes these; O4 reports them.

Builds on S0 (heat_map) + O1 (object_freshness.build); a filesystem is inherently a tree, so this
is a native hierarchical roll-up -- NOT a generic similarity-cluster. (Scoping referenced
"reuse comp-cluster/TSGRAPH"; grounded 2026-06-25: no comp-cluster tool exists + TSGRAPH is a
spike, so the native dir-tree roll-up is both the available and the correct primitive here.)

ADVISORY-ONLY: O2 identifies + ranks cold subtrees. It does NOT recommend-to-delete (O3, behind
the NFRA_DEBTSCAN never-auto-delete + blast-radius verify-before-recommend chain) and never acts.

Usage:
    python object_locality.py [--root .] [--cold-threshold 0.9] [--min-files 5] [--top 30] [--json OUT]
Author: 0.4.0_DS_ClientPlatform (NFRA_EXPAND Strand-C, leg O2). 2026-06-25.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heat_map import HeatParams, HeatScore  # noqa: E402
from object_freshness import build  # noqa: E402


def _ancestors(path: str) -> list[str]:
    """Directory ancestors of a path, root-first: 'a/b/c/f.py' -> ['a', 'a/b', 'a/b/c']."""
    parts = path.replace("\\", "/").split("/")[:-1]   # drop the filename
    return ["/".join(parts[:i + 1]) for i in range(len(parts))]


def aggregate_tree(scores: list[HeatScore]) -> dict[str, dict]:
    """Roll per-file heat up the directory hierarchy: every ancestor dir accumulates the SUBTREE
    counts (n / n_cold / oldest_age / score-sum). Returns {dir: {n, n_cold, cold_frac,
    oldest_age_days, mean_score, depth}}."""
    agg: dict[str, dict] = {}
    for s in scores:
        is_cold = s.band == "cold"
        for d in _ancestors(s.item_id):
            a = agg.get(d)
            if a is None:
                a = agg[d] = {"n": 0, "n_cold": 0, "oldest_age_days": 0.0,
                              "_score_sum": 0.0, "depth": d.count("/") + 1}
            a["n"] += 1
            a["n_cold"] += 1 if is_cold else 0
            a["oldest_age_days"] = max(a["oldest_age_days"], s.age_days)
            a["_score_sum"] += s.score
    for d, a in agg.items():
        a["cold_frac"] = a["n_cold"] / a["n"] if a["n"] else 0.0
        a["mean_score"] = a["_score_sum"] / a["n"] if a["n"] else 0.0
        del a["_score_sum"]
    return agg


def maximal_cold_subtrees(agg: dict[str, dict], cold_threshold: float = 0.9,
                          min_files: int = 5) -> list[dict]:
    """The MAXIMAL cold subtree roots: a dir whose subtree is >= cold_threshold cold (and has
    >= min_files), whose PARENT is NOT itself a qualifying cold subtree. Reporting only the
    maximal root avoids listing a/b/c, a/b, a when the whole of a/ is cold -- archive at the
    top, not per-nested-dir. Ranked by cold file count, then age."""
    def qualifies(d: str) -> bool:
        a = agg.get(d)
        return bool(a) and a["n"] >= min_files and a["cold_frac"] >= cold_threshold

    roots: list[dict] = []
    for d, a in agg.items():
        if not qualifies(d):
            continue
        parent = d.rsplit("/", 1)[0] if "/" in d else ""
        if parent and qualifies(parent):
            continue   # not maximal -- the parent subtree already covers it
        roots.append({"dir": d, "n": a["n"], "n_cold": a["n_cold"],
                      "cold_frac": round(a["cold_frac"], 4),
                      "oldest_age_days": round(a["oldest_age_days"], 1),
                      "mean_score": round(a["mean_score"], 6), "depth": a["depth"]})
    roots.sort(key=lambda r: (-r["n_cold"], -r["oldest_age_days"]))
    return roots


def main() -> int:
    ap = argparse.ArgumentParser(description="O2 filesystem-locality clustering (cold subtrees)")
    ap.add_argument("--root", default=".")
    ap.add_argument("--cold-threshold", type=float, default=0.9, help="min subtree cold_frac to flag")
    ap.add_argument("--min-files", type=int, default=5, help="min files in a flagged subtree")
    ap.add_argument("--half-life", type=float, default=30.0)
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--json", default="")
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    now_ts = time.time()

    scores, _src = build(root, HeatParams(half_life_days=args.half_life), now_ts)
    agg = aggregate_tree(scores)
    cold = maximal_cold_subtrees(agg, args.cold_threshold, args.min_files)

    n_files_in_cold = sum(r["n"] for r in cold)
    print(f"=== O2 locality: maximal COLD SUBTREES  root={root} ===")
    print(f"  {len(scores):,} files -> {len(cold)} maximal cold subtree(s) "
          f"(>= {args.cold_threshold:.0%} cold, >= {args.min_files} files), "
          f"covering {n_files_in_cold:,} files")
    print(f"  top {min(args.top, len(cold))} by cold-file count (archive candidates -> O3):")
    for r in cold[:args.top]:
        print(f"    {r['n_cold']:5d}/{r['n']:<5d} cold  {r['cold_frac']:.0%}  "
              f"oldest={r['oldest_age_days']:.0f}d  {r['dir']}/")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"generated_ts": int(now_ts), "root": root,
                       "cold_threshold": args.cold_threshold, "min_files": args.min_files,
                       "n_files": len(scores), "maximal_cold_subtrees": cold}, fh, indent=2)
        print(f"OK: wrote cold-subtree snapshot -> {args.json} ({len(cold)} subtrees)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
