"""Red-first controls for surprise-row-gate.py (CVO~A @0d272d257c RC1-3; re-grade @0dbf12ebb3).

Run against the OLD gate first (GATE_PATH=<a copy of HEAD's gate>; expect DEFECTS = the holes
are present), then against the worktree gate (expect 0). Prints one line per control and a
DEFECTS total. Exit 1 on any defect.

Placement: CTO deliverables, NOT .tools/tests/ -- the TOOL_BATTERIES lane (Andrew-direct
2026-09-02) permits only 0.8.0_AE_CloudComp there. Graduation is that seat's to accept.
"""
import copy
import importlib.util
import json
import os
import subprocess
import sys

GATE_PATH = os.environ.get("GATE_PATH", ".tools/surprise-row-gate.py")
sys.path.insert(0, os.path.abspath(".tools"))
_spec = importlib.util.spec_from_file_location("gate", GATE_PATH)
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)
ROOT = os.path.abspath(".")
SCHEMA_REL = "org/surprise_channel/schemas/investigation_item.schema.json"


def _line(ok, got, expect, name):
    print("  %-7s %-6s->%-6s  %s" % ("OK" if ok else "DEFECT", got, expect, name))


def schema(kind):
    return gate._schema(ROOT, kind)


GOOD_INV = {
    "id": "ETFS_GUARDRAIL-Z-S999",
    "project": "ETFS_GUARDRAIL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~A",
    "surfaced_at": "2026-09-02T17:00Z",
    "one_line": "a control row that is fully legal",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {"status": "GROUNDED", "evidence": ["file:line @ abc123"]},
    "disposition": "GRADUATED",
    "spec_asserts": "the TO said X would be present",
    "world_is": "X was absent at the served key",
}
GOOD_REM = {
    "id": "ETFS_GUARDRAIL-Z-S999",
    "project": "ETFS_GUARDRAIL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the grounded attribution carried verbatim",
    "evidence": ["file:line @ abc123"],
    "remedy": "do the thing",
    "owner": "0.7.0_AE_CloudOps",
    "round": "v1",
    "remediation": {"state": "OPEN", "owner": "0.7.0_AE_CloudOps", "round": "v1"},
    "route": "SPEC_ERROR",
    "loop_target": 6,
}


def mut(base, **kw):
    r = copy.deepcopy(base)
    r.update(kw)
    return r


def drop(base, *keys):
    r = copy.deepcopy(base)
    for k in keys:
        r.pop(k, None)
    return r


def _sc(**kw):
    return mut(GOOD_REM, route="SCOPE_CHANGE", loop_target=2, **kw)


ROW_CONTROLS = [
    ("RC1 good investigation row (positive control, must PASS)", "INVESTIGATION", GOOD_INV, "PASS"),
    ("RC1 absent project+fabric", "INVESTIGATION", drop(GOOD_INV, "project", "fabric"), "REFUSE"),
    ("RC1 wrong project (id says ETFS_GUARDRAIL)", "INVESTIGATION",
     mut(GOOD_INV, project="WRONG_PROJECT"), "REFUSE"),
    ("RC1 wrong fabric (id has -Z-, fabric=laptop)", "INVESTIGATION",
     mut(GOOD_INV, fabric="laptop"), "REFUSE"),
    ("RC1 invalid surfaced_at (21:2xZ)", "INVESTIGATION",
     mut(GOOD_INV, surfaced_at="2026-09-02T21:2xZ"), "REFUSE"),
    ("RC1 GRADUATED without GROUNDED evidence", "INVESTIGATION",
     mut(GOOD_INV, grounding={"status": "INFERRED", "evidence": []}), "REFUSE"),
    ("RC1 nested enum: grounding.status=BOGUS", "INVESTIGATION",
     mut(GOOD_INV, grounding={"status": "BOGUS", "evidence": ["x @ y"]}), "REFUSE"),
    ("RC3 good SPEC_ERROR remediation (positive control, must PASS)", "REMEDIATION", GOOD_REM, "PASS"),
    ("RC3 FWD-NONE sentinel", "REMEDIATION", _sc(outcome_ref="FWD-NONE"), "REFUSE"),
    ("RC3 SCOPE_CHANGE with no scope_change_kind", "REMEDIATION", _sc(outcome_ref="FWD-3"), "REFUSE"),
    ("RC3 CONTRADICTS_NAMED_OUTCOME + real FWD-n (must PASS)", "REMEDIATION",
     _sc(scope_change_kind="CONTRADICTS_NAMED_OUTCOME", outcome_ref="FWD-3"), "PASS"),
    ("RC3 CONTRADICTS_NAMED_OUTCOME + null ref", "REMEDIATION",
     _sc(scope_change_kind="CONTRADICTS_NAMED_OUTCOME", outcome_ref=None), "REFUSE"),
    ("RC3 REQUIRES_UNNAMED_OUTCOME + required-null + proposed (must PASS)", "REMEDIATION",
     _sc(scope_change_kind="REQUIRES_UNNAMED_OUTCOME", outcome_ref=None,
         proposed_outcome="advisors can see X without opening Y"), "PASS"),
    ("RC3 REQUIRES_UNNAMED_OUTCOME with outcome_ref key ABSENT (not null)", "REMEDIATION",
     drop(_sc(scope_change_kind="REQUIRES_UNNAMED_OUTCOME", proposed_outcome="advisors can see X"),
          "outcome_ref"), "REFUSE"),
    ("RC3 REQUIRES_UNNAMED_OUTCOME with no proposed_outcome", "REMEDIATION",
     _sc(scope_change_kind="REQUIRES_UNNAMED_OUTCOME", outcome_ref=None), "REFUSE"),
]


def run_row_controls():
    fails = 0
    for name, kind, row, expect in ROW_CONTROLS:
        violations = gate._check_row(row, kind, schema(kind))
        got = "PASS" if not violations else "REFUSE"
        ok = got == expect
        fails += int(not ok)
        _line(ok, got, expect, name)
        if not ok and violations:
            print("           first: %s" % violations[0][:110])
    return fails


def _fence(rows):
    return "```json\n" + json.dumps(rows) + "\n```"


def run_mutation_controls():
    """RC2: mutation / deletion / DUPLICATE-ID via the gate's staged-vs-HEAD seam."""
    if not hasattr(gate, "_mutation_violations"):
        print("  DEFECT  gate has no _mutation_violations -- existing-row edits are UNCHECKED (P0-2)")
        return 4
    a, b = GOOD_INV, mut(GOOD_INV, id="ETFS_GUARDRAIL-Z-S998")
    head = _fence([a, b])
    contradictory_dup = mut(a, one_line="A CONTRADICTORY REWRITE OF S999")
    scenarios = [
        ("RC2 unchanged existing rows (must PASS)", _fence([a, b]), 0),
        ("RC2 existing row MUTATED in place", _fence([mut(a, one_line="EDITED"), b]), 1),
        ("RC2 existing row DELETED", _fence([a]), 1),
        ("RC2 DUPLICATE id: contradictory copy PREPENDED, original unchanged after it (dict collapse)",
         _fence([contradictory_dup, a, b]), 1),
    ]
    fails = 0
    for name, staged, expect in scenarios:
        violations = gate._mutation_violations("x.md", head, staged)
        got = 1 if violations else 0
        ok = got == expect
        fails += int(not ok)
        _line(ok, "REFUSE" if got else "PASS", "REFUSE" if expect else "PASS", name)
    return fails


def run_parser_controls():
    """RC1 second pass: raw .json bodies, fenced non-objects, zero-row targets."""
    fails = 0
    cases = [
        ("RC1 parser: raw .json INVALID body counts as malformed", "{not json", True, "REFUSE"),
        ("RC1 parser: raw .json valid object (must PASS)", json.dumps(GOOD_INV), True, "PASS"),
        ("RC1 parser: raw .json list with a STRING item", json.dumps([GOOD_INV, "stray"]), True, "REFUSE"),
        ("RC1 parser: fenced SCALAR block", "```json\n42\n```", False, "REFUSE"),
        ("RC1 parser: fenced list of non-objects", "```json\n[1, 2]\n```", False, "REFUSE"),
        ("RC1 parser: fenced valid object (must PASS)", _fence([GOOD_INV]), False, "PASS"),
    ]
    for name, text, raw, expect in cases:
        try:
            rows, bad = gate._rows(text, raw)
        except TypeError:
            _line(False, "NOAPI", expect, name + "  (gate._rows has no raw_json parameter)")
            fails += 1
            continue
        got = "REFUSE" if (bad or not rows) else "PASS"
        ok = got == expect
        fails += int(not ok)
        _line(ok, got, expect, name)
    return fails


def run_blob_controls():
    """RC2 second pass: HEAD absence vs HEAD read FAILURE must be different states."""
    fails = 0
    cases = [
        ("blob: real path at HEAD", "HEAD", SCHEMA_REL, "OK"),
        ("blob: MISSING path at HEAD -> ABSENT", "HEAD", "org/surprise_channel/NOPE/INVESTIGATION_v1.md", "ABSENT"),
        ("blob: BOGUS ref -> ERROR, not ABSENT", "not-a-ref-zz", SCHEMA_REL, "ERROR"),
        ("blob: staged index copy of the schema", "", SCHEMA_REL, "OK"),
    ]
    for name, ref, rel, expect in cases:
        res = gate._blob(ROOT, ref, rel)
        if not (isinstance(res, tuple) and len(res) == 2):
            _line(False, "NONE" if res is None else "TEXT", expect, name + "  (single-value return: absence == failure)")
            fails += 1
            continue
        got = res[0]
        ok = got == expect
        fails += int(not ok)
        _line(ok, got, expect, name)
    # staged-schema: _schema must return the INDEX bytes, not the worktree file.
    try:
        idx = json.loads(subprocess.run(["git", "show", ":" + SCHEMA_REL], capture_output=True, text=True).stdout)
        via_gate = gate._schema(ROOT, "INVESTIGATION")
        ok = via_gate == idx
        _line(ok, "INDEX" if ok else "OTHER", "INDEX", "schema: _schema() reads the STAGED INDEX copy")
        fails += int(not ok)
    except Exception as exc:  # noqa: BLE001
        _line(False, "ERR", "INDEX", "schema: _schema() raised %s" % exc)
        fails += 1
    return fails


def run_index_diff_controls():
    """RC2 watcher half: an id/hash index must expose a SAME-COUNT rewrite that a count cannot."""
    fails = 0
    before = {("f.md", "P-S1"): "aaaa", ("f.md", "P-S2"): "bbbb"}
    same_count_rewrite = {("f.md", "P-S1"): "aaaa", ("f.md", "P-S2"): "CHANGED"}
    delete_and_add = {("f.md", "P-S1"): "aaaa", ("f.md", "P-S3"): "cccc"}
    for name, after, expect in [
        ("watcher: unchanged index (must PASS)", dict(before), 0),
        ("watcher: same-count REWRITE of S2 is visible", same_count_rewrite, 1),
        ("watcher: same-count DELETE S2 + ADD S3 is visible", delete_and_add, 1),
    ]:
        emitted = sum(1 for k, h in before.items() if k not in after or after[k] != h)
        got = 1 if emitted else 0
        ok = got == expect
        fails += int(not ok)
        _line(ok, "WARN" if got else "QUIET", "WARN" if expect else "QUIET", name)
    # and the real tool produces the index in the agreed shape
    r = subprocess.run([sys.executable, ".tools/surprise-corpus-validate.py", "--index"], capture_output=True, text=True)
    lines = [ln for ln in r.stdout.splitlines() if ln.count("\t") == 2]
    ok = r.returncode == 0 and len(lines) >= 190
    _line(ok, "%d rows" % len(lines), ">=190", "watcher: --index emits path/id/hash for the corpus")
    fails += int(not ok)
    return fails


if __name__ == "__main__":
    print("== gate under test: %s ==" % GATE_PATH)
    print("== ROW CONTROLS (RC1 + RC3) ==")
    f1 = run_row_controls()
    print("== MUTATION CONTROLS (RC2) ==")
    f2 = run_mutation_controls()
    print("== PARSER CONTROLS (RC1 second pass) ==")
    f3 = run_parser_controls()
    print("== BLOB / STAGED-SCHEMA CONTROLS (RC1+RC2 second pass) ==")
    f4 = run_blob_controls()
    print("== WATCHER INDEX CONTROLS (RC2 second pass) ==")
    f5 = run_index_diff_controls()
    total = f1 + f2 + f3 + f4 + f5
    print("DEFECTS: %d row + %d mutation + %d parser + %d blob + %d watcher = %d" % (f1, f2, f3, f4, f5, total))
    sys.exit(1 if total else 0)
