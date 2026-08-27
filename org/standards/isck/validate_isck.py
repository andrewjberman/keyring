#!/usr/bin/env python
"""ISCK CONTRACT v0 -- validator + self-test + mutant battery.

Validates instances against ISCK_CONTRACT.v0.schema.json (Draft 2020-12).

Modes:
  validate_isck.py --self-test     run 10 positive fixtures + mutant battery, print PASS/FAIL
  validate_isck.py <file.json>     validate one instance (or array of instances)

Every verdict prints its denominator. Exit 0 only on full PASS.
Both controls run: fixtures must ACCEPT (positive arm), mutants must REJECT (negative arm).
A mutant that VALIDATES is a hole in the contract, reported by name.
"""
import copy
import json
import os
import sys

import jsonschema

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(HERE, "ISCK_CONTRACT.v0.schema.json")

U = "0123456789abcdefghjkmnpqrstvwxyz"  # crockford lowercase
ULID_A = "01jabcde0123456789abcdefgh"[:26]
ULID_B = "01jzyxwv9876543210zyxwvtsr"[:26]
TS = "2026-08-27T17:30:00Z"
SHA = "sha256:" + "ab" * 32

FIXTURES = {
    "entity": {
        "record_type": "entity", "entity_serial": f"ent:{ULID_A}",
        "entity_class": "file", "plane": "file", "entity_grain": "repo_path_file",
        "identity_scope": "logical", "minted_at": TS,
        "minting_authority": "1.0.0_SA_CTO~X@laptop", "identity_policy": "git_history_v0",
        "current_status": "active",
    },
    "entity_binding": {
        "record_type": "entity_binding", "binding_id": f"bind:{ULID_A}",
        "entity_serial": f"ent:{ULID_A}", "identity_space": "git",
        "native_key": "portal/src/App.tsx", "fabric_scope": "fabric_invariant",
        "valid_from": "commit:9fc70e31a1", "valid_to": None,
        "binding_basis": "independently_observed", "status": "open",
    },
    "state_observation": {
        "record_type": "state_observation", "observation_id": f"obs:{ULID_A}",
        "entity_serial": f"ent:{ULID_A}", "identity_space": "git",
        "source_vintage": "commit:9fc70e31a1", "observed_at": TS,
        "fabric_id": "laptop", "failure_state": "observed",
        "fingerprint": SHA, "fingerprint_method": "sha256_raw_bytes",
        "normalization_version": "none_raw_v0",
    },
    "identity_relation": {
        "record_type": "identity_relation", "relation_id": f"rel:{ULID_A}",
        "relation_type": "candidate_equivalence",
        "subject_serial": f"ent:{ULID_A}", "object_serial": f"ent:{ULID_B}",
        "claim_origin": "rule_derived", "verification_standing": "unverified",
        "asserted_at": TS, "asserted_by": "1.0.0_SA_CTO~X",
    },
    "materializer": {
        "record_type": "materializer", "materializer_serial": f"mat:{ULID_A}",
        "semantic_layer": "C2", "canonical_role": "c2_motif_individuation",
        "owner": "3.0.0_SA_CVO", "current_status": "active",
    },
    "materializer_version": {
        "record_type": "materializer_version", "version_id": f"matv:{ULID_A}",
        "materializer_serial": f"mat:{ULID_A}",
        "bundle_completeness": "partial_legacy",
        "absent_components": ["dependency_lock", "declared_opinions"],
        "bundle_digest": SHA, "valid_from": TS,
    },
    "materialization_run": {
        "record_type": "materialization_run", "run_id": f"run:{ULID_A}",
        "materializer_serial": f"mat:{ULID_A}", "materializer_version_id": f"matv:{ULID_A}",
        "source_frontier_id": f"sf:{ULID_A}", "fabric_id": "laptop",
        "started_at": TS, "run_status": "succeeded",
        "random_seeds": "not_applicable",
        "output_surface_version_ids": [f"sv:{ULID_A}"],
    },
    "source_frontier": {
        "record_type": "source_frontier", "source_frontier_id": f"sf:{ULID_A}",
        "entries": [{
            "source_serial": f"ent:{ULID_A}", "identity_space": "iceberg_table",
            "authority_ref": "nessie:main", "source_version": "snapshot:8601547680771488785",
            "observed_at": TS, "fabric_id": "laptop",
        }],
    },
    "surface_version": {
        "record_type": "surface_version", "surface_version_id": f"sv:{ULID_A}",
        "logical_surface_serial": f"ent:{ULID_A}", "producing_run_id": f"run:{ULID_A}",
        "content_digest": SHA, "fingerprint_method": "sha256_raw_bytes",
        "normalization_version": "none_raw_v0",
        "source_frontier_id": f"sf:{ULID_A}", "published_ref": None,
        "built_at": TS, "fabric_id": "laptop",
    },
    "coherence_evaluation": {
        "record_type": "coherence_evaluation", "evaluation_id": f"ce:{ULID_A}",
        "subject_ref": f"sv:{ULID_A}", "target_policy": "declared_release",
        "target_ref": "nessie:refs/tags/audit-baseline-2026-06-17",
        "evaluated_at": TS, "evaluator": "1.0.0_SA_CTO~X",
        "fabric_id": "laptop", "availability": "available", "integrity": "verified",
        "currency": "at_target", "provenance": "complete",
        "fabric_validity": "valid_for_fabric",
    },
}


def _mutants():
    """Each mutant is (name, instance) and MUST be rejected by the schema."""
    muts = []

    def m(name, base_key, **changes):
        inst = copy.deepcopy(FIXTURES[base_key])
        for k, v in changes.items():
            if v is _DEL:
                inst.pop(k, None)
            else:
                inst[k] = v
        muts.append((name, inst))

    class _Del:
        pass
    global _DEL
    _DEL = _Del()

    # LAW 1: mint, never derive -- a path-shaped or sha-shaped serial must not validate.
    # DECLARED LIMIT (found by this battery's own first run): a 26-char hex string fits the
    # crockford alphabet, so a hash-derived value of the right LENGTH passes the shape check.
    # The regex enforces SHAPE; derivation-freedom is a MINTING-PROCESS property (audited at the
    # minting authority), not a schema property. Recorded in ISCK_CONTRACT.md sec 6.
    m("entity.serial-is-a-path", "entity", entity_serial="ent:portal/src/App.tsx")
    m("entity.serial-is-sha256-shaped", "entity", entity_serial="ent:sha256:" + "ab" * 32)
    # LAW 2: fingerprint never travels without method+normalization
    m("observation.fingerprint-without-normalization", "state_observation", normalization_version=_DEL)
    m("observation.fingerprint-without-method", "state_observation", fingerprint_method=_DEL)
    # bare-except law: a failed instrument may not carry a value
    m("observation.substrate-unavailable-carries-fingerprint", "state_observation",
      failure_state="substrate_unavailable")
    # LAW 3: bindings carry validity; open-ended mutation is inexpressible
    m("binding.missing-valid-from", "entity_binding", valid_from=_DEL)
    m("binding.device-local-without-fabric", "entity_binding", fabric_scope="device_local")
    # LAW 4: rule 26 metadata
    m("observation.missing-fabric", "state_observation", fabric_id=_DEL)
    m("run.missing-fabric", "materialization_run", fabric_id=_DEL)
    # LAW 5: frontier not head
    m("frontier.empty-entries", "source_frontier", entries=[])
    m("surface.missing-frontier", "surface_version", source_frontier_id=_DEL)
    m("coherence.missing-target-policy", "coherence_evaluation", target_policy=_DEL)
    # honesty conditionals
    m("matversion.partial-legacy-without-absent-components", "materializer_version",
      absent_components=_DEL)
    m("matversion.complete-without-bundle-fields", "materializer_version",
      bundle_completeness="complete", absent_components=_DEL)
    m("run.seeds-absent", "materialization_run", random_seeds=_DEL)
    m("run.seeds-empty-list", "materialization_run", random_seeds=[])
    # enum discipline: the dead two-value basis cannot come back
    m("binding.basis-is-dead-enum-measured", "entity_binding", binding_basis="measured")
    m("relation.unknown-type", "identity_relation", relation_type="same_as")
    # closed records: no smuggled fields
    m("entity.smuggled-field", "entity", legacy_name="c2_instances")
    return muts


def main():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as fh:
        schema = json.load(fh)
    validator = jsonschema.Draft202012Validator(schema)

    if len(sys.argv) > 1 and sys.argv[1] != "--self-test":
        with open(sys.argv[1], "r", encoding="utf-8") as fh:
            data = json.load(fh)
        instances = data if isinstance(data, list) else [data]
        errs = 0
        for i, inst in enumerate(instances):
            problems = sorted(validator.iter_errors(inst), key=lambda e: e.json_path)
            if problems:
                errs += 1
                print(f"ERROR: instance[{i}] ({inst.get('record_type', '?')}):")
                for p in problems[:5]:
                    print(f"  {p.json_path}: {p.message[:140]}")
        print(f"{'ERROR' if errs else 'OK'}: {len(instances) - errs} of {len(instances)} instances valid")
        return 1 if errs else 0

    # --- self-test ---
    pos_fail = []
    for name, inst in FIXTURES.items():
        errs = list(validator.iter_errors(inst))
        if errs:
            pos_fail.append((name, errs[0].message[:120]))
    muts = _mutants()
    neg_fail = []
    for name, inst in muts:
        if not list(validator.iter_errors(inst)):
            neg_fail.append(name)

    print(f"POSITIVE ARM: {len(FIXTURES) - len(pos_fail)} of {len(FIXTURES)} fixtures ACCEPT")
    for name, msg in pos_fail:
        print(f"  ERROR: fixture {name} rejected: {msg}")
    print(f"NEGATIVE ARM: {len(muts) - len(neg_fail)} of {len(muts)} mutants REJECT")
    for name in neg_fail:
        print(f"  ERROR: mutant {name} VALIDATED -- hole in the contract")
    if pos_fail or neg_fail:
        print("FAIL")
        return 1
    print(f"PASS: {len(FIXTURES)}/{len(FIXTURES)} positive + {len(muts)}/{len(muts)} negative")
    return 0


if __name__ == "__main__":
    sys.exit(main())
