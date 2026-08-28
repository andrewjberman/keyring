#!/usr/bin/env python3
"""Measure projected duplicate-edge semantics in the held Kuzu topology."""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path

from build_views import KUZU_DB, kuzu_rows


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "STRUCTURE_POPULATION_MULTIEDGE_EVIDENCE.json"

QUERY = (
    "MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) "
    "WHERE a.layer <> 'semctl' AND b.layer <> 'semctl' "
    "RETURN a.node_id,b.node_id,e.edge_type,e.props,e.layer,e.snapshot_ts "
    "ORDER BY a.node_id,b.node_id,e.edge_type,e.props,e.layer,e.snapshot_ts"
)


def main() -> int:
    import kuzu

    database = kuzu.Database(str(KUZU_DB), read_only=True)
    connection = kuzu.Connection(database)
    rows = kuzu_rows(connection, QUERY)

    groups: dict[tuple[str, str, str], list[list[object]]] = defaultdict(list)
    for source, target, edge_type, props, layer, snapshot_ts in rows:
        key = (str(source), str(target), str(edge_type))
        groups[key].append([str(props or ""), str(layer or ""), int(snapshot_ts or 0)])

    duplicates = []
    for (source, target, edge_type), variants in sorted(groups.items()):
        if len(variants) <= 1:
            continue
        duplicates.append(
            {
                "projected_tuple": [source, target, edge_type],
                "row_count": len(variants),
                "distinct_full_identity_count": len({tuple(variant) for variant in variants}),
                "variants": [
                    {
                        "props": variant[0],
                        "props_sha256": hashlib.sha256(variant[0].encode("utf-8")).hexdigest(),
                        "layer": variant[1],
                        "snapshot_ts": variant[2],
                    }
                    for variant in variants
                ],
            }
        )

    evidence = {
        "schema": "nfra-c3materialize.structure-population-multiedge-evidence/1.0",
        "query": QUERY,
        "source_edge_rows": len(rows),
        "unique_projected_tuples": len(groups),
        "duplicate_projected_tuple_count": len(duplicates),
        "duplicate_projected_row_count": sum(item["row_count"] - 1 for item in duplicates),
        "duplicates": duplicates,
        "source_identity_rule": (
            "CloudEdge loader identity is source_id + target_id + edge_type + props; "
            "the B4 topology projection omits properties but preserves one graph edge per source row."
        ),
        "consumer_rule": (
            "Preserve row multiplicity as parallel directed edges. Never convert the edge rows "
            "to a set and never silently deduplicate projected tuples."
        ),
    }
    OUTPUT.write_text(json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

    print(f"source_edge_rows={len(rows)}")
    print(f"unique_projected_tuples={len(groups)}")
    print(f"duplicate_projected_tuple_count={len(duplicates)}")
    print(f"duplicate_projected_row_count={evidence['duplicate_projected_row_count']}")
    for item in duplicates:
        print(json.dumps(item, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
