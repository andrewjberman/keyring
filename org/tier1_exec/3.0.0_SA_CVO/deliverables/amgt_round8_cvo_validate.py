"""Validate complete original coverage, seven grades, and eight monotone advances."""

import collections
import datetime
import importlib.util
import json
import subprocess
from amgt_round8_cvo_intake import ROOT, HOME, PROJECT, records

CHANNEL = PROJECT + "/surprise-channel/"
NEW = [
    CHANNEL + "adjudications/ADJUDICATION_v8.md",
    CHANNEL + "remediations/REMEDIATION_v8.md",
]
ADVANCES = [
    CHANNEL + "remediations/REMEDIATION_v5.md",
    CHANNEL + "remediations/REMEDIATION_v7.md",
]
spec = importlib.util.spec_from_file_location(
    "gate", ROOT / ".tools/surprise-row-gate.py"
)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def rows(path):
    return records((ROOT / path).read_text(encoding="utf-8"))


issues = {
    p: [
        v
        for r in rows(p)
        for v in gate._check_row(
            r, gate._kind(p), gate._schema(str(ROOT), gate._kind(p))
        )
    ]
    for p in NEW
}
paths = set(NEW)
for pattern in (
    gate.INVESTIGATION_PATTERNS + gate.ADJUDICATION_PATTERNS + gate.REMEDIATION_PATTERNS
):
    found, note = gate._index_paths(str(ROOT), [pattern % "AMGT_RESAPP"])
    assert found is not None, note
    paths.update(found)
files, remids, ids = [], [], []
for p in sorted(paths):
    rr = rows(p)
    if gate._kind(p) == "REMEDIATION":
        remids.extend(r["id"] for r in rr)
    else:
        files.append((p, rr))
        ids.extend(r["id"] for r in rr)
latest, unknown = gate._resolve_latest(files, remids)
clock_changes = {}
for p in ADVANCES:
    before = {
        r["id"]: r
        for r in records(
            subprocess.check_output(["git", "show", "HEAD:" + p], cwd=ROOT).decode(
                "utf-8"
            )
        )
    }
    after = {r["id"]: r for r in rows(p)}
    assert before.keys() == after.keys()
    clock_changes[p] = {
        rid: gate._monotone_advance(before[rid], after[rid])
        for rid in before
        if before[rid] != after[rid]
    }
compile = json.loads(
    (HOME / "AMGT_RESAPP_ROUND8_CVO_COMPILE_20260913_Z.json").read_text()
)
reviewed = set(compile["reviewed_originals"])
new = rows(NEW[0])
covered = collections.Counter(
    rid for r in new for rid in r.get("adjudicates", []) if rid in reviewed
)
intake = json.loads(
    (HOME / "AMGT_RESAPP_ROUND8_CVO_INTAKE_20260913_Z.json").read_text()
)
types = json.loads((HOME / "AMGT_RESAPP_ROUND8_CVO_TYPES_20260913_Z.json").read_text())
portal = json.loads(
    (HOME / "AMGT_RESAPP_ROUND8_CVO_PORTAL_20260913_Z.json").read_text()
)
grades = [g for r in new for g in r.get("grades", [])]
out = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "head": subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip(),
    "new_rows": {p: len(rows(p)) for p in NEW},
    "row_violations": issues,
    "originals": len(latest),
    "pending": [rid for rid, disp in latest.items() if disp == "UNDER_INVESTIGATION"],
    "unknown_targets": unknown,
    "duplicate_remedy_ids": [
        rid for rid, n in collections.Counter(remids).items() if n > 1
    ],
    "duplicate_surfacing_ids": [
        rid for rid, n in collections.Counter(ids).items() if n > 1
    ],
    "clock_changes": clock_changes,
    "orders": {
        p: gate._open_tos_for_project(str(ROOT), p)
        for p in ["AMGT_RESAPP", "POSN_ASTTAX", "ZZZZ_NOSUCH"]
    },
    "reviewed_once": set(covered) == reviewed and all(n == 1 for n in covered.values()),
    "proofs_valid": len(intake["proof_checks"]) == 44
    and all(c["rc"] == 0 for c in intake["proof_checks"].values()),
    "grade_count": len(grades),
    "grade_criteria": [g["criterion"] for g in grades],
    "portal_assertions": portal["tests"],
    "typecheck": {
        "files": len(types["baseline"]["files"]),
        "rc": types["baseline"]["rc"],
        "mutant_rc": types["mutant"]["rc"],
        "restored": types["restored_byte_identical"],
    },
    "limits": "Prospective working-file validation. Safe-commit repeats its index and corpus checks. No originals, task orders or proof instances changed by this review.",
}
(HOME / "AMGT_RESAPP_ROUND8_CVO_VALIDATION_20260913_Z.json").write_text(
    json.dumps(out, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(out))
assert not any(issues.values()) and not out["pending"] and not unknown
assert not out["duplicate_remedy_ids"] and not out["duplicate_surfacing_ids"]
assert out["reviewed_once"] and out["proofs_valid"] and len(grades) == 7
assert (
    all(all(v.values()) for v in clock_changes.values())
    and sum(len(v) for v in clock_changes.values()) == 8
)
assert len(latest) == compile["originals"] and list(out["orders"]["AMGT_RESAPP"]) == [
    [],
    46,
    "",
]
assert (
    all(portal["tests"].values())
    and types["baseline"]["rc"] == 0
    and len(types["baseline"]["files"]) > 1000
    and types["mutant"]["rc"] != 0
    and types["restored_byte_identical"]
)
