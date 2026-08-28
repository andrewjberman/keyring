#!/usr/bin/env python3
"""Verify the exact B4 STRUCTURE carrier before any graph inference runs."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_CARRIER = HERE / "STRUCTURE_POPULATION_CARRIER.json"
EXPECTED_SCHEMA = "nfra-c3materialize.structure-population-carrier/1.0"
EXPECTED_ANCHOR = "bb01a202721f9c3a719a3a662319cebc194a1720"
EXPECTED_SOURCE_DIGEST = "a323f598e82eed9a694e808c5a14877727c699a3c8aa3ce9daac64f09dc361e4"
EXPECTED_NODE_COUNT = 19_482
EXPECTED_EDGE_COUNT = 36_549
EXPECTED_UNIQUE_PROJECTED_EDGE_COUNT = 36_548
EXPECTED_DUPLICATE_PROJECTED_TUPLE_COUNT = 1
EXPECTED_DUPLICATE_PROJECTED_ROW_COUNT = 1


def canonical_bytes(value: object) -> bytes:
    return (
        json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n"
    ).encode("utf-8")


def refuse(reason: str) -> int:
    print(f"REFUSED: {reason}")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--carrier", type=Path, default=DEFAULT_CARRIER)
    parser.add_argument("--expected-sha256", required=True)
    args = parser.parse_args()

    payload = args.carrier.read_bytes()
    actual_sha256 = hashlib.sha256(payload).hexdigest()
    if actual_sha256 != args.expected_sha256.lower():
        return refuse(
            f"object SHA-256 mismatch: {actual_sha256} != {args.expected_sha256.lower()}"
        )

    try:
        carrier = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        return refuse(f"carrier is not valid UTF-8 JSON: {exc}")
    if canonical_bytes(carrier) != payload:
        return refuse("carrier bytes are not canonical UTF-8 JSON plus one LF")
    if carrier.get("schema") != EXPECTED_SCHEMA:
        return refuse(f"schema mismatch: {carrier.get('schema')!r}")
    if carrier.get("git_anchor") != EXPECTED_ANCHOR:
        return refuse(f"anchor mismatch: {carrier.get('git_anchor')!r}")
    if carrier.get("source", {}).get("held_computation_input_digest") != EXPECTED_SOURCE_DIGEST:
        return refuse("held source input digest mismatch")

    population = carrier.get("population", {})
    node_ids = population.get("node_ids")
    edges = population.get("directed_edges")
    if not isinstance(node_ids, list) or not isinstance(edges, list):
        return refuse("population node_ids/directed_edges arrays are missing")
    if len(node_ids) != EXPECTED_NODE_COUNT:
        return refuse(f"node count {len(node_ids)} != {EXPECTED_NODE_COUNT}")
    if len(edges) != EXPECTED_EDGE_COUNT:
        return refuse(f"edge count {len(edges)} != {EXPECTED_EDGE_COUNT}")
    if len(set(node_ids)) != len(node_ids):
        return refuse("duplicate node ID")
    if node_ids != sorted(node_ids):
        return refuse("node IDs are not in ascending order")
    if edges != sorted(edges, key=lambda edge: (edge[0], edge[1], edge[2])):
        return refuse("directed edges are not in ascending source/target/type order")
    if any(not isinstance(edge, list) or len(edge) != 3 for edge in edges):
        return refuse("directed edge tuple shape is not [source_id,target_id,edge_type]")
    population_ids = set(node_ids)
    outside = [edge for edge in edges if edge[0] not in population_ids or edge[1] not in population_ids]
    if outside:
        return refuse(f"{len(outside)} edges reference a node outside the population")

    counts = carrier.get("counts", {})
    if counts.get("edge_incident_non_semctl_nodes") != len(node_ids):
        return refuse("declared node count differs from object-read count")
    if counts.get("directed_non_semctl_edge_rows") != len(edges):
        return refuse("declared edge count differs from object-read count")
    projected_counts: dict[tuple[str, str, str], int] = {}
    for edge in edges:
        key = tuple(edge)
        projected_counts[key] = projected_counts.get(key, 0) + 1
    duplicate_tuple_count = sum(count > 1 for count in projected_counts.values())
    duplicate_row_count = sum(count - 1 for count in projected_counts.values() if count > 1)
    if len(projected_counts) != EXPECTED_UNIQUE_PROJECTED_EDGE_COUNT:
        return refuse("unique projected edge count mismatch")
    if duplicate_tuple_count != EXPECTED_DUPLICATE_PROJECTED_TUPLE_COUNT:
        return refuse("duplicate projected tuple count mismatch")
    if duplicate_row_count != EXPECTED_DUPLICATE_PROJECTED_ROW_COUNT:
        return refuse("duplicate projected row count mismatch")
    if counts.get("unique_projected_source_target_type_tuples") != len(projected_counts):
        return refuse("declared unique projected tuple count differs from object-read count")
    if counts.get("duplicate_projected_tuple_count") != duplicate_tuple_count:
        return refuse("declared duplicate tuple count differs from object-read count")
    if counts.get("duplicate_projected_row_count") != duplicate_row_count:
        return refuse("declared duplicate row count differs from object-read count")
    contract = carrier.get("consumer_contract", {})
    if contract.get("one_object") is not True:
        return refuse("one-object contract is not true")
    if contract.get("rebuild_kuzu_in_container") is not False:
        return refuse("in-container Kuzu rebuild is not forbidden")
    if contract.get("refuse_on_digest_mismatch") is not True:
        return refuse("digest-mismatch refusal contract is not true")
    if contract.get("directed_multigraph") is not True:
        return refuse("directed-multigraph contract is not true")
    if contract.get("preserve_edge_row_multiplicity") is not True:
        return refuse("edge-row multiplicity preservation contract is not true")
    if contract.get("set_conversion_or_deduplication_forbidden") is not True:
        return refuse("set-conversion/deduplication prohibition is not true")
    if contract.get("simple_graph_collapse_forbidden") is not True:
        return refuse("simple-graph-collapse prohibition is not true")

    print("PASS: STRUCTURE population carrier verified")
    print(f"object_sha256={actual_sha256}")
    print(f"bytes={len(payload)}")
    print(f"git_anchor={carrier['git_anchor']}")
    print(f"source_input_digest={EXPECTED_SOURCE_DIGEST}")
    print(f"nodes={len(node_ids)}")
    print(f"directed_edges={len(edges)}")
    print(f"unique_projected_edge_tuples={len(projected_counts)}")
    print(f"duplicate_projected_tuple_count={duplicate_tuple_count}")
    print(f"duplicate_projected_row_count={duplicate_row_count}")
    print("normalization=UTF-8 canonical JSON + one LF")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
