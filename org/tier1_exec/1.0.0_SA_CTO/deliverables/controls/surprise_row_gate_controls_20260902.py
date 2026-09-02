"""Red-first controls for surprise-row-gate.py (CVO~A @0d272d257c release conditions 1-3).

Run against the CURRENT gate first (expect wrongly-PASSES = the defect is present), then
against the rewritten gate (expect REFUSED). Each control is a (name, kind, row, expect)
tuple or a mutation scenario. Prints one line per control and a DEFECTS total.

Placement note: this lives under the CTO deliverables, NOT .tools/tests/, because the
TOOL_BATTERIES lane (Andrew-direct 2026-09-02) permits only 0.8.0_AE_CloudComp there. The
lane refusing its own author is the lane working. Graduation into the batteries is that
seat's to accept.
"""
import copy
import importlib.util
import json
import os
import sys

sys.path.insert(0, os.path.abspath(".tools"))
_spec = importlib.util.spec_from_file_location("gate", ".tools/surprise-row-gate.py")
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)
ROOT = os.path.abspath(".")


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
    """A SCOPE_CHANGE remediation row with the given extra fields."""
    return mut(GOOD_REM, route="SCOPE_CHANGE", loop_target=2, **kw)


CONTROLS = [
    # --- RC1: identity + nested Draft-07 ---
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
    # --- RC3: scope-change payload ---
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


def _line(ok, got, expect, name):
    print("  %-7s %-6s->%-6s  %s" % ("OK" if ok else "DEFECT", got, expect, name))


def run_row_controls():
    fails = 0
    for name, kind, row, expect in CONTROLS:
        violations = gate._check_row(row, kind, schema(kind))
        got = "PASS" if not violations else "REFUSE"
        ok = got == expect
        fails += int(not ok)
        _line(ok, got, expect, name)
        if not ok and violations:
            print("           first: %s" % violations[0][:110])
    return fails


def run_mutation_controls():
    """RC2: existing-row mutation / deletion via the gate's staged-vs-HEAD seam."""
    if not hasattr(gate, "_mutation_violations"):
        print("  DEFECT  gate has no _mutation_violations -- existing-row edits are UNCHECKED (P0-2 present)")
        return 3
    base = [GOOD_INV, mut(GOOD_INV, id="ETFS_GUARDRAIL-Z-S998")]
    head_txt = "```json\n" + json.dumps(base) + "\n```"
    same = "```json\n" + json.dumps(base) + "\n```"
    mutated = "```json\n" + json.dumps([mut(base[0], one_line="EDITED IN PLACE"), base[1]]) + "\n```"
    deleted = "```json\n" + json.dumps([base[0]]) + "\n```"
    scenarios = [
        ("RC2 unchanged existing rows (must PASS)", same, 0),
        ("RC2 existing row MUTATED in place", mutated, 1),
        ("RC2 existing row DELETED", deleted, 1),
    ]
    fails = 0
    for name, staged, expect in scenarios:
        violations = gate._mutation_violations("x.md", head_txt, staged)
        got = 1 if violations else 0
        ok = got == expect
        fails += int(not ok)
        _line(ok, "REFUSE" if got else "PASS", "REFUSE" if expect else "PASS", name)
    return fails


if __name__ == "__main__":
    print("== ROW CONTROLS (RC1 + RC3) ==")
    row_fails = run_row_controls()
    print("== MUTATION CONTROLS (RC2) ==")
    mut_fails = run_mutation_controls()
    print("DEFECTS: %d row + %d mutation = %d" % (row_fails, mut_fails, row_fails + mut_fails))
    sys.exit(1 if row_fails + mut_fails else 0)
