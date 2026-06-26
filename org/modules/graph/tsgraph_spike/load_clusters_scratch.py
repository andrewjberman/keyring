"""
NFRA_TSGRAPH.P2-1 -- scratch Kuzu load + Phase-2 mandate validation of the cluster layer.

Loads the BASE ReactComponent nodes (P1 emit) + the ADDITIVE cluster layer (Page/PanelCluster nodes +
CLUSTERS/CONTAINS_DRILLDOWN/SHARES_SOURCE edges) into a scratch Kuzu on the EXACT platform schema
(CloudNode/CloudEdge, node_type/edge_type STRING discriminators) -- so the Cypher here is the SAME query
shape that runs against the canonical Nessie->Kuzu once AE (P2-2) materializes the layer. SCRATCH / frozen
vintage (Rule 20): local-load only; the real Nessie write is AE-owned.

Run: python load_clusters_scratch.py
"""
from __future__ import annotations

import json
import os
import shutil

import kuzu

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, "out", "portal_full.graph.json")
CLUSTERS = os.path.join(HERE, "out", "portal_clusters.graph.json")
DB_PATH = os.path.join(HERE, "out", "scratch_clusters_db")


def main() -> int:
    base = json.load(open(BASE, encoding="utf-8"))
    cl = json.load(open(CLUSTERS, encoding="utf-8"))

    # nodes needed for the cluster traversal: ReactComponent (base) + Page/PanelCluster (additive)
    rc_nodes = [n for n in base["nodes"] if n["label"] == "ReactComponent"]
    nodes = rc_nodes + cl["nodes"]
    edges = cl["edges"]  # CLUSTERS / CONTAINS_DRILLDOWN / SHARES_SOURCE
    node_ids = {n["id"] for n in nodes}
    # keep only edges whose endpoints are present (CONTAINS_DRILLDOWN -> ReactComponent stays in scope)
    edges = [e for e in edges if e["src"] in node_ids and e["dst"] in node_ids]

    if os.path.isdir(DB_PATH):
        try:
            shutil.rmtree(DB_PATH)
        except OSError:
            pass
    db = kuzu.Database(DB_PATH)
    conn = kuzu.Connection(db)
    for drop in ("DROP TABLE CloudEdge", "DROP TABLE CloudNode"):
        try:
            conn.execute(drop)
        except RuntimeError:
            pass
    conn.execute("CREATE NODE TABLE CloudNode(node_id STRING, node_type STRING, props STRING, PRIMARY KEY(node_id))")
    conn.execute("CREATE REL TABLE CloudEdge(FROM CloudNode TO CloudNode, edge_type STRING, props STRING)")

    for n in nodes:
        conn.execute("CREATE (:CloudNode {node_id:$i, node_type:$t, props:$p})",
                     {"i": n["id"], "t": n["label"], "p": json.dumps(n.get("attrs", {}))})
    for e in edges:
        conn.execute(
            "MATCH (a:CloudNode {node_id:$s}),(b:CloudNode {node_id:$d}) "
            "CREATE (a)-[:CloudEdge {edge_type:$t, props:$p}]->(b)",
            {"s": e["src"], "d": e["dst"], "t": e["label"], "p": json.dumps(e.get("attrs", {}))})
    print(f"OK: scratch Kuzu loaded (CloudNode/CloudEdge platform schema) -- {len(nodes)} nodes, {len(edges)} edges")

    def q(cy, params=None):
        r = conn.execute(cy, params or {})
        rows = []
        while r.has_next():
            rows.append(r.get_next())
        return rows

    # --- Phase-2 MANDATE query (node_type form of the TO's (p:Page)-[:CLUSTERS]->(c:PanelCluster)-[:CONTAINS_DRILLDOWN*0..]->(d)) ---
    # KUZU-BUILD LIMITATION (local pkg, empirically pinned 2026-06-26): variable-length recursion over the
    # single-table CloudEdge schema is unstable -- an inline rel-property filter on `*0..` is a PARSER ERROR,
    # and the `*0..N WHERE all(r in rels(e) ...)` workaround SEGFAULTS (exit 139) at bound N>=4 (N<=3 is safe).
    # The real drilldown tree reaches depth 4, so no safe recursive bound covers it locally. We therefore
    # validate the traversal with EXPLICIT fixed-length single-hop chains (single-hop inline filters are
    # crash-free) UNION'd over depths 1..MAXD -- crash-free AND full-depth. The recursive `*0..` form is
    # reserved for the comp-kuzu CANONICAL surface (newer Kuzu build) once AE P2-2 materializes the layer.
    MAXD = 4  # observed max CONTAINS_DRILLDOWN nesting depth (1..4)

    def _chain(n: int) -> str:
        # exactly n chained single-hop CONTAINS_DRILLDOWN edges from c to d
        hops = "".join(
            "-[:CloudEdge {edge_type:'CONTAINS_DRILLDOWN'}]->" + ("(:CloudNode)" if i < n - 1 else "(d:CloudNode)")
            for i in range(n))
        return f"MATCH (c){hops}"

    def _reach_distinct(cluster_pred: str) -> set:
        # DISTINCT drilldown-reachable node ids across depths 1..MAXD for clusters matching cluster_pred
        ids = set()
        for n in range(1, MAXD + 1):
            # WHERE-bind c in MATCH #1, then a second MATCH chains off the carried c (comma/new-MATCH required;
            # a bare pattern after WHERE is a parser error). _chain(n) itself starts with 'MATCH (c)...'.
            cy = (f"MATCH (c:CloudNode {{node_type:'PanelCluster'}}) WHERE {cluster_pred} "
                  + _chain(n)
                  + " RETURN DISTINCT d.node_id AS id")
            for (i,) in q(cy):
                ids.add(i)
        return ids

    print("\n=== Phase-2 mandate: per-page  Page -CLUSTERS-> PanelCluster -CONTAINS_DRILLDOWN(1..%d)-> d ===" % MAXD)
    page_rows = q(
        "MATCH (p:CloudNode {node_type:'Page'})-[:CloudEdge {edge_type:'CLUSTERS'}]->(c:CloudNode {node_type:'PanelCluster'}) "
        "RETURN p.props AS page, count(DISTINCT c) AS clusters ORDER BY clusters DESC")
    for page, c in page_rows:
        nm = json.loads(page).get("name")
        reach = _reach_distinct(f"c.node_id STARTS WITH 'cluster:{nm}:'")
        print(f"  {nm:28s} clusters={c:3d}  reachable(CONTAINS_DRILLDOWN 1..{MAXD})={len(reach)}")

    # --- drilldown nesting depth traverses (AdvisorIntelligence) ---
    print("\n=== AdvisorIntelligence: drilldown nesting depth (explicit per-depth chains, crash-free) ===")
    max_depth = 0
    ai_nodes: set = set()
    for n in range(1, MAXD + 1):
        cy = ("MATCH (c:CloudNode {node_type:'PanelCluster'}) WHERE c.node_id STARTS WITH 'cluster:AdvisorIntelligence:' "
              + _chain(n) + " RETURN DISTINCT d.node_id AS id")
        hits = [i for (i,) in q(cy)]
        if hits:
            max_depth = n
            ai_nodes.update(hits)
    print(f"  AdvisorIntelligence: max CONTAINS_DRILLDOWN depth = {max_depth}, distinct reachable nodes = {len(ai_nodes)}")

    # --- per-firm _partners cohort tagged first-class on drilldown edges ---
    print("\n=== per-firm _partners cohort axis tagged on CONTAINS_DRILLDOWN (first-class L3) ===")
    rows = q(
        "MATCH ()-[e:CloudEdge {edge_type:'CONTAINS_DRILLDOWN'}]->() "
        "RETURN e.props AS p")
    cohorts: dict[str, int] = {}
    kinds: dict[str, int] = {}
    for (p,) in rows:
        pp = json.loads(p)
        co = pp.get("cohort")
        if co:
            cohorts[co] = cohorts.get(co, 0) + 1
        kinds[pp.get("kind", "?")] = kinds.get(pp.get("kind", "?"), 0) + 1
    print(f"  cohort tag counts: {cohorts}")
    print(f"  drilldown kind counts: {kinds}")

    # --- SHARES_SOURCE cross-panel coupling sample ---
    print("\n=== SHARES_SOURCE cross-panel coupling (sample) ===")
    rows = q(
        "MATCH (a:CloudNode {node_type:'PanelCluster'})-[e:CloudEdge {edge_type:'SHARES_SOURCE'}]->(b:CloudNode {node_type:'PanelCluster'}) "
        "RETURN a.node_id, b.node_id, e.props LIMIT 6")
    for a, b, p in rows:
        pp = json.loads(p)
        print(f"  {a.split(':',1)[1]} <-> {b.split(':',1)[1]}  shared={pp.get('sharedSources') or pp.get('sharedTypes')} ({pp.get('sourceType')})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
