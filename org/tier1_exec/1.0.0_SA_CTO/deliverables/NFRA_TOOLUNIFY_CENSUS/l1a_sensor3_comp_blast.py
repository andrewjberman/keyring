"""l1a_sensor3_comp_blast -- L1a residue sensor #3: comp-blast over its own DAG source.

NFRA_COMPLEARN L1a-SENSOR-3 (dispatch 1.0.0_SA_CTO~Z 20260725T090835Z). The DATA/DAG-shaped
sensor the L1a spec requires -- "one where doc_only is N/A" -- so the L2 aggregate is never
designed against a single schema shape.

PATTERN, NOT PLATFORM (SENSOR_CONTRACT_PLATFORM_OR_PATTERN.md): this sensor REUSES NOTHING of
comp-residue's extractor (whose structure-vs-data law inverts on a DAG); it shares only the
TYPE (boundary_report) and the exit contract.

TOOL UNDER SENSE: comp-blast (engine: org/modules/graph/cli.py cmd_blast + trace_graph.TraceGraph).
SOURCE, derived from the tool's own code: the DAG cache cli.py reads (_CACHE_FILE ->
.comp-graph/graph.json). NOT the shared kuzu DB -- no substrate contention.

UNIT GRAIN (the load-bearing choice for this shape): the DAG's TYPE plane -- edge_type values
and node_type values -- never file paths, never raw container keys (the s3 inversion:
2261 meaningless container paths vs the real typed units). One report per grain; grains are
different address spaces and are NEVER aggregated together.

TRAVERSAL DERIVATION -- FROM THE TOOL'S OWN CODE, NEVER HAND-DECLARED:
  edge_type grain: the blast BFS (trace_graph.upstream/downstream) is verified TYPE-BLIND by
    AST inspection AT RUN TIME -- the sensor parses trace_graph.py and asserts no If-test in
    either walk function references edge_type. Type-blind walk => every live edge_type is
    traversed. If the AST check ever finds a type filter, affected units become UNKNOWN
    (first-class, reported, never silently dropped and never coerced to covered).
  node_type grain: the --all-producers sweep's candidate filter is EXECUTED, not read --
    cli._producer_node_types() is imported and called. covered = live types the filter admits;
    orphan = live types the filter excludes (evidence cites the executing function).

doc_only: the DAG has NO prose plane -> applicable=false, count=null. N/A IS NEVER 0.

MENTION ANNOTATION (in-band items, direction declared): a literal-mention scan over the engine
files annotates each unit. CAVEAT carried in-band: cli.py hosts multiple subcommands, so a
mention may belong to a non-blast subcommand -- the mention annotation is engine-file-scoped,
not blast-function-scoped. Mentions UNDER-report traversal (METHODS law) and here may also
over-attribute knowledge to blast specifically; the partition never rests on mentions, only
the annotations do.

EXIT CONTRACT (== comp-residue): 0 PASS (clean) / 1 FAIL (tool error) / 2 VERDICT (residue
found -- an estate verdict, not a tool failure) / 3 REFUSE (nothing could be compared; never
"everything is residue").

ASCII-only. Read-only: reads graph.json + engine sources; writes ONLY --emit target.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

RC_PASS, RC_FAIL, RC_VERDICT, RC_REFUSE = 0, 1, 2, 3

_ENGINE_REL = (".tools/comp-blast", "org/modules/graph/cli.py", "org/modules/graph/trace_graph.py")


def _ws_root() -> Path:
    """Workspace root = nearest ancestor holding the boundary_report type. Self-contained
    resolution -- no /c/ vs /cygdrive/c/ vs C:/ construction (the three-convention hazard)."""
    p = Path(__file__).resolve()
    for anc in p.parents:
        if (anc / "org" / "modules" / "graph" / "boundary_report.py").is_file():
            return anc
    raise RuntimeError("workspace root not found above %s" % p)


def _load_graph(path: Path):
    """Load the DAG. Returns (nodes: dict, edges: list) or raises with a REFUSE-able reason."""
    if not path.is_file():
        raise FileNotFoundError("graph source not found: %s" % path)
    raw = json.loads(path.read_text(encoding="utf-8"))
    nodes = raw.get("nodes")
    edges = raw.get("edges")
    if not isinstance(nodes, dict) or not isinstance(edges, list):
        raise ValueError("graph source lacks nodes{}/edges[] shape: %s" % path)
    return raw, nodes, edges


def _walk_is_type_blind(trace_graph_path: Path) -> tuple:
    """AST-derive whether the blast BFS filters on edge_type. Returns (blind: bool, detail).

    Mechanical, run-time derivation from the tool's own code (never a hand-declared claim):
    parse trace_graph.py, locate TraceGraph.upstream/.downstream, and inspect every If test
    inside them for a reference to `edge_type`. No such test => the walk traverses every edge
    regardless of type => every live edge_type is traversed.
    """
    tree = ast.parse(trace_graph_path.read_text(encoding="utf-8"))
    found = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in ("upstream", "downstream"):
            filters = []
            for sub in ast.walk(node):
                if isinstance(sub, ast.If):
                    test_src = ast.dump(sub.test)
                    if "edge_type" in test_src:
                        filters.append(test_src[:120])
            found[node.name] = filters
    if set(found) != {"upstream", "downstream"}:
        raise ValueError("could not locate both walk functions in %s (found: %s)"
                         % (trace_graph_path, sorted(found)))
    blind = not (found["upstream"] or found["downstream"])
    return blind, found


def _mention_map(ws: Path, units: list) -> dict:
    texts = {}
    for rel in _ENGINE_REL:
        fp = ws / rel
        texts[rel] = fp.read_text(encoding="utf-8", errors="replace") if fp.is_file() else ""
    out = {}
    for u in units:
        pat = re.compile(r"\b" + re.escape(u) + r"\b")
        out[u] = sorted(rel for rel, txt in texts.items() if pat.search(txt))
    return out


def build_report(ws: Path, graph_path: Path, grain: str) -> tuple:
    """Returns (report_dict, stdout_lines, exit_code)."""
    raw, nodes, edges = _load_graph(graph_path)
    head = str(raw.get("built_at") or "UNKNOWN-VINTAGE")

    if grain == "edge_type":
        units = sorted({e.get("edge_type") for e in edges if e.get("edge_type")})
    else:
        units = sorted({n.get("node_type") for n in nodes.values() if n.get("node_type")})
    if not units:
        raise ValueError("zero %s units enumerable from %s -- nothing to compare" % (grain, graph_path))

    mentions = _mention_map(ws, units)
    lines = []
    unknown = []  # first-class: (unit, reason) -- reported, excluded from the partition, never dropped

    if grain == "edge_type":
        address_space = "dag_edge_type"
        blind, filter_detail = _walk_is_type_blind(ws / "org/modules/graph/trace_graph.py")
        if blind:
            covered = list(units)
            orphan = []
            evidence = ("traversed by the blast BFS: AST-verified TYPE-BLIND this run "
                        "(no If-test on edge_type in trace_graph.upstream/downstream)")
        else:
            # A filter exists that this sensor cannot semantically evaluate -> UNKNOWN, not covered.
            covered, orphan = [], []
            unknown = [(u, "walk carries an edge_type filter this sensor cannot evaluate: %s"
                        % filter_detail) for u in units]
            evidence = "walk NOT type-blind"
        traversal_note = ("traversal under test: the blast BFS itself (both directions), "
                         "derivation: run-time AST inspection of trace_graph.py")
        dead_declared = []  # declared-set drift is computed below for stdout, common path
        try:
            import trace_graph  # noqa: F401  (import for the declared set)
            declared = set(trace_graph.EDGE_TYPES)
        except Exception:
            sys.path.insert(0, str(ws / "org" / "modules" / "graph"))
            import trace_graph
            declared = set(trace_graph.EDGE_TYPES)
        dead_declared = sorted(declared - set(units))
        undeclared_live = sorted(set(units) - declared)
        declared_note = ("declared EDGE_TYPES (trace_graph.py) vs live source: %d declared members "
                        "ABSENT from live data (%s) -- declared OVER-reports; %d live types "
                        "UNDECLARED (%s). Dead members are NOT in the source surface and are "
                        "therefore reported here IN-BAND, outside the partition."
                        % (len(dead_declared), ", ".join(dead_declared) or "-",
                           len(undeclared_live), ", ".join(undeclared_live) or "-"))
    else:
        address_space = "dag_node_type"
        sys.path.insert(0, str(ws / "org" / "modules" / "graph"))
        import cli as blast_cli  # the tool's own code, EXECUTED (guarded by __main__ in cli.py)
        filt = set(blast_cli._producer_node_types())
        covered = sorted(set(units) & filt)
        orphan = sorted(set(units) - filt)
        evidence = ("candidate filter EXECUTED: cli._producer_node_types() -> %s" % sorted(filt))
        traversal_note = ("traversal under test: the --all-producers sweep's candidate filter "
                         "(cli.py _producer_node_types), derivation: the function is imported and "
                         "CALLED, not read")
        dead_declared = sorted(filt - set(units))
        declared_note = ("filter members ABSENT from live data: %d (%s) -- the hardcoded candidate "
                        "set has drifted from the source's live enumeration (frozen-enumeration "
                        "shape, inside the tool). NOT in the source surface -> reported IN-BAND, "
                        "outside the partition." % (len(dead_declared), ", ".join(dead_declared) or "-"))

    classified = [u for u in units if u not in {x[0] for x in unknown}]
    items = []
    for u in classified:
        cell = "covered" if u in covered else "orphan"
        m = mentions.get(u) or []
        items.append({
            "address": u,
            "cell": cell,
            "method": "traversal",
            "evidence": evidence + (" | engine-file mention: %s" % ", ".join(m) if m
                                    else " | NO engine-file mention (walked/excluded anonymously)"),
        })

    report = {
        "tool": "comp-blast",
        "source": str(graph_path),
        "address_space": address_space,
        "head": head,
        "surface_total": len(classified),
        "cells": {
            "covered": {"applicable": True, "count": len([u for u in classified if u in covered]),
                        "method": "traversal"},
            "member": {"applicable": True, "count": 0, "method": "traversal"},
            "doc_only": {"applicable": False, "count": None, "method": None},
            "orphan": {"applicable": True, "count": len([u for u in classified if u in orphan]),
                       "method": "traversal"},
        },
        "items": items,
    }

    lines.append("L1A-SENSOR-3 (comp-blast, DAG shape) -- grain=%s address_space=%s" % (grain, address_space))
    lines.append("  source: %s  head(built_at): %s" % (graph_path, head))
    lines.append("  %s" % traversal_note)
    lines.append("  DENOMINATOR: %d live %s units enumerated from the source; %d classified, %d UNKNOWN"
                 % (len(units), grain, len(classified), len(unknown)))
    lines.append("  partition: covered=%d member=0 orphan=%d doc_only=N/A (no prose plane on a DAG -- "
                 "applicable=false, count=null, NEVER zero)"
                 % (report["cells"]["covered"]["count"], report["cells"]["orphan"]["count"]))
    lines.append("  direction: partition method=traversal (exact). Mention annotations UNDER-report "
                 "(and are engine-file-scoped, may over-attribute to blast specifically). "
                 "Declared sets OVER-report.")
    lines.append("  " + declared_note)
    for u, why in unknown:
        lines.append("  UNKNOWN: %s -- %s (excluded from surface_total, printed, never dropped)" % (u, why))
    if report["cells"]["orphan"]["count"]:
        lines.append("  ORPHANS (in-source, not traversed by the mode under test -- materiality is "
                     "the inference gate's call, not this sensor's):")
        for u in sorted(orphan):
            lines.append("    - %s" % u)

    rc = RC_VERDICT if report["cells"]["orphan"]["count"] else RC_PASS
    return report, lines, rc


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="L1a residue sensor #3: comp-blast over its DAG source")
    ap.add_argument("--graph", default=None, help="graph.json path (default: the tool's own cache)")
    ap.add_argument("--grain", choices=("edge_type", "node_type"), required=True,
                    help="the DAG's type plane -- the unit grain for this report")
    ap.add_argument("--emit", default=None, help="write the boundary report JSON here")
    args = ap.parse_args(argv)

    try:
        ws = _ws_root()
        graph_path = Path(args.graph) if args.graph else (ws / ".comp-graph" / "graph.json")
        try:
            report, lines, rc = build_report(ws, graph_path, args.grain)
        except (FileNotFoundError, ValueError, json.JSONDecodeError) as err:
            print("REFUSE: %s" % err)
            print("  (coverage refusal: the source could not be established -- refusing is not "
                  "'everything is residue')")
            print("EXIT: %d (REFUSE)" % RC_REFUSE)
            return RC_REFUSE

        sys.path.insert(0, str(ws))
        from org.modules.graph.boundary_report import validate
        violations = validate(report)
        non_br008 = [v for v in violations if v.code != "BR008"]
        for line in lines:
            print(line)
        if non_br008:
            print("  CONFORMANCE: FAIL -- %s" % non_br008)
            print("EXIT: %d (FAIL)" % RC_FAIL)
            return RC_FAIL
        print("  CONFORMANCE: PASS (%s)" % (
            "clean" if not violations else
            "BR008 only -- open-set address_space %r reported-not-silent, by design" % report["address_space"]))

        if args.emit:
            Path(args.emit).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
            print("  emitted: %s" % args.emit)
        verdictword = {RC_PASS: "PASS -- clean, no residue at this grain",
                       RC_VERDICT: "VERDICT -- residue found (an estate verdict, not a tool failure)"}[rc]
        print("EXIT: %d (%s)" % (rc, verdictword))
        return rc
    except Exception as err:  # tool error -- LOUD, never a silent empty
        print("FAIL: %s: %s" % (type(err).__name__, err))
        print("EXIT: %d (FAIL)" % RC_FAIL)
        return RC_FAIL


if __name__ == "__main__":
    sys.exit(main())
