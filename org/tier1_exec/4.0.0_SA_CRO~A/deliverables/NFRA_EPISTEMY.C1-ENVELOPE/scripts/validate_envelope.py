#!/usr/bin/env python3
"""Validate Observation_Record envelopes and this package boundary."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT / "src"))
from observation_envelope import build_record, canonical_bytes, validate_record  # noqa: E402


def self_test() -> int:
    common = dict(
        instrument_id="control",
        instrument_version="v1",
        request={"q": "control"},
        plane="DESIRED",
        substrate="codebase",
        population_predicate="one planted control",
        denominator_count=1,
        denominator_grain="control",
        denominator_process="fixed one-member fixture",
        observed_at="2026-08-20T20:40:00Z",
        support_pointers=["control@v1"],
        substantive_value=0,
        unknown_reason="planted failure",
    )
    known = build_record(
        **common,
        status={"acquisition": "PRESENT", "transport": "SUCCEEDED", "enumeration": "SUCCEEDED", "parse": "SUCCEEDED"},
    )
    unknown = build_record(
        **common,
        status={"acquisition": "FAILED", "transport": "NOT_ATTEMPTED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"},
    )
    cases = [("known-zero", known, True), ("failed-forces-unknown", unknown, True)]
    contaminated = copy.deepcopy(unknown)
    contaminated["substantive_result"] = {"state": "KNOWN", "value": 0, "reason": None}
    cases.append(("failed-cannot-be-zero", contaminated, False))
    fused_axes = copy.deepcopy(known)
    fused_axes["plane"] = "DESIRED_REPOSITORY"
    fused_axes.pop("substrate")
    cases.append(("plane-substrate-fusion-rejected", fused_axes, False))
    passed = 0
    for name, record, should_pass in cases:
        actual = not validate_record(record)
        if actual != should_pass:
            print(f"ERROR: {name} expected {should_pass} got {actual}")
            return 1
        passed += 1
    if canonical_bytes(unknown) != canonical_bytes(copy.deepcopy(unknown)):
        print("ERROR: deterministic serialization control failed")
        return 1
    passed += 1
    print(f"OK: envelope self-test PASS ({passed}/5; false-clean and fused-axis limbs discriminate)")
    return 0


def check_package() -> int:
    manifest_path = PACKAGE_ROOT / "PACKAGE_MANIFEST.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot load package manifest: {exc}")
        return 3
    declared = set(manifest.get("members", []))
    actual = {
        path.relative_to(PACKAGE_ROOT).as_posix()
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    if declared != actual:
        for path in sorted(declared - actual):
            print(f"ERROR: manifest member missing: {path}")
        for path in sorted(actual - declared):
            print(f"ERROR: undeclared package file: {path}")
        return 1
    print(f"OK: package manifest PASS ({len(actual)} member(s), exact set match)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--check-package", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if args.check_package:
        return check_package()
    if args.record is None:
        parser.error("record is required unless --self-test or --check-package is used")
    try:
        record = json.loads(args.record.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot load record: {exc}")
        return 3
    errors = validate_record(record)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"ERROR: validation FAIL ({len(errors)} finding(s))")
        return 1
    print("OK: Observation_Record validation PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
