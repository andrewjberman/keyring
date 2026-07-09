#!/usr/bin/env python3
"""
comp-graph -- freshness/status view across every dependency graph (NFRA_GRAPHS D3).

`comp-graph status` answers, in one place, "which graphs exist, how fresh is each,
and when was it last derived" -- the missing operational complement to the
query-vs-rebuild doctrine catalogued in org/modules/graph/graph-call-manifest.yaml.
It reports both the local trace-layer caches (.comp-graph/) and the cloud/
cross-layer artifacts (infra/aws/globgrph/), each with its freshness verdict, age,
TTL, canonical query tool, and rebuild command.

`comp-graph clear [name|all]` drops a local trace-layer cache so the next call
rebuilds it (gitignored cache only -- never touches the cloud artifacts).

Freshness contract -- THREE states (CTO GO 20260709T201214Z):
  - (default) serve the cache iff that tool's freshness PREDICATE says fresh.
  - --check   REPORT staleness, never rebuild.  0 = fresh | 2 = stale | 1 = tool error.
  - --force   always re-derive.
  - --fresh   DEPRECATED no-op alias of default (warns; removed next cycle).

There is no single universal predicate, and this tool must not invent one: the trace graph binds
per-node CONTENT-SHA drift (age is never evaluated on the default path), while graph_cache binds a
stat-only fingerprint AND a TTL. `status` prints each tool's ACTUAL predicate, and takes the trace
verdict by CALLING the enforcer (`cli.trace_freshness`) rather than re-modelling it.

Usage:
    comp-graph status                # freshness table for every graph
    comp-graph status --json         # machine-readable
    comp-graph clear platinum        # drop the comp-platinum caches
    comp-graph clear trace           # drop the trace graph cache
    comp-graph clear all             # drop all local trace-layer caches
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph import graph_cache as gc  # noqa: E402

_CACHE_DIR = _WORKSPACE / ".comp-graph"
_GLOBGRPH_DIR = _WORKSPACE / "infra" / "aws" / "globgrph"

# `_TRACE_TTL = 300` USED TO LIVE HERE. It was a hand-copied second expression modelling a predicate
# the enforcing code does not use: `cli.py::_get_graph`'s default path binds per-node content-SHA
# drift and NEVER evaluates age (the TTL `elif` hangs off `if check_freshness:`). Exercised at
# (age=4000s, drift=0) the old verdict said "STALE (next call rebuilds)" while `_get_graph` SERVED
# the cache -- wrong in both directions. We now CALL the enforcer (`cli.trace_freshness`) and print
# what it returns. MSTR 20260709T200348Z, ratified: a control's reported value and its enforcing
# value must be the SAME EXPRESSION, not two expressions that agree today.
# CTO GO 20260709T201214Z; 0.7.0_AE_CloudOps (tool owner) co-signed 20260709T205010Z.

# The freshness contract's POPULATION, derived from each tool's actual capability -- never inherited
# from the manifest's `rebuild-when-query` token list, which under-collected (it named one launcher
# for a cli.py that backs five) and mis-collected (`comp-aws derive` has no cached read at all).
# Silence about the classes recreates the false-uniformity claim one category over, so status names
# all three (CTO ruling; 0.7.0's framing).
_CONTRACT_TOOLS = ["comp-trace", "comp-blast", "comp-diff", "comp-xref", "comp-platinum",
                   "comp-system"]
_REBUILD_VERB = ["comp-build"]          # default IS the rebuild; --check probes. No warm cached read.
_PURE_PRODUCERS = ["comp-aws derive", "comp-stitch-refresh"]
_QUERY_ONLY = ["comp-kuzu"]


def _fmt_age(seconds) -> str:
    """Human-readable age (e.g. '42s', '7m', '3h', '5d')."""
    if seconds is None:
        return "-"
    s = int(seconds)
    if s < 90:
        return f"{s}s"
    if s < 5400:
        return f"{s // 60}m"
    if s < 172800:
        return f"{s // 3600}h"
    return f"{s // 86400}d"


def _json_built_at(path: Path):
    """Cheaply read a leading `"built_at": <num>` from a graph JSON head."""
    try:
        head = path.read_bytes()[:512].decode("utf-8", errors="replace")
        m = re.search(r'"built_at"\s*:\s*([0-9.]+)', head)
        if m:
            return float(m.group(1))
    except Exception:
        pass
    return None


def _now() -> float:
    return time.time()


def _trace_cli():
    """Import the ENFORCER. Lazy: cli.py pulls the trace-graph machinery, and `comp-graph clear`
    must not pay for it."""
    from org.modules.graph import cli as _cli
    return _cli


def _trace_freshness():
    """Call the enforcing predicate. Fail-closed: if we cannot ASK the enforcer, we do not invent a
    verdict -- an unevaluable status is UNVERIFIABLE, never FRESH."""
    try:
        return _trace_cli().trace_freshness()
    except Exception as e:  # noqa: BLE001
        return "UNVERIFIABLE", f"cannot reach the enforcer ({type(e).__name__}: {e})", 0, []


def _trace_predicate() -> str:
    try:
        return _trace_cli().TRACE_PREDICATE
    except Exception:  # noqa: BLE001
        return "UNKNOWN (enforcer unreachable)"


#: comp-platinum's predicate, named from graph_cache's own contract rather than restated here.
_GC_PREDICATE = f"stat-only (max-mtime, file-count) fingerprint AND age < {gc.DEFAULT_TTL}s TTL"


def _ttl_verdict(exists: bool, age, ttl) -> str:
    if not exists:
        return "MISSING"
    if age is None:
        return "PRESENT"
    return "FRESH" if age < ttl else "STALE"


def _present_verdict(exists: bool) -> str:
    return "PRESENT" if exists else "MISSING"


def _collect():
    """Return the ordered list of graph status records."""
    records = []
    now = _now()

    # --- Local trace layer (.comp-graph/) -----------------------------------
    # Trace graph (comp-trace / comp-blast / comp-diff / comp-xref).
    # VERDICT COMES FROM THE ENFORCER, not from a TTL we keep a copy of. See the _TRACE_TTL note.
    gpath = _CACHE_DIR / "graph.json"
    ba = _json_built_at(gpath) if gpath.exists() else None
    age = (now - ba) if ba else None
    verdict, detail, _n, _drift = _trace_freshness()
    records.append({
        "group": "local", "name": "graph",
        "desc": "trace graph (comp-trace/comp-blast/comp-diff/comp-xref)",
        "path": str(gpath.relative_to(_WORKSPACE)),
        "exists": gpath.exists(), "built_at": ba, "age": age,
        "ttl": None, "verdict": verdict, "detail": detail,
        "predicate": _trace_predicate(),
        "query": "comp-trace / comp-blast", "rebuild": "comp-build",
    })

    # xref baseline (snapshot; no TTL).
    bpath = _CACHE_DIR / "baseline.json"
    bba = _json_built_at(bpath) if bpath.exists() else None
    records.append({
        "group": "local", "name": "baseline",
        "desc": "xref baseline snapshot (comp-xref)",
        "path": str(bpath.relative_to(_WORKSPACE)),
        "exists": bpath.exists(), "built_at": bba,
        "age": (now - bba) if bba else None,
        "ttl": None, "verdict": _present_verdict(bpath.exists()),
        "query": "comp-xref", "rebuild": "comp-xref --save",
    })

    # comp-platinum caches (NFRA_GRAPHS D2) -- discover all platinum.*.cache.
    plat = sorted(_CACHE_DIR.glob("platinum.*.cache")) if _CACHE_DIR.exists() else []
    plat_descs = {
        "platinum.routing": "comp-platinum routing table",
        "platinum.dataflows": "comp-platinum component dataflows",
    }
    for cf in plat:
        name = cf.name[:-len(".cache")]  # strip suffix
        if name.startswith("platinum.dag."):
            firm = name[len("platinum.dag."):]
            desc = f"comp-platinum gold DAG [firm={firm}]"
        else:
            desc = plat_descs.get(name, f"comp-platinum cache ({name})")
        meta = gc.cache_meta(name)
        age = meta.get("age")
        records.append({
            "group": "local", "name": name, "desc": desc,
            "path": str(cf.relative_to(_WORKSPACE)),
            "exists": True, "built_at": meta.get("built_at"), "age": age,
            "ttl": gc.DEFAULT_TTL,
            "verdict": _ttl_verdict(True, age, gc.DEFAULT_TTL),
            "predicate": _GC_PREDICATE,
            "query": "comp-platinum", "rebuild": "comp-platinum ... --force",
        })
    if not plat:
        records.append({
            "group": "local", "name": "platinum.*",
            "desc": "comp-platinum caches (per-firm, keyed by --firm)",
            "path": ".comp-graph/platinum.*.cache",
            "exists": False, "built_at": None, "age": None,
            "ttl": gc.DEFAULT_TTL, "verdict": "MISSING",
            "query": "comp-platinum", "rebuild": "comp-platinum page <C> --firm <F>",
        })

    # --- Cloud / cross-layer (infra/aws/globgrph/) --------------------------
    # Kuzu Cypher DB (comp-kuzu) -- nightly load + intraday Nessie commits.
    kuzu = _GLOBGRPH_DIR / "kuzu_db"
    k_mtime = kuzu.stat().st_mtime if kuzu.exists() else None
    records.append({
        "group": "cloud", "name": "kuzu_db",
        "desc": "comp-kuzu Cypher DB (AWS + stitch layers)",
        "path": str(kuzu.relative_to(_WORKSPACE)) if kuzu.exists() else "infra/aws/globgrph/kuzu_db",
        "exists": kuzu.exists(), "built_at": k_mtime,
        "age": (now - k_mtime) if k_mtime else None,
        "ttl": None, "verdict": _present_verdict(kuzu.exists()),
        "query": "comp-kuzu", "rebuild": "kuzu_nessie_load.py --force (nightly 02:00 + intraday)",
    })

    # P2-STITCH unified graph build artifact.
    stitch = _GLOBGRPH_DIR / "stitch_graph.json"
    s_mtime = stitch.stat().st_mtime if stitch.exists() else None
    records.append({
        "group": "cloud", "name": "stitch_graph",
        "desc": "P2-STITCH unified cross-layer graph (build artifact)",
        "path": "infra/aws/globgrph/stitch_graph.json",
        "exists": stitch.exists(), "built_at": s_mtime,
        "age": (now - s_mtime) if s_mtime else None,
        "ttl": None, "verdict": _present_verdict(stitch.exists()),
        "query": "comp-kuzu (after kuzu_stitch_load)", "rebuild": "derive_stitch.py",
    })

    return records


def cmd_status(args):
    records = _collect()

    for r in records:
        r["path"] = r["path"].replace("\\", "/")

    if getattr(args, "json", False):
        print(json.dumps({
            "generated_at": _now(),
            "contract": "org/modules/graph/graph-call-manifest.yaml",
            "graphs": records,
        }, indent=2, default=str))
        return

    print("COMP-GRAPH STATUS  (query-vs-rebuild freshness)")
    print("  contract: org/modules/graph/graph-call-manifest.yaml")
    print()

    groups = [("local", "LOCAL TRACE LAYER (.comp-graph/)"),
              ("cloud", "CLOUD / CROSS-LAYER (infra/aws/globgrph/)")]
    for gkey, gtitle in groups:
        rows = [r for r in records if r["group"] == gkey]
        if not rows:
            continue
        print(gtitle)
        for r in rows:
            verdict = r["verdict"]
            age = _fmt_age(r["age"]) if r["exists"] and r["age"] is not None else "-"
            ttl = f"TTL {r['ttl']}s" if r["ttl"] else "no-TTL"
            note = ""
            if verdict == "STALE":
                note = f"  (next call rebuilds: {r['rebuild']})"
            elif verdict == "MISSING":
                note = f"  (build: {r['rebuild']})"
            elif verdict == "UNVERIFIABLE":
                note = "  (could not evaluate -- NOT a pass)"
            print(f"  {r['name']:<20} {verdict:<12} {('built ' + age + ' ago') if r['exists'] and r['age'] is not None else ('present' if r['exists'] else 'absent'):<18} {ttl:<9} {r['desc']}{note}")
            # State the PREDICATE and the DENOMINATOR the verdict came from. A verdict whose basis
            # is invisible is a verdict a reader cannot check -- and this row's old verdict was
            # computed from a TTL its own tool never evaluates.
            if r.get("predicate"):
                print(f"  {'':<20} predicate: {r['predicate']}")
            if r.get("detail"):
                print(f"  {'':<20} evaluated: {r['detail']}")
        print()

    # The contract states the CONTRACT. It does NOT state a universal ("cached within TTL") that is
    # false for both of its members: the trace graph binds content-SHA drift and never reads age;
    # graph_cache binds a stat-only fingerprint AND a TTL. Each tool's ACTUAL predicate is printed
    # per-row above. CTO 20260709T201214Z.
    print("FRESHNESS CONTRACT (3 states):")
    print("  (default)  serve the cache iff that tool's freshness PREDICATE says fresh")
    print("  --check    REPORT staleness, never rebuild.   0 = fresh | 2 = stale | 1 = tool error")
    print("  --force    always re-derive")
    print("  --fresh    DEPRECATED no-op alias of default (warns; removed next cycle) -- the")
    print("             NFRA_GRAPHUNI P2/D2 head-pin made default honor the fingerprint and")
    print("             collapsed FRESH into DEFAULT. Proven no-op, with a control.")
    print()
    # Naming the classes IS the denominator rule applied to a status surface: a page that lists
    # "rebuild-capable graph tools" while silently omitting the pure producers asserts a universal
    # over a set it never states.
    print("POPULATION (derived from each tool's actual capability, not a token list):")
    print("  contract tools  (warm cached read + rebuild; default/--check/--force):")
    print("     %s" % ", ".join(_CONTRACT_TOOLS))
    print("  rebuild+probe verb (no warm cached read -- its DEFAULT is the rebuild; --check probes):")
    print("     %s" % ", ".join(_REBUILD_VERB))
    print("  pure producers  (always re-derive; no cached query path -- --force/--fresh collapse):")
    print("     %s" % ", ".join(_PURE_PRODUCERS))
    print("  query-only      (no rebuild path of its own; cannot own a --force):")
    print("     %s" % ", ".join(_QUERY_ONLY))


def cmd_clear(args):
    target = args.target
    cleared = []
    if target in ("platinum", "all"):
        for cf in sorted(_CACHE_DIR.glob("platinum.*.cache")):
            cf.unlink()
            cleared.append(cf.name)
    if target in ("trace", "all"):
        gpath = _CACHE_DIR / "graph.json"
        if gpath.exists():
            gpath.unlink()
            cleared.append(gpath.name)
    if target not in ("platinum", "trace", "all"):
        print(f"comp-graph clear: unknown target '{target}' (use: platinum | trace | all)",
              file=sys.stderr)
        sys.exit(2)
    if cleared:
        print(f"Cleared {len(cleared)} cache file(s): {', '.join(cleared)}")
        print("Next call to the affected tool will rebuild + re-cache.")
    else:
        print("Nothing to clear (no matching cache files present).")


def main():
    parser = argparse.ArgumentParser(
        prog="comp-graph",
        description="Freshness/status view across every dependency graph (NFRA_GRAPHS D3).",
    )
    sub = parser.add_subparsers(dest="command")

    p_status = sub.add_parser("status", help="Freshness table for every graph")
    p_status.add_argument("--json", action="store_true", help="Machine-readable output")

    p_clear = sub.add_parser("clear", help="Drop a local trace-layer cache (forces next-call rebuild)")
    p_clear.add_argument("target", choices=["platinum", "trace", "all"],
                         help="Which cache(s) to clear")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    {"status": cmd_status, "clear": cmd_clear}[args.command](args)


if __name__ == "__main__":
    main()
