# TO MDPF_DEMQUE.TO-DQ-t37 -- round 9 DQ-t-37: the standing extension refuses a --today after the local date
<to_id>MDPF_DEMQUE.TO-DQ-t37</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~29</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>EXTGUARD2</workstream>
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-11 ~17:3xZ (row MDPF_DEMQUE-D1-W29-S1, BLOCKING; issuer defect):** the face said `test_demque_extend_frontier.py` stays unedited and monkeypatches `date.today`; it does neither: two of its tests pass `today="2026-10-12"`, a date after the real local date, which the new refusal rejects, and they would pass only once the calendar passes 2026-10-12. GRANTED: `data/mdpf/scripts/demque/test_demque_extend_frontier.py` for ONE change: pin the local date inside `extend_frontier` for those tests with the same date-subclass monkeypatch your new file uses (a fixed local date on or after the latest date any of its tests passes), so they no longer depend on the real clock. No assertion about the plan, the file or the pacer changes. All three extension test files must then pass. No criterion change.
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-37` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 2) |
**outcome_ref:** C-PRICES | **depends_on:** DQ-t-36 (merged @df9aaa34cc)

---

## WORKER FACE

### THE CELL

`DQ-t-37` (issuer, found while writing the never-widen half for DQ-t-31: an override must be covered by the sign-off or not land). With DQ-t-36 a
manual `--today` can no longer SHORTEN a served file, but a `--today` AFTER the real local date still plans and applies: the window ends in the
future, `price_store.write` records a lock `valid_to` that has not happened, and the next normal run is then refused by DQ-t-36's own guard
(its frontier is before the store's latest `valid_to`) until the calendar catches up: the daily run fails loudly for days.

**Build** (in `data/mdpf/scripts/demque/extend_frontier.py`, and a NEW test file):
1. `plan()` raises `SystemExit` when `today` is later than `date.today()` (the local date), with a message that names both dates ("--today
   2026-10-12 is after the local date 2026-10-11: the extension plans no future day"). `apply()` calls `plan()` first, so it writes no
   request file and resets no pacer entry in that case. `today=None` and `today` equal to the local date plan as before; an earlier
   `--today` still reaches DQ-t-36's guard. The `--plan` JSON keys are unchanged.
2. NEW `test_demque_extend_future.py` (pytest; a LOCAL store root under `tmp_path`, a pacer JSON and a queue folder in `tmp_path`, no network;
   monkeypatch `date.today` in the module the way `test_demque_extend_frontier.py` does for its dates) with exactly these names:
   `test_plan_refuses_a_today_after_the_local_date`,
   `test_apply_refuses_a_future_today_and_writes_nothing` (the queue folder and the pacer JSON are byte-identical afterwards) and
   `test_today_equal_to_the_local_date_still_plans`. `test_demque_extend_frontier.py` and `test_demque_extend_guard.py` keep passing UNEDITED; if
   one passes a `today` later than the real date, that is a surprise row, not an edit (they should pin the local date by monkeypatch).

### ACCEPTANCE

<criterion id="DQ9-t37-AC1" cell_refs="DQ-t-37"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t37_tests.py</invocation><expect>FUT-OK</expect></criterion>
<criterion id="DQ9-t37-AC2" cell_refs="DQ-t-37"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t37_real.py</invocation><expect>FUT-REAL-OK</expect></criterion>
`DQ9-t37-AC1` -- the three named tests. `DQ9-t37-AC2` -- on the REAL served store (S3 read only): `--plan --today <tomorrow>` exits non-zero, prints no plan
and names the local date; `--plan` with no `--today` and with `--today <the local date>` print the same frontier.

<expected_criteria>DQ9-t37-AC1,DQ9-t37-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `FUT-BAD no file ...`; `FUT-REAL-BAD arms=tomorrow_refused,names_local_date`.
If `test_demque_extend_frontier.py` asserts a `plan(... today=<a date later than the real local date>)`, pin the local date in YOUR new tests
only; do not edit that file.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Read-only against S3; no write to the served store, the real pacer or queue, no AWS write, no Yahoo or Bloomberg call, no deploy.**
  `--apply` is never run against the real home.
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W29-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/extend_frontier.py
data/mdpf/scripts/demque/test_demque_extend_future.py
data/mdpf/scripts/demque/test_demque_extend_frontier.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-37`.
<owned_cells>DQ-t-37</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t37-AC1, DQ9-t37-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~29/MDPF_DEMQUE.TO-DQ-t37.extension-refuses-a-future-today.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t37-AC1,DQ9-t37-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the refusal message verbatim, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write; the S3 read is the seat's existing read.
comp-adversary: DECLARED-NOT-APPLICABLE a narrowing guard on a planning tool.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order.
</preflight>

Source: issuer, never-widen half for TO-DQ-t31 (the override-covered-or-not-landed rule, CLAUDE.md section 5); TO-DQ-t36; decomposition round 9.
