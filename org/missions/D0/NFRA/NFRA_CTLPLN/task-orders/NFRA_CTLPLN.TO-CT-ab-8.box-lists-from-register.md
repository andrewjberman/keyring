# TO NFRA_CTLPLN.TO-CT-ab-8 -- workstream REGISTER round 1 (cell CT-ab-8): the two hand-typed box lists in the tools come from the device register (FWD-2)

<to_id>NFRA_CTLPLN.TO-CT-ab-8</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~81</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>REGISTER</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ab-8` (`decompositions/NFRA_CTLPLN_DECOMP.round12.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-2: a box is added once, in one place (`org/devices/DEVICES.json`, read by `lib/devices.py`), and every tool knows its name and role. MEASURED: `.tools/to-pipeline-gate.py:93` reads exactly `FABRIC_ENUM = ("laptop", "site-z", "dell1", "dell2")` (the gate's decisions already go through `_fabric_values()` at about :103-111, which calls `lib/devices.py placement_values()`, so the literal is a stale second copy); `.tools/box-status-report-check.py:33` reads `BOXES = {"laptop", "sitez", "dell1", "dell2"}`. `lib/devices.py` offers `names()` (about :49, the box names), `placement_values()` (about :70, a tuple with `site-z` hyphenated), `load()` (fails closed). `.tools/tests/test_no_hand_listed_boxes.py` censuses hand-listed boxes (real tree: `hand_listed=9`); `.tools/tests/test_fabric_enum_dell.py` and `test_fabric_readers_dell.py` pass today.

### BUILD

1. `.tools/to-pipeline-gate.py`: `FABRIC_ENUM` becomes `tuple(<lib.devices placement_values()>)`, imported the way `_fabric_values()` already imports it (fail closed if the register cannot be read, exactly as `_fabric_values()` does). Every reader of `FABRIC_ENUM` (including the AST read by `.tools/missions-tree-check` or others that print "read by AST" -- search for `FABRIC_ENUM` across `.tools/` and `lib/` with the Grep tool and list every hit) must still work; where a reader parses the literal by AST, make it call the derived value instead, and say so.
2. `.tools/box-status-report-check.py`: `BOXES` becomes `set(<lib.devices names()>)`.
3. A NEW test `.tools/tests/test_box_lists_from_register.py` (standard library): asserts that neither file contains a literal tuple/set/list of box-name strings, that `FABRIC_ENUM` equals `placement_values()` and `BOXES` equals `set(names())`, and prints one final line `BOX-LISTS-FROM-REGISTER gate=<derived|literal> status_report=<derived|literal> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. No aws, no push. `.tools/safe-commit.sh` for every commit (note: your own edit to `to-pipeline-gate.py` runs in that gate at your commit; if it refuses its own change, STOP and file a BLOCKING row). Do NOT commit the `portal` gitlink. ASCII only; Python 3.11; ruff clean. CLAUDE.md and org/XXX.md are LOCKED. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W81-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTab8-AC1" cell_refs="CT-ab-8"><invocation>python .tools/tests/test_box_lists_from_register.py</invocation><expect>gate=derived status_report=derived ok=True</expect></criterion>
`CTab8-AC1` -- both lists derive from the register.

<criterion id="CTab8-AC2" cell_refs="CT-ab-8"><invocation>python .tools/tests/test_fabric_enum_dell.py</invocation><expect>ok=True</expect></criterion>
`CTab8-AC2` -- the gate still admits and refuses as before (a control that PASSES at the base).

<criterion id="CTab8-AC3" cell_refs="CT-ab-8"><invocation>python .tools/tests/test_no_hand_listed_boxes.py</invocation><expect>ok=True</expect></criterion>
`CTab8-AC3` -- the hand-listed census test still passes; report its real-tree `hand_listed=` count (base 9; expected 7).
</proof_of_spec>

<expected_criteria>CTab8-AC1,CTab8-AC2,CTab8-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~81/NFRA_CTLPLN.TO-CT-ab-8.box-lists-from-register.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTab8-AC1,CTab8-AC2,CTab8-AC3`, flip `<status>` to `complete` only when all pass and the instance is VALID (if refused as outside your grant, leave it `pending` and say so).

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round12.md</decomp_doc>
<owned_cells>CT-ab-8</owned_cells>
</decomp_ref>

<paths>
.tools/to-pipeline-gate.py
.tools/box-status-report-check.py
.tools/tests/test_box_lists_from_register.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a register read that fails open and admits any fabric (fail closed, AC2's refusal arm); an AST reader of the literal broken silently (BUILD 1 lists every reader); BLIND: hand-listed boxes in PowerShell schedules (box-sync-schedule.ps1, carried).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CVO re-grade 2026-10-13 FWD-2 (E5); fact sheet section C.
