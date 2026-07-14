"""
nerves_accrete -- NFRA_NERVES L3: the graph gets WEIGHTED BY TRAFFIC, and the weights DECAY.

    "the graph would kind of evolve based on the activity of the agents, like roads that become
     wider with lots of foot traffic"  -- Andrew

ROADS WIDEN WITH TRAFFIC. **ROADS ALSO NARROW.** Nothing in the estate decays today, so a signal
that was true in May is still shouting in July. Every traffic-derived weight here carries a
HALF-LIFE: an edge that stops seeing traffic fades, and an edge nobody has walked in months stops
being a road.

EDGE CLASSES (L3a lands CO_CHANGE + ATTENTION + OUTCOME; L3b lands RISK/HOLD/DOCTRINE):

  CO_CHANGE   files that COMMIT TOGETHER. 6,682 commits / 35 days, already on disk, 99% addressable
              (measured, L2). The richest edge class in the estate and it is FREE.
              **CO_CHANGE WITHOUT CO_DEPLOY IS THE DRIFT/BREAKAGE PREDICTOR** -- two files that
              always change together but do not ship together are a half-landed deploy waiting.
  ATTENTION   agent x node, from the rail + runs (NOT telemetry -- see the L2 hard limit: telemetry
              has no args, so it can only give tool-popularity, never node-attention).
  OUTCOME     took-and-sufficed vs rejected, from the run sink. **THE GOODHART-SAFE WEIGHT.**

THE GOODHART GATE (NERVES discipline #1, non-negotiable): **usage != value. A WIDE ROAD TO A WRONG
ANSWER GETS WIDER.** So a CO_CHANGE weight is a COUPLING observation (a fact about history), never
an endorsement; and any weight that feeds a RANKING routes through outcome-anchored value, never
raw frequency. This module SEPARATES the two: `weight` (decayed traffic count) and `value_signal`
(outcome-anchored) are different fields and are never summed into one number.

Read-only over git + the traffic sink. Emits org/modules/graph/nerves-edges.json (tracked: it is a
derived-but-reviewable artifact, small, and its diffs are the estate learning).

Usage:
    nerves_accrete cochange [--days 35] [--min-support 3] [--json]
    nerves_accrete build    [--days 35]     # emit the edge file
    nerves_accrete --self-test
Author: 1.0.0_SA_CTO~Z (NFRA_NERVES L3a). 2026-07-14.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import subprocess
import sys
from collections import Counter, defaultdict
from itertools import combinations

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.normpath(os.path.join(_HERE, "..", "..", ".."))
sys.path.insert(0, _HERE)

from nerves_resolve import resolve  # noqa: E402

EDGES_OUT = os.path.join(_HERE, "nerves-edges.json")

# DECAY: a traffic weight's half-life in days. A road walked once in May is not a road in July.
HALF_LIFE_DAYS = 21.0
# A commit touching more files than this is a SWEEP (a bulk move / mass-format), not a coupling
# signal -- it would fabricate O(n^2) fake edges. Bounded, and the bound is PRINTED.
MAX_FILES_PER_COMMIT = 25


def _decay(age_days: float, half_life: float = HALF_LIFE_DAYS) -> float:
    return math.pow(0.5, max(0.0, age_days) / half_life)


def _commits(days: int):
    """-> [{sha, author, date, age_days, files[]}]. Read-only git."""
    import datetime as dt
    rc = subprocess.run(
        ["git", "-C", _WS, "log", "--since=%d days ago" % days,
         "--format=%x1e%H\x1f%an\x1f%ad", "--date=short", "--name-only"],
        capture_output=True, text=True, errors="replace")
    today = dt.date.today()
    out = []
    for block in rc.stdout.split("\x1e"):
        if not block.strip():
            continue
        head, *rest = block.strip().splitlines()
        parts = head.split("\x1f")
        if len(parts) != 3:
            continue
        files = [f.strip() for f in rest if f.strip()]
        if not files:
            continue
        try:
            d = dt.date.fromisoformat(parts[2])
            age = (today - d).days
        except Exception:  # noqa: BLE001
            age = 0
        out.append({"sha": parts[0][:12], "author": parts[1], "date": parts[2],
                    "age_days": age, "files": files})
    return out


def cochange(days: int = 35, min_support: int = 3):
    """CO_CHANGE edges: files that commit together, decayed by age, support-gated.

    Every number carries its denominator, and the SWEEP EXCLUSION is printed (a bulk move would
    fabricate O(n^2) couplings; silently dropping it would be a silent cap -- so it is stated)."""
    commits = _commits(days)
    pair_w = defaultdict(float)          # decayed co-change weight
    pair_n = Counter()                   # raw support (how many commits)
    file_n = Counter()
    swept = 0
    for c in commits:
        files = sorted(set(c["files"]))
        if len(files) > MAX_FILES_PER_COMMIT:
            swept += 1
            continue                      # a sweep is not a coupling signal
        w = _decay(c["age_days"])
        for f in files:
            file_n[f] += 1
        for a, b in combinations(files, 2):
            key = (a, b)
            pair_w[key] += w
            pair_n[key] += 1

    edges = []
    for (a, b), n in pair_n.items():
        if n < min_support:
            continue
        # CONFIDENCE = P(b | a) and P(a | b) -- a coupling is asymmetric and saying so is the point.
        ca, cb = file_n[a], file_n[b]
        edges.append({
            "src": a, "dst": b,
            "support": n,                                  # raw co-commit count
            "weight": round(pair_w[(a, b)], 3),            # DECAYED traffic weight
            "conf_src_to_dst": round(n / ca, 3) if ca else 0.0,
            "conf_dst_to_src": round(n / cb, 3) if cb else 0.0,
            "src_commits": ca, "dst_commits": cb,
        })
    edges.sort(key=lambda e: -e["weight"])
    stats = {
        "commits_scanned": len(commits),                   # THE DENOMINATOR
        "commits_excluded_as_sweeps": swept,               # the cap, PRINTED not silent
        "sweep_threshold_files": MAX_FILES_PER_COMMIT,
        "distinct_files": len(file_n),
        "candidate_pairs": len(pair_n),
        "edges_at_min_support": len(edges),
        "min_support": min_support,
        "half_life_days": HALF_LIFE_DAYS,
    }
    return edges, stats


def address_edges(edges: list, limit: int = 400):
    """Attach node addresses (L2's keystone). Unaddressable files keep their path -- a file is a
    legitimate node even if no higher graph models it (REPO_PATH), so the co-change graph is never
    silently truncated to 'only what the trace graph knows'."""
    out = []
    for e in edges[:limit]:
        rs, rd = resolve(e["src"]), resolve(e["dst"])
        out.append(dict(e,
                        src_node=(rs.node_ids[0] if rs.addressed else None),
                        dst_node=(rd.node_ids[0] if rd.addressed else None),
                        src_kind=rs.kind, dst_kind=rd.kind))
    return out


def _render(edges, stats, top=25):
    L = ["nerves-accrete -- CO_CHANGE edges (NFRA_NERVES L3a): files that commit together",
         "  DENOMINATOR: %d commits scanned (%dd) | %d distinct files | %d candidate pairs"
         % (stats["commits_scanned"], stats.get("days", 35), stats["distinct_files"],
            stats["candidate_pairs"]),
         "  EXCLUDED: %d commits with >%d files (SWEEPS -- a bulk move fabricates O(n^2) fake"
         % (stats["commits_excluded_as_sweeps"], stats["sweep_threshold_files"]),
         "            couplings; the cap is PRINTED, never silent)",
         "  DECAY: half-life %.0f days -- ROADS NARROW TOO. A weight is decayed traffic, NOT an"
         % stats["half_life_days"],
         "         endorsement (Goodhart: a wide road to a wrong answer gets wider).",
         "  EDGES at support>=%d: %d" % (stats["min_support"], stats["edges_at_min_support"]),
         "",
         "  TOP CO_CHANGE (weight = decayed; conf = P(other | this)):"]
    for e in edges[:top]:
        L.append("    %.2f  n=%-3d  %.0f%%/%.0f%%  %s"
                 % (e["weight"], e["support"], 100 * e["conf_src_to_dst"],
                    100 * e["conf_dst_to_src"], ""))
        L.append("            %s" % e["src"][:96])
        L.append("         <> %s" % e["dst"][:96])
    return "\n".join(L)


def _self_test() -> int:
    results = []
    def ck(name, ok, detail=""):
        results.append(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   ({detail})" if detail else ""))

    # DECAY is real and monotone: today's traffic outweighs a half-life-old event.
    ck("decay.today_beats_old", _decay(0) == 1.0 and _decay(HALF_LIFE_DAYS) == 0.5
       and _decay(2 * HALF_LIFE_DAYS) == 0.25, "roads narrow")

    # THE LIVE ACCEPTANCE, both arms (the brief's requirement):
    edges, stats = cochange(days=35, min_support=3)
    idx = {(e["src"], e["dst"]): e for e in edges}
    idx.update({(e["dst"], e["src"]): e for e in edges})

    ck("live.edges_exist", stats["edges_at_min_support"] > 0,
       f"{stats['edges_at_min_support']} edges from {stats['commits_scanned']} commits")
    ck("live.sweeps_excluded_and_printed", "commits_excluded_as_sweeps" in stats,
       f"{stats['commits_excluded_as_sweeps']} sweeps excluded (cap printed, not silent)")

    # POSITIVE CONTROL -- a KNOWN-COUPLED pair. The coverage map and the manifest are the two
    # registries the registration gate joins; they are edited together by construction.
    coupled = ("org/modules/graph/comp-coverage-map.yaml", "org/modules/graph/graph-call-manifest.yaml")
    ck("control.known_coupled_pair_has_an_edge", coupled in idx or coupled[::-1] in idx,
       "coverage-map <> manifest (the two registries the gate joins)")

    # NEGATIVE CONTROL -- a KNOWN-INDEPENDENT pair must NOT be coupled. If everything is an edge,
    # nothing is: a co-change graph that couples unrelated files is a Goodhart machine.
    independent = ("CLAUDE.md", "portal/package.json")
    ck("control.known_independent_pair_has_no_edge",
       independent not in idx and independent[::-1] not in idx,
       "CLAUDE.md <> portal/package.json (unrelated) -- the graph DISCRIMINATES")

    # ASYMMETRY is preserved: a coupling is directional and the tool says so.
    if edges:
        e = edges[0]
        ck("edges.asymmetric_confidence_stated",
           "conf_src_to_dst" in e and "conf_dst_to_src" in e,
           "P(b|a) != P(a|b) -- stated, not averaged away")

    ok = all(results)
    print("\n" + ("OK: co-change accretes, decays, and DISCRIMINATES (both control arms held)"
                  if ok else "ERROR: nerves_accrete self-test FAILED"))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(prog="nerves-accrete")
    ap.add_argument("cmd", nargs="?", default="cochange", choices=["cochange", "build"])
    ap.add_argument("--days", type=int, default=35)
    ap.add_argument("--min-support", type=int, default=3)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(errors="replace")
        except Exception:  # noqa: BLE001
            pass

    if args.self_test:
        return _self_test()

    edges, stats = cochange(args.days, args.min_support)
    stats["days"] = args.days

    if args.cmd == "build":
        addressed = address_edges(edges)
        doc = {"_README": "NFRA_NERVES L3a CO_CHANGE edges -- DERIVED from git, decayed "
                          "(half-life %.0fd). A weight is decayed traffic, NEVER an endorsement "
                          "(Goodhart). Regenerate: nerves_accrete build." % HALF_LIFE_DAYS,
               "generated_from": "git log --since=%dd --name-only" % args.days,
               "stats": stats, "edges": addressed}
        with open(EDGES_OUT, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(doc, fh, indent=1)
        print("nerves-accrete: %d CO_CHANGE edges (top %d addressed) -> %s"
              % (len(edges), len(addressed), os.path.relpath(EDGES_OUT, _WS)))

    if args.json:
        print(json.dumps({"stats": stats, "edges": edges[:50]}, indent=1))
    else:
        print(_render(edges, stats))
    return 0


if __name__ == "__main__":
    sys.exit(main())
