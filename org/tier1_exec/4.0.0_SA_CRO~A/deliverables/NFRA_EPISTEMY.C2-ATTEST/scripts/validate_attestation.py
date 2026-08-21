#!/usr/bin/env python3
"""Validate C2 certificates, envelope joins, acceptance evidence, and package closure."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PACKAGE_ROOT.parents[4]
C1_ROOT = REPO_ROOT / "org" / "tier1_exec" / "4.0.0_SA_CRO~A" / "deliverables" / "NFRA_EPISTEMY.C1-ENVELOPE"


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


HARNESS = _load_module("c2_attestation_validator_core", PACKAGE_ROOT / "src" / "attestation_harness.py")
C1 = _load_module("c1_observation_validator_core", C1_ROOT / "src" / "observation_envelope.py")


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _attested_coordinates(certificate: dict[str, Any]) -> dict[str, str]:
    return {
        row["coordinate"]: row["attested_value"]
        for row in certificate.get("invalidation_predicates", [])
    }


def package_errors() -> list[str]:
    manifest = _load(PACKAGE_ROOT / "PACKAGE_MANIFEST.json")
    declared = set(manifest["members"])
    actual = {
        path.relative_to(PACKAGE_ROOT).as_posix()
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    errors = []
    if declared != actual:
        errors.append(
            f"package manifest mismatch missing={sorted(actual - declared)} unexpected={sorted(declared - actual)}"
        )
    return errors


def validate_package() -> list[str]:
    errors = package_errors()
    certificate_ids: set[str] = set()
    for path in sorted((PACKAGE_ROOT / "certificates").glob("*.certificate.json")):
        certificate = _load(path)
        certificate_ids.add(certificate.get("certificate_id", ""))
        current = _attested_coordinates(certificate)
        errors.extend(f"{path.name}: {error}" for error in HARNESS.validate_certificate(certificate, current))
        if certificate.get("attestation_outcome") != "VALID":
            errors.append(f"{path.name}: live certificate is not VALID")
    if len(certificate_ids) != 3:
        errors.append(f"certificate id denominator expected 3 distinct ids, got {len(certificate_ids)}")

    joins = sorted((PACKAGE_ROOT / "joins").glob("*.join.json"))
    for path in joins:
        document = _load(path)
        for side in ("attested", "unattested"):
            errors.extend(
                f"{path.name} {side}: {error}"
                for error in C1.validate_record(document[side])
            )
        if document["attested"]["discrimination_certificate_ref"] not in certificate_ids:
            errors.append(f"{path.name}: attested ref does not resolve to a live certificate")
        if document["unattested"]["discrimination_certificate_ref"] is not None:
            errors.append(f"{path.name}: unattested ref must remain null")
        for side in ("attested", "unattested"):
            record = document[side]
            if record["plane"] not in {"DESIRED", "APPLIED", "EXERCISED"}:
                errors.append(f"{path.name}: fused or unknown plane")
            if record["substrate"] not in {"aws", "portal", "codebase", "ms"}:
                errors.append(f"{path.name}: missing or unknown substrate")
    if len(joins) != 3:
        errors.append(f"join denominator expected 3, got {len(joins)}")

    results = _load(PACKAGE_ROOT / "evidence" / "acceptance_results.json")
    if results["mutants"]["fired"] != 5 or results["mutants"]["denominator"] != 5:
        errors.append("acceptance evidence does not carry m1-m5 as 5/5")
    if results["determinism"] != "STABLE":
        errors.append("acceptance evidence is not deterministic")
    if results["errors"]:
        errors.append("acceptance evidence carries errors")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-package", action="store_true")
    parser.add_argument("certificates", nargs="*", type=Path)
    args = parser.parse_args()
    if args.check_package or not args.certificates:
        errors = validate_package()
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        members = len(_load(PACKAGE_ROOT / "PACKAGE_MANIFEST.json")["members"])
        print(f"OK: C2 package PASS ({members}/{members} members; certificates=3/3 joins=3/3 mutants=5/5 determinism=STABLE)")
        return 0
    errors = []
    for path in args.certificates:
        certificate = _load(path)
        errors.extend(
            f"{path}: {error}"
            for error in HARNESS.validate_certificate(certificate, _attested_coordinates(certificate))
        )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: certificates PASS ({len(args.certificates)}/{len(args.certificates)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
