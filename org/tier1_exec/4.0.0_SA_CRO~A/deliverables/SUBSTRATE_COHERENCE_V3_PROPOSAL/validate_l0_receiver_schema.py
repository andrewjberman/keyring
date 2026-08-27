#!/usr/bin/env python3
"""Adversarial controls for the L0 part-semantic receiver migration."""

from __future__ import annotations

import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[5]
SCHEMA_PATH = ROOT / "org/standards/L0_GRAPH_SUBSTRATE_MANIFEST.schema.json"
MANIFEST_PATH = ROOT / "org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_MANIFEST/graph_object_manifest.json"


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def receiver_document(manifest: dict, receiver: str, value: dict) -> dict:
    candidate = copy.deepcopy(manifest)
    candidate["parts"][0][receiver] = value
    return candidate


def rejected(validator: Draft202012Validator, document: dict) -> bool:
    return bool(list(validator.iter_errors(document)))


def enum_contract_errors(schema: dict) -> list[str]:
    errors: list[str] = []
    properties = schema["$defs"]["part"]["properties"]
    enum_paths = {
        "grain.claim_status": properties["grain"]["properties"]["claim_status"],
        "key.claim_status": properties["key"]["properties"]["claim_status"],
        "key.key_is_stable": properties["key"]["properties"]["key_is_stable"],
        "failure_mode.claim_status": properties["failure_mode"]["properties"]["claim_status"],
        "failure_mode.distinguishable_from_true_negative": properties["failure_mode"]["properties"]["distinguishable_from_true_negative"],
    }
    for path, node in enum_paths.items():
        if "x-rule24" not in node and "x-rule24-record-at" not in node:
            errors.append(f"{path}: missing Rule-24 record or reuse pointer")
            continue
        audit_text = json.dumps(
            {"description": node.get("description"), "x-rule24": node.get("x-rule24")},
            sort_keys=True,
        )
        for value in node["enum"]:
            if isinstance(value, str) and value not in audit_text:
                errors.append(f"{path}: value {value!r} has no schema-local semantics")
    return errors


def main() -> int:
    schema = load(SCHEMA_PATH)
    manifest = load(MANIFEST_PATH)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    failures: list[str] = []
    if rejected(validator, manifest):
        failures.append("current 42-part manifest rejected")

    unknown = {
        "grain": {
            "claim_status": "unknown", "unit": None, "basis": "absent",
            "evidence": "NONE -- exact subject-to-part relation absent", "owner": "UNOWNED",
        },
        "key": {
            "claim_status": "unknown", "identity_space": None, "key_expression": None,
            "key_is_stable": None, "crosses_spaces": None, "declared_mapping": None,
            "basis": "absent", "evidence": "NONE -- exact subject-to-part relation absent", "owner": "UNOWNED",
        },
        "failure_mode": {
            "claim_status": "unknown", "returns_on_failure": None,
            "distinguishable_from_true_negative": None, "silent_degrade_paths": None,
            "basis": "absent", "evidence": "NONE -- exact subject-to-part relation absent", "owner": "UNOWNED",
        },
    }
    declared = {
        "grain": {
            "claim_status": "declared", "unit": "manifest part member", "basis": "measured",
            "evidence": "fixture:declared-grain", "owner": "4.0.0_SA_CRO~A",
        },
        "key": {
            "claim_status": "declared", "identity_space": "part-local-id", "key_expression": "id",
            "key_is_stable": "stable", "crosses_spaces": False, "declared_mapping": None,
            "basis": "measured", "evidence": "fixture:declared-key", "owner": "4.0.0_SA_CRO~A",
        },
        "failure_mode": {
            "claim_status": "declared", "returns_on_failure": "raises",
            "distinguishable_from_true_negative": "yes", "silent_degrade_paths": [],
            "basis": "measured", "evidence": "fixture:declared-failure", "owner": "4.0.0_SA_CRO~A",
        },
    }

    for receiver, value in unknown.items():
        if rejected(validator, receiver_document(manifest, receiver, value)):
            failures.append(f"legal unknown {receiver} rejected")
    for receiver, value in declared.items():
        if rejected(validator, receiver_document(manifest, receiver, value)):
            failures.append(f"legal declared {receiver} rejected")

    payload_fields = {
        "grain": ["unit"],
        "key": ["identity_space", "key_expression", "key_is_stable", "crosses_spaces", "declared_mapping"],
        "failure_mode": ["returns_on_failure", "distinguishable_from_true_negative", "silent_degrade_paths"],
    }
    for receiver, fields in payload_fields.items():
        for field in fields:
            missing = copy.deepcopy(unknown[receiver])
            missing.pop(field)
            if not rejected(validator, receiver_document(manifest, receiver, missing)):
                failures.append(f"unknown {receiver} accepted omitted {field}")
        bad_basis = copy.deepcopy(unknown[receiver])
        bad_basis["basis"] = "measured"
        if not rejected(validator, receiver_document(manifest, receiver, bad_basis)):
            failures.append(f"unknown {receiver} accepted measured basis")

        absent_declared = copy.deepcopy(declared[receiver])
        absent_declared["basis"] = "absent"
        if not rejected(validator, receiver_document(manifest, receiver, absent_declared)):
            failures.append(f"declared {receiver} accepted absent basis")

        for metadata_field in ("evidence", "owner"):
            for invalid_value in (None, ""):
                bad_metadata = copy.deepcopy(declared[receiver])
                bad_metadata[metadata_field] = invalid_value
                if not rejected(validator, receiver_document(manifest, receiver, bad_metadata)):
                    failures.append(f"declared {receiver} accepted {metadata_field}={invalid_value!r}")

        extra = copy.deepcopy(declared[receiver])
        extra["undeclared_semantic"] = True
        if not rejected(validator, receiver_document(manifest, receiver, extra)):
            failures.append(f"declared {receiver} accepted additional property")

    declared_nulls = {
        "grain": ["unit"],
        "key": ["identity_space", "key_expression", "key_is_stable", "crosses_spaces"],
        "failure_mode": ["returns_on_failure", "distinguishable_from_true_negative", "silent_degrade_paths"],
    }
    for receiver, fields in declared_nulls.items():
        for field in fields:
            bad = copy.deepcopy(declared[receiver])
            bad[field] = None
            if not rejected(validator, receiver_document(manifest, receiver, bad)):
                failures.append(f"declared {receiver} accepted null {field}")

    failures.extend(enum_contract_errors(schema))
    descriptions = " ".join(
        schema["$defs"]["part"]["properties"][name].get("description", "")
        for name in ("grain", "key", "failure_mode")
    ).lower()
    for phrase in ("subject resource", "exact 1:1", "substring"):
        if phrase not in descriptions:
            failures.append(f"receiver contract does not state {phrase!r} boundary")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("PASS: L0 receiver schema compatibility and adversarial controls")
    print("PASS: declared/unknown presence, value, metadata, exact-closure, and Rule-24 enum controls")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
