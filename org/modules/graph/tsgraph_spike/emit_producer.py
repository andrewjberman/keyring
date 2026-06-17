"""
NFRA_TSGRAPH.P1 Leg A/B -- translate the extractor's internal graph JSON into 0.7.0_AE's derive
producer contract, for the Nessie ingestion leg.

Contract (AE msg 192324Z/200157Z): node {"id","type",...} / edge {"source","target","edge_type",...},
wrapped { "producer":"ts-semantic","generated_at",...,"nodes","edges","coverage":{...,"unresolved":[...]} }.
node.type/edge.edge_type are STRING discriminators on the existing CloudNode/CloudEdge (NO schema change).

Run: python emit_producer.py [in_graph.json] [out_producer.json]
  defaults: out/portal_full.graph.json -> out/portal_full.producer.json
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GENERATED_AT = "2026-06-17T20:00:00Z"  # deterministic (Date.now() avoided); stamp at stage-time if needed


def main() -> int:
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out", "portal_full.graph.json")
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "out", "portal_full.producer.json")
    with open(src, "r", encoding="utf-8") as fh:
        g = json.load(fh)

    nodes = [{"id": n["id"], "type": n["label"], **n.get("attrs", {})} for n in g["nodes"]]
    edges = [{"source": e["src"], "target": e["dst"], "edge_type": e["label"], **e.get("attrs", {})} for e in g["edges"]]

    producer = {
        "producer": "ts-semantic",
        "generated_at": GENERATED_AT,
        "slice": g.get("meta", {}).get("slice") or g.get("meta", {}).get("mode") or "portal-full",
        "extractor": g.get("meta", {}).get("extractor"),
        "nodes": nodes,
        "edges": edges,
        "coverage": {
            "node_count": len(nodes),
            "edge_count": len(edges),
            "by_node_type": g.get("metrics", {}).get("nodes_by_label"),
            "by_edge_type": g.get("metrics", {}).get("edges_by_label"),
            "flowsto_by_kind": g.get("metrics", {}).get("flowsto_by_kind"),
            "per_category": g.get("metrics", {}).get("coverage"),
            "unresolved": g.get("unresolved", []),
        },
    }
    with open(dst, "w", encoding="utf-8") as fh:
        json.dump(producer, fh, indent=2)
    print(f"OK: wrote {os.path.relpath(dst, HERE)} ({len(nodes)} nodes, {len(edges)} edges, "
          f"{len(producer['coverage']['unresolved'])} unresolved recorded)")
    # a tiny sample for the AE scope-ping (manifest head + 2 node + 2 edge examples)
    sample = {
        "manifest_head": {k: producer[k] for k in ("producer", "generated_at", "slice", "extractor")},
        "coverage_summary": {k: producer["coverage"][k] for k in ("node_count", "edge_count", "flowsto_by_kind")},
        "node_examples": nodes[:2],
        "edge_examples": [e for e in edges if e["edge_type"] in ("FLOWS_TO", "FETCHES")][:2],
    }
    with open(os.path.join(HERE, "out", "portal_full.sample.json"), "w", encoding="utf-8") as fh:
        json.dump(sample, fh, indent=2)
    print("OK: wrote out/portal_full.sample.json (for the AE ingestion-scope ping)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
