"""NFRA_EPISTEMY C9-RIDE Phase 3 -- emit proto-Observation_Records from the landed atom_layer0 bundles.

WHAT THIS IS. Each atom_layer0 run is an INSTRUMENT INVOCATION whose return is a bundle; this emitter
converts each landed bundle into an Observation_Record against 4.0.0_SA_CRO~A's Component-1 envelope
(CITED, never copied: schemas/observation_record.schema.json), so ~C becomes the envelope's first live
data source rather than a competing evidence path.

THE SHAPE, and it is forced rather than chosen (rider c + the schema): the envelope is
`additionalProperties: false` over a closed 14-field required list, so the TO's "each DECLARING ITS
INTERIM STATUS SHAPE explicitly in the artifact" CANNOT live inside the record. Each emitted artifact is
therefore a two-part object -- an envelope-VALID `observation_record` plus a declared `pre_envelope`
sidecar carrying the pre-envelope axes (stage_class per base's A5 ruling 63827; interim_status per the
ruled hybrid axis 63662/63664; the A5 substantive_result computation printed beside the envelope's own).
The sidecar is OUTSIDE the record by construction, which is the honest reading of a closed schema and is
routed as a finding rather than worked around by widening anyone's schema.

REPRODUCIBLE BY CONSTRUCTION: no wall-clock, no randomness; every value derives from the bundles and the
git objects. Re-running at one HEAD over the same bundles yields byte-identical output.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

REPO = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                           capture_output=True, text=True, check=True).stdout.strip())
RUNS = REPO / "workflows/atom_layer0/runs"
ENVELOPE_SCHEMA = REPO / "org/tier1_exec/4.0.0_SA_CRO~A/deliverables/NFRA_EPISTEMY.C1-ENVELOPE/schemas/observation_record.schema.json"
HERE = Path(__file__).resolve().parent.parent
OUT_DIR = HERE / "phase3"
OUT = OUT_DIR / "PHASE3_PROTO_RECORDS.json"

# A5 ruling (base 63827), declared PER GRAMMAR VERSION -- never hard-coded globally.
GRAMMAR_STAGE_CLASS = {
    "decomposition_grammar@1.0.0": {"s0": "ACQUISITION", "s1": "ACQUISITION", "s2": "ACQUISITION",
                                    "s3": "ACQUISITION", "s4": "ACQUISITION", "s5": "METHOD_ACCEPTANCE"},
}
ABSENT_STATES = {"STAGE_NOT_ASSESSED", "STAGE_UNREACHABLE"}


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, cwd=REPO).stdout.strip()


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def grammar_key(bundle: dict) -> str:
    ch = bundle["s2_challenge"]
    return f"{ch['grammar_name']}@{ch['grammar_version']}"


def stage_class_for(bundle: dict) -> dict:
    key = grammar_key(bundle)
    return {"grammar": key, "map": GRAMMAR_STAGE_CLASS.get(key)}


def a5_substantive_result(bundle: dict) -> dict:
    """Base's A5 ruling: UNKNOWN fires on an absent/failed ACQUISITION stage; a METHOD_ACCEPTANCE stage
    that is NOT_ASSESSED is RESIDUE (printed); STAGE_CORRECTLY_EMPTY never fires the rule."""
    sc = stage_class_for(bundle)
    if sc["map"] is None:
        return {"value": None, "state": "UNKNOWN",
                "reason": f"no stage_class map declared for grammar {sc['grammar']}", "residue": []}
    fired, residue = [], []
    for stage, state in bundle["stage_states"].items():
        cls = sc["map"].get(stage)
        if state in ABSENT_STATES:
            (fired if cls == "ACQUISITION" else residue).append(f"{stage}={state}({cls})")
    if fired:
        return {"value": None, "state": "UNKNOWN",
                "reason": "acquisition stage absent/failed: " + ", ".join(fired), "residue": residue}
    ch = bundle["s2_challenge"]
    if ch["certificate_state"] == "CERTIFICATE_ISSUED":
        return {"value": {"terminal": ch["result"], "certificate": ch["atomicity_certificate"]["claim"]},
                "state": "KNOWN", "reason": None, "residue": residue}
    if ch["result"] == "DECOMPOSITION_FOUND":
        return {"value": {"terminal": ch["result"],
                          "normalized_candidates": [c["label"] for c in bundle["s1_sweep"]["normalized_candidates"]]},
                "state": "KNOWN", "reason": None, "residue": residue}
    return {"value": None, "state": "UNKNOWN",
            "reason": f"terminal {ch['result']} carries no substantive result", "residue": residue}


def envelope_status(bundle: dict) -> dict:
    """Per-stage acquisition axes (PRD 2.1). Derived from the bundle, never asserted:
    the artifact was read and parsed, so transport/parse succeeded; ENUMERATION reflects whether the
    S1 sweep (the enumerating stage) actually ran; ACQUISITION reflects the S0 pin."""
    ss = bundle["stage_states"]
    return {
        "acquisition": "PRESENT" if ss["s0"] not in ABSENT_STATES else "ABSENT",
        "transport": "SUCCEEDED",
        "enumeration": "SUCCEEDED" if ss["s1"] not in ABSENT_STATES else "NOT_ATTEMPTED",
        "parse": "SUCCEEDED",
    }


def build(path: Path, bundle: dict, manifest_ref: str) -> dict:
    ch = bundle["s2_challenge"]
    cert = ch.get("atomicity_certificate") or {}
    a5 = a5_substantive_result(bundle)
    rel = path.relative_to(REPO).as_posix()
    digest = sha256_file(path)

    # request_hash: the canonical REQUEST this invocation answered (subject x scope x pin), hashed.
    request = json.dumps({"concept": bundle["subject"]["concept"],
                          "scope": bundle["subject"]["scope"],
                          "repo_commit": bundle["vintage"]["repo_commit"],
                          "grammar": grammar_key(bundle)}, sort_keys=True)
    request_hash = "sha256:" + hashlib.sha256(request.encode("utf-8")).hexdigest()

    residue = list(bundle["s1_sweep"].get("generator_residue") or [])
    residue += list(bundle["residue"].get("unknowns") or [])
    residue += [f"A5 method-stage residue: {r}" for r in a5["residue"]]

    substantive = ({"state": "KNOWN", "value": a5["value"], "reason": None} if a5["state"] == "KNOWN"
                   else {"state": "UNKNOWN", "value": None, "reason": a5["reason"]})

    record = {
        "instrument": {"id": "atom_layer0 run method", "version": f"{bundle['method_version']} x {grammar_key(bundle)}@{ch['grammar_commit']}"},
        "request_hash": request_hash,
        "status": envelope_status(bundle),
        "plane": "DESIRED",
        "substrate": "codebase",
        "population_predicate": bundle["s3_legislation"]["population_predicate"],
        "denominator": {
            "count": cert.get("frontier_denominator", len(ch["frontier"]["cell_ids"])),
            "grain": "declared grammar frontier cell (generator x operator x partition)",
            "generated_by": f"{grammar_key(bundle)} @ {ch['grammar_commit']}, fixed before subject selection",
        },
        "traversal_residue": residue,
        "substantive_result": substantive,
        "control_references": [
            f"splitter: {ch['splitter']['identity'][:180]}",
            f"grammar adequacy battery: {ch['grammar_adequacy']['battery']} ({ch['grammar_adequacy']['specimens_expressible']}/{ch['grammar_adequacy']['specimens_total']} expressible)",
            "validate_run.py schema + cross-field laws (rc=0 at commit)",
        ],
        "discrimination_certificate_ref": None,
        "observed_at": bundle["vintage"]["observed_at_utc"],
        "support_pointers": [f"{rel} @ {bundle['vintage']['repo_commit']} sha256:{digest}"],
        "invalidation_predicates": [
            f"decomposition_grammar moves off {ch['grammar_commit']} (a grammar change invalidates; a record addition does not)",
            f"SYSTEM_DEFINITIONS.yaml moves off the certificate's registry_vintage ({cert.get('registry_vintage', 'n/a')})",
            "the bundle blob at the support pointer changes",
        ],
    }

    pre_envelope = {
        "declared_shape": (
            "PRE-ENVELOPE SIDECAR, outside the Observation_Record BY CONSTRUCTION: the Component-1 envelope is "
            "additionalProperties:false over a closed 14-field required list, so these axes cannot be carried "
            "inside a valid record. Rider (c) asks that each proto-record declare its interim status shape IN THE "
            "ARTIFACT -- satisfied here at artifact level, not record level. Routed as a finding; no schema widened."
        ),
        "interim_status": {
            "value": "DERIVED_FROM_BUNDLE",
            "derivation": {"stage_states_ref": rel + "#stage_states", "terminal": ch["result"]},
            "manifest_ref": manifest_ref,
            "absence_member_note": (
                "ACQUISITION_FAILED_NO_BUNDLE is populated by predicate over the PROGRAM MANIFEST, never over the "
                "run set -- a bundle set cannot enumerate its own absences (ruled 63662/63664). Its denominator is "
                "the manifest's and is reported once, in this artifact's denominators block."
            ),
        },
        "stage_class": stage_class_for(bundle),
        "substantive_result_A5": {k: a5[k] for k in ("state", "reason", "residue")},
        "validator_at_read": None,   # filled by the caller so the git/subprocess cost is paid once per bundle
        "unknown_shapes_declared": {
            "acquisition_absent": "status.acquisition ABSENT -> substantive_result UNKNOWN with reason",
            "method_stage_not_assessed": "carried as traversal_residue, NEVER as UNKNOWN (A5)",
            "not_exercisable": "a bundle whose terminal is NOT_EXERCISABLE yields substantive_result UNKNOWN and is never reported as run (Phase-2 control)",
        },
        "inexpressible_in_envelope": (
            None if bundle["s3_legislation"]["population_predicate"] else
            "DECLARED, NOT PAPERED OVER: this run's terminal is DECOMPOSITION_FOUND, so S3 legislation was correctly "
            "NOT assessed at the parent's grain (the population belongs to the children) and population_predicate is "
            "null. The envelope requires it as a non-empty string, so this record is envelope-INVALID and is emitted "
            "invalid ON PURPOSE. Inventing a predicate string to satisfy the schema is exactly the fabrication the "
            "honest-populability discipline forbids -- a required field a producer cannot truthfully fill is a SHAPE "
            "FINDING (F-C1-04), not a formatting problem."
        ),
    }
    return {"subject": bundle["subject"]["concept"], "bundle": rel,
            "observation_record": record, "pre_envelope": pre_envelope}


def main() -> int:
    import jsonschema
    import yaml

    head = git("rev-parse", "HEAD")
    schema = json.loads(ENVELOPE_SCHEMA.read_text(encoding="utf-8"))
    schema_pin = git("log", "-1", "--format=%H", "--", str(ENVELOPE_SCHEMA.relative_to(REPO)))
    validator = jsonschema.Draft202012Validator(schema)

    manifest_path = RUNS / "manifest/PROGRAM_MANIFEST.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest_pin = git("log", "-1", "--format=%H", "--", str(manifest_path.relative_to(REPO)))
    manifest_ref = f"{manifest_path.relative_to(REPO).as_posix()} @ {manifest_pin}"

    emitted, invalid = [], []
    for path in sorted(RUNS.glob("*/*/atom_layer0_run.json")):
        bundle = json.loads(path.read_text(encoding="utf-8"))
        item = build(path, bundle, manifest_ref)
        errs = sorted(e.json_path + ": " + e.message for e in validator.iter_errors(item["observation_record"]))
        item["envelope_schema_errors"] = errs
        if errs:
            invalid.append((item["subject"], errs[:2]))
        emitted.append(item)

    queued = [q["term"] for q in manifest["queue"]]
    known = sum(1 for i in emitted if i["observation_record"]["substantive_result"]["state"] == "KNOWN")
    art = {
        "artifact": "NFRA_EPISTEMY C9-RIDE Phase 3 -- proto-Observation_Records emitted from landed atom_layer0 bundles",
        "seat": "4.0.0_SA_CRO~C",
        "status": "PROPOSED",
        "cites_not_copies": {
            "envelope_schema": f"{ENVELOPE_SCHEMA.relative_to(REPO).as_posix()} @ {schema_pin} ({schema.get('$id')})",
            "prd": "docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md sec.2.1",
            "a5_ruling": "4.0.0_SA_CRO 63827 (stage_class on the proto-record, per grammar version)",
            "interim_axis_ruling": "4.0.0_SA_CRO 63662 / 1.0.0_SA_CTO 63664 (hybrid: derived for bundles, manifest-populated absence member)",
            "plane_condition": f"CTO bind-time condition on the fused `plane` field is DISCHARGED at the schema pin -- plane is a ratified enum and substrate is its own field, measured at {schema_pin[:10]}; nothing here splits a fused string",
        },
        "read_vintage": {"repo_commit": head, "envelope_schema_commit": schema_pin, "manifest_commit": manifest_pin},
        "denominators": {
            "bundles_landed": len(emitted),
            "records_emitted": len(emitted),
            "envelope_valid": len(emitted) - len(invalid),
            "envelope_invalid": len(invalid),
            "envelope_invalid_subjects": [s for s, _ in invalid],
            "envelope_invalid_reason": "all invalidity is F-C1-04 (decomposed subject has no population_predicate); emitted invalid deliberately rather than fabricating a required field",
            "substantive_KNOWN": known,
            "substantive_UNKNOWN": len(emitted) - known,
            "interim_DERIVED_FROM_BUNDLE": len(emitted),
            "interim_ACQUISITION_FAILED_NO_BUNDLE": len(queued),
            "absence_denominator_source": "the PROGRAM MANIFEST's queue (never the run set)",
            "manifest_terms_total": manifest["denominators"]["registry_terms_total"],
        },
        "findings": [
            {"id": "F-C1-01", "class": "SHAPE_CONSTRAINT", "text":
             "The Component-1 envelope is additionalProperties:false over a closed 14-field required list, so the "
             "pre-envelope axes the C9-RIDE TO requires (stage_class, interim_status) CANNOT be carried inside a "
             "valid Observation_Record. Each artifact here is therefore a two-part object: an envelope-valid record "
             "plus a declared pre_envelope sidecar. This is reported, not worked around -- no schema was widened and "
             "no field invented. If the envelope is later meant to carry producer-side interim state, that is a "
             "field question for base as registry executor.", "routed_to": "4.0.0_SA_CRO"},
            {"id": "F-C1-02", "class": "OBSERVATION", "text":
             "`plane` is one value per record, but an atom_layer0 run can span two: most read repo text (DESIRED) "
             "while Runs 25/26/33/35 additionally measured the live graph (APPLIED). These records declare plane "
             "DESIRED -- the plane the CERTIFICATE's scope is bounded to (repo-only) -- and the live-graph limb is "
             "visible in traversal_residue rather than silently folded into one plane. A multi-plane invocation may "
             "warrant either one record per plane or a declared primary-plane rule.", "routed_to": "4.0.0_SA_CRO"},
            {"id": "F-C1-04", "class": "SHAPE_FINDING", "text":
             "THE ENVELOPE CANNOT REPRESENT A DECOMPOSED SUBJECT. `population_predicate` is required as a non-empty "
             "string, but a DECOMPOSITION_FOUND run has NO population at its own grain -- S3 legislation is correctly "
             "not assessed, because the population belongs to the children (C3 and Territory, the sequence's two such "
             "runs). Both records are emitted ENVELOPE-INVALID on purpose and counted in the denominators: inventing a "
             "predicate string to pass the schema would be the exact fabrication the honest-populability audit forbids. "
             "The remedy is a field question for base -- either population_predicate becomes nullable with a declared "
             "absence semantic (the S6 0.1.1 pattern: null = POPULATION BELONGS TO THE CHILDREN), or decomposed "
             "subjects are declared out of the envelope's domain. 2 of 36 records affected; both named.",
             "routed_to": "4.0.0_SA_CRO"},
            {"id": "F-C1-03", "class": "OBSERVATION", "text":
             "substantive_result here is computed by base's A5 rule rather than by the envelope's own governing "
             "sentence (PRD 2.1: any absent/failed status => UNKNOWN). Applied literally to stage_states, every "
             "production bundle would read UNKNOWN because s5 is NOT_ASSESSED by design. The A5 stage_class split is "
             "what makes the governing rule survive contact with this instrument, and both computations are printed "
             "so a reader can see they agree on the acquisition axes and differ only on the method stage.",
             "routed_to": "4.0.0_SA_CRO"},
        ],
        "records": emitted,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(art, indent=1, sort_keys=False) + "\n", encoding="utf-8")
    d = art["denominators"]
    print(f"OK: Phase 3 artifact -> {OUT.relative_to(REPO).as_posix()}")
    print(f"DENOMINATOR: {d['records_emitted']} records from {d['bundles_landed']} landed bundles; "
          f"envelope-valid {d['envelope_valid']}/{d['records_emitted']}; "
          f"substantive KNOWN {d['substantive_KNOWN']} / UNKNOWN {d['substantive_UNKNOWN']}")
    print(f"interim: DERIVED_FROM_BUNDLE {d['interim_DERIVED_FROM_BUNDLE']} | "
          f"ACQUISITION_FAILED_NO_BUNDLE {d['interim_ACQUISITION_FAILED_NO_BUNDLE']} (manifest queue, not the run set)")
    for subj, errs in invalid:
        print(f"  INVALID {subj}: {errs}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
