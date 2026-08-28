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
ULID_C = "01jprt1a10000000000000000c"[:26]
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
        "status_basis": {"current_status": "authored"},
    },
    "entity_binding": {
        "record_type": "entity_binding", "binding_id": f"bind:{ULID_A}",
        "entity_serial": f"ent:{ULID_A}", "identity_space": "git",
        "native_key": "portal/src/App.tsx", "referent_scope": "fabric_invariant",
        "valid_from": "commit:9fc70e31a1", "valid_to": None,
        "binding_basis": "independently_observed", "status": "open",
        "status_basis": {"status": "authored"},
        "evidence_refs": [f"obs:{ULID_A}"],
    },
    "state_observation": {
        "record_type": "state_observation", "observation_id": f"obs:{ULID_A}",
        "entity_serial": f"ent:{ULID_A}", "identity_space": "git",
        "source_vintage": "commit:9fc70e31a1", "observed_at": TS,
        "observed_on_fabric": "laptop", "referent_scope": "fabric_invariant",
        "failure_state": "observed",
        "fingerprint": SHA, "fingerprint_method": "sha256_raw_bytes",
        "normalization_version": "none_raw_v0",
    },
    "state_observation_absence": {
        "record_type": "state_observation", "observation_id": f"obs:{ULID_B}",
        "entity_serial": f"ent:{ULID_A}", "identity_space": "s3_key",
        "source_native_key": "warehouse/_branch_head.dev.json",
        "source_vintage": "list-objects-v2:2026-08-27T21:26Z", "observed_at": TS2,
        "observed_on_fabric": "laptop", "referent_scope": "fabric_invariant",
        "failure_state": "observed_absent",
        "evidence_refs": ["obs:" + ULID_A],
    },
    "state_observation_partial": {
        "record_type": "state_observation", "observation_id": f"obs:{ULID_C}",
        "entity_serial": f"ent:{ULID_A}", "identity_space": "git",
        "source_vintage": "commit:9fc70e31a1", "observed_at": TS,
        "observed_on_fabric": "laptop", "referent_scope": "fabric_invariant",
        "failure_state": "partial",
        "fingerprint": SHA, "fingerprint_method": "sha256_raw_bytes",
        "normalization_version": "none_raw_v0",
        "evidence_refs": ["obs:" + ULID_A + "#unseen:submodule-tree"],
    },
    "identity_relation": {
        "record_type": "identity_relation", "relation_id": f"rel:{ULID_A}",
        "relation_type": "candidate_equivalence",
        "subject_serial": f"ent:{ULID_A}", "object_serial": f"ent:{ULID_B}",
        "claim_origin": "rule_derived", "verification_standing": "unverified",
        "status_basis": {"verification_standing": "authored"},
        "asserted_at": TS, "asserted_by": "1.0.0_SA_CTO~X",
        "evidence_refs": ["migration-map:kimi_to_isck_v0"],
    },
    "bridge_assertion": {
        "record_type": "bridge_assertion", "bridge_id": f"br:{ULID_A}",
        "relation_kind": "containment",
        "subject_entity_serial": f"ent:{ULID_A}", "subject_plane": "symbol",
        "subject_grain": "parser_symbol",
        "object_entity_serial": f"ent:{ULID_B}", "object_plane": "file",
        "object_grain": "repo_path_file",
        "claim_origin": "rule_derived", "verification_standing": "unverified",
        "registry_standing": "candidate",
        "status_basis": {"verification_standing": "authored", "registry_standing": "authored"},
        "declared_cardinality": "function",
        "firm_scope": "opal",
        "evidence_refs": ["parser:source-span portal/src/App.tsx:12-40"],
        "asserted_at": TS, "asserted_by": "1.0.0_SA_CTO~X",
        "valid_from": "commit:9fc70e31a1", "valid_to": None,
    },
    "mint_receipt": {
        "record_type": "mint_receipt", "receipt_id": f"mr:{ULID_A}",
        "entity_serial": f"ent:{ULID_A}", "minted_at": TS,
        "minting_authority": "1.0.0_SA_CTO~X@laptop", "minted_on_fabric": "laptop",
        "serial_form": "ulid26_lowercase_v1",
        "collision_preflight": "checked_unique",
        "evidence_refs": ["ledger-scan:0-collisions@2026-08-27T21Z"],
    },
    "materializer": {
        "record_type": "materializer", "materializer_serial": f"mat:{ULID_A}",
        "semantic_layer": "C2", "canonical_role": "c2_motif_individuation",
        "owner": "3.0.0_SA_CVO", "current_status": "active",
        "status_basis": {"current_status": "authored"},
    },
    "materializer_version": {
        "record_type": "materializer_version", "version_id": f"matv:{ULID_A}",
        "materializer_serial": f"mat:{ULID_A}",
        "bundle_completeness": "partial",
        "absent_components": ["dependency_lock", "declared_opinions"],
        "bundle_digest": SHA, "valid_from": TS,
    },
    # R2-2 (c): contests are their own record with a TYPED target -- one opened (entity), one
    # resolved (binding), two contest ids, so both target kinds and both event kinds have positive
    # coverage
    "contest_event": {
        "record_type": "contest_event", "event_id": f"ctev:{ULID_A}",
        "contest_id": f"ct:{ULID_A}", "event_kind": "opened",
        "target_kind": "entity", "target_entity_serial": f"ent:{ULID_A}",
        "occurred_at": TS, "actor": "3.0.0_SA_CVO~X",
        "basis": "two provisional serials claim one logical entity across fabrics",
        "evidence_refs": [f"mr:{ULID_A}", f"mr:{ULID_B}"],
    },
    "contest_event_resolved": {
        "record_type": "contest_event", "event_id": f"ctev:{ULID_B}",
        "contest_id": f"ct:{ULID_B}", "event_kind": "resolved",
        "target_kind": "binding", "target_binding_id": f"bind:{ULID_A}",
        "occurred_at": TS2, "actor": "3.0.0_SA_CVO~X",
        "outcome": "upheld", "adjudicated_by": "3.0.0_SA_CVO~X",
        "consequence_refs": [f"bind:{ULID_B}"],
        "evidence_refs": [f"obs:{ULID_B}"],
    },
    # R2-2 (a)/(g): the append-only carrier of a vocabulary rewrite -- this instance IS the receipt
    # for the fixture rewrite partial_legacy -> partial (migration/R2_2_MIGRATION_MANIFEST.json)
    "migration_receipt": {
        "record_type": "migration_receipt", "receipt_id": f"mig:{ULID_A}",
        "migrated_record_ref": f"matv:{ULID_A}", "field": "bundle_completeness",
        "source_value": "partial_legacy", "target_value": "partial",
        "recoverability": "recovered",
        "migration_map": "migration/R2_2_MIGRATION_MANIFEST.json",
        "migrated_at": TS2, "migrated_by": "1.0.0_SA_CTO~X",
        "evidence_refs": ["R2_2_DERIVED_STATUS_DESIGN.md#3d"],
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
        "source_frontier_id": f"sf:{ULID_A}", "executed_on_fabric": "laptop",
        "started_at": TS, "completed_at": TS2, "run_status": "succeeded",
        "random_seeds": "not_applicable",
        "output_surface_version_ids": [f"sv:{ULID_A}", f"sv:{ULID_B}"],
    },
    "source_frontier": {
        "record_type": "source_frontier", "source_frontier_id": f"sf:{ULID_A}",
        "normalization_version": "coord_v1", "completeness": "complete", "expected_count": 1,
        "entries": [{
            "source_serial": f"ent:{ULID_A}", "identity_space": "iceberg_table",
            "authority_ref": "nessie:main", "source_version": "snapshot:8601547680771488785",
            "canonical_key": "nessie:main/iceberg_table/ent:" + ULID_A,
            "availability": "available", "referent_scope": "fabric_invariant",
            "observed_at": TS, "observed_on_fabric": "laptop",
        }],
    },
    # R3-CVO-4: the OTHER legitimate partial -- fewer entries than expected, all of them available
    "source_frontier_partial_short": {
        "record_type": "source_frontier", "source_frontier_id": f"sf:{ULID_C}",
        "normalization_version": "coord_v1", "completeness": "partial", "expected_count": 2,
        "entries": [{
            "source_serial": f"ent:{ULID_A}", "identity_space": "iceberg_table",
            "authority_ref": "nessie:main", "source_version": "snapshot:8601547680771488785",
            "canonical_key": "nessie:main/iceberg_table/ent:" + ULID_A,
            "availability": "available", "referent_scope": "fabric_invariant",
            "observed_at": TS, "observed_on_fabric": "laptop",
        }],
    },
    # R3-CRO-8: a PARTIAL frontier keeps its unavailable source PRESENT, with the warrant of absence
    "source_frontier_partial": {
        "record_type": "source_frontier", "source_frontier_id": f"sf:{ULID_B}",
        "normalization_version": "coord_v1", "completeness": "partial", "expected_count": 2,
        "entries": [{
            "source_serial": f"ent:{ULID_A}", "identity_space": "iceberg_table",
            "authority_ref": "nessie:main", "source_version": "snapshot:8601547680771488785",
            "canonical_key": "nessie:main/iceberg_table/ent:" + ULID_A,
            "availability": "available", "referent_scope": "fabric_invariant",
            "observed_at": TS, "observed_on_fabric": "laptop",
        }, {
            "source_serial": f"ent:{ULID_B}", "identity_space": "device_local_path",
            "authority_ref": "file", "source_version": "unavailable",
            "canonical_key": "file/C:/warehouse/catalog.db",
            "availability": "unavailable", "absence_evidence": "probe:ENOENT@laptop",
            "referent_scope": "device_local", "referent_fabric_id": "laptop",
            "referent_device_id": "some-laptop",
            "observed_at": TS, "observed_on_fabric": "laptop",
        }],
    },
    "surface_version": {
        "record_type": "surface_version", "surface_version_id": f"sv:{ULID_A}",
        "logical_surface_serial": f"ent:{ULID_A}", "producing_run_id": f"run:{ULID_A}",
        "content_digest": SHA, "fingerprint_method": "sha256_raw_bytes",
        "normalization_version": "none_raw_v0",
        "source_frontier_id": f"sf:{ULID_A}", "published_ref": None,
        "publication_state": "unpublished",
        "built_at": TS, "built_on_fabric": "laptop",
    },
    # R3-CRO-10: publication is a STATE with its receipt, never a bare ref
    "surface_version_published": {
        "record_type": "surface_version", "surface_version_id": f"sv:{ULID_B}",
        "logical_surface_serial": f"ent:{ULID_A}", "producing_run_id": f"run:{ULID_A}",
        "content_digest": SHA, "fingerprint_method": "sha256_raw_bytes",
        "normalization_version": "none_raw_v0",
        "source_frontier_id": f"sf:{ULID_A}", "published_ref": "kuzu:prod/current",
        "publication_state": "published", "published_at": TS2,
        "promoted_by": "0.7.0_AE_CloudOps", "promotion_evidence_refs": ["deploy:kuzu-prod@" + TS2],
        "built_at": TS, "built_on_fabric": "laptop",
    },
    "coherence_evaluation": {
        "record_type": "coherence_evaluation", "evaluation_id": f"ce:{ULID_A}",
        "subject_ref": f"sv:{ULID_A}", "target_policy": "declared_release",
        "target_ref": "nessie:refs/tags/audit-baseline-2026-06-17",
        "evaluated_at": TS, "evaluator": "1.0.0_SA_CTO~X",
        "evaluated_on_fabric": "laptop", "availability": "available", "integrity": "verified",
        "currency": "at_target", "provenance": "complete",
        "fabric_validity": "valid_for_fabric",
        "evidence_refs": ["obs:" + ULID_A],
    },
    # R3-CRO-11: latest_authority carries the head it RESOLVED to, or the verdict is not reproducible
    "coherence_evaluation_latest": {
        "record_type": "coherence_evaluation", "evaluation_id": f"ce:{ULID_B}",
        "subject_ref": f"sv:{ULID_A}", "target_policy": "latest_authority",
        "target_ref": "nessie:main", "resolved_target_ref": "nessie:main",
        "resolved_target_version": "snapshot:8601547680771488785",
        "evaluated_at": TS2, "evaluator": "1.0.0_SA_CTO~X",
        "evaluated_on_fabric": "laptop", "availability": "available", "integrity": "unverified",
        "currency": "unknown", "provenance": "complete",
        "fabric_validity": "valid_for_fabric",
    },
    # ROUND 4 / v0.3-candidate (ROUND3_CHARTER.md sec 11, eight items): the append-only carriers the
    # WP-3 design could not derive from +38, each with positive coverage of every conditional arm
    "lifecycle_event": {
        "record_type": "lifecycle_event", "event_id": f"lce:{ULID_A}",
        "event_kind": "materializer_superseded", "materializer_serial": f"mat:{ULID_A}",
        "superseding_version_id": f"matv:{ULID_C}",
        "occurred_at": TS2, "actor": "3.0.0_SA_CVO~X",
        "evidence_refs": ["LD-0461#materializer-succession"],
    },
    "lifecycle_event_decommissioned": {
        "record_type": "lifecycle_event", "event_id": f"lce:{ULID_B}",
        "event_kind": "materializer_decommissioned", "materializer_serial": f"mat:{ULID_A}",
        "occurred_at": TS2, "actor": "3.0.0_SA_CVO~X",
        "evidence_refs": ["LD-0461#materializer-decommission"],
    },
    "binding_event": {
        "record_type": "binding_event", "event_id": f"bev:{ULID_A}",
        "event_kind": "closed", "binding_id": f"bind:{ULID_A}",
        "occurred_at": TS2, "actor": "1.0.0_SA_CTO~X",
        "evidence_refs": ["commit:9fc70e31a1#rename portal/src/App.tsx"],
    },
    "authority_epoch_event": {
        "record_type": "authority_epoch_event", "event_id": f"aep:{ULID_A}",
        "event_kind": "opened", "authority_id": "1.0.0_SA_CTO~X@laptop",
        "occurred_at": TS, "actor": "0.0.0_AB_MSTR",
        "evidence_refs": ["ISCK_CONTRACT.md#sec-5-minting-authority"],
    },
    # item 8: a contest whose TARGET is a lifecycle event (the correction path for a mis-typed
    # process supersession); resolved+upheld names exactly one replacement event
    "contest_event_lifecycle": {
        "record_type": "contest_event", "event_id": f"ctev:{ULID_C}",
        "contest_id": f"ct:{ULID_C}", "event_kind": "resolved",
        "target_kind": "lifecycle_event", "target_event_id": f"lce:{ULID_A}",
        "occurred_at": TS2, "actor": "3.0.0_SA_CVO~X",
        "outcome": "upheld", "adjudicated_by": "3.0.0_SA_CVO~X",
        "consequence_refs": [f"lce:{ULID_C}"],
        "evidence_refs": ["LD-0461#wrong-successor-version"],
    },
    # the REPLACEMENT the upheld contest names: same event_kind + materializer_serial, NEW id
    # (R3-CVO-12 c3) -- the first draft of this fixture set named the decommission event as the
    # replacement and the semantic arm rejected its own author's fixture, which is the arm working
    "lifecycle_event_replacement": {
        "record_type": "lifecycle_event", "event_id": f"lce:{ULID_C}",
        "event_kind": "materializer_superseded", "materializer_serial": f"mat:{ULID_A}",
        "superseding_version_id": f"matv:{ULID_C}",
        "occurred_at": TS2, "actor": "3.0.0_SA_CVO~X",
        "evidence_refs": ["LD-0461#materializer-succession", f"ctev:{ULID_C}"],
    },
    # item 1: the backward supersession link on an assertion (the new head names its predecessor)
    "identity_relation_superseding": {
        "record_type": "identity_relation", "relation_id": f"rel:{ULID_B}",
        "relation_type": "candidate_equivalence",
        "subject_serial": f"ent:{ULID_A}", "object_serial": f"ent:{ULID_B}",
        "claim_origin": "independently_observed", "verification_standing": "corroborated",
        "status_basis": {"verification_standing": "authored"},
        "asserted_at": TS2, "asserted_by": "4.0.0_SA_CRO~X",
        "supersedes": f"rel:{ULID_A}",
        "evidence_refs": ["obs:" + ULID_B],
    },
}


# ATTACK TARGETS (path-grained assertions, round 2: COO~X 76662 same-keyword-drift closure).
# Per mutant: the FIELD(s) its rejection must reference. DECLARED here, never derived from the
# instance -- a drifted instance would contaminate a derived set with its own corruption. A mutant
# absent from this dict is UNSCOREABLE and FAILS the self-test (the ARM-2 rule).
ATTACK_TARGETS = {
    "entity.serial-is-a-path": ["entity_serial"],
    "entity.serial-is-sha256-shaped": ["entity_serial"],
    "observation.fingerprint-without-normalization": ["normalization_version"],
    "observation.fingerprint-without-method": ["fingerprint_method"],
    "observation.partial-fingerprint-no-method": ["fingerprint_method", "normalization_version"],
    "observation.method-without-fingerprint": ["fingerprint"],
    "observation.substrate-unavailable-carries-fingerprint": ["fingerprint"],
    "observation.absent-carries-fingerprint": ["fingerprint"],
    "observation.absent-no-warrant": ["evidence_refs"],
    "observation.invariant-with-referent-fabric": ["referent_fabric_id"],
    "observation.fabric-local-without-fabric": ["referent_fabric_id"],
    "observation.fabric-local-with-device": ["referent_device_id"],
    "observation.device-local-missing-device": ["referent_device_id"],
    "binding.invariant-with-referent-fabric": ["referent_fabric_id"],
    "binding.fabric-local-without-fabric": ["referent_fabric_id"],
    "binding.device-local-missing-both-keys": ["referent_fabric_id", "referent_device_id"],
    "run.missing-execution-fabric": ["executed_on_fabric"],
    "binding.missing-valid-from": ["valid_from"],
    "frontier.empty-entries": ["entries"],
    "surface.missing-frontier": ["source_frontier_id"],
    "coherence.missing-target-policy": ["target_policy"],
    "coherence.verified-no-evidence": ["evidence_refs"],
    "coherence.mismatch-no-delta": ["delta_summary"],
    "coherence.currency-verdict-no-evidence": ["evidence_refs"],
    "relation.corroborated-no-evidence": ["evidence_refs"],
    "relation.corroborated-with-adjudicator": ["adjudicated_by"],
    "relation.retirement-with-object": ["object_serial"],
    "relation.non-retirement-without-object": ["object_serial"],
    "entity.no-status-basis": ["status_basis"],
    "entity.status-basis-derived": ["status_basis"],
    "bridge.status-basis-partial-map": ["status_basis"],
    "binding.status-basis-extra-key": ["status_basis"],
    "contest.entity-kind-with-binding-ref": ["target_binding_id"],
    "contest.binding-kind-without-ref": ["target_binding_id"],
    "contest.opened-without-basis": ["basis"],
    "contest.opened-with-outcome": ["outcome"],
    "contest.resolved-without-adjudicator": ["adjudicated_by"],
    "contest.upheld-without-consequence": ["consequence_refs"],
    "contest.dismissed-with-consequence": ["consequence_refs"],
    "contest.merged-without-survivor": ["surviving_contest_id"],
    "contest.merged-with-consequence": ["consequence_refs"],
    "contest.upheld-with-survivor": ["surviving_contest_id"],
    "contest.survivor-not-a-contest-id": ["surviving_contest_id"],
    "relation.retirement-without-evidence": ["evidence_refs"],
    "mig.missing-evidence": ["evidence_refs"],
    "frontier.missing-expected-count": ["expected_count"],
    "frontier.entry-missing-canonical-key": ["canonical_key"],
    "frontier.entry-unavailable-without-absence-evidence": ["absence_evidence"],
    "frontier.entry-available-with-absence-evidence": ["absence_evidence"],
    "frontier.entry-device-local-without-device": ["referent_device_id"],
    "frontier.entry-invariant-with-fabric": ["referent_fabric_id"],
    "surface.published-without-published-at": ["published_at"],
    "surface.unpublished-with-published-at": ["published_at"],
    "surface.unpublished-with-published-ref": ["published_ref"],
    "surface.published-with-null-ref": ["published_ref"],
    "surface.unpublished-without-published-ref": ["published_ref"],
    "coherence.latest-without-resolved-head": ["resolved_target_ref"],
    "coherence.declared-release-with-resolved-head": ["resolved_target_ref"],
    "relation.evidence-empty-list": ["evidence_refs"],
    "matversion.partial-without-absent-components": ["absent_components"],
    "matversion.complete-without-bundle-fields": ["source_tree_digest", "dependency_lock_digest",
                                                  "configuration_digest",
                                                  "declared_opinions_digest",
                                                  "normalizer_versions",
                                                  "runtime_contract_version"],
    "run.seeds-absent": ["random_seeds"],
    "run.seeds-empty-list": ["random_seeds"],
    "run.running-with-completed": ["completed_at"],
    "run.succeeded-without-completed": ["completed_at"],
    "observation.garbage-timestamp": ["observed_at"],
    "relation.independently-observed-no-evidence": ["evidence_refs"],
    "observation.observed-with-nothing": ["fingerprint", "fingerprint_method",
                                          "normalization_version"],
    "observation.normalization-alone": ["fingerprint"],
    "binding.independently-observed-no-evidence": ["evidence_refs"],
    "materializer.superseded-no-successor": ["superseded_by_version"],
    "materializer.active-with-successor": ["superseded_by_version"],
    "entity.contested-no-adjudicator": ["adjudicated_by"],
    "entity.active-with-adjudicator": ["adjudicated_by"],
    "relation.unverified-with-adjudicator": ["adjudicated_by"],
    "relation.rule-derived-no-evidence": ["evidence_refs"],
    "binding.model-inferred-no-evidence": ["evidence_refs"],
    "binding.basis-is-dead-enum-measured": ["binding_basis"],
    "entity.status-dead-value-candidate": ["current_status"],
    "relation.unknown-type": ["relation_type"],
    "entity.smuggled-field": ["legacy_name"],
    "binding.closed-null-valid_to": ["valid_to"],
    "binding.open-with-valid_to": ["valid_to"],
    "observation.partial-no-warrant": ["evidence_refs"],
    "bridge.admitted-no-evidence": ["evidence_refs"],
    "bridge.origin-no-evidence": ["evidence_refs"],
    "bridge.corroborated-no-evidence": ["evidence_refs"],
    "bridge.held-no-named-item": ["held_on"],
    "bridge.inadmissible-no-owner": ["store_owner"],
    "bridge.rejected-no-adjudicator": ["adjudicated_by"],
    "bridge.candidate-with-adjudicator": ["adjudicated_by"],
    "bridge.symbol-plane-no-firm-scope": ["firm_scope"],
    "bridge.dead-basis-measured": ["claim_origin"],
    "bridge.held_on-outside-held": ["held_on"],
    "bridge.store_owner-outside-inadmissible": ["store_owner"],
    "mv.complete-with-absent-components": ["absent_components"],
    "ce.delta-summary-on-verified": ["delta_summary"],
    "mint.checked-no-evidence": ["evidence_refs"],
    "mint.wrong-serial-form": ["serial_form"],
    "mint.missing-preflight": ["collision_preflight"],
    # ROUND 4 / v0.3-candidate
    "lce.superseded-without-successor": ["superseding_version_id"],
    "lce.decommissioned-with-successor": ["superseding_version_id"],
    "lce.missing-evidence": ["evidence_refs"],
    "lce.unknown-kind": ["event_kind"],
    "lce.successor-not-a-version-id": ["superseding_version_id"],
    "bev.unknown-kind": ["event_kind"],
    "bev.binding-ref-wrong-shape": ["binding_id"],
    "bev.missing-actor": ["actor"],
    "aep.missing-authority": ["authority_id"],
    "aep.empty-authority": ["authority_id"],
    "aep.unknown-kind": ["event_kind"],
    "contest.lifecycle-kind-without-event-ref": ["target_event_id"],
    "contest.lifecycle-kind-with-entity-ref": ["target_entity_serial"],
    "contest.entity-kind-with-event-ref": ["target_event_id"],
    "contest.binding-kind-with-event-ref": ["target_event_id"],
    "contest.event-ref-wrong-shape": ["target_event_id"],
    "contest.consequence-not-a-record-id": ["consequence_refs"],
    "contest.consequence-empty-list": ["consequence_refs"],
    "mig.ref-not-a-record-id": ["migrated_record_ref"],
    "relation.supersedes-wrong-shape": ["supersedes"],
    "bridge.supersedes-wrong-shape": ["supersedes"],
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
        normalization_version=_DEL, evidence_refs=["obs:" + ULID_B])
    add("observation.method-without-fingerprint", "state_observation",
        ["dependentRequired"], failure_state="partial", fingerprint=_DEL,
        normalization_version=_DEL, evidence_refs=["obs:" + ULID_B])
    # ARM-1 adjudication (ARM1_ADJUDICATION.md, cut 2): a partial observation names what it could
    # not see -- partial-without-warrant is indistinguishable from observed-with-a-field-missing
    add("observation.partial-no-warrant", "state_observation", ["required"],
        failure_state="partial")
    add("observation.substrate-unavailable-carries-fingerprint", "state_observation",
        ["not"], failure_state="substrate_unavailable")
    # R2-5 absence cell (round-2 charter; the GPT review's item)
    add("observation.absent-carries-fingerprint", "state_observation", ["not"],
        failure_state="observed_absent", evidence_refs=["obs:" + ULID_A])
    add("observation.absent-no-warrant", "state_observation", ["required"],
        failure_state="observed_absent", fingerprint=_DEL, fingerprint_method=_DEL,
        normalization_version=_DEL)
    # R2-1 referent family, two-directional BY IDIOM on both carrying records
    add("observation.invariant-with-referent-fabric", "state_observation", ["not"],
        referent_fabric_id="laptop")
    add("observation.fabric-local-without-fabric", "state_observation", ["required"],
        referent_scope="fabric_local")
    add("observation.fabric-local-with-device", "state_observation", ["not"],
        referent_scope="fabric_local", referent_fabric_id="laptop",
        referent_device_id="some-laptop")
    add("observation.device-local-missing-device", "state_observation", ["required"],
        referent_scope="device_local", referent_fabric_id="laptop")
    add("binding.invariant-with-referent-fabric", "entity_binding", ["not"],
        referent_fabric_id="laptop")
    add("binding.fabric-local-without-fabric", "entity_binding", ["required"],
        referent_scope="fabric_local")
    add("binding.device-local-missing-both-keys", "entity_binding", ["required"],
        referent_scope="device_local")
    add("run.missing-execution-fabric", "materialization_run", ["required"],
        executed_on_fabric=_DEL)
    # LAW 3 intervals (DT-4)
    add("binding.missing-valid-from", "entity_binding", ["required"], valid_from=_DEL)
    add("binding.closed-null-valid_to", "entity_binding", ["type"], status="closed")
    # ARM-1 adjudication (ARM1_ADJUDICATION.md, cut 1): an OPEN binding carrying an end instant is
    # a closed binding wearing open's label -- the mirror of DT-4
    add("binding.open-with-valid_to", "entity_binding", ["type"], status="open",
        valid_to="commit:9fc70e31a1")
    # LAW 4 locality (DT-7 / DT-8)
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
        verification_standing="corroborated", claim_origin="producer_declared",
        evidence_refs=_DEL)
    add("relation.evidence-empty-list", "identity_relation", ["minItems"],
        verification_standing="corroborated", evidence_refs=[])
    # R2-2 LANDING. (b) the enum-set forbid arm SHRANK when superseded left the axis -- COO~X 77156
    # asked for an explicit mutant on the narrowed set rather than trust the diff
    add("relation.corroborated-with-adjudicator", "identity_relation", ["not"],
        verification_standing="corroborated", adjudicated_by="3.0.0_SA_CVO~X")
    # (d) retirement: the terminal event with no successor, two-directional
    add("relation.retirement-with-object", "identity_relation", ["not"],
        relation_type="retirement")
    add("relation.non-retirement-without-object", "identity_relation", ["required"],
        object_serial=_DEL)
    # (f) status_basis: REQUIRED, exact-key, authored-only pre-WP-3
    add("entity.no-status-basis", "entity", ["required"], status_basis=_DEL)
    add("entity.status-basis-derived", "entity", ["const"],
        status_basis={"current_status": "derived"})
    add("bridge.status-basis-partial-map", "bridge_assertion", ["required"],
        status_basis={"verification_standing": "authored"})
    add("binding.status-basis-extra-key", "entity_binding", ["additionalProperties"],
        status_basis={"status": "authored", "valid_to": "authored"})
    # (c) contest_event: typed target + total event vocabulary, every arm two-directional or ruled
    add("contest.entity-kind-with-binding-ref", "contest_event", ["not"],
        target_binding_id=f"bind:{ULID_A}")
    add("contest.binding-kind-without-ref", "contest_event", ["required"],
        target_kind="binding", target_entity_serial=_DEL)
    add("contest.opened-without-basis", "contest_event", ["required"], basis=_DEL)
    add("contest.opened-with-outcome", "contest_event", ["not"], outcome="dismissed")
    add("contest.resolved-without-adjudicator", "contest_event_resolved", ["required"],
        adjudicated_by=_DEL)
    add("contest.upheld-without-consequence", "contest_event_resolved", ["required"],
        consequence_refs=_DEL)
    add("contest.dismissed-with-consequence", "contest_event_resolved", ["not"],
        outcome="dismissed")
    # ROUND 3 REWORK-2 (CRO~X at bf6fbe53d9): merged names its SURVIVOR by a typed field, never
    # an untyped ref in consequence_refs -- two-directional against upheld
    add("contest.merged-without-survivor", "contest_event_resolved", ["required"],
        outcome="merged", consequence_refs=_DEL)
    add("contest.merged-with-consequence", "contest_event_resolved", ["not"],
        outcome="merged", surviving_contest_id=f"ct:{ULID_C}")
    add("contest.upheld-with-survivor", "contest_event_resolved", ["not"],
        surviving_contest_id=f"ct:{ULID_C}")
    add("contest.survivor-not-a-contest-id", "contest_event_resolved", ["pattern"],
        outcome="merged", consequence_refs=_DEL, surviving_contest_id=f"rel:{ULID_C}")
    # ROUND 3 REWORK-1 (CRO~X): the retirement REASON lives on evidence_refs (sec 3.12) -- a
    # producer-declared retirement with no evidence validated
    add("relation.retirement-without-evidence", "identity_relation", ["required"],
        relation_type="retirement", object_serial=_DEL, claim_origin="producer_declared",
        evidence_refs=_DEL)
    # (a) migration receipt: a rewrite without its evidence is the laundering defect by the remedy
    add("mig.missing-evidence", "migration_receipt", ["required"], evidence_refs=_DEL)
    # ROUND 3 R3-CRO-5/6/8/10/11 (CRO~X at 36a5514df8): frontier completeness + locality +
    # availability, surface publication state, coherence target resolution
    add("frontier.missing-expected-count", "source_frontier", ["required"], expected_count=_DEL)
    _e = copy.deepcopy(FIXTURES["source_frontier"]["entries"][0])
    add("frontier.entry-missing-canonical-key", "source_frontier", ["required"],
        entries=[{k: x for k, x in _e.items() if k != "canonical_key"}])
    add("frontier.entry-unavailable-without-absence-evidence", "source_frontier", ["required"],
        entries=[dict(_e, availability="unavailable")])
    add("frontier.entry-available-with-absence-evidence", "source_frontier", ["not"],
        entries=[dict(_e, absence_evidence="probe:ENOENT")])
    add("frontier.entry-device-local-without-device", "source_frontier", ["required"],
        entries=[dict(_e, referent_scope="device_local", referent_fabric_id="laptop")])
    add("frontier.entry-invariant-with-fabric", "source_frontier", ["not"],
        entries=[dict(_e, referent_fabric_id="laptop")])
    add("surface.published-without-published-at", "surface_version_published", ["required"],
        published_at=_DEL)
    add("surface.unpublished-with-published-at", "surface_version", ["not"], published_at=TS2)
    add("surface.unpublished-with-published-ref", "surface_version", ["type"],
        published_ref="kuzu:prod/current")
    add("surface.published-with-null-ref", "surface_version_published", ["type"],
        published_ref=None)
    # R3-CVO-5: the declared null carrier must be PRESENT, not merely null-if-present
    add("surface.unpublished-without-published-ref", "surface_version", ["required"],
        published_ref=_DEL)
    add("coherence.latest-without-resolved-head", "coherence_evaluation_latest", ["required"],
        resolved_target_ref=_DEL)
    add("coherence.declared-release-with-resolved-head", "coherence_evaluation", ["not"],
        resolved_target_ref="nessie:main")
    # honesty conditionals
    add("matversion.partial-without-absent-components", "materializer_version",
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
        claim_origin="independently_observed", evidence_refs=_DEL)
    add("observation.observed-with-nothing", "state_observation", ["required"],
        fingerprint=_DEL, fingerprint_method=_DEL, normalization_version=_DEL)
    add("observation.normalization-alone", "state_observation", ["dependentRequired"],
        failure_state="partial", fingerprint=_DEL, fingerprint_method=_DEL,
        evidence_refs=["obs:" + ULID_B])
    # R2-3 warrants (round-2 batch 1: CRO~X gap 2 + COO~X 76588)
    add("binding.independently-observed-no-evidence", "entity_binding", ["required"],
        evidence_refs=_DEL)
    add("materializer.superseded-no-successor", "materializer", ["required"],
        current_status="superseded")
    # ROUND-2 BATCH 2 (DT-R2-1/DT-R2-2 + CRO~X R2-3 PARTIAL)
    add("materializer.active-with-successor", "materializer", ["not"],
        superseded_by_version=f"matv:{ULID_B}")
    add("entity.contested-no-adjudicator", "entity", ["required"],
        current_status="contested")
    add("entity.active-with-adjudicator", "entity", ["not"],
        adjudicated_by="1.0.0_SA_CTO~X")
    add("relation.unverified-with-adjudicator", "identity_relation", ["not"],
        adjudicated_by="3.0.0_SA_CVO~X")
    add("relation.rule-derived-no-evidence", "identity_relation", ["required"],
        evidence_refs=_DEL)
    add("binding.model-inferred-no-evidence", "entity_binding", ["required"],
        binding_basis="model_inferred", evidence_refs=_DEL)
    # R2-8 BRIDGE_ASSERTION (the first load-bearing consumer; CV-1's carried requirement lands)
    add("bridge.admitted-no-evidence", "bridge_assertion", ["required"],
        registry_standing="admitted", claim_origin="producer_declared",
        verification_standing="unverified", evidence_refs=_DEL)
    add("bridge.origin-no-evidence", "bridge_assertion", ["required"],
        evidence_refs=_DEL)
    add("bridge.corroborated-no-evidence", "bridge_assertion", ["required"],
        verification_standing="corroborated", claim_origin="producer_declared",
        evidence_refs=_DEL)
    add("bridge.held-no-named-item", "bridge_assertion", ["required"],
        registry_standing="held")
    add("bridge.inadmissible-no-owner", "bridge_assertion", ["required"],
        registry_standing="inadmissible")
    add("bridge.rejected-no-adjudicator", "bridge_assertion", ["required"],
        registry_standing="rejected")
    add("bridge.candidate-with-adjudicator", "bridge_assertion", ["not"],
        adjudicated_by="3.0.0_SA_CVO~X")
    add("bridge.symbol-plane-no-firm-scope", "bridge_assertion", ["required"],
        firm_scope=_DEL)
    add("bridge.dead-basis-measured", "bridge_assertion", ["enum"],
        claim_origin="measured")
    # R2-7 MINT_RECEIPT (LAW 1's compensating control, defined)
    add("mint.checked-no-evidence", "mint_receipt", ["required"], evidence_refs=_DEL)
    add("mint.wrong-serial-form", "mint_receipt", ["const"], serial_form="ulid26_uppercase")
    add("mint.missing-preflight", "mint_receipt", ["required"], collision_preflight=_DEL)
    # ARM-4 adjudication: the four upheld forbid-mirrors (21 candidates ruled NO with reasons)
    add("bridge.held_on-outside-held", "bridge_assertion", ["not"], held_on="LD-0999")
    add("bridge.store_owner-outside-inadmissible", "bridge_assertion", ["not"],
        store_owner="0.8.0_AE_CloudComp")
    add("mv.complete-with-absent-components", "materializer_version", ["not"],
        bundle_completeness="complete", configuration_digest=SHA,
        declared_opinions_digest=SHA, dependency_lock_digest=SHA,
        normalizer_versions=["norm-v1"], runtime_contract_version="rc-1",
        source_tree_digest=SHA)
    add("ce.delta-summary-on-verified", "coherence_evaluation", ["not"],
        delta_summary="3 axes moved")
    # enum discipline (F4 renames; dead enums stay dead)
    add("binding.basis-is-dead-enum-measured", "entity_binding", ["enum"],
        binding_basis="measured")
    add("entity.status-dead-value-candidate", "entity", ["enum"], current_status="candidate")
    add("relation.unknown-type", "identity_relation", ["enum"], relation_type="same_as")
    add("entity.smuggled-field", "entity", ["additionalProperties"], legacy_name="c2_instances")
    # ROUND 4 / v0.3-candidate -- one negative per then-arm of the three new carriers, the widened
    # contest target (every direction), the two typings, and the backward supersedes shape
    add("lce.superseded-without-successor", "lifecycle_event", ["required"],
        superseding_version_id=_DEL)
    add("lce.decommissioned-with-successor", "lifecycle_event", ["not"],
        event_kind="materializer_decommissioned")
    add("lce.missing-evidence", "lifecycle_event", ["required"], evidence_refs=_DEL)
    add("lce.unknown-kind", "lifecycle_event", ["enum"], event_kind="materializer_retired")
    add("lce.successor-not-a-version-id", "lifecycle_event", ["pattern"],
        superseding_version_id=f"mat:{ULID_C}")
    add("bev.unknown-kind", "binding_event", ["enum"], event_kind="disputed")
    add("bev.binding-ref-wrong-shape", "binding_event", ["pattern"], binding_id=f"ent:{ULID_A}")
    add("bev.missing-actor", "binding_event", ["required"], actor=_DEL)
    add("aep.missing-authority", "authority_epoch_event", ["required"], authority_id=_DEL)
    add("aep.empty-authority", "authority_epoch_event", ["minLength"], authority_id="")
    add("aep.unknown-kind", "authority_epoch_event", ["enum"], event_kind="revoked")
    add("contest.lifecycle-kind-without-event-ref", "contest_event_lifecycle", ["required"],
        target_event_id=_DEL)
    add("contest.lifecycle-kind-with-entity-ref", "contest_event_lifecycle", ["not"],
        target_entity_serial=f"ent:{ULID_A}")
    add("contest.entity-kind-with-event-ref", "contest_event", ["not"],
        target_event_id=f"lce:{ULID_A}")
    add("contest.binding-kind-with-event-ref", "contest_event_resolved", ["not"],
        target_event_id=f"lce:{ULID_A}")
    add("contest.event-ref-wrong-shape", "contest_event_lifecycle", ["pattern"],
        target_event_id=f"ctev:{ULID_A}")
    add("contest.consequence-not-a-record-id", "contest_event_resolved", ["pattern"],
        consequence_refs=["see the ticket"])
    add("contest.consequence-empty-list", "contest_event_resolved", ["minItems"],
        consequence_refs=[])
    add("mig.ref-not-a-record-id", "migration_receipt", ["pattern"],
        migrated_record_ref="materializer_version#partial_legacy")
    add("relation.supersedes-wrong-shape", "identity_relation_superseding", ["pattern"],
        supersedes=f"br:{ULID_A}")
    add("bridge.supersedes-wrong-shape", "bridge_assertion", ["pattern"],
        supersedes=f"rel:{ULID_A}")
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
        ("sem.bridge-self-loop",
         _mk("bridge_assertion", object_entity_serial=f"ent:{ULID_A}")),
        ("sem.relation-entirely-self-cited",
         _mk("identity_relation", verification_standing="corroborated",
             claim_origin="producer_declared", evidence_refs=[f"rel:{ULID_A}"])),
        ("sem.observation-cites-own-vintage",
         _mk("state_observation", evidence_refs=["commit:9fc70e31a1"])),
        ("sem.frontier-noncanonical-key",
         _mk("source_frontier", entries=[dict(FIXTURES["source_frontier"]["entries"][0],
                                              canonical_key="file/C:/warehouse/tmp/../catalog.db")])),
        ("sem.frontier-same-canonical-key-two-versions",
         _mk("source_frontier", completeness="partial", entries=[
             FIXTURES["source_frontier"]["entries"][0],
             dict(FIXTURES["source_frontier"]["entries"][0], source_serial=f"ent:{ULID_B}",
                  source_version="snapshot:1")])),
        ("sem.frontier-complete-count-mismatch",
         _mk("source_frontier", expected_count=2)),
        ("sem.frontier-partial-costume",
         _mk("source_frontier", completeness="partial")),
        ("sem.frontier-overfull-denominator",
         _mk("source_frontier_partial", expected_count=1)),
        ("sem.frontier-complete-with-unavailable",
         _mk("source_frontier", entries=[dict(FIXTURES["source_frontier"]["entries"][0],
                                              availability="unavailable",
                                              absence_evidence="probe:ENOENT")])),
        ("sem.frontier-observed-after-run-start",
         [_mk("source_frontier", entries=[dict(FIXTURES["source_frontier"]["entries"][0],
                                               observed_at="2026-08-27T19:30:00Z")]),
          _mk("materialization_run")]),
        ("sem.surface-not-in-run-outputs",
         [_mk("surface_version", surface_version_id=f"sv:{ULID_C}"), _mk("materialization_run")]),
        ("sem.surface-frontier-disagrees-with-run",
         [_mk("surface_version", source_frontier_id=f"sf:{ULID_B}"), _mk("materialization_run")]),
        ("sem.published-from-failed-run",
         [_mk("surface_version_published"), _mk("materialization_run", run_status="failed")]),
        ("sem.published-before-run-completed",
         [_mk("surface_version_published", published_at=TS), _mk("materialization_run")]),
        ("sem.frontier-duplicate-coordinate",
         _mk("source_frontier", entries=[
             FIXTURES["source_frontier"]["entries"][0],
             dict(FIXTURES["source_frontier"]["entries"][0],
                  source_version="snapshot:9999999999999999999"),
         ])),
        # ROUND 4 / v0.3-candidate
        ("sem.relation-supersedes-self",
         _mk("identity_relation_superseding", supersedes=f"rel:{ULID_B}")),
        ("sem.bridge-supersedes-self",
         _mk("bridge_assertion", supersedes=f"br:{ULID_A}")),
        ("sem.lifecycle-superseded-by-own-version",
         [_mk("lifecycle_event", superseding_version_id=f"matv:{ULID_B}"),
          _mk("materializer_version_complete")]),
        ("sem.lifecycle-contest-two-replacements",
         _mk("contest_event_lifecycle", consequence_refs=[f"lce:{ULID_B}", f"lce:{ULID_C}"])),
        ("sem.lifecycle-contest-replacement-wrong-kind",
         [_mk("contest_event_lifecycle", consequence_refs=[f"lce:{ULID_B}"]), _mk("lifecycle_event"),
          _mk("lifecycle_event_decommissioned")]),
        ("sem.lifecycle-contest-replacement-is-target",
         [_mk("contest_event_lifecycle", consequence_refs=[f"lce:{ULID_A}"]), _mk("lifecycle_event")]),
    ]


_ISO_FIELDS = ["minted_at", "observed_at", "asserted_at", "started_at", "completed_at",
               "built_at", "evaluated_at", "valid_from", "occurred_at"]
_PRIMARY_ID = {"entity": "entity_serial", "entity_binding": "binding_id",
               "mint_receipt": "receipt_id", "contest_event": "event_id",
               "migration_receipt": "receipt_id",
               "lifecycle_event": "event_id", "binding_event": "event_id",
               "authority_epoch_event": "event_id",
               "bridge_assertion": "bridge_id",
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


def _batch_provenance_errors(instances):
    """R3-CRO-7/9/10: cross-record checks that are decidable when BOTH records are in the batch
    (frontier <-> run temporal order; surface <-> run membership + frontier identity; publication
    only from a SUCCEEDED run and never before it completed). Beyond the batch: ledger, sec 6."""
    errs = []
    by_id = {}
    for i, inst in enumerate(instances):
        if isinstance(inst, dict):
            pid = _PRIMARY_ID.get(inst.get("record_type"))
            if pid and inst.get(pid):
                by_id[inst[pid]] = (i, inst)
    for i, inst in enumerate(instances):
        if not isinstance(inst, dict):
            continue
        rt = inst.get("record_type")
        if rt == "materialization_run":
            sf = by_id.get(inst.get("source_frontier_id"))
            if sf:
                latest = max((e.get("observed_at", "") for e in sf[1].get("entries", [])
                              if isinstance(e, dict)), default="")
                if latest and isinstance(inst.get("started_at"), str) and latest > inst["started_at"]:
                    errs.append(f"[{i}] materialization_run: consumes frontier [{sf[0]}] whose latest "
                                f"observation {latest} is AFTER started_at {inst['started_at']} -- "
                                "temporal impossibility (R3-CRO-7)")
        if rt == "surface_version":
            run = by_id.get(inst.get("producing_run_id"))
            if run:
                r = run[1]
                if inst.get("surface_version_id") not in (r.get("output_surface_version_ids") or []):
                    errs.append(f"[{i}] surface_version: names producing_run_id {r.get('run_id')} whose "
                                "output_surface_version_ids does NOT include this surface (R3-CRO-9)")
                if inst.get("source_frontier_id") != r.get("source_frontier_id"):
                    errs.append(f"[{i}] surface_version: source_frontier_id {inst.get('source_frontier_id')} "
                                f"DISAGREES with its producing run's {r.get('source_frontier_id')} (R3-CRO-9)")
                if inst.get("publication_state") == "published":
                    if r.get("run_status") != "succeeded":
                        errs.append(f"[{i}] surface_version: PUBLISHED from a run with run_status="
                                    f"{r.get('run_status')} -- only a succeeded run's output may become "
                                    "authority (R3-CRO-10)")
                    c = r.get("completed_at")
                    if isinstance(c, str) and isinstance(inst.get("published_at"), str) and inst["published_at"] < c:
                        errs.append(f"[{i}] surface_version: published_at {inst['published_at']} precedes "
                                    f"the producing run's completed_at {c} (R3-CRO-10)")
    return errs


def semantic_errors(instances):
    """Field-pair, calendar, and batch checks the schema cannot express (sec 6 items 4/5/7).

    R3-CRO-16: the input is a LIST of records and nothing else. A dict passed here used to be
    iterated over its KEYS, every key skipped as a non-dict, and the clean shape [] returned -- a
    wrong-container misuse read as a validator PASS (it nearly upheld a planted claim). A non-list
    RAISES; a non-dict member is an ERROR entry, never a silent skip."""
    if not isinstance(instances, list):
        raise TypeError("semantic_errors takes a LIST of record dicts; got %s -- wrap a single "
                        "record as [record] (R3-CRO-16: a dict iterates its keys and returns a "
                        "clean [])" % type(instances).__name__)
    errs = _batch_provenance_errors(instances)
    seen = {}
    for i, inst in enumerate(instances):
        if not isinstance(inst, dict):
            errs.append(f"[{i}] NOT A RECORD: batch member is {type(inst).__name__}, not an object "
                        "(R3-CRO-16 -- a member the checks cannot read is an error, not a skip)")
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
        if rt == "bridge_assertion" and inst.get("subject_entity_serial") == inst.get("object_entity_serial"):
            errs.append(f"[{i}] bridge_assertion: SELF-BRIDGE "
                        f"{inst.get('subject_entity_serial')} -- an entity bridged to itself "
                        "asserts nothing (sec 3.12's self-loop class, bridge form)")
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
            # R3-CRO-6: the coordinate key reads only schema-reachable fields (the old key read a
            # dead `fabric_id`); R3-CRO-5: uniqueness ALSO runs on the declared canonical_key, and
            # an obviously non-canonical key is rejected (the mechanical half; sec 6 limit 12)
            coords = {}
            canon = {}
            entries = [e for e in inst.get("entries", []) if isinstance(e, dict)]
            for j, e in enumerate(entries):
                key = (e.get("source_serial"), e.get("identity_space"), e.get("authority_ref"),
                       e.get("referent_fabric_id"), e.get("referent_device_id"))
                if key in coords:
                    errs.append(f"[{i}] source_frontier: entries [{coords[key]}] and [{j}] pin "
                                f"the SAME source coordinate {key} -- a frontier is a vector, one "
                                "version per coordinate (sec 6 / R2-6)")
                else:
                    coords[key] = j
                ck = e.get("canonical_key")
                if isinstance(ck, str):
                    if "/../" in ck or "/./" in ck or "//" in ck or ck.endswith("/"):
                        errs.append(f"[{i}] source_frontier: entry [{j}] canonical_key {ck!r} is "
                                    "NOT canonical (dot-segments / empty segments / trailing "
                                    "slash) -- normalize under normalization_version (R3-CRO-5)")
                    prev = canon.get(ck)
                    if prev is not None and entries[prev].get("source_version") != e.get("source_version"):
                        errs.append(f"[{i}] source_frontier: entries [{prev}] and [{j}] share "
                                    f"canonical_key {ck!r} with DIFFERENT source_version -- one "
                                    "semantic coordinate double-counted (R3-CRO-5)")
                    canon.setdefault(ck, j)
            # R3-CRO-8 / R3-CVO-4: completeness is a CLAIM with a denominator, never an adjective --
            # and BOTH values are constrained (partial is not the free cell)
            n_exp = inst.get("expected_count")
            if isinstance(n_exp, int) and n_exp < len(entries):
                errs.append(f"[{i}] source_frontier: {len(entries)} entries exceed expected_count="
                            f"{n_exp} -- a frontier cannot carry more sources than it expected (R3-CVO-4)")
            if inst.get("completeness") == "partial" and isinstance(n_exp, int):
                short = n_exp > len(entries)
                absent = any(e.get("availability") == "unavailable" for e in entries)
                if not short and not absent:
                    errs.append(f"[{i}] source_frontier: completeness=partial with expected_count == "
                                f"{len(entries)} entries and none unavailable -- nothing is missing; "
                                "partial is a costume on a complete frontier (R3-CVO-4)")
            if inst.get("completeness") == "complete":
                if inst.get("expected_count") != len(entries):
                    errs.append(f"[{i}] source_frontier: completeness=complete but expected_count="
                                f"{inst.get('expected_count')} vs {len(entries)} entries (R3-CRO-8)")
                if any(e.get("availability") == "unavailable" for e in entries):
                    errs.append(f"[{i}] source_frontier: completeness=complete with an UNAVAILABLE "
                                "entry -- a complete frontier has no absent source (R3-CRO-8)")
        if rt == "materializer_version" and inst.get("supersedes") == inst.get("version_id") \
                and inst.get("supersedes") is not None:
            errs.append(f"[{i}] materializer_version: supersedes itself")
        # ROUND 4 item 1: the backward link on an assertion is a different record, never itself
        if rt in ("identity_relation", "bridge_assertion") and inst.get("supersedes") is not None \
                and inst.get("supersedes") == inst.get(_PRIMARY_ID[rt]):
            errs.append(f"[{i}] {rt}: supersedes itself (round 4 item 1 -- the head of a chain "
                        "names its PREDECESSOR)")
        # ROUND 4 item 4: process-level supersession points at a version of ANOTHER materializer;
        # decidable in-batch when the version record is present (beyond the batch: the ledger,
        # WP3 row 7 L-07-cross-materializer-supersedes-rejected)
        if rt == "lifecycle_event" and inst.get("event_kind") == "materializer_superseded":
            for j, other in enumerate(instances):
                if isinstance(other, dict) and other.get("record_type") == "materializer_version" \
                        and other.get("version_id") == inst.get("superseding_version_id") \
                        and other.get("materializer_serial") == inst.get("materializer_serial"):
                    errs.append(f"[{i}] lifecycle_event: materializer_superseded by version [{j}] of "
                                "the SAME materializer -- that is a version succession "
                                "(materializer_version.supersedes), not a process supersession "
                                "(round 4 item 4)")
        # ROUND 4 item 8 (R3-CVO-12 condition 3): an upheld contest on a lifecycle event names
        # exactly ONE replacement of the same event_kind and materializer_serial; decidable
        # in-batch when the target and the replacement are present
        if rt == "contest_event" and inst.get("target_kind") == "lifecycle_event" \
                and inst.get("outcome") == "upheld":
            cons = inst.get("consequence_refs") or []
            if len(cons) != 1:
                errs.append(f"[{i}] contest_event: upheld on a lifecycle event names {len(cons)} "
                            "consequences -- exactly ONE replacement event (R3-CVO-12 c3)")
            by_id = {o.get("event_id"): o for o in instances
                     if isinstance(o, dict) and o.get("record_type") == "lifecycle_event"}
            tgt = by_id.get(inst.get("target_event_id"))
            for c in cons:
                rep = by_id.get(c)
                if tgt and rep and (rep.get("event_kind") != tgt.get("event_kind")
                                    or rep.get("materializer_serial") != tgt.get("materializer_serial")):
                    errs.append(f"[{i}] contest_event: replacement {c} differs from the contested "
                                "event in event_kind or materializer_serial (R3-CVO-12 c3)")
                if rep is not None and c == inst.get("target_event_id"):
                    errs.append(f"[{i}] contest_event: the replacement IS the contested event "
                                "(R3-CVO-12 c3 -- a new event id)")
        if rt == "materialization_run":
            s, c = inst.get("started_at"), inst.get("completed_at")
            if isinstance(s, str) and isinstance(c, str) and _parse_iso(s) and _parse_iso(c):
                if c < s:
                    errs.append(f"[{i}] materialization_run: completed_at precedes started_at")
        # CVR2-1: syntactic self-citation (sec 6 limit 2's mechanical subcase, moved to the
        # partially-mechanical class). ENTIRELY-self-cited evidence defeats the warrant.
        refs = inst.get("evidence_refs")
        if isinstance(refs, list) and refs:
            self_tokens = {inst.get(_PRIMARY_ID.get(rt, "")), inst.get("subject_serial"),
                           inst.get("entity_serial"), inst.get("source_vintage"),
                           inst.get("source_native_key")}
            self_tokens.discard(None)
            self_hits = [r for r in refs if r in self_tokens]
            if self_hits and len(self_hits) == len(refs):
                errs.append(f"[{i}] {rt}: evidence_refs is ENTIRELY self-citation "
                            f"({self_hits}) -- a warrant that cites only its own record is "
                            "no warrant (sec 6 limit 2, mechanical subcase / CVR2-1)")
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
    axes = {"claim_origin": 5, "verification_standing": 3, "registry_standing": 6,
            "referent_scope": 3}
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
        targets = ATTACK_TARGETS.get(name)
        if targets is None:
            neg_bad.append(f"mutant {name} UNSCOREABLE -- no declared attack target (add it to "
                           "ATTACK_TARGETS; an undeclared mutant cannot dilute the denominator)")
            continue
        # PATH-GRAINED (COO~X 76662): the matching-keyword error must REFERENCE a declared
        # target field -- same-keyword drift at an undeclared field no longer satisfies it.
        hit = False
        for e in errs:
            if e.validator not in expected:
                continue
            locus = e.json_path + " " + str(list(e.path)) + " " + e.message
            if any(t in locus for t in targets):
                hit = True
                break
        if not hit:
            got = sorted({e.validator for e in errs})
            neg_bad.append(f"mutant {name} rejected but NOT at its declared target "
                           f"{targets}: keywords {got} at other loci (same-keyword drift, "
                           "or the rule moved)")
    print(f"NEGATIVE ARM: {len(muts) - len(neg_bad)} of {len(muts)} mutants reject FOR THEIR "
          f"NAMED REASON AT THEIR DECLARED TARGET")
    fails += neg_bad

    # DRIFT META-CONTROL (COO~X 76662's injection, made standing): a record whose ONLY defect is
    # the drift (corrupt serial, true target intact) must NOT satisfy a target-declared assertion.
    masked = _mk("state_observation")
    masked["entity_serial"] = masked["entity_serial"].upper()
    merrs = _leaf_errors(_branch_validator(schema, "state_observation"), masked)
    dtargets = ATTACK_TARGETS["observation.fingerprint-without-normalization"]
    mhit = any(e.validator in {"required", "dependentRequired"} and
               any(t in (e.json_path + " " + e.message) for t in dtargets) for e in merrs)
    if merrs and not mhit:
        print("DRIFT META-CONTROL: a drift-only rejection does NOT satisfy a target-declared "
              "assertion (the 76662 class is now detectable)")
    else:
        fails.append("DRIFT META-CONTROL: a drift-only rejection SATISFIED the assertion -- "
                     "path-grained scoring is not discriminating")

    # SEMANTIC ARM: semantic mutants must each produce >=1 semantic error.
    smuts = _semantic_mutants()
    sem_bad = []
    for name, payload in smuts:
        batch = payload if isinstance(payload, list) else [payload]
        if not semantic_errors(batch):
            sem_bad.append(f"semantic mutant {name} produced 0 errors")
    print(f"SEMANTIC ARM: {len(smuts) - len(sem_bad)} of {len(smuts)} semantic mutants FIRE")
    fails += sem_bad

    # R3-CRO-16 CONTAINER CONTROLS: the arm above only proves the LIST path fires. The misuse
    # path (a dict) must RAISE, a non-dict member must ERROR, and the valid list must stay clean.
    api_bad = []
    try:
        semantic_errors(_mk("state_observation"))
        api_bad.append("semantic_errors ACCEPTED a dict and returned silently (R3-CRO-16)")
    except TypeError:
        pass
    if not any("NOT A RECORD" in e for e in semantic_errors([_mk("entity"), "not-a-record"])):
        api_bad.append("semantic_errors SKIPPED a non-dict batch member silently (R3-CRO-16)")
    if semantic_errors([_mk("entity")]):
        api_bad.append("semantic_errors errored on a valid single-record list (control broken)")
    print(f"CONTAINER CONTROLS: {3 - len(api_bad)} of 3 (dict RAISES / non-dict member ERRORS / "
          "valid list clean)")
    fails += api_bad

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
