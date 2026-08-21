#!/usr/bin/env python3
"""Mint and evaluate local, expiring Discrimination_Certificate objects.

Source of record: docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md sec.2.2.
This implementation cites that shared object and does not widen its fields.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

import jsonschema


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = PACKAGE_ROOT / "schemas" / "discrimination_certificate.schema.json"
SOURCE_OF_RECORD = "docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md sec.2.2"


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode(
        "ascii"
    )


def digest(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(value)).hexdigest()


def certificate_id(certificate: dict[str, Any]) -> str:
    payload = copy.deepcopy(certificate)
    payload.pop("certificate_id", None)
    return "dc:" + digest(payload)


def _semantic_findings(
    certificate: dict[str, Any], current_coordinates: dict[str, str] | None = None
) -> tuple[str, list[str]]:
    unknown: list[str] = []
    invalid: list[str] = []
    expired: list[str] = []

    positive = certificate["isolated_positive_control"]
    negative = certificate["known_negative"]
    discrimination = certificate["observed_discrimination"]
    domain = certificate["shared_failure_domain"]
    crossings = certificate["independence_crossings"]

    if positive["execution_mode"] != "ISOLATED_FROM_TARGET":
        invalid.append("positive control was run against the target, not in isolation")
    if not positive["passed"]:
        invalid.append("isolated positive control did not pass")
    provenance = negative.get("generation_provenance")
    if not isinstance(provenance, dict) or provenance.get("kind") != "GENERATED":
        invalid.append("negative control lacks GENERATED provenance")
    elif provenance.get("artifact_digest") != digest(provenance.get("artifact")):
        invalid.append("generated-negative artifact digest does not match generated artifact")
    if not negative["passed"]:
        invalid.append("generated negative did not produce its expected contrast")
    if positive["observed"] == negative["observed"]:
        invalid.append("positive and generated-negative controls did not discriminate")
    if (
        not discrimination["passed"]
        or discrimination["contrasts_observed"] < discrimination["contrasts_required"]
    ):
        invalid.append("observed discrimination did not meet its declared denominator")

    instrument_dependencies = set(domain["instrument_dependencies"])
    control_dependencies = set(domain["control_dependencies"])
    actual_shared = instrument_dependencies & control_dependencies
    if set(domain["shared_dependencies"]) != actual_shared:
        invalid.append("declared shared dependencies do not equal the measured intersection")
    if domain["total_failure_shared"] or instrument_dependencies <= control_dependencies:
        invalid.append("instrument and controls share the instrument's total failure domain")
    if not any(row["demonstrated"] for row in crossings):
        invalid.append("no demonstrated independence crossing")
    for row in crossings:
        if row["demonstrated"] and row["instrument_side"] == row["control_side"]:
            invalid.append(f"crossing {row['cut']} does not cross a dependency cut")

    coordinates = current_coordinates or {}
    for predicate in certificate["invalidation_predicates"]:
        coordinate = predicate["coordinate"]
        if coordinate not in coordinates:
            unknown.append(f"current coordinate unavailable: {coordinate}")
        elif coordinates[coordinate] != predicate["attested_value"]:
            expired.append(
                f"{coordinate} changed from {predicate['attested_value']} to {coordinates[coordinate]}"
            )
    version = coordinates.get("instrument.version")
    if version is not None and version != certificate["instrument"]["version"]:
        expired.append(
            f"instrument.version changed from {certificate['instrument']['version']} to {version}"
        )

    if invalid:
        return "INVALID", invalid
    if expired:
        return "EXPIRED", expired
    if unknown:
        return "UNKNOWN", unknown
    return "VALID", []


def derive_outcome(
    certificate: dict[str, Any], current_coordinates: dict[str, str] | None = None
) -> tuple[str, list[str]]:
    """Derive one terminal. Failure to re-attest never preserves validity."""
    try:
        return _semantic_findings(certificate, current_coordinates)
    except (KeyError, TypeError, ValueError) as exc:
        return "UNKNOWN", [f"certificate operands unreadable: {exc}"]


def finalize_certificate(
    draft: dict[str, Any], current_coordinates: dict[str, str]
) -> dict[str, Any]:
    certificate = copy.deepcopy(draft)
    certificate["source_of_record"] = SOURCE_OF_RECORD
    certificate["attestation_outcome"] = "UNKNOWN"
    certificate["outcome_reasons"] = ["not yet derived"]
    certificate["certificate_id"] = "dc:sha256:" + ("0" * 64)
    outcome, reasons = derive_outcome(certificate, current_coordinates)
    certificate["attestation_outcome"] = outcome
    certificate["outcome_reasons"] = reasons
    certificate["certificate_id"] = certificate_id(certificate)
    return certificate


def validate_certificate(
    certificate: dict[str, Any], current_coordinates: dict[str, str] | None = None
) -> list[str]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    errors = [
        f"schema {'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(certificate), key=lambda item: list(item.absolute_path))
    ]
    if errors:
        return errors
    expected_id = certificate_id(certificate)
    if certificate["certificate_id"] != expected_id:
        errors.append("certificate_id does not match canonical certificate payload")
    expected_outcome, expected_reasons = derive_outcome(certificate, current_coordinates)
    if certificate["attestation_outcome"] != expected_outcome:
        errors.append(
            f"attestation_outcome={certificate['attestation_outcome']} but operands derive {expected_outcome}"
        )
    if certificate["outcome_reasons"] != expected_reasons:
        errors.append("outcome_reasons do not match derived findings")
    return errors


def certificate_ref(certificate: dict[str, Any]) -> str | None:
    return certificate["certificate_id"] if certificate["attestation_outcome"] == "VALID" else None
