from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parents[4]
SCHEMA = ROOT / "schemas" / "l2_source_input_pin.v1.schema.json"
DOCUMENT = ROOT / "l2_source_input_pin.v1.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def semantic_errors(document: dict, authenticate: bool = True) -> list[str]:
    errors: list[str] = []
    if set(document["scope"]["included_views"]) != {"structure", "behavior"}:
        errors.append("only structure and behavior are included")
    if {row["view"] for row in document["scope"]["excluded_views"]} != {"flow", "semantic"}:
        errors.append("flow and semantic must remain explicitly excluded")

    progress = document["progress_boundary"]
    if progress["populated_view_cells"] != 0 or progress["operative_view_outputs"] != 0:
        errors.append("source pin cannot claim populated cells or operative view output")

    views = {row["view"]: row for row in document["views"]}
    if set(views) != {"structure", "behavior"}:
        errors.append("view pins must contain structure and behavior exactly")
    for view in views.values():
        if view["declared_entity_set_present"] or view["declared_entity_set_path"] is not None or view["declared_entity_denominator"] is not None:
            errors.append(f"{view['view']}: input pin cannot masquerade as a declared entity set")
        if view["procedure_selection"]["selected"] or view["procedure_selection"]["procedure_id"] is not None:
            errors.append(f"{view['view']}: procedure remains unselected at this pin")

    structure = views.get("structure", {})
    behavior = views.get("behavior", {})
    if structure.get("named_hazard_response", {}).get("current_disposition") != "procedure_selection_blocked":
        errors.append("structure must carry the unresolved installed-procedure gap")
    if behavior.get("named_hazard_response", {}).get("current_disposition") != "exclude_score_feature":
        errors.append("behavior must exclude comp-heat score")

    roles = [source["role"] for view in views.values() for source in view["pinned_sources"]]
    if len(roles) != len(set(roles)):
        errors.append("each pinned source role must have one exact home")

    if authenticate:
        pinned = [document["decomposition_pin"]["rectangle"], document["decomposition_pin"]["task_order"]]
        pinned.extend(source for view in views.values() for source in view["pinned_sources"])
        for source in pinned:
            path = WORKSPACE / source["path"]
            if not path.is_file():
                errors.append(f"missing pinned source: {source['path']}")
                continue
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if digest != source["sha256"]:
                errors.append(f"digest mismatch: {source['path']}")
    return errors


def validate(document: dict, authenticate: bool = True) -> list[str]:
    schema = load(SCHEMA)
    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(schema)
    errors = [
        f"schema {'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(document), key=lambda item: list(item.absolute_path))
    ]
    if not errors:
        errors.extend(semantic_errors(document, authenticate=authenticate))
    return errors


def main() -> int:
    document = load(DOCUMENT)
    errors = validate(document)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    mutants: list[tuple[str, dict]] = []

    operative_output = copy.deepcopy(document)
    operative_output["progress_boundary"]["operative_view_outputs"] = 1
    mutants.append(("source-pin-claims-operative-output", operative_output))

    flow_included = copy.deepcopy(document)
    flow_included["scope"]["included_views"][0] = "flow"
    mutants.append(("flow-enters-frozen-scope", flow_included))

    false_entity_set = copy.deepcopy(document)
    false_entity_set["views"][0]["declared_entity_set_present"] = True
    mutants.append(("prior-cover-masquerades-as-entity-set", false_entity_set))

    heat_score_admitted = copy.deepcopy(document)
    heat_score_admitted["views"][1]["named_hazard_response"]["current_disposition"] = "procedure_selection_blocked"
    mutants.append(("comp-heat-score-hazard-unanswered", heat_score_admitted))

    invented_structure_procedure = copy.deepcopy(document)
    invented_structure_procedure["views"][0]["procedure_selection"] = {"selected": True, "procedure_id": "graph_tool_sbm"}
    mutants.append(("missing-dependency-procedure-claimed-selected", invented_structure_procedure))

    overlapping_source_home = copy.deepcopy(document)
    overlapping_source_home["views"][1]["pinned_sources"][1]["role"] = "cochange_engine"
    mutants.append(("duplicate-source-role", overlapping_source_home))

    for name, mutant in mutants:
        if not validate(mutant, authenticate=False):
            print(f"ERROR: mutant accepted: {name}")
            return 1
        print(f"PASS: mutant rejected: {name}")

    print("PASS: L2 structure and behavior source-input pin")
    print(f"PASS: negative controls {len(mutants)}/{len(mutants)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
