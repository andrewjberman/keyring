#!/usr/bin/env python3
"""
comp-pipescript -- authoritative pipeline dependency tool.

Usage:
    comp-pipescript dag                        # full execution DAG with I/O edges
    comp-pipescript io D_00                    # inputs + outputs for one script
    comp-pipescript chain downstream           # show chain membership + order
    comp-pipescript chain full                 # show full chain
    comp-pipescript feeds D_00                 # what scripts feed D_00 (upstream)
    comp-pipescript consumers D_00             # what scripts consume D_00 output
    comp-pipescript overlap D_00 D_03          # shared S3 artifacts between two scripts
    comp-pipescript inject                     # inject pipeline edges into comp-trace graph
    comp-pipescript stats                      # graph statistics

Data sources (authoritative, not heuristic):
    lib/s3_layout.py      -- every S3 key as a named constant
    gold_dispatch.sh      -- execution order, chains, groups, catalog
    each script's AST     -- from lib.s3_layout import (...) block
"""

import argparse
import json
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.extract_pipeline import build_pipeline_dag, inject_pipeline_edges


def _build_dag():
    return build_pipeline_dag(_WORKSPACE)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_dag(args):
    dag = _build_dag()

    if args.json:
        result = {}
        for sid, sio in sorted(dag.scripts.items(), key=lambda x: x[1].run_order):
            result[sid] = {
                "filename": sio.filename,
                "group": sio.group,
                "run_order": sio.run_order,
                "reads": sio.read_keys,
                "writes": sio.write_keys,
                "feeds_from": [(u, k) for u, k, _ in dag.feeds(sid)],
                "feeds_to": [(d, k) for d, k, _ in dag.consumers(sid)],
            }
        print(json.dumps(result, indent=2))
        return

    print("PIPELINE DAG")
    print(f"  Scripts: {len(dag.scripts)}")
    print(f"  S3 keys: {len(dag.s3_keys)}")
    print()

    for sid, sio in sorted(dag.scripts.items(), key=lambda x: x[1].run_order):
        upstream = dag.feeds(sid)
        downstream = dag.consumers(sid)
        print(f"  {sid} ({sio.filename})")
        print(f"    Group: {sio.group} | Order: {sio.run_order}")
        print(f"    Reads:  {len(sio.read_keys)} keys | Writes: {len(sio.write_keys)} keys")
        if upstream:
            scripts = sorted(set(u for u, _, _ in upstream))
            print(f"    Fed by: {', '.join(scripts)}")
        if downstream:
            scripts = sorted(set(d for d, _, _ in downstream))
            print(f"    Feeds:  {', '.join(scripts)}")
        print()


def cmd_io(args):
    dag = _build_dag()
    script_id = args.script_id.upper()

    # Allow partial match: "D_00" or "d_00" or "D_00.portal_aggregates"
    sio = dag.scripts.get(script_id)
    if not sio:
        # Try substring match
        matches = [s for s in dag.scripts if script_id.upper() in s.upper()]
        if len(matches) == 1:
            sio = dag.scripts[matches[0]]
            script_id = matches[0]
        elif matches:
            print(f"Multiple matches: {', '.join(matches)}")
            sys.exit(1)
        else:
            print(f"Unknown script: {script_id}")
            print(f"Valid IDs: {', '.join(sorted(dag.scripts.keys()))}")
            sys.exit(1)

    if args.json:
        print(json.dumps({
            "script_id": script_id,
            "filename": sio.filename,
            "group": sio.group,
            "run_order": sio.run_order,
            "reads": [{"constant": c, "s3_key": dag.s3_keys[c].s3_path}
                      for c in sio.reads if c in dag.s3_keys],
            "writes": [{"constant": c, "s3_key": dag.s3_keys[c].s3_path}
                       for c in sio.writes if c in dag.s3_keys],
        }, indent=2))
        return

    print(f"I/O MANIFEST: {script_id} ({sio.filename})")
    print(f"  Group: {sio.group} | Order: {sio.run_order}")
    print()

    if sio.reads:
        print(f"  READS ({len(sio.reads)}):")
        for const in sio.reads:
            sk = dag.s3_keys.get(const)
            key = sk.s3_path if sk else '?'
            prefix_tag = " [PREFIX]" if sk and sk.is_prefix else ""
            func_tag = " [FUNC]" if sk and sk.is_function else ""
            # Show who writes this key
            writers = dag._writers.get(key, [])
            writers = [w for w in writers if w != script_id]
            writer_str = f" <- {', '.join(writers)}" if writers else " <- (external/silver)"
            print(f"    {const}: {key}{prefix_tag}{func_tag}{writer_str}")
    else:
        print("  READS: (none detected)")

    print()

    if sio.writes:
        print(f"  WRITES ({len(sio.writes)}):")
        for const in sio.writes:
            sk = dag.s3_keys.get(const)
            key = sk.s3_path if sk else '?'
            func_tag = " [FUNC]" if sk and sk.is_function else ""
            # Show who reads this key
            readers = dag._readers.get(key, [])
            readers = [r for r in readers if r != script_id]
            reader_str = f" -> {', '.join(readers)}" if readers else " -> (terminal)"
            print(f"    {const}: {key}{func_tag}{reader_str}")
    else:
        print("  WRITES: (none detected)")


def cmd_chain(args):
    dag = _build_dag()
    chain_name = args.chain_name.lower()

    if chain_name not in dag.chains:
        print(f"Unknown chain: {chain_name}")
        print(f"Valid chains: {', '.join(sorted(dag.chains.keys()))}")
        sys.exit(1)

    script_ids = dag.chains[chain_name]
    print(f"CHAIN: {chain_name} ({len(script_ids)} scripts)")
    print()

    for i, sid in enumerate(script_ids, 1):
        sio = dag.scripts.get(sid)
        if sio:
            print(f"  {i:2d}. {sid:6s} {sio.filename}")
            print(f"         reads: {len(sio.read_keys)} | writes: {len(sio.write_keys)}")
        else:
            print(f"  {i:2d}. {sid:6s} (not found in scripts)")


def cmd_feeds(args):
    dag = _build_dag()
    script_id = args.script_id.upper()
    sio = dag.scripts.get(script_id)
    if not sio:
        print(f"Unknown script: {script_id}")
        sys.exit(1)

    upstream = dag.feeds(script_id)
    if not upstream:
        print(f"{script_id}: no upstream pipeline dependencies (reads from silver or external)")
        return

    if args.json:
        print(json.dumps([
            {"script": u, "s3_key": k, "constant": c}
            for u, k, c in upstream
        ], indent=2))
        return

    print(f"UPSTREAM FEEDS into {script_id}:")
    print()
    # Group by upstream script
    by_script: dict[str, list[tuple[str, str]]] = {}
    for u_script, s3_key, const in upstream:
        by_script.setdefault(u_script, []).append((s3_key, const))

    for u_script, keys in sorted(by_script.items()):
        print(f"  {u_script}:")
        for s3_key, const in keys:
            print(f"    {const}: {s3_key}")
    print()
    print(f"  Total: {len(upstream)} artifacts from {len(by_script)} scripts")


def cmd_consumers(args):
    dag = _build_dag()
    script_id = args.script_id.upper()
    sio = dag.scripts.get(script_id)
    if not sio:
        print(f"Unknown script: {script_id}")
        sys.exit(1)

    downstream = dag.consumers(script_id)
    if not downstream:
        print(f"{script_id}: no downstream pipeline consumers (terminal or portal-only)")
        return

    if args.json:
        print(json.dumps([
            {"script": d, "s3_key": k, "constant": c}
            for d, k, c in downstream
        ], indent=2))
        return

    print(f"DOWNSTREAM CONSUMERS of {script_id}:")
    print()
    by_script: dict[str, list[tuple[str, str]]] = {}
    for d_script, s3_key, const in downstream:
        by_script.setdefault(d_script, []).append((s3_key, const))

    for d_script, keys in sorted(by_script.items()):
        print(f"  {d_script}:")
        for s3_key, const in keys:
            print(f"    {const}: {s3_key}")
    print()
    print(f"  Total: {len(downstream)} artifacts consumed by {len(by_script)} scripts")


def cmd_overlap(args):
    dag = _build_dag()
    a = args.script_a.upper()
    b = args.script_b.upper()

    if a not in dag.scripts:
        print(f"Unknown script: {a}")
        sys.exit(1)
    if b not in dag.scripts:
        print(f"Unknown script: {b}")
        sys.exit(1)

    result = dag.overlap(a, b)
    if not result:
        print(f"No shared S3 artifacts between {a} and {b}")
        return

    print(f"OVERLAP: {a} <-> {b}")
    print()
    for relationship, keys in result.items():
        print(f"  {relationship}:")
        for key in keys:
            print(f"    {key}")
    print()


def cmd_inject(args):
    dag = _build_dag()
    added = inject_pipeline_edges(dag, _WORKSPACE)
    if added is None:
        print("No comp-trace graph cache found. Run comp-build first.")
        sys.exit(1)
    print(f"Injected {added} pipeline edges into comp-trace graph cache.")


def cmd_stats(args):
    dag = _build_dag()
    print("PIPELINE STATISTICS")
    print(f"  Scripts:    {len(dag.scripts)}")
    print(f"  S3 keys:    {len(dag.s3_keys)} ({sum(1 for k in dag.s3_keys.values() if k.is_prefix)} prefixes, {sum(1 for k in dag.s3_keys.values() if k.is_function)} functions)")
    print(f"  Chains:     {len(dag.chains)}")
    print(f"  Groups:     {len(dag.groups)}")
    print(f"  Catalog:    {len(dag.catalog)} entries")
    print()

    # Edge counts
    total_reads = sum(len(s.read_keys) for s in dag.scripts.values())
    total_writes = sum(len(s.write_keys) for s in dag.scripts.values())
    print(f"  Total read edges:  {total_reads}")
    print(f"  Total write edges: {total_writes}")
    print()

    # Scripts with no detected reads (likely missing extraction)
    no_reads = [sid for sid, s in dag.scripts.items() if not s.reads]
    if no_reads:
        print(f"  WARNING: {len(no_reads)} scripts with no detected reads:")
        for sid in sorted(no_reads):
            print(f"    {sid}")
    print()

    # Scripts with no detected writes
    no_writes = [sid for sid, s in dag.scripts.items() if not s.writes]
    if no_writes:
        print(f"  NOTE: {len(no_writes)} scripts with no detected writes:")
        for sid in sorted(no_writes):
            print(f"    {sid}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog='comp-pipescript',
        description='Authoritative pipeline dependency tool for gold layer scripts.',
    )
    sub = parser.add_subparsers(dest='command')

    # dag
    p_dag = sub.add_parser('dag', help='Full execution DAG with I/O edges')
    p_dag.add_argument('--json', action='store_true', help='JSON output')

    # io
    p_io = sub.add_parser('io', help='Input/output manifest for one script')
    p_io.add_argument('script_id', help='Script ID (e.g., D_00)')
    p_io.add_argument('--json', action='store_true', help='JSON output')

    # chain
    p_chain = sub.add_parser('chain', help='Show chain membership and order')
    p_chain.add_argument('chain_name', help='Chain name (full, canonical, downstream, foundation, rebuild)')

    # feeds
    p_feeds = sub.add_parser('feeds', help='What scripts feed this one (upstream)')
    p_feeds.add_argument('script_id', help='Script ID')
    p_feeds.add_argument('--json', action='store_true', help='JSON output')

    # consumers
    p_consumers = sub.add_parser('consumers', help='What scripts consume this one (downstream)')
    p_consumers.add_argument('script_id', help='Script ID')
    p_consumers.add_argument('--json', action='store_true', help='JSON output')

    # overlap
    p_overlap = sub.add_parser('overlap', help='Shared S3 artifacts between two scripts')
    p_overlap.add_argument('script_a', help='First script ID')
    p_overlap.add_argument('script_b', help='Second script ID')

    # inject
    sub.add_parser('inject', help='Inject pipeline edges into comp-trace graph cache')

    # stats
    sub.add_parser('stats', help='Pipeline graph statistics')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    commands = {
        'dag': cmd_dag,
        'io': cmd_io,
        'chain': cmd_chain,
        'feeds': cmd_feeds,
        'consumers': cmd_consumers,
        'overlap': cmd_overlap,
        'inject': cmd_inject,
        'stats': cmd_stats,
    }
    commands[args.command](args)


if __name__ == '__main__':
    main()
