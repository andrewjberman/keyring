#!/usr/bin/env python3
"""Ratify the canonical 72-card KEYFILL registry compile, or refuse with evidence.

This is the RAT half of NFRA_SUBSTRATECARDING.TO-KEYFILL-RAT.  It never edits a
card, schema, or graph manifest.  It validates the compiler output at the one
settled authority pin, evaluates the registry's existing key admission
predicate without changing it, exercises a null-key negative control, and then
sets only ``ratified_at_commit`` in the registry.  The full per-member verdict
is written to a separate report.
"""
from __future__ import annotations

import argparse
import collections
import copy
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(
    subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
)
REGISTRY_REL = (
    "org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/"
    "D11_MANIFEST/card_population_registry.v1.json"
)
SCHEMA_REL = (
    "org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/"
    "D11_MANIFEST/CARD_POPULATION_REGISTRY.v1.schema.json"
)
COMPILE_RECEIPT_REL = (
    "org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/"
    "D11_MANIFEST/card_population_registry.v1.compile_receipt.json"
)
REPORT_REL = (
    "org/tier1_exec/4.0.0_SA_CRO~X/deliverables/"
    "NFRA_SUBSTRATECARDING.TO-KEYFILL-RAT_RATIFICATION_REPORT.json"
)
RECEIPT_REL = (
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/"
    "D11_V31_SETTLED_RECEIPT_cf66984cfc.md"
)
COMPILE_COMMIT = "92f1b8da9d564f8e5ed8740e1e1a2278577507e5"
SETTLED_PIN = "cf66984cfc39e7f45c0799c75be43c4ec1fb7934"
RECEIPT_COMMIT = "f635574b36"
EXPECTED_DIGEST = "d1e07efb2829a63674e02351c459de6d03605fab87841f5b2ebf3d26f71b44cc"
EXPECTED_PREDICATE = {
    "required_fields": [
        "trust.key.identity_space",
        "trust.key.key_expression",
        "trust.key.key_is_stable",
        "trust.key.crosses_spaces",
        "trust.key.declared_mapping",
        "trust.key.basis",
        "trust.key.evidence",
        "trust.key.owner",
    ],
    "basis_allowed": ["measured", "held", "inferred"],
    "all_non_blank": True,
}
EXPECTED_BASIS_BY_FIELD = {"absent": 1, "held": 10, "measured": 61}
EXPECTED_NULL_MEMBER = (
    "org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_CARDS_W2/"
    "W2-yjky__opal-estate-report_kuzu_nessie_db.json"
)
EXPECTED_ABSENT_BASIS_MEMBER = (
    "org/tier2_senior/0.8.0_AE_CloudComp/deliverables/D11_CARDS_W2/"
    "W2-qgtd_graph_contracts.json"
)
EXPECTED_EXCLUSION = (
    "org/tier2_senior/0.8.0_AE_CloudComp/deliverables/D11_CARDS_W4/"
    "W4-FILE.cells.json"
)
TOKEN_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
PATHLIKE_RE = re.compile(r"^[A-Za-z0-9_.][A-Za-z0-9_./-]*\.[A-Za-z0-9]{1,6}$")


def git(*args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True
    )
    if check and result.returncode:
        raise RuntimeError(
            "git %s failed rc=%d: %s"
            % (" ".join(args), result.returncode, result.stderr.strip()[:400])
        )
    return result.stdout.strip()


def commit(ref: str) -> str:
    return git("rev-parse", "--verify", "%s^{commit}" % ref)


def blob_at(pin: str, rel: str) -> str | None:
    result = subprocess.run(
        ["git", "rev-parse", "%s:%s" % (pin, rel)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def bytes_at(pin: str, rel: str) -> bytes:
    result = subprocess.run(
        ["git", "show", "%s:%s" % (pin, rel)], cwd=ROOT, capture_output=True
    )
    if result.returncode:
        raise RuntimeError("cannot read %s at %s" % (rel, pin[:12]))
    return result.stdout


def card_at(pin: str, rel: str) -> dict:
    return json.loads(bytes_at(pin, rel).decode("utf-8"))


def dotted(doc: dict, path: str):
    value = doc
    for part in path.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def blank(value) -> bool:
    return value is None or value == "" or value == [] or value == {}


def admission(card: dict, predicate: dict) -> tuple[str, str | None]:
    for field in predicate["required_fields"]:
        value = dotted(card, field)
        if predicate["all_non_blank"] and blank(value):
            return "NOT_ADMITTED", field
    basis = dotted(card, "trust.key.basis")
    if basis not in predicate["basis_allowed"]:
        return "NOT_ADMITTED", "trust.key.basis"
    return "ADMITTED", None


def candidate_digest(members: list[dict]) -> str:
    payload = "\n".join(
        "%s %s %s" % (m["git_blob_id"], m["path"], m["subject_id"])
        for m in sorted(members, key=lambda item: item["path"])
    ) + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def predicate_digest(predicate: dict) -> str:
    payload = json.dumps(predicate, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def derive_subject_disposition(members: list[dict], pin: str) -> dict:
    exact = sorted(
        subject
        for subject, count in collections.Counter(
            member["subject_id"] for member in members
        ).items()
        if count > 1
    )
    by_base: dict[str, list[dict]] = collections.defaultdict(list)
    for member in members:
        by_base[os.path.basename(member["subject_id"])].append(member)
    name_misses = {
        base: sorted(row["subject_id"] for row in rows)
        for base, rows in by_base.items()
        if len(rows) > 1 and len({row["subject_id"] for row in rows}) > 1
    }
    present, absent, names, s3 = [], [], [], []
    for member in members:
        subject = member["subject_id"]
        if subject.startswith("s3://"):
            s3.append(subject)
        elif not PATHLIKE_RE.match(subject):
            names.append(subject)
        elif blob_at(pin, subject) is None:
            absent.append(subject)
        else:
            present.append(subject)
    return {
        "exact_duplicate_subject_ids": exact,
        "name_misses_not_merged": dict(sorted(name_misses.items())),
        "subjects_absent_at_pin": sorted(absent),
        "subjects_not_a_path": len(names),
        "subjects_present_at_pin": len(present),
        "subjects_s3_uri": len(s3),
    }


def validate_receipt() -> dict:
    receipt_commit = commit(RECEIPT_COMMIT)
    raw = bytes_at(receipt_commit, RECEIPT_REL).decode("utf-8", "replace")
    required = [
        SETTLED_PIN,
        "already v3.1 72",
        "PASS 72",
        "LIVE false claim 0",
        "scalar UNDERSTATES true-MIN floor 0",
        "unbased valued sub-claim 0",
    ]
    missing = [token for token in required if token not in raw]
    if missing:
        raise RuntimeError("settled receipt is missing token(s): %s" % missing)
    return {
        "path": RECEIPT_REL,
        "commit": receipt_commit,
        "settled_pin": SETTLED_PIN,
        "pass": 72,
        "live_false_claim": 0,
        "understates": 0,
        "unbased": 0,
    }


def validate_compile_receipt(compile_commit: str, registry: dict) -> dict:
    raw = bytes_at(compile_commit, COMPILE_RECEIPT_REL)
    receipt = json.loads(raw.decode("utf-8"))
    expected_keys = {
        "candidate_set_digest",
        "compile_note",
        "compiled_at_commit",
        "kind",
        "registry_path",
        "registry_sha256",
        "subject_disposition",
        "why_here",
    }
    if set(receipt) != expected_keys:
        raise RuntimeError("compile receipt root keys changed: %s" % sorted(receipt))
    registry_raw = bytes_at(compile_commit, REGISTRY_REL)
    registry_sha = "sha256:" + hashlib.sha256(registry_raw).hexdigest()
    if receipt.get("kind") != "card_population_registry.v1.compile_receipt":
        raise RuntimeError("compile receipt kind is not canonical")
    if receipt.get("registry_path") != REGISTRY_REL:
        raise RuntimeError("compile receipt points at the wrong registry")
    if receipt.get("registry_sha256") != registry_sha:
        raise RuntimeError("compile receipt registry_sha256 does not bind the compiled bytes")
    if receipt.get("candidate_set_digest") != registry.get("candidate_set_digest"):
        raise RuntimeError("compile receipt candidate_set_digest does not bind the registry")
    if receipt.get("compiled_at_commit") != commit(SETTLED_PIN):
        raise RuntimeError("compile receipt compiled_at_commit is not the settled pin")
    if not str(receipt.get("compile_note", "")).strip():
        raise RuntimeError("compile receipt compile_note is blank")
    return {
        "path": COMPILE_RECEIPT_REL,
        "git_blob_id": blob_at(compile_commit, COMPILE_RECEIPT_REL),
        "sha256": "sha256:" + hashlib.sha256(raw).hexdigest(),
        "registry_sha256": registry_sha,
        "candidate_set_digest": receipt["candidate_set_digest"],
        "compiled_at_commit": receipt["compiled_at_commit"],
        "compile_note": receipt["compile_note"],
        "subject_disposition": receipt["subject_disposition"],
    }


def validate_real_member_control(cards: dict[str, dict]) -> dict:
    anchor_path = next(
        path for path in cards if path.endswith("/D11_CARDS_W2/anchor_catalog.json")
    )
    card = cards[anchor_path]
    home = dotted(card, "artifact.location.home")
    if not isinstance(home, str) or " :" not in home:
        raise RuntimeError("real-member control card has no parseable pinned source home")
    source_path = home.split(" :", 1)[0]
    source = bytes_at(SETTLED_PIN, source_path).decode("utf-8", "replace")
    member, key = "compute-orchestration", "EVENT_RULE"
    if member not in source or key not in source:
        raise RuntimeError("real-member control cannot find its member/key in the pinned source")
    if not TOKEN_RE.fullmatch(key):
        raise RuntimeError("real-member key fails the bare-token target-space predicate")
    identity_space = card["trust"]["key"]["identity_space"]
    if "token" not in identity_space.lower():
        raise RuntimeError("real-member control is not in the expected token identity space")
    return {
        "card": anchor_path,
        "source_path": source_path,
        "source_blob_at_pin": blob_at(SETTLED_PIN, source_path),
        "member": member,
        "key": key,
        "identity_space": identity_space,
        "target_space_predicate": TOKEN_RE.pattern,
        "predicate_result": "PASS",
    }


def run(apply: bool, write_refusal: bool = False) -> dict:
    compile_commit = commit(COMPILE_COMMIT)
    settled_pin = commit(SETTLED_PIN)
    registry_path = ROOT / REGISTRY_REL
    report_path = ROOT / REPORT_REL

    if git("diff", "--", REGISTRY_REL, COMPILE_RECEIPT_REL):
        raise RuntimeError("registry/compile-receipt pair is dirty before RAT; refusing to mix another writer")
    if blob_at("HEAD", REGISTRY_REL) != blob_at(compile_commit, REGISTRY_REL):
        raise RuntimeError("HEAD registry bytes do not equal canonical compile %s" % compile_commit[:12])
    if blob_at("HEAD", COMPILE_RECEIPT_REL) != blob_at(compile_commit, COMPILE_RECEIPT_REL):
        raise RuntimeError("HEAD compile-receipt bytes do not equal canonical compile %s" % compile_commit[:12])

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    compile_receipt = validate_compile_receipt(compile_commit, registry)
    if registry.get("ratified_at_commit") is not None:
        raise RuntimeError("registry is already ratified; one-shot RAT refuses")
    if registry.get("candidate_set_digest") != EXPECTED_DIGEST:
        raise RuntimeError("compiled candidate_set_digest is not the GO value")

    predicate = registry["receiver_source_populations"]["key"]["admission_predicate"]
    if predicate != EXPECTED_PREDICATE:
        raise RuntimeError("key admission predicate changed or was loosened")

    members = registry["extension_population"]["members"]
    if len(members) != 72:
        raise RuntimeError("member denominator is %d, expected 72" % len(members))
    recomputed_digest = candidate_digest(members)
    if recomputed_digest != registry["candidate_set_digest"]:
        raise RuntimeError("candidate_set_digest does not recompute")

    results, cards = [], {}
    basis_by_field: collections.Counter[str] = collections.Counter()
    blob_matches = 0
    for member in members:
        path = member["path"]
        actual_blob = blob_at(settled_pin, path)
        if actual_blob != member["git_blob_id"]:
            raise RuntimeError("blob mismatch: %s" % path)
        blob_matches += 1
        card = card_at(settled_pin, path)
        cards[path] = card
        subject = dotted(card, "subject.id")
        if subject != member["subject_id"]:
            raise RuntimeError("subject mismatch: %s" % path)
        status, failing_field = admission(card, predicate)
        field_basis = dotted(card, "trust.key.basis_by_field.key_expression")
        basis_by_field[str(field_basis)] += 1
        results.append(
            {
                "path": path,
                "git_blob_id": member["git_blob_id"],
                "subject_id": member["subject_id"],
                "key_admission": status,
                "failing_field": failing_field,
                "basis_by_field_key_expression": field_basis,
            }
        )

    admitted = [row for row in results if row["key_admission"] == "ADMITTED"]
    not_admitted = [row for row in results if row["key_admission"] == "NOT_ADMITTED"]
    # The card schema permits declared_mapping=null as an honest statement that a mapping is
    # only conventional.  The registry's receiver predicate is independently stricter: it names
    # declared_mapping among eight required fields AND sets all_non_blank=true.  Those cards are
    # valid cards but are not key-receiver-admissible.  Treating an explicit null as "present" here
    # would silently loosen the exact predicate this RAT exists to hold.
    if len(admitted) != 43 or len(not_admitted) != 29:
        raise RuntimeError(
            "admission denominator changed: admitted=%d not_admitted=%d"
            % (len(admitted), len(not_admitted))
        )
    failures = collections.Counter(row["failing_field"] for row in not_admitted)
    if failures != {
        "trust.key.declared_mapping": 27,
        "trust.key.key_expression": 1,
        "trust.key.basis": 1,
    }:
        raise RuntimeError("non-admission fields changed: %s" % dict(failures))
    null_rows = [row for row in not_admitted if row["path"] == EXPECTED_NULL_MEMBER]
    if len(null_rows) != 1 or null_rows[0]["failing_field"] != "trust.key.key_expression":
        raise RuntimeError("the expected null-key member is absent or failed on the wrong field")
    absent_basis_rows = [
        row for row in not_admitted if row["path"] == EXPECTED_ABSENT_BASIS_MEMBER
    ]
    if len(absent_basis_rows) != 1 or absent_basis_rows[0]["failing_field"] != "trust.key.basis":
        raise RuntimeError("the expected absent-basis member is absent or failed on the wrong field")

    basis_dist = dict(sorted(basis_by_field.items()))
    if basis_dist != EXPECTED_BASIS_BY_FIELD:
        raise RuntimeError("basis_by_field census changed: %s" % basis_dist)
    if basis_by_field.get("inferred", 0):
        raise RuntimeError("basis_by_field.key_expression inferred is prohibited")

    fixture = copy.deepcopy(cards[admitted[0]["path"]])
    fixture["trust"]["key"]["key_expression"] = None
    fixture_status, fixture_field = admission(fixture, predicate)
    if (fixture_status, fixture_field) != (
        "NOT_ADMITTED",
        "trust.key.key_expression",
    ):
        raise RuntimeError("null-key negative fixture did not discriminate")

    exclusion = card_at(settled_pin, EXPECTED_EXCLUSION)
    if exclusion.get("schema_version") or exclusion.get("subject"):
        raise RuntimeError("the named census exclusion now looks like a card")
    if EXPECTED_EXCLUSION in {member["path"] for member in members}:
        raise RuntimeError("the named cell manifest was admitted as a card")

    derived_subjects = derive_subject_disposition(members, settled_pin)
    recorded_subjects = dict(compile_receipt["subject_disposition"])
    recorded_subjects.pop("note", None)
    if derived_subjects != recorded_subjects:
        derived_absent = set(derived_subjects["subjects_absent_at_pin"])
        recorded_absent = set(recorded_subjects["subjects_absent_at_pin"])
        live_fallback_subjects = sorted(derived_absent - recorded_absent)
        affected = [
            {
                "card": member["path"],
                "subject": member["subject_id"],
                "subject_blob_at_pin": blob_at(settled_pin, member["subject_id"]),
                "subject_exists_in_live_working_tree": (ROOT / member["subject_id"]).exists(),
            }
            for member in members
            if member["subject_id"] in live_fallback_subjects
        ]
        refusal = {
            "schema_version": "1.0",
            "to_id": "NFRA_SUBSTRATECARDING.TO-KEYFILL-RAT",
            "ratifier": "4.0.0_SA_CRO~X",
            "status": "REFUSED",
            "reason": (
                "The compiled subject disposition is not single-pin. "
                "compile_card_registry_ext.py:255 falls back from blob_at(pin, subject) to "
                "os.path.exists() on the live working tree, so five subjects absent at the "
                "settled pin were recorded as present."
            ),
            "compile_commit": compile_commit,
            "compiled_at_commit": settled_pin,
            "compile_receipt": compile_receipt,
            "settled_receipt": validate_receipt(),
            "registry": {
                "path": REGISTRY_REL,
                "members": len(members),
                "blob_matches_at_pin": blob_matches,
                "candidate_set_digest": registry["candidate_set_digest"],
                "candidate_set_digest_recomputed": recomputed_digest,
                "ratified_at_commit": None,
                "registry_unchanged_from_compile": True,
                "predicate": predicate,
                "predicate_sha256": predicate_digest(predicate),
            },
            "admission": {
                "denominator": len(results),
                "admitted": len(admitted),
                "not_admitted": len(not_admitted),
                "not_admitted_by_field": dict(sorted(failures.items())),
                "not_admitted_rows": not_admitted,
                "results": results,
            },
            "basis_by_field_key_expression": {
                "denominator": len(results),
                "distribution": basis_dist,
                "inferred": basis_by_field.get("inferred", 0),
            },
            "negative_control": {
                "mutation": "set trust.key.key_expression to null on one admitted real card",
                "result": fixture_status,
                "failing_field": fixture_field,
            },
            "real_member_control": validate_real_member_control(cards),
            "census_exclusion": {
                "path": EXPECTED_EXCLUSION,
                "reason": "cell manifest: no schema_version and no subject; not a substrate card",
            },
            "subject_disposition": {
                "recorded": recorded_subjects,
                "pin_only_recomputed": derived_subjects,
                "affected_members": affected,
                "recorded_counts": {"present": 21, "absent": 16},
                "pin_only_counts": {"present": 16, "absent": 21},
                "exact_duplicates": 0,
                "name_misses_not_merged": 7,
            },
            "required_rework": (
                "Remove the live os.path.exists fallback from subject classification, recompile "
                "from the same canonical settled inputs, and reissue the compile for RAT."
            ),
        }
        if write_refusal:
            report_path.write_text(
                json.dumps(refusal, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
                newline="\n",
            )
            print("RAT REFUSAL REPORT %s" % REPORT_REL)
        raise RuntimeError(
            "subject disposition is mixed-pin; affected members: %s"
            % ", ".join(row["card"] for row in affected)
        )
    collision = derived_subjects["name_misses_not_merged"].get("c2_instances.json")
    if not collision or len(collision) != 2:
        raise RuntimeError("required c2_instances.json name-miss is absent")

    receipt = validate_receipt()
    real_member_control = validate_real_member_control(cards)
    ratification_parent = commit("HEAD")
    report = {
        "schema_version": "1.0",
        "to_id": "NFRA_SUBSTRATECARDING.TO-KEYFILL-RAT",
        "ratifier": "4.0.0_SA_CRO~X",
        "status": "PASS",
        "compile_commit": compile_commit,
        "compiled_at_commit": settled_pin,
        "compile_receipt": compile_receipt,
        "settled_receipt": receipt,
        "ratification_parent": ratification_parent,
        "registry": {
            "path": REGISTRY_REL,
            "members": len(members),
            "blob_matches_at_pin": blob_matches,
            "candidate_set_digest": registry["candidate_set_digest"],
            "candidate_set_digest_recomputed": recomputed_digest,
            "predicate": predicate,
            "predicate_sha256": predicate_digest(predicate),
            "receiver_key_members_unchanged": 0,
            "receiver_key_members_note": (
                "registry v1 keeps every receiver population empty while transform_status is "
                "absent; these per-member labels evaluate the unloosened predicate and do not "
                "invent a governed transform"
            ),
        },
        "admission": {
            "denominator": len(results),
            "admitted": len(admitted),
            "not_admitted": len(not_admitted),
            "not_admitted_by_field": dict(sorted(failures.items())),
            "not_admitted_rows": not_admitted,
            "results": results,
        },
        "basis_by_field_key_expression": {
            "denominator": len(results),
            "distribution": basis_dist,
            "inferred": basis_by_field.get("inferred", 0),
        },
        "negative_control": {
            "mutation": "set trust.key.key_expression to null on one admitted real card",
            "result": fixture_status,
            "failing_field": fixture_field,
        },
        "real_member_control": real_member_control,
        "census_exclusion": {
            "path": EXPECTED_EXCLUSION,
            "reason": "cell manifest: no schema_version and no subject; not a substrate card",
        },
        "subject_disposition": derived_subjects,
        "collision_disposition": (
            "Every exact duplicate set is empty. All seven basename name-misses remain distinct; "
            "c2_instances.json is recorded first and neither id form is ratified as a joined part. "
            "No basename collapse and no inferred bytes."
        ),
    }

    ratified = copy.deepcopy(registry)
    ratified["ratified_at_commit"] = ratification_parent
    from jsonschema import Draft202012Validator

    schema = json.loads(bytes_at(compile_commit, SCHEMA_REL).decode("utf-8"))
    errors = list(Draft202012Validator(schema).iter_errors(ratified))
    if errors:
        schema_errors = [
            {
                "instance_path": "/".join(str(part) for part in error.absolute_path),
                "validator": error.validator,
                "message": error.message,
            }
            for error in errors
        ]
        refusal = copy.deepcopy(report)
        refusal["status"] = "REFUSED"
        refusal["reason"] = (
            "The would-be ratified registry violates its own v1 schema at the root. "
            "No member failed; the compile added fields forbidden by additionalProperties=false."
        )
        refusal["registry"]["ratified_at_commit"] = None
        refusal["registry"]["proposed_ratified_at_commit"] = ratification_parent
        refusal["schema_validation"] = {
            "status": "FAIL",
            "schema_path": SCHEMA_REL,
            "schema_blob_at_compile": blob_at(compile_commit, SCHEMA_REL),
            "compile_commit": compile_commit,
            "errors": schema_errors,
            "last_ratified_registry_commit": commit("82e795810d"),
            "last_ratified_root_has_forbidden_fields": False,
            "required_rework": (
                "Produce a schema-valid registry and carry compile/disposition evidence in the "
                "RAT report or receipt, unless the issuer explicitly changes the no-schema-byte "
                "task boundary."
            ),
        }
        if write_refusal:
            report_path.write_text(
                json.dumps(refusal, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
                newline="\n",
            )
            print("RAT REFUSAL REPORT %s" % REPORT_REL)
        raise RuntimeError("ratified registry fails schema: %s" % errors[0].message)

    print("RAT PASS at parent %s" % ratification_parent)
    print("  members: 72 | blobs at pin: 72 | digest: MATCH")
    print("  key predicate: ADMITTED 43 | NOT_ADMITTED 29")
    print("  NOT_ADMITTED fields: declared_mapping 27 | key_expression 1 | basis 1")
    print("  null-key member: %s" % EXPECTED_NULL_MEMBER)
    print(
        "  basis_by_field.key_expression denominator 72: measured 61 | held 10 | "
        "absent 1 | inferred 0"
    )
    print("  null-key fixture: NOT_ADMITTED(trust.key.key_expression)")
    print("  subject disposition: exact duplicates 0 | name-misses 7 | absent paths 21")

    if apply:
        registry_path.write_text(
            json.dumps(ratified, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n"
        )
        report_path.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n"
        )
        print("  APPLIED ratified_at_commit=%s" % ratification_parent)
        print("  REPORT %s" % REPORT_REL)
    else:
        print("  DRY RUN: no files written")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--apply", action="store_true", help="write registry RAT field and report")
    group.add_argument(
        "--write-refusal",
        action="store_true",
        help="when a fail-closed check fires, write the refusal report but never the registry",
    )
    args = parser.parse_args()
    try:
        run(args.apply, args.write_refusal)
    except Exception as exc:  # noqa: BLE001 -- fail closed with the exact reason
        print("RAT REFUSED: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
