#!/usr/bin/env python3
"""proof-of-spec-check -- validate a PROOF_OF_SPEC instance against the canonical schema.

Andrew-direct 2026-08-11 ~0815Z: build TOs carry machine-readable JSON deliverable
expectations the Tier-2 assignee fills to PROVE work was done to spec. This is the
mechanical gate: a TO is not complete until its instance passes here.

Usage: proof-of-spec-check <instance.json> [expected_criterion_ids]
  expected_criterion_ids: comma-separated list OR a path to a file (one id per line) --
  the TO's embedded criterion set. When given, COVERAGE is checked BEFORE quality:
  an instance valid on every row it carries can still silently OMIT a criterion
  (the row-quality/row-coverage split -- CVO's step-zero, mechanized). Missing or
  extra criteria are violations, with both denominators printed.
Exit 0 = VALID. Exit 1 = INVALID (every violation printed). Exit 2 = usage/read error.

Layered: jsonschema (if installed) for structure, then the conditional rules the
schema cannot express -- ALWAYS run, so absence of the jsonschema package degrades
coverage LOUDLY rather than silently passing (the import-guard-answers-completion
-not-presence class).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "org" / "standards" / "PROOF_OF_SPEC.schema.json"


def conditional_checks(inst: dict) -> list[str]:
    """The rules draft-07 can't carry. Each violation is one printed line."""
    v: list[str] = []
    for i, row in enumerate(inst.get("acceptance", [])):
        rid = row.get("criterion_id", f"row-{i}")
        if row.get("status") != "PASS" and not row.get("status_reason"):
            v.append(f"acceptance[{rid}]: status={row.get('status')} REQUIRES status_reason")
        if row.get("status") == "PASS" and len(row.get("output_evidence", "").strip()) < 8:
            v.append(f"acceptance[{rid}]: PASS with thin/empty output_evidence -- a bare value; INVALID")
    m = inst.get("controls", {}).get("mutant", {})
    if m.get("status") == "DID-NOT-FIRE (deliverable INVALID)":
        v.append("controls.mutant: DID-NOT-FIRE -- the deliverable is INVALID by its own control")
    d = inst.get("controls", {}).get("determinism", {})
    if d.get("status") == "UNSTABLE (deliverable INVALID)":
        v.append("controls.determinism: UNSTABLE -- the deliverable is INVALID by its own control")
    if d.get("status") == "N/A-WITH-REASON" and len(d.get("method", "").strip()) < 8:
        v.append("controls.determinism: N/A-WITH-REASON requires the reason in method")
    # PER-ARTIFACT ACCEPTANCE COVERAGE (CVO gate candidate 2026-08-11: A_03 shipped with ZERO
    # battery rows, caught by eyeball twice independently -- luck-per-firm, now machinery).
    # Heuristic linkage via the criterion-id grammar ({firm}-{group}-{artifact}-{check}): an
    # artifact's stem token must appear in >=1 criterion_id, OR the artifact is named in
    # declared_exclusions. Matching is printed, never silent.
    import re as _re
    ids_blob = " ".join(r.get("criterion_id", "") for r in inst.get("acceptance", [])).upper()
    excl_blob = " ".join(str(e) for e in inst.get("declared_exclusions", [])).lower()
    for a in inst.get("artifacts_produced", []):
        if a.get("kind") not in ("script", "s3_object"):
            continue
        stem = Path(a.get("path_or_key", "")).name.split(".")[0]
        tokens = {t.upper().replace("_", "") for t in _re.findall(r"[A-Za-z]+_?\d+|[A-Za-z]{3,}", stem)}
        if not tokens:
            continue
        if any(t in ids_blob.replace("-", "").replace("_", "") for t in tokens if len(t) >= 3):
            continue
        if stem.lower() in excl_blob:
            continue
        v.append(f"artifact-coverage: '{a.get('path_or_key')}' has NO acceptance row referencing it "
                 f"(tokens tried: {sorted(tokens)}) and is not in declared_exclusions -- "
                 f"the A_03 zero-battery class; add rows or declare the exclusion")
    return v


def coverage_check(inst: dict, expected_arg: str) -> list[str]:
    """CVO step-zero mechanized: instance criterion set vs the TO's expected set."""
    p = Path(expected_arg)
    raw = p.read_text(encoding="utf-8").splitlines() if p.is_file() else expected_arg.split(",")
    expected = {s.strip() for s in raw if s.strip()}
    carried = {r.get("criterion_id", "") for r in inst.get("acceptance", [])}
    v = [f"coverage: criterion '{c}' in the TO's expected set has NO instance row (silent omission)"
         for c in sorted(expected - carried)]
    v += [f"coverage: instance row '{c}' is NOT in the TO's expected set (unexpected addition -- state it or fix the TO)"
          for c in sorted(carried - expected)]
    v.insert(0, f"coverage-frame: expected={len(expected)} carried={len(carried)} matched={len(expected & carried)}") if v else None
    return v


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print(__doc__)
        return 2
    try:
        inst = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"READ-ERROR: {exc}")
        return 2

    violations: list[str] = []
    if len(sys.argv) == 3:
        violations.extend(coverage_check(inst, sys.argv[2]))
    else:
        print("NOTE: no expected_criterion_ids given -- COVERAGE UNCHECKED (row quality only; "
              "an omitted criterion is invisible to this run). The cert consumer runs step-zero.")
    try:
        import jsonschema  # type: ignore

        for err in sorted(jsonschema.Draft7Validator(schema).iter_errors(inst), key=str):
            violations.append(f"schema: {'/'.join(str(p) for p in err.absolute_path) or '<root>'}: {err.message}")
        structural = "jsonschema"
    except ImportError:
        # Degrade LOUDLY: minimal required-keys check only.
        structural = "FALLBACK (jsonschema not installed -- structural coverage PARTIAL; install for full)"
        for k in schema.get("required", []):
            if k not in inst:
                violations.append(f"schema-fallback: missing required key '{k}'")

    violations.extend(conditional_checks(inst))

    n_acc = len(inst.get("acceptance", []))
    print(f"proof-of-spec-check | structural={structural} | acceptance rows={n_acc} | violations={len(violations)}")
    for line in violations:
        print(f"  VIOLATION: {line}")
    print("VALID" if not violations else "INVALID")
    return 0 if not violations else 1


if __name__ == "__main__":
    sys.exit(main())
