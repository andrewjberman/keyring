"""NFRA_EPISTEMY C9-RIDE Phase 1 -- S0 ground-read of the landed atom_layer0 run bundles.

Enumerates workflows/atom_layer0/runs/<subject>/<stamp>/atom_layer0_run.json (denominator
printed), reads each bundle's stage_states + terminal + certificate_state + contract counts,
validates each against the package validator AT THE READ VINTAGE, and writes one deterministic
JSON artifact beside this script's parent (S0_GROUND_READ.json). Re-running at the same HEAD over
the same bundles yields a byte-identical artifact (no wall-clock inside; the only clocks are the
pins it reads). Read-only on every input. The interim axis it derives is the RULED one (63662/63664,
S6 schema 0.1.1 interim_status): DERIVED_FROM_BUNDLE over bundles that exist; the absence member is
populated by predicate over the PROGRAM MANIFEST (its denominator), never over the run set.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                           capture_output=True, text=True, check=True).stdout.strip())
RUNS = REPO / "workflows/atom_layer0/runs"
MANIFEST = RUNS / "manifest/PROGRAM_MANIFEST.yaml"
VALIDATOR = REPO / "org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ATOM_LAYER0/scripts/validate_run.py"
OUT = Path(__file__).resolve().parent.parent / "S0_GROUND_READ.json"

TERMINALS = ["DECOMPOSITION_FOUND", "DECLARED_FRONTIER_EXHAUSTED",
             "BUDGET_EXHAUSTED_WITH_FRONTIER_OPEN", "INSTRUMENT_UNKNOWN", "NOT_EXERCISABLE"]


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, cwd=REPO).stdout.strip()


def main() -> int:
    head = git("rev-parse", "HEAD")
    validator_pin = git("log", "-1", "--format=%H", "--", str(VALIDATOR.relative_to(REPO)))
    validator_dirty = bool(git("status", "--porcelain", "--", str(VALIDATOR.relative_to(REPO))))

    bundles = sorted(RUNS.glob("*/*/atom_layer0_run.json"))
    rows = []
    for f in bundles:
        r = json.loads(f.read_text(encoding="utf-8"))
        proc = subprocess.run([sys.executable, str(VALIDATOR), str(f)], capture_output=True, text=True)
        errs = [ln for ln in (proc.stdout + proc.stderr).splitlines()
                if ln.startswith("ERROR") and "validation FAIL" not in ln]
        contracts = r["s4_resolution"]["contracts"]
        rows.append({
            "concept": r["subject"]["concept"],
            "run_dir": f.parent.relative_to(RUNS).as_posix() + "/",
            "run_id": r["run_id"],
            "evidence_vintage": r["vintage"]["repo_commit"],
            "observed_at_utc": r["vintage"]["observed_at_utc"],
            "stage_states": r["stage_states"],
            "terminal": r["s2_challenge"]["result"],
            "certificate_state": r["s2_challenge"]["certificate_state"],
            "contracts": len(contracts),
            "unresolved": sum(1 for c in contracts if not c["resolved"]),
            "rule24_record_ids": len(r["rule24_record_ids"]),
            "source_census_row": (r.get("source_census_row") or {}).get("id"),
            "validator_at_read": {"rc": proc.returncode, "errors": errs},
            "interim_status": {"value": "DERIVED_FROM_BUNDLE",
                               "derivation": {"stage_states_ref": f.relative_to(REPO).as_posix() + "#stage_states",
                                              "terminal": r["s2_challenge"]["result"]}},
        })

    manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    manifest_pin = git("log", "-1", "--format=%H", "--", str(MANIFEST.relative_to(REPO)))
    by_concept = {x["concept"] for x in rows}
    completed_terms = [c["term"] for c in manifest["completed"]]
    queued_terms = [q["term"] for q in manifest["queue"]]
    absent = [{"term": t, "interim_status": {"value": "ACQUISITION_FAILED_NO_BUNDLE", "derivation": None,
                                             "manifest_ref": f"PROGRAM_MANIFEST.yaml @ {manifest_pin} (QUEUED rank {q['rank']})"}}
              for q in manifest["queue"] for t in [q["term"]] if t not in by_concept]
    completed_missing_bundle = [t for t in completed_terms if t not in by_concept]

    terminal_counts = {t: sum(1 for x in rows if x["terminal"] == t) for t in TERMINALS}
    unseen = [t for t in TERMINALS if terminal_counts[t] == 0]

    art = {
        "artifact": "NFRA_EPISTEMY C9-RIDE Phase 1 -- S0 ground-read of landed atom_layer0 bundles",
        "seat": "4.0.0_SA_CRO~C",
        "status": "PROPOSED",
        "read_vintage": {"repo_commit": head, "validator_commit": validator_pin, "validator_working_tree_dirty": validator_dirty,
                         "manifest_commit": manifest_pin},
        "denominators": {
            "bundles_found": len(rows),
            "subject_dirs": len({x["run_dir"].split("/")[0] for x in rows}),
            "manifest_terms_total": manifest["denominators"]["registry_terms_total"],
            "manifest_completed": len(completed_terms),
            "manifest_queued": len(queued_terms),
            "interim_DERIVED_FROM_BUNDLE": len(rows),
            "interim_ACQUISITION_FAILED_NO_BUNDLE": len(absent),
            "completed_terms_without_bundle": completed_missing_bundle,
            "validator_rc0_at_read": sum(1 for x in rows if x["validator_at_read"]["rc"] == 0),
            "validator_nonzero_at_read": sum(1 for x in rows if x["validator_at_read"]["rc"] != 0),
            "contracts_total": sum(x["contracts"] for x in rows),
            "unresolved_total": sum(x["unresolved"] for x in rows),
            "terminal_counts": terminal_counts,
            "terminals_unseen_in_ledger": unseen,
        },
        "bundles": rows,
        "absent_by_manifest_predicate": absent,
        "notes": [
            "A bundle that exists but fails the validator AT READ VINTAGE is still DERIVED_FROM_BUNDLE: validity is vintage-relative (ruling 63721, vintage-aware law pending) and is carried as validator_at_read, an ATTRIBUTE of the row, not a third member of the interim axis.",
            "The absence member's denominator is the MANIFEST's (queued terms without a bundle), never the run set's -- the run set cannot enumerate its own absences.",
            "terminals_unseen_in_ledger is printed so that an unexercised terminal (e.g. NOT_EXERCISABLE) is never read as impossible; Phase 2 plants a control for it on a scratch copy.",
        ],
    }
    OUT.write_text(json.dumps(art, indent=1, sort_keys=False) + "\n", encoding="utf-8")
    print(f"OK: S0 ground-read written -> {OUT.relative_to(REPO).as_posix()}")
    print(f"DENOMINATOR: {len(rows)} bundles in {art['denominators']['subject_dirs']} subject dirs; "
          f"manifest {len(completed_terms)} completed / {len(queued_terms)} queued; "
          f"ACQUISITION_FAILED_NO_BUNDLE = {len(absent)} (manifest predicate)")
    print(f"validator@read {validator_pin[:10]}{' (DIRTY)' if validator_dirty else ''}: rc0={art['denominators']['validator_rc0_at_read']} "
          f"nonzero={art['denominators']['validator_nonzero_at_read']}")
    print(f"terminals: {terminal_counts}; unseen: {unseen}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
