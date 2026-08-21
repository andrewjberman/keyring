#!/usr/bin/env python3
"""Validate an atom_layer0 run bundle.

The JSON Schema is the shape source of record. This script adds cross-field laws that
JSON Schema alone does not express economically. It writes nothing.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover - environment failure path
    print("ERROR: INSTRUMENT_UNKNOWN: jsonschema>=4 is required", file=sys.stderr)
    raise SystemExit(3) from exc

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment failure path
    print("ERROR: INSTRUMENT_UNKNOWN: PyYAML>=6 is required", file=sys.stderr)
    raise SystemExit(3) from exc


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = PACKAGE_ROOT / "schemas" / "atom_layer0_run.schema.json"
TEMPLATE_PATH = PACKAGE_ROOT / "templates" / "atom_layer0_run.template.json"
MANIFEST_PATH = PACKAGE_ROOT / "PACKAGE_MANIFEST.json"
RETRODICTION_SCHEMA_PATH = PACKAGE_ROOT / "schemas" / "retrodiction_battery.schema.json"
REPO_ROOT = PACKAGE_ROOT.parents[4]
RULE24_RECORDS_RELPATH = (
    "org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ATOM_LAYER0/"
    "rule24/SCHEMA_ENUMERATION_RECORDS.json"
)
POST_12_VINTAGE = "45a2892ed24f84356e6e50e16ba6e543f50c5169"
PRE_12_VINTAGE = "602b73a1f99d889dabbc884525b10dd8e7bf2e56"
INITIAL_RULE24_VINTAGE = "462ac78311a3d5f1310a8da3f4f7638127d449bd"
STAGES = ("s0", "s1", "s2", "s3", "s4", "s5")
SEAM_AXES = {"MECHANICAL", "DECLARATIVE", "SEMANTIC"}
REGISTRY_VINTAGE_PATTERN = re.compile(r"^([0-9a-f]{7,40})(?:\s.*)?$")


def _load(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _load_structured(path: Path) -> Any:
    """Load a JSON or YAML interface artifact without changing its row objects."""
    with path.open("r", encoding="utf-8") as handle:
        if path.suffix.lower() == ".json":
            return json.load(handle)
        return yaml.safe_load(handle)


def _bundle_registry_vintage(bundle: dict[str, Any]) -> str | None:
    """Resolve coverage vintage in the ruled order: certificate pin, then bundle pin."""
    challenge = bundle.get("s2_challenge")
    if isinstance(challenge, dict):
        certificate = challenge.get("atomicity_certificate")
        if isinstance(certificate, dict) and certificate.get("registry_vintage"):
            match = REGISTRY_VINTAGE_PATTERN.fullmatch(str(certificate["registry_vintage"]))
            return match.group(1) if match else str(certificate["registry_vintage"])
    vintage = bundle.get("vintage")
    if isinstance(vintage, dict) and vintage.get("repo_commit"):
        return str(vintage["repo_commit"])
    return None


@lru_cache(maxsize=128)
def _rule24_records_at_vintage(vintage: str) -> tuple[frozenset[str] | None, str | None]:
    proc = subprocess.run(
        ["git", "show", f"{vintage}:{RULE24_RECORDS_RELPATH}"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if proc.returncode != 0:
        commit_exists = subprocess.run(
            ["git", "cat-file", "-e", f"{vintage}^{{commit}}"],
            cwd=REPO_ROOT,
            capture_output=True,
        ).returncode == 0
        predates_package = commit_exists and subprocess.run(
            ["git", "merge-base", "--is-ancestor", vintage, INITIAL_RULE24_VINTAGE],
            cwd=REPO_ROOT,
            capture_output=True,
        ).returncode == 0
        if predates_package:
            proc = subprocess.run(
                ["git", "show", f"{INITIAL_RULE24_VINTAGE}:{RULE24_RECORDS_RELPATH}"],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
        if proc.returncode != 0:
            detail = (proc.stderr or proc.stdout).strip().splitlines()
            suffix = detail[0] if detail else "git show returned no diagnostic"
            return None, f"VINTAGE_UNRESOLVABLE: {vintage}: {suffix}"
    try:
        document = json.loads(proc.stdout)
        rows = document["records"]
        record_ids = [row["record_id"] for row in rows]
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        return None, f"VINTAGE_UNRESOLVABLE: {vintage}: malformed Rule-24 registry: {exc}"
    if len(record_ids) != len(set(record_ids)):
        return None, f"VINTAGE_UNRESOLVABLE: {vintage}: duplicate Rule-24 record ids"
    return frozenset(record_ids), None


def _rule24_coverage_frame(
    bundle: dict[str, Any],
) -> tuple[str | None, frozenset[str] | None, list[str]]:
    vintage = _bundle_registry_vintage(bundle)
    if not vintage:
        return None, None, ["VINTAGE_UNRESOLVABLE: bundle carries no registry or package vintage"]
    required, resolution_error = _rule24_records_at_vintage(vintage)
    if resolution_error or required is None:
        return vintage, None, [resolution_error or "VINTAGE_UNRESOLVABLE"]
    carried = set(bundle.get("rule24_record_ids", []))
    errors: list[str] = []
    missing = sorted(required - carried)
    unexpected = sorted(carried - required)
    if missing:
        errors.append(
            f"Rule-24 coverage at vintage {vintage} missing {len(missing)} of "
            f"{len(required)} record(s): {missing}"
        )
    if unexpected:
        errors.append(
            f"Rule-24 coverage at vintage {vintage} carries {len(unexpected)} "
            f"record(s) absent at that vintage: {unexpected}"
        )
    return vintage, required, errors


def _select_census_row(document: Any, row_id: str | None) -> tuple[dict[str, Any], str | None]:
    if not isinstance(document, dict):
        raise ValueError("census input must be a row object or a document object")
    rows = document.get("rows")
    if rows is None:
        return document, document.get("vintage")
    if not isinstance(rows, list):
        raise ValueError("census document rows must be an array")
    if not row_id:
        raise ValueError("--census-row-id is required for a document containing rows[]")
    matches = [row for row in rows if isinstance(row, dict) and row.get("id") == row_id]
    if len(matches) != 1:
        raise ValueError(f"census row selector {row_id!r} matched {len(matches)} rows")
    return matches[0], document.get("read_vintage")


def _resolution_expected(contract: dict[str, Any]) -> bool | None:
    operands: list[bool | None] = []
    count = contract["live_authority_target_count"]
    operands.append(None if count is None else count == 1)
    operands.append(contract["pointer_resolves_at_head"])
    operands.append(contract["target_carries_claimed_content"])
    operands.append(contract["declared_grain"] == contract["authority_grain"])

    axes = contract["seam_axes"]
    axis_names = {row["axis"] for row in axes}
    if axis_names != SEAM_AXES:
        return None
    operands.extend(row["passed"] for row in axes)

    if contract["is_code_binding"]:
        cite = contract["code_cites_authority"]
        redeclare = contract["code_redeclares_vocabulary"]
        operands.append(cite)
        operands.append(None if redeclare is None else not redeclare)

    if any(value is False for value in operands):
        return False
    if any(value is None for value in operands):
        return None
    return True


def semantic_errors(bundle: dict[str, Any], require_proving_defect: bool = False) -> list[str]:
    errors: list[str] = []
    challenge = bundle["s2_challenge"]
    frontier = challenge["frontier"]
    result = challenge["result"]
    certificate = challenge["atomicity_certificate"]
    certificate_state = challenge["certificate_state"]
    adequacy = challenge["grammar_adequacy"]

    expected_adequacy = bool(
        adequacy["battery"]
        and adequacy["specimens_total"] > 0
        and adequacy["specimens_expressible"] == adequacy["specimens_total"]
    )
    if adequacy["specimens_expressible"] > adequacy["specimens_total"]:
        errors.append("grammar adequacy expressible count cannot exceed total")
    if adequacy["demonstrated"] is not expected_adequacy:
        errors.append(
            f"grammar_adequacy.demonstrated={adequacy['demonstrated']!r} "
            f"but operands derive {expected_adequacy!r}"
        )

    if bundle["stage_states"]["s0"] in {"STAGE_ASSESSED", "STAGE_CORRECTLY_EMPTY"}:
        for field in ("definition", "claimed_layer", "declared_grain"):
            if not bundle["subject"][field]:
                errors.append(f"completed S0 requires subject.{field}")

    source_row = bundle["source_census_row"]
    if source_row is not None:
        if source_row["concept"] != bundle["subject"]["concept"]:
            errors.append("source_census_row.concept must equal subject.concept")
        mapped_fields = {
            "claimed_content": "definition",
            "declared_layer": "claimed_layer",
            "declared_grain": "declared_grain",
            "scope": "scope",
        }
        for row_field, subject_field in mapped_fields.items():
            if row_field in source_row and source_row[row_field]:
                if source_row[row_field] != bundle["subject"][subject_field]:
                    errors.append(
                        f"source_census_row.{row_field} must equal subject.{subject_field}"
                    )

    cells = set(frontier["cell_ids"])
    assessed = set(frontier["assessed_cell_ids"])
    opened = set(frontier["open_cell_ids"])
    unreachable = set(frontier["unreachable_cell_ids"])

    for label, subset in (
        ("assessed", assessed),
        ("open", opened),
        ("unreachable", unreachable),
    ):
        if not subset.issubset(cells):
            errors.append(f"frontier {label} cell is not in cell_ids")

    if assessed & opened or assessed & unreachable or opened & unreachable:
        errors.append("frontier assessed/open/unreachable partitions overlap")

    if result == "DECLARED_FRONTIER_EXHAUSTED":
        if not cells:
            errors.append("frontier exhaustion requires a non-empty declared frontier")
        if assessed != cells or opened or unreachable:
            errors.append("frontier exhaustion requires every cell assessed and no open/unreachable cells")
        if challenge["splitter"]["differently_derived"] is not True:
            errors.append("frontier exhaustion requires a differently-derived splitter")
        if adequacy["demonstrated"] is not True:
            errors.append("frontier exhaustion requires demonstrated grammar adequacy")
        if certificate is None:
            errors.append("frontier exhaustion requires an atomicity certificate")
        elif certificate["frontier_denominator"] != len(cells):
            errors.append("certificate frontier_denominator must equal len(cell_ids)")
    elif certificate is not None:
        errors.append("atomicity certificate is forbidden unless result is DECLARED_FRONTIER_EXHAUSTED")

    expected_certificate_state = (
        "CERTIFICATE_ISSUED"
        if result == "DECLARED_FRONTIER_EXHAUSTED" and certificate is not None
        else "CERTIFICATE_WITHHELD"
    )
    if certificate_state != expected_certificate_state:
        errors.append(
            f"certificate_state={certificate_state} but operands derive {expected_certificate_state}"
        )

    if result == "DECOMPOSITION_FOUND" and not bundle["s1_sweep"]["normalized_candidates"]:
        errors.append("DECOMPOSITION_FOUND requires at least one normalized candidate")
    if result == "BUDGET_EXHAUSTED_WITH_FRONTIER_OPEN" and not opened:
        errors.append("budget exhaustion requires at least one open frontier cell")
    if result == "NOT_EXERCISABLE" and challenge["splitter"]["differently_derived"] is not False:
        errors.append("NOT_EXERCISABLE requires differently_derived=false")

    if bundle["stage_states"]["s3"] == "STAGE_ASSESSED" and certificate is None:
        errors.append("S3 cannot be assessed without an atomicity certificate")

    for contract in bundle["s4_resolution"]["contracts"]:
        axes = [row["axis"] for row in contract["seam_axes"]]
        if len(set(axes)) != 3 or set(axes) != SEAM_AXES:
            errors.append(f"{contract['binding_id']}: seam_axes must contain each axis exactly once")
            continue
        expected = _resolution_expected(contract)
        if contract["resolved"] is not expected:
            errors.append(
                f"{contract['binding_id']}: resolved={contract['resolved']!r} "
                f"but operands derive {expected!r}"
            )
        direction = contract["failure_direction"]
        if not direction["fails_loud"] and not direction["fails_clean"]:
            errors.append(f"{contract['binding_id']}: failure direction cannot be empty")
        for prefix in ("loud", "clean"):
            if direction[f"fails_{prefix}"]:
                if not direction[f"{prefix}_condition"] or not direction[f"{prefix}_detector"]:
                    errors.append(
                        f"{contract['binding_id']}: {prefix} failure requires condition and detector"
                    )

    expected_not_assessed = {
        stage for stage in STAGES if bundle["stage_states"][stage] == "STAGE_NOT_ASSESSED"
    }
    recorded_not_assessed = set(bundle["residue"]["stage_not_assessed"])
    if expected_not_assessed != recorded_not_assessed:
        errors.append(
            "residue.stage_not_assessed must exactly match stages marked STAGE_NOT_ASSESSED"
        )

    _, _, coverage_errors = _rule24_coverage_frame(bundle)
    errors.extend(coverage_errors)

    proving = bundle["s5_proving"]
    expected_acceptance = bool(
        bundle["stage_states"]["s5"] == "STAGE_ASSESSED"
        and proving["subject_selected_by"] not in (None, "", "4.0.0_SA_CRO~A")
        and proving["method_defect"]["found"] is True
        and proving["method_defect"]["repair"]
        and proving["regression_check"]
    )
    if proving["acceptance_satisfied"] is not expected_acceptance:
        errors.append(
            f"s5 acceptance_satisfied={proving['acceptance_satisfied']!r} "
            f"but operands derive {expected_acceptance!r}"
        )

    if require_proving_defect:
        if bundle["stage_states"]["s5"] != "STAGE_ASSESSED":
            errors.append("proving acceptance requires S5 STAGE_ASSESSED")
        if proving["subject_selected_by"] in (None, "", "4.0.0_SA_CRO~A"):
            errors.append("proving subject must be selected outside the method-authoring seat")
        if proving["method_defect"]["found"] is not True:
            errors.append("proving acceptance requires method_defect.found=true")
        if not proving["method_defect"]["repair"]:
            errors.append("proving acceptance requires a recorded repair")
        if not proving["regression_check"]:
            errors.append("proving acceptance requires a regression check")
        if proving["acceptance_satisfied"] is not True:
            errors.append("proving acceptance requires acceptance_satisfied=true")

    return errors


def validate(bundle: dict[str, Any], require_proving_defect: bool = False) -> list[str]:
    schema = _load(SCHEMA_PATH)
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    errors = [
        f"schema {'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(bundle), key=lambda item: list(item.absolute_path))
    ]
    if not errors:
        errors.extend(semantic_errors(bundle, require_proving_defect=require_proving_defect))
    return errors


def validate_retrodiction_battery(battery: dict[str, Any]) -> list[str]:
    schema = _load(RETRODICTION_SCHEMA_PATH)
    validator = jsonschema.Draft202012Validator(schema)
    errors = [
        f"schema {'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(battery), key=lambda item: list(item.absolute_path))
    ]
    if errors:
        return errors

    ids = [row["id"] for row in battery["specimens"]]
    if len(set(ids)) != len(ids):
        errors.append("retrodiction specimen ids must be unique")
    all_expressible = all(row["expressible"] for row in battery["specimens"])
    if battery["all_expressible"] is not all_expressible:
        errors.append("all_expressible must derive from every specimen expressible flag")
    if battery["grammar_v2_required"] is not (not all_expressible):
        errors.append("grammar_v2_required must be the inverse of all_expressible")

    for row in battery["specimens"]:
        if row["expressible"]:
            if row["operator"] is None or len(row["children"]) < 2 or not row["reconstruction_rule"]:
                errors.append(f"{row['id']}: expressible specimen requires operator, 2+ children, and reconstruction_rule")
            if not all(row["admissibility"].values()):
                errors.append(f"{row['id']}: expressible specimen must pass every admissibility test")
            if row["inexpressibility_reason"] is not None or row["v2_operator_proposal"] is not None:
                errors.append(f"{row['id']}: expressible specimen cannot carry a v2 defect proposal")
        else:
            if row["inexpressibility_reason"] is None or row["v2_operator_proposal"] is None:
                errors.append(f"{row['id']}: inexpressible specimen requires reason and v2 operator proposal")
    return errors


def compile_census_row(row: dict[str, Any], document_vintage: str | None = None) -> dict[str, Any]:
    external = "id" in row
    required = (
        {
            "id",
            "surface",
            "concept",
            "assessment_state",
            "resolution_state",
            "failure_classes",
            "display_verdict",
            "evidence",
            "owner",
        }
        if external
        else {
            "row_id",
            "surface",
            "concept",
            "verdict",
            "verdict_schema",
            "evidence_pointer",
            "candidate_owner",
            "vintage",
        }
    )
    missing = sorted(required - set(row))
    if missing:
        raise ValueError(f"census row missing required fields: {missing}")

    row_id = row["id"] if external else row["row_id"]
    vintage = document_vintage if external else row["vintage"]
    if not vintage:
        raise ValueError("external census row requires document read_vintage")

    bundle = _load(TEMPLATE_PATH)
    bundle["run_id"] = f"AL0-FROM-{row_id}"
    bundle["vintage"] = {
        "repo_commit": vintage,
        "observed_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    bundle["subject"] = {
        "concept": row["concept"],
        "definition": row.get("claimed_content") or None,
        "claimed_layer": row.get("declared_layer") or None,
        "declared_grain": row.get("declared_grain") or None,
        "scope": row.get("scope") or f"{row['surface']} x {row['concept']}",
    }
    bundle["source_census_row"] = copy.deepcopy(row)
    required_records, resolution_error = _rule24_records_at_vintage(vintage)
    if resolution_error or required_records is None:
        raise ValueError(resolution_error or "VINTAGE_UNRESOLVABLE")
    bundle["rule24_record_ids"] = sorted(required_records)
    bundle["s5_proving"]["subject_selected_by"] = "4.0.0_SA_CRO~B via 4.0.0_SA_CRO"
    bundle["residue"]["unknowns"] = [
        f"S0 must assess fields not supplied by census row {row_id}"
    ]
    return bundle


def self_test() -> int:
    base = _load(TEMPLATE_PATH)
    base["vintage"]["repo_commit"] = POST_12_VINTAGE
    post_records, post_error = _rule24_records_at_vintage(POST_12_VINTAGE)
    if post_error or post_records is None:
        print(f"ERROR: self-test post-12 control cannot resolve: {post_error}")
        return 1
    base["rule24_record_ids"] = sorted(post_records)
    cases: list[tuple[str, dict[str, Any], bool, bool]] = []
    cases.append(("template", copy.deepcopy(base), False, True))

    decorated = _load(PACKAGE_ROOT / "proving_runs" / "R015_CONTRACT_RECORD" / "atom_layer0_run.json")
    decorated["s2_challenge"]["atomicity_certificate"]["registry_vintage"] = (
        f"{POST_12_VINTAGE} (SYSTEM_DEFINITIONS.yaml blob 43b50adf54, v3.11)"
    )
    cases.append(("decorated-registry-vintage", decorated, False, True))

    pre_12 = copy.deepcopy(base)
    pre_12["vintage"]["repo_commit"] = PRE_12_VINTAGE
    pre_12["rule24_record_ids"] = [f"R24-AL0-{number:03d}" for number in range(1, 12)]
    cases.append(("pre-12-valid-at-vintage", pre_12, False, True))

    no_pin = copy.deepcopy(base)
    no_pin["vintage"]["repo_commit"] = "UNRESOLVED"
    cases.append(("vintage-unresolvable", no_pin, False, False))

    wrong_cert = copy.deepcopy(base)
    wrong_cert["s2_challenge"]["atomicity_certificate"] = {
        "claim": "ATOMIC_WITHIN(decomposition_grammar@1.0.0 x test)",
        "grammar": "decomposition_grammar@1.0.0",
        "scope": "test",
        "grain": "concept",
        "frontier_denominator": 1,
        "evidence_vintage": "dae378a",
    }
    cases.append(("certificate-without-closure", wrong_cert, False, False))

    false_exhaustion = copy.deepcopy(base)
    false_exhaustion["s2_challenge"]["result"] = "DECLARED_FRONTIER_EXHAUSTED"
    false_exhaustion["s2_challenge"]["frontier"] = {
        "cell_ids": ["c1"],
        "assessed_cell_ids": [],
        "open_cell_ids": ["c1"],
        "unreachable_cell_ids": [],
    }
    cases.append(("open-frontier-closure", false_exhaustion, False, False))

    bad_residue = copy.deepcopy(base)
    bad_residue["residue"]["stage_not_assessed"] = []
    cases.append(("silent-not-assessed", bad_residue, False, False))

    bad_proving = copy.deepcopy(base)
    cases.append(("proving-without-defect", bad_proving, True, False))

    bad_result = copy.deepcopy(base)
    bad_result["s2_challenge"]["result"] = "BUDGET_EXHAUSTED_WITH_FRONTIER_OPEN"
    cases.append(("budget-with-no-open-frontier", bad_result, False, False))

    unretrodicted = copy.deepcopy(base)
    unretrodicted["s2_challenge"]["result"] = "DECLARED_FRONTIER_EXHAUSTED"
    unretrodicted["s2_challenge"]["certificate_state"] = "CERTIFICATE_ISSUED"
    unretrodicted["s2_challenge"]["splitter"]["differently_derived"] = True
    unretrodicted["s2_challenge"]["frontier"] = {
        "cell_ids": ["c1"],
        "assessed_cell_ids": ["c1"],
        "open_cell_ids": [],
        "unreachable_cell_ids": [],
    }
    unretrodicted["s2_challenge"]["atomicity_certificate"] = {
        "claim": "ATOMIC_WITHIN(decomposition_grammar@1.0.0 x test)",
        "grammar": "decomposition_grammar@1.0.0",
        "scope": "test",
        "grain": "concept",
        "frontier_denominator": 1,
        "evidence_vintage": "dae378a",
    }
    cases.append(("certificate-without-grammar-adequacy", unretrodicted, False, False))

    compiled = compile_census_row(
        {
            "row_id": "ROW-1",
            "surface": "example/file.yaml",
            "concept": "Example_Concept",
            "verdict": "EXTERNAL_TYPED_VALUE",
            "verdict_schema": "resolution_census@external",
            "evidence_pointer": "example/file.yaml:1 @ deadbee",
            "candidate_owner": "example-owner",
            "vintage": PRE_12_VINTAGE,
        }
    )
    cases.append(("census-row-compiler", compiled, False, True))

    passed = 0
    for name, bundle, require_defect, should_pass in cases:
        errors = validate(bundle, require_proving_defect=require_defect)
        actual_pass = not errors
        if actual_pass != should_pass:
            print(f"ERROR: self-test {name} expected {should_pass} got {actual_pass}")
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        passed += 1
    battery = _load(PACKAGE_ROOT / "proving_runs" / "RETRODICTION_BATTERY_20260820.json")
    battery_errors = validate_retrodiction_battery(battery)
    if battery_errors:
        for error in battery_errors:
            print(f"ERROR: retrodiction battery self-test: {error}")
        return 1
    passed += 1

    bad_battery = copy.deepcopy(battery)
    bad_battery["grammar_v2_required"] = True
    if not validate_retrodiction_battery(bad_battery):
        print("ERROR: retrodiction battery mutant was not rejected")
        return 1
    passed += 1

    total = len(cases) + 2
    pre_records, _ = _rule24_records_at_vintage(PRE_12_VINTAGE)
    post_records, _ = _rule24_records_at_vintage(POST_12_VINTAGE)
    print(f"OK: 1 bundle validated at vintage {PRE_12_VINTAGE} ({len(pre_records or [])} records)")
    print(f"OK: 1 bundle validated at vintage {POST_12_VINTAGE} ({len(post_records or [])} records)")
    print("OK: 1 bundle rejected VINTAGE_UNRESOLVABLE")
    print(f"OK: self-test PASS ({passed}/{total}; failure limbs discriminate)")
    return 0


def check_package() -> int:
    try:
        manifest = _load(MANIFEST_PATH)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: INSTRUMENT_UNKNOWN: cannot load package manifest: {exc}")
        return 3

    declared = set(manifest.get("members", []))
    actual = {
        path.relative_to(PACKAGE_ROOT).as_posix()
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    missing = sorted(declared - actual)
    undeclared = sorted(actual - declared)
    if missing or undeclared:
        for path in missing:
            print(f"ERROR: manifest member missing from tree: {path}")
        for path in undeclared:
            print(f"ERROR: tree member absent from manifest: {path}")
        return 1
    print(f"OK: package manifest PASS ({len(actual)} member(s), exact set match)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run", nargs="*", type=Path)
    parser.add_argument("--require-proving-defect", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--check-package", action="store_true")
    parser.add_argument("--retrodiction-battery", type=Path)
    parser.add_argument("--compile-census-row", type=Path)
    parser.add_argument("--census-row-id")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if args.check_package:
        return check_package()
    if args.retrodiction_battery is not None:
        try:
            battery = _load(args.retrodiction_battery)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"ERROR: INSTRUMENT_UNKNOWN: cannot load retrodiction battery: {exc}")
            return 3
        errors = validate_retrodiction_battery(battery)
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            print(f"ERROR: retrodiction battery FAIL ({len(errors)} finding(s))")
            return 1
        print(f"OK: retrodiction battery PASS ({len(battery['specimens'])}/6 expressible)")
        return 0
    if args.compile_census_row is not None:
        if args.output is None:
            parser.error("--output is required with --compile-census-row")
        try:
            document = _load_structured(args.compile_census_row)
            row, document_vintage = _select_census_row(document, args.census_row_id)
            bundle = compile_census_row(row, document_vintage=document_vintage)
        except (OSError, json.JSONDecodeError, yaml.YAMLError, ValueError) as exc:
            print(f"ERROR: INSTRUMENT_UNKNOWN: cannot compile census row: {exc}")
            return 3
        errors = validate(bundle)
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8", newline="\n") as handle:
            json.dump(bundle, handle, indent=2, ensure_ascii=True)
            handle.write("\n")
        print(f"OK: census row compiled to {args.output}")
        return 0
    if not args.run:
        parser.error("run is required unless --self-test is used")

    partitions: Counter[tuple[str, int]] = Counter()
    unresolved = 0
    total_errors = 0
    for run_path in args.run:
        try:
            bundle = _load(run_path)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"ERROR: INSTRUMENT_UNKNOWN: cannot load {run_path}: {exc}", file=sys.stderr)
            return 3
        errors = validate(bundle, require_proving_defect=args.require_proving_defect)
        vintage, required, _ = _rule24_coverage_frame(bundle)
        if vintage and required is not None:
            partitions[(vintage, len(required))] += 1
        else:
            unresolved += 1
        if errors:
            for error in errors:
                print(f"ERROR: {run_path}: {error}")
            total_errors += len(errors)
    for (vintage, record_count), count in sorted(partitions.items()):
        noun = "bundle" if count == 1 else "bundles"
        print(f"OK: {count} {noun} validated at vintage {vintage} ({record_count} records)")
    if unresolved:
        print(f"ERROR: VINTAGE_UNRESOLVABLE: {unresolved} bundle(s)")
    if total_errors:
        print(f"ERROR: validation FAIL ({total_errors} finding(s) across {len(args.run)} bundle(s))")
        return 1
    print(f"OK: validation PASS ({len(args.run)}/{len(args.run)} bundle(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
