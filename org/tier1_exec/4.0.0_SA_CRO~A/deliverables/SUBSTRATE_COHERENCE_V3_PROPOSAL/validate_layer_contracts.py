from __future__ import annotations

import copy
import json
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parent
SCHEMA = ROOT / "schemas" / "layer_contracts_and_checkpoints.v1.schema.json"
DOCUMENT = ROOT / "layer_contracts_and_checkpoints.v1.json"
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
        l0_measurements.get("manifest_parts") != 39
        or l0_measurements.get("manifest_validation_error_count") != 0
        or l0_measurements.get("manifest_negative_control_error_count", 0) <= 0
    ):
        errors.append("L0 baseline must preserve the validated populated 39-part manifest and firing negative control")
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
        errors.append("execution plan must carry the one measured wave3-to-L0 compilation gap")
    else:
        gap = gaps[0]
        if (
            gap["gap_id"] != "wave3_to_l0_manifest_compilation"
            or gap["implementation_present"]
            or gap["task_order_ref"] is not None
            or gap["owner_ref"] is not None
        ):
            errors.append("wave3-to-L0 compilation remains absent, unordered, and unowned at this observation")

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
    if len(resolved) != 1 or resolved[0]["selected_value"] != "every_entity":
        errors.append("DEC-01 must resolve identity grain to every_entity")
    elif set(resolved[0]["not_decided_dimensions"]) != {"membership_model", "identity_form"}:
        errors.append("identity-grain ruling must not decide membership model or identity form")
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
