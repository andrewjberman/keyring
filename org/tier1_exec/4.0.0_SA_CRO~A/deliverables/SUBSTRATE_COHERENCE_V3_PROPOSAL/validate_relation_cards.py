from __future__ import annotations

import copy
import json
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parent
SCHEMA = ROOT / "schemas" / "substrate_relation_card.v1.schema.json"
FIXTURE_ROOT = ROOT / "fixtures" / "relations"
FIXTURES = sorted(FIXTURE_ROOT.glob("*.json"))


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def claim_rows(document: dict) -> list[dict]:
    return list(document["state_claims"].values()) + list(document["standing_claims"].values())


def semantic_errors(document: dict) -> list[str]:
    errors: list[str] = []
    evidence_ids = [row["evidence_id"] for row in document["evidence"]]
    if len(evidence_ids) != len(set(evidence_ids)):
        errors.append("evidence ids must be unique within a relation card")
    evidence_set = set(evidence_ids)

    operation_ids = [row["operation_id"] for row in document["operations"]]
    if len(operation_ids) != len(set(operation_ids)):
        errors.append("operation ids must be unique within a relation card")
    claim_ids = [row["claim_id"] for row in claim_rows(document)]
    if len(claim_ids) != len(set(claim_ids)):
        errors.append("claim ids must be unique within a relation card")
    addressable = set(operation_ids) | set(claim_ids)

    for operation in document["operations"]:
        refs = set(operation["evidence_refs"])
        if not refs <= evidence_set:
            errors.append(f"{operation['operation_id']}: unresolved evidence reference")
        origin = operation["binding_origin"]
        trace = set(operation["binding_trace"])
        domain = operation["target_domain"]
        if origin == "runtime_input" and "runtime_argument" not in trace:
            errors.append(f"{operation['operation_id']}: runtime_input requires runtime_argument in binding trace")
        if domain == "open_runtime" and origin != "runtime_input":
            errors.append(f"{operation['operation_id']}: open_runtime target requires runtime_input origin")
        if origin == "allowlist_registry" and "allowlist_member" not in trace:
            errors.append(f"{operation['operation_id']}: allowlist_registry requires allowlist_member in binding trace")

    for claim in claim_rows(document):
        refs = set(claim["evidence_refs"])
        if not refs <= evidence_set:
            errors.append(f"{claim['claim_id']}: unresolved evidence reference")
        if claim["claim_status"] == "known":
            if claim["value"] is None or claim["basis_mode"] is None or not refs:
                errors.append(f"{claim['claim_id']}: known claim requires value, basis, and evidence")
        else:
            if claim["value"] is not None or claim["basis_mode"] is not None or refs:
                errors.append(f"{claim['claim_id']}: unknown claim must not masquerade as a valued or grounded claim")

    for evidence in document["evidence"]:
        targets = set(evidence["claim_ids"])
        if not targets <= addressable:
            errors.append(f"{evidence['evidence_id']}: evidence names an unknown operation or claim")

    actor_kind = document["actor_ref"]["registry_id"].split(":", 1)[0]
    artifact_kind = document["artifact_ref"]["registry_id"].split(":", 1)[0]
    if actor_kind != "actor" or artifact_kind != "artifact":
        errors.append("relation endpoints must resolve actor then artifact roles")
    return errors


def schema_errors(document: dict) -> list[str]:
    validator = jsonschema.Draft202012Validator(load(SCHEMA))
    return [
        f"schema {'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(document), key=lambda item: list(item.absolute_path))
    ]


def validate(document: dict) -> list[str]:
    errors = schema_errors(document)
    if not errors:
        errors.extend(semantic_errors(document))
    return errors


def population_errors(documents: list[dict]) -> list[str]:
    errors: list[str] = []
    relation_ids = [row["relation_id"] for row in documents]
    pairs = [(row["actor_ref"]["registry_id"], row["artifact_ref"]["registry_id"]) for row in documents]
    if len(relation_ids) != len(set(relation_ids)):
        errors.append("relation ids must be unique across the population")
    if len(pairs) != len(set(pairs)):
        errors.append("actor-artifact pairs must be unique across the population")

    expected = {
        "relation:derive_runner:graph_nodes",
        "relation:derive_runner:graph_edges",
        "relation:derive_runner:graph_contracts",
    }
    if set(relation_ids) != expected:
        errors.append("derive_runner fixture population must contain the three exact relations")
    by_id = {row["relation_id"]: row for row in documents}
    contracts = by_id.get("relation:derive_runner:graph_contracts")
    nodes = by_id.get("relation:derive_runner:graph_nodes")
    edges = by_id.get("relation:derive_runner:graph_edges")
    if contracts:
        effects = {row["effect_kind"] for row in contracts["operations"]}
        if effects != {"create_if_absent", "append"}:
            errors.append("graph_contracts must preserve create-if-absent and append as distinct effects")
        lifecycle = contracts["artifact_lifecycle"]
        if lifecycle["mutation_policy"] != "append_only" or lifecycle["authorship_mode"] != "mixed_origin":
            errors.append("graph_contracts must preserve append-only mixed-origin lifecycle")
    for row in (nodes, edges):
        if row and row["artifact_lifecycle"]["mutation_policy"] != "whole_document_replace":
            errors.append(f"{row['relation_id']}: graph table lifecycle must remain whole_document_replace")
    return errors


def main() -> int:
    schema = load(SCHEMA)
    jsonschema.Draft202012Validator.check_schema(schema)
    documents = [load(path) for path in FIXTURES]
    for path, document in zip(FIXTURES, documents):
        errors = validate(document)
        if errors:
            for error in errors:
                print(f"ERROR: {path}: {error}")
            return 1
        print(f"PASS: fixture {path.name}")
    errors = population_errors(documents)
    if errors:
        for error in errors:
            print(f"ERROR: population: {error}")
        return 1

    base = documents[0]
    mutants: list[tuple[str, dict, bool]] = []

    mixed_artifacts = copy.deepcopy(base)
    mixed_artifacts["artifact_ref"] = [mixed_artifacts["artifact_ref"], {"registry_id": "artifact:graph_edges"}]
    mutants.append(("multiple-artifacts-in-one-relation", mixed_artifacts, False))

    file_standing = copy.deepcopy(base)
    file_standing["materializer_standing"] = "canonical"
    mutants.append(("file-level-materializer-standing", file_standing, False))

    unknown_as_value = copy.deepcopy(base)
    unknown_as_value["state_claims"]["desired"]["value"] = "unknown"
    mutants.append(("unknown-inside-value-domain", unknown_as_value, False))

    known_without_evidence = copy.deepcopy(base)
    known_without_evidence["state_claims"]["applied"]["evidence_refs"] = []
    mutants.append(("known-claim-without-evidence", known_without_evidence, False))

    parameter_as_origin = copy.deepcopy(base)
    parameter_as_origin["operations"][0]["binding_origin"] = "function_parameter"
    mutants.append(("function-parameter-as-origin", parameter_as_origin, False))

    open_without_runtime = copy.deepcopy(base)
    open_without_runtime["operations"][0]["target_domain"] = "open_runtime"
    mutants.append(("open-target-without-runtime-origin", open_without_runtime, False))

    disposition_inside_card = copy.deepcopy(base)
    disposition_inside_card["forward_disposition"] = {"standing": "keep"}
    mutants.append(("disposition-inside-relation-card", disposition_inside_card, False))

    unknown_with_basis = copy.deepcopy(base)
    unknown_with_basis["state_claims"]["exercised"]["basis_mode"] = "derived"
    mutants.append(("unknown-claim-with-basis", unknown_with_basis, False))

    unresolved_evidence = copy.deepcopy(base)
    unresolved_evidence["operations"][0]["evidence_refs"] = ["evidence:missing"]
    mutants.append(("unresolved-evidence-ref", unresolved_evidence, False))

    authored_artifact_projection = copy.deepcopy(base)
    authored_artifact_projection["artifact_lifecycle"]["authorship_mode"] = "human_authored"
    authored_artifact_projection["artifact_lifecycle"]["authority_role"] = "authoritative_source"
    mutants.append(("lifecycle-change-is-schema-valid-not-universally-invalid", authored_artifact_projection, True))

    for name, mutant, should_pass in mutants:
        passed = not validate(mutant)
        if passed != should_pass:
            print(f"ERROR: mutant {name} expected pass={should_pass} got pass={passed}")
            return 1
        print(f"PASS: mutant {'accepted as independent axes' if should_pass else 'rejected'}: {name}")

    duplicate = copy.deepcopy(documents)
    duplicate.append(copy.deepcopy(documents[0]))
    if not population_errors(duplicate):
        print("ERROR: duplicate actor-artifact population mutant accepted")
        return 1
    print("PASS: population mutant rejected: duplicate actor-artifact pair")
    print("PASS: substrate relation card schema and semantic validation")
    print("PASS: negative and independence controls 11/11")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
