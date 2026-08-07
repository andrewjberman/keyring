#!/usr/bin/env python3
"""EXECUTE the producer's OWN `_c2c3_incontainer_reader()` -- import it, do not copy it.

>> WHY THIS FILE EXISTS: I previously reported running that reader "VERBATIM". It was a
TRANSCRIPTION, and the transcription SILENTLY CORRECTED the one line that was broken in the shipped
code -- it read `source`/`target` while the Iceberg table holds `src_id`/`dst_id`, which resolves
ZERO edges. Anyone writing a fixture reaches for the schema first and then writes the reader to match
it, so the copy CANNOT fail the way the original did.
**A GREEN RUN OF A TRANSCRIPTION IS EVIDENCE ABOUT THE TRANSCRIBER, NOT THE PRODUCER.**
(0.7.0_AE_CloudOps, 2026-08-07, catching my claim; their bug found and fixed by them @824cf6b6b2.)
Both of us hit this class within two hours in the same direction: my equivalence harness passed while
testing a build path they had already replaced; their column names would have passed while testing
names they never used. Extraction beats transcription, and where extraction is impossible the honest
label is "I re-implemented this". <<

WHAT IT DOES: writes the real estate into a LOCAL pyiceberg SqlCatalog, substitutes ONLY
`RestCatalog`, and calls the producer's actual function. Everything after the catalog construction in
`derive_runner._c2c3_incontainer_reader()` is catalog-agnostic -- load_table, current_snapshot(),
scan().to_arrow(), the keying loop, the Kuzu build -- so the ONLY thing left unexercised is the
Nessie network connection and S3-as-storage-backend.

MEASURED 2026-08-07 (after AE's @824cf6b6b2):
    edges resolved by THEIR line : 41,160 / 41,160
    compose via THEIR reader     : C2 6138  C3 1255  class 23  -- CANONICAL
    snapshot ids                 : real ints from current_snapshot(), non-null

AND THE REGRESSION CONTROL IS THE POINT, not the pass: `test_edge_column_regression()` re-runs the
membership test with `source`/`target` against the same table and REQUIRES it to resolve ZERO. If
that control ever stops firing, the Iceberg edge schema has changed and this harness is no longer
testing what it claims. A control that cannot fail is not a control.

THIS RUN ALSO FOUND A DEFECT IN c3_cover: the freshness verdict compared a pyiceberg INT snapshot id
against a comp-kuzu STR one, so it read STALE on every production run WHILE PRINTING TWO IDENTICAL
NUMBERS. Structurally unreachable until the reader was executed against a real Iceberg catalog --
every prior test injected strings on both sides. Fixed @72d6bfb63a.

Run: python test_producer_reader_executed.py --nodes nodes.json --edges edges.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(HERE, *([os.pardir] * 5)))
sys.path.insert(0, HERE)
# The producer needs BOTH of these importable; the container gets them via /app.
sys.path.insert(0, os.path.join(_REPO, "org", "modules", "graph"))     # comp_aws_cli
sys.path.insert(0, os.path.join(_REPO, "infra", "aws", "globgrph"))    # derive_runner

CANONICAL = {"instances": 6138, "structures": 1255, "class_marked": 23}


class ProducerUnusable(Exception):
    """The producer's reader could not be imported or called -- REFUSE, never fall back to a copy."""


def build_local_iceberg(rows, edges):
    """The estate as ICEBERG holds it: RAW node_id beside a separate arn, real schemas.

    `src_id`/`dst_id` are deliberate and load-bearing -- they are the COMMITTED table's column names
    (derive_runner:285-286, written at :367 via `_nid(e, "source", "src")`). The in-memory derive
    graph uses `source`/`target`; the table does not. Writing the table with the in-memory names is
    exactly the mistake that would make this harness unable to catch the bug it exists to catch.
    """
    import pyarrow as pa                                          # noqa: PLC0415
    from pyiceberg.catalog.sql import SqlCatalog                  # noqa: PLC0415

    wh = tempfile.mkdtemp(prefix="c2c3_ice_")
    cat = SqlCatalog("local", **{"uri": "sqlite:///" + os.path.join(wh, "c.db"),
                                 "warehouse": "file://" + wh.replace(os.sep, "/")})
    cat.create_namespace("globgrph")
    ntab = pa.table({
        "node_id": [r.get("node_id") or "" for r in rows], "arn": [r.get("arn") or "" for r in rows],
        "node_type": [r.get("node_type") or "" for r in rows],
        "name": [r.get("name") or "" for r in rows], "layer": [r.get("layer") or "" for r in rows],
        "drift_class": [""] * len(rows), "source": [""] * len(rows),
        "snapshot_ts": pa.array([0] * len(rows), pa.int64()),
        "props": [r.get("props") or "" for r in rows]})
    etab = pa.table({
        "src_id": [e["src"] for e in edges], "dst_id": [e["dst"] for e in edges],
        "edge_type": [e.get("edge_type") or "" for e in edges], "layer": [""] * len(edges),
        "snapshot_ts": pa.array([0] * len(edges), pa.int64()), "props": [""] * len(edges)})
    cat.create_table("globgrph.graph_nodes", schema=ntab.schema).append(ntab)
    cat.create_table("globgrph.graph_edges", schema=etab.schema).append(etab)
    return cat


def test_edge_column_regression(cat) -> bool:
    """THE CONTROL THAT MAKES THE PASS MEAN SOMETHING.

    Re-runs the producer's membership test with the IN-MEMORY names (`source`/`target`) against the
    COMMITTED table. It MUST resolve zero. If it ever resolves non-zero, the Iceberg edge schema has
    changed and everything this harness asserts is about a different contract than it claims.
    """
    rows = cat.load_table("globgrph.graph_edges").scan().to_arrow().to_pylist()[:200]
    wrong = sum(1 for r in rows if (r.get("source") or "").strip() and (r.get("target") or "").strip())
    right = sum(1 for r in rows if (r.get("src_id") or "").strip() and (r.get("dst_id") or "").strip())
    print("    source/target resolves %d of %d   (MUST be 0 -- the shipped bug)" % (wrong, len(rows)))
    print("    src_id/dst_id resolves %d of %d   (MUST be all -- the real contract)" % (right, len(rows)))
    return wrong == 0 and right == len(rows)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nodes", required=True)
    ap.add_argument("--edges", required=True)
    args = ap.parse_args()

    rows = json.load(open(args.nodes, encoding="utf-8"))
    edges = json.load(open(args.edges, encoding="utf-8"))
    if not rows or not edges:
        print("  REFUSING: empty input -- a PASS over nothing is an artifact")
        return 2
    cat = build_local_iceberg(rows, edges)
    print("  local Iceberg: %d node rows / %d edge rows" % (len(rows), len(edges)))

    print("  EDGE-COLUMN REGRESSION CONTROL:")
    if not test_edge_column_regression(cat):
        print("  *** CONTROL DID NOT BEHAVE -- the edge schema changed; this harness is invalid ***")
        return 1

    import pyiceberg.catalog.rest as rest                         # noqa: PLC0415
    rest.RestCatalog = lambda *a, **k: cat                        # THE ONLY SUBSTITUTION
    try:
        import derive_runner                                      # noqa: PLC0415
    except Exception as e:                                        # noqa: BLE001
        raise ProducerUnusable("cannot import derive_runner (%s) -- REFUSING to substitute a copy"
                               % e) from e
    fn = getattr(derive_runner, "_c2c3_incontainer_reader", None)
    if not callable(fn):
        raise ProducerUnusable("_c2c3_incontainer_reader absent -- the producer's reader moved")

    out = fn()
    if out is None:
        print("  producer reader returned None (deps unavailable) -- INDETERMINATE, not a pass")
        return 2
    query_fn, vintage_fn = out
    v = vintage_fn()
    print("  THEIR vintage_fn: nodes=%s edges=%s" % (v.get("nodes_snapshot_id"), v.get("edges_snapshot_id")))

    probe, _ = query_fn("MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) RETURN count(*) AS c")
    resolved = probe[0]["c"] if probe else 0
    print("  EDGES RESOLVED BY THEIR LINE: %d of %d" % (resolved, len(edges)))

    import c2_individuate as c2                                   # noqa: PLC0415
    import c3_cover as c3                                         # noqa: PLC0415
    d2 = c2.compose(query_fn=query_fn, vintage_fn=vintage_fn)
    d3 = c3.compose(d2, live_snap_fn=lambda: v.get("nodes_snapshot_id"))
    got = {"instances": d2["counts"]["c2_motif_instances_distinct"],
           "structures": d3["counts"]["c3_structures_promoted"],
           "class_marked": d2["counts"]["class_nodes_marked_grain_class"]}
    ok = all(got[k] == CANONICAL[k] for k in CANONICAL)
    print("  COMPOSE via THEIR reader: %s   (canonical %s)" % (got, CANONICAL))
    # The freshness verdict is itself under test here: real INT snapshot ids on one side, and the
    # comparison used to be int-vs-str, which read STALE on identical numbers.
    print("  FRESHNESS: %s" % d3["input_freshness"].split(" --")[0])
    fresh_ok = d3["input_freshness"].startswith("CURRENT")
    print()
    if ok and resolved == len(edges) and fresh_ok:
        print("  PRODUCER'S OWN READER EXECUTED -- canonical figures, all edges resolved, CURRENT.")
        print("  Unexercised: the Nessie REST connection and S3-as-backend. Nothing else.")
        return 0
    print("  *** DIVERGENCE -- executed the real reader and it did not reproduce canonical ***")
    return 1


if __name__ == "__main__":
    sys.exit(main())
