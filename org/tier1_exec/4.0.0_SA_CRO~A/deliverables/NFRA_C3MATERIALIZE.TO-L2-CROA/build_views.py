#!/usr/bin/env python3
"""Build the NFRA_C3MATERIALIZE L2 STRUCTURE and BEHAVIOR view artifacts.

This producer deliberately does not fuse the two views.  STRUCTURE fails closed
when a graph-tool-class SBM implementation is unavailable; BEHAVIOR is a pinned,
deterministic file co-change view over Git history.
"""
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import math
import os
import subprocess
import argparse
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
KUZU_DB = ROOT / "infra" / "aws" / "globgrph" / "kuzu_nessie_db"
MACHINE_EXCLUSIONS = {
    "infra/system/06_current_state.md": "gate-regenerated",
    "infra/system/06_current_state.json": "gate-regenerated",
    "org/compiler-tools-log.md": "retired auto-append",
}
COMMIT_SIZE_CAP = 25
MIN_SHARED_COMMITS = 2
HEAT_HALF_LIFE_DAYS = 30.0
REQUESTED_STRUCTURE_RUNS = 25


def run_git(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, encoding="utf-8", errors="replace",
        capture_output=True,
    )
    if proc.returncode:
        raise RuntimeError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_digest(value: object) -> str:
    return sha256_bytes(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8"))


def kuzu_rows(conn, query: str) -> list[list[object]]:
    result = conn.execute(query)
    rows: list[list[object]] = []
    while result.has_next():
        rows.append(result.get_next())
    return rows


def structure_view(anchor: str) -> dict:
    import kuzu

    db = kuzu.Database(str(KUZU_DB), read_only=True)
    conn = kuzu.Connection(db)
    nodes = kuzu_rows(
        conn,
        "MATCH (n:CloudNode) WHERE n.layer <> 'semctl' "
        "RETURN n.node_id,n.node_type,n.layer ORDER BY n.node_id",
    )
    edges = kuzu_rows(
        conn,
        "MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) "
        "WHERE a.layer <> 'semctl' AND b.layer <> 'semctl' "
        "RETURN a.node_id,b.node_id,e.edge_type ORDER BY a.node_id,b.node_id,e.edge_type",
    )
    degree: Counter[str] = Counter()
    for source, target, _ in edges:
        degree[str(source)] += 1
        degree[str(target)] += 1

    graph_tool_present = importlib.util.find_spec("graph_tool") is not None
    scanned_node_records = [
        {
            "entity_id": str(node_id),
            "node_type": str(node_type),
            "layer": str(layer),
            "features": {
                "topology_signal": "MEASURED" if degree[str(node_id)] else "ABSENT",
                "consensus_affinity": "ABSENT",
            },
        }
        for node_id, node_type, layer in nodes
    ]
    node_records = [row for row in scanned_node_records if row["features"]["topology_signal"] == "MEASURED"]
    isolated = len(scanned_node_records) - len(node_records)
    seeds = [int(hashlib.sha256(f"{anchor}:STRUCTURE:{i}".encode()).hexdigest()[:16], 16) for i in range(REQUESTED_STRUCTURE_RUNS)]

    return {
        "view_id": "STRUCTURE",
        "signal": "who connects to whom",
        "delivery_status": "DELIVERED-BLOCKED",
        "entity_set": {
            "definition": "Every edge-incident CloudNode in the current device-local Kuzu graph whose layer is not semctl; semctl is excluded to prevent inference from prior C2/C3 output, and isolated nodes carry no topology signal so are outside this view's entity set.",
            "denominator": len(node_records),
            "entities": node_records,
        },
        "coverage": {
            "topology_signal": {"measured": len(node_records), "absent": 0, "denominator": len(node_records)},
            "consensus_affinity": {"measured": 0, "absent": len(node_records), "denominator": len(node_records)},
            "directed_edge_rows": len(edges),
            "source_census": {"non_semctl_nodes_scanned": len(scanned_node_records), "isolated_without_topology_signal": isolated},
        },
        "matrix": {
            "status": "ABSENT-NOT-ZERO",
            "pairs": [],
            "default_for_unlisted_pair": "ABSENT",
            "reason": "No conforming graph-tool-class SBM inference implementation is installed or repository-local; a different community algorithm is not represented as SBM.",
        },
        "computation": {
            "requested": "degree-corrected SBM runs followed by pair co-assignment frequency over N runs",
            "executed": "Kuzu topology census only; inference refused before run 1",
            "input_digest": canonical_digest({"nodes": nodes, "edges": edges}),
            "input_rows": {"nodes_scanned": len(nodes), "edge_incident_entities": len(node_records), "directed_edges": len(edges)},
            "installed": {"graph_tool": graph_tool_present, "numpy": bool(importlib.util.find_spec("numpy")), "scipy": bool(importlib.util.find_spec("scipy")), "networkx": bool(importlib.util.find_spec("networkx"))},
            "historical_run_status": "HISTORICAL-UNREPRODUCIBLE: its producer, output, and 19,482/36,513 input are absent; not reused as current evidence",
        },
        "reproducibility": {
            "N_requested": REQUESTED_STRUCTURE_RUNS,
            "N_executed": 0,
            "seed_policy": "seed_i = first 64 bits of sha256(<git_anchor>:STRUCTURE:<zero-based-run-index>)",
            "seeds_requested": seeds,
            "per_run_record": "Would record seed, partition assignment, objective, iteration count, convergence state, and input digest; no run record exists because the dependency gate failed before run 1.",
            "consensus_definition": "W_STRUCTURE(i,j) = runs placing i and j in the same block / N; this consensus, not a selected partition, is the intended view.",
        },
        "discrimination_gate": {
            "status": "FAIL",
            "could_have_differed": True,
            "observed": "No measured affinities; zero bits admitted to downstream fusion.",
            "rule": "PASS only if N runs complete and the consensus matrix contains at least two affinity values with neither all-pair 0 nor all-pair 1.",
        },
        "failure_mode": {
            "mode": "Missing conforming inference engine/producer prevents the view from being measured.",
            "distinguishable_from_genuine_low_affinity": True,
            "distinction": "Dependency absence emits ABSENT-NOT-ZERO and zero measured pairs; genuine low affinity requires a completed run record and measured numeric affinities near zero.",
        },
        "named_hazard_answer": "graph_tool is absent. NumPy/SciPy/NetworkX presence is not treated as proof of an equivalent SBM. The gap is BLOCKING for STRUCTURE affinity and is carried as a failed delivered view.",
    }


def parse_git_history(anchor: str) -> tuple[list[dict], int]:
    raw = run_git(
        "log", "--no-merges", anchor,
        "--pretty=format:%x1e%H%x1f%cI", "--name-only",
    )
    commits: list[dict] = []
    for chunk in raw.split("\x1e"):
        if not chunk.strip():
            continue
        lines = chunk.splitlines()
        meta = lines[0].split("\x1f")
        if len(meta) != 2:
            continue
        paths = sorted({p.strip().replace("\\", "/") for p in lines[1:] if p.strip()})
        commits.append({"sha": meta[0], "iso": meta[1], "paths": paths})
    return commits, len(commits)


def behavior_view(anchor: str, anchor_iso: str) -> dict:
    commits, parsed_total = parse_git_history(anchor)
    accepted: list[dict] = []
    oversized = 0
    empty = 0
    exclusion_hits: Counter[str] = Counter()
    for commit in commits:
        filtered = []
        for path in commit["paths"]:
            if path in MACHINE_EXCLUSIONS:
                exclusion_hits[path] += 1
            else:
                filtered.append(path)
        if not filtered:
            empty += 1
            continue
        if len(filtered) > COMMIT_SIZE_CAP:
            oversized += 1
            continue
        accepted.append({**commit, "paths": filtered})

    path_commits: Counter[str] = Counter()
    pair_commits: Counter[tuple[str, str]] = Counter()
    latest: dict[str, datetime] = {}
    for commit in accepted:
        when = datetime.fromisoformat(commit["iso"])
        for path in commit["paths"]:
            path_commits[path] += 1
            if path not in latest or when > latest[path]:
                latest[path] = when
        for pair in itertools.combinations(commit["paths"], 2):
            pair_commits[pair] += 1

    anchor_time = datetime.fromisoformat(anchor_iso)
    retained_pairs = {pair: n for pair, n in pair_commits.items() if n >= MIN_SHARED_COMMITS}
    retained_entities = {path for pair in retained_pairs for path in pair}
    entities = []
    for path in sorted(retained_entities):
        age_days = max(0.0, (anchor_time - latest[path]).total_seconds() / 86400.0)
        entities.append({
            "entity_id": path,
            "features": {
                "cochange_signal": "MEASURED",
                "git_recency_heat": "MEASURED",
                "propagation_drift": "ABSENT",
            },
            "commit_count": path_commits[path],
            "last_commit_iso": latest[path].isoformat(),
            "git_recency_heat": round(math.exp(-math.log(2.0) * age_days / HEAT_HALF_LIFE_DAYS), 8),
        })

    pairs = []
    for (left, right), shared in sorted(retained_pairs.items()):
        affinity = shared / math.sqrt(path_commits[left] * path_commits[right])
        pairs.append({"i": left, "j": right, "shared_commits": shared, "affinity": round(affinity, 8), "status": "MEASURED"})

    possible = len(entities) * (len(entities) - 1) // 2
    values = {p["affinity"] for p in pairs}
    density = len(pairs) / possible if possible else 0.0
    gate_pass = bool(parsed_total and accepted and pairs and len(values) >= 2 and 0.0 < density < 1.0)
    input_record = {
        "anchor": anchor,
        "accepted_commits": [{"sha": c["sha"], "iso": c["iso"], "paths": c["paths"]} for c in accepted],
        "commit_size_cap": COMMIT_SIZE_CAP,
        "minimum_shared_commits": MIN_SHARED_COMMITS,
        "machine_exclusions": MACHINE_EXCLUSIONS,
    }

    return {
        "view_id": "BEHAVIOR",
        "signal": "what changes together, with pinned Git-recency heat metadata",
        "delivery_status": "DELIVERED-MEASURED",
        "entity_set": {
            "definition": "Distinct repository-relative paths participating in at least one repeated co-change pair (>=2 shared accepted commits). Accepted commits are non-merges at or before the anchor, after declared machine exclusions, with 1..25 retained paths.",
            "denominator": len(entities),
            "entities": entities,
        },
        "coverage": {
            "cochange_signal": {"measured": len(entities), "absent": 0, "denominator": len(entities)},
            "git_recency_heat": {"measured": len(entities), "absent": 0, "denominator": len(entities)},
            "propagation_drift": {"measured": 0, "absent": len(entities), "denominator": len(entities)},
            "commit_frame": {"parsed_non_merge": parsed_total, "accepted": len(accepted), "oversized_excluded": oversized, "empty_after_exclusions": empty},
            "pair_frame": {"measured_nonzero": len(pairs), "measured_zero": possible - len(pairs), "possible": possible},
        },
        "matrix": {
            "status": "MEASURED-SPARSE",
            "pairs": pairs,
            "default_for_unlisted_pair": "MEASURED-ZERO (both entities were observed in the same pinned commit frame and shared no accepted commit)",
            "affinity_definition": "shared accepted commits / sqrt(accepted commits touching i * accepted commits touching j)",
        },
        "computation": {
            "git_anchor": anchor,
            "git_anchor_iso": anchor_iso,
            "input_digest": canonical_digest(input_record),
            "commit_size_cap": COMMIT_SIZE_CAP,
            "minimum_shared_commits": MIN_SHARED_COMMITS,
            "machine_exclusions": [{"path": p, "reason": r, "observations_dropped": exclusion_hits[p]} for p, r in MACHINE_EXCLUSIONS.items()],
            "heat": f"Path-resolving Git history; exp(-ln(2)*age_days/{HEAT_HALF_LIFE_DAYS}). comp-heat score is not called.",
            "drift": "Not used: comp-drift is a propagation-target orchestrator, not a file-pair feature at this entity grain. Explicit ABSENT is carried per entity.",
        },
        "reproducibility": {
            "N": 1,
            "seed_policy": "NONE: deterministic Git DAG walk, sorted paths, canonical JSON",
            "per_run_record": "git anchor, anchor timestamp, accepted commit SHAs/paths digest, cap, exclusions, path counts, and pair shared-commit counts",
        },
        "discrimination_gate": {
            "status": "PASS" if gate_pass else "FAIL",
            "could_have_differed": True,
            "observed": {"distinct_positive_affinities": len(values), "nonzero_pairs": len(pairs), "possible_pairs": possible, "density": density},
            "rule": "PASS iff acquisition is non-empty, at least two distinct positive affinities exist, and nonzero-pair density is strictly between 0 and 1.",
            "negative_control": "An all-1 constant-affinity mutant fails because it has one distinct value and density 1.",
        },
        "failure_mode": {
            "mode": "Git retrieval failure, vacuous eligible population, cap/exclusion domination, or a constant affinity matrix.",
            "distinguishable_from_genuine_low_affinity": True,
            "distinction": "Retrieval and vacuity are hard failures; ABSENT features are explicit; a genuine low-affinity pair is a MEASURED-ZERO inside a non-empty pinned frame.",
        },
        "named_hazard_answer": "comp-heat score is NOT USED because it does not resolve its id. Heat metadata is derived only after the file path is resolved by the pinned Git history. comp-drift is grain-incompatible and carried ABSENT, never zero.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--anchor", default="HEAD", help="Git commit that pins the behavior view")
    args = parser.parse_args()
    anchor = run_git("rev-parse", args.anchor).strip()
    anchor_iso = run_git("show", "-s", "--format=%cI", anchor).strip()
    artifact = {
        "schema": "nfra-c3materialize.l2.independent-views/1.0",
        "generated_at_anchor_time": anchor_iso,
        "git_anchor": anchor,
        "no_fusion": True,
        "cross_view_affinities": [],
        "views": [structure_view(anchor), behavior_view(anchor, anchor_iso)],
    }
    artifact["artifact_digest"] = canonical_digest(artifact)
    target = OUT / "L2_VIEW_ARTIFACTS.json"
    target.write_text(json.dumps(artifact, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"OK: wrote {target.relative_to(ROOT)}")
    for view in artifact["views"]:
        print(f"{view['view_id']}: {view['delivery_status']} entities={view['entity_set']['denominator']} gate={view['discrimination_gate']['status']}")
    print(f"artifact_digest={artifact['artifact_digest']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
