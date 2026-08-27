#!/usr/bin/env python
"""ISCK CONTRACT v0.1 -- validator + self-test + mutant battery + semantic arm.

Validates instances against ISCK_CONTRACT.v0.schema.json (Draft 2020-12) AND runs the
SEMANTIC checks the schema cannot express (field-pair comparison, calendar validity,
batch serial uniqueness) -- ISCK_CONTRACT.md sec 6 items 4/5/7.

Modes:
  validate_isck.py --self-test     axis arm + fixtures + mutants (with EXPECTED-REASON
                                   assertions, F7) + semantic mutants + gutted-schema
                                   meta-control. Exit 0 only on full PASS.
  validate_isck.py <file.json>     validate one instance or an array (semantic checks
                                   run batch-wide on arrays; vocabulary membership WARNs).

Battery discipline (round-1 boundary, F7): every mutant asserts its EXPECTED REJECTION
REASON (keyword set), branch-scoped past the root oneOf -- a mutant that starts rejecting
for a different reason FAILS the self-test instead of passing silently. The gutted-schema
meta-control proves the battery notices a deleted law.
"""
import copy
import datetime
import json
import os
import sys

import jsonschema

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(HERE, "ISCK_CONTRACT.v0.schema.json")
VOCAB = {
    "entity_class": "entity_classes.json",
    "identity_space": "identity_spaces.json",
    "identity_policy": "identity_policies.json",
}

ULID_A = "01jabcde0123456789abcdefgh"[:26]
ULID_B = "01jzyxwv9876543210zyxwvtsr"[:26]
TS = "2026-08-27T17:30:00Z"
TS2 = "2026-08-27T18:30:00Z"
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
        "evidence_refs": [f"obs:{ULID_A}"],
    },
    "state_observation": {
        "record_type": "state_observation", "observation_id": f"obs:{ULID_A}",
        "entity_serial": f"ent:{ULID_A}", "identity_space": "git",
        "source_vintage": "commit:9fc70e31a1", "observed_at": TS,
        "fabric_id": "laptop", "fabric_scope": "fabric_invariant",
        "failure_state": "observed",
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
    "materializer_version_complete": {
        "record_type": "materializer_version", "version_id": f"matv:{ULID_B}",
        "materializer_serial": f"mat:{ULID_A}",
        "bundle_completeness": "complete",
        "source_tree_digest": SHA, "dependency_lock_digest": SHA,
        "configuration_digest": SHA, "declared_opinions_digest": SHA,
        "normalizer_versions": ["none_raw_v0"], "runtime_contract_version": "rtc_v0",
        "bundle_digest": SHA, "valid_from": TS,
    },
    "materialization_run": {
        "record_type": "materialization_run", "run_id": f"run:{ULID_A}",
        "materializer_serial": f"mat:{ULID_A}", "materializer_version_id": f"matv:{ULID_A}",
        "source_frontier_id": f"sf:{ULID_A}", "fabric_id": "laptop",
        "fabric_scope": "fabric_invariant",
        "started_at": TS, "completed_at": TS2, "run_status": "succeeded",
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
        "evidence_refs": ["obs:" + ULID_A],
    },
}

_DEL = object()


def _mk(base_key, **changes):
    inst = copy.deepcopy(FIXTURES[base_key])
    for k, v in changes.items():
        if v is _DEL:
            inst.pop(k, None)
        else:
            inst[k] = v
    return inst


def _mutants():
    """(name, instance, expected_keywords) -- each MUST reject, for one of the named reasons."""
    m = []

    def add(name, base, expected, **ch):
        m.append((name, _mk(base, **ch), set(expected)))

    # LAW 1 shape (regex enforces SHAPE only -- ISCK_CONTRACT.md sec 6 limit 1)
    add("entity.serial-is-a-path", "entity", ["pattern"], entity_serial="ent:portal/src/App.tsx")
    add("entity.serial-is-sha256-shaped", "entity", ["pattern"], entity_serial="ent:sha256:" + "ab" * 32)
    # LAW 2 coupling (DT-1 / DT-5 / F-original)
    add("observation.fingerprint-without-normalization", "state_observation",
        ["required", "dependentRequired"], normalization_version=_DEL)
    add("observation.fingerprint-without-method", "state_observation",
        ["required", "dependentRequired"], fingerprint_method=_DEL)
    add("observation.partial-fingerprint-no-method", "state_observation",
        ["dependentRequired"], failure_state="partial", fingerprint_method=_DEL,
        normalization_version=_DEL)
    add("observation.method-without-fingerprint", "state_observation",
        ["dependentRequired"], failure_state="partial", fingerprint=_DEL,
        normalization_version=_DEL)
    add("observation.substrate-unavailable-carries-fingerprint", "state_observation",
        ["not"], failure_state="substrate_unavailable")
    # LAW 3 intervals (DT-4)
    add("binding.missing-valid-from", "entity_binding", ["required"], valid_from=_DEL)
    add("binding.closed-null-valid_to", "entity_binding", ["type"], status="closed")
    # LAW 4 locality (DT-7 / DT-8)
    add("binding.device-local-without-fabric", "entity_binding", ["required"],
        fabric_scope="device_local")
    add("binding.invariant-with-fabric", "entity_binding", ["not"], fabric_id="laptop")
    add("observation.invariant-with-device", "state_observation", ["not"], device_id="some-laptop")
    add("observation.missing-fabric", "state_observation", ["required"], fabric_id=_DEL)
    add("run.missing-fabric", "materialization_run", ["required"], fabric_id=_DEL)
    add("run.device-local-without-device", "materialization_run", ["required"],
        fabric_scope="device_local")
    # LAW 5 frontier + coherence warrants (CV-3)
    add("frontier.empty-entries", "source_frontier", ["minItems"], entries=[])
    add("surface.missing-frontier", "surface_version", ["required"], source_frontier_id=_DEL)
    add("coherence.missing-target-policy", "coherence_evaluation", ["required"],
        target_policy=_DEL)
    add("coherence.verified-no-evidence", "coherence_evaluation", ["required"],
        evidence_refs=_DEL, currency="unknown")
    add("coherence.mismatch-no-delta", "coherence_evaluation", ["required"],
        integrity="mismatch")
    add("coherence.currency-verdict-no-evidence", "coherence_evaluation", ["required"],
        integrity="unverified", evidence_refs=_DEL)
    # F5 warrant conditionals on identity_relation
    add("relation.corroborated-no-evidence", "identity_relation", ["required"],
        verification_standing="corroborated")
    add("relation.contradicted-no-adjudicator", "identity_relation", ["required"],
        verification_standing="contradicted", evidence_refs=["obs:" + ULID_A])
    add("relation.superseded-no-successor", "identity_relation", ["required"],
        verification_standing="superseded")
    add("relation.evidence-empty-list", "identity_relation", ["minItems"],
        verification_standing="corroborated", evidence_refs=[])
    # honesty conditionals
    add("matversion.partial-legacy-without-absent-components", "materializer_version",
        ["required"], absent_components=_DEL)
    add("matversion.complete-without-bundle-fields", "materializer_version", ["required"],
        bundle_completeness="complete", absent_components=_DEL)
    add("run.seeds-absent", "materialization_run", ["required"], random_seeds=_DEL)
    add("run.seeds-empty-list", "materialization_run", ["oneOf", "minItems", "const"],
        random_seeds=[])
    # run-status coherence (CV-4)
    add("run.running-with-completed", "materialization_run", ["type"], run_status="running")
    add("run.succeeded-without-completed", "materialization_run", ["required"],
        completed_at=_DEL)
    # timestamps (CV-4)
    add("observation.garbage-timestamp", "state_observation", ["pattern"],
        observed_at="2026-13-45T99:99:99Z")
    # ABLATION COVERAGE (COO~X 76625: 5 conditional rules no mutant depended on -- one per rule,
    # each built so ONLY its rule catches it, making every arm ablation-visible)
    add("relation.independently-observed-no-evidence", "identity_relation", ["required"],
        claim_origin="independently_observed")
    add("run.invariant-with-device", "materialization_run", ["not"], device_id="some-laptop")
    add("observation.observed-with-nothing", "state_observation", ["required"],
        fingerprint=_DEL, fingerprint_method=_DEL, normalization_version=_DEL)
    add("observation.device-local-without-device", "state_observation", ["required"],
        fabric_scope="device_local", fabric_id="laptop")
    add("observation.normalization-alone", "state_observation", ["dependentRequired"],
        failure_state="partial", fingerprint=_DEL, fingerprint_method=_DEL)
    # R2-3 warrants (round-2 batch 1: CRO~X gap 2 + COO~X 76588)
    add("binding.independently-observed-no-evidence", "entity_binding", ["required"],
        evidence_refs=_DEL)
    add("materializer.superseded-no-successor", "materializer", ["required"],
        current_status="superseded")
    # enum discipline (F4 renames; dead enums stay dead)
    add("binding.basis-is-dead-enum-measured", "entity_binding", ["enum"],
        binding_basis="measured")
    add("entity.status-dead-value-candidate", "entity", ["enum"], current_status="candidate")
    add("relation.unknown-type", "identity_relation", ["enum"], relation_type="same_as")
    add("entity.smuggled-field", "entity", ["additionalProperties"], legacy_name="c2_instances")
    return m


def _semantic_mutants():
    """(name, instance-or-batch) -- each MUST produce >=1 semantic error."""
    return [
        ("sem.relation-self-loop",
         _mk("identity_relation", relation_type="merged_into", object_serial=f"ent:{ULID_A}")),
        ("sem.entity-self-canonicalization",
         _mk("entity", canonicalized_as=f"ent:{ULID_A}")),
        ("sem.matversion-self-supersession",
         _mk("materializer_version", supersedes=f"matv:{ULID_A}")),
        ("sem.run-time-travel",
         _mk("materialization_run", started_at=TS2, completed_at=TS)),
        ("sem.calendar-feb30",
         _mk("state_observation", observed_at="2026-02-30T10:00:00Z")),
        ("sem.batch-duplicate-serial",
         [_mk("entity"), _mk("entity", entity_class="symbol", plane="symbol")]),
        ("sem.entity-active-canonicalized",
         _mk("entity", canonicalized_as=f"ent:{ULID_B}")),
        ("sem.frontier-duplicate-coordinate",
         _mk("source_frontier", entries=[
             FIXTURES["source_frontier"]["entries"][0],
             dict(FIXTURES["source_frontier"]["entries"][0],
                  source_version="snapshot:9999999999999999999"),
         ])),
    ]


_ISO_FIELDS = ["minted_at", "observed_at", "asserted_at", "started_at", "completed_at",
               "built_at", "evaluated_at", "valid_from"]
_PRIMARY_ID = {"entity": "entity_serial", "entity_binding": "binding_id",
               "state_observation": "observation_id", "identity_relation": "relation_id",
               "materializer": "materializer_serial", "materializer_version": "version_id",
               "materialization_run": "run_id", "source_frontier": "source_frontier_id",
               "surface_version": "surface_version_id", "coherence_evaluation": "evaluation_id"}


def _parse_iso(v):
    try:
        datetime.datetime.fromisoformat(v.replace("Z", "+00:00"))
        return True
    except (ValueError, AttributeError):
        return False


def semantic_errors(instances):
    """Field-pair, calendar, and batch checks the schema cannot express (sec 6 items 4/5/7)."""
    errs = []
    seen = {}
    for i, inst in enumerate(instances):
        if not isinstance(inst, dict):
            continue
        rt = inst.get("record_type", "?")
        # calendar validity past the pattern
        for f in _ISO_FIELDS:
            v = inst.get(f)
            if isinstance(v, str) and not _parse_iso(v):
                # only flag values that LOOK like timestamps (pattern-shaped fields)
                if "T" in v:
                    errs.append(f"[{i}] {rt}.{f}: not a real calendar instant: {v}")
        # field-pair comparisons
        if rt == "identity_relation" and inst.get("subject_serial") == inst.get("object_serial"):
            errs.append(f"[{i}] identity_relation: SELF-LOOP {inst.get('subject_serial')} "
                        f"({inst.get('relation_type')}) -- cardinality 1->1 would read as a "
                        "continuation (sec 3.12)")
        if rt == "entity" and inst.get("canonicalized_as") == inst.get("entity_serial") \
                and inst.get("canonicalized_as") is not None:
            errs.append(f"[{i}] entity: canonicalized_as itself")
        # R2-3: active-but-canonicalized contradiction (COO~X 76588 R2-5)
        if rt == "entity" and inst.get("canonicalized_as") is not None \
                and inst.get("canonicalized_as") != inst.get("entity_serial") \
                and inst.get("current_status") not in ("retired", "contested"):
            errs.append(f"[{i}] entity: canonicalized_as set while current_status="
                        f"{inst.get('current_status')} -- a canonicalized entity is retired or "
                        "contested, never active/provisional (sec 3.4)")
        # R2-6: frontier coordinate uniqueness (CRO~X gap 4 + COO~X 76588 R2-6, convergent)
        if rt == "source_frontier":
            coords = {}
            for j, e in enumerate(inst.get("entries", [])):
                if not isinstance(e, dict):
                    continue
                key = (e.get("source_serial"), e.get("identity_space"),
                       e.get("authority_ref"), e.get("fabric_id"))
                if key in coords:
                    errs.append(f"[{i}] source_frontier: entries [{coords[key]}] and [{j}] pin "
                                f"the SAME source coordinate {key} -- a frontier is a vector, one "
                                "version per coordinate (sec 6 / R2-6)")
                else:
                    coords[key] = j
        if rt == "materializer_version" and inst.get("supersedes") == inst.get("version_id") \
                and inst.get("supersedes") is not None:
            errs.append(f"[{i}] materializer_version: supersedes itself")
        if rt == "materialization_run":
            s, c = inst.get("started_at"), inst.get("completed_at")
            if isinstance(s, str) and isinstance(c, str) and _parse_iso(s) and _parse_iso(c):
                if c < s:
                    errs.append(f"[{i}] materialization_run: completed_at precedes started_at")
        # batch-scope serial uniqueness
        pid_field = _PRIMARY_ID.get(rt)
        if pid_field:
            pid = inst.get(pid_field)
            if pid in seen:
                errs.append(f"[{i}] {rt}: duplicate primary id {pid} (first at [{seen[pid]}])")
            elif pid is not None:
                seen[pid] = i
    return errs


def _leaf_errors(validator, inst):
    out = []

    def walk(e):
        if e.context:
            for c in e.context:
                walk(c)
        else:
            out.append(e)
    for e in validator.iter_errors(inst):
        walk(e)
    return out


def _branch_validator(schema, record_type):
    return jsonschema.Draft202012Validator(
        {"$ref": f"#/$defs/{record_type}", "$defs": schema["$defs"]})


def _load_vocab():
    vocab = {}
    for field, fname in VOCAB.items():
        p = os.path.join(HERE, "vocab", fname)
        try:
            with open(p, "r", encoding="utf-8") as fh:
                vocab[field] = set(json.load(fh)["members"])
        except (OSError, KeyError, ValueError) as exc:
            print(f"ERROR: vocab registry {fname} unreadable ({exc}) -- failing closed")
            raise
    return vocab


def _vocab_warnings(instances, vocab):
    warns = []
    for i, inst in enumerate(instances):
        if not isinstance(inst, dict):
            continue
        for field, members in vocab.items():
            v = inst.get(field)
            if isinstance(v, str) and v and v not in members:
                warns.append(f"WARN: [{i}] {inst.get('record_type', '?')}.{field}='{v}' is not a "
                             f"registered vocabulary member (sec 3.15 -- warn-not-reject at v0.1)")
    return warns


def main():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as fh:
        schema = json.load(fh)
    validator = jsonschema.Draft202012Validator(schema)
    vocab = _load_vocab()

    if len(sys.argv) > 1 and sys.argv[1] != "--self-test":
        with open(sys.argv[1], "r", encoding="utf-8") as fh:
            data = json.load(fh)
        instances = data if isinstance(data, list) else [data]
        errs = 0
        for i, inst in enumerate(instances):
            problems = _leaf_errors(validator, inst)
            if problems:
                errs += 1
                print(f"ERROR: instance[{i}] ({inst.get('record_type', '?')}):")
                for p in problems[:5]:
                    print(f"  {p.json_path}: {p.message[:140]}")
        sem = semantic_errors(instances)
        for s in sem:
            print(f"SEMANTIC: {s}")
        for w in _vocab_warnings(instances, vocab):
            print(w)
        ok = errs == 0 and not sem
        print(f"{'OK' if ok else 'ERROR'}: {len(instances) - errs} of {len(instances)} "
              f"schema-valid, {len(sem)} semantic error(s)")
        return 0 if ok else 1

    # ---------------- self-test ----------------
    fails = []

    # AXIS ARM (76257): the ruled axes exist as $defs with exact closed domains.
    axes = {"claim_origin": 5, "verification_standing": 4, "registry_standing": 6,
            "fabric_scope": 2}
    axis_bad = []
    for axis, n in axes.items():
        d = schema.get("$defs", {}).get(axis)
        if d is None:
            axis_bad.append(f"{axis}: ABSENT from $defs")
        elif len(d.get("enum", [])) != n:
            axis_bad.append(f"{axis}: {len(d.get('enum', []))} values, expected {n}")
    print(f"AXIS ARM: {len(axes) - len(axis_bad)} of {len(axes)} axes present with exact domains")
    fails += axis_bad

    # POSITIVE ARM: fixtures accept, produce zero semantic errors, zero vocab warnings.
    pos_bad = []
    for name, inst in FIXTURES.items():
        errs = _leaf_errors(validator, inst)
        if errs:
            pos_bad.append(f"fixture {name} rejected: {errs[0].message[:110]}")
    sem = semantic_errors(list(FIXTURES.values()))
    pos_bad += [f"fixture semantic: {s}" for s in sem]
    vw = _vocab_warnings(list(FIXTURES.values()), vocab)
    pos_bad += [f"fixture vocab: {w}" for w in vw]
    print(f"POSITIVE ARM: {len(FIXTURES) - len([b for b in pos_bad if b.startswith('fixture ') and 'rejected' in b])} "
          f"of {len(FIXTURES)} fixtures ACCEPT; semantic 0-expected got {len(sem)}; "
          f"vocab 0-expected got {len(vw)}")
    fails += pos_bad

    # NEGATIVE ARM with EXPECTED-REASON assertions (F7).
    muts = _mutants()
    neg_bad = []
    for name, inst, expected in muts:
        rt = inst.get("record_type")
        bv = _branch_validator(schema, rt)
        errs = _leaf_errors(bv, inst)
        if not errs:
            neg_bad.append(f"mutant {name} VALIDATED -- hole in the contract")
            continue
        got = {e.validator for e in errs}
        if not (got & expected):
            neg_bad.append(f"mutant {name} rejected for the WRONG reason: got {sorted(got)}, "
                           f"expected one of {sorted(expected)} (F7 drift)")
    print(f"NEGATIVE ARM: {len(muts) - len(neg_bad)} of {len(muts)} mutants reject FOR THEIR "
          f"NAMED REASON")
    fails += neg_bad

    # SEMANTIC ARM: semantic mutants must each produce >=1 semantic error.
    smuts = _semantic_mutants()
    sem_bad = []
    for name, payload in smuts:
        batch = payload if isinstance(payload, list) else [payload]
        if not semantic_errors(batch):
            sem_bad.append(f"semantic mutant {name} produced 0 errors")
    print(f"SEMANTIC ARM: {len(smuts) - len(sem_bad)} of {len(smuts)} semantic mutants FIRE")
    fails += sem_bad

    # META-CONTROL (F7): gut LAW 2 from a COPY; the coupling mutant must then VALIDATE,
    # proving the battery notices a deleted law (because this self-test would then FAIL).
    gutted = copy.deepcopy(schema)
    gutted["$defs"]["state_observation"].pop("dependentRequired", None)
    gutted["$defs"]["state_observation"].pop("allOf", None)
    gv = _branch_validator(gutted, "state_observation")
    gut_probe = _mk("state_observation", normalization_version=_DEL)
    if _leaf_errors(gv, gut_probe):
        fails.append("META-CONTROL: LAW-2 gutting NOT detected -- the coupling mutant still "
                     "rejects under a gutted schema, so the battery could not notice the deletion")
        print("META-CONTROL: FAIL")
    else:
        print("META-CONTROL: gutted-schema sensitivity CONFIRMED (coupling mutant flips to "
              "ACCEPT when LAW 2 is deleted -- the battery would catch the deletion)")

    if fails:
        for f in fails:
            print(f"  ERROR: {f}")
        print("FAIL")
        return 1
    print(f"PASS: {len(axes)}/{len(axes)} axes + {len(FIXTURES)}/{len(FIXTURES)} positive + "
          f"{len(muts)}/{len(muts)} negative (reason-asserted) + {len(smuts)}/{len(smuts)} "
          f"semantic + meta-control")
    return 0


if __name__ == "__main__":
    sys.exit(main())
