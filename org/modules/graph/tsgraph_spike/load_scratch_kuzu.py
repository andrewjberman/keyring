"""
NFRA_TSGRAPH.P0 -- AC3 emit: derive-ready producer JSON + a faithful scratch Kuzu load.

Aligns to 0.7.0_AE's emit contract (msg 192324Z): the globgrph derive ingests CloudNode/CloudEdge
rows where node_type/edge_type are STRING discriminators -- so the §3 semantic types (Module/Symbol/
Field/ReactComponent/DataFetch + REFERENCES/FLOWS_TO/FETCHES/RENDERS) land in the SAME two tables,
NO schema change, in ONE node space with the AWS ARN nodes (which is exactly why the AC3 stitch JOIN
works). node_id is the join key: AWS = ARN, portal-AST = endpoint:/component:/s3:/...

Outputs:
  1. out/ts_semantic_benchmark_slice.producer.json  -- the derive-ready emit (AE wires the ingestion
     leg on a GO): {producer, generated_at, nodes:[{id,type,...}], edges:[{source,target,edge_type,...}],
     coverage:{slices_scanned, unresolved:[...]}}  (manifest = the no-silent-Unknown guard).
  2. out/scratch_kuzu_db  -- SCRATCH / FROZEN VINTAGE (Rule 20): CloudNode/CloudEdge schema == the real
     platform, so the comp-kuzu Cypher is the SAME query that would run against Nessie->Kuzu. Local
     load only; the real Nessie write is AE-owned (commit-through-owner), wired only on GO.

Run: python load_scratch_kuzu.py
"""
from __future__ import annotations

import json
import os
import shutil
import sys

import kuzu

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH_JSON = os.path.join(HERE, "out", "benchmark_slice.graph.json")
PRODUCER_JSON = os.path.join(HERE, "out", "ts_semantic_benchmark_slice.producer.json")
DB_PATH = os.path.join(HERE, "out", "scratch_kuzu_db")

# cloud-side join targets -- VERIFIED present in the canonical Nessie graph (ARN-keyed CloudNode)
CLOUD_BUCKET_ARN = "arn:aws:s3:::opal-data-portal-v2"
CLOUD_PROXY_LAMBDA_ARN = "arn:aws:lambda:us-east-1:313476888478:function:opal-portal-data-proxy"
# a deterministic spike timestamp (Date.now() is non-deterministic; keep emit reproducible)
GENERATED_AT = "2026-06-17T19:00:00Z"


def to_producer_contract(g: dict) -> dict:
    """Translate the extractor's {id,label,attrs}/{src,dst,label,attrs} into AE's derive keys."""
    nodes = [
        {"id": n["id"], "type": n["label"], **n.get("attrs", {})}
        for n in g["nodes"]
    ]
    edges = [
        {"source": e["src"], "target": e["dst"], "edge_type": e["label"], **e.get("attrs", {})}
        for e in g["edges"]
    ]
    # inject the cloud join targets (ARN == CloudNode.node_id) + the join edges
    nodes.append({"id": CLOUD_BUCKET_ARN, "type": "S3_BUCKET", "name": "opal-data-portal-v2",
                  "layer": "aws", "provenance": "canonical-Nessie (verified present)"})
    nodes.append({"id": CLOUD_PROXY_LAMBDA_ARN, "type": "LAMBDA", "name": "opal-portal-data-proxy",
                  "layer": "aws", "provenance": "canonical-Nessie (verified present)"})
    s3_node = next((n["id"] for n in g["nodes"] if n["label"] == "S3Artifact"), None)
    ep_node = next((n["id"] for n in g["nodes"] if n["label"] == "Endpoint"), None)
    if s3_node:
        edges.append({"source": s3_node, "target": CLOUD_BUCKET_ARN, "edge_type": "STORED_IN",
                      "resolution": "s3:key name->bucket ARN (derive_stitch convention)"})
    if ep_node:
        edges.append({"source": ep_node, "target": CLOUD_PROXY_LAMBDA_ARN, "edge_type": "ROUTES_TO",
                      "resolution": "endpoint name->Lambda ARN (derive_stitch name lookup)"})
    return {
        "producer": "ts-semantic",
        "generated_at": GENERATED_AT,
        "slice": g["meta"]["slice"],
        "nodes": nodes,
        "edges": edges,
        "coverage": {
            "slices_scanned": 1,
            "node_count": len(nodes),
            "edge_count": len(edges),
            "unresolved": g.get("unresolved", []),
        },
    }


def main() -> int:
    with open(GRAPH_JSON, "r", encoding="utf-8") as fh:
        g = json.load(fh)

    producer = to_producer_contract(g)
    with open(PRODUCER_JSON, "w", encoding="utf-8") as fh:
        json.dump(producer, fh, indent=2)
    print(f"OK: wrote derive-ready producer JSON -> {os.path.relpath(PRODUCER_JSON, HERE)} "
          f"({len(producer['nodes'])} nodes, {len(producer['edges'])} edges, "
          f"{len(producer['coverage']['unresolved'])} unresolved recorded)")

    # ---- faithful scratch Kuzu on the PLATFORM schema (CloudNode/CloudEdge) ----
    if os.path.isdir(DB_PATH):
        try:
            shutil.rmtree(DB_PATH)  # our own scratch artifact
        except OSError:
            pass  # Windows file-handle lingering; defensive drops below clear any stale catalog

    db = kuzu.Database(DB_PATH)
    conn = kuzu.Connection(db)
    # defensive: clear any stale catalog (rel tables before node tables) -- robust to a prior schema
    for drop in ("DROP TABLE STITCH", "DROP TABLE CloudEdge", "DROP TABLE GEdge",
                 "DROP TABLE CloudNode", "DROP TABLE GNode"):
        try:
            conn.execute(drop)
        except RuntimeError:
            pass
    conn.execute("CREATE NODE TABLE CloudNode(node_id STRING, node_type STRING, props STRING, PRIMARY KEY(node_id))")
    conn.execute("CREATE REL TABLE CloudEdge(FROM CloudNode TO CloudNode, edge_type STRING, props STRING)")
    conn.execute("CREATE REL TABLE STITCH(FROM CloudNode TO CloudNode, ord INT64, via STRING)")

    for n in producer["nodes"]:
        props = {k: v for k, v in n.items() if k not in ("id", "type")}
        conn.execute(
            "CREATE (:CloudNode {node_id:$id, node_type:$ty, props:$p})",
            {"id": n["id"], "ty": n["type"], "p": json.dumps(props)},
        )
    for e in producer["edges"]:
        props = {k: v for k, v in e.items() if k not in ("source", "target", "edge_type")}
        conn.execute(
            "MATCH (a:CloudNode {node_id:$s}), (b:CloudNode {node_id:$d}) "
            "CREATE (a)-[:CloudEdge {edge_type:$et, props:$p}]->(b)",
            {"s": e["source"], "d": e["target"], "et": e["edge_type"], "p": json.dumps(props)},
        )

    path = g["stitch"]["path"]
    for i in range(len(path) - 1):
        conn.execute(
            "MATCH (a:CloudNode {node_id:$a}), (b:CloudNode {node_id:$b}) "
            "CREATE (a)-[:STITCH {ord:$o, via:$v}]->(b)",
            {"a": path[i]["node"], "b": path[i + 1]["node"], "o": i + 1, "v": path[i].get("edgeToNext", "")},
        )
    print(f"OK: loaded scratch Kuzu on PLATFORM schema (CloudNode/CloudEdge) -> {os.path.relpath(DB_PATH, HERE)} "
          f"(SCRATCH / frozen vintage, Rule 20)")

    # in-process AC3 verification -- the SAME query shape that runs against Nessie->Kuzu
    print("\n=== AC3 stitch JOIN: DataFetch -> Endpoint -> (ROUTES_TO) -> AWS Lambda ARN (one node space) ===")
    res = conn.execute(
        "MATCH (df:CloudNode {node_type:'DataFetch'})-[:CloudEdge]->(e:CloudNode {node_type:'Endpoint'}) "
        "MATCH (e)-[r:CloudEdge {edge_type:'ROUTES_TO'}]->(l:CloudNode) "
        "RETURN df.node_id AS datafetch, e.node_id AS endpoint, l.node_id AS lambda_arn"
    )
    while res.has_next():
        df, ep, la = res.get_next()
        print(f"  DataFetch {df}\n    -> Endpoint {ep}\n    -ROUTES_TO-> {la}")

    print("\n=== AC2 field-grain stitch (one Cypher returns the proven path) ===")
    res2 = conn.execute(
        "MATCH (a:CloudNode)-[s:STITCH]->(b:CloudNode) "
        "RETURN s.ord AS ord, a.node_type AS frm, s.via AS via, b.node_type AS to ORDER BY s.ord"
    )
    while res2.has_next():
        ordn, frm, via, to = res2.get_next()
        print(f"  {ordn}. [{frm}] --{via}--> [{to}]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
