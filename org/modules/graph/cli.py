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

from org.modules.graph.trace_graph import (
    TraceGraph, build_graph, format_trace, format_blast,
    diff_graphs, save_baseline, format_delta,
)


def _get_graph(force_rebuild: bool = False) -> TraceGraph:
    """Load cached graph or build a new one."""
    if not force_rebuild and _CACHE_FILE.exists():
        try:
            g = TraceGraph.load(_CACHE_FILE)
            age = time.time() - g.built_at
            if age < 300:  # 5 min cache
                return g
        except Exception:
            pass

    print("Building trace graph...", file=sys.stderr)
    t0 = time.time()
    g = build_graph(_WORKSPACE)
    g.save(_CACHE_FILE)
    elapsed = time.time() - t0
    print(f"Graph built: {len(g.nodes)} nodes, {len(g.edges)} edges ({elapsed:.1f}s)", file=sys.stderr)
    return g


def cmd_build(args):
    g = _get_graph(force_rebuild=True)
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


def cmd_trace(args):
    g = _get_graph()
    query = args.query

    # Find matching nodes
    matches = g.find_node(query)
    if not matches:
        print(f"No nodes matching: {query}")
        sys.exit(0)

    if len(matches) > 1 and not args.all:
        print(f"Multiple matches for '{query}':")
        for m in matches[:10]:
            print(f"  [{m.node_type}] {m.id} -- {m.label}")
        if len(matches) > 10:
            print(f"  ... and {len(matches) - 10} more")
        print("\nUse a more specific query or --all to trace all matches.")
        sys.exit(0)

    targets = matches if args.all else [matches[0]]

    for node in targets:
        if args.direction in ("up", "both"):
            results = g.upstream(node.id, max_depth=args.depth)
            output = format_trace(node.id, results, "up")
            if args.json:
                print(json.dumps({"node": node.id, "direction": "up",
                                  "results": [{"id": n.id, "type": n.node_type, "label": n.label,
                                               "edge": e.edge_type, "depth": d}
                                              for n, e, d in results]}, indent=2))
            else:
                print(output)

        if args.direction in ("down", "both"):
            results = g.downstream(node.id, max_depth=args.depth)
            output = format_trace(node.id, results, "down")
            if args.json:
                print(json.dumps({"node": node.id, "direction": "down",
                                  "results": [{"id": n.id, "type": n.node_type, "label": n.label,
                                               "edge": e.edge_type, "depth": d}
                                              for n, e, d in results]}, indent=2))
            else:
                print(output)


def cmd_blast(args):
    g = _get_graph()
    query = args.query

    # If --function specified, look for gold:script:function
    if args.function:
        query = f"{Path(query).stem}:{args.function}"

    matches = g.find_node(query)
    if not matches:
        print(f"No nodes matching: {query}")
        sys.exit(0)

    node = matches[0]
    downstream = g.downstream(node.id, max_depth=args.depth)

    # ADHC_ROUTER.T1 fix: for function-grain nodes (gold:<script>:<function>),
    # the "change-impact radius" semantic includes callers — changing a leaf
    # helper breaks its callers, not the other way around. Surface both
    # sections so blast on any function (entry point or helper) answers
    # "what breaks if I change this" correctly.
    is_function_grain = (
        node.node_type == "GOLD_SCRIPT"
        and getattr(node, "function_name", None)
        and node.id.count(":") >= 2
    )
    upstream = g.upstream(node.id, max_depth=args.depth) if is_function_grain else []

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
        if is_function_grain and upstream:
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
                    print(f"    Blast radius: none (leaf node)")
                print()

    if args.json:
        print(json.dumps({"changed_files": len(changed_files), "affected": all_affected}, indent=2))


_BASELINE_FILE = _CACHE_DIR / "baseline.json"


def cmd_xref(args):
    """Compare current graph against baseline snapshot."""
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
        from dataclasses import asdict
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
    sub.add_parser("build", help="Force rebuild the trace graph")

    # trace
    p_trace = sub.add_parser("trace", help="Trace data path from a node")
    p_trace.add_argument("query", help="File, component, or node to trace")
    p_trace.add_argument("--direction", choices=["up", "down", "both"], default="both")
    p_trace.add_argument("--depth", type=int, default=10)
    p_trace.add_argument("--json", action="store_true")
    p_trace.add_argument("--all", action="store_true", help="Trace all matches")

    # blast
    p_blast = sub.add_parser("blast", help="Show blast radius of a change")
    p_blast.add_argument("query", help="File or node to check")
    p_blast.add_argument("--function", help="Specific function within the file")
    p_blast.add_argument("--depth", type=int, default=10)
    p_blast.add_argument("--json", action="store_true")

    # diff
    p_diff = sub.add_parser("diff", help="Map git changes to graph impact")
    p_diff.add_argument("--ref", help="Git ref to diff against (e.g., HEAD~3, main)")
    p_diff.add_argument("--staged", action="store_true", help="Only staged changes")
    p_diff.add_argument("--depth", type=int, default=5)
    p_diff.add_argument("--json", action="store_true")

    # xref (placeholder -- COO implementing)
    p_xref = sub.add_parser("xref", help="Compare graph against baseline snapshot")
    p_xref.add_argument("--save", action="store_true", help="Save current graph as baseline")
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
