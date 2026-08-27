from __future__ import annotations

import copy
import json
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parent
SCHEMA = ROOT / "schemas" / "contract_audit.v1.schema.json"
DOCUMENT = ROOT / "contract_audit.v1.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def semantic_errors(document: dict) -> list[str]:
    errors: list[str] = []
    occurrences = document["enum_occurrence_audit"]
    occurrence_ids = [row["occurrence_id"] for row in occurrences]
    if occurrence_ids != [f"ENUM-{number:02d}" for number in range(1, 14)]:
        errors.append("enum occurrence audit must cover ENUM-01 through ENUM-13 exactly and in order")
    if len({row["schema_path"] for row in occurrences}) != 13:
        errors.append("enum occurrence schema paths must be unique")

    findings = document["concept_findings"]
    finding_ids = [row["finding_id"] for row in findings]
    if len(finding_ids) != len(set(finding_ids)):
        errors.append("concept finding ids must be unique")

    boundaries = {row["document_kind"]: row for row in document["contract_boundary"]}
    expected_kinds = {
        "substrate_entity_registry",
        "substrate_relation_card",
        "substrate_disposition_manifest",
        "substrate_coherence_run_manifest",
        "substrate_coherence_receipt",
    }
    if set(boundaries) != expected_kinds:
        errors.append("contract boundary must contain the five exact document kinds")
    receipt = boundaries.get("substrate_coherence_receipt")
    if receipt and receipt["authorship_mode"] != "machine_generated":
        errors.append("substrate coherence receipt must be machine generated")

    stages = document["compiled_process"]
    if [row["ordinal"] for row in stages] != list(range(1, len(stages) + 1)):
        errors.append("compiled process ordinals must be contiguous from one")
    if document["shared_root_changes"]["made"] is not False:
        errors.append("this proposal must not claim an operative shared-root change")
    if document["scope"]["cards_valid"] if "cards_valid" in document["scope"] else False:
        errors.append("validation results belong in baseline_validation, not scope")
    if document["naming_correction"] != {
        "semantic_invariant": "Rule 24",
        "execution_locality": "Rule 26",
        "prohibited_name": "Rule-26 coherence process",
    }:
        errors.append("Rule 24 and Rule 26 must retain their independent meanings")
    return errors


def validate(document: dict) -> list[str]:
    schema = load(SCHEMA)
    validator = jsonschema.Draft202012Validator(schema)
    errors = [
        f"schema {'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(document), key=lambda item: list(item.absolute_path))
    ]
    if not errors:
        errors.extend(semantic_errors(document))
    return errors


def main() -> int:
    document = load(DOCUMENT)
    errors = validate(document)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    mutants: list[tuple[str, dict]] = []
    missing_enum = copy.deepcopy(document)
    missing_enum["enum_occurrence_audit"].pop()
    mutants.append(("missing-enum-occurrence", missing_enum))

    duplicate_finding = copy.deepcopy(document)
    duplicate_finding["concept_findings"][1]["finding_id"] = duplicate_finding["concept_findings"][0]["finding_id"]
    mutants.append(("duplicate-finding-id", duplicate_finding))

    authored_receipt = copy.deepcopy(document)
    for row in authored_receipt["contract_boundary"]:
        if row["document_kind"] == "substrate_coherence_receipt":
            row["authorship_mode"] = "human_authored"
    mutants.append(("generated-receipt-masquerades-as-authored", authored_receipt))

    shared_change = copy.deepcopy(document)
    shared_change["shared_root_changes"]["made"] = True
    mutants.append(("proposal-claims-operative-root-change", shared_change))

    conflated_rules = copy.deepcopy(document)
    conflated_rules["naming_correction"]["semantic_invariant"] = "Rule 26"
    mutants.append(("rule24-rule26-conflation", conflated_rules))

    for name, mutant in mutants:
        if not validate(mutant):
            print(f"ERROR: mutant accepted: {name}")
            return 1
        print(f"PASS: mutant rejected: {name}")

    print("PASS: contract audit schema and semantic validation")
    print(f"PASS: negative controls {len(mutants)}/{len(mutants)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
