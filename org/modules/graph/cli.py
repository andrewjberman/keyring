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
            age = time.time() - g.built_at
            if age < 300:  # 5 min cache
                if check_freshness:
                    drift = check_node_freshness(g, _WORKSPACE)
                    emit_stale_warn(drift)
                return g
        except Exception:
            pass

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


def cmd_build(args):
    # --check mode: verify cached graph against current FS without rebuilding
    # (ADHC_COMPIL_V4.012 AC3). Exits 2 if any node has SHA drift; 0 if clean.
    if getattr(args, 'check', False):
        if not _CACHE_FILE.exists():
            print("comp-build --check: no cached graph found", file=sys.stderr)
            print("  Run `comp-build` first.", file=sys.stderr)
            sys.exit(2)
        g = TraceGraph.load(_CACHE_FILE)
        drift = check_node_freshness(g, _WORKSPACE)
        if not drift:
            indexed = sum(1 for n in g.nodes.values() if n.source_sha)
            print(f"comp-build --check: clean ({indexed} indexed nodes; no SHA drift)")
            sys.exit(0)
        emit_stale_warn(drift)
        sys.exit(2)

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
    g = _get_graph()
    query = args.query

    # Find matching nodes
    matches = g.find_node(query)
    if not matches:
        if args.json:
            print(json.dumps({"query": query, "matches": []}))
        else:
            print(f"No nodes matching: {query}")
        sys.exit(0)

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

    for node in targets:
        if direction in ("up", "both"):
            results = g.upstream(node.id, max_depth=args.depth)
            output = format_trace(node.id, results, "up")
            if args.json:
                print(json.dumps({"node": node.id, "direction": "up",
                                  "results": [{"id": n.id, "type": n.node_type, "label": n.label,
                                               "edge": e.edge_type, "depth": d}
                                              for n, e, d in results]}, indent=2))
            else:
                print(output)

        if direction in ("down", "both"):
            results = g.downstream(node.id, max_depth=args.depth)
            output = format_trace(node.id, results, "down")
            if args.json:
                print(json.dumps({"node": node.id, "direction": "down",
                                  "results": [{"id": n.id, "type": n.node_type, "label": n.label,
                                               "edge": e.edge_type, "depth": d}
                                              for n, e, d in results]}, indent=2))
            else:
                print(output)


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
    g = _get_graph()

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
        print(f"No nodes matching: {query}")
        sys.exit(0)

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

    g = _get_graph()

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
        print(f"git diff failed: {result.stderr.strip()}")
        sys.exit(1)

    changed_files = [f.strip() for f in result.stdout.strip().splitlines() if f.strip()]
    if not changed_files:
        print("No changed files detected.")
        return

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
        print("  No matches in graph.")
        print()
        print("  Hints:")
        print("    - Symbol may be a Python module/function not yet indexed")
        print("    - Run 'comp-build' to refresh graph; check stale-cache warnings")
        print("    - For COMP_LEARNS-corpus symbols, comp-xref does not index that tree (out-of-scope)")
        return

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
    # ADHC_COMPIL_V4.014 — symbol cross-reference mode
    symbol = getattr(args, 'symbol', None)
    if symbol:
        g = _get_graph()
        _xref_symbol_lookup(g, symbol)
        return

    g = _get_graph(force_rebuild=True)

    if args.save:
        path = save_baseline(g, _CACHE_DIR)
        print(f"Baseline saved: {len(g.nodes)} nodes, {len(g.edges)} edges")
        print(f"Path: {path}")
        return

    # Load baseline
    if not _BASELINE_FILE.exists():
        print("No baseline found. Run 'comp-xref --save' to create one first.")
        sys.exit(1)

    try:
        baseline = TraceGraph.load(_BASELINE_FILE)
    except Exception as e:
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
    parser = argparse.ArgumentParser(description="Opal full-stack trace compiler")
    sub = parser.add_subparsers(dest="command")

    # build
    p_build = sub.add_parser("build", help="Force rebuild the trace graph")
    p_build.add_argument("--check", action="store_true",
                         help="Verify cached graph SHA freshness without rebuilding (exit 2 on drift)")

    # trace
    p_trace = sub.add_parser("trace", help="Trace data path from a node")
    p_trace.add_argument("query", help="File, component, or node to trace")
    p_trace.add_argument("--direction",
                         choices=["up", "upstream", "down", "downstream", "both"],
                         default="both",
                         help="Traversal direction: up/upstream, down/downstream, or both (default).")
    p_trace.add_argument("--depth", type=int, default=10)
    p_trace.add_argument("--json", action="store_true")
    p_trace.add_argument("--all", action="store_true", help="Trace all matches")

    # blast
    p_blast = sub.add_parser("blast", help="Show blast radius of a change")
    p_blast.add_argument("query",
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
    p_blast.add_argument("--pipeline", choices=["inf", "bd", "all"], default=None,
                         help="Filter --all-producers sweep by pipeline (inf/bd/all).")

    # diff
    p_diff = sub.add_parser("diff", help="Map git changes to graph impact")
    p_diff.add_argument("--ref", help="Git ref to diff against (e.g., HEAD~3, main)")
    p_diff.add_argument("--staged", action="store_true", help="Only staged changes")
    p_diff.add_argument("--depth", type=int, default=5)
    p_diff.add_argument("--json", action="store_true")

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

    args = parser.parse_args()
    if args.command == "build":
        cmd_build(args)
    elif args.command == "trace":
        cmd_trace(args)
    elif args.command == "blast":
        cmd_blast(args)
    elif args.command == "diff":
        cmd_diff(args)
    elif args.command == "xref":
        cmd_xref(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
