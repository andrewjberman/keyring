#!/usr/bin/env python3
"""COMPOSE TWICE -- the second time against a graph containing the FIRST run's own output.

>> THE CLASS THIS EXISTS FOR: every validation on this thread ran against a graph that does not yet
contain the validator's own product. The composition, the reader, the acceptance harness, the
determinism runs -- all of them were exercised in an epoch that ENDS the moment the layer lands.
A defect that only appears in the second epoch is UNREACHABLE UNTIL THE THING BEING TESTED
SUCCEEDS, and it arrives on the night everything finally works. <<

TWO REAL DEFECTS OF EXACTLY THIS SHAPE WERE FOUND 2026-08-07, in two seats, from ONE root cause:

  * `3.0.0_SA_CVO` (mine): the class-marking query selects on `node_type` alone. Post-landing all
    ~7,400 composed instances match it and are rewritten `grain:class` -- run 1 builds the layer,
    run 2 destroys it. Fixed @0871ce898f.
  * `1.0.0_SA_CTO~B`: `FROZEN_CONTROL` asserted the UNFILTERED node_type count == 19/4. Post-landing
    unfiltered C2Motif is 19 class + ~6,138 instance, so the self-test FAILS ON THE RUN WHERE
    EVERYTHING WORKED. Fixed @c73f4824b2. **A control that breaks when the system succeeds is not a
    control** -- and it would have fired in the same window as the defect above, meaning something
    completely different.

THE ROOT CAUSE IS ONE RULING, UNPROPAGATED (CTO~B's own analysis): instances must reuse the
REGISTERED node_types, because `derive_runner.py:1775` fails the derive closed on an unregistered
one. **That ruling made `node_type` NON-DISCRIMINATING between class and instance** -- grain became
the discriminator. Both seats then wrote code treating node_type as if it still separated the two
populations, in code written AFTER the ruling that stopped it doing so. Not two mistakes: one
unpropagated consequence.

WHAT THIS HARNESS PROVIDES that nobody had: a POST-LANDING GRAPH FIXTURE. Any instrument that will
run after the layer lands can be pointed at it TODAY.

MEASURED (2026-08-07, after both fixes):
    RUN 1  20,604 nodes / 41,160 edges  -> C2 6138  C3 1255  class 23  skipped 0
    RUN 2  27,997 nodes / 68,116 edges  -> C2 6138  C3 1255  class 23  skipped 7393
    IDEMPOTENT: YES.  7,416 emitted - 23 class upserts = 7,393 skipped -- the guard skips exactly
    the instances and re-marks exactly the class nodes.

NOT COVERED: this simulates the landed graph by UPSERTING run 1's output into the node table, which
matches the derive's wholesale overwrite of `graph_nodes`. It does NOT exercise the Iceberg commit
itself (in-VPC), and it does not prove anything about ACCUMULATION across many nights -- the derive
overwrites rather than appends, so accumulation is out of scope by construction, not by test.

Run: python test_idempotency_post_landing.py --nodes nodes.json --edges edges.json
(same inputs as test_incontainer_reader_equivalence.py -- see its docstring for the extraction)
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def _key_of(row):
    """The producer's keying -- imported, not re-typed."""
    from test_incontainer_reader_equivalence import key_of      # noqa: PLC0415
    return key_of(row)


def build(base, edges, extra_nodes=(), extra_edges=()):
    """A Kuzu DB under the PRODUCER'S OWN DDL, optionally carrying a prior run's output.

    UPSERT, not append: `merged[node_id] = n` mirrors the derive overwriting `graph_nodes`
    wholesale. Naive concatenation raises a duplicate-PK error on the 23 re-emitted class nodes --
    an artifact of the simulation, NOT of the product, and worth stating so the next reader does
    not chase it.
    """
    import kuzu                                                  # noqa: PLC0415
    import pyarrow as pa                                         # noqa: PLC0415
    from test_incontainer_reader_equivalence import extracted_ddl  # noqa: PLC0415

    merged = dict(base)
    for n in extra_nodes:
        merged[n["node_id"]] = n
    db_dir = os.path.join(tempfile.mkdtemp(prefix="c2c3_idem_"), "db")
    conn = kuzu.Connection(kuzu.Database(db_dir))
    for stmt in extracted_ddl():
        conn.execute(stmt)

    ks = list(merged)
    g = lambda k, f, dv="": (merged[k].get(f) or dv)             # noqa: E731
    ntab = pa.table({  # noqa: F841 - kuzu COPY resolves this from the caller frame
        "node_id": ks, "arn": [g(k, "arn") for k in ks],
        "node_type": [g(k, "node_type") for k in ks], "name": [g(k, "name") for k in ks],
        "layer": [g(k, "layer") for k in ks], "drift_class": [""] * len(ks),
        "source": [""] * len(ks), "snapshot_ts": [0] * len(ks),
        "props": [g(k, "props") for k in ks],
    })
    conn.execute("COPY CloudNode FROM ntab")

    kset = set(ks)
    se = [(e["src"], e["dst"], e.get("edge_type") or "")
          for e in edges if e["src"] in kset and e["dst"] in kset]
    se += [(e["source"], e["target"], e["edge_type"]) for e in extra_edges
           if e["source"] in kset and e["target"] in kset]
    etab = pa.table({"src": [x[0] for x in se], "dst": [x[1] for x in se],  # noqa: F841 - as above
                     "edge_type": [x[2] for x in se], "layer": [""] * len(se),
                     "snapshot_ts": [0] * len(se), "props": [""] * len(se)})
    conn.execute("COPY CloudEdge FROM etab")
    return conn, len(ks), len(se)


def reader_for(conn):
    def query_fn(cypher):
        try:
            res = conn.execute(cypher)
            cols = res.get_column_names()
        except Exception:                                        # noqa: BLE001
            return [], -1
        return [dict(zip(cols, r)) for r in res], 0
    return query_fn


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nodes", required=True)
    ap.add_argument("--edges", required=True)
    args = ap.parse_args()

    import c2_individuate as c2                                  # noqa: PLC0415
    import c3_cover as c3                                        # noqa: PLC0415

    rows = json.load(open(args.nodes, encoding="utf-8"))
    edges = json.load(open(args.edges, encoding="utf-8"))
    base = {}
    for r in rows:
        k = _key_of(r)
        if k:
            base[k] = r
    if not base:
        print("  REFUSING: node set is EMPTY -- an idempotency PASS over nothing is an artifact")
        return 2

    vf = lambda: {"nodes_snapshot_id": "SIM", "edges_snapshot_id": "SIM-E"}   # noqa: E731

    conn1, n1, e1 = build(base, edges)
    a2 = c2.compose(query_fn=reader_for(conn1), vintage_fn=vf)
    a3 = c3.compose(a2, live_snap_fn=lambda: "SIM")
    print("  RUN 1  graph %6d nodes / %6d edges -> C2 %d  C3 %d  class %d  skipped %d"
          % (n1, e1, a2["counts"]["c2_motif_instances_distinct"],
             a3["counts"]["c3_structures_promoted"],
             a2["counts"]["class_nodes_marked_grain_class"],
             a2["counts"]["already_instance_skipped"]))

    # THE POST-LANDING FIXTURE: run 1's output, landed exactly as the derive lands it (layer=semctl).
    extra = [{"node_id": n["node_id"], "node_type": n["node_type"], "layer": "semctl",
              "arn": "", "name": n["node_id"], "props": json.dumps(n["props"])}
             for n in list(a2["nodes"]) + list(a3["nodes"])]
    conn2, n2, e2 = build(base, edges, extra, list(a2["edges"]) + list(a3["edges"]))
    b2 = c2.compose(query_fn=reader_for(conn2), vintage_fn=vf)
    b3 = c3.compose(b2, live_snap_fn=lambda: "SIM")
    print("  RUN 2  graph %6d nodes / %6d edges -> C2 %d  C3 %d  class %d  skipped %d"
          % (n2, e2, b2["counts"]["c2_motif_instances_distinct"],
             b3["counts"]["c3_structures_promoted"],
             b2["counts"]["class_nodes_marked_grain_class"],
             b2["counts"]["already_instance_skipped"]))

    same = all([
        a2["counts"]["c2_motif_instances_distinct"] == b2["counts"]["c2_motif_instances_distinct"],
        a3["counts"]["c3_structures_promoted"] == b3["counts"]["c3_structures_promoted"],
        a2["counts"]["class_nodes_marked_grain_class"] == b2["counts"]["class_nodes_marked_grain_class"],
    ])
    engaged = b2["counts"]["already_instance_skipped"] > 0
    print()
    print("  IDEMPOTENT UNDER ITS OWN OUTPUT : %s" % ("YES" if same else "*** NO ***"))
    # WITHOUT THIS SECOND ASSERTION THE FIRST IS HOLLOW: if the fixture failed to land run 1's
    # output, run 2 would be a clean-graph run and would trivially "match".
    print("  GUARD ENGAGED ON RUN 2          : %s (skipped %d of %d landed nodes)"
          % (engaged, b2["counts"]["already_instance_skipped"], len(extra)))
    if same and engaged:
        print("  -> the second epoch is exercised, and the composition is stable in it")
    return 0 if (same and engaged) else 1


if __name__ == "__main__":
    sys.exit(main())
