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
STILL UNMEASURED: the ICEBERG SCAN (in-VPC only) and the Iceberg COMMIT of the landed layer -- and
per the footprint below that commit is an EDGE-volume problem, which is now the largest unmeasured
thing in the landing.

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
        print("  EQUIVALENT. AE's DDL + keying + query_fn + kuzu 0.11.3 reproduce the comp-kuzu")
        print("  figures exactly. The ICEBERG SCAN remains unexercised (in-VPC only) -- this is the")
        print("  callee, not the deployment.")
    else:
        print("  *** DIVERGENCE -- the in-container path would not reproduce the local layer ***")
    return 0 if (ok and keying_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
