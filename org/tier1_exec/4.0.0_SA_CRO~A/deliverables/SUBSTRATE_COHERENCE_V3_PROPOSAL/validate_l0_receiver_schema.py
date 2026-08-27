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


def resolve_local_ref(schema: dict, node: dict) -> dict:
    """Resolve the schema-local $defs references used by enum contracts."""
    ref = node.get("$ref")
    if ref is None:
        return node
    prefix = "#/$defs/"
    if not ref.startswith(prefix) or "/" in ref[len(prefix):]:
        raise ValueError(f"unsupported enum contract reference: {ref}")
    return schema["$defs"][ref[len(prefix):]]


def count_pattern(schema_fragment: object, pattern: str) -> int:
    if isinstance(schema_fragment, dict):
        own = int(schema_fragment.get("pattern") == pattern)
        return own + sum(count_pattern(value, pattern) for value in schema_fragment.values())
    if isinstance(schema_fragment, list):
        return sum(count_pattern(value, pattern) for value in schema_fragment)
    return 0


def enum_contract_errors(schema: dict) -> list[str]:
    errors: list[str] = []
    properties = schema["$defs"]["part"]["properties"]
    enum_paths = {
        "grain.claim_status": properties["grain"]["properties"]["claim_status"],
        "grain.basis": properties["grain"]["properties"]["basis"],
        "key.claim_status": properties["key"]["properties"]["claim_status"],
        "key.key_is_stable": properties["key"]["properties"]["key_is_stable"],
        "key.basis": properties["key"]["properties"]["basis"],
        "failure_mode.claim_status": properties["failure_mode"]["properties"]["claim_status"],
        "failure_mode.distinguishable_from_true_negative": properties["failure_mode"]["properties"]["distinguishable_from_true_negative"],
        "failure_mode.basis": properties["failure_mode"]["properties"]["basis"],
        "member_set.basis": properties["member_set"]["properties"]["basis"],
    }
    for path, node in enum_paths.items():
        try:
            contract = resolve_local_ref(schema, node)
        except (KeyError, ValueError) as exc:
            errors.append(f"{path}: unresolved enum contract reference: {exc}")
            continue
        if "x-rule24" not in contract and "x-rule24-record-at" not in contract:
            errors.append(f"{path}: missing Rule-24 record or reuse pointer")
            continue
        audit_text = json.dumps(
            {
                "description": node.get("description"),
                "x-enum-definitions": contract.get("x-enum-definitions"),
                "x-rule24": contract.get("x-rule24"),
            },
            sort_keys=True,
        )
        definitions = contract.get("x-enum-definitions", {})
        for value in contract["enum"]:
            if isinstance(value, str) and value not in audit_text:
                errors.append(f"{path}: value {value!r} has no schema-local semantics")
            if isinstance(value, str) and "$ref" in node and not isinstance(definitions.get(value), str):
                errors.append(f"{path}: value {value!r} lacks an x-enum-definitions entry")
            if value is None and "null_semantics" not in contract.get("x-rule24", {}):
                errors.append(f"{path}: admitted null lacks explicit structural-sentinel semantics")
    return errors


def main() -> int:
    schema = load(SCHEMA_PATH)
    manifest = load(MANIFEST_PATH)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    failures: list[str] = []
    if rejected(validator, manifest):
        failures.append("current 42-part manifest rejected")

    expected_held_unbuilt_parts = {
        "affinity_matrix",
        "identity_and_succession",
        "similarity_network_fusion",
    }
    unbuilt_parts = {part["id"]: part for part in manifest["parts"] if part["id"] in expected_held_unbuilt_parts}
    if set(unbuilt_parts) != expected_held_unbuilt_parts:
        failures.append("current manifest does not contain the exact three governed unbuilt parts")
    for part_id, part in unbuilt_parts.items():
        if part.get("basis") != "held":
            failures.append(f"live unbuilt part {part_id} does not use held basis")
        if part.get("home_space") != "none" or part.get("home") != "NONE":
            failures.append(f"live unbuilt part {part_id} does not carry home_space=none and home=NONE")
    absent_part = copy.deepcopy(manifest)
    absent_part["parts"][0]["basis"] = "absent"
    if not rejected(validator, absent_part):
        failures.append("production part accepted absent basis without an outer unknown claim")

    final_receiver_fields = {"home_space", "grain", "key", "failure_mode"}
    part_contract = schema["$defs"]["part"]
    missing_required = final_receiver_fields - set(part_contract["required"])
    if missing_required:
        failures.append(f"final part contract does not require {sorted(missing_required)}")
    missing_by_field = {
        field: [part["id"] for part in manifest["parts"] if field not in part]
        for field in sorted(final_receiver_fields)
    }
    for field, part_ids in missing_by_field.items():
        if part_ids:
            sample = part_ids[:5]
            failures.append(
                f"final manifest lacks {field} on {len(part_ids)} part(s); "
                f"sample={sample}"
            )
    if part_contract["properties"]["basis"].get("$ref") != "#/$defs/basis_present":
        failures.append("part.basis is not mechanically bound to basis_present")
    denominator_contract = schema["properties"]["denominator"]
    if "parts_registered" in manifest["denominator"]:
        failures.append("current manifest still carries retired parts_registered")
    if "parts_registered" in denominator_contract.get("properties", {}):
        failures.append("shared schema still admits retired parts_registered")

    legacy_denominator_phrases = (
        "3 are SET rows covering 14 member objects",
        "47 DISTINCT OBJECTS",
        "6-member SET row",
    )
    denominator_method = manifest["denominator"]["method"]
    for phrase in legacy_denominator_phrases:
        if phrase in denominator_method:
            failures.append(f"denominator method retains withdrawn population claim {phrase!r}")

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
            for invalid_value in (None, "", " ", "\t"):
                bad_metadata = copy.deepcopy(declared[receiver])
                bad_metadata[metadata_field] = invalid_value
                if not rejected(validator, receiver_document(manifest, receiver, bad_metadata)):
                    failures.append(f"declared {receiver} accepted {metadata_field}={invalid_value!r}")

                bad_unknown_metadata = copy.deepcopy(unknown[receiver])
                bad_unknown_metadata[metadata_field] = invalid_value
                if not rejected(validator, receiver_document(manifest, receiver, bad_unknown_metadata)):
                    failures.append(f"unknown {receiver} accepted {metadata_field}={invalid_value!r}")

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

    for invalid_mapping in (None, "", " ", "\t"):
        bad_cross_space_mapping = copy.deepcopy(declared["key"])
        bad_cross_space_mapping["crosses_spaces"] = True
        bad_cross_space_mapping["declared_mapping"] = invalid_mapping
        if not rejected(validator, receiver_document(manifest, "key", bad_cross_space_mapping)):
            failures.append(f"declared cross-space key accepted mapping={invalid_mapping!r}")
    for invalid_same_space_mapping in ("map", "", " "):
        bad_same_space_mapping = copy.deepcopy(declared["key"])
        bad_same_space_mapping["crosses_spaces"] = False
        bad_same_space_mapping["declared_mapping"] = invalid_same_space_mapping
        if not rejected(validator, receiver_document(manifest, "key", bad_same_space_mapping)):
            failures.append(f"declared same-space key accepted mapping={invalid_same_space_mapping!r}")

    for invalid_path in ("", " ", "\t"):
        bad_silent_path = copy.deepcopy(declared["failure_mode"])
        bad_silent_path["silent_degrade_paths"] = [invalid_path]
        if not rejected(validator, receiver_document(manifest, "failure_mode", bad_silent_path)):
            failures.append(f"declared failure mode accepted silent path={invalid_path!r}")

    legal_member_set = {
        "enumerable": True,
        "members": ["artifact:a", "artifact:b"],
        "basis": "measured",
        "evidence": "fixture:member-set",
        "owner": "4.0.0_SA_CRO~A",
    }
    if rejected(validator, receiver_document(manifest, "member_set", legal_member_set)):
        failures.append("legal two-member member_set rejected")
    legal_runtime_family = {
        "enumerable": False,
        "pattern": "artifact.tmp.<pid>.<monotonic_ns>.<counter>",
        "pattern_source_home": "producer.py",
        "pattern_source_line": 42,
        "variant_suffixes": {
            ".wal": {
                "mint": "unknown",
                "note": "write-ahead log companion",
            },
        },
        "variant_suffixes_completeness": "partial",
        "variant_suffixes_source_home": "producer.py",
        "variant_suffixes_source_line": 43,
        "basis": "measured",
        "evidence": "fixture:runtime-family",
        "owner": "4.0.0_SA_CRO~A",
    }
    if rejected(validator, receiver_document(manifest, "member_set", legal_runtime_family)):
        failures.append("legal runtime-pattern member_set rejected")
    member_set_mutants = {
        "one member": {**legal_member_set, "members": ["artifact:a"]},
        "absent basis": {**legal_member_set, "basis": "absent"},
        "whitespace evidence": {**legal_member_set, "evidence": " "},
        "whitespace owner": {**legal_member_set, "owner": "\t"},
        "empty members": {**legal_member_set, "members": []},
        "duplicate members": {**legal_member_set, "members": ["artifact:a", "artifact:a"]},
        "stored cardinality": {**legal_member_set, "cardinality": 2},
        "stored null cardinality": {**legal_runtime_family, "cardinality": None},
        "stored derivation": {**legal_member_set, "derivation": "length(members)"},
        "stored count": {**legal_member_set, "count": 2},
        "pattern in enumerable branch": {**legal_member_set, "pattern": "artifact.*", "pattern_source_home": "producer.py", "pattern_source_line": 42},
        "members in runtime branch": {**legal_runtime_family, "members": ["artifact:a", "artifact:b"]},
        "runtime absent basis": {**legal_runtime_family, "basis": "absent"},
        "runtime whitespace pattern": {**legal_runtime_family, "pattern": " "},
        "runtime mixed normalized and f-string pattern": {**legal_runtime_family, "pattern": "x.<pid>.{mono}"},
        "runtime whitespace source home": {**legal_runtime_family, "pattern_source_home": "\t"},
        "runtime embedded-space source home": {**legal_runtime_family, "pattern_source_home": "producer file.py"},
        "runtime trailing-LF source home": {**legal_runtime_family, "pattern_source_home": "producer.py\n"},
        "runtime trailing-CR source home": {**legal_runtime_family, "pattern_source_home": "producer.py\r"},
        "runtime trailing-CRLF source home": {**legal_runtime_family, "pattern_source_home": "producer.py\r\n"},
        "runtime S3 source home": {**legal_runtime_family, "pattern_source_home": "s3://bucket/producer.py"},
        "runtime HTTPS source home": {**legal_runtime_family, "pattern_source_home": "https://example/producer.py"},
        "runtime zero source line": {**legal_runtime_family, "pattern_source_line": 0},
        "runtime negative source line": {**legal_runtime_family, "pattern_source_line": -1},
        "runtime string source line": {**legal_runtime_family, "pattern_source_line": "42"},
        "runtime fractional source line": {**legal_runtime_family, "pattern_source_line": 1.5},
        "runtime compound source home": {**legal_runtime_family, "pattern_source_home": "_canonical.py:288"},
        "runtime suffix note trailing LF": {
            **legal_runtime_family,
            "variant_suffixes": {".wal": {"mint": "unknown", "note": "condition\n"}},
        },
        "runtime suffix note trailing CR": {
            **legal_runtime_family,
            "variant_suffixes": {".wal": {"mint": "unknown", "note": "condition\r"}},
        },
        "runtime suffix note line separator": {
            **legal_runtime_family,
            "variant_suffixes": {".wal": {"mint": "unknown", "note": "condition\u2028second"}},
        },
        "runtime conditional suffix without condition": {
            **legal_runtime_family,
            "variant_suffixes": {".wal": {"mint": "conditional", "note": "write-ahead log companion"}},
        },
        "runtime conditional suffix with unconditional evidence": {
            **legal_runtime_family,
            "variant_suffixes": {
                ".wal": {
                    "mint": "conditional",
                    "note": "write-ahead log companion",
                    "condition": "while an open transaction exists",
                    "evidence": "producer makes this unconditional",
                }
            },
        },
        "runtime unknown suffix with unconditional evidence": {
            **legal_runtime_family,
            "variant_suffixes": {
                ".wal": {
                    "mint": "unknown",
                    "note": "write-ahead log companion",
                    "evidence": "producer makes this unconditional",
                }
            },
        },
        "retired compound source": {**legal_runtime_family, "pattern_source": "producer.py:42"},
    }
    for mutant_name, mutant in member_set_mutants.items():
        if not rejected(validator, receiver_document(manifest, "member_set", mutant)):
            failures.append(f"member_set accepted {mutant_name}")
    for required_field in (
        "enumerable",
        "pattern",
        "pattern_source_home",
        "pattern_source_line",
        "variant_suffixes",
        "variant_suffixes_completeness",
        "variant_suffixes_source_home",
        "variant_suffixes_source_line",
        "basis",
        "evidence",
        "owner",
    ):
        missing = copy.deepcopy(legal_runtime_family)
        missing.pop(required_field)
        if not rejected(validator, receiver_document(manifest, "member_set", missing)):
            failures.append(f"runtime member_set accepted omitted {required_field}")
    variant_schema = schema["$defs"]["part"]["properties"]["member_set"]["properties"]["variant_suffixes"]
    for example_index, example in enumerate(variant_schema.get("examples", [])):
        example_member_set = copy.deepcopy(legal_runtime_family)
        example_member_set["variant_suffixes"] = example
        if rejected(validator, receiver_document(manifest, "member_set", example_member_set)):
            failures.append(f"variant_suffixes schema example {example_index} fails its own contract")

    for home_space in ("repo_path", "db_path"):
        https_home = copy.deepcopy(manifest)
        https_home["parts"][0]["home_space"] = home_space
        https_home["parts"][0]["home"] = "https://example/x"
        if not rejected(validator, https_home):
            failures.append(f"{home_space} accepted HTTPS URI home")
    uri_scheme_pattern = r"^[A-Za-z][A-Za-z0-9+.\-]*://"
    uri_scheme_authority_count = count_pattern(schema, uri_scheme_pattern)
    if uri_scheme_authority_count != 1:
        failures.append(
            "URI-scheme exclusion is not localized to one schema authority "
            f"(found {uri_scheme_authority_count})"
        )

    basis_drift_schema = copy.deepcopy(schema)
    basis_drift_schema["$defs"]["basis_present"]["enum"] = ["measured", "inferred"]
    basis_drift_schema["$defs"]["basis_present"]["x-enum-definitions"].pop("held")
    basis_drift_validator = Draft202012Validator(basis_drift_schema)
    for receiver, value in declared.items():
        held_value = copy.deepcopy(value)
        held_value["basis"] = "held"
        if not rejected(basis_drift_validator, receiver_document(manifest, receiver, held_value)):
            failures.append(f"declared {receiver} did not follow narrowed basis_present reference")
    held_member_set = copy.deepcopy(legal_member_set)
    held_member_set["basis"] = "held"
    if not rejected(basis_drift_validator, receiver_document(manifest, "member_set", held_member_set)):
        failures.append("member_set did not follow narrowed basis_present reference")

    failures.extend(enum_contract_errors(schema))
    rule24_mutants = {}
    missing_rule24 = copy.deepcopy(schema)
    missing_rule24["$defs"]["basis_full"].pop("x-rule24")
    rule24_mutants["basis_full without Rule-24 record"] = missing_rule24
    missing_definition = copy.deepcopy(schema)
    missing_definition["$defs"]["basis_full"]["x-enum-definitions"].pop("held")
    rule24_mutants["basis_full without held definition"] = missing_definition
    broken_ref = copy.deepcopy(schema)
    broken_ref["$defs"]["part"]["properties"]["member_set"]["properties"]["basis"]["$ref"] = "#/$defs/missing_basis"
    rule24_mutants["member_set with unresolved basis reference"] = broken_ref
    for mutant_name, mutant_schema in rule24_mutants.items():
        if not enum_contract_errors(mutant_schema):
            failures.append(f"Rule-24 audit accepted {mutant_name}")
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
    print(f"PASS: Rule-24 audit mutants rejected {len(rule24_mutants)}/{len(rule24_mutants)}")
    print("PASS: Base round-6 part-basis, address-space, and mechanical-drift controls")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
