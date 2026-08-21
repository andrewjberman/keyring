"""ATOM_LAYER0 integration driver (seat 4.0.0_SA_CRO~C).

Batch-compiles every UNRESOLVED census row into an atom_layer0 run bundle via
~A's --compile-census-row interface, and runs the per-row VINTAGE-DRIFT GUARD
(base CRO binding addition, msg 63335): compare each evidence surface's blob at
the row's pinned vintage against HEAD. A moved surface makes the row's evidence
a PRIOR, not a fact -- those rows are flagged for direct re-read before any
disposition is filed.

Writes: run_bundles/R###_run.json (one per unresolved row) and
vintage_guard_report.json. Read-only on every owner surface.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(subprocess.run(
    ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True
).stdout.strip())

SEAT = REPO / "org/tier1_exec/4.0.0_SA_CRO~C/deliverables/ATOM_LAYER0_INTEGRATION"
CENSUS = REPO / "org/tier1_exec/4.0.0_SA_CRO~B/deliverables/ATOM_LAYER0_RESOLUTION_CENSUS_20260820.yaml"
VALIDATOR = REPO / "org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ATOM_LAYER0/scripts/validate_run.py"
BUNDLES = SEAT / "run_bundles"

# Worst-first per the census's own display_verdict_precedence.
WORST_FIRST = [
    "R015",                                                  # AMBIGUOUS_TWO_HOMES
    "R010",                                                  # GOVERNED_DUAL_CARRIER
    "R027", "R028",                                          # CODE_REDECLARATION
    "R001", "R002", "R018", "R021", "R022", "R023", "R024",  # CONTENT_MISMATCH
    "R025", "R026", "R047", "R051", "R052", "R056", "R059",
    "R020", "R042", "R046", "R048", "R049", "R054", "R058",  # SUPERSEDED_UNBANNERED
    "R006", "R007", "R016",                                  # NO_DECLARED_TARGET_CONTENT
    "R012",                                                  # NON_INDEPENDENT_RESOLUTION
    "R045",                                                  # NOT_EXERCISABLE
]

PATH_RE = re.compile(r"(?:^|;\s*)((?:infra|org|docs)/[^\s:;]+)")
PIN_RE = re.compile(r"@\s*([0-9a-f]{10,40})")


def load_rows():
    import yaml
    doc = yaml.safe_load(CENSUS.read_text(encoding="utf-8"))
    return {r["id"]: r for r in doc["rows"]}


def blob(commit: str, path: str) -> str | None:
    r = subprocess.run(["git", "rev-parse", f"{commit}:{path}"],
                       capture_output=True, text=True, cwd=REPO)
    return r.stdout.strip() if r.returncode == 0 else None


def main() -> int:
    rows = load_rows()
    unresolved = [rid for rid in WORST_FIRST if rows[rid]["resolution_state"] == "UNRESOLVED"]
    declared = set(WORST_FIRST)
    actual = {rid for rid, r in rows.items() if r["resolution_state"] == "UNRESOLVED"}
    if declared != actual:
        print(f"ERROR: worst-first list != census unresolved set: "
              f"missing={sorted(actual - declared)} extra={sorted(declared - actual)}")
        return 2

    BUNDLES.mkdir(parents=True, exist_ok=True)
    guard: list[dict] = []
    compiled = failed = 0

    for rid in unresolved:
        row = rows[rid]
        out = BUNDLES / f"{rid}_run.json"
        r = subprocess.run([sys.executable, str(VALIDATOR),
                            "--compile-census-row", str(CENSUS),
                            "--census-row-id", rid, "--output", str(out)],
                           capture_output=True, text=True, cwd=REPO)
        if r.returncode == 0:
            compiled += 1
        else:
            failed += 1
            print(f"ERROR: compile {rid}: {r.stdout.strip()} {r.stderr.strip()}")

        ev = row["evidence"]
        pins = PIN_RE.findall(ev)
        pin = pins[-1] if pins else None
        surfaces = []
        for path in PATH_RE.findall(ev):
            path = path.split(":")[0]
            if pin is None:
                surfaces.append({"path": path, "state": "NO_PIN_IN_EVIDENCE"})
                continue
            b_pin, b_head = blob(pin, path), blob("HEAD", path)
            if b_pin is None:
                state = "PIN_READ_FAILED"
            elif b_head is None:
                state = "ABSENT_AT_HEAD"
            elif b_pin == b_head:
                state = "UNMOVED"
            else:
                state = "MOVED"
            surfaces.append({"path": path, "pin": pin, "state": state,
                             "blob_pin": b_pin, "blob_head": b_head})
        moved = [s["path"] for s in surfaces if s["state"] not in ("UNMOVED",)]
        guard.append({"row": rid, "concept": row["concept"],
                      "display_verdict": row["display_verdict"], "owner": row["owner"],
                      "surfaces": surfaces,
                      "guard_state": "ALL_UNMOVED" if not moved else "SURFACE_MOVED",
                      "moved_surfaces": moved})

    report = {
        "artifact": "ATOM_LAYER0_INTEGRATION_VINTAGE_GUARD",
        "seat": "4.0.0_SA_CRO~C",
        "head_at_run": subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                                      text=True, cwd=REPO).stdout.strip(),
        "denominator": {"unresolved_rows": len(unresolved), "compiled": compiled,
                        "compile_failed": failed},
        "rows": guard,
    }
    (SEAT / "vintage_guard_report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8")

    n_moved = sum(1 for g in guard if g["guard_state"] != "ALL_UNMOVED")
    print(f"OK: {compiled}/{len(unresolved)} bundles compiled ({failed} failed); "
          f"vintage guard: {len(guard) - n_moved} ALL_UNMOVED, {n_moved} with moved/unreadable surfaces")
    for g in guard:
        if g["guard_state"] != "ALL_UNMOVED":
            states = {s["path"]: s["state"] for s in g["surfaces"] if s["state"] != "UNMOVED"}
            print(f"  {g['row']} ({g['concept']}): {states}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
