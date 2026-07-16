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


class TreeAgg(dict):
    """{dir: stats} PLUS the rollup's own coverage disclosure.

    Subclasses dict so every existing consumer is byte-identical (.items(), [k], iteration,
    len() all unchanged -- maximal_cold_subtrees() cannot see a difference); the denominator
    rides as ATTRIBUTES rather than reserved keys, because a magic "__coverage__" key would be
    walked by every dir-iterating consumer and read as a directory named __coverage__.

    clustered_n: scores that reached >= 1 cluster.  total_n: scores handed in.
    clustered_n < total_n means the rollup silently does not cover every item you gave it.
    """

    clustered_n: int = 0
    total_n: int = 0


def _ancestors(path: str) -> list[str]:
    """Locality keys for a path, root-first: 'a/b/c/f.py' -> ['a', 'a/b', 'a/b/c'].

    A ROOT-LEVEL (slash-less) path IS ITS OWN LOCUS -> 'README.md' -> ['README.md'].
    (CTO ruling 2026-07-16 135028Z, the strong form: it makes the rollup denominator whole at
    the same cost as merely disclosing a drop. Self-as-locus beats a synthetic '<root>' bucket,
    which would have split a root FOLDER node from its own subtree cluster -- 'Cottonwood' the
    node landing in '<root>' while 'Cottonwood/*' rolled up under 'Cottonwood'.)

    THE LAST SEGMENT IS OTHERWISE DROPPED AS A FILENAME, so a NESTED folder node keeps its own
    name eaten: 'a/b/somefolder' -> ['a', 'a/b'] -- its self-heat rolls into its parents and it
    is never its own key. For a subtree rollup that is defensible and is NOT changed here; just
    know that n is a NODE count, not a file count, whenever folders are in the scored set.

    THE BUG THIS FIXES (measured, not theorized -- 0.8.0_AE_CloudComp~Z's MS_GRAPH index at the
    HEATMAP_OBJECT owner review, 2026-07-16): 82 slash-less of 5,560 scored nodes (69 root-level
    MS_FOLDER + 13 MS_FILE) returned [] here, carried cluster="", and contributed to ZERO
    rollups -- no error, no warning, no count. ALL 82 were band=cold. The drop was therefore not
    neutral: it removed the exact population a cold-subtree analytic exists to surface, and it
    removed it at the TOP of the tree, which is precisely where maximal_cold_subtrees() is
    designed to archive ("archive at the top, not per-nested-dir").
    """
    parts = path.replace("\\", "/").split("/")[:-1]   # drop the filename
    if not parts:
        return [path.replace("\\", "/")] if path else []   # root-level item IS its own locus
    return ["/".join(parts[:i + 1]) for i in range(len(parts))]


def aggregate_tree(scores: list[HeatScore]) -> TreeAgg:
    """Roll per-file heat up the directory hierarchy: every ancestor dir accumulates the SUBTREE
    counts (n / n_cold / oldest_age / score-sum). Returns a TreeAgg (a dict of
    {dir: {n, n_cold, cold_frac, oldest_age_days, mean_score, depth}}) whose clustered_n /
    total_n attributes DISCLOSE the rollup's coverage -- assert clustered_n == total_n if you
    are assigning a cluster per node, rather than trusting that every item found a home.
    """
    agg = TreeAgg()
    clustered = 0
    for s in scores:
        is_cold = s.band == "cold"
        keys = _ancestors(s.item_id)
        if keys:
            clustered += 1
        for d in keys:
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
    agg.clustered_n = clustered
    agg.total_n = len(scores)
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


def _self_test() -> int:
    """Pin the root-locus fix + the coverage disclosure. Exercised, not asserted-by-reading."""
    from heat_map import score_items   # noqa: PLC0415 -- self-test-only import

    now, day = 1_000_000_000.0, 86400.0
    old = now - 200 * day   # cold

    # 1. THE FIX: a root-level item is its own cluster key (was: dropped to no cluster at all).
    agg = aggregate_tree(score_items([("README.md", old)], now))
    assert "README.md" in agg, "root-level item must be its own locus"
    assert agg["README.md"]["n"] == 1
    assert agg.clustered_n == agg.total_n == 1, "coverage must be whole"

    # 2. REGRESSION PIN: nested paths behave exactly as before the fix.
    agg = aggregate_tree(score_items([("a/b/c/f.py", old)], now))
    assert sorted(agg.keys()) == ["a", "a/b", "a/b/c"], "nested rollup must be unchanged"
    assert agg.clustered_n == agg.total_n == 1

    # 3. THE CTO-SHAPE PROPERTY: a root FOLDER node joins its OWN subtree cluster, rather than
    #    being split off into a synthetic '<root>' bucket away from its own children.
    agg = aggregate_tree(score_items([("Cottonwood", old), ("Cottonwood/f.py", old)], now))
    assert agg["Cottonwood"]["n"] == 2, "root folder must land in its own subtree cluster"
    assert agg.clustered_n == agg.total_n == 2

    # 4. THE ORIGINAL BUG, PINNED SO IT CANNOT SILENTLY RETURN: mixed root + nested, all covered.
    scores = score_items([("nested/deep/f1.py", old), ("nested/deep/f2.py", old),
                          ("ROOTLEVEL.md", old), ("ALSO_ROOT.txt", old)], now)
    agg = aggregate_tree(scores)
    assert agg.clustered_n == agg.total_n == 4, "the 82-node drop class must not recur"
    assert "ROOTLEVEL.md" in agg and "ALSO_ROOT.txt" in agg

    # 5. THE MUTANT -- prove the disclosure CAN fail. An instrument that cannot report a gap is
    #    not an instrument; without this the clustered_n==total_n assertions above are vacuous.
    agg = aggregate_tree(score_items([("", old), ("real/f.py", old)], now))
    assert agg.clustered_n == 1 and agg.total_n == 2, \
        "coverage disclosure must FALL when an item reaches no cluster"

    print("OK: object_locality self-test passed (5/5) -- root-locus fix, nested regression pin,")
    print("    root-folder-joins-own-subtree, the 82-node drop class, and the mutant that proves")
    print("    the coverage disclosure can actually fail.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="O2 filesystem-locality clustering (cold subtrees)")
    ap.add_argument("--self-test", action="store_true", help="run the pinned self-test and exit")
    ap.add_argument("--root", default=".")
    ap.add_argument("--cold-threshold", type=float, default=0.9, help="min subtree cold_frac to flag")
    ap.add_argument("--min-files", type=int, default=5, help="min files in a flagged subtree")
    ap.add_argument("--half-life", type=float, default=30.0)
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--json", default="")
    args = ap.parse_args()
    if args.self_test:
        return _self_test()
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
    # Denominator, printed unconditionally: the rollup's coverage of what it was handed.
    # Never a WARN-only line -- a disclosure that only prints when it is bad is invisible on
    # every good day, and its silence then reads as "covered everything" (which is how the
    # 82-node drop stayed invisible in the first place).
    print(f"  rollup coverage: {agg.clustered_n:,}/{agg.total_n:,} scored items clustered"
          + ("" if agg.clustered_n == agg.total_n
             else f"  <-- {agg.total_n - agg.clustered_n:,} UNCOVERED (empty item_id)"))
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
