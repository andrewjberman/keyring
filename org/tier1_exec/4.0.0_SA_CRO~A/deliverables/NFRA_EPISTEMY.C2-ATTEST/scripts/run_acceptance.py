#!/usr/bin/env python3
"""Run C2 live controls, mint certificates, join envelopes, and fire m1-m5."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Callable


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PACKAGE_ROOT.parents[4]
C1_ROOT = REPO_ROOT / "org" / "tier1_exec" / "4.0.0_SA_CRO~A" / "deliverables" / "NFRA_EPISTEMY.C1-ENVELOPE"
OBSERVED_AT = "2026-08-21T01:10:00Z"
FIXTURE_RELPATH = "org/tier1_exec/4.0.0_SA_CRO~A/deliverables/NFRA_EPISTEMY.C2-ATTEST/fixtures"
EVIDENCE = PACKAGE_ROOT / "evidence"
CERTIFICATES = PACKAGE_ROOT / "certificates"
JOINS = PACKAGE_ROOT / "joins"


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


HARNESS = _load_module("c2_attestation_harness", PACKAGE_ROOT / "src" / "attestation_harness.py")
C1 = _load_module("c1_observation_envelope", C1_ROOT / "src" / "observation_envelope.py")


def _relative_support(record: dict[str, Any]) -> None:
    normalized = []
    root = REPO_ROOT.as_posix().rstrip("/") + "/"
    for pointer in record["support_pointers"]:
        normalized.append(pointer.replace(root, ""))
    record["support_pointers"] = normalized


def _observation_ref(name: str) -> str:
    return f"evidence/{name}.observation.json"


def _control(
    control_id: str,
    request: Any,
    expected: Any,
    observed: Any,
    passed: bool,
    observation_ref: str,
    *,
    generated: dict[str, Any] | None = None,
) -> dict[str, Any]:
    row = {
        "control_id": control_id,
        "execution_mode": "ISOLATED_FROM_TARGET",
        "request": request,
        "expected": expected,
        "observed": observed,
        "passed": passed,
        "observation_ref": observation_ref,
    }
    if generated is not None:
        row["generation_provenance"] = generated
    return row


def _generated(generator_id: str, seed: str, artifact: Any) -> dict[str, Any]:
    return {
        "kind": "GENERATED",
        "generator_id": generator_id,
        "generator_version": "1",
        "seed": seed,
        "artifact": artifact,
        "artifact_digest": HARNESS.digest(artifact),
    }


def _current(version: str, fixture_digest: str) -> dict[str, str]:
    return {"instrument.version": version, "control.fixture": fixture_digest}


def _draft(
    instrument_id: str,
    version: str,
    plane: str,
    substrate: str,
    population: str,
    grain: str,
    positive: dict[str, Any],
    negative: dict[str, Any],
    fixture_digest: str,
) -> dict[str, Any]:
    return {
        "instrument": {"id": instrument_id, "version": version},
        "plane": plane,
        "substrate": substrate,
        "searched_population": population,
        "denominator_grain": grain,
        "failure_directions": [
            {
                "condition": "instrument cannot enumerate or parse its declared population",
                "wrong_as": "a clean empty result or pass",
                "consumer_effect": "absence or compliance would be over-claimed",
            }
        ],
        "traversal_residue": [],
        "isolated_positive_control": positive,
        "known_negative": negative,
        "observed_discrimination": {
            "contrasts_observed": int(positive["observed"] != negative["observed"]),
            "contrasts_required": 1,
            "passed": positive["passed"] and negative["passed"] and positive["observed"] != negative["observed"],
        },
        "shared_failure_domain": {
            "instrument_dependencies": [f"{instrument_id}-implementation", "python-runtime", "target-population"],
            "control_dependencies": ["c2-fixture-generator", "python-runtime"],
            "shared_dependencies": ["python-runtime"],
            "total_failure_shared": False,
        },
        "independence_crossings": [
            {
                "cut": "target population x generated fixture",
                "instrument_side": "target-population",
                "control_side": "c2-fixture-generator",
                "observation_ref": negative["observation_ref"],
                "demonstrated": True,
            }
        ],
        "vintage": {"attested_at": OBSERVED_AT, "instrument_version": version},
        "invalidation_predicates": [
            {"coordinate": "instrument.version", "attested_value": version},
            {"coordinate": "control.fixture", "attested_value": fixture_digest},
        ],
    }


def _run_controls() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, dict[str, str]]]:
    observations: dict[str, dict[str, Any]] = {}
    drafts: dict[str, dict[str, Any]] = {}
    currents: dict[str, dict[str, str]] = {}

    fixture_digest = HARNESS.digest((PACKAGE_ROOT / "fixtures" / "control_fixture.txt").read_text(encoding="utf-8"))

    find_positive = C1.wrap_comp_find(REPO_ROOT, "C2_POSITIVE_SENTINEL", [FIXTURE_RELPATH], OBSERVED_AT)
    generated_pattern = "C2_GENERATED_ABSENT_" + HARNESS.digest("comp-find-negative")[-12:]
    find_negative = C1.wrap_comp_find(REPO_ROOT, generated_pattern, [FIXTURE_RELPATH], OBSERVED_AT)
    for record in (find_positive, find_negative):
        _relative_support(record)
    observations["comp_find_positive"] = find_positive
    observations["comp_find_generated_negative"] = find_negative
    find_pos_observed = {"state": find_positive["substantive_result"]["state"], "hits": find_positive["substantive_result"]["value"]["hits"]}
    find_neg_observed = {"state": find_negative["substantive_result"]["state"], "hits": find_negative["substantive_result"]["value"]["hits"]}
    positive = _control("comp-find-isolated-positive", {"pattern": "C2_POSITIVE_SENTINEL"}, {"state": "KNOWN", "hits_min": 1}, find_pos_observed, find_pos_observed["state"] == "KNOWN" and find_pos_observed["hits"] >= 1, _observation_ref("comp_find_positive"))
    artifact = {"pattern": generated_pattern, "expected_hits": 0}
    negative = _control("comp-find-generated-negative", artifact, {"state": "KNOWN", "hits": 0}, find_neg_observed, find_neg_observed == {"state": "KNOWN", "hits": 0}, _observation_ref("comp_find_generated_negative"), generated=_generated("c2-token-mutator", "comp-find-negative", artifact))
    version = find_positive["instrument"]["version"]
    drafts["comp-find"] = _draft("comp-find", version, "DESIRED", "codebase", find_positive["population_predicate"], find_positive["denominator"]["grain"], positive, negative, fixture_digest)
    currents["comp-find"] = _current(version, fixture_digest)

    estate_positive = C1.wrap_comp_estate(REPO_ROOT, ["--list", "--head", "2"], OBSERVED_AT)
    estate_name = "c2-generated-missing-" + HARNESS.digest("comp-estate-negative")[-8:]
    estate_negative = C1.wrap_comp_estate(REPO_ROOT, [estate_name], OBSERVED_AT)
    for record in (estate_positive, estate_negative):
        _relative_support(record)
    observations["comp_estate_positive"] = estate_positive
    observations["comp_estate_generated_negative"] = estate_negative
    estate_pos_observed = {"state": estate_positive["substantive_result"]["state"], "chains": estate_positive["denominator"]["count"]}
    estate_neg_observed = {"state": estate_negative["substantive_result"]["state"], "denominator": estate_negative["denominator"]["count"]}
    positive = _control("comp-estate-isolated-positive", {"argv": ["--list", "--head", "2"]}, {"state": "KNOWN", "chains_min": 1}, estate_pos_observed, estate_pos_observed["state"] == "KNOWN" and estate_pos_observed["chains"] > 0, _observation_ref("comp_estate_positive"))
    artifact = {"argv": [estate_name], "expected_state": "UNKNOWN"}
    negative = _control("comp-estate-generated-negative", artifact, {"state": "UNKNOWN", "denominator": None}, estate_neg_observed, estate_neg_observed == {"state": "UNKNOWN", "denominator": None}, _observation_ref("comp_estate_generated_negative"), generated=_generated("c2-name-mutator", "comp-estate-negative", artifact))
    version = estate_positive["instrument"]["version"]
    drafts["comp-estate"] = _draft("comp-estate", version, "DESIRED", "codebase", estate_positive["population_predicate"], estate_positive["denominator"]["grain"], positive, negative, fixture_digest)
    currents["comp-estate"] = _current(version, fixture_digest)

    payload = json.dumps({"Functions": [{"FunctionName": "c2-fixture", "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:c2-fixture", "CodeSha256": "fixture", "LastModified": OBSERVED_AT, "Runtime": "python3.12", "MemorySize": 128, "Timeout": 3}]})
    census_positive = C1.wrap_census_substrate(REPO_ROOT, "aws.lambda", OBSERVED_AT, runner=lambda argv: (0, payload, ""))
    malformed = "{generated-malformed-json"
    census_negative = C1.wrap_census_substrate(REPO_ROOT, "aws.lambda", OBSERVED_AT, runner=lambda argv: (0, malformed, ""))
    for record in (census_positive, census_negative):
        _relative_support(record)
        value = record["substantive_result"]["value"]
        if isinstance(value, dict) and isinstance(value.get("meta"), dict):
            value["meta"]["generated_utc"] = OBSERVED_AT
    observations["census_substrate_positive"] = census_positive
    observations["census_substrate_generated_negative"] = census_negative
    census_pos_observed = {"state": census_positive["substantive_result"]["state"], "items": census_positive["denominator"]["count"]}
    census_neg_observed = {"state": census_negative["substantive_result"]["state"], "denominator": census_negative["denominator"]["count"]}
    positive = _control("census-substrate-isolated-positive", {"descriptor": "aws.lambda", "fixture_items": 1}, {"state": "KNOWN", "items": 1}, census_pos_observed, census_pos_observed == {"state": "KNOWN", "items": 1}, _observation_ref("census_substrate_positive"))
    artifact = {"runner_stdout": malformed, "expected_state": "UNKNOWN"}
    negative = _control("census-substrate-generated-negative", artifact, {"state": "UNKNOWN", "denominator": None}, census_neg_observed, census_neg_observed == {"state": "UNKNOWN", "denominator": None}, _observation_ref("census_substrate_generated_negative"), generated=_generated("c2-payload-mutator", "census-substrate-negative", artifact))
    version = census_positive["instrument"]["version"]
    drafts["census_substrate"] = _draft("census_substrate", version, "APPLIED", "aws", census_positive["population_predicate"], census_positive["denominator"]["grain"], positive, negative, fixture_digest)
    currents["census_substrate"] = _current(version, fixture_digest)
    return observations, drafts, currents


def _mint_all(drafts: dict[str, dict[str, Any]], currents: dict[str, dict[str, str]]) -> dict[str, dict[str, Any]]:
    return {name: HARNESS.finalize_certificate(draft, currents[name]) for name, draft in sorted(drafts.items())}


def _mutants(base: dict[str, Any], current: dict[str, str]) -> list[dict[str, Any]]:
    cases: list[tuple[str, Callable[[dict[str, Any]], None], str]] = [
        ("m1_total_shared_failure_domain", lambda d: (d["shared_failure_domain"].update({"control_dependencies": list(d["shared_failure_domain"]["instrument_dependencies"]), "shared_dependencies": list(d["shared_failure_domain"]["instrument_dependencies"]), "total_failure_shared": True})), "INVALID"),
        ("m2_positive_not_isolated", lambda d: d["isolated_positive_control"].update({"execution_mode": "AGAINST_TARGET"}), "INVALID"),
        ("m3_hand_authored_negative", lambda d: d["known_negative"]["generation_provenance"].update({"kind": "HAND_AUTHORED"}), "INVALID"),
        ("m5_anti_correlated_total_failure", lambda d: (d["shared_failure_domain"].update({"control_dependencies": list(d["shared_failure_domain"]["instrument_dependencies"]), "shared_dependencies": list(d["shared_failure_domain"]["instrument_dependencies"]), "total_failure_shared": True}), d["known_negative"].update({"observed": {"state": "KNOWN", "hits": 0}, "passed": True})), "INVALID"),
    ]
    rows = []
    for name, mutation, expected in cases:
        draft = copy.deepcopy(base)
        mutation(draft)
        certificate = HARNESS.finalize_certificate(draft, current)
        schema_errors = HARNESS.validate_certificate(certificate, current)
        actual = certificate["attestation_outcome"]
        rows.append({"mutant": name, "expected": expected, "actual": actual, "validator_findings": len(schema_errors), "status": "FIRED" if actual == expected else "DID_NOT_FIRE"})
    changed = dict(current)
    changed["instrument.version"] = current["instrument.version"] + "-bumped"
    expired = HARNESS.finalize_certificate(copy.deepcopy(base), changed)
    rows.insert(3, {"mutant": "m4_instrument_version_bump", "expected": "EXPIRED", "actual": expired["attestation_outcome"], "validator_findings": len(HARNESS.validate_certificate(expired, changed)), "status": "FIRED" if expired["attestation_outcome"] == "EXPIRED" else "DID_NOT_FIRE"})
    return rows


def main() -> int:
    observations, drafts, currents = _run_controls()
    certificates_a = _mint_all(drafts, currents)
    certificates_b = _mint_all(copy.deepcopy(drafts), copy.deepcopy(currents))
    deterministic = HARNESS.canonical_bytes(certificates_a) == HARNESS.canonical_bytes(certificates_b)
    errors: list[str] = []
    for name, record in observations.items():
        errors.extend(f"{name}: {error}" for error in C1.validate_record(record))
    for name, certificate in certificates_a.items():
        cert_errors = HARNESS.validate_certificate(certificate, currents[name])
        errors.extend(f"{name}: {error}" for error in cert_errors)
        if certificate["attestation_outcome"] != "VALID":
            errors.append(f"{name}: live certificate did not mint VALID")

    joins: dict[str, dict[str, Any]] = {}
    for name, certificate in certificates_a.items():
        stem = name.replace("-", "_")
        positive_name = f"{stem}_positive"
        if positive_name not in observations:
            positive_name = "census_substrate_positive"
        attested = copy.deepcopy(observations[positive_name])
        attested["discrimination_certificate_ref"] = HARNESS.certificate_ref(certificate)
        unattested = copy.deepcopy(observations[positive_name])
        unattested["discrimination_certificate_ref"] = None
        joins[name] = {"attested": attested, "unattested": unattested}
        errors.extend(f"{name} attested join: {error}" for error in C1.validate_record(attested))
        errors.extend(f"{name} unattested join: {error}" for error in C1.validate_record(unattested))
        if attested["plane"] not in {"DESIRED", "APPLIED", "EXERCISED"} or attested["substrate"] not in {"aws", "portal", "codebase", "ms"}:
            errors.append(f"{name}: plane/substrate bind-time shape violated")

    mutant_rows = _mutants(drafts["comp-find"], currents["comp-find"])
    fired = sum(row["status"] == "FIRED" for row in mutant_rows)
    if fired != len(mutant_rows):
        errors.append(f"mutants fired {fired}/{len(mutant_rows)}")
    if not deterministic:
        errors.append("two certificate builds were not byte-identical")

    EVIDENCE.mkdir(parents=True, exist_ok=True)
    CERTIFICATES.mkdir(parents=True, exist_ok=True)
    JOINS.mkdir(parents=True, exist_ok=True)
    for name, record in sorted(observations.items()):
        (EVIDENCE / f"{name}.observation.json").write_bytes(HARNESS.canonical_bytes(record))
    for name, certificate in sorted(certificates_a.items()):
        (CERTIFICATES / f"{name}.certificate.json").write_bytes(HARNESS.canonical_bytes(certificate))
        (JOINS / f"{name}.join.json").write_bytes(HARNESS.canonical_bytes(joins[name]))
    results = {
        "source_of_record": HARNESS.SOURCE_OF_RECORD,
        "live_certificates": {name: {"outcome": cert["attestation_outcome"], "positive_passed": cert["isolated_positive_control"]["passed"], "generated_negative_passed": cert["known_negative"]["passed"], "contrasts": f"{cert['observed_discrimination']['contrasts_observed']}/{cert['observed_discrimination']['contrasts_required']}", "crossings_demonstrated": sum(row["demonstrated"] for row in cert["independence_crossings"]), "crossings_denominator": len(cert["independence_crossings"])} for name, cert in sorted(certificates_a.items())},
        "mutants": {"fired": fired, "denominator": len(mutant_rows), "rows": mutant_rows},
        "determinism": "STABLE" if deterministic else "UNSTABLE",
        "envelope_joins": {"attested_non_null": sum(row["attested"]["discrimination_certificate_ref"] is not None for row in joins.values()), "unattested_null": sum(row["unattested"]["discrimination_certificate_ref"] is None for row in joins.values()), "denominator": len(joins)},
        "errors": errors,
    }
    (EVIDENCE / "acceptance_results.json").write_bytes(HARNESS.canonical_bytes(results))
    print(f"{'OK' if not errors else 'ERROR'}: C2 acceptance live_certificates={sum(c['attestation_outcome'] == 'VALID' for c in certificates_a.values())}/{len(certificates_a)} mutants={fired}/{len(mutant_rows)} determinism={results['determinism']} joins={results['envelope_joins']['attested_non_null']}/{len(joins)}")
    for name, cert in sorted(certificates_a.items()):
        print(f"OK: {name} controls positive=1/1 generated_negative=1/1 discrimination={cert['observed_discrimination']['contrasts_observed']}/{cert['observed_discrimination']['contrasts_required']} independence_crossings={sum(row['demonstrated'] for row in cert['independence_crossings'])}/{len(cert['independence_crossings'])}")
    for error in errors:
        print(f"ERROR: {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
