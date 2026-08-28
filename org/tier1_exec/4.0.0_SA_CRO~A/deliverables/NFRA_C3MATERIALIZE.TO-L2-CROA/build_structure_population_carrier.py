#!/usr/bin/env python3
"""Emit the exact B4 STRUCTURE population as one digest-addressable object.

The historical L2 artifact serialized the edge-incident node records but only
reported the directed-edge count.  B4 needs both node IDs and edge rows to run
the held degree-corrected SBM oracle.  This producer deliberately reuses the
same Kuzu queries and canonical input digest as ``build_views.py`` and refuses
to write output if the device-local topology no longer matches that input.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

from build_views import KUZU_DB, canonical_digest, kuzu_rows


HERE = Path(__file__).resolve().parent
L2_ARTIFACT = HERE / "L2_VIEW_ARTIFACTS.json"
DEFAULT_OUTPUT = HERE / "STRUCTURE_POPULATION_CARRIER.json"

EXPECTED_ANCHOR = "bb01a202721f9c3a719a3a662319cebc194a1720"
EXPECTED_INPUT_DIGEST = "a323f598e82eed9a694e808c5a14877727c699a3c8aa3ce9daac64f09dc361e4"
EXPECTED_NODE_COUNT = 19_482
EXPECTED_EDGE_COUNT = 36_549
EXPECTED_UNIQUE_PROJECTED_EDGE_COUNT = 36_548
EXPECTED_DUPLICATE_PROJECTED_ROW_COUNT = 1
L2_ARTIFACT_COMMIT = "f42970fdefdc40013497a72f7bd46e992baad934"

NODE_QUERY = (
    "MATCH (n:CloudNode) WHERE n.layer <> 'semctl' "
    "RETURN n.node_id,n.node_type,n.layer ORDER BY n.node_id"
)
EDGE_QUERY = (
    "MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) "
    "WHERE a.layer <> 'semctl' AND b.layer <> 'semctl' "
    "RETURN a.node_id,b.node_id,e.edge_type "
    "ORDER BY a.node_id,b.node_id,e.edge_type"
)


def canonical_bytes(value: object) -> bytes:
    """Return the exact carrier serialization: canonical UTF-8 JSON plus LF."""
    return (
        json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n"
    ).encode("utf-8")


def structure_entity_ids() -> list[str]:
    artifact = json.loads(L2_ARTIFACT.read_text(encoding="utf-8"))
    structure = next(view for view in artifact["views"] if view["view_id"] == "STRUCTURE")
    if artifact["git_anchor"] != EXPECTED_ANCHOR:
        raise RuntimeError(
            f"L2 anchor mismatch: {artifact['git_anchor']} != {EXPECTED_ANCHOR}"
        )
    ids = [str(entity["entity_id"]) for entity in structure["entity_set"]["entities"]]
    if len(ids) != EXPECTED_NODE_COUNT or structure["entity_set"]["denominator"] != len(ids):
        raise RuntimeError(
            "L2 STRUCTURE denominator mismatch: "
            f"denominator={structure['entity_set']['denominator']} ids={len(ids)}"
        )
    return ids


def build_carrier() -> tuple[dict, str]:
    import kuzu

    database = kuzu.Database(str(KUZU_DB), read_only=True)
    connection = kuzu.Connection(database)
    nodes = kuzu_rows(connection, NODE_QUERY)
    edges = kuzu_rows(connection, EDGE_QUERY)

    source_digest = canonical_digest({"nodes": nodes, "edges": edges})
    if source_digest != EXPECTED_INPUT_DIGEST:
        raise RuntimeError(
            "REFUSED: device-local topology no longer matches the held L2 source input: "
            f"{source_digest} != {EXPECTED_INPUT_DIGEST}"
        )
    if len(edges) != EXPECTED_EDGE_COUNT:
        raise RuntimeError(
            f"REFUSED: directed-edge count {len(edges)} != {EXPECTED_EDGE_COUNT}"
        )

    degree: Counter[str] = Counter()
    normalized_edges: list[list[str]] = []
    for source, target, edge_type in edges:
        source_id = str(source)
        target_id = str(target)
        normalized_edges.append([source_id, target_id, str(edge_type)])
        degree[source_id] += 1
        degree[target_id] += 1

    projected_edge_counts = Counter(tuple(edge) for edge in normalized_edges)
    duplicate_projected_tuples = [
        list(edge) for edge, count in sorted(projected_edge_counts.items()) if count > 1
    ]
    duplicate_projected_rows = sum(count - 1 for count in projected_edge_counts.values() if count > 1)
    if len(projected_edge_counts) != EXPECTED_UNIQUE_PROJECTED_EDGE_COUNT:
        raise RuntimeError(
            "REFUSED: unique projected edge count "
            f"{len(projected_edge_counts)} != {EXPECTED_UNIQUE_PROJECTED_EDGE_COUNT}"
        )
    if duplicate_projected_rows != EXPECTED_DUPLICATE_PROJECTED_ROW_COUNT:
        raise RuntimeError(
            "REFUSED: duplicate projected edge row count "
            f"{duplicate_projected_rows} != {EXPECTED_DUPLICATE_PROJECTED_ROW_COUNT}"
        )

    carrier_node_ids = [str(node_id) for node_id, _, _ in nodes if degree[str(node_id)] > 0]
    artifact_node_ids = structure_entity_ids()
    if carrier_node_ids != artifact_node_ids:
        raise RuntimeError(
            "REFUSED: reconstructed edge-incident IDs differ from L2 STRUCTURE entity order"
        )
    if len(carrier_node_ids) != EXPECTED_NODE_COUNT:
        raise RuntimeError(
            f"REFUSED: edge-incident node count {len(carrier_node_ids)} != {EXPECTED_NODE_COUNT}"
        )
    if len(set(carrier_node_ids)) != len(carrier_node_ids):
        raise RuntimeError("REFUSED: duplicate node ID in carrier population")

    population = set(carrier_node_ids)
    outside = [edge for edge in normalized_edges if edge[0] not in population or edge[1] not in population]
    if outside:
        raise RuntimeError(f"REFUSED: {len(outside)} edge rows reference nodes outside the population")

    carrier = {
        "schema": "nfra-c3materialize.structure-population-carrier/1.0",
        "git_anchor": EXPECTED_ANCHOR,
        "population": {
            "definition": (
                "Every edge-incident CloudNode in the pinned device-local Kuzu topology "
                "whose layer is not semctl, with every directed non-semctl CloudEdge row."
            ),
            "node_ids": carrier_node_ids,
            "directed_edges": normalized_edges,
        },
        "counts": {
            "edge_incident_non_semctl_nodes": len(carrier_node_ids),
            "directed_non_semctl_edge_rows": len(normalized_edges),
            "unique_projected_source_target_type_tuples": len(projected_edge_counts),
            "duplicate_projected_tuple_count": len(duplicate_projected_tuples),
            "duplicate_projected_row_count": duplicate_projected_rows,
        },
        "source": {
            "kuzu_database": "infra/aws/globgrph/kuzu_nessie_db",
            "node_query": NODE_QUERY,
            "edge_query": EDGE_QUERY,
            "l2_view_artifact": (
                "org/tier1_exec/4.0.0_SA_CRO~A/deliverables/"
                "NFRA_C3MATERIALIZE.TO-L2-CROA/L2_VIEW_ARTIFACTS.json"
            ),
            "l2_view_artifact_commit": L2_ARTIFACT_COMMIT,
            "held_computation_input_digest": source_digest,
            "held_computation_input_digest_definition": (
                "sha256 of UTF-8 canonical JSON for {nodes: full ordered non-semctl node rows, "
                "edges: full ordered directed non-semctl edge rows}; this validates source "
                "equivalence and is not the carrier object's byte digest"
            ),
            "multiedge_evidence": (
                "org/tier1_exec/4.0.0_SA_CRO~A/deliverables/"
                "NFRA_C3MATERIALIZE.TO-L2-CROA/"
                "STRUCTURE_POPULATION_MULTIEDGE_EVIDENCE.json"
            ),
            "duplicate_projected_tuples": duplicate_projected_tuples,
        },
        "normalization": {
            "encoding": "UTF-8",
            "line_endings": "LF",
            "serialization": (
                "json.dumps(value, sort_keys=True, separators=(',', ':'), "
                "ensure_ascii=False) followed by one LF byte"
            ),
            "node_order": "ascending node_id from the held Kuzu query",
            "edge_order": "ascending source_id, target_id, edge_type from the held Kuzu query",
            "directed_edge_tuple_fields": ["source_id", "target_id", "edge_type"],
            "directed": True,
            "edge_multiplicity": (
                "One carrier row equals one source CloudEdge row. Exact projected tuple "
                "duplicates are intentional parallel directed edges when source identities "
                "differ by properties."
            ),
        },
        "consumer_contract": {
            "one_object": True,
            "rebuild_kuzu_in_container": False,
            "digest_rule": "SHA-256 over the complete object bytes exactly as serialized above",
            "refuse_on_digest_mismatch": True,
            "directed_multigraph": True,
            "preserve_edge_row_multiplicity": True,
            "set_conversion_or_deduplication_forbidden": True,
            "simple_graph_collapse_forbidden": True,
        },
    }
    return carrier, source_digest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    carrier, source_digest = build_carrier()
    payload = canonical_bytes(carrier)
    args.output.write_bytes(payload)
    object_digest = hashlib.sha256(payload).hexdigest()

    round_trip = canonical_bytes(json.loads(args.output.read_text(encoding="utf-8")))
    if round_trip != payload:
        raise RuntimeError("REFUSED: written carrier does not round-trip to identical canonical bytes")

    print(f"OK: wrote {args.output.relative_to(HERE.parents[4])}")
    print(f"git_anchor={EXPECTED_ANCHOR}")
    print(f"source_input_digest={source_digest}")
    print(f"nodes={len(carrier['population']['node_ids'])}")
    print(f"directed_edges={len(carrier['population']['directed_edges'])}")
    print(
        "unique_projected_edge_tuples="
        f"{carrier['counts']['unique_projected_source_target_type_tuples']}"
    )
    print(
        "duplicate_projected_tuple_count="
        f"{carrier['counts']['duplicate_projected_tuple_count']}"
    )
    print(
        "duplicate_projected_row_count="
        f"{carrier['counts']['duplicate_projected_row_count']}"
    )
    print(f"bytes={len(payload)}")
    print(f"object_sha256={object_digest}")
    print("normalization=UTF-8 canonical JSON + one LF")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
