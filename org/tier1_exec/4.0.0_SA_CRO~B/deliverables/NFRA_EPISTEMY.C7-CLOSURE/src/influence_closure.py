#!/usr/bin/env python3
"""NFRA_EPISTEMY Component 7 production-influence closure compiler.

Source of record (cited, not widened):
docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md sections 0, 2.1,
and Component 7 at INPUT_COMMIT. Observation_Record construction is delegated
to the landed C1 implementation; this module does not own its field set.
"""

from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import json
import subprocess
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

import yaml


COMPILER_ID = "nfra_epistemy.c7.influence_closure"
COMPILER_VERSION = "0.1.0-proposed"
INPUT_COMMIT = "b30b05d00675f0b3758d1ed8ccbedf0004b901f5"
PASS3_PATH = (
    "org/tier1_exec/4.0.0_SA_CRO~B/deliverables/"
    "ATOM_LAYER0_RESOLUTION_CENSUS_PASS3_CODE_GRAIN_20260820.yaml"
)
TRIGGER_COMPILER_PATH = "infra/aws/lambda/ci/trigger-census.py"
TRIGGER_MAP_PATH = "infra/aws/lambda/ci/trigger-map.json"
CENSUS_SUBSTRATE_PATH = "org/modules/graph/census_substrate.py"
ESTATE_DRIFT_PATH = "org/modules/graph/opal_estate_infrastructure.py"
C1_MODULE_PATH = (
    "org/tier1_exec/4.0.0_SA_CRO~A/deliverables/"
    "NFRA_EPISTEMY.C1-ENVELOPE/src/observation_envelope.py"
)
C1_SCHEMA_PATH = (
    "org/tier1_exec/4.0.0_SA_CRO~A/deliverables/"
    "NFRA_EPISTEMY.C1-ENVELOPE/schemas/observation_record.schema.json"
)
RULE24_PATH = (
    "org/tier1_exec/4.0.0_SA_CRO~B/deliverables/"
    "NFRA_EPISTEMY.C7-CLOSURE/rule24/C7_AXES_AND_PREDICATES_PRE_RECORD.json"
)

EXPECTED_BLOBS = {
    PASS3_PATH: "18d49c1611b3b75c27302a22017d36a90c171346",
    TRIGGER_COMPILER_PATH: "cc196e33c83432e31b2ab9e1b917cc42fc80c889",
    TRIGGER_MAP_PATH: "7c254d168a0fbaedc89dcda9d053769b07b39fdc",
    CENSUS_SUBSTRATE_PATH: "ea27e693716e449935e20ad682a383d87ae69f9b",
    ESTATE_DRIFT_PATH: "1f646d7c26d95dff3af19b5eee74e81385709ff7",
    C1_MODULE_PATH: "4aa72ab99cea52b8a1c46091aa08c73c9d73b859",
    C1_SCHEMA_PATH: "4673036e8d12a1a73d6e5c9abd214ee7d30b513e",
}

EDGE_KINDS = ("CODE_BINDING", "TRIGGER_TARGET", "INVENTORY_DESCRIPTOR")
CLOSURE_STATES = ("REACHED", "NOT_REACHED", "UNKNOWN", "FAILED")


def repo_root_from_script() -> Path:
    proc = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=Path(__file__).resolve().parent,
        capture_output=True,
        text=True,
        check=True,
    )
    return Path(proc.stdout.strip()).resolve()


def canonical_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
        + "\n"
    ).encode("ascii")


def sha256_id(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(value)).hexdigest()


def git_bytes(repo_root: Path, commit: str, path: str) -> bytes:
    return subprocess.check_output(
        ["git", "show", f"{commit}:{path}"], cwd=repo_root
    )


def git_blob(repo_root: Path, commit: str, path: str) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", f"{commit}:{path}"], cwd=repo_root, text=True
    ).strip()


def git_commit_time(repo_root: Path, commit: str) -> str:
    return subprocess.check_output(
        ["git", "show", "-s", "--format=%cI", commit], cwd=repo_root, text=True
    ).strip()


def verify_pinned_inputs(repo_root: Path) -> dict[str, str]:
    observed = {path: git_blob(repo_root, INPUT_COMMIT, path) for path in EXPECTED_BLOBS}
    mismatches = {
        path: {"expected": EXPECTED_BLOBS[path], "observed": blob}
        for path, blob in observed.items()
        if EXPECTED_BLOBS[path] != blob
    }
    if mismatches:
        raise RuntimeError(f"pinned input blob mismatch: {mismatches}")
    return observed


class _DescriptorNames(ast.NodeTransformer):
    def __init__(self, values: dict[str, Any]):
        self.values = values

    def visit_Name(self, node: ast.Name) -> ast.AST:
        if node.id in self.values:
            return ast.copy_location(ast.Constant(self.values[node.id]), node)
        return node


def parse_descriptors(source: str) -> dict[str, dict[str, Any]]:
    tree = ast.parse(source, filename=CENSUS_SUBSTRATE_PATH)
    constants: dict[str, Any] = {}
    descriptor_node: ast.AST | None = None
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        names = [target.id for target in node.targets if isinstance(target, ast.Name)]
        if len(names) == 1:
            try:
                constants[names[0]] = ast.literal_eval(node.value)
            except (ValueError, TypeError):
                pass
        if "DESCRIPTORS" in names:
            descriptor_node = copy.deepcopy(node.value)
    if descriptor_node is None:
        raise ValueError("DESCRIPTORS assignment not found")
    descriptor_node = _DescriptorNames(constants).visit(descriptor_node)
    ast.fix_missing_locations(descriptor_node)
    result = ast.literal_eval(descriptor_node)
    if not isinstance(result, dict) or not result:
        raise ValueError("DESCRIPTORS must be a non-empty mapping")
    return result


def make_seed(
    *,
    edge_kind: str,
    source_node: str,
    target_node: str | None,
    production_terminal: bool,
    source_ref: str,
    attributes: dict[str, Any],
    source_complete: bool = True,
    unknown_reason: str | None = None,
) -> dict[str, Any]:
    seed_identity = {
        "edge_kind": edge_kind,
        "source_node": source_node,
        "target_node": target_node,
        "source_ref": source_ref,
        "attributes": attributes,
    }
    return {
        "seed_id": sha256_id(seed_identity),
        **seed_identity,
        "production_terminal": bool(production_terminal),
        "source_complete": bool(source_complete),
        "unknown_reason": unknown_reason,
    }


def load_declared_inputs(repo_root: Path) -> dict[str, Any]:
    blobs = verify_pinned_inputs(repo_root)
    pass3 = yaml.safe_load(git_bytes(repo_root, INPUT_COMMIT, PASS3_PATH))
    trigger_map = json.loads(git_bytes(repo_root, INPUT_COMMIT, TRIGGER_MAP_PATH))
    descriptor_source = git_bytes(repo_root, INPUT_COMMIT, CENSUS_SUBSTRATE_PATH).decode(
        "utf-8"
    )
    descriptors = parse_descriptors(descriptor_source)
    rule24_bytes = (repo_root / RULE24_PATH).read_bytes()
    compiler_bytes = Path(__file__).read_bytes()

    receipts = {receipt["id"]: receipt for receipt in pass3["engine_receipts"]}
    code_seeds = []
    for row in pass3["rows"]:
        receipt = receipts[row["surface"]]
        code_seeds.append(
            make_seed(
                edge_kind="CODE_BINDING",
                source_node=f"code:{receipt['path']}",
                target_node=f"ontology:{row['concept']}",
                production_terminal=True,
                source_ref=f"{PASS3_PATH}#{row['id']} @ {INPUT_COMMIT}",
                attributes={
                    "pass3_row_id": row["id"],
                    "resolution_state": row["resolution_state"],
                    "display_verdict": row["display_verdict"],
                    "failure_classes": row["failure_classes"],
                },
            )
        )

    triggers = trigger_map.get("triggers") or {}
    trigger_seeds = []
    for trigger_name in sorted(triggers):
        record = triggers[trigger_name]
        for index, target in enumerate(record.get("targets") or []):
            target_identity = target.get("arn") or target.get("name")
            trigger_seeds.append(
                make_seed(
                    edge_kind="TRIGGER_TARGET",
                    source_node=f"trigger:{record.get('service')}:{trigger_name}",
                    target_node=f"resource:{target.get('type')}:{target_identity}",
                    production_terminal=True,
                    source_ref=f"{TRIGGER_MAP_PATH}#triggers/{trigger_name}/targets/{index} @ {INPUT_COMMIT}",
                    attributes={
                        "trigger_name": trigger_name,
                        "service": record.get("service"),
                        "state": record.get("state"),
                        "expression": record.get("expression"),
                        "target_type": target.get("type"),
                        "declared": record.get("declared"),
                    },
                )
            )

    declared_total = int((trigger_map.get("_denominators") or {}).get("total_triggers", 0))
    trigger_key_delta = declared_total - len(triggers)
    unknown_seeds = []
    for index in range(max(0, trigger_key_delta)):
        unknown_seeds.append(
            make_seed(
                edge_kind="TRIGGER_TARGET",
                source_node=f"trigger:UNKNOWN:unmaterialized-{index + 1}",
                target_node=None,
                production_terminal=False,
                source_ref=f"{TRIGGER_MAP_PATH}#_denominators/total_triggers @ {INPUT_COMMIT}",
                attributes={
                    "declared_total": declared_total,
                    "keyed_trigger_rows": len(triggers),
                    "residue_index": index + 1,
                },
                source_complete=False,
                unknown_reason=(
                    "trigger-map declared denominator exceeds keyed rows; collision versus stale "
                    "denominator is not decidable from the committed map"
                ),
            )
        )
    if trigger_key_delta < 0:
        raise ValueError("trigger-map keyed rows exceed its declared denominator")

    descriptor_seeds = []
    for key in sorted(descriptors):
        descriptor = descriptors[key]
        descriptor_seeds.append(
            make_seed(
                edge_kind="INVENTORY_DESCRIPTOR",
                source_node=f"descriptor:{key}",
                target_node=f"inventory-api:{descriptor.get('api')}",
                production_terminal=False,
                source_ref=f"{CENSUS_SUBSTRATE_PATH}#DESCRIPTORS/{key} @ {INPUT_COMMIT}",
                attributes={
                    "descriptor": key,
                    "provider": descriptor.get("provider"),
                    "service": descriptor.get("service"),
                    "api": descriptor.get("api"),
                    "join_graph": descriptor.get("join_graph"),
                },
            )
        )

    input_manifest = {
        "input_commit": INPUT_COMMIT,
        "blobs": blobs,
        "rule24_sha256": "sha256:" + hashlib.sha256(rule24_bytes).hexdigest(),
        "compiler_version": COMPILER_VERSION,
        "adapter_denominators": {
            "pass3_rows": len(code_seeds),
            "trigger_declared_total": declared_total,
            "trigger_keyed_rows": len(triggers),
            "trigger_target_edges": len(trigger_seeds),
            "trigger_unknown_residue": len(unknown_seeds),
            "inventory_descriptors": len(descriptor_seeds),
        },
    }
    return {
        "input_manifest": input_manifest,
        "generation_run_id": sha256_id(input_manifest),
        "compiler_source_sha256": "sha256:" + hashlib.sha256(compiler_bytes).hexdigest(),
        "observed_at": git_commit_time(repo_root, INPUT_COMMIT),
        "seeds": code_seeds + trigger_seeds + descriptor_seeds + unknown_seeds,
    }


def row_identity(row: dict[str, Any]) -> dict[str, Any]:
    return {
        key: copy.deepcopy(row[key])
        for key in (
            "seed_id",
            "edge_kind",
            "source_node",
            "target_node",
            "source_ref",
            "attributes",
            "closure_state",
            "path_witness",
            "state_reason",
        )
    }


def _path_to_terminal(
    source: str,
    adjacency: dict[str, list[tuple[str, str]]],
    terminals: set[str],
) -> list[str] | None:
    queue = deque([(source, [])])
    visited = {source}
    while queue:
        node, path = queue.popleft()
        if node in terminals and path:
            return path
        for target, edge_id in sorted(adjacency.get(node, [])):
            if target in visited:
                continue
            visited.add(target)
            queue.append((target, path + [edge_id]))
    return None


def compile_population(
    bundle: dict[str, Any], extra_seeds: list[dict[str, Any]] | None = None
) -> dict[str, Any]:
    seeds = copy.deepcopy(bundle["seeds"]) + copy.deepcopy(extra_seeds or [])
    adjacency: dict[str, list[tuple[str, str]]] = defaultdict(list)
    terminals: set[str] = set()
    valid_edge_ids: set[str] = set()

    for seed in seeds:
        if seed.get("edge_kind") not in EDGE_KINDS:
            continue
        source, target = seed.get("source_node"), seed.get("target_node")
        if seed.get("source_complete") and source and target:
            adjacency[source].append((target, seed["seed_id"]))
            valid_edge_ids.add(seed["seed_id"])
            if seed.get("production_terminal"):
                terminals.add(target)

    rows = []
    for seed in sorted(seeds, key=lambda item: item["seed_id"]):
        required = ("seed_id", "edge_kind", "source_node", "source_ref", "attributes")
        malformed = [name for name in required if not seed.get(name)]
        if seed.get("edge_kind") not in EDGE_KINDS:
            malformed.append("edge_kind_not_declared")

        if malformed or (seed.get("source_complete") and not seed.get("target_node")):
            state = "FAILED"
            path: list[str] = []
            reason = "normalization failed: " + ", ".join(
                malformed or ["known seed missing target_node"]
            )
        elif not seed.get("source_complete"):
            state = "UNKNOWN"
            path = []
            reason = seed.get("unknown_reason") or "source population is incomplete"
        else:
            found = _path_to_terminal(seed["source_node"], adjacency, terminals)
            if found:
                state, path, reason = "REACHED", found, "path witness reaches a declared production terminal"
            else:
                state, path, reason = "NOT_REACHED", [], "valid seed has no path to a declared production terminal"

        row = {
            "seed_id": seed["seed_id"],
            "edge_kind": seed.get("edge_kind"),
            "source_node": seed.get("source_node"),
            "target_node": seed.get("target_node"),
            "source_ref": seed.get("source_ref"),
            "attributes": copy.deepcopy(seed.get("attributes") or {}),
            "closure_state": state,
            "path_witness": path,
            "state_reason": reason,
            "generation": {
                "generated_by": COMPILER_ID,
                "compiler_version": COMPILER_VERSION,
                "generation_run_id": bundle["generation_run_id"],
            },
        }
        row["row_id"] = sha256_id(row_identity(row))
        rows.append(row)

    state_counts = {state: sum(row["closure_state"] == state for row in rows) for state in CLOSURE_STATES}
    kind_counts = {kind: sum(row["edge_kind"] == kind for row in rows) for kind in EDGE_KINDS}
    population = {
        "schema": "nfra_epistemy.c7.d3_population/0.1.0-proposed",
        "source_of_record": (
            "docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md sections "
            f"0 and component 7 @ {INPUT_COMMIT}"
        ),
        "generation": {
            "generated_by": COMPILER_ID,
            "compiler_version": COMPILER_VERSION,
            "compiler_source_sha256": bundle["compiler_source_sha256"],
            "generation_run_id": bundle["generation_run_id"],
            "input_manifest": copy.deepcopy(bundle["input_manifest"]),
        },
        "population_predicate": (
            "all normalized influence seeds generated by the three declared adapters at "
            "the pinned input commit, plus explicit source-denominator residue"
        ),
        "denominators": {
            "d3_rows": len(rows),
            "edge_kind_counts": kind_counts,
            "closure_state_counts": state_counts,
            "valid_graph_edges": len(valid_edge_ids),
            "production_terminal_nodes": len(terminals),
        },
        "traversal_residue": [
            "subscriber instance population is not present in the declared C7 input bundle",
            "inventory descriptors have no pinned live inventory result and therefore terminate NOT_REACHED",
        ],
        "rows": rows,
    }
    population["population_digest"] = sha256_id(population)
    return population


def validate_process_generated_row(row: dict[str, Any], generation_run_id: str) -> list[str]:
    errors = []
    generation = row.get("generation") or {}
    if generation.get("generated_by") != COMPILER_ID:
        errors.append("generated_by mismatch")
    if generation.get("compiler_version") != COMPILER_VERSION:
        errors.append("compiler_version mismatch")
    if generation.get("generation_run_id") != generation_run_id:
        errors.append("generation_run_id mismatch")
    try:
        expected = sha256_id(row_identity(row))
    except KeyError as exc:
        errors.append(f"row identity field absent: {exc}")
    else:
        if row.get("row_id") != expected:
            errors.append("row_id does not recompute")
    return errors


def validate_population(population: dict[str, Any]) -> list[str]:
    errors = []
    generation_run_id = (population.get("generation") or {}).get("generation_run_id")
    rows = population.get("rows") or []
    if population.get("denominators", {}).get("d3_rows") != len(rows):
        errors.append("d3 row denominator mismatch")
    if len({row.get("row_id") for row in rows}) != len(rows):
        errors.append("row_id uniqueness failure")
    for index, row in enumerate(rows):
        for error in validate_process_generated_row(row, generation_run_id):
            errors.append(f"row[{index}] {error}")
        if row.get("closure_state") not in CLOSURE_STATES:
            errors.append(f"row[{index}] closure_state not declared")
        if row.get("edge_kind") not in EDGE_KINDS:
            errors.append(f"row[{index}] edge_kind not declared")
        if row.get("closure_state") == "REACHED" and not row.get("path_witness"):
            errors.append(f"row[{index}] REACHED without path witness")
        if row.get("closure_state") != "REACHED" and row.get("path_witness"):
            errors.append(f"row[{index}] non-REACHED row carries path witness")
    digest = population.get("population_digest")
    candidate = copy.deepcopy(population)
    candidate.pop("population_digest", None)
    if digest != sha256_id(candidate):
        errors.append("population_digest does not recompute")
    return errors


def load_c1_module(repo_root: Path):
    module_file = repo_root / C1_MODULE_PATH
    working_blob = subprocess.check_output(
        ["git", "hash-object", str(module_file)], cwd=repo_root, text=True
    ).strip()
    if working_blob != EXPECTED_BLOBS[C1_MODULE_PATH]:
        raise RuntimeError("landed C1 implementation working bytes differ from pinned blob")
    spec = importlib.util.spec_from_file_location("nfra_epistemy_c1_observation", module_file)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load landed C1 observation implementation")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_observation(repo_root: Path, bundle: dict[str, Any], population: dict[str, Any]) -> dict[str, Any]:
    c1 = load_c1_module(repo_root)
    record = c1.build_record(
        instrument_id=COMPILER_ID,
        instrument_version=bundle["compiler_source_sha256"],
        request={
            "input_commit": INPUT_COMMIT,
            "generation_run_id": bundle["generation_run_id"],
            "population_predicate": population["population_predicate"],
        },
        status={
            "acquisition": "PRESENT",
            "transport": "SUCCEEDED",
            "enumeration": "SUCCEEDED",
            "parse": "SUCCEEDED",
        },
        plane="DESIRED",
        substrate="codebase",
        population_predicate=population["population_predicate"],
        denominator_count=population["denominators"]["d3_rows"],
        denominator_grain="directed production-influence seed closure row",
        denominator_process=(
            "NFRA_EPISTEMY C7 compiler over pinned Pass-3, trigger-map, and "
            "census_substrate descriptor inputs"
        ),
        substantive_value=population,
        unknown_reason="",
        observed_at=bundle["observed_at"],
        support_pointers=[
            f"{PASS3_PATH} @ {INPUT_COMMIT}",
            f"{TRIGGER_MAP_PATH} @ {INPUT_COMMIT}",
            f"{CENSUS_SUBSTRATE_PATH} @ {INPUT_COMMIT}",
            f"{RULE24_PATH} @ ed742cd929",
        ],
        traversal_residue=population["traversal_residue"],
        control_references=[
            "NFRA_EPISTEMY.C7-CLOSURE/evidence/acceptance_results.json",
            "C7 hand-authored-row and unreachable-edge mutants",
        ],
        discrimination_certificate_ref=None,
        invalidation_predicates=[
            "any pinned input blob changes",
            "compiler source or adapter contract changes",
            "Rule-24 edge/state/predicate record changes",
            "trigger-map declared/keyed denominator mismatch changes",
        ],
    )
    errors = c1.validate_record(record)
    if errors:
        raise ValueError(f"C1 envelope validation failed: {errors}")
    return record
