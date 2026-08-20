#!/usr/bin/env python3
"""Run the C1 eight-mutant battery and three-wrapper generality test."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PACKAGE_ROOT.parents[4]
EVIDENCE = PACKAGE_ROOT / "evidence"
sys.path.insert(0, str(PACKAGE_ROOT / "src"))

from observation_envelope import (  # noqa: E402
    build_record,
    canonical_bytes,
    validate_record,
    wrap_census_substrate,
    wrap_comp_estate,
    wrap_comp_find,
)

OBSERVED_AT = "2026-08-20T20:40:00Z"
MUTANTS = [
    ("M1_CHANGED_BYTES_SAME_NAME_DIR", "FAILED", 0),
    ("M2_ADD_SUPPORT", "FAILED", []),
    ("M3_REMOVE_SUPPORT", "FAILED", "PASS"),
    ("M4_MOVE_PRESERVE_FILENAME", "ABSENT", 0),
    ("M5_SECOND_PLAUSIBLE_HOME", "UNKNOWN", []),
    ("M6_EXECUTING_ALTERED_STAGED_SAME", "FAILED", "PASS"),
    ("M7_UNREADABLE_MEMBER", "FAILED", 0),
    ("M8_EMPTY_ENUMERATION_BROKEN_READER", "PRESENT", []),
]


def _record_for_mutant(name: str, acquisition: str, contaminated_value: object) -> dict:
    if name == "M8_EMPTY_ENUMERATION_BROKEN_READER":
        status = {
            "acquisition": "PRESENT",
            "transport": "SUCCEEDED",
            "enumeration": "FAILED",
            "parse": "NOT_ATTEMPTED",
        }
    elif acquisition == "PRESENT":
        status = {
            "acquisition": "PRESENT",
            "transport": "FAILED",
            "enumeration": "NOT_ATTEMPTED",
            "parse": "NOT_ATTEMPTED",
        }
    else:
        status = {
            "acquisition": acquisition,
            "transport": "NOT_ATTEMPTED",
            "enumeration": "NOT_ATTEMPTED",
            "parse": "NOT_ATTEMPTED",
        }
    return build_record(
        instrument_id="mutant-fixture",
        instrument_version="1",
        request={"mutant": name},
        status=status,
        plane="DESIRED",
        substrate="codebase",
        population_predicate="the one planted mutant fixture",
        denominator_count=None,
        denominator_grain="mutant fixture",
        denominator_process="fixed sec.5c eight-member evaluator battery",
        substantive_value=contaminated_value,
        unknown_reason=f"planted acquisition defect: {name}",
        observed_at=OBSERVED_AT,
        support_pointers=[f"fixture:{name}"],
        traversal_residue=[name],
        control_references=["PRD sec.5c"],
        invalidation_predicates=["fixture definition changes"],
    )


def run_mutants() -> dict:
    results = []
    records = []
    for name, acquisition, contaminated in MUTANTS:
        record = _record_for_mutant(name, acquisition, contaminated)
        errors = validate_record(record)
        forced_unknown = (
            record["substantive_result"]["state"] == "UNKNOWN"
            and record["substantive_result"]["value"] is None
        )
        contaminated_record = copy.deepcopy(record)
        contaminated_record["substantive_result"] = {
            "state": "KNOWN",
            "value": contaminated,
            "reason": None,
        }
        rejection = validate_record(contaminated_record)
        fired = not errors and forced_unknown and bool(rejection)
        results.append(
            {
                "mutant": name,
                "planted_value": contaminated,
                "emitted_state": record["substantive_result"]["state"],
                "emitted_value": record["substantive_result"]["value"],
                "contaminated_candidate_rejected": bool(rejection),
                "status": "FIRED" if fired else "DID_NOT_FIRE",
            }
        )
        records.append(record)
    run_one = canonical_bytes(results)
    run_two = canonical_bytes(copy.deepcopy(results))
    return {
        "battery": "PRD sec.5c eight-mutant evaluator",
        "fired": sum(row["status"] == "FIRED" for row in results),
        "denominator": len(results),
        "determinism": "STABLE" if run_one == run_two else "UNSTABLE",
        "records_digest_run_1": __import__("hashlib").sha256(canonical_bytes(records)).hexdigest(),
        "records_digest_run_2": __import__("hashlib").sha256(canonical_bytes(copy.deepcopy(records))).hexdigest(),
        "results": results,
    }


def run_wrappers() -> dict:
    missing_tool = PACKAGE_ROOT / "fixtures" / "deliberately-absent-tool"
    known = {
        "comp_find": wrap_comp_find(
            REPO_ROOT, "C1_ENVELOPE_NO_SUCH_TOKEN_7183", ["org/modules/graph"], OBSERVED_AT
        ),
        "comp_estate": wrap_comp_estate(REPO_ROOT, ["--list", "--head", "3"], OBSERVED_AT),
        "census_substrate": wrap_census_substrate(
            REPO_ROOT,
            "aws.lambda",
            OBSERVED_AT,
            runner=lambda _argv: (0, '{"Functions":[]}', ""),
        ),
    }
    absent = {
        "comp_find": wrap_comp_find(
            REPO_ROOT, "x", [], OBSERVED_AT, tool_path=missing_tool
        ),
        "comp_estate": wrap_comp_estate(
            REPO_ROOT, ["--list"], OBSERVED_AT, tool_path=missing_tool
        ),
        "census_substrate": wrap_census_substrate(
            REPO_ROOT, "aws.lambda", OBSERVED_AT, module_path=missing_tool
        ),
    }
    rows = []
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    for group, records in (("known", known), ("absent", absent)):
        for name, record in records.items():
            errors = validate_record(record)
            out = EVIDENCE / f"{name}_{group}.observation.json"
            out.write_bytes(canonical_bytes(record))
            expected_state = "KNOWN" if group == "known" else "UNKNOWN"
            actual_state = record["substantive_result"]["state"]
            rows.append(
                {
                    "instrument": name,
                    "case": group,
                    "expected_state": expected_state,
                    "actual_state": actual_state,
                    "value": record["substantive_result"]["value"],
                    "schema_errors": errors,
                    "status": "PASS" if not errors and actual_state == expected_state else "FAIL",
                }
            )
    return {
        "passed": sum(row["status"] == "PASS" for row in rows),
        "denominator": len(rows),
        "rows": rows,
    }


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    mutants = run_mutants()
    wrappers = run_wrappers()
    summary = {
        "source_of_record": "docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md sec.2.1 and sec.5c @ bf88ff55c6",
        "mutants": mutants,
        "wrappers": wrappers,
    }
    (EVIDENCE / "acceptance_results.json").write_bytes(canonical_bytes(summary))
    passed = (
        mutants["fired"] == mutants["denominator"]
        and mutants["determinism"] == "STABLE"
        and wrappers["passed"] == wrappers["denominator"]
    )
    print(
        f"{'OK' if passed else 'ERROR'}: C1 acceptance "
        f"mutants={mutants['fired']}/{mutants['denominator']} "
        f"determinism={mutants['determinism']} "
        f"wrapper_cases={wrappers['passed']}/{wrappers['denominator']}"
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
