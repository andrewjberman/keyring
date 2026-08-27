from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parent
WORKSPACE = Path(__file__).resolve().parents[5]
SCHEMA = ROOT / "schemas" / "layer_contracts_and_checkpoints.v1.schema.json"
DOCUMENT = ROOT / "layer_contracts_and_checkpoints.v1.json"
L0_MANIFEST = WORKSPACE / "org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_MANIFEST/graph_object_manifest.json"
L0_RECEIPT = WORKSPACE / "org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_MANIFEST/graph_object_manifest.receipt.json"
LAYERS = ["L0", "L1", "L2", "L3", "L4"]
CHECKPOINTS = ["CP-L0-L1", "CP-L1-L2", "CP-L2-L3", "CP-L3-L4", "CP-L4-DONE"]
EXECUTABLE_NOW = {"L0", "L2_STRUCTURE", "L2_BEHAVIOR"}
DEPENDENCY_EDGES = {
    ("L0", "L1"),
    ("L1", "L2_FUSION_ADMISSIBLE"),
    ("L1", "L3"),
    ("L3", "L4"),
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def semantic_errors(document: dict) -> list[str]:
    errors: list[str] = []
    contract_status = document["contract_status"]
    if (
        contract_status["adoption_state"] != "proposed"
        or contract_status["operative_gate"]
        or contract_status["work_start_effect"] != "non_blocking_design_constraint"
        or not contract_status["l1_work_startable"]
        or contract_status["operative_transition_ready"]
    ):
        errors.append("proposed contract cannot gate work or claim an operative transition")
    post_rerun_queue = document["post_rerun_rule24_queue"]
    queued_findings = post_rerun_queue["findings"]
    expected_queued_findings = {
        "L0-R24-01": "empty_suffix_enumeration_interpretation",
        "L0-R24-02": "suffix_completeness_partition",
        "L0-R24-03": "repo_relative_path_rule24_partition",
        "L0-R24-04": "home_space_lifecycle_vocabulary",
        "L0-R24-05": "variant_suffix_source_authority",
    }
    expected_change_states = {
        "L0-R24-01": "unchanged",
        "L0-R24-02": "unchanged",
        "L0-R24-03": "unchanged",
        "L0-R24-04": "unchanged",
        "L0-R24-05": "new",
    }
    expected_rerun_effects = {
        "L0-R24-01": "metadata_only_no_current_emission",
        "L0-R24-02": "metadata_only_no_current_emission",
        "L0-R24-03": "metadata_only_no_current_emission",
        "L0-R24-04": "metadata_only_no_current_emission",
        "L0-R24-05": "emitted_authority_contradiction",
    }
    if (
        post_rerun_queue["queue_state"] != "open_until_post_rerun_remediation"
        or post_rerun_queue["frozen_schema_commit"] != "a767d213921dfa013eed546b39c27f73712e0ec6"
        or post_rerun_queue["frozen_schema_blob"] != "e6cba54189f9a6a14db6d6a47a8954135a74f142"
        or post_rerun_queue["freeze_exit_condition"] != "coordinated_rerun_emits_42_of_42_receivers_with_coherent_claim_status"
        or post_rerun_queue["promotion_condition"] != "evidence_that_finding_changes_an_emitted_value"
        or {row["finding_id"]: row["semantic_dimension"] for row in queued_findings} != expected_queued_findings
        or {row["finding_id"]: row["evidence_run_change_state"] for row in queued_findings} != expected_change_states
        or {row["finding_id"]: row["rerun_effect"] for row in queued_findings} != expected_rerun_effects
        or any(row["finding_state"] != "open" for row in queued_findings)
    ):
        errors.append("frozen shared-schema Rule 24 findings must remain open in the post-rerun queue")

    base_validation = document["post_rerun_base_validation"]
    evidence_pair = base_validation["evidence_pair"]
    structural = base_validation["structural_emission"]
    declarations = base_validation["declaration_measurement"]
    home_space = base_validation["home_space_measurement"]
    population = base_validation["population_completeness"]
    suffix_authority = base_validation["variant_suffix_authority"]
    lifecycle_coverage = base_validation["lifecycle_axis_coverage"]
    receipt_contract = base_validation["receipt_contract"]
    unknown_lifecycle = base_validation["unknown_lifecycle_expressibility"]
    remediation = base_validation["remediation_sequence"]
    if (
        base_validation["validation_state"] != "failed"
        or base_validation["release_gate_state"] != "held"
        or structural["manifest_part_count"] != 42
        or structural["frozen_schema_validation_error_count"] != 0
        or any(count != 42 for count in structural["receiver_presence_count"].values())
        or declarations["unknown_coherence_state"] != "coherent"
        or any(declarations[receiver] != {"declared_count": 0, "unknown_count": 42} for receiver in ("grain", "key", "failure_mode"))
        or home_space != {"repo_path_count": 25, "s3_uri_count": 14, "none_count": 3}
        or sum(home_space.values()) != 42
    ):
        errors.append("post-rerun Base record must separate structural emission from declaration and home-space distributions")
    if (
        population["assessment_state"] != "unmeasurable"
        or population["registered_part_count"] != 42
        or population["known_unsearched_entry_count"] != 12
        or population["known_unsearched_representation"] != "mixed_prose"
        or population["known_missing_subject_lower_bound"] < 2
        or set(population["known_missing_subject_ids"]) != {
            "org/modules/graph/comp_aws_cli.py",
            "infra/aws/lambda/globgrph/incremental_updater/lambda_function.py",
        }
        or population["coverage_fraction_claim_permitted"]
    ):
        errors.append("42-of-42 receiver presence cannot masquerade as complete substrate-population coverage")
    if (
        suffix_authority["observed_source_role"] != "removal_repertoire"
        or suffix_authority["required_source_role"] != "minting_producer"
        or suffix_authority["authority_match_state"] != "contradicted"
    ):
        errors.append("removal evidence cannot masquerade as variant minting authority")
    if (
        lifecycle_coverage["manifest_document"] != {
            "authorship_mode_state": "absent", "mutation_policy_state": "absent",
            "temporal_claim_state": "absent", "authority_role_state": "absent",
        }
        or lifecycle_coverage["receipt_document"] != {
            "authorship_mode_state": "absent", "mutation_policy_state": "absent",
            "temporal_claim_state": "absent", "authority_role_state": "absent",
        }
        or lifecycle_coverage["parts"] != {
            "part_count": 42, "authorship_mode_present_count": 0,
            "mutation_policy_present_count": 0, "temporal_claim_present_count": 42,
            "authority_role_present_count": 42,
        }
    ):
        errors.append("post-rerun lifecycle-axis coverage must preserve the measured document and part gaps")
    if (
        receipt_contract["document_kind_state"] != "absent"
        or receipt_contract["governing_schema_state"] != "absent"
        or receipt_contract["lifecycle_axes_state"] != "absent"
        or receipt_contract["input_closure_state"] != "incomplete"
        or set(receipt_contract["unbound_input_classes"]) != {
            "compiler_commit_and_home", "card_population_registry_blob",
            "card_population_registry_schema_blob", "base_manifest_blob",
            "card_to_part_map_blob", "substrate_card_schema_blob",
            "admitted_card_blobs", "structured_replay_digests",
        }
    ):
        errors.append("receipt contract cannot claim schema governance or replayable input closure before remediation")
    if (
        unknown_lifecycle != {
            "claim_status_token": "unknown",
            "unknown_lifecycle_axis_state": "absent",
            "terminal_transitional_partition_state": "inexpressible",
        }
        or remediation != {
            "current_pair_role": "pre_remediation_evidence_only",
            "next_step": "dt_receipt_contract_and_control_source_tranche",
            "shared_schema_step": "coordinated_before_final_emission",
            "final_pair_step": "new_authorized_run_after_shared_schema_remediation",
            "release_step": "base_pass_on_final_committed_pair",
        }
    ):
        errors.append("unknown lifecycle and remediation sequence must remain explicit and non-releasing")
    for label, path in (("manifest", L0_MANIFEST), ("receipt", L0_RECEIPT)):
        if not path.is_file():
            errors.append(f"post-rerun evidence {label} is absent from its exact home")
            continue
        raw = path.read_bytes()
        expected = evidence_pair[label]
        blob = hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()
        if (
            hashlib.sha256(raw).hexdigest() != expected["sha256"]
            or blob != expected["git_blob"]
            or expected["home"] != path.relative_to(WORKSPACE).as_posix()
        ):
            errors.append(f"post-rerun evidence {label} bytes do not match the frozen Base-validation pin")
    mission = document["mission"]
    if any((mission["new_directive"], mission["project_mint"], mission["registration_act"], mission["approval_gate"])):
        errors.append("D11 arc cannot mint, register, or introduce an approval gate")

    layers = document["layer_contracts"]
    if [row["layer_id"] for row in layers] != LAYERS:
        errors.append("layer contracts must contain L0 through L4 exactly and in order")
    for row in layers:
        lifecycle = row["deliverable"]["document_lifecycle"]
        if lifecycle["authorship_mode"] != "machine_generated":
            errors.append(f"{row['layer_id']}: compiled deliverable must be machine_generated")
        if not row["deliverable"]["generated_source_separation"]:
            errors.append(f"{row['layer_id']}: generated output must remain separated from authored sources")
    l4 = next((row for row in layers if row["layer_id"] == "L4"), None)
    if l4 and l4["deliverable"]["document_lifecycle"]["mutation_policy"] != "append_only":
        errors.append("L4 identity ledger must be append_only")

    baseline = document["starting_position"]
    if baseline["proposal_classification"] != "control_plane_spec_not_operative_layer_artifact":
        errors.append("proposal cannot count as operative layer progress")
    baseline_layers = baseline["layers"]
    if [row["layer_id"] for row in baseline_layers] != LAYERS:
        errors.append("starting position must contain L0 through L4 exactly and in order")
    for row in baseline_layers:
        if row["layer_id"] == "L0" and row["state"] != "partial":
            errors.append("measured starting position requires L0 partial")
        if row["layer_id"] != "L0":
            if row["state"] != "unbuilt" or row["operative_contract_artifacts"] != 0:
                errors.append(f"{row['layer_id']}: measured starting position is unbuilt with zero operative artifacts")
    l0_measurements = baseline_layers[0]["measurements"]
    if (
        l0_measurements.get("manifest_parts") != 42
        or l0_measurements.get("manifest_validation_error_count") != 0
        or l0_measurements.get("manifest_negative_control_error_count", 0) <= 0
    ):
        errors.append("L0 baseline must preserve the validated populated 42-part manifest and firing negative control")
    excluded = {row["path"] for row in baseline["homonym_exclusions"]}
    expected_homonyms = {
        "org/tier1_exec/4.0.0_SA_CRO~A/deliverables/SPEC_IDENTITY_SPINE_FAM_RESOLUTION_20260819.md",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/IDENTITY_SPINE_ARCHITECTURE_RATIFY_20260819.md",
    }
    if excluded != expected_homonyms:
        errors.append("starting position must exclude the two exact FAM/account identity-spine homonyms")

    overlap = document["design_measurements"]["cover_partition_baseline"]
    if overlap["single_system_members"] + overlap["two_system_members"] + overlap["three_system_members"] != overlap["total_members"]:
        errors.append("cover baseline system-count distribution must equal the measured population")
    multi_members = overlap["two_system_members"] + overlap["three_system_members"]
    if overlap["same_domain_multi_members"] + overlap["cross_domain_multi_members"] != multi_members:
        errors.append("cover baseline domain classes must exhaust multiply assigned members")
    if overlap["cross_domain_multi_members"] != 540:
        errors.append("cover baseline must retain the measured 540 cross-domain members")
    compile_baseline = document["design_measurements"]["wave3_manifest_compile_baseline"]
    if compile_baseline["enrich_existing_part_rows"] + compile_baseline["add_new_part_rows"] != compile_baseline["card_relation_rows"]:
        errors.append("wave3 enrichment and addition rows must exhaust the 13-row compile population")
    expected_new_parts = {
        "infra/aws/globgrph/kuzu_load.py",
        "infra/aws/globgrph/kuzu_stitch_load.py",
        "infra/aws/globgrph/snap_store.py",
    }
    if set(compile_baseline["new_part_subject_paths"]) != expected_new_parts:
        errors.append("wave3 new-part population must contain the three measured generic writers")
    if (
        compile_baseline["measurement_join_method"] != "indicative_substring_probe"
        or compile_baseline["compiler_join_requirement"] != "structured_card_artifact_ref_to_exact_part_id"
    ):
        errors.append("indicative substring measurement must not masquerade as the compiler join")
    release = document["design_measurements"]["l1_release_baseline"]
    if release["stores_exact_count"] != release["manifest_parts"]:
        errors.append("L1 release baseline must retain exact 42-of-42 store coverage")
    prose_counts = (
        release["grain_prose_substring_count"],
        release["key_prose_substring_count"],
        release["failure_mode_prose_substring_count"],
    )
    field_paths = release["operative_schema_field_paths_before_amendment"]
    if prose_counts != (7, 6, 3) or release["prose_measurement_method"] != "substring_count_not_semantic_coverage":
        errors.append("7/6/3 must remain labelled as prose counts, never semantic coverage")
    if (
        field_paths["measurement_method"] != "defined_property_path_extraction"
        or any(field_paths[field] != 0 for field in ("grain", "key", "failure_mode"))
    ):
        errors.append("operative schema structurally had zero grain key and failure-mode receiver paths")
    if release["wave3_completion_sufficient"] or not release["l1_work_startable"] or release["operative_transition_ready"]:
        errors.append("L1 work may start, but wave3 completion cannot establish operative transition readiness")

    receiver_grain = document["design_measurements"]["card_to_part_receiver_grain"]
    if (
        receiver_grain["card_trust_qualifies"] != "subject_resource"
        or set(receiver_grain["does_not_qualify"]) != {"card_document", "persisted_artifact_universally"}
        or receiver_grain["part_projection_relation"] != "exact_one_to_one_subject_id_to_part_id"
        or receiver_grain["ambiguous_missing_or_substring_relation"] != "explicit_compilation_residue"
        or not receiver_grain["grain_settled"]
    ):
        errors.append("card trust may reach PART only through exact subject-resource identity")
    landing = receiver_grain["landing_sequence"]
    retirement = landing["parts_registered_retirement_sequence"]
    receiver_population = landing["post_rerun_receiver_population"]
    readiness = landing["receiver_readiness_axes"]
    card_population = landing["admitted_card_population"]
    if (
        landing["strategy"] != "receiver_before_join"
        or landing["schema_change"] != "additive_optional"
        or retirement != {
            "generator_write_sites_removed": True,
            "committed_manifest_field_present": True,
            "shared_schema_property_present": True,
            "next_required_act": "generator_rerun_after_shared_schema_pass",
            "final_required_act": "remove_schema_property_after_emitted_manifest_validation",
            "hand_edit_manifest_prohibited": True,
        }
        or receiver_population["total_parts"] != 42
        or receiver_population["admitted_exact_subject_matches"] != 0
        or any(
            receiver_population[field]["declared"] + receiver_population[field]["unknown"]
            != receiver_population["total_parts"]
            for field in ("home_space", "grain", "key", "failure_mode")
        )
        or receiver_population["home_space"] != {"emitted": 42, "declared": 42, "unknown": 0}
        or any(
            receiver_population[field] != {"emitted": 42, "declared": 0, "unknown": 42}
            for field in ("grain", "key", "failure_mode")
        )
        or not receiver_population["summation_across_receivers_prohibited"]
        or card_population != {
            "source_glob": "org/**/D11_CARDS_W3/*.json",
            "total": 13,
            "exact_subject_matches": 0,
            "receiver_residue": 13,
        }
        or landing["unknown_satisfies_operative_completeness"]
        or landing["future_mapping_effect"] != "unknown_to_declared_enrichment"
    ):
        errors.append("receiver must land additively before the join while unknown remains non-complete")
    expected_readiness = {
        "candidate_population": {
            "home": "org/**/D11_CARDS_W4/*.json",
            "admission_state": "not_admitted",
            "candidate_json_file_count": 24,
            "valid_card_document_count": 23,
            "non_card_document_count": 1,
            "excluded_non_card_home": "org/tier2_senior/0.8.0_AE_CloudComp/deliverables/D11_CARDS_W4/W4-FILE.cells.json",
            "exact_subject_match_count": 23,
        },
        "home_space": {
            "source_payload_state": "not_required",
            "source_complete_candidate_count": 0,
            "registry_admission_state": "not_required",
            "transformation_state": "implemented_fail_closed",
            "compiler_implementation_state": "implemented_fail_closed",
        },
        "failure_mode": {
            "source_payload_state": "complete",
            "source_complete_candidate_count": 23,
            "registry_admission_state": "blocked",
            "transformation_state": "absent",
            "compiler_implementation_state": "absent",
        },
        "key": {
            "source_payload_state": "incomplete",
            "source_complete_candidate_count": 0,
            "registry_admission_state": "blocked",
            "transformation_state": "absent",
            "compiler_implementation_state": "absent",
        },
        "grain": {
            "source_payload_state": "absent",
            "source_complete_candidate_count": 0,
            "registry_admission_state": "blocked",
            "transformation_state": "absent",
            "compiler_implementation_state": "absent",
        },
    }
    if readiness != expected_readiness:
        errors.append("receiver readiness must keep source, admission, transform authority, and compiler implementation independent")
    completion = landing["completion_populations"]
    cardable = completion["cardable"]
    unbuilt = completion["unbuilt"]
    l1_resolved = completion["l1_resolved"]
    if (
        cardable != {"part_count": 36, "terminal_claim_status": "declared", "current_terminal_count": 0}
        or unbuilt != {
            "part_count": 3,
            "terminal_claim_status_under_current_directive": "unknown",
            "becomes_declarable_when": "part_is_built",
        }
        or cardable["part_count"] + unbuilt["part_count"] + l1_resolved["part_count"] != 42
        or l1_resolved["measurement_state"] != "completed"
        or l1_resolved["complete_four_receiver_source_count"] != 0
        or set(l1_resolved["exact_part_ids"])
        != {".comp-graph/graph.json", "graph_contracts", "resource_summaries"}
        or l1_resolved["home_space_present_count"] != 0
        or l1_resolved["grain_receiver_present_count"] != 0
        or l1_resolved["key_expression_present_count"] != 0
        or l1_resolved["failure_mode_present_basis_count"] != 2
    ):
        errors.append("completion bar must print 42/42 emission separately from the three terminal declaration populations")

    l1_card_paths = {
        ".comp-graph/graph.json": WORKSPACE / "org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_CARDS_W2/W2-lqzx__.comp-graph_graph.json.json",
        "graph_contracts": WORKSPACE / "org/tier2_senior/0.8.0_AE_CloudComp/deliverables/D11_CARDS_W2/W2-qgtd_graph_contracts.json",
        "resource_summaries": WORKSPACE / "org/tier2_senior/0.7.0_AE_CloudOps/deliverables/D11_CARDS_W2/resource_summaries.json",
    }
    measured_home_space = measured_grain = measured_key_expression = measured_failure_present = 0
    for part_id, card_path in l1_card_paths.items():
        card_bytes = card_path.read_bytes()
        card = json.loads(card_bytes)
        if card["subject"]["id"] != part_id:
            errors.append(f"L1-resolved card subject does not exactly equal part id: {part_id}")
        if hashlib.sha256(card_bytes).hexdigest() != l1_resolved["card_sha256"][part_id]:
            errors.append(f"L1-resolved card bytes drifted from measured pin: {part_id}")
        measured_home_space += int("home_space" in card["artifact"]["location"])
        measured_grain += int("grain" in card)
        measured_key_expression += int("key_expression" in card["trust"]["key"])
        measured_failure_present += int(card["trust"]["failure_mode"]["basis"] != "absent")
    if (
        measured_home_space != l1_resolved["home_space_present_count"]
        or measured_grain != l1_resolved["grain_receiver_present_count"]
        or measured_key_expression != l1_resolved["key_expression_present_count"]
        or measured_failure_present != l1_resolved["failure_mode_present_basis_count"]
    ):
        errors.append("L1-resolved three-card receiver measurement does not match pinned source bytes")

    remediation = landing["unknown_remediation_population"]
    class_census = remediation["part_class_census"]
    queue_classifier = remediation["operational_queue_classifier"]
    queue_partition = queue_classifier["queue_partition"]
    boundary = remediation["population_boundary"]
    remote = remediation["remote_uri_denominators"]
    remote_instrument = remediation["remote_uri_instrument"]
    member_set = remediation["member_set_contract"]
    brace_census = remediation["brace_part_census"]
    enumerated_evidence = remediation["enumerated_member_evidence"]
    runtime_family = remediation["runtime_named_family_contract"]
    parent_manifest = load(L0_MANIFEST)
    parent_ids = {part["id"] for part in parent_manifest["parts"]}
    parent_sha256 = hashlib.sha256(L0_MANIFEST.read_bytes()).hexdigest()
    excluded_ids = set(boundary["excluded_exact_part_ids"])
    remote_manifest_ids = set(remote["remote_uri_manifest_part_ids"])
    remote_residue_ids = set(remote["residue_remote_uri_part_ids"])
    actual_remote_ids = {part["id"] for part in parent_manifest["parts"] if part["home"].startswith("s3://")}
    expected_stable_families = [
        {
            "part_id": ".comp-graph/platinum.CACHE_SET",
            "home_expression": ".comp-graph/platinum.{dag.bd,dag.cot,dag.inf,dataflows,routing}.cache",
            "members": [
                ".comp-graph/platinum.dag.bd.cache",
                ".comp-graph/platinum.dag.cot.cache",
                ".comp-graph/platinum.dag.inf.cache",
                ".comp-graph/platinum.dataflows.cache",
                ".comp-graph/platinum.routing.cache",
            ],
        },
        {
            "part_id": "_build_manifest.json.SET",
            "home_expression": "infra/aws/globgrph/{kuzu_nessie_db,kuzu_db,kuzu_stitch_db}._build_manifest.json",
            "members": [
                "infra/aws/globgrph/kuzu_nessie_db._build_manifest.json",
                "infra/aws/globgrph/kuzu_db._build_manifest.json",
                "infra/aws/globgrph/kuzu_stitch_db._build_manifest.json",
            ],
        },
    ]
    if (
        remediation["source"] != "manifest_parts_with_unknown_receiver"
        or remediation["total"] != receiver_population["grain"]["unknown"]
        or boundary["parent_document_home"] != L0_MANIFEST.relative_to(WORKSPACE).as_posix()
        or boundary["parent_sha256"] != parent_sha256
        or excluded_ids
        or not excluded_ids <= parent_ids
        or len(parent_ids) != remediation["total"]
        or boundary["operation"] != "identity"
        or sum(class_census.values()) != remediation["total"]
        or sum(queue_partition.values()) != remediation["total"]
        or remediation["resolution_grain"] != "per_part"
        or set(remediation["prohibited_resolution_proxies"]) != {"part_class", "filesystem_path_exists"}
        or set(remediation["subject_semantic_partitions_required"]) != {"materializer_subject", "non_materializer_resource_subject", "aggregate_rollup_relation"}
        or queue_classifier["precedence"] != ["unbuilt_future_layer", "brace_expression", "remote_s3_uri", "local_file_path", "path_shaped_absent"]
        or queue_classifier["assignment_rule"] != "first_matching_class_only"
        or set(queue_classifier["required_independent_axes"]) != {"locator_form", "realization_state", "enumerability_state"}
        or queue_partition != {"file_resolves": 22, "remote_uri": 14, "brace_pattern": 3, "unbuilt_future_layer": 3, "path_shaped_but_absent": 0}
        or remediation["partition_controls"] != {"known_present": True, "known_absent": False}
        or remote_manifest_ids != actual_remote_ids
        or remote_residue_ids != actual_remote_ids - excluded_ids
        or len(remote_residue_ids) != queue_partition["remote_uri"]
        or remote["arn_scheme_part_ids"] != []
        or remote["predicate"] != "home_starts_s3_scheme"
        or remote_instrument["result_field"] != "KeyCount"
        or not remote_instrument["same_bucket_positive_control_required"]
        or not remote_instrument["head_object_alone_prohibited"]
        or remote_instrument["execution_state"] != "not_run"
        or remediation["cardable_candidate_total"] != remediation["total"] - queue_partition["unbuilt_future_layer"]
        or set(remediation["unbuilt_future_layer_ids"]) != {"affinity_matrix", "similarity_network_fusion", "identity_and_succession"}
        or remediation["unbuilt_disposition"] != "exclude_never_manufacture_substrate"
        or remediation["brace_pattern_part_count"] != queue_partition["brace_pattern"]
        or remediation["brace_pattern_syntactic_expansion_count"] != 14
        or remediation["brace_pattern_syntactic_expansion_role"] != "parser_control_not_population"
        or brace_census != {"stable_enumerable": 2, "runtime_named_non_enumerable": 1}
        or sum(brace_census.values()) != remediation["brace_pattern_part_count"]
        or enumerated_evidence["source_manifest"] != {"home": L0_MANIFEST.relative_to(WORKSPACE).as_posix(), "git_commit": "94efcda69cf00db573866174b110a0bcbe39a42b", "git_blob": "3f7bd6ee2251891bc05d57ba6b9b2e889a9f8431"}
        or enumerated_evidence["stable_families"] != expected_stable_families
        or sum(len(family["members"]) for family in enumerated_evidence["stable_families"]) != 8
        or remediation["brace_correction_evidence"] != {"withdrawn_syntactic_member_claim_count": 6, "reason": "runtime_named_instances_do_not_form_a_durable_member_population"}
        or remediation["brace_pattern_disposition"] != "split_by_enumerability"
        or runtime_family != {"part_id": "kuzu_nessie_db.rebuild.tmp.SET", "disposition": "declared_pattern_non_enumerable", "population_status": "orphaned", "pattern_representation": "normalized_semantic_family_template", "normalized_pattern": "<base>.rebuild.tmp.<pid>.<monotonic_ns>.<uniq>", "pattern_source_home": "infra/aws/globgrph/_canonical.py", "pattern_source_line": 288, "pattern_source_git_commit": "17eb3fa310ae04b7cb8ca55cfde8f801f34e8c04", "pattern_source_git_blob": "7867f1a0a88dab0c9e1e273d794e5901d0aade48", "pattern_source_sha256": "edaa00ae4617f06b07932f8706c20fbbe0482ee610f8854ac1f7d591a1dd601c", "observation_count_is_population": False}
        or not member_set["enumerability_axis_required"]
        or not member_set["stored_cardinality_prohibited"]
        or member_set["enumerable_shape"] != {"members_required": True, "minimum_members": 2, "cardinality_derivation": "length(members)", "recursive_expansion_required": True}
        or member_set["non_enumerable_shape"] != {"pattern_required": True, "pattern_source_home_required": True, "pattern_source_line_required": True, "members_field_prohibited": True, "cardinality_field_prohibited": True}
        or not member_set["shared_schema_receiver_present"]
        or member_set["shared_schema_validation_state"] not in {"not_run", "failed", "passed"}
        or member_set["interim_prose_is_complete"]
        or set(remediation["resolved_preconditions"]) != {"remote_uri_instrument_named", "map_owner_runtime_family_disposition"}
        or remediation["unresolved_preconditions"] != []
        or set(remediation["remaining_contract_gaps"]) != {"shared_schema_validation", "compiler_validation"}
        or remediation["wave_cut_ready"]
    ):
        errors.append("42-part unknown-receiver population must preserve independent field, subject, and resolution partitions before wave cut")

    pattern_source = WORKSPACE / runtime_family["pattern_source_home"]
    pattern_source_bytes = pattern_source.read_bytes()
    git_blob_digest = hashlib.sha1(
        b"blob " + str(len(pattern_source_bytes)).encode("ascii") + b"\0" + pattern_source_bytes
    ).hexdigest()
    source_lines = pattern_source_bytes.decode("utf-8").splitlines()
    source_line = source_lines[runtime_family["pattern_source_line"] - 1].strip()
    if (
        hashlib.sha256(pattern_source_bytes).hexdigest() != runtime_family["pattern_source_sha256"]
        or git_blob_digest != runtime_family["pattern_source_git_blob"]
        or source_line
        != 'return f"{base}.rebuild.tmp.{os.getpid()}.{time.monotonic_ns()}.{next(_UNIQ)}"'
    ):
        errors.append("runtime family normalized pattern must remain bound to the pinned producer bytes and line")

    l1_baseline = document["design_measurements"]["l1_identity_and_population_baseline"]
    firm_identity = l1_baseline["firm_qualified_symbol_identity"]
    population_basis = l1_baseline["population_basis"]
    discrimination = l1_baseline["coverage_discrimination"]
    denominators = population_basis["denominator_contracts"]
    lane_delivery = l1_baseline["lane_delivery"]
    expected_source_ids = {
        "file": {"portal_filesystem", "kuzu_portal_module"},
        "chain_motif": {"c2_chain_instances", "kuzu_semctl"},
        "symbol": {"trace_graph_symbols", "kuzu_portal_nonmodule", "kuzu_pipeline_symbols"},
        "arn_resource": {"kuzu_arn", "stitch_arn"},
    }
    expected_discriminators = {
        "file": "committed_same_vintage_member_set",
        "chain_motif": "comparable_graph_vintage_and_declared_scope",
        "symbol": "external_coverage_oracle",
        "arn_resource": "declared_scan_scope",
    }
    if (
        firm_identity["raw_join_count"] != 0
        or firm_identity["lossy_parse_join_count"] != 1331
        or firm_identity["parse"] != "strip_pipeline_firm_prefix"
        or set(firm_identity["firm_values"]) != {"bd", "inf", "mdpf"}
        or firm_identity["bare_gold_target_count"] != 3
        or not firm_identity["firm_must_remain_in_identity"]
    ):
        errors.append("firm-qualified symbol identity must reject lossy prefix-strip canonicalization")
    if (
        population_basis["prd_claimed_is_denominator"]
        or population_basis["single_substrate_sweep_signatures"]["arn_resource"]["prd_claimed_count"]
        != population_basis["single_substrate_sweep_signatures"]["arn_resource"]["matching_substrate_count"]
        or population_basis["single_substrate_sweep_signatures"]["chain_motif"]["prd_claimed_count"]
        != population_basis["single_substrate_sweep_signatures"]["chain_motif"]["matching_substrate_count"]
        or population_basis["observed_cross_store_union_counts"]["semantic_role"]
        != "evidence_only_not_population_denominator"
        or population_basis["symbol_prd_provenance"] != "unresolved"
        or population_basis["file_prd_claim_source"] != "co_change_corpus"
        or population_basis["measurement_evidence"] != {"home": "org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_L1/L1_CELLS.json", "git_commit": "c0ccc0de3183cc839b4b60e25b4adb0c3472fa5a", "git_blob": "29cb90710e445f915c09bdac9717976c6752fbe9", "cell_pointers": {"chain_motif": "/cells/1", "symbol": "/cells/8", "file": "/cells/16", "arn_resource": "/cells/23"}}
        or any(denominators[space]["denominator_status"] != "unresolved" for space in expected_source_ids)
        or any("count" in denominators[space] for space in expected_source_ids)
        or any(denominators[space]["exclusion_status"] != "unresolved" for space in expected_source_ids)
        or any(denominators[space]["missing_discriminator"] != expected_discriminators[space] for space in expected_source_ids)
        or any({source["source_id"] for source in denominators[space]["source_populations"]} != expected_source_ids[space] for space in expected_source_ids)
        or any(source["replayability_state"] != "not_replayable_from_tracked_evidence" for space in expected_source_ids for source in denominators[space]["source_populations"])
        or any(not source["selector"] or not source["source_home"] for space in expected_source_ids for source in denominators[space]["source_populations"])
    ):
        errors.append("L1 population basis must preserve single-substrate sweep signatures without promoting observed unions to denominators")
    file_coverage = discrimination["file"]
    if (
        file_coverage != {"coverage_adjudication": "measured_snapshot", "oracle": "filesystem", "observed_filesystem_count": 429, "observed_kuzu_portal_module_count": 374, "observed_shared_count": 373, "observed_filesystem_only_count": 56, "observed_kuzu_only_count": 1, "observed_union_count": 430}
        or file_coverage["observed_filesystem_count"] != file_coverage["observed_shared_count"] + file_coverage["observed_filesystem_only_count"]
        or file_coverage["observed_kuzu_portal_module_count"] != file_coverage["observed_shared_count"] + file_coverage["observed_kuzu_only_count"]
        or file_coverage["observed_union_count"] != file_coverage["observed_shared_count"] + file_coverage["observed_filesystem_only_count"] + file_coverage["observed_kuzu_only_count"]
        or discrimination["chain_motif"]["coverage_adjudication"] != "blocked_missing_discriminator"
        or discrimination["chain_motif"]["missing_discriminator"] != "comparable_graph_vintage_and_declared_scope"
        or discrimination["symbol"]["coverage_adjudication"] != "blocked_missing_discriminator"
        or discrimination["symbol"]["missing_discriminator"] != "external_coverage_oracle"
        or discrimination["symbol"]["observed_trace_symbol_count"] != 2249
        or discrimination["arn_resource"]["coverage_adjudication"] != "blocked_missing_discriminator"
        or discrimination["arn_resource"]["missing_discriminator"] != "declared_scan_scope"
    ):
        errors.append("L1 coverage must distinguish measured snapshot discrimination from unresolved population denominators")
    if lane_delivery != {"commit": "c0ccc0de3183cc839b4b60e25b4adb0c3472fa5a", "cell_total": 29, "measured": 26, "unmeasured": 3, "acceptance_criteria_met": 6, "acceptance_criteria_total": 7, "ac7_state": "unmet", "operative_effect": "none"}:
        errors.append("L1 lane delivery must preserve 29-cell evidence without manufacturing AC7 or operative release")

    bridge = document["l0_deliverable_bridge"]
    if bridge["relabel_existing"] or bridge["rehome_existing"] or not bridge["new_target_document_required"]:
        errors.append("existing graph manifest must remain at home as source to a new target projection")
    if bridge["existing_document_kind"] == bridge["target_document_kind"]:
        errors.append("existing graph manifest and target projection must remain distinct document kinds")
    if bridge["target_required_section_count"] != 9 or bridge["existing_target_sections_satisfied"] != ["parts"]:
        errors.append("existing graph manifest satisfies only parts of the nine-section proposed target")
    l0_contract = layers[0]
    if "l0_graph_substrate_manifest" not in l0_contract["input_document_kinds"]:
        errors.append("L0 target projection must declare the existing graph manifest as a source input")
    required_l0_sections = {section["field"] for section in l0_contract["required_sections"]}
    if len(required_l0_sections) != bridge["target_required_section_count"]:
        errors.append("L0 bridge section count must equal the target deliverable contract")

    execution = document["execution_plan"]
    if set(execution["currently_executable_units"]) != EXECUTABLE_NOW:
        errors.append("only L0, L2 STRUCTURE, and L2 BEHAVIOR are executable now")
    actual_edges = {(row["prerequisite"], row["dependent"]) for row in execution["dependency_edges"]}
    if actual_edges != DEPENDENCY_EDGES:
        errors.append("dependency edges must preserve L0->L1, L1->L2 fusion admissibility, L1->L3, and L3->L4")
    stages = {row["stage_id"]: row for row in execution["l2_output_stages"]}
    raw = stages.get("raw_view_evidence")
    normalized = stages.get("spine_normalized_affinity")
    if not raw or raw["execution_availability"] != "available_now" or raw["fusion_admissible"]:
        errors.append("raw L2 view evidence must be available now and not fusion-admissible")
    if (
        not normalized
        or normalized["execution_availability"] != "prerequisite_bound"
        or not normalized["fusion_admissible"]
        or "l1_entity_spine" not in normalized["required_input_document_kinds"]
    ):
        errors.append("fusion-admissible L2 output must remain bound to the L1 entity spine")
    guard = execution["downstream_guard"]
    if set(guard["prohibited_units"]) != {"L3", "L4"} or guard["until_document_kind_exists"] != "l1_entity_spine":
        errors.append("L3 and L4 must remain prohibited until the L1 entity spine exists")
    gaps = execution["operational_gaps"]
    if len(gaps) != 1:
        errors.append("execution plan must carry the one measured L0-to-L1 semantic gap")
    else:
        gap = gaps[0]
        if (
            gap["gap_id"] != "l0_part_semantics_for_l1"
            or not gap["grain_contract_settled"]
            or not gap["receiver_schema_extension_present"]
            or not gap["receiver_semantics_validated"]
            or gap["w3_extension_boundary_state"] != "intentional_temporal"
            or gap["receiver_source_registry_present"]
            or gap["candidate_glob_expands_authority"]
            or gap["required_registry_home"] != "org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/D11_MANIFEST/card_population_registry.v1.json"
            or gap["required_registry_populations"] != {
                "extension_population": {"current_member_count": 13, "consumer_scope": "existing_w3_map_enrichment_only"},
                "receiver_source_populations": {
                    "grain": {"current_member_count": 0, "admission_predicate": "declared_grain_branch_complete", "transform_required": True},
                    "key": {"current_member_count": 0, "admission_predicate": "declared_key_branch_complete", "transform_required": True},
                    "failure_mode": {"current_member_count": 0, "admission_predicate": "declared_failure_mode_branch_complete", "transform_required": True},
                },
            }
            or gap["w4_candidate_ceiling"] != {
                "candidate_json_file_count": 24,
                "valid_card_document_count": 23,
                "non_card_document_count": 1,
                "excluded_non_card_home": "org/tier2_senior/0.8.0_AE_CloudComp/deliverables/D11_CARDS_W4/W4-FILE.cells.json",
                "exact_subject_count": 23,
                "governed_cardable_part_count": 36,
                "task_order_card_requirement_state": "absent_all_three_tranches",
                "task_order_card_schema_binding_state": "absent_all_three_tranches",
                "produced_card_schema": "org/standards/SUBSTRATE_CARD.v2.schema.json",
                "produced_card_schema_selection_authority": "lane_selected",
                "produced_card_schema_validation_state": "passed",
                "title_acceptance_surprise_state": "not_raised_before_execution",
                "remote_missing_card_count": 12,
                "remote_card_delivery_obligation_state": "not_issued",
                "issuer_work_unit_state": "not_cut_until_registry_exists",
            }
            or gap["grain_contract_owner"] != "4.0.0_SA_CRO~A"
            or gap["schema_extension_owner"] != "1.0.0_SA_CTO~X"
            or gap["receiver_source_registry_owner"] != "0.4.0_DT_ClientPlatform~X"
            or not gap["prevents_operative_transition"]
        ):
            errors.append("structured L0 part semantics must preserve settled grain and one owner per remaining act")
        w4_paths = sorted(WORKSPACE.glob("org/**/D11_CARDS_W4/*.json"))
        w4_cards: list[tuple[Path, dict]] = []
        w4_non_cards: list[Path] = []
        for path in w4_paths:
            value = load(path)
            if isinstance(value.get("subject"), dict) and value["subject"].get("id"):
                w4_cards.append((path, value))
            else:
                w4_non_cards.append(path)
        card_schema = load(WORKSPACE / "org/standards/SUBSTRATE_CARD.v2.schema.json")
        card_validator = jsonschema.Draft202012Validator(card_schema)
        invalid_w4_cards = [path for path, value in w4_cards if list(card_validator.iter_errors(value))]
        relative_non_cards = {path.relative_to(WORKSPACE).as_posix() for path in w4_non_cards}
        measured_subjects = {value["subject"]["id"] for _, value in w4_cards}
        if (
            len(w4_paths) != 24
            or len(w4_cards) != 23
            or len(w4_non_cards) != 1
            or len(measured_subjects) != 23
            or invalid_w4_cards
            or relative_non_cards != {gap["w4_candidate_ceiling"]["excluded_non_card_home"]}
        ):
            errors.append("W4 ceiling must distinguish candidate JSON files, valid cards, exact subjects, and the excluded cells document")

    checkpoints = document["checkpoint_sequence"]
    if [row["checkpoint_id"] for row in checkpoints] != CHECKPOINTS:
        errors.append("checkpoint sequence must contain the five exact transitions in order")
    criterion_ids: list[str] = []
    for checkpoint in checkpoints:
        if checkpoint["approval_gate"]:
            errors.append(f"{checkpoint['checkpoint_id']}: checkpoint cannot be an approval gate")
        for criterion in checkpoint["criteria"]:
            criterion_ids.append(criterion["criterion_id"])
            if not criterion["required"]:
                errors.append(f"{criterion['criterion_id']}: non-required criterion does not belong in a transition contract")
            state = criterion["measurement_state_at_design"]
            reason = criterion["unmeasurable_reason"]
            owner = criterion["resolution_owner"]
            if state == "measurable" and (reason is not None or owner is not None):
                errors.append(f"{criterion['criterion_id']}: measurable criterion cannot carry unmeasurable residue")
            if state == "currently_unmeasurable" and (not reason or not owner):
                errors.append(f"{criterion['criterion_id']}: unmeasurable criterion requires a reason and resolution owner")
    if len(criterion_ids) != len(set(criterion_ids)):
        errors.append("checkpoint criterion ids must be globally unique")
    resolved = document["resolved_decisions"]
    if (
        len(resolved) != 1
        or resolved[0]["selected_value"] != "every_entity"
        or resolved[0]["identity_scope"] != "plane_qualified"
        or resolved[0]["canonical_coordinate"] != "ordered_pair_plane_entity"
        or resolved[0]["cross_plane_comparison"] != "explicit_bridge_only"
        or resolved[0]["cross_plane_comparison_demand"] != "none_measured"
        or resolved[0]["declared_bridge_pair_count"] != 0
    ):
        errors.append("DEC-01 must resolve plane-qualified every-entity identity with explicit cross-plane bridges")
    elif set(resolved[0]["not_decided_dimensions"]) != {"membership_model", "identifier_encoding_and_minting"}:
        errors.append("identity-grain ruling must not decide membership model or identifier encoding and minting")
    open_ids = {decision["decision_id"] for decision in document["open_decisions"]}
    if open_ids != {"DEC-02", "DEC-03", "DEC-04", "DEC-05"}:
        errors.append("only DEC-02 through DEC-05 remain open")
    l1_grain_criterion = next((
        criterion
        for criterion in checkpoints[1]["criteria"]
        if criterion["criterion_id"] == "L1-C01"
    ), None)
    if (
        not l1_grain_criterion
        or l1_grain_criterion["measurement_state_at_design"] != "measurable"
        or l1_grain_criterion["unmeasurable_reason"] is not None
        or l1_grain_criterion["resolution_owner"] is not None
    ):
        errors.append("ruled every-entity grain must make L1-C01 measurable")
    overlap_criterion = next((
        criterion
        for checkpoint in checkpoints
        for criterion in checkpoint["criteria"]
        if criterion["criterion_id"] == "L3-C06"
    ), None)
    if (
        not overlap_criterion
        or overlap_criterion["measurement_state_at_design"] != "measurable"
        or overlap_criterion["predicate"]["compiler_rule"] != "C3M_L3_OVERLAP_ACCOUNTING"
    ):
        errors.append("L3 must measurably account for all baseline overlap before a partition can pass")
    compile_criterion = next((
        criterion
        for checkpoint in checkpoints
        for criterion in checkpoint["criteria"]
        if criterion["criterion_id"] == "L0-C06"
    ), None)
    if (
        not compile_criterion
        or compile_criterion["measurement_state_at_design"] != "measurable"
        or compile_criterion["predicate"]["compiler_rule"] != "C3M_L0_CARDS_COMPILED"
    ):
        errors.append("L0 must test deterministic compilation of every admitted substrate card")
    required_l0_compile_rules = {
        "C3M_L0_CARDS_COMPILED",
        "C3M_L0_TRANSFORM_EXHAUSTIVE",
        "C3M_L0_EXACT_PART_JOIN",
    }
    actual_l0_compile_rules = {
        criterion["predicate"]["compiler_rule"]
        for criterion in checkpoints[0]["criteria"]
        if criterion["criterion_id"] in {"L0-C06", "L0-C07", "L0-C08"}
    }
    if actual_l0_compile_rules != required_l0_compile_rules:
        errors.append("L0 compile checkpoint must separate coverage, transformation class, and exact join")
    l1_release_criterion = next((
        criterion
        for criterion in checkpoints[0]["criteria"]
        if criterion["criterion_id"] == "L0-C09"
    ), None)
    if (
        not l1_release_criterion
        or l1_release_criterion["predicate"]["compiler_rule"] != "C3M_L0_L1_PRECONDITIONS_COMPLETE"
    ):
        errors.append("CP-L0-L1 must require structured store grain key and failure-mode completeness")
    target_instance_criterion = next((
        criterion
        for criterion in checkpoints[0]["criteria"]
        if criterion["criterion_id"] == "L0-C10"
    ), None)
    if (
        not target_instance_criterion
        or target_instance_criterion["predicate"]["compiler_rule"] != "C3M_L0_TARGET_INSTANCE_EXISTS"
    ):
        errors.append("proposed CP-L0-L1 must require a distinct target projection instance")
    member_set_criterion = next((criterion for criterion in checkpoints[0]["criteria"] if criterion["criterion_id"] == "L0-C11"), None)
    if not member_set_criterion or member_set_criterion["predicate"]["compiler_rule"] != "C3M_L0_MEMBER_SET_COMPLETE":
        errors.append("CP-L0-L1 must preserve aggregate member sets without stored cardinality")
    firm_criterion = next((criterion for criterion in checkpoints[1]["criteria"] if criterion["criterion_id"] == "L1-C05"), None)
    population_criterion = next((criterion for criterion in checkpoints[1]["criteria"] if criterion["criterion_id"] == "L1-C06"), None)
    if not firm_criterion or firm_criterion["predicate"]["compiler_rule"] != "C3M_L1_FIRM_IDENTITY_PRESERVED":
        errors.append("CP-L1-L2 must reject cross-firm identity merges")
    if not population_criterion or population_criterion["predicate"]["compiler_rule"] != "C3M_L1_POPULATION_BASIS":
        errors.append("CP-L1-L2 must reject PRD or single-substrate counts as denominators")

    if document["shared_root_changes"]["made"] is not False:
        errors.append("proposal must not claim shared-root changes before package validation")
    return errors


def validate(document: dict) -> list[str]:
    schema = load(SCHEMA)
    validator = jsonschema.Draft202012Validator(schema)
    errors = [
        f"schema {'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(document), key=lambda item: list(item.absolute_path))
    ]
    if not errors:
        errors.extend(semantic_errors(document))
    return errors


def main() -> int:
    document = load(DOCUMENT)
    errors = validate(document)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    mutants: list[tuple[str, dict]] = []

    queued_finding_closed = copy.deepcopy(document)
    queued_finding_closed["post_rerun_rule24_queue"]["findings"][0]["finding_state"] = "closed"
    mutants.append(("open-post-rerun-finding-masquerades-as-closed", queued_finding_closed))

    freeze_exit_weakened = copy.deepcopy(document)
    freeze_exit_weakened["post_rerun_rule24_queue"]["freeze_exit_condition"] = "contract_stops_changing"
    mutants.append(("freeze-exits-before-42-receivers", freeze_exit_weakened))

    emitted_authority_finding_removed = copy.deepcopy(document)
    emitted_authority_finding_removed["post_rerun_rule24_queue"]["findings"].pop()
    mutants.append(("emitted-authority-contradiction-removed", emitted_authority_finding_removed))

    frozen_finding_called_new = copy.deepcopy(document)
    frozen_finding_called_new["post_rerun_rule24_queue"]["findings"][0]["evidence_run_change_state"] = "new"
    mutants.append(("unchanged-frozen-finding-masquerades-as-new", frozen_finding_called_new))

    receiver_presence_rounded_up = copy.deepcopy(document)
    receiver_presence_rounded_up["post_rerun_base_validation"]["structural_emission"]["receiver_presence_count"]["grain"] = 41
    mutants.append(("receiver-presence-rounded-to-42", receiver_presence_rounded_up))

    declaration_manufactured = copy.deepcopy(document)
    declaration_manufactured["post_rerun_base_validation"]["declaration_measurement"]["grain"] = {"declared_count": 1, "unknown_count": 41}
    mutants.append(("unknown-emission-masquerades-as-declaration", declaration_manufactured))

    home_space_partition_broken = copy.deepcopy(document)
    home_space_partition_broken["post_rerun_base_validation"]["home_space_measurement"]["repo_path_count"] = 24
    mutants.append(("home-space-counts-do-not-exhaust-parts", home_space_partition_broken))

    open_population_called_complete = copy.deepcopy(document)
    open_population_called_complete["post_rerun_base_validation"]["population_completeness"]["assessment_state"] = "complete"
    mutants.append(("open-population-called-complete", open_population_called_complete))

    known_unsearched_undercounted = copy.deepcopy(document)
    known_unsearched_undercounted["post_rerun_base_validation"]["population_completeness"]["known_unsearched_entry_count"] = 11
    mutants.append(("known-unsearched-entry-dropped", known_unsearched_undercounted))

    missing_subject_evidence_dropped = copy.deepcopy(document)
    missing_subject_evidence_dropped["post_rerun_base_validation"]["population_completeness"]["known_missing_subject_ids"].pop()
    mutants.append(("known-missing-subject-dropped", missing_subject_evidence_dropped))

    removal_called_producer = copy.deepcopy(document)
    removal_called_producer["post_rerun_base_validation"]["variant_suffix_authority"]["observed_source_role"] = "minting_producer"
    mutants.append(("removal-repertoire-masquerades-as-producer", removal_called_producer))

    contradicted_authority_called_match = copy.deepcopy(document)
    contradicted_authority_called_match["post_rerun_base_validation"]["variant_suffix_authority"]["authority_match_state"] = "satisfied"
    mutants.append(("contradicted-authority-called-satisfied", contradicted_authority_called_match))

    missing_lifecycle_called_present = copy.deepcopy(document)
    missing_lifecycle_called_present["post_rerun_base_validation"]["lifecycle_axis_coverage"]["manifest_document"]["authorship_mode_state"] = "present"
    mutants.append(("missing-document-lifecycle-called-present", missing_lifecycle_called_present))

    incomplete_receipt_called_closed = copy.deepcopy(document)
    incomplete_receipt_called_closed["post_rerun_base_validation"]["receipt_contract"]["input_closure_state"] = "complete"
    mutants.append(("incomplete-receipt-called-replayable", incomplete_receipt_called_closed))

    untracked_receipt_called_committed = copy.deepcopy(document)
    untracked_receipt_called_committed["post_rerun_base_validation"]["evidence_pair"]["receipt"]["persistence_state"] = "committed"
    mutants.append(("untracked-receipt-called-committed", untracked_receipt_called_committed))

    unknown_lifecycle_manufactured = copy.deepcopy(document)
    unknown_lifecycle_manufactured["post_rerun_base_validation"]["unknown_lifecycle_expressibility"]["terminal_transitional_partition_state"] = "expressible"
    mutants.append(("inexpressible-unknown-lifecycle-called-expressible", unknown_lifecycle_manufactured))

    release_before_shared_remediation = copy.deepcopy(document)
    release_before_shared_remediation["post_rerun_base_validation"]["remediation_sequence"]["shared_schema_step"] = "after_release"
    mutants.append(("release-precedes-shared-schema-remediation", release_before_shared_remediation))

    missing_layer = copy.deepcopy(document)
    missing_layer["layer_contracts"].pop(2)
    mutants.append(("missing-layer", missing_layer))

    approval_gate = copy.deepcopy(document)
    approval_gate["checkpoint_sequence"][0]["approval_gate"] = True
    mutants.append(("invented-approval-gate", approval_gate))

    unowned_unknown = copy.deepcopy(document)
    target = unowned_unknown["checkpoint_sequence"][3]["criteria"][0]
    target["unmeasurable_reason"] = None
    target["resolution_owner"] = None
    mutants.append(("unmeasurable-without-reason-owner", unowned_unknown))

    measurable_with_residue = copy.deepcopy(document)
    target = measurable_with_residue["checkpoint_sequence"][0]["criteria"][0]
    target["unmeasurable_reason"] = "invented"
    target["resolution_owner"] = "invented"
    mutants.append(("measurable-with-unmeasurable-residue", measurable_with_residue))

    false_l1_progress = copy.deepcopy(document)
    false_l1_progress["starting_position"]["layers"][1]["operative_contract_artifacts"] = 1
    mutants.append(("homonym-counted-as-l1-progress", false_l1_progress))

    missing_homonym = copy.deepcopy(document)
    missing_homonym["starting_position"]["homonym_exclusions"].pop()
    mutants.append(("missing-homonym-exclusion", missing_homonym))

    authored_projection = copy.deepcopy(document)
    authored_projection["layer_contracts"][2]["deliverable"]["document_lifecycle"]["authorship_mode"] = "human_authored"
    mutants.append(("generated-l2-masquerades-as-authored", authored_projection))

    mutable_identity = copy.deepcopy(document)
    mutable_identity["layer_contracts"][4]["deliverable"]["document_lifecycle"]["mutation_policy"] = "whole_document_replace"
    mutants.append(("replaceable-identity-ledger", mutable_identity))

    minted_project = copy.deepcopy(document)
    minted_project["mission"]["project_mint"] = True
    mutants.append(("project-mint-under-d11", minted_project))

    reordered_checkpoints = copy.deepcopy(document)
    reordered_checkpoints["checkpoint_sequence"][1], reordered_checkpoints["checkpoint_sequence"][2] = (
        reordered_checkpoints["checkpoint_sequence"][2],
        reordered_checkpoints["checkpoint_sequence"][1],
    )
    mutants.append(("checkpoint-order-changed", reordered_checkpoints))

    serialized_l2 = copy.deepcopy(document)
    serialized_l2["execution_plan"]["currently_executable_units"].remove("L2_STRUCTURE")
    mutants.append(("l2-structure-incorrectly-serialized", serialized_l2))

    premature_fusion = copy.deepcopy(document)
    target = premature_fusion["execution_plan"]["l2_output_stages"][1]
    target["execution_availability"] = "available_now"
    target["required_input_document_kinds"].remove("l1_entity_spine")
    mutants.append(("l2-fusion-without-spine", premature_fusion))

    premature_l3 = copy.deepcopy(document)
    premature_l3["execution_plan"]["currently_executable_units"][0] = "L3"
    mutants.append(("l3-before-l1", premature_l3))

    erased_cross_domain = copy.deepcopy(document)
    erased_cross_domain["design_measurements"]["cover_partition_baseline"]["cross_domain_multi_members"] = 0
    mutants.append(("cross-domain-baseline-erased", erased_cross_domain))

    unmeasured_partition_loss = copy.deepcopy(document)
    unmeasured_partition_loss["checkpoint_sequence"][3]["criteria"] = [
        criterion
        for criterion in unmeasured_partition_loss["checkpoint_sequence"][3]["criteria"]
        if criterion["criterion_id"] != "L3-C06"
    ]
    mutants.append(("partition-loss-unmeasured", unmeasured_partition_loss))

    false_zero_manifest = copy.deepcopy(document)
    false_zero_manifest["starting_position"]["layers"][0]["measurements"]["manifest_parts"] = 0
    mutants.append(("populated-l0-misreported-zero", false_zero_manifest))

    missing_compile_step = copy.deepcopy(document)
    missing_compile_step["checkpoint_sequence"][0]["criteria"] = [
        criterion
        for criterion in missing_compile_step["checkpoint_sequence"][0]["criteria"]
        if criterion["criterion_id"] != "L0-C06"
    ]
    mutants.append(("wave3-cards-have-no-compile-criterion", missing_compile_step))

    nonexhaustive_compile_shape = copy.deepcopy(document)
    nonexhaustive_compile_shape["design_measurements"]["wave3_manifest_compile_baseline"]["enrich_existing_part_rows"] = 9
    mutants.append(("wave3-row-classification-not-exhaustive", nonexhaustive_compile_shape))

    substring_join_promoted = copy.deepcopy(document)
    substring_join_promoted["design_measurements"]["wave3_manifest_compile_baseline"]["compiler_join_requirement"] = "indicative_substring_probe"
    mutants.append(("substring-probe-promoted-to-compiler-join", substring_join_promoted))

    missing_transform_criterion = copy.deepcopy(document)
    missing_transform_criterion["checkpoint_sequence"][0]["criteria"] = [
        criterion
        for criterion in missing_transform_criterion["checkpoint_sequence"][0]["criteria"]
        if criterion["criterion_id"] != "L0-C07"
    ]
    mutants.append(("compile-transformation-unchecked", missing_transform_criterion))

    systems_only_grain = copy.deepcopy(document)
    systems_only_grain["resolved_decisions"][0]["selected_value"] = "systems_only"
    mutants.append(("systems-only-identity-grain", systems_only_grain))

    grain_still_open = copy.deepcopy(document)
    grain_still_open["open_decisions"].append({
        "decision_id": "DEC-01",
        "question": "What canonical entity grain does L1 own?",
        "owner": "1.0.0_SA_CTO~X",
        "blocks_checkpoint": "CP-L1-L2",
        "does_not_block_drive": True,
    })
    mutants.append(("resolved-grain-still-open", grain_still_open))

    collapsed_grain_axes = copy.deepcopy(document)
    collapsed_grain_axes["resolved_decisions"][0]["not_decided_dimensions"] = ["membership_model"]
    mutants.append(("grain-ruling-collapses-independent-axes", collapsed_grain_axes))

    grain_reverted_unknown = copy.deepcopy(document)
    target = grain_reverted_unknown["checkpoint_sequence"][1]["criteria"][0]
    target["measurement_state_at_design"] = "currently_unmeasurable"
    target["unmeasurable_reason"] = "reopened after ruling"
    target["resolution_owner"] = "1.0.0_SA_CTO~X"
    mutants.append(("ruled-grain-reverted-unmeasurable", grain_reverted_unknown))

    wave3_releases_l1 = copy.deepcopy(document)
    wave3_releases_l1["design_measurements"]["l1_release_baseline"]["wave3_completion_sufficient"] = True
    mutants.append(("wave3-completion-releases-l1", wave3_releases_l1))

    proposed_contract_blocks_work = copy.deepcopy(document)
    proposed_contract_blocks_work["contract_status"]["l1_work_startable"] = False
    mutants.append(("proposed-contract-blocks-l1-work", proposed_contract_blocks_work))

    sparse_manifest_transition_ready = copy.deepcopy(document)
    sparse_manifest_transition_ready["design_measurements"]["l1_release_baseline"]["operative_transition_ready"] = True
    mutants.append(("sparse-manifest-claimed-transition-ready", sparse_manifest_transition_ready))

    lower_bound_claimed_exact = copy.deepcopy(document)
    lower_bound_claimed_exact["design_measurements"]["l1_release_baseline"]["prose_measurement_method"] = "exact_structured_field"
    mutants.append(("prose-count-claimed-semantic", lower_bound_claimed_exact))

    prose_promoted_to_field_paths = copy.deepcopy(document)
    prose_promoted_to_field_paths["design_measurements"]["l1_release_baseline"]["operative_schema_field_paths_before_amendment"]["grain"] = 7
    mutants.append(("prose-count-promoted-to-field-path", prose_promoted_to_field_paths))

    card_document_key = copy.deepcopy(document)
    card_document_key["design_measurements"]["card_to_part_receiver_grain"]["card_trust_qualifies"] = "card_document"
    mutants.append(("card-document-key-projected-to-part", card_document_key))

    substring_relation = copy.deepcopy(document)
    substring_relation["design_measurements"]["card_to_part_receiver_grain"]["part_projection_relation"] = "substring_match"
    mutants.append(("substring-relation-admitted", substring_relation))

    joint_owner = copy.deepcopy(document)
    joint_owner["execution_plan"]["operational_gaps"][0]["schema_extension_owner"] = "1.0.0_SA_CTO~X+4.0.0_SA_CRO~A"
    mutants.append(("shared-schema-act-jointly-owned", joint_owner))

    crossed_compiler_boundary = copy.deepcopy(document)
    crossed_compiler_boundary["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["admitted_card_population"]["source_glob"] = "org/**/D11_CARDS_W*.json"
    mutants.append(("estate-wide-cards-masquerade-as-admitted-input", crossed_compiler_boundary))

    discovery_promoted_to_authority = copy.deepcopy(document)
    discovery_promoted_to_authority["execution_plan"]["operational_gaps"][0]["candidate_glob_expands_authority"] = True
    mutants.append(("candidate-glob-promoted-to-admission-authority", discovery_promoted_to_authority))

    failure_candidates_preadmitted = copy.deepcopy(document)
    failure_candidates_preadmitted["execution_plan"]["operational_gaps"][0]["required_registry_populations"]["receiver_source_populations"]["failure_mode"]["current_member_count"] = 23
    mutants.append(("source-complete-failure-candidates-admitted-without-transform", failure_candidates_preadmitted))

    lane_schema_promoted_to_issued_authority = copy.deepcopy(document)
    lane_schema_promoted_to_issued_authority["execution_plan"]["operational_gaps"][0]["w4_candidate_ceiling"]["produced_card_schema_selection_authority"] = "task_order_bound"
    mutants.append(("lane-selected-card-schema-masquerades-as-issued-authority", lane_schema_promoted_to_issued_authority))

    remote_retroactive_debt = copy.deepcopy(document)
    remote_retroactive_debt["execution_plan"]["operational_gaps"][0]["w4_candidate_ceiling"]["remote_card_delivery_obligation_state"] = "issued"
    mutants.append(("unissued-remote-cards-masquerade-as-lane-debt", remote_retroactive_debt))

    cells_document_counted_as_card = copy.deepcopy(document)
    cells_document_counted_as_card["execution_plan"]["operational_gaps"][0]["w4_candidate_ceiling"]["valid_card_document_count"] = 24
    cells_document_counted_as_card["execution_plan"]["operational_gaps"][0]["w4_candidate_ceiling"]["non_card_document_count"] = 0
    mutants.append(("w4-cells-document-counted-as-card", cells_document_counted_as_card))

    readiness_cells_document_counted_as_card = copy.deepcopy(document)
    readiness_candidate = readiness_cells_document_counted_as_card["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["receiver_readiness_axes"]["candidate_population"]
    readiness_candidate["valid_card_document_count"] = 24
    readiness_candidate["non_card_document_count"] = 0
    mutants.append(("receiver-readiness-cells-document-counted-as-card", readiness_cells_document_counted_as_card))

    receiver_axes_collapsed = copy.deepcopy(document)
    receiver_axes_collapsed["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["post_rerun_receiver_population"]["key"] = {"emitted": 42, "declared": 3, "unknown": 39}
    mutants.append(("independent-receiver-states-collapsed-to-stale-three", receiver_axes_collapsed))

    receiver_counts_summed = copy.deepcopy(document)
    receiver_counts_summed["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["post_rerun_receiver_population"]["summation_across_receivers_prohibited"] = False
    mutants.append(("receiver-declaration-counts-summed-as-progress", receiver_counts_summed))

    failure_admission_manufactured = copy.deepcopy(document)
    failure_admission_manufactured["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["receiver_readiness_axes"]["failure_mode"]["registry_admission_state"] = "admitted"
    mutants.append(("failure-payload-availability-masquerades-as-registry-admission", failure_admission_manufactured))

    failure_transform_manufactured = copy.deepcopy(document)
    failure_transform_manufactured["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["receiver_readiness_axes"]["failure_mode"]["transformation_state"] = "implemented_fail_closed"
    mutants.append(("reachable-failure-payload-masquerades-as-governed-transform", failure_transform_manufactured))

    failure_compiler_path_manufactured = copy.deepcopy(document)
    failure_compiler_path_manufactured["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["receiver_readiness_axes"]["failure_mode"]["compiler_implementation_state"] = "implemented_fail_closed"
    mutants.append(("absent-declaration-code-path-masquerades-as-implemented", failure_compiler_path_manufactured))

    key_source_manufactured = copy.deepcopy(document)
    key_source_manufactured["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["receiver_readiness_axes"]["key"]["source_payload_state"] = "complete"
    mutants.append(("key-properties-masquerade-as-key-expression-source", key_source_manufactured))

    emission_claimed_from_declaration = copy.deepcopy(document)
    emission_claimed_from_declaration["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["post_rerun_receiver_population"]["grain"]["emitted"] = 0
    mutants.append(("emission-count-collapsed-into-declaration-count", emission_claimed_from_declaration))

    unbuilt_manufactured_declared = copy.deepcopy(document)
    unbuilt_manufactured_declared["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["completion_populations"]["unbuilt"]["terminal_claim_status_under_current_directive"] = "declared"
    mutants.append(("unbuilt-terminal-unknown-misreported-declared", unbuilt_manufactured_declared))

    unknown_claimed_complete = copy.deepcopy(document)
    unknown_claimed_complete["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_satisfies_operative_completeness"] = True
    mutants.append(("unknown-receiver-claimed-operative-complete", unknown_claimed_complete))

    join_first = copy.deepcopy(document)
    join_first["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["strategy"] = "join_before_receiver"
    mutants.append(("absent-receiver-delayed-on-join", join_first))

    class_proxy = copy.deepcopy(document)
    class_proxy["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_remediation_population"]["resolution_grain"] = "part_class"
    mutants.append(("part-class-used-as-resolution-proxy", class_proxy))

    rollup_forced_one_to_one = copy.deepcopy(document)
    rollup_forced_one_to_one["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_remediation_population"]["brace_pattern_disposition"] = "artifact_subject"
    mutants.append(("aggregate-rollup-forced-one-to-one", rollup_forced_one_to_one))

    wave_cut_before_partition = copy.deepcopy(document)
    wave_cut_before_partition["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_remediation_population"]["wave_cut_ready"] = True
    mutants.append(("wave-cut-before-partition", wave_cut_before_partition))

    unbuilt_carded = copy.deepcopy(document)
    unbuilt_carded["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_remediation_population"]["unbuilt_disposition"] = "card_as_existing"
    mutants.append(("unbuilt-layer-manufactured-as-substrate", unbuilt_carded))

    resolution_partition_loses_member = copy.deepcopy(document)
    resolution_partition_loses_member["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_remediation_population"]["operational_queue_classifier"]["queue_partition"]["remote_uri"] = 11
    mutants.append(("resolution-partition-does-not-sum", resolution_partition_loses_member))

    population_qualifier_lost = copy.deepcopy(document)
    population_qualifier_lost["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_remediation_population"]["population_boundary"]["excluded_exact_part_ids"] = ["cse_test_24458e6c", "cse_test_bb57a916", ".comp-graph/graph.json"]
    mutants.append(("same-count-wrong-population-exclusions", population_qualifier_lost))

    remote_manifest_count_as_residue = copy.deepcopy(document)
    remote_manifest_count_as_residue["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_remediation_population"]["remote_uri_denominators"]["residue_remote_uri_part_ids"][0] = "graph_contracts"
    mutants.append(("all-manifest-remote-count-masquerades-as-residue", remote_manifest_count_as_residue))

    stale_brace_fanout = copy.deepcopy(document)
    stale_brace_fanout["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_remediation_population"]["brace_pattern_syntactic_expansion_count"] = 11
    mutants.append(("single-brace-parser-undercount", stale_brace_fanout))

    syntactic_expansion_as_population = copy.deepcopy(document)
    syntactic_expansion_as_population["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_remediation_population"]["brace_pattern_syntactic_expansion_role"] = "artifact_population"
    mutants.append(("syntactic-expansion-masquerades-as-population", syntactic_expansion_as_population))

    fictional_runtime_members = copy.deepcopy(document)
    fictional_runtime_members["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_remediation_population"]["enumerated_member_evidence"]["stable_families"][0]["members"][0] = ".comp-graph/platinum.fictional.cache"
    mutants.append(("runtime-named-family-fictionally-enumerated", fictional_runtime_members))

    runtime_family_as_unsearched = copy.deepcopy(document)
    runtime_family_as_unsearched["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_remediation_population"]["runtime_named_family_contract"]["disposition"] = "known_unsearched"
    mutants.append(("producer-defined-runtime-family-called-unsearched", runtime_family_as_unsearched))

    runtime_members_admitted = copy.deepcopy(document)
    runtime_members_admitted["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_remediation_population"]["member_set_contract"]["non_enumerable_shape"]["members_field_prohibited"] = False
    mutants.append(("runtime-family-admits-snapshot-members", runtime_members_admitted))

    stored_cardinality = copy.deepcopy(document)
    stored_cardinality["design_measurements"]["card_to_part_receiver_grain"]["landing_sequence"]["unknown_remediation_population"]["member_set_contract"]["stored_cardinality_prohibited"] = False
    mutants.append(("derived-cardinality-serialized", stored_cardinality))

    firm_stripped = copy.deepcopy(document)
    firm_stripped["design_measurements"]["l1_identity_and_population_baseline"]["firm_qualified_symbol_identity"]["firm_must_remain_in_identity"] = False
    mutants.append(("cross-firm-prefix-stripped", firm_stripped))

    prd_as_denominator = copy.deepcopy(document)
    prd_as_denominator["design_measurements"]["l1_identity_and_population_baseline"]["population_basis"]["prd_claimed_is_denominator"] = True
    mutants.append(("prd-count-masquerades-as-population", prd_as_denominator))

    observed_union_as_denominator = copy.deepcopy(document)
    observed_union_as_denominator["design_measurements"]["l1_identity_and_population_baseline"]["population_basis"]["observed_cross_store_union_counts"]["semantic_role"] = "population_denominator"
    mutants.append(("observed-union-masquerades-as-population", observed_union_as_denominator))

    measurement_cell_swapped = copy.deepcopy(document)
    measurement_cell_swapped["design_measurements"]["l1_identity_and_population_baseline"]["population_basis"]["measurement_evidence"]["cell_pointers"]["file"] = "/cells/8"
    mutants.append(("file-census-pinned-to-symbol-cell", measurement_cell_swapped))

    missing_discriminator_dropped = copy.deepcopy(document)
    del missing_discriminator_dropped["design_measurements"]["l1_identity_and_population_baseline"]["coverage_discrimination"]["chain_motif"]["missing_discriminator"]
    mutants.append(("unmeasured-coverage-without-missing-discriminator", missing_discriminator_dropped))

    denominator_source_dropped = copy.deepcopy(document)
    denominator_source_dropped["design_measurements"]["l1_identity_and_population_baseline"]["population_basis"]["denominator_contracts"]["arn_resource"]["source_populations"] = []
    mutants.append(("denominator-without-source-population", denominator_source_dropped))

    denominator_exclusions_dropped = copy.deepcopy(document)
    del denominator_exclusions_dropped["design_measurements"]["l1_identity_and_population_baseline"]["population_basis"]["denominator_contracts"]["file"]["exclusion_status"]
    mutants.append(("denominator-without-explicit-exclusions", denominator_exclusions_dropped))

    count_on_unresolved_denominator = copy.deepcopy(document)
    count_on_unresolved_denominator["design_measurements"]["l1_identity_and_population_baseline"]["population_basis"]["denominator_contracts"]["symbol"]["count"] = 2249
    mutants.append(("count-attached-to-unresolved-denominator", count_on_unresolved_denominator))

    kuzu_count_as_file_denominator = copy.deepcopy(document)
    file_denominator = kuzu_count_as_file_denominator["design_measurements"]["l1_identity_and_population_baseline"]["population_basis"]["denominator_contracts"]["file"]
    file_denominator["denominator_status"] = "adjudicated"
    file_denominator["count"] = 374
    mutants.append(("kuzu-module-count-masquerades-as-file-denominator", kuzu_count_as_file_denominator))

    derived_union_as_primitive_source = copy.deepcopy(document)
    derived_union_as_primitive_source["design_measurements"]["l1_identity_and_population_baseline"]["population_basis"]["denominator_contracts"]["symbol"]["source_populations"][0]["source_id"] = "measured_union_space"
    mutants.append(("derived-union-masquerades-as-primitive-source", derived_union_as_primitive_source))

    unresolved_exclusions_called_none = copy.deepcopy(document)
    unresolved_exclusions_called_none["design_measurements"]["l1_identity_and_population_baseline"]["population_basis"]["denominator_contracts"]["file"]["exclusion_status"] = "none"
    mutants.append(("unresolved-exclusions-masquerade-as-none", unresolved_exclusions_called_none))

    source_selector_dropped = copy.deepcopy(document)
    del source_selector_dropped["design_measurements"]["l1_identity_and_population_baseline"]["population_basis"]["denominator_contracts"]["arn_resource"]["source_populations"][0]["selector"]
    mutants.append(("source-population-without-selector", source_selector_dropped))

    release_criterion_removed = copy.deepcopy(document)
    release_criterion_removed["checkpoint_sequence"][0]["criteria"] = [
        criterion
        for criterion in release_criterion_removed["checkpoint_sequence"][0]["criteria"]
        if criterion["criterion_id"] != "L0-C09"
    ]
    mutants.append(("l1-release-criterion-removed", release_criterion_removed))

    proposed_contract_claims_gate = copy.deepcopy(document)
    proposed_contract_claims_gate["contract_status"]["operative_gate"] = True
    mutants.append(("proposed-contract-claims-operative-gate", proposed_contract_claims_gate))

    relabel_existing = copy.deepcopy(document)
    relabel_existing["l0_deliverable_bridge"]["relabel_existing"] = True
    mutants.append(("existing-manifest-relabelled-as-target", relabel_existing))

    target_criterion_removed = copy.deepcopy(document)
    target_criterion_removed["checkpoint_sequence"][0]["criteria"] = [
        criterion
        for criterion in target_criterion_removed["checkpoint_sequence"][0]["criteria"]
        if criterion["criterion_id"] != "L0-C10"
    ]
    mutants.append(("distinct-target-instance-unchecked", target_criterion_removed))

    for name, mutant in mutants:
        if not validate(mutant):
            print(f"ERROR: mutant accepted: {name}")
            return 1
        print(f"PASS: mutant rejected: {name}")

    print("PASS: L0-L4 deliverable contracts and checkpoint sequence")
    print(f"PASS: negative controls {len(mutants)}/{len(mutants)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
