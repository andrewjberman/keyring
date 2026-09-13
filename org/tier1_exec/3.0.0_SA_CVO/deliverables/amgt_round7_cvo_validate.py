"""Validate new CVO rows, exact original coverage and monotone existing clocks."""

import collections
import importlib.util
import json
import re
import subprocess
from amgt_round7_cvo_supplement import ROOT, HOME, PROJECT, rows

CHANNEL = PROJECT + "/surprise-channel/"
NEW = [
    CHANNEL + "adjudications/ADJUDICATION_v7.md",
    CHANNEL + "remediations/REMEDIATION_v7.md",
]
ADVANCES = [
    CHANNEL + "remediations/REMEDIATION_v5.md",
    CHANNEL + "remediations/REMEDIATION_v6.md",
]
spec = importlib.util.spec_from_file_location(
    "gate", ROOT / ".tools/surprise-row-gate.py"
)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)
issues = {}
for path in NEW:
    kind = gate._kind(path)
    schema = gate._schema(str(ROOT), kind)
    issues[path] = [
        v for row in rows(ROOT / path) for v in gate._check_row(row, kind, schema)
    ]
paths = set(NEW)
for pattern in (
    gate.INVESTIGATION_PATTERNS + gate.ADJUDICATION_PATTERNS + gate.REMEDIATION_PATTERNS
):
    found, note = gate._index_paths(str(ROOT), [pattern % "AMGT_RESAPP"])
    assert found is not None, note
    paths.update(found)
files = []
rem_ids = []
all_ids = []
for path in sorted(paths):
    records = rows(ROOT / path)
    if gate._kind(path) == "REMEDIATION":
        rem_ids.extend(r["id"] for r in records)
    else:
        files.append((path, records))
        all_ids.extend(r["id"] for r in records)
latest, unknown = gate._resolve_latest(files, rem_ids)
clock_changes = {}
for path in ADVANCES:
    old = subprocess.check_output(["git", "show", "HEAD:" + path], cwd=ROOT).decode(
        "utf-8"
    )
    rr = []
    for block in re.findall(r"```json\s*(.*?)```", old, re.S):
        value = json.loads(block)
        rr.extend(value if isinstance(value, list) else [value])
    before = {r["id"]: r for r in rr}
    after = {r["id"]: r for r in rows(ROOT / path)}
    assert before.keys() == after.keys()
    clock_changes[path] = {
        rid: gate._monotone_advance(before[rid], after[rid])
        for rid in before
        if before[rid] != after[rid]
    }
orders = gate._open_tos_for_project(str(ROOT), "AMGT_RESAPP")
intake = json.loads(
    (HOME / "AMGT_RESAPP_ROUND7_CVO_INTAKE_20260912_Z.json").read_text()
)
pending_before = {r["id"] for r in intake["pending"]}
late = json.loads((HOME / "AMGT_RESAPP_ROUND7_CVO_LATE_20260912_Z.json").read_text())
pending_before.update(late["rows"])
new = rows(ROOT / NEW[0])
covered = collections.Counter(
    rid for r in new for rid in r.get("adjudicates", []) if rid in pending_before
)
out = {
    "utc": __import__("datetime")
    .datetime.now(__import__("datetime").timezone.utc)
    .isoformat(),
    "head": subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip(),
    "new_rows": {p: len(rows(ROOT / p)) for p in NEW},
    "row_violations": issues,
    "originals": len(latest),
    "pending": [rid for rid, disp in latest.items() if disp == "UNDER_INVESTIGATION"],
    "unknown_targets": unknown,
    "duplicate_remediation_ids": [
        rid for rid, n in collections.Counter(rem_ids).items() if n > 1
    ],
    "duplicate_investigation_or_adjudication_ids": [
        rid for rid, n in collections.Counter(all_ids).items() if n > 1
    ],
    "clock_changes": clock_changes,
    "orders": orders,
    "pending_intake_covered_once": set(covered) == pending_before
    and all(n == 1 for n in covered.values()),
    "judgment_grades": [g for r in new for g in r.get("grades", [])],
    "limits": "Prospective current working-file census; safe-commit repeats checks against its index. No overrides; current source pin and offline/composed evidence are in the intake and audits.",
}
(HOME / "AMGT_RESAPP_ROUND7_CVO_VALIDATION_20260912_Z.json").write_text(
    json.dumps(out, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({k: v for k, v in out.items() if k != "judgment_grades"}))
assert not any(issues.values()) and not out["pending"] and not unknown
assert (
    not out["duplicate_remediation_ids"]
    and not out["duplicate_investigation_or_adjudication_ids"]
)
assert out["pending_intake_covered_once"] and all(
    ok for changes in clock_changes.values() for ok in changes.values()
)
assert sum(len(c) for c in clock_changes.values()) == 5
assert len(latest) == 94 and list(orders) == [[], 43, ""]
