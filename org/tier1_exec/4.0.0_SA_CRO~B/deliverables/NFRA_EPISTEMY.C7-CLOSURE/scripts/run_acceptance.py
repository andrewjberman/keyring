#!/usr/bin/env python3
"""Scratch-first acceptance and process-generation driver for C7-CLOSURE."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SRC = PACKAGE_ROOT / "src" / "influence_closure.py"


def load_compiler():
    spec = importlib.util.spec_from_file_location("nfra_epistemy_c7_closure", SRC)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load C7 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def run(write: bool = False) -> dict:
    c7 = load_compiler()
    repo_root = c7.repo_root_from_script()
    bundle = c7.load_declared_inputs(repo_root)

    unreachable_seed = c7.make_seed(
        edge_kind="INVENTORY_DESCRIPTOR",
        source_node="mutant:unreachable-source",
        target_node="mutant:nonterminal-frontier",
        production_terminal=False,
        source_ref="scratch-mutant:unreachable-edge",
        attributes={"mutant": "UNREACHABLE_EDGE"},
    )
    malformed_seed = c7.make_seed(
        edge_kind="TRIGGER_TARGET",
        source_node="mutant:malformed-source",
        target_node=None,
        production_terminal=True,
        source_ref="scratch-mutant:malformed-edge",
        attributes={"mutant": "FAILED_NORMALIZATION"},
        source_complete=True,
    )

    # Phase 2: write only into an OS scratch directory. No D3 deliverable exists yet.
    with tempfile.TemporaryDirectory(prefix="nfra_epistemy_c7_scratch_") as scratch:
        scratch_path = Path(scratch) / "scratch_population.json"
        scratch_population = c7.compile_population(
            bundle, extra_seeds=[unreachable_seed, malformed_seed]
        )
        scratch_path.write_bytes(c7.canonical_bytes(scratch_population))
        scratch_roundtrip = json.loads(scratch_path.read_text(encoding="ascii"))

        unreachable_rows = [
            row
            for row in scratch_roundtrip["rows"]
            if row["attributes"].get("mutant") == "UNREACHABLE_EDGE"
        ]
        malformed_rows = [
            row
            for row in scratch_roundtrip["rows"]
            if row["attributes"].get("mutant") == "FAILED_NORMALIZATION"
        ]
        assert len(unreachable_rows) == 1
        assert unreachable_rows[0]["closure_state"] == "NOT_REACHED"
        assert unreachable_rows[0]["path_witness"] == []
        assert len(malformed_rows) == 1
        assert malformed_rows[0]["closure_state"] == "FAILED"

        hand_authored = copy.deepcopy(unreachable_rows[0])
        hand_authored["generation"]["generated_by"] = "hand-authored-mutant"
        origin_errors = c7.validate_process_generated_row(
            hand_authored, bundle["generation_run_id"]
        )
        assert "generated_by mismatch" in origin_errors

    # Phase 3: same-input production runs, still in memory until every check passes.
    population_a = c7.compile_population(bundle)
    population_b = c7.compile_population(bundle)
    bytes_a = c7.canonical_bytes(population_a)
    bytes_b = c7.canonical_bytes(population_b)
    assert bytes_a == bytes_b
    population_errors = c7.validate_population(population_a)
    assert population_errors == [], population_errors

    denominators = population_a["denominators"]
    assert denominators["d3_rows"] == 175
    assert denominators["edge_kind_counts"] == {
        "CODE_BINDING": 10,
        "TRIGGER_TARGET": 163,
        "INVENTORY_DESCRIPTOR": 2,
    }
    assert denominators["closure_state_counts"] == {
        "REACHED": 172,
        "NOT_REACHED": 2,
        "UNKNOWN": 1,
        "FAILED": 0,
    }
    assert all(
        not c7.validate_process_generated_row(row, bundle["generation_run_id"])
        for row in population_a["rows"]
    )

    observation_a = c7.build_observation(repo_root, bundle, population_a)
    observation_b = c7.build_observation(repo_root, bundle, population_b)
    observation_bytes_a = c7.canonical_bytes(observation_a)
    observation_bytes_b = c7.canonical_bytes(observation_b)
    assert observation_bytes_a == observation_bytes_b

    results = {
        "component": "NFRA_EPISTEMY.C7-CLOSURE",
        "input_commit": c7.INPUT_COMMIT,
        "generation_run_id": bundle["generation_run_id"],
        "scratch_before_d3_write": "PASS",
        "mutants": {
            "hand_authored_d3_row": {
                "expected": "REJECTED_NOT_PROCESS_GENERATED",
                "observed_errors": origin_errors,
                "status": "FIRED",
            },
            "unreachable_edge": {
                "expected": "NOT_REACHED_WITH_EMPTY_PATH_WITNESS",
                "observed": unreachable_rows[0]["closure_state"],
                "status": "FIRED",
            },
            "malformed_edge": {
                "expected": "FAILED_NOT_DROPPED",
                "observed": malformed_rows[0]["closure_state"],
                "status": "FIRED",
            },
        },
        "declared_status_shape_exercise": {
            "REACHED": denominators["closure_state_counts"]["REACHED"],
            "NOT_REACHED": denominators["closure_state_counts"]["NOT_REACHED"],
            "UNKNOWN": denominators["closure_state_counts"]["UNKNOWN"],
            "FAILED_scratch_mutant": 1,
            "status": "ALL_FOUR_TERMINALS_EXERCISED",
        },
        "denominators": denominators,
        "process_generation": {
            "rows_valid": 175,
            "rows_total": 175,
            "hand_authored_rows_admitted": 0,
            "status": "PASS",
        },
        "determinism": {
            "population_two_runs_byte_identical": True,
            "observation_two_runs_byte_identical": True,
            "population_digest": population_a["population_digest"],
            "status": "STABLE",
        },
        "c1_envelope": {
            "source": c7.C1_MODULE_PATH,
            "schema": c7.C1_SCHEMA_PATH,
            "substantive_state": observation_a["substantive_result"]["state"],
            "denominator_count": observation_a["denominator"]["count"],
            "status": "VALID",
        },
        "population_validation_errors": population_errors,
        "overall": "PASS",
    }

    if write:
        write_bytes(PACKAGE_ROOT / "generated" / "d3_population.json", bytes_a)
        write_bytes(
            PACKAGE_ROOT / "generated" / "d3_population.observation.json",
            observation_bytes_a,
        )
        write_bytes(
            PACKAGE_ROOT / "evidence" / "acceptance_results.json",
            c7.canonical_bytes(results),
        )

    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="after all scratch and determinism checks pass, write generated artifacts",
    )
    args = parser.parse_args()
    results = run(write=args.write)
    print(
        "OK: C7 acceptance overall=%s rows=%d states=%s mutants=%s determinism=%s write=%s"
        % (
            results["overall"],
            results["denominators"]["d3_rows"],
            results["denominators"]["closure_state_counts"],
            ",".join(
                "%s:%s" % (name, value["status"])
                for name, value in results["mutants"].items()
            ),
            results["determinism"]["status"],
            args.write,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
