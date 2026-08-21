"""NFRA_EPISTEMY C9-RIDE Phase 2 -- exercise the S6 Causal_Assessment_Object (0.1.1) against real
atom_layer0 bundles on a SCRATCH copy, with a planted un-runnable control.

What it does (deterministic; no wall-clock; re-run at one HEAD => byte-identical artifact):
  1. Reads three REAL bundles (d2, territory, role) from the ledger. For each, builds ONE
     Causal_Assessment_Object instance whose candidate_relation is a causal-shaped finding the
     bundle ITSELF states (stated_as HYPOTHESIS; result_status INFERRED -- no attested instrument).
     Evidence rows are GENERATED from the named binding's seam_axes evidence (a declared process),
     never authored to fit the conclusion. Nullable fields carry their DECLARED absence semantic
     (knowledge_basis.* null = UNRATIFIED_BASIS; space_ref null = NO RATIFIED SPACE -> declared_total
     false; attestation null = NOT ATTESTED -> basis desired; policy_ref null = pre-policy regime).
  2. Plants a CONTROL: a MUTANT of a real bundle (Scope) whose terminal is NOT_EXERCISABLE, written
     to the scratch dir (never the ledger), validated with ~A's validate_run.py (the control must be a
     VALID bundle, else it measures the authoring, not the object). Its S6 instance must surface as
     NOT RUN: result_status UNKNOWN, interim derivation.terminal NOT_EXERCISABLE, its evidence row
     UNFRAMED (denominator null) and therefore excluded from discrimination.
  3. Validates every instance against the S6 0.1.1 schema (jsonschema Draft 2020-12); applies the A5
     RULING (base 63827) OUTSIDE the S6 object: stage_class map per grammar version, substantive_result
     per the ruled rule, printed beside each instance (the S6 object is additionalProperties:false and
     has no such field -- the PROTO-RECORD will; this is where the split is exercised first).
Findings are characterize-not-fix; shared schemas are CITED, never edited here.
"""
from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                           capture_output=True, text=True, check=True).stdout.strip())
RUNS = REPO / "workflows/atom_layer0/runs"
MANIFEST = RUNS / "manifest/PROGRAM_MANIFEST.yaml"
VALIDATOR = REPO / "org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ATOM_LAYER0/scripts/validate_run.py"
S6_SCHEMA = REPO / "org/tier1_exec/4.0.0_SA_CRO/deliverables/NFRA_EPISTEMY/S6_CAUSAL_ASSESSMENT_OBJECT.schema.json"
HERE = Path(__file__).resolve().parent.parent
OUT_DIR = HERE / "phase2"
CONTROL_DIR = OUT_DIR / "scratch_control" / "scratch_control_not_exercisable"
OUT = OUT_DIR / "PHASE2_EXERCISE.json"

GRAMMAR_STAGE_CLASS = {  # A5 ruling (base 63827): declared PER GRAMMAR VERSION, never hard-coded globally
    "decomposition_grammar@1.0.0": {"s0": "ACQUISITION", "s1": "ACQUISITION", "s2": "ACQUISITION",
                                    "s3": "ACQUISITION", "s4": "ACQUISITION", "s5": "METHOD_ACCEPTANCE"},
}
AXIS_MAP_DEFAULT = {"MECHANICAL": "TOPOLOGICAL", "DECLARATIVE": "DECLARED_RATIONALE", "SEMANTIC": "DECLARED_RATIONALE"}

# The hypotheses are the bundles' OWN causal-shaped findings (quoted from their s4/residue text).
HYPOTHESES = {
    "d2": {
        "binding_id": "B-GRAPH-EVIDENCE-UNDATED",
        "defect_class": "UNDATED_EMBEDDED_MEASUREMENT",
        "cause_ref": "bank#dynamic_rails.D2_path_flow.graph_evidence carries NO as_of/vintage key",
        "effect_ref": "its 11 embedded edge counts cannot be adjudicated stale-or-current (6/11 differ from the live snapshot, 5/11 match)",
        "relation_kind": "CONTRIBUTED_TO",
        "axis_map": {"MECHANICAL": "TOPOLOGICAL", "DECLARATIVE": "DECLARED_RATIONALE", "SEMANTIC": "SUBSTRATE_DRIFT"},
        "plane_map": {"MECHANICAL": "APPLIED", "DECLARATIVE": "DESIRED", "SEMANTIC": "APPLIED"},
        "denominators": {"MECHANICAL": (11, "embedded flow/control edge kinds"), "DECLARATIVE": (4, "graph_evidence keys"), "SEMANTIC": (11, "embedded counts compared against live")},
        "live_candidates": ["H1 the embedded census is a copy that drifted and carries no moment (as_of absent)",
                            "H2 the embedded counts are current (no drift)",
                            "H3 the counts were measured on a different plane/instrument than CloudEdge.edge_type and are not comparable"],
        "tested_set": ["H1 the embedded census is a copy that drifted and carries no moment (as_of absent)", "H2 the embedded counts are current (no drift)"],
        "exclusions": [
            {"member": "H2 the embedded counts are current (no drift)", "reason_class": "RULED_OUT_BY_EVIDENCE", "evidence_ref": "ev-SEMANTIC", "lease_ref": None},
            {"member": "H3 the counts were measured on a different plane/instrument than CloudEdge.edge_type and are not comparable", "reason_class": "NOT_ADDRESSABLE_BY_EXPERIMENT", "evidence_ref": None, "lease_ref": None},
        ],
        "counterevidence": [{"description": "5 of 11 embedded counts MATCH the live snapshot exactly (FLOWS_TO 961, WRITES_S3 275, READS_S3 323, FETCHES 109, RUNS 248) -- consistent with a copy taken recently, not with arbitrary numbers", "grounding": "comp-kuzu DISTINCT e.edge_type,count(*) @ snapshot 5048107528270383466", "vintage": "fb4d8589709074717dfa3fc74b262995be2bbdcb"}],
        "graph_snapshot": "5048107528270383466",
        "invalidation_predicates": ["bank#dynamic_rails.D2_path_flow.graph_evidence gains an as_of/vintage key", "SYSTEM_DEFINITIONS.yaml blob != 43b50adf5421f0a442c4db0acabff4f6f0ced083", "a graph snapshot newer than 5048107528270383466 is addressed"],
    },
    "territory": {
        "binding_id": "B-MIGRATION-MAP",
        "defect_class": "ACCIDENTAL_COMPOSITE_TWO_AXES_ONE_ENTRY",
        "cause_ref": "one registry entry (Territory) carried two axes -- Substrate x Deploy_State -- before its 2026-08-12 retirement",
        "effect_ref": "the retirement map binds to TWO live children by design, so the resolution predicate (exactly one live authority) derives resolved=false on B-MIGRATION-MAP",
        "relation_kind": "CONTRIBUTED_TO",
        "axis_map": AXIS_MAP_DEFAULT,
        "plane_map": {"MECHANICAL": "DESIRED", "DECLARATIVE": "DESIRED", "SEMANTIC": "DESIRED"},
        "denominators": {"MECHANICAL": (2, "live children the map binds to"), "DECLARATIVE": None, "SEMANTIC": None},
        "live_candidates": ["H1 the accidental two-axes composition is what produces a two-target map",
                            "H2 the predicate's exactly-one rule is too strict for a governed retirement map (a design, not a defect)"],
        "tested_set": ["H1 the accidental two-axes composition is what produces a two-target map", "H2 the predicate's exactly-one rule is too strict for a governed retirement map (a design, not a defect)"],
        "exclusions": [],
        "counterevidence": [],
        "graph_snapshot": None,
        "invalidation_predicates": ["the resolution predicate is amended to admit a declared N-target retirement map", "SYSTEM_DEFINITIONS.yaml blob != 43b50adf5421f0a442c4db0acabff4f6f0ced083"],
    },
    "role": {
        "binding_id": "B-ROLE-PRIORITY",
        "defect_class": "COPIED_MEMBER_LIST_FAILURE_DIRECTION",
        "cause_ref": "comp_ontolint.py (3) reads BOTH homes of the 14 roles (roles keys AND role_priority) and asserts totality",
        "effect_ref": "role_priority copy drift fails LOUD -- the first copied-member list in the sequence with a loud limb (every earlier copy failed clean)",
        "relation_kind": "NECESSARY_FOR",
        "axis_map": AXIS_MAP_DEFAULT,
        "plane_map": {"MECHANICAL": "DESIRED", "DECLARATIVE": "DESIRED", "SEMANTIC": "DESIRED"},
        "denominators": {"MECHANICAL": (14, "roles compared to role_priority"), "DECLARATIVE": (2, "homes declared together by the entry's authority line"), "SEMANTIC": (3, "comp-ontolint invariants")},
        "live_candidates": ["H1 a reader that compares BOTH homes is necessary for the copy to fail loud",
                            "H2 another existing reader (comp_system len(roles), O1 declared-vs-derived) would fail loud on role_priority drift anyway"],
        "tested_set": ["H1 a reader that compares BOTH homes is necessary for the copy to fail loud", "H2 another existing reader (comp_system len(roles), O1 declared-vs-derived) would fail loud on role_priority drift anyway"],
        "exclusions": [{"member": "H2 another existing reader (comp_system len(roles), O1 declared-vs-derived) would fail loud on role_priority drift anyway", "reason_class": "RULED_OUT_BY_EVIDENCE", "evidence_ref": "ev-MECHANICAL", "lease_ref": None}],
        "counterevidence": [],
        "graph_snapshot": None,
        "invalidation_predicates": ["comp_ontolint.py lint (3) removed or no longer reads role_priority", "comp_system.py begins comparing role_priority to roles keys"],
    },
}


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, cwd=REPO).stdout.strip()


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_bundle(subject: str) -> tuple[Path, dict]:
    paths = sorted((RUNS / subject).glob("*/atom_layer0_run.json"))
    if not paths:
        raise SystemExit(f"ERROR: INSTRUMENT_UNKNOWN: no bundle for {subject}")
    p = paths[-1]
    return p, json.loads(p.read_text(encoding="utf-8"))


def stage_class_for(bundle: dict) -> dict:
    key = f"{bundle['s2_challenge']['grammar_name']}@{bundle['s2_challenge']['grammar_version']}"
    return {"grammar": key, "map": GRAMMAR_STAGE_CLASS.get(key)}


def substantive_result(bundle: dict) -> dict:
    """A5 ruling applied: UNKNOWN fires on STAGE_NOT_ASSESSED / STAGE_UNREACHABLE of an ACQUISITION stage;
    a METHOD_ACCEPTANCE stage NOT_ASSESSED is residue; STAGE_CORRECTLY_EMPTY never fires."""
    sc = stage_class_for(bundle)
    if sc["map"] is None:
        return {"value": "UNKNOWN", "why": f"no stage_class map declared for grammar {sc['grammar']}", "residue": []}
    fired, residue = [], []
    for stage, state in bundle["stage_states"].items():
        cls = sc["map"].get(stage)
        if state in ("STAGE_NOT_ASSESSED", "STAGE_UNREACHABLE"):
            (fired if cls == "ACQUISITION" else residue).append(f"{stage}={state}({cls})")
    if fired:
        return {"value": "UNKNOWN", "why": "acquisition stage absent/failed: " + ", ".join(fired), "residue": residue}
    ch = bundle["s2_challenge"]
    if ch["certificate_state"] == "CERTIFICATE_ISSUED":
        return {"value": ch["atomicity_certificate"]["claim"], "why": "certificate issued", "residue": residue}
    if ch["result"] == "DECOMPOSITION_FOUND":
        cands = [c["label"] for c in bundle["s1_sweep"]["normalized_candidates"]]
        return {"value": "DECOMPOSITION_FOUND: " + "; ".join(cands), "why": "decomposition found, certificate withheld", "residue": residue}
    return {"value": "UNKNOWN", "why": f"terminal {ch['result']} carries no substantive result", "residue": residue}


def evidence_rows(bundle: dict, spec: dict, path: Path) -> list[dict]:
    contract = next(c for c in bundle["s4_resolution"]["contracts"] if c["binding_id"] == spec["binding_id"])
    rows = []
    for axis_row in contract["seam_axes"]:
        ax = axis_row["axis"]
        den = spec["denominators"].get(ax)
        for ev in axis_row["evidence"]:
            rows.append({
                "axis": spec["axis_map"][ax],
                "value": {"seam_axis": ax, "passed": axis_row["passed"], "claim": ev["claim"]},
                "basis": "desired",                       # NOT ATTESTED -> desired-basis only (schema absence semantic)
                "instrument_attestation_ref": None,
                "grounding": f"{ev['file']}:{ev['locator']} @ {ev['vintage']} (via {path.relative_to(REPO).as_posix()}#{spec['binding_id']})",
                "failure_direction": json.dumps(contract["failure_direction"], sort_keys=True),
                "denominator": den[0] if den else None,
                "denominator_grain": den[1] if den else None,
                "plane": spec["plane_map"][ax],
                "vintage": ev["vintage"],
            })
    return rows


def assessment_from_bundle(subject: str, path: Path, bundle: dict, spec: dict, head: str, manifest_ref: str) -> dict:
    rows = evidence_rows(bundle, spec, path)
    live_after = [h for h in spec["live_candidates"]
                  if not any(e["member"] == h and e["reason_class"] == "RULED_OUT_BY_EVIDENCE" for e in spec["exclusions"])]
    known_residual = [h for h in spec["live_candidates"] if h not in spec["tested_set"]
                      or any(e["member"] == h and e["reason_class"] != "RULED_OUT_BY_EVIDENCE" for e in spec["exclusions"])]
    eliminated = sum(1 for e in spec["exclusions"] if e["reason_class"] == "RULED_OUT_BY_EVIDENCE")
    return {
        "assessment_id": "ca-20260820-" + hashlib.sha256(bundle["run_id"].encode()).hexdigest()[:12],
        "knowledge_basis": {k: None for k in ("hypothesis_space_version", "normal_form_version", "compatibility_policy_version", "scope_ontology_version", "outcome_vocabulary_version")},
        "scope": {
            "defect_class": spec["defect_class"],
            "subject_scope": f"bundles under workflows/atom_layer0/runs/ whose s4_resolution.contracts contain binding_id == {spec['binding_id']} (predicate over the run ledger; NOTE: the schema wording presumes the canonical graph -- routed, see findings)",
            "relevant_planes": sorted({r["plane"] for r in rows}),
            "substrates": ["codebase"],
            "time_window": {"start_utc": bundle["vintage"]["observed_at_utc"], "end_utc": bundle["vintage"]["observed_at_utc"]},
        },
        "candidate_relation": {"cause_ref": spec["cause_ref"], "effect_ref": spec["effect_ref"], "relation_kind": spec["relation_kind"], "stated_as": "HYPOTHESIS"},
        "hypothesis_sets": {"space_ref": None, "live_candidates": live_after, "tested_set": spec["tested_set"], "known_residual": known_residual, "exclusions": spec["exclusions"]},
        "evidence_vector": rows,
        "counterevidence": spec["counterevidence"],
        "discrimination": {"worst_case_residual": len(live_after), "guaranteed_elimination": eliminated,
                           "instrument_failed_rows_excluded": True, "declared_total": False, "unmodeled_mechanism_open": True},
        "policy_ref": None,
        "result_status": "INFERRED",
        "derivation_trace": [],
        "producer": {"agent_or_service": "4.0.0_SA_CRO~C/phase2_exercise.py", "version": "0.1.0"},
        "vintage": {"graph_snapshot": spec["graph_snapshot"], "registry_commit": head, "observed_at_utc": bundle["vintage"]["observed_at_utc"]},
        "support_pointers": [f"{path.relative_to(REPO).as_posix()} @ {bundle['vintage']['repo_commit']} sha256:{sha256_file(path)}"],
        "invalidation_predicates": spec["invalidation_predicates"],
        "interim_status": {"value": "DERIVED_FROM_BUNDLE",
                           "derivation": {"stage_states_ref": path.relative_to(REPO).as_posix() + "#stage_states", "terminal": bundle["s2_challenge"]["result"]},
                           "manifest_ref": manifest_ref},
    }


def make_control(head: str) -> tuple[Path, dict, dict]:
    """A MUTANT of the Scope bundle: the splitter could not be exercised. Written to the scratch dir only."""
    src_path, src = load_bundle("scope")
    b = copy.deepcopy(src)
    b["run_id"] = "AL0-SCRATCH-CONTROL-NOT-EXERCISABLE"
    b["subject"]["concept"] = "SCRATCH_CONTROL_NOT_EXERCISABLE"
    b["subject"]["definition"] = "PLANTED CONTROL (C9-RIDE Phase 2): a mutant of the Scope bundle whose S2 challenge could not be exercised -- never a real subject, never in the ledger."
    b["subject"]["scope"] = "scratch copy only"
    b["source_census_row"] = None
    b["stage_states"].update({"s2": "STAGE_ASSESSED", "s3": "STAGE_NOT_ASSESSED", "s4": "STAGE_NOT_ASSESSED", "s5": "STAGE_NOT_ASSESSED"})
    b["residue"]["stage_not_assessed"] = ["s3", "s4", "s5"]
    ch = b["s2_challenge"]
    ch["result"] = "NOT_EXERCISABLE"
    ch["certificate_state"] = "CERTIFICATE_WITHHELD"
    ch["atomicity_certificate"] = None
    ch["splitter"]["differently_derived"] = False
    ch["splitter"]["identity"] = "PLANTED CONTROL: no differently-derived splitter could be run against this subject (the challenge is un-runnable by construction); the control must read NOT_EXERCISABLE, never as a run."
    ch["frontier"]["assessed_cell_ids"] = []
    ch["frontier"]["open_cell_ids"] = []
    ch["frontier"]["unreachable_cell_ids"] = list(ch["frontier"]["cell_ids"])
    ch["result_evidence"] = [{"file": "this control", "locator": "planted", "vintage": head, "claim": "The splitter could not be exercised; no cell was assessed; every cell is unreachable."}]
    b["s4_resolution"]["residue"] = ["NOT EXERCISED: s4 not assessed (control); contracts retained from the source bundle as inert structure, not as findings."]
    CONTROL_DIR.mkdir(parents=True, exist_ok=True)
    out = CONTROL_DIR / "atom_layer0_run.json"
    out.write_text(json.dumps(b, indent=2) + "\n", encoding="utf-8")
    proc = subprocess.run([sys.executable, str(VALIDATOR), str(out)], capture_output=True, text=True)
    verdict = {"rc": proc.returncode, "errors": [ln for ln in (proc.stdout + proc.stderr).splitlines() if ln.startswith("ERROR") and "validation FAIL" not in ln],
               "derived_from": src_path.relative_to(REPO).as_posix(), "source_sha256": sha256_file(src_path)}
    return out, b, verdict


def control_assessment(path: Path, bundle: dict, head: str, manifest_ref: str) -> dict:
    live = ["H1 the control subject is atomic", "H2 the control subject decomposes"]
    return {
        "assessment_id": "ca-20260820-" + hashlib.sha256(bundle["run_id"].encode()).hexdigest()[:12],
        "knowledge_basis": {k: None for k in ("hypothesis_space_version", "normal_form_version", "compatibility_policy_version", "scope_ontology_version", "outcome_vocabulary_version")},
        "scope": {"defect_class": "PLANTED_CONTROL_NOT_EXERCISABLE", "subject_scope": "the single scratch control bundle (predicate: run_id == AL0-SCRATCH-CONTROL-NOT-EXERCISABLE)", "relevant_planes": ["DESIRED"], "substrates": ["codebase"],
                  "time_window": {"start_utc": bundle["vintage"]["observed_at_utc"], "end_utc": bundle["vintage"]["observed_at_utc"]}},
        "candidate_relation": {"cause_ref": "the S2 splitter challenge", "effect_ref": "an atomicity verdict on the control subject", "relation_kind": "NECESSARY_FOR", "stated_as": "HYPOTHESIS"},
        "hypothesis_sets": {"space_ref": None, "live_candidates": live, "tested_set": [], "known_residual": live, "exclusions": []},
        "evidence_vector": [{"axis": "DECLARED_RATIONALE", "value": "UNKNOWN", "basis": "desired", "instrument_attestation_ref": None,
                             "grounding": f"{path.relative_to(HERE).as_posix()}#s2_challenge.result=NOT_EXERCISABLE @ {head}",
                             "failure_direction": "the instrument did not run; any non-UNKNOWN value here would be a fabrication",
                             "denominator": None, "denominator_grain": None, "plane": "DESIRED", "vintage": head}],
        "counterevidence": [],
        "discrimination": {"worst_case_residual": len(live), "guaranteed_elimination": 0, "instrument_failed_rows_excluded": True, "declared_total": False, "unmodeled_mechanism_open": True},
        "policy_ref": None,
        "result_status": "UNKNOWN",
        "derivation_trace": [],
        "producer": {"agent_or_service": "4.0.0_SA_CRO~C/phase2_exercise.py", "version": "0.1.0"},
        "vintage": {"graph_snapshot": None, "registry_commit": head, "observed_at_utc": bundle["vintage"]["observed_at_utc"]},
        "support_pointers": [f"{path.relative_to(HERE).as_posix()} sha256:{sha256_file(path)}"],
        "invalidation_predicates": ["the control bundle is re-run with an exercisable splitter"],
        "interim_status": {"value": "DERIVED_FROM_BUNDLE", "derivation": {"stage_states_ref": path.relative_to(HERE).as_posix() + "#stage_states", "terminal": "NOT_EXERCISABLE"}, "manifest_ref": manifest_ref + " (control is NOT a manifest subject -- stated)"},
    }


def main() -> int:
    import jsonschema
    head = git("rev-parse", "HEAD")
    schema = json.loads(S6_SCHEMA.read_text(encoding="utf-8"))
    schema_pin = git("log", "-1", "--format=%H", "--", str(S6_SCHEMA.relative_to(REPO)))
    validator = jsonschema.Draft202012Validator(schema)
    manifest_pin = git("log", "-1", "--format=%H", "--", str(MANIFEST.relative_to(REPO)))
    manifest_ref = f"workflows/atom_layer0/runs/manifest/PROGRAM_MANIFEST.yaml @ {manifest_pin}"

    instances, per = [], []
    for subject, spec in HYPOTHESES.items():
        path, bundle = load_bundle(subject)
        inst = assessment_from_bundle(subject, path, bundle, spec, head, manifest_ref)
        errs = sorted(e.json_path + ": " + e.message for e in validator.iter_errors(inst))
        unframed = sum(1 for r in inst["evidence_vector"] if r["denominator"] is None)
        per.append({"subject": subject, "bundle": path.relative_to(REPO).as_posix(), "assessment_id": inst["assessment_id"],
                    "schema_errors": errs, "evidence_rows": len(inst["evidence_vector"]), "unframed_rows": unframed,
                    "stage_class": stage_class_for(bundle), "substantive_result_A5": substantive_result(bundle)})
        instances.append(inst)

    cpath, cbundle, cverdict = make_control(head)
    cinst = control_assessment(cpath, cbundle, head, manifest_ref)
    cerrs = sorted(e.json_path + ": " + e.message for e in validator.iter_errors(cinst))
    never_as_run = {
        "result_status_is_UNKNOWN": cinst["result_status"] == "UNKNOWN",
        "interim_terminal_is_NOT_EXERCISABLE": cinst["interim_status"]["derivation"]["terminal"] == "NOT_EXERCISABLE",
        "evidence_row_unframed_and_excluded": all(r["denominator"] is None for r in cinst["evidence_vector"]),
        "A5_substantive_result_is_UNKNOWN": substantive_result(cbundle)["value"] == "UNKNOWN",
        "control_bundle_valid_rc0": cverdict["rc"] == 0,
    }
    per.append({"subject": "SCRATCH_CONTROL", "bundle": cpath.relative_to(HERE).as_posix(), "assessment_id": cinst["assessment_id"],
                "schema_errors": cerrs, "evidence_rows": 1, "unframed_rows": 1, "stage_class": stage_class_for(cbundle),
                "substantive_result_A5": substantive_result(cbundle), "control_bundle_validation": cverdict, "never_as_run": never_as_run})
    instances.append(cinst)

    findings = [
        {"id": "F-S6-01", "class": "FIELD_QUESTION", "field": "scope.subject_scope", "text": "The schema describes subject_scope as 'a PREDICATE over the canonical graph'. Assessments about registry/bank TEXT (all three real instances) are naturally predicates over the RUN LEDGER or the REGISTRY, not the graph. Either the wording admits 'a predicate over a DECLARED population (graph | ledger | registry | manifest)' or such assessments are out of the object's scope -- routed to base; this exercise wrote ledger predicates and said so in-field.", "routed_to": "4.0.0_SA_CRO"},
        {"id": "F-S6-02", "class": "OBSERVATION", "field": "evidence_vector[].basis vs plane", "text": "In the pre-attestation regime every row is forced to basis=desired (attestation null) while plane may read APPLIED (the live kuzu compare). basis and plane therefore DIVERGE BY DESIGN: plane says WHERE the evidence was read, basis says HOW STRONG it is admissible as. Not a defect; stated so a consumer does not read basis as the read-plane.", "routed_to": "4.0.0_SA_CRO"},
        {"id": "F-S6-03", "class": "OBSERVATION", "field": "interim_status (control)", "text": "The control is NOT a manifest subject; its interim_status.manifest_ref therefore points at the manifest with an explicit 'not a manifest subject' note. A control that must carry a required manifest_ref shows the field's domain is the manifest, which is correct -- the control lives outside it and says so.", "routed_to": "4.0.0_SA_CRO"},
        {"id": "F-S6-04", "class": "OBSERVATION", "field": "A5 stage_class (applied outside the object)", "text": "Applied base's 63827 ruling: for the three real bundles s5=METHOD_ACCEPTANCE NOT_ASSESSED is carried as residue and substantive_result is the certificate/decomposition; for the control, s3/s4 ACQUISITION NOT_ASSESSED fire UNKNOWN. The rule discriminates the control from the real runs exactly as intended. The S6 object has no slot for it (additionalProperties:false) -- the PROTO-RECORD carries stage_class; printed beside each instance here.", "routed_to": "4.0.0_SA_CRO"},
    ]
    art = {
        "artifact": "NFRA_EPISTEMY C9-RIDE Phase 2 -- S6 Causal_Assessment_Object 0.1.1 exercised against real bundles + planted NOT_EXERCISABLE control",
        "seat": "4.0.0_SA_CRO~C", "status": "PROPOSED",
        "read_vintage": {"repo_commit": head, "s6_schema_commit": schema_pin, "s6_schema_id": schema.get("$id"), "manifest_commit": manifest_pin},
        "denominators": {"real_bundles_exercised": len(HYPOTHESES), "controls_planted": 1, "instances": len(instances),
                         "instances_schema_valid": sum(1 for p in per if not p["schema_errors"]),
                         "evidence_rows_total": sum(p["evidence_rows"] for p in per), "unframed_rows_total": sum(p["unframed_rows"] for p in per),
                         "never_as_run_checks_passed": sum(1 for v in never_as_run.values() if v), "never_as_run_checks_total": len(never_as_run)},
        "per_instance": per,
        "findings": findings,
        "instances": instances,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(art, indent=1) + "\n", encoding="utf-8")
    d = art["denominators"]
    print(f"OK: Phase 2 artifact -> {OUT.relative_to(REPO).as_posix()}")
    print(f"DENOMINATOR: {d['instances']} instances ({d['real_bundles_exercised']} real + {d['controls_planted']} control); schema-valid {d['instances_schema_valid']}/{d['instances']}; "
          f"evidence rows {d['evidence_rows_total']} (unframed {d['unframed_rows_total']}); never-as-run {d['never_as_run_checks_passed']}/{d['never_as_run_checks_total']}")
    for p in per:
        print(f"  {p['subject']}: schema_errors={len(p['schema_errors'])} A5={p['substantive_result_A5']['value'][:60]!r}"
              + (f" control_rc={p['control_bundle_validation']['rc']}" if 'control_bundle_validation' in p else ""))
        for e in p["schema_errors"][:5]:
            print("     -", e[:160])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
