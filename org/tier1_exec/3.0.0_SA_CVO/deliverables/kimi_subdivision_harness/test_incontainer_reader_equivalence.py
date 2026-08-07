#!/usr/bin/env python3
"""EXECUTE the in-container reader path that was only ever verified BY CONSTRUCTION.

DONE-MEANS item 5. `0.7.0_AE_CloudOps` landed the Iceberg->Kuzu reader @525716a1df and stated
plainly that it was "verified BY CONSTRUCTION and NOT BY EXECUTION"; `1.0.0_SA_CTO~B` correctly
refused it as done. Nobody could execute it, because the Iceberg read is in-VPC only.

>> BUT THE ICEBERG READ IS SEPARABLE FROM THE PART THAT RUNS THE COMPOSITION. What actually risks
failing in-container is: AE's DDL, AE's keying expression, AE's query_fn row shape, and whether the
catalog's Cypher executes under kuzu 0.11.3 at all. NONE of that needs a VPC -- it needs a Kuzu DB
built the way AE builds it. This harness substitutes locally-extracted rows for the Iceberg scan and
executes everything downstream of it. <<

The local box has kuzu 0.11.3 -- the EXACT version pinned in the image -- so the engine under test is
the engine that will run.

WHAT THIS PROVES (executed, not argued):
  * the catalog's 14 detector queries + my 2 all EXECUTE under AE's DDL on kuzu 0.11.3
  * AE's query_fn row shape feeds the composition unchanged
  * the composition returns IDENTICAL figures to the comp-kuzu path:
        6,138 instances | 6,657 rows | 23 class | 1,255 structures | 8,978 CONTAINS edges

WHAT THIS DOES *NOT* PROVE -- stated so nobody reads it as full coverage of item 5:
  * the ICEBERG SCAN itself (pyiceberg RestCatalog against Nessie) is NOT exercised. In-VPC only.
  * `--build the image and run it` is not done here. This is the callee, not the deployment.
  * the rows fed in are already key-normalised (the local DB's node_id IS the key), so the main
    equivalence run does not exercise the raw-Iceberg -> key derivation. `test_keying()` below
    covers that dimension separately, on raw-shaped rows, WITH a negative control.

Run: python test_incontainer_reader_equivalence.py [--nodes nodes.json --edges edges.json]
Extract the inputs with:
  comp-kuzu --json "MATCH (n:CloudNode) RETURN n.node_id AS node_id, n.arn AS arn,
                    n.node_type AS node_type, n.name AS name, n.layer AS layer, n.props AS props"
  comp-kuzu --json "MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode)
                    RETURN a.node_id AS src, b.node_id AS dst, e.edge_type AS edge_type"
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# The comp-kuzu-path figures this must reproduce. Not aspirational -- measured on the same snapshot.
EXPECTED = {"instances": 6138, "rows_seen": 6657, "class_marked": 23,
            "structures": 1255, "contains": 8978}


def key_of(row):
    """AE's keying, lifted from kuzu_nessie_load.py:150 -- character-for-character."""
    return (row.get("arn") or "").strip() or (row.get("node_id") or "").strip()


def test_keying() -> bool:
    """The dimension the equivalence run CANNOT reach: raw-Iceberg-shaped rows.

    The local DB's node_ids are already keyed, so `arn or node_id` is idempotent there -- a pass
    proves nothing about the re-key. These rows carry a SHORT node_id beside a separate arn, which
    is what Iceberg actually holds.
    """
    cases = [
        ({"node_id": "opal-data-inf", "arn": "arn:aws:s3:::opal-data-inf"},
         "arn:aws:s3:::opal-data-inf"),
        ({"node_id": "out:AdvisorTable", "arn": ""}, "out:AdvisorTable"),
        ({"node_id": "out:AdvisorTable", "arn": None}, "out:AdvisorTable"),
        ({"node_id": "x", "arn": "   "}, "x"),
        ({"node_id": "  y  ", "arn": ""}, "y"),
    ]
    ok = True
    for row, want in cases:
        got = key_of(row)
        ok = ok and (got == want)
        print("    %s  %-24s -> %s" % ("PASS" if got == want else "FAIL", repr(row)[:24], got[:44]))
    # NEGATIVE CONTROL: the naive "read Iceberg node_id directly" reader must CHANGE identity here,
    # or this battery is not discriminating between the correct and the incorrect implementation.
    naive = (cases[0][0].get("node_id") or "").strip()
    discriminates = naive != cases[0][1]
    print("    negative control: naive raw-node_id keying yields %r (identity CHANGES): %s"
          % (naive, discriminates))
    return ok and discriminates


def build_db(nodes, edges):
    import kuzu                                              # noqa: PLC0415 - optional dep
    db_dir = os.path.join(tempfile.mkdtemp(prefix="c2c3_ae_ddl_"), "db")
    conn = kuzu.Connection(kuzu.Database(db_dir))
    # AE'S EXACT DDL @525716a1df:195-199. `props` is load-bearing: a props-less shape (SHAPE C)
    # returns CLEAN EMPTY results for every grain/substrate_side predicate rather than failing.
    conn.execute("CREATE NODE TABLE CloudNode(node_id STRING, arn STRING, node_type STRING, "
                 "name STRING, layer STRING, drift_class STRING, source STRING, "
                 "snapshot_ts INT64, props STRING, PRIMARY KEY(node_id))")
    conn.execute("CREATE REL TABLE CloudEdge(FROM CloudNode TO CloudNode, edge_type STRING, "
                 "layer STRING, snapshot_ts INT64, props STRING)")
    best = {}
    for r in nodes:
        k = key_of(r)
        if k:
            best[k] = r
    for k, r in best.items():
        conn.execute(
            "CREATE (n:CloudNode {node_id: $k, arn: $a, node_type: $t, name: $nm, "
            "layer: $l, props: $p})",
            {"k": k, "a": r.get("arn") or "", "t": r.get("node_type") or "",
             "nm": r.get("name") or "", "l": r.get("layer") or "", "p": r.get("props") or ""})
    n_edges = 0
    for e in edges:
        s, d = e.get("src"), e.get("dst")
        if s in best and d in best:
            conn.execute("MATCH (a:CloudNode {node_id: $s}), (b:CloudNode {node_id: $d}) "
                         "CREATE (a)-[:CloudEdge {edge_type: $t}]->(b)",
                         {"s": s, "d": d, "t": e.get("edge_type") or ""})
            n_edges += 1
    return conn, len(best), n_edges


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nodes", required=True)
    ap.add_argument("--edges", required=True)
    args = ap.parse_args()

    print("  KEYING BATTERY (the dimension the equivalence run cannot reach):")
    keying_ok = test_keying()
    print()

    nodes = json.load(open(args.nodes, encoding="utf-8"))
    edges = json.load(open(args.edges, encoding="utf-8"))
    conn, n_nodes, n_edges = build_db(nodes, edges)
    print("  DB built under AE's DDL: %d nodes, %d edges" % (n_nodes, n_edges))

    import c2_individuate as c2                               # noqa: PLC0415
    import c3_cover as c3                                     # noqa: PLC0415

    def query_fn(cypher):
        """AE's exact query_fn @525716a1df:236-247."""
        try:
            res = conn.execute(cypher)
            cols = res.get_column_names()
        except Exception as e:                                # noqa: BLE001
            print("    CYPHER FAILED: %s" % str(e)[:110])
            return [], -1
        return [dict(zip(cols, r)) for r in res], 0

    d2 = c2.compose(query_fn=query_fn,
                    vintage_fn=lambda: {"nodes_snapshot_id": "SIM", "edges_snapshot_id": "SIM-E"})
    d3 = c3.compose(d2, live_snap_fn=lambda: "SIM")
    got = {
        "instances": d2["counts"]["c2_motif_instances_distinct"],
        "rows_seen": d2["counts"]["rows_seen"],
        "class_marked": sum(1 for n in d2["nodes"] if n["props"].get("grain") == "class"),
        "structures": d3["counts"]["c3_structures_promoted"],
        "contains": d3["counts"]["contains_edges"],
    }
    print()
    ok = True
    for k, want in EXPECTED.items():
        good = got[k] == want
        ok = ok and good
        print("    %s  %-14s AE-reader=%-7d comp-kuzu=%d" % ("PASS" if good else "FAIL",
                                                             k, got[k], want))
    print()
    if ok and keying_ok:
        print("  EQUIVALENT. AE's DDL + keying + query_fn + kuzu 0.11.3 reproduce the comp-kuzu")
        print("  figures exactly. The ICEBERG SCAN remains unexercised (in-VPC only) -- this is the")
        print("  callee, not the deployment.")
    else:
        print("  *** DIVERGENCE -- the in-container path would not reproduce the local layer ***")
    return 0 if (ok and keying_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
