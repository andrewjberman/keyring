#!/usr/bin/env python3
"""
CLI entry point for opal-trace and opal-blast.

Usage:
    python -m org.modules.graph.cli trace AdvisorsTab.tsx --direction both
    python -m org.modules.graph.cli blast D_00.portal_aggregates.py --function build_employee_leaderboard
    python -m org.modules.graph.cli build   # force rebuild the graph

Or via bash wrappers:
    opal-trace AdvisorsTab.tsx
    opal-blast D_00.portal_aggregates.py --function build_employee_leaderboard
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

# Resolve workspace root (assume we're somewhere under ajb_workspace)
_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent  # org/modules/graph -> workspace root
_CACHE_DIR = _WORKSPACE / ".comp-graph"
_CACHE_FILE = _CACHE_DIR / "graph.json"

# Add workspace to path so imports work
sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.trace_graph import (  # noqa: E402
    TraceGraph, build_graph, format_trace, format_blast,
    diff_graphs, save_baseline, format_delta,
    check_node_freshness, emit_stale_warn,
)


def _get_graph(force_rebuild: bool = False, check_freshness: bool = True) -> TraceGraph:
    """Load cached graph or build a new one.

    When check_freshness=True (default), re-loads emit STALE_NODE_WARN to stderr
    for any node whose source-file SHA has drifted since indexing
    (ADHC_COMPIL_V4.012). Doesn't block; preserves clean stdout.
    """
    if not force_rebuild and _CACHE_FILE.exists():
        try:
            g = TraceGraph.load(_CACHE_FILE)
            if check_freshness:
                # NFRA_GRAPHUNI P2/D2 (b) -- HEAD-PINNED build_graph (JOINT VERDICT 20260701,
                # CTO ruling-2-intent + CVO~B fixture-bar): serve the cache ONLY if it reflects the
                # CURRENT source (no node-SHA drift) = ONE current vintage, never a divergent-vintage
                # cache. This KILLS the stale-cache-phantom class (the 1347-vs-1337 catch) + is the D4
                # one-head guarantee for the structure tools. A drifted cache -> rebuild (below), NOT
                # serve-stale-within-a-5min-TTL. Answers stay == fresh build_graph (zero coverage
                # regression -- (a), the literal Kuzu-projection re-point, is the deferred follow-on).
                drift = check_node_freshness(g, _WORKSPACE)
                if not drift:
                    return g
                emit_stale_warn(drift)   # drifted -> fall through to a head-pinned rebuild
            elif (time.time() - g.built_at) < 300:
                # freshness opted out (e.g. internal callers) -> retain the cheap TTL fast-path
                return g
        except Exception as e:  # noqa: BLE001 -- resilience: a corrupt/truncated cache MUST self-heal to a rebuild
            # Disclose, don't swallow silently: this fires on a truncated cache (the C1 reap
            # window, now closed by the atomic save) OR a genuine load/freshness bug. We still
            # rebuild below (belt), but a SILENT swallow hid a real bug behind a slow rebuild
            # (the silent-skip class). Clean stdout preserved -- WARN goes to stderr.
            print(f"WARN: cache load/freshness-check failed ({type(e).__name__}: {e}); "
                  f"rebuilding from source.", file=sys.stderr)

    print("Building trace graph...", file=sys.stderr)
    t0 = time.time()
    g = build_graph(_WORKSPACE)
    g.save(_CACHE_FILE)
    elapsed = time.time() - t0
    print(f"Graph built: {len(g.nodes)} nodes, {len(g.edges)} edges ({elapsed:.1f}s)", file=sys.stderr)
    # AC-GRAIN sentinel (NFRA_GRAPHS D5) — WARN-level on the trace graph. The cloud
    # identity-format invariants (S3_BUCKET no-'/' etc.) don't map to trace node
    # types (FUNCTION/SCRIPT/MODULE), so this is a no-op today; present so the bar
    # fires if the trace graph ever gains a cloud-class node. Never blocks comp-build.
    try:
        import sys as _sys
        import os as _os
        _sys.path.insert(0, _os.path.dirname(__file__))
        from grain_sentinel import run_grain_sentinel
        _gr = run_grain_sentinel([{"node_type": n.node_type, "node_id": n.id}
                                  for n in g.nodes.values()])
        if not _gr.passed:
            print("WARN: " + _gr.render(), file=_sys.stderr)
    except Exception:
        pass
    return g


# ------------------------------------------------------------------ freshness contract (NFRA_GRAPHS)
# CTO GO 20260709T201214Z. THREE states, not four:
#     (default)  serve the cache iff the tool's freshness predicate says fresh
#     --check    REPORT staleness, never rebuild.   0 = fresh | 2 = stale | 1 = tool error
#     --force    always re-derive
#
# `--fresh` is a PROVEN NO-OP alias of default and is DEPRECATED. NFRA_GRAPHUNI P2/D2's head-pin
# correctly made DEFAULT honor the source fingerprint (killing the stale-cache-phantom class) and in
# doing so collapsed FRESH into DEFAULT. Nobody retired the flag. It is accepted with a WARN rather
# than silently aliased (a silent alias is a lying affordance) or silently dropped (it is
# user-visible). Remove next cycle.
#
# THE PREDICATE IS ONE EXPRESSION, NOT TWO THAT AGREE TODAY (MSTR 20260709T200348Z): every surface
# that reports trace-graph freshness calls `_freshness_probe()`, which calls the SAME
# `check_node_freshness` that `_get_graph` uses to decide serve-vs-rebuild. A status surface that
# re-models the predicate drifts from it silently -- `graph_status_cli._TRACE_TTL = 300` is exactly
# that bug: the default path never consults a TTL at all.
_FRESH_DEPRECATION = (
    "WARN: --fresh is a no-op alias of default since the head-pin (NFRA_GRAPHUNI P2/D2) -- "
    "default already rebuilds on source drift. Use default, or --force to rebuild. "
    "This flag is removed next cycle."
)


class _ContractParser(argparse.ArgumentParser):
    """argparse exits 2 on a USAGE error. The contract reserves 2 for STALE.

    Found by exercise, not by reading: `comp-trace --check` (no positional) hit argparse's
    "the following arguments are required: query" and exited 2 -- indistinguishable, to a CI job,
    from "your cache is stale". The probe had never even run. A usage error is a TOOL FAILURE, which
    the standard defines as 1 (CTO 20260709T195217Z: "1 means the tool failed, and ONLY that").
    """

    def error(self, message):  # noqa: A003
        self.print_usage(sys.stderr)
        self.exit(1, f"{self.prog}: error: {message}\n")


def add_freshness_args(p) -> None:
    """The uniform 3-state contract on a query parser."""
    p.add_argument("--check", action="store_true",
                   help="REPORT staleness, never rebuild (0=fresh 2=stale 1=error)")
    p.add_argument("--force", action="store_true", help="Always re-derive, ignoring the cache")
    p.add_argument("--fresh", action="store_true",
                   help="DEPRECATED no-op alias of default (removed next cycle)")


def _require_query(args, parser, name: str = "query") -> None:
    """--check is a PROBE over the cache: it needs no target. Every other invocation does.

    So the positional is nargs='?' and this enforces it -- rather than argparse enforcing it and
    making `--check` impossible to call.
    """
    if not getattr(args, "check", False) and not getattr(args, name, None):
        parser.error(f"the following arguments are required: {name}")


#: The trace graph's freshness PREDICATE, exactly as `_get_graph` enforces it: per-node content-SHA
#: drift. NOT a TTL -- the default serve path never evaluates age (the `elif` on the TTL hangs off
#: `if check_freshness:`, so an un-drifted cache is served at ANY age).
TRACE_PREDICATE = "content-SHA drift per indexed node (no TTL on the default path)"


def trace_freshness() -> tuple:
    """THE enforcing predicate, as a VALUE. Returns (verdict, detail, denominator, drift).

    verdict in {"FRESH", "STALE", "MISSING", "UNVERIFIABLE"}.

    Every surface that REPORTS trace-graph freshness must call this, and every surface that ACTS on
    it (`_get_graph`) evaluates the same `check_node_freshness`. MSTR 20260709T200348Z, ratified:
    "a control's reported value and its enforcing value must be the same expression, not two
    expressions that agree today." `comp-graph status` previously re-modelled this with a
    hand-copied `_TRACE_TTL = 300` and was wrong in BOTH directions -- exercised at
    (age=4000s, drift=0) it said "STALE (next call rebuilds)" while `_get_graph` SERVED the cache.
    """
    if not _CACHE_FILE.exists():
        return "MISSING", "no cached graph -- run comp-build", 0, []
    try:
        g = TraceGraph.load(_CACHE_FILE)
        drift = check_node_freshness(g, _WORKSPACE)
    except Exception as e:  # noqa: BLE001 -- cannot evaluate is never "fresh"
        return "UNVERIFIABLE", f"{type(e).__name__}: {e}", 0, []
    indexed = sum(1 for n in g.nodes.values() if n.source_sha)
    if not drift:
        return "FRESH", f"{indexed} indexed nodes; no SHA drift", indexed, []
    return "STALE", f"{len(drift)} of {indexed} indexed nodes drifted", indexed, drift


def _freshness_probe() -> int:
    """THE enforcing predicate, reported. 0 = fresh | 2 = stale | 1 = tool error.

    Names the universe it swept (CTO standing rule 20260709T192409Z: a gate that cannot state its
    denominator cannot be trusted to have a numerator).
    """
    verdict, detail, _n, drift = trace_freshness()
    if verdict == "FRESH":
        print(f"--check: clean ({detail})")
        return 0
    if verdict == "UNVERIFIABLE":
        print(f"--check: UNVERIFIABLE ({detail})", file=sys.stderr)
        return 1
    if verdict == "MISSING":
        print(f"--check: {detail}. (STALE)", file=sys.stderr)
        return 2
    emit_stale_warn(drift)      # keep comp-build --check's node-level listing (no info regression)
    print(f"--check: STALE ({detail})", file=sys.stderr)
    return 2


def _resolve_graph(args) -> TraceGraph:
    """The single entry every query handler uses. Honors the 3-state contract; exits on --check."""
    if getattr(args, "check", False):
        sys.exit(_freshness_probe())
    if getattr(args, "fresh", False):
        print(_FRESH_DEPRECATION, file=sys.stderr)
    return _get_graph(force_rebuild=getattr(args, "force", False))


def cmd_build(args):
    # --check: report staleness, never rebuild. Delegates to the shared probe so comp-build and the
    # four query tools cannot disagree about what "stale" means (ADHC_COMPIL_V4.012 AC3).
    if getattr(args, 'check', False):
        sys.exit(_freshness_probe())

    g = _get_graph(force_rebuild=True, check_freshness=False)
    print(f"Graph built: {len(g.nodes)} nodes, {len(g.edges)} edges")
    print(f"Cached at: {_CACHE_FILE}")

    # Summary by type
    by_type = {}
    for n in g.nodes.values():
        by_type[n.node_type] = by_type.get(n.node_type, 0) + 1
    print("\nNode types:")
    for t, c in sorted(by_type.items()):
        print(f"  {t}: {c}")

    edge_types = {}
    for e in g.edges:
        edge_types[e.edge_type] = edge_types.get(e.edge_type, 0) + 1
    print("\nEdge types:")
    for t, c in sorted(edge_types.items()):
        print(f"  {t}: {c}")

    # Source-SHA coverage
    indexed_count = sum(1 for n in g.nodes.values() if n.source_sha)
    file_node_count = sum(1 for n in g.nodes.values() if n.file_path)
    print(f"\nSource SHAs indexed: {indexed_count}/{file_node_count} file-backed nodes")


def cmd_trace(args):
    g = _resolve_graph(args)
    query = args.query

    # Find matching nodes
    matches = g.find_node(query)
    if not matches:
        # NOT-FOUND is LOUD (rc=3), NOT a silent rc=0. A query that resolves to
        # zero nodes is a typo / wrong-target, which on a Rule-20 change-safety
        # gate must NEVER read as a verified "nothing depends on this" clear.
        # Only a SUCCESSFUL match that then has zero results may exit 0.
        # (false-clear fix, 3.0.0_SA_CVO 2026-06-26; comp-tools duress sweep)
        if args.json:
            print(json.dumps({"query": query, "matches": [], "status": "NOT_FOUND"}))
        else:
            print(f"NOT-FOUND: no graph node matches '{query}' -- check the name "
                  f"(typo?) or run comp-build. This is a NOT-FOUND, not a "
                  f"'nothing-upstream/downstream' clear.", file=sys.stderr)
        sys.exit(3)

    if len(matches) > 1 and not args.all:
        # ADHC_COMPIL_V4.021 Cat 3.5: --json honored on multi-match disambiguation
        if args.json:
            print(json.dumps({
                "query": query,
                "match_count": len(matches),
                "matches": [{"id": m.id, "type": m.node_type, "label": m.label}
                            for m in matches],
                "hint": "use --all to trace all, or be more specific",
            }, indent=2))
            sys.exit(0)
        print(f"Multiple matches for '{query}':")
        for m in matches[:10]:
            print(f"  [{m.node_type}] {m.id} -- {m.label}")
        if len(matches) > 10:
            print(f"  ... and {len(matches) - 10} more")
        print("\nUse a more specific query or --all to trace all matches.")
        sys.exit(0)

    targets = matches if args.all else [matches[0]]

    # F.3: normalize upstream/downstream aliases to canonical up/down
    direction = {"upstream": "up", "downstream": "down"}.get(args.direction, args.direction)

    # CT1 (NFRA_TOOLPASS): collect all trace results into ONE JSON document. Previously each
    # (node, direction) printed its own json.dumps, so `--direction both` (or `--all`) emitted
    # multiple concatenated JSON objects on stdout -- a strict json.load rejects that. A single
    # {"query", "traces":[...]} object is parseable and matches the sibling --json idiom.
    json_traces: list = []
    for node in targets:
        if direction in ("up", "both"):
            results = g.upstream(node.id, max_depth=args.depth)
            if args.json:
                json_traces.append({"node": node.id, "direction": "up",
                                    "results": [{"id": n.id, "type": n.node_type, "label": n.label,
                                                 "edge": e.edge_type, "depth": d}
                                                for n, e, d in results]})
            else:
                print(format_trace(node.id, results, "up"))

        if direction in ("down", "both"):
            results = g.downstream(node.id, max_depth=args.depth)
            if args.json:
                json_traces.append({"node": node.id, "direction": "down",
                                    "results": [{"id": n.id, "type": n.node_type, "label": n.label,
                                                 "edge": e.edge_type, "depth": d}
                                                for n, e, d in results]})
            else:
                print(format_trace(node.id, results, "down"))

    if args.json:
        print(json.dumps({"query": query, "traces": json_traces}, indent=2))


def _producer_node_types() -> set[str]:
    return {'LAMBDA', 'GOLD_SCRIPT', 'GOLD_FUNCTION', 'SILVER_SCRIPT', 'S3_ARTIFACT'}


def _is_producer_pipeline_match(node_id: str, pipeline: str | None) -> bool:
    if not pipeline or pipeline == 'all':
        return True
    nid = node_id.lower()
    if pipeline == 'inf':
        return 'inf' in nid or 'inflect' in nid or 'orion' in nid or 'INF' in node_id
    if pipeline == 'bd':
        return 'bd' in nid or 'black_diamond' in nid or 'BD' in node_id
    return True


def cmd_blast(args):
    g = _resolve_graph(args)

    # --all-producers sweep mode: list all producer nodes with zero downstream consumers
    if getattr(args, 'all_producers', False):
        pipeline = getattr(args, 'pipeline', None)
        producer_types = _producer_node_types()
        phantoms = []
        checked = 0
        for node_id, node in sorted(g.nodes.items()):
            if node.node_type not in producer_types:
                continue
            if not _is_producer_pipeline_match(node_id, pipeline):
                continue
            checked += 1
            downstream = g.downstream(node_id, max_depth=1)
            if not downstream:
                phantoms.append(node)
        print(f'PHANTOM-CONSUMER SWEEP: {len(phantoms)} producers with zero EXTRACTED-edge consumers of {checked} checked')
        print('  (LOWER BOUND -- "zero" = no extracted edge, NOT provably orphan; dynamic/FUNC-key')
        print('   consumers are invisible. Treat as CANDIDATES to verify, not confirmed orphans.)')
        if phantoms:
            print(f'  {"NODE-ID":<60}  TYPE')
            print(f'  {"-"*60}  {"-"*20}')
            for n in phantoms:
                print(f'  {n.id:<60}  {n.node_type}')
        if getattr(args, 'check_consumers', False):
            sys.exit(1 if phantoms else 0)
        return

    query = args.query

    # If --function specified, look for gold:script:function
    if args.function:
        query = f"{Path(query).stem}:{args.function}"

    matches = g.find_node(query)
    if not matches:
        # NOT-FOUND is LOUD (rc=3). On comp-blast (a Rule-20 "what breaks if I
        # change X" gate) a typo'd target must NEVER exit 0 as if it were a
        # verified "nothing breaks" clear. (false-clear fix, 2026-06-26)
        print(f"NOT-FOUND: no graph node matches '{query}' -- check the name "
              f"(typo?) or run comp-build. This is a NOT-FOUND, not a "
              f"'nothing breaks' clear.", file=sys.stderr)
        sys.exit(3)

    node = matches[0]

    # F.4: --direction flag wires through uniformly for all resolver paths
    # (bare name, prefix-qualified lambda:/gold:/component:, full file path).
    # Default (None) preserves existing blast-radius semantic: downstream-only
    # unless the node is function-grain (ADHC_ROUTER.T1).
    direction = getattr(args, 'direction', None)

    is_function_grain = (
        node.node_type == "GOLD_SCRIPT"
        and getattr(node, "function_name", None)
        and node.id.count(":") >= 2
    )

    # Downstream: always, except when direction is explicitly 'up'
    downstream = g.downstream(node.id, max_depth=args.depth) if direction != 'up' else []

    # Upstream: when direction is 'up'/'both', or for function-grain with no explicit direction
    # (preserves ADHC_ROUTER.T1 semantic — "what breaks if I change this function?")
    if direction in ('up', 'both'):
        upstream = g.upstream(node.id, max_depth=args.depth)
    elif direction is None and is_function_grain:
        upstream = g.upstream(node.id, max_depth=args.depth)
    else:
        upstream = []

    # --check-consumers: exit 0 if >=1 downstream consumer, exit 1 if zero
    if getattr(args, 'check_consumers', False):
        if downstream:
            print(f'CONSUMER-OK: {node.id} has {len(downstream)} downstream consumer(s)')
            sys.exit(0)
        else:
            print(f'PHANTOM-CONSUMER: {node.id} -- zero downstream consumers IN GRAPH')
            print(f'  Node type: {node.node_type}')
            print('  "Zero" = no EXTRACTED edge, NOT provably no consumer. A real consumer')
            print('  reading this via a dynamic/FUNC-key (the comp-pipescript miss class) is')
            print('  INVISIBLE here. Verify (grep the artifact key / comp-pipescript consumers)')
            print('  before treating as orphan -- do not assume safe-to-delete.')
            sys.exit(1)

    if args.json:
        by_type = {}
        for n, e, d in downstream:
            by_type.setdefault(n.node_type, []).append({
                "id": n.id, "label": n.label, "depth": d,
                "direction": "downstream",
            })
        for n, e, d in upstream:
            by_type.setdefault(n.node_type, []).append({
                "id": n.id, "label": n.label, "depth": d,
                "direction": "upstream",
            })
        print(json.dumps({"source": node.id, "consumers": by_type}, indent=2))
    else:
        print(format_blast(node.id, downstream))
        if upstream:
            print()
            print(f"CALLER CHAIN (upstream from {node.id}):")
            seen = set()
            for n, _, d in upstream:
                if n.id in seen:
                    continue
                seen.add(n.id)
                print(f"  [{d}] {n.label}")


def cmd_diff(args):
    """Map git changes to graph impact. Shows which trace graph nodes are
    affected by files changed in git (staged, unstaged, or between refs)."""
    import subprocess

    g = _resolve_graph(args)

    # Get changed files from git
    if args.ref:
        # Compare against a git ref: git diff --name-only <ref>
        result = subprocess.run(
            ["git", "diff", "--name-only", args.ref],
            capture_output=True, text=True, cwd=str(_WORKSPACE),
        )
    elif args.staged:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            capture_output=True, text=True, cwd=str(_WORKSPACE),
        )
    else:
        # Default: all uncommitted changes (staged + unstaged)
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            capture_output=True, text=True, cwd=str(_WORKSPACE),
        )

    if result.returncode != 0:
        # CD1 (NFRA_TOOLPASS): --json must emit ONLY JSON on stdout. The human-text lines
        # ("git diff failed", "No changed files", "Changed files: N", "no graph nodes")
        # were printed regardless of --json, so a strict parser failed at char 0.
        if args.json:
            print(json.dumps({"error": f"git diff failed: {result.stderr.strip()}"}))
        else:
            print(f"git diff failed: {result.stderr.strip()}")
        sys.exit(1)

    changed_files = [f.strip() for f in result.stdout.strip().splitlines() if f.strip()]
    if not changed_files:
        if args.json:
            print(json.dumps({"changed_files": 0, "affected": []}, indent=2))
        else:
            print("No changed files detected.")
        return

    if not args.json:
        print(f"Changed files: {len(changed_files)}\n")

    # Map each changed file to graph nodes
    all_affected = []
    for filepath in changed_files:
        # Normalize path
        fp_normalized = filepath.replace("\\", "/")

        # Find graph nodes whose file_path matches this changed file
        matched_nodes = []
        for node in g.nodes.values():
            if node.file_path and fp_normalized in node.file_path:
                matched_nodes.append(node)

        # Also check by filename stem (e.g., "D_00.portal_aggregates" matches gold:D_00.portal_aggregates)
        stem = Path(filepath).stem
        if not matched_nodes:
            for node in g.nodes.values():
                if stem and stem in node.id:
                    matched_nodes.append(node)

        if not matched_nodes:
            if not args.json:                       # CD1: don't pollute --json stdout
                print(f"  {fp_normalized} -- no graph nodes (not tracked)")
            continue

        for node in matched_nodes:
            downstream = g.downstream(node.id, max_depth=args.depth)
            upstream = g.upstream(node.id, max_depth=args.depth)

            if args.json:
                all_affected.append({
                    "file": fp_normalized,
                    "node": node.id,
                    "type": node.node_type,
                    "downstream_count": len(downstream),
                    "upstream_count": len(upstream),
                    "downstream": [{"id": n.id, "type": n.node_type, "label": n.label}
                                   for n, e, d in downstream],
                })
            else:
                down_types = {}
                for n, e, d in downstream:
                    down_types.setdefault(n.node_type, []).append(n.label)

                print(f"  {fp_normalized}")
                print(f"    Node: [{node.node_type}] {node.id}")
                if downstream:
                    parts = [f"{len(v)} {k}" for k, v in sorted(down_types.items())]
                    print(f"    Blast radius: {', '.join(parts)}")
                    # Show component-level impacts specifically (most actionable)
                    components = [n for n, e, d in downstream if n.node_type == "COMPONENT"]
                    if components:
                        print(f"    Affected pages: {', '.join(c.label for c in components)}")
                else:
                    print("    Blast radius: none (leaf node)")
                print()

    if args.json:
        print(json.dumps({"changed_files": len(changed_files), "affected": all_affected}, indent=2))


_BASELINE_FILE = _CACHE_DIR / "baseline.json"


def _xref_symbol_lookup(g: TraceGraph, symbol: str) -> None:
    """Symbol cross-reference lookup (ADHC_COMPIL_V4.014).

    Searches graph nodes by id/label/file_path substring (case-insensitive) and
    edges by source/target. Output format mirrors comp-blast structure so agents
    already know how to read it.

    Anchor: 2026-04-21 17/25 FAILs from agents passing positional args to
    `comp-xref` thinking it was a symbol-lookup tool. This mode closes the gap.
    """
    q = symbol.strip().lower()
    if not q:
        print("comp-xref: empty symbol; provide a non-empty argument.", file=sys.stderr)
        sys.exit(1)

    # Match nodes: substring on id, label, file_path
    matched_nodes = []
    for node in g.nodes.values():
        if (q in node.id.lower() or
            q in node.label.lower() or
            (node.file_path and q in node.file_path.lower())):
            matched_nodes.append(node)

    # Match edges: substring on source/target
    matched_edges = []
    for edge in g.edges:
        if q in edge.source.lower() or q in edge.target.lower():
            matched_edges.append(edge)

    print(f"XREF LOOKUP: '{symbol}'")
    print(f"  ({len(matched_nodes)} node(s), {len(matched_edges)} edge(s) matched)")
    print()

    if not matched_nodes and not matched_edges:
        # NOT-FOUND is LOUD (rc=3), not a silent rc=0 return. A zero-match xref
        # is a typo / unindexed symbol; it must be distinguishable from a
        # successful lookup so it can't read as "verified clear". (fix 2026-06-26)
        print("  No matches in graph.", file=sys.stderr)
        print("  Hints:", file=sys.stderr)
        print("    - Symbol may be a Python module/function not yet indexed", file=sys.stderr)
        print("    - Run 'comp-build' to refresh graph; check stale-cache warnings", file=sys.stderr)
        print("    - For COMP_LEARNS-corpus symbols, comp-xref does not index that tree (out-of-scope)", file=sys.stderr)
        sys.exit(3)

    if matched_nodes:
        # Group by node_type for readability
        by_type: dict[str, list] = {}
        for n in matched_nodes:
            by_type.setdefault(n.node_type, []).append(n)
        print(f"  NODES ({len(matched_nodes)}):")
        for ntype in sorted(by_type.keys()):
            print(f"    [{ntype}]")
            for n in sorted(by_type[ntype], key=lambda x: x.id)[:15]:
                fp = f" — {n.file_path}" if n.file_path else ""
                fn = f" :: {n.function_name}" if n.function_name else ""
                print(f"      {n.id}{fn}{fp}")
            if len(by_type[ntype]) > 15:
                print(f"      ... and {len(by_type[ntype]) - 15} more")
        print()

    if matched_edges:
        # Group by edge_type
        by_etype: dict[str, list] = {}
        for e in matched_edges:
            by_etype.setdefault(e.edge_type, []).append(e)
        print(f"  EDGES ({len(matched_edges)}):")
        for etype in sorted(by_etype.keys()):
            print(f"    [{etype}]")
            for e in by_etype[etype][:10]:
                print(f"      {e.source} -> {e.target}")
            if len(by_etype[etype]) > 10:
                print(f"      ... and {len(by_etype[etype]) - 10} more")
        print()


def cmd_xref(args):
    """Compare current graph against baseline snapshot, OR cross-reference a symbol.

    Dual-purpose (ADHC_COMPIL_V4.014):
      no positional arg -> graph-state-diff vs baseline (existing behavior)
      positional arg    -> symbol cross-reference lookup (NEW)

    Symbol-lookup matches against node ids, labels, file paths, and edge
    sources/targets. Returns all references for agent disambiguation.
    """
    # --check is mode-independent: it probes the cache, never rebuilds, in EITHER mode.
    if getattr(args, "check", False):
        sys.exit(_freshness_probe())
    if getattr(args, "fresh", False):
        print(_FRESH_DEPRECATION, file=sys.stderr)

    # ADHC_COMPIL_V4.014 — symbol cross-reference mode
    symbol = getattr(args, 'symbol', None)
    if symbol:
        g = _get_graph(force_rebuild=getattr(args, "force", False))
        _xref_symbol_lookup(g, symbol)
        return

    # baseline-diff mode re-derives BY DESIGN: it compares the CURRENT graph against the saved
    # snapshot, so serving a cache would compare the baseline against itself. --force is implied.
    g = _get_graph(force_rebuild=True)

    if args.save:
        path = save_baseline(g, _CACHE_DIR)
        if args.json:                                       # CX1: --json clean on the --save path too
            print(json.dumps({"baseline_saved": {"nodes": len(g.nodes),
                                                  "edges": len(g.edges), "path": str(path)}}, indent=2))
        else:
            print(f"Baseline saved: {len(g.nodes)} nodes, {len(g.edges)} edges")
            print(f"Path: {path}")
        return

    # Load baseline
    # CX1 (NFRA_TOOLPASS, the comp-diff CD1 analog): --json must emit ONLY JSON on stdout. These
    # edge paths printed human text regardless of --json -> a strict parse failed at char 0.
    if not _BASELINE_FILE.exists():
        if args.json:
            print(json.dumps({"error": "no baseline", "hint": "run comp-xref --save to create one"}))
        else:
            print("No baseline found. Run 'comp-xref --save' to create one first.")
        sys.exit(1)

    try:
        baseline = TraceGraph.load(_BASELINE_FILE)
    except Exception as e:
        if args.json:
            print(json.dumps({"error": f"failed to load baseline: {e}"}))
        else:
            print(f"Failed to load baseline: {e}")
        sys.exit(1)

    delta = diff_graphs(baseline, g)

    if args.json:
        output = {
            "baseline": {
                "nodes": len(baseline.nodes),
                "edges": len(baseline.edges),
                "built_at": baseline.built_at,
            },
            "current": {
                "nodes": len(g.nodes),
                "edges": len(g.edges),
                "built_at": g.built_at,
            },
            "summary": delta.summary(),
            "added_nodes": [{"id": n.id, "type": n.node_type, "label": n.label}
                            for n in delta.added_nodes],
            "removed_nodes": [{"id": n.id, "type": n.node_type, "label": n.label}
                              for n in delta.removed_nodes],
            "added_edges": [{"source": e.source, "target": e.target, "type": e.edge_type}
                            for e in delta.added_edges],
            "removed_edges": [{"source": e.source, "target": e.target, "type": e.edge_type}
                              for e in delta.removed_edges],
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"Baseline: {len(baseline.nodes)} nodes, {len(baseline.edges)} edges")
        print(f"Current:  {len(g.nodes)} nodes, {len(g.edges)} edges")
        print()
        print(format_delta(delta))


def main():
    # _ContractParser: a usage error exits 1 (tool failure), never 2 (which the freshness contract
    # reserves for STALE). parser_class propagates it to every subparser.
    parser = _ContractParser(description="Opal full-stack trace compiler")
    sub = parser.add_subparsers(dest="command", parser_class=_ContractParser)

    # build
    p_build = sub.add_parser("build", help="Force rebuild the trace graph")
    p_build.add_argument("--check", action="store_true",
                         help="Verify cached graph SHA freshness without rebuilding (exit 2 on drift)")

    # trace
    p_trace = sub.add_parser("trace", help="Trace data path from a node")
    p_trace.add_argument("query", nargs="?", help="File, component, or node to trace")
    p_trace.add_argument("--direction",
                         choices=["up", "upstream", "down", "downstream", "both"],
                         default="both",
                         help="Traversal direction: up/upstream, down/downstream, or both (default).")
    p_trace.add_argument("--depth", type=int, default=10)
    p_trace.add_argument("--json", action="store_true")
    p_trace.add_argument("--all", action="store_true", help="Trace all matches")
    add_freshness_args(p_trace)

    # blast
    p_blast = sub.add_parser("blast", help="Show blast radius of a change")
    p_blast.add_argument("query", nargs="?",
                         help="File, node, or prefix-qualified node "
                              "(e.g. lambda:fn-name, gold:D_04, component:AdvisorsTab.tsx)")
    p_blast.add_argument("--function", help="Specific function within the file")
    p_blast.add_argument("--depth", type=int, default=10)
    p_blast.add_argument("--json", action="store_true")
    p_blast.add_argument("--direction", choices=["up", "down", "both"], default=None,
                         help="Traversal direction: up (upstream callers), down (downstream consumers, "
                              "default), both. Works with prefix-qualified queries "
                              "(lambda:, gold:, silver:, component:).")
    p_blast.add_argument("--check-consumers", action="store_true",
                         help="Exit 0 if node has >=1 downstream consumer; exit 1 if zero (phantom-consumer check). "
                              "Combine with --all-producers for sweep mode.")
    p_blast.add_argument("--all-producers", action="store_true",
                         help="Sweep all producer nodes in graph; list those with zero downstream consumers. "
                              "Use with --check-consumers and --pipeline.")
    add_freshness_args(p_blast)
    p_blast.add_argument("--pipeline", choices=["inf", "bd", "all"], default=None,
                         help="Filter --all-producers sweep by pipeline (inf/bd/all).")

    # diff
    p_diff = sub.add_parser("diff", help="Map git changes to graph impact")
    p_diff.add_argument("--ref", help="Git ref to diff against (e.g., HEAD~3, main)")
    p_diff.add_argument("--staged", action="store_true", help="Only staged changes")
    p_diff.add_argument("--depth", type=int, default=5)
    p_diff.add_argument("--json", action="store_true")
    add_freshness_args(p_diff)

    # xref — dual-purpose: graph-diff (no-arg) + symbol-lookup (positional)
    p_xref = sub.add_parser(
        "xref",
        help="Compare graph against baseline (no-arg) OR cross-reference a symbol (positional)",
    )
    p_xref.add_argument(
        "symbol", nargs="?", default=None,
        help="Symbol to cross-reference (function name, file path, S3 key, Lambda name, etc.). "
             "When provided, runs symbol-lookup mode; otherwise runs graph-diff. (ADHC_COMPIL_V4.014)",
    )
    p_xref.add_argument("--save", action="store_true", help="Save current graph as baseline (no-arg mode)")
    p_xref.add_argument("--json", action="store_true")
    add_freshness_args(p_xref)

    args = parser.parse_args()
    if args.command == "build":
        cmd_build(args)
    elif args.command == "trace":
        _require_query(args, parser)
        cmd_trace(args)
    elif args.command == "blast":
        _require_query(args, parser)
        cmd_blast(args)
    elif args.command == "diff":
        cmd_diff(args)
    elif args.command == "xref":
        cmd_xref(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
