"""comp_cochange.py -- agent-type CO-MOVEMENT over git history (comp-cochange engine).

SOVEREIGN BASIS: Andrew ~1945Z @22f33727a ("comp-cochange (for git change records tagged
by agent types)... incorporated into the kimi metaanalysis segment"). ARCH CONSTRAINTS:
CTO 200144Z verbatim -- typed dispatch over EXISTING substrate, no new git-walking engine,
read-only, no LLM, denominators printed. INSTRUMENT DEFINITION: CTO~B F4 -- agent-type
CO-MOVEMENT with BOTH denominators on every output: commits-attributed/total AND
pairs-observed/possible. CONSUMER: the State/Friction design's Friction battery (third
leg beside comp-blast overlap + comp-heat trajectory) -- the Kimi meta-analysis segment.

SUBSTRATE DISPATCH (the no-new-walker constraint, honored structurally): the ONLY git
access in this module is `comp_missions.commits()` -- the attribution-grade walk that
already carries the sentinel-parsing and DAG-range lessons (.tools/comp_missions.py:71,
its own comments are the record). This module never invokes git. The agent-type tag
source is the author-serial convention (safe-commit --author "N.N.N_TT_Name[~lane]").

WHAT CO-MOVEMENT MEANS HERE (F4): two agent TYPES co-move when both touch the SAME FILE
within the window (commit grain preserved underneath: per-pair evidence lists the shared
files and each side's commit counts on them). This is COUPLING EVIDENCE, not verdict:
a high co-movement pair is a friction/coordination surface for the battery to weigh --
the tool prints observations + denominators, never conclusions (no LLM, no judgment).

READ-ONLY: no writes anywhere. Every output carries: HEAD anchor (vintage law), the
window expression, and BOTH F4 denominators. UNATTRIBUTED commits (authors outside the
serial convention, e.g. human operators) are COUNTED IN THE TOTAL and excluded from
pairs -- visible in the attribution denominator, never silently dropped.

Modes:
  matrix (default)   -- ranked pair table over the window
  pair <T1> <T2>     -- one pair's shared-file evidence
  file <path-substr> -- co-movement around matching files: which types touch them,
                        and what else those same commits touched (classic co-change)
  --self-test        -- serial-parse fixtures + a live 5-commit smoke walk

Usage:
  comp-cochange [matrix] [--since "14 days ago" | --range A..B] [--min-shared 1]
                [--top 20] [--grain type|serial] [--json]
  comp-cochange pair DS AE [--since ...]
  comp-cochange file dim_mdpf_aum_metrics [--since ...]
Author: 0.2.0_DS_PortfolioAnalytics (ADHOC.comp-cochange-build). ASCII only.
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

_TOOLS = Path(__file__).resolve().parents[3] / ".tools"
sys.path.insert(0, str(_TOOLS))
import comp_missions  # noqa: E402  -- THE substrate; this module never calls git itself

# The author-serial convention: N.N.N_TT_Name[~lane]. TYPE = the role segment.
_SERIAL_RE = re.compile(r"\b\d+\.\d+\.\d+_([A-Z]{2,4})_")


def agent_tag(author: str, grain: str) -> str | None:
    """Author string -> agent tag at the requested grain, or None (UNATTRIBUTED)."""
    if grain == "serial":
        m = re.search(r"\b(\d+\.\d+\.\d+_[A-Z]{2,4}_[A-Za-z0-9]+(~[A-Z])?)", author)
        return m.group(1) if m else None
    m = _SERIAL_RE.search(author)
    return m.group(1) if m else None


def walk(since: str | None, rng: str | None):
    """Dispatch the substrate walk. RANGE: prefix = DAG range (comp_missions' own
    author-date-nonmonotonic lesson); plain string = git --since expression."""
    expr = f"RANGE:{rng}" if rng else (since or "14 days ago")
    return comp_missions.commits(expr, None)


def head_anchor() -> str:
    cs = comp_missions.commits("RANGE:HEAD~1..HEAD", None)
    if cs:
        c = cs[0]
        return f"{c['short']}  {c['iso']}  {c['author'][:30]}"
    return "(unresolvable)"


def tag_commits(cs: list, grain: str):
    """Split the walk into (attributed[(tag, commit)], total, untagged_authors)."""
    attributed, untagged = [], Counter()
    for c in cs:
        t = agent_tag(c["author"], grain)
        if t:
            attributed.append((t, c))
        else:
            untagged[c["author"]] += 1
    return attributed, untagged


def build_pairs(attributed, min_shared: int):
    """Core F4 aggregation. Returns (pair_rows, active_tags, possible, observed)."""
    files_by_tag: dict[str, Counter] = defaultdict(Counter)   # tag -> file -> commit count
    for tag, c in attributed:
        for p in c["paths"]:
            files_by_tag[tag][p] += 1
    active = sorted(files_by_tag)
    rows = []
    for a, b in itertools.combinations(active, 2):
        shared = set(files_by_tag[a]) & set(files_by_tag[b])
        if len(shared) < min_shared:
            continue
        union = set(files_by_tag[a]) | set(files_by_tag[b])
        top = sorted(shared, key=lambda f: -(files_by_tag[a][f] + files_by_tag[b][f]))
        rows.append({
            "pair": [a, b],
            "shared_files": len(shared),
            "jaccard": round(len(shared) / len(union), 4) if union else 0.0,
            "commits_a_on_shared": int(sum(files_by_tag[a][f] for f in shared)),
            "commits_b_on_shared": int(sum(files_by_tag[b][f] for f in shared)),
            "top_shared": top[:5],
        })
    rows.sort(key=lambda r: -r["shared_files"])
    possible = len(active) * (len(active) - 1) // 2
    return rows, active, possible, len(rows)


def denominator_block(total: int, attributed_n: int, untagged: Counter,
                      observed: int, possible: int) -> dict:
    return {
        "commits_attributed": attributed_n,
        "commits_total": total,
        "unattributed_authors": dict(untagged.most_common(5)),
        "pairs_observed": observed,
        "pairs_possible": possible,
    }


def fmt_denoms(d: dict) -> list[str]:
    ua = ", ".join(f"{k} x{v}" for k, v in d["unattributed_authors"].items()) or "-"
    return [
        f"DENOMINATOR 1 (F4): commits-attributed {d['commits_attributed']} / total "
        f"{d['commits_total']} (unattributed counted, never dropped: {ua})",
        f"DENOMINATOR 2 (F4): pairs-observed {d['pairs_observed']} / possible "
        f"{d['pairs_possible']} (possible = C(active-tags, 2))",
    ]


def header_lines(mode: str, window: str, grain: str) -> list[str]:
    return [
        f"comp-cochange {mode}  |  window: {window}  |  grain: {grain}",
        f"HEAD anchor: {head_anchor()}",
        "substrate: comp-missions commit walk (typed dispatch; this tool runs no git). "
        "READ-ONLY; observations + denominators, never verdicts.",
    ]


def main() -> int:
    ap = argparse.ArgumentParser(description="agent-type co-movement over git history")
    ap.add_argument("mode", nargs="?", default="matrix",
                    choices=["matrix", "pair", "file"])
    ap.add_argument("args", nargs="*", help="pair: T1 T2 | file: path-substring")
    ap.add_argument("--since", default=None, help='git --since expression (default "14 days ago")')
    ap.add_argument("--range", dest="rng", default=None, help="git commit range A..B")
    ap.add_argument("--grain", default="type", choices=["type", "serial"])
    ap.add_argument("--min-shared", type=int, default=1)
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()

    if a.self_test:
        return self_test()

    window = f"range {a.rng}" if a.rng else (a.since or "14 days ago")
    cs = walk(a.since, a.rng)
    attributed, untagged = tag_commits(cs, a.grain)
    rows, active, possible, observed = build_pairs(attributed, a.min_shared)
    denoms = denominator_block(len(cs), len(attributed), untagged, observed, possible)

    if a.mode == "pair":
        if len(a.args) != 2:
            print("usage: comp-cochange pair <T1> <T2>", file=sys.stderr)
            return 2
        want = sorted(t.upper() for t in a.args)
        rows = [r for r in rows if sorted(r["pair"]) == want]

    if a.mode == "file":
        if len(a.args) != 1:
            print("usage: comp-cochange file <path-substring>", file=sys.stderr)
            return 2
        sub = a.args[0]
        touch: dict[str, Counter] = defaultdict(Counter)   # matched file -> tag counts
        cochanged: Counter = Counter()
        for tag, c in attributed:
            hit = [p for p in c["paths"] if sub in p]
            if not hit:
                continue
            for p in hit:
                touch[p][tag] += 1
            for p in c["paths"]:
                if sub not in p:
                    cochanged[p] += 1
        out = {"mode": "file", "match": sub, "window": window,
               "files": {f: dict(t) for f, t in touch.items()},
               "cochanged_top": cochanged.most_common(a.top),
               "denominators": denoms}
        if a.json:
            print(json.dumps(out, indent=2))
        else:
            for line in header_lines("file", window, a.grain):
                print(line)
            print()
            if not touch:
                print(f"NO MATCH: no attributed commit in window touched a path containing "
                      f"{sub!r} (a no-match is a result, not an error)")
            for f, t in sorted(touch.items()):
                print(f"  {f}: " + ", ".join(f"{k} x{v}" for k, v in t.most_common()))
            if cochanged:
                print(f"  co-changed alongside (top {a.top}):")
                for p, n in cochanged.most_common(a.top):
                    print(f"    {n:>3}x  {p}")
            print()
            for line in fmt_denoms(denoms):
                print(line)
        return 0

    out = {"mode": a.mode, "window": window, "grain": a.grain,
           "active_tags": active, "pairs": rows[:a.top], "denominators": denoms}
    if a.json:
        print(json.dumps(out, indent=2))
        return 0
    for line in header_lines(a.mode, window, a.grain):
        print(line)
    print()
    if not rows:
        print("NO CO-MOVEMENT at min-shared >= %d among active tags %s "
              "(a zero is a result, not an error)" % (a.min_shared, active))
    for r in rows[:a.top]:
        print(f"  {r['pair'][0]:>6} x {r['pair'][1]:<6}  shared_files={r['shared_files']:<4} "
              f"jaccard={r['jaccard']:<7} commits {r['commits_a_on_shared']}/{r['commits_b_on_shared']}")
        for f in r["top_shared"][:3]:
            print(f"           {f}")
    print()
    for line in fmt_denoms(denoms):
        print(line)
    return 0


def self_test() -> int:
    """Parse fixtures (pure) + a live 5-commit smoke through the substrate."""
    fixtures = [
        ("0.2.0_DS_PortfolioAnalytics", "type", "DS"),
        ("0.7.0_AE_CloudOps~F", "type", "AE"),
        ("1.0.0_SA_CTO", "type", "SA"),
        ("0.0.0_AB_MSTR", "type", "AB"),
        ("Andrew Berman", "type", None),
        ("0.4.0_DE_ClientPlatform", "serial", "0.4.0_DE_ClientPlatform"),
        ("0.8.0_AE_CloudComp~D <x@y>", "serial", "0.8.0_AE_CloudComp~D"),
    ]
    bad = [(a, g, want, agent_tag(a, g)) for a, g, want in fixtures
           if agent_tag(a, g) != want]
    for a, g, want, got in bad:
        print(f"FAIL parse: {a!r} grain={g} want={want!r} got={got!r}")
    smoke = comp_missions.commits("RANGE:HEAD~5..HEAD", None)
    ok_smoke = len(smoke) >= 1 and all("paths" in c and "author" in c for c in smoke)
    print(f"parse fixtures: {len(fixtures) - len(bad)}/{len(fixtures)} PASS")
    print(f"substrate smoke (HEAD~5..HEAD): {len(smoke)} commits walked, "
          f"fields present: {ok_smoke}")
    return 0 if (not bad and ok_smoke) else 1


if __name__ == "__main__":
    sys.exit(main())
