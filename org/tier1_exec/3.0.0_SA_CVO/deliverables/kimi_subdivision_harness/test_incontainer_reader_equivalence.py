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

>> UPDATE 2026-08-07 -- THE ICEBERG SCAN *IS* NOW EXERCISED, and it was never VPC-blocked. <<
Everything after `catalog = RestCatalog(...)` in derive_runner:1424-1460 is CATALOG-AGNOSTIC:
load_table, current_snapshot(), scan().to_arrow(), the keying loop, the Kuzu build. Only the
CONNECTION is Nessie-specific. Wrote the real estate (20,604 nodes / 41,160 edges, RAW node_id +
separate arn, real 9-field/6-field schemas) into a local pyiceberg SqlCatalog and ran a TRANSCRIPTION
of AE's reader body against it.
>> I ORIGINALLY WROTE "VERBATIM" HERE AND THAT WAS FALSE. It was a transcription, and the
transcription SILENTLY CORRECTED the one line that was broken in their shipped code -- it read
`source`/`target` while Iceberg holds `src_id`/`dst_id`, which resolves ZERO edges against a real
table. Anyone writing this fixture reaches for the schema first and then writes the reader to match
it, so the copy cannot fail in the way the original did. A GREEN RUN OF A TRANSCRIPTION IS EVIDENCE
ABOUT THE TRANSCRIBER, NOT THE PRODUCER. Their bug was found by them @824cf6b6b2; this run did not
and could not have. SUPERSEDED by a real execution: importing derive_runner (with org/modules/graph
on sys.path for comp_aws_cli) and calling THEIR `_c2c3_incontainer_reader()` with only `RestCatalog`
substituted -- 41,160 edges resolved by THEIR line, C2 6138 / C3 1255 / class 23. <<
The transcribed run's figures, retained because its OTHER findings stand:
    SCAN       load_table + current_snapshot + scan().to_arrow()   0.03s
    KEY+BUILD  20,604 unique keys / 41,160 edges                   0.65s
    COMPOSE    C2 6138  C3 1255  class 23                          0.30s
    END-TO-END Iceberg -> Kuzu -> composition                      0.99s
    vintage stamped from REAL Iceberg snapshot ids (7891676592218021200 / 9020091458538502682)
    MATCHES CANONICAL 6138 / 1255 / 23
That independently confirms AE's ~1.0s end-to-end figure, and it exercises the vintage_fn path with
ACTUAL snapshot ids rather than injected strings.

WHAT THIS DOES *NOT* PROVE -- stated so nobody reads it as full coverage of item 5:
  * the NESSIE REST CONNECTION and S3-as-storage-backend are still unexercised -- genuinely in-VPC.
    That is now the ONLY unexercised piece of the reader, down from "the whole scan".
  * `--build the image and run it` is not done here. This is the callee, not the deployment.
  * the rows fed in are already key-normalised (the local DB's node_id IS the key), so the main
    equivalence run does not exercise the raw-Iceberg -> key derivation. `test_keying()` below
    covers that dimension separately, on raw-shaped rows, WITH a negative control.

COST, MEASURED 2026-08-07 (0.7.0_AE_CloudOps had this as "unmeasured"; these are the composition
half only, and the split matters more than either number):
    composition via the local comp-kuzu SHELL path : 52.8s   (C2 50.2 + C3 2.6, 16 subprocess spawns)
    composition via an EMBEDDED kuzu connection    :  0.2s   (C2 0.2 + C3 0.0), identical figures
>> 250x. THE COMPOSITION IS ESSENTIALLY FREE; the 52.8s was ENTIRELY subprocess overhead, which the
in-container path does not pay. Anyone sizing the derive off the local wall-clock would budget ~53s
for something that costs 0.2s. <<
THE DB BUILD WAS THE OTHER 143s, AND IT IS NOW 0.6s. My split decomposed AE's 158s and left the
obvious question: if the composition is 0.2s, what was the other 157? Their build was row-by-row
(one execute per node and per edge, 61,764 times). Fixed to bulk COPY @191b8461eb:
    row-by-row   nodes 40.8s + edges 102.5s = 143.3s
    bulk COPY    nodes  0.5s + edges   0.1s =   0.6s      225x
Independently reproduced here on the same graph: nodes 0.5s + edges 0.1s, and the composition
figures are IDENTICAL through the bulk path (6138/6657/1255/8978) -- a speedup that changes the
answer is not a speedup. End-to-end is now ~1.0s.
BOTH large numbers in this path were artifacts of HOW, not costs of WHAT.
THE ICEBERG COMMIT IS NOT AN EDGE-VOLUME PROBLEM -- I SAID IT WAS, AND I WAS WRONG. Measured
2026-08-07 against a LOCAL pyiceberg SqlCatalog with the real 9-field/6-field derive_runner schemas:
    nodes append ( 7,416 rows) : 0.15s
    edges append (26,956 rows) : 0.03s
    TOTAL                      : 0.18s
    on-disk parquet + metadata : 0.5 MB   (the envelope JSON is ~9.8 MB -- parquet is ~20x smaller)
    READBACK CONTROL           : 7,416 and 26,956 rows scanned back -- a fast write that lost rows
                                 is not a fast write.
I had published "edges dominate at 3.6x, so the commit is an edge-volume problem" to two seats. That
was an INFERENCE FROM A ROW COUNT, and the measurement falsifies it: 26,956 edges are trivial to
serialize. Whatever the in-VPC commit costs is S3/Nessie NETWORK AND CATALOG latency, which at this
scale is roughly independent of these row counts.

WHAT THIS LOCAL MEASUREMENT DOES NOT COVER: the S3 PUT leg and the Nessie REST commit round-trip. It
measures serialization and write, not network. The SCAN remains in-VPC-only and unmeasured.

FOOTPRINT the landed layer adds to the graph:
    C2  6,161 nodes + 17,978 edges | C3  1,255 nodes + 8,978 edges
    TOTAL 7,416 nodes + 26,956 edges (~9.8 MB of envelope JSON)
    20,604 nodes today -> 28,020 after landing = +36.0% node count; edges dominate at 3.6x nodes.

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
import re
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


# Anchored to the REPO, not the CWD. This was os.path.join("infra", ...) -- CWD-relative -- so
# running the harness from its own directory refused with "cannot read the producer", which reads as
# THE PRODUCER IS MISSING when the truth was THE HARNESS IS STANDING IN THE WRONG PLACE. Found by
# 0.7.0_AE_CloudOps. A refusal is only useful if it names its ACTUAL cause; misattributing sends the
# reader at the wrong system, and this one would have sent them at derive_runner.
_REPO = os.path.abspath(os.path.join(HERE, *([os.pardir] * 5)))
DERIVE_RUNNER = os.path.join(_REPO, "infra", "aws", "globgrph", "derive_runner.py")


class ProducerSourceUnreadable(Exception):
    """The DDL could not be EXTRACTED from derive_runner -- so this harness REFUSES to run.

    It does NOT fall back to a transcription. A transcription is what caused the defect this
    extraction exists to remove, and a fallback would restore it silently at exactly the moment
    the extraction stopped working.
    """


def extracted_ddl(src_path=None):
    """Pull the CloudNode/CloudEdge DDL OUT OF derive_runner AT RUNTIME.

    >> WHY EXTRACT RATHER THAN TRANSCRIBE (0.7.0_AE_CloudOps, 2026-08-07): this harness previously
    embedded a character-perfect COPY of the producer's build. It was correct when written, AE
    changed the build to bulk COPY @191b8461eb, and the copy KEPT PASSING -- verifying a code path
    that no longer existed anywhere. A drifted transcription does not fail; it succeeds about the
    wrong thing, which is strictly worse than failing. Extraction makes drift IMPOSSIBLE instead of
    merely detectable: if the producer's DDL changes, this test changes with it or refuses. <<
    """
    path = src_path or DERIVE_RUNNER
    try:
        src = open(path, encoding="utf-8").read()
    except OSError as e:
        raise ProducerSourceUnreadable(
            "cannot read the producer at %s (%s). If that path looks wrong, the HARNESS is "
            "mislocated, not the producer -- DERIVE_RUNNER is anchored to the repo via HERE, not "
            "to the CWD." % (path, e)) from e
    out = []
    for table in ("CREATE NODE TABLE CloudNode", "CREATE REL TABLE CloudEdge"):
        # the statement is a multi-line implicitly-concatenated literal inside conn.execute(...)
        i = src.find(table)
        if i < 0:
            raise ProducerSourceUnreadable(
                "%r not found in %s -- the producer's DDL moved or was renamed; REFUSING to fall "
                "back to a transcription" % (table, path))
        j = src.find(")\n", i)
        chunk = src[i - 20:j]
        lits = re.findall(r'"([^"]*)"', chunk)
        stmt = "".join(lits)
        if table.split()[-1] not in stmt:
            raise ProducerSourceUnreadable("extracted a fragment for %r, not a statement" % table)
        out.append(stmt)
    return out


def build_db(nodes, edges):
    import kuzu                                              # noqa: PLC0415 - optional dep
    db_dir = os.path.join(tempfile.mkdtemp(prefix="c2c3_ae_ddl_"), "db")
    conn = kuzu.Connection(kuzu.Database(db_dir))
    for stmt in extracted_ddl():
        conn.execute(stmt)
    best = {}
    for r in nodes:
        k = key_of(r)
        if k:
            best[k] = r
    # BULK COPY, not row-by-row. This built one execute() per node and per edge -- 61,764 of them,
    # ~235s. 0.7.0_AE_CloudOps hit the same shape in the producer (143.3s -> 0.6s @191b8461eb) and
    # flagged it here; I owed it and had explicitly refused to claim it done until it was.
    # A 235s harness does not get re-run, and a test nobody re-runs stops being a control the moment
    # the thing it guards changes -- which is precisely how the transcription in this same file went
    # stale without anyone noticing.
    import pyarrow as pa                                       # noqa: PLC0415 - optional dep
    ks = list(best)
    g = lambda k, f: (best[k].get(f) or "")                    # noqa: E731
    ntab = pa.table({                                          # noqa: F841 - kuzu COPY reads the
        "node_id": ks, "arn": [g(k, "arn") for k in ks],       #   caller's frame; removing this
        "node_type": [g(k, "node_type") for k in ks],          #   assignment breaks the load while
        "name": [g(k, "name") for k in ks],                    #   the lint goes green
        "layer": [g(k, "layer") for k in ks],
        "drift_class": [""] * len(ks), "source": [""] * len(ks),
        "snapshot_ts": pa.array([0] * len(ks), pa.int64()),
        "props": [g(k, "props") for k in ks]})
    conn.execute("COPY CloudNode FROM ntab")
    se = [(e["src"], e["dst"], e.get("edge_type") or "")
          for e in edges if e.get("src") in best and e.get("dst") in best]
    etab = pa.table({"src": [x[0] for x in se], "dst": [x[1] for x in se],   # noqa: F841 - as above
                     "edge_type": [x[2] for x in se], "layer": [""] * len(se),
                     "snapshot_ts": pa.array([0] * len(se), pa.int64()),
                     "props": [""] * len(se)})
    conn.execute("COPY CloudEdge FROM etab")
    return conn, len(best), len(se)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nodes", required=True)
    ap.add_argument("--edges", required=True)
    args = ap.parse_args()

    try:
        ddl = extracted_ddl()
    except ProducerSourceUnreadable as e:
        print("  REFUSING: %s" % e)
        return 2
    print("  DDL EXTRACTED FROM THE PRODUCER (not transcribed):")
    for stmt in ddl:
        print("    %s..." % stmt[:88])
    print()
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
        print("  EQUIVALENT. The producer's DDL + keying + query_fn + kuzu 0.11.3 reproduce the")
        print("  comp-kuzu figures exactly.")
        # This line used to claim the Iceberg scan was unexercised. It no longer is -- and a stale
        # scope caveat is the same drift class this file's extraction fix exists to remove, so it
        # points at the harness that superseded it rather than overstating what THIS one covers.
        print("  SCOPE: this exercises the DDL/keying/Cypher chain. The Iceberg SCAN is covered by")
        print("  test_producer_reader_executed.py, which runs the producer's OWN reader. Only the")
        print("  Nessie REST connection and S3-as-backend remain unexercised anywhere.")
    else:
        print("  *** DIVERGENCE -- the in-container path would not reproduce the local layer ***")
    return 0 if (ok and keying_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
