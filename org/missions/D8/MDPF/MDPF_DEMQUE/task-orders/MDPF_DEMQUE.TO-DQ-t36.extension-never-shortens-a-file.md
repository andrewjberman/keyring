# TO MDPF_DEMQUE.TO-DQ-t36 -- round 9 DQ-t-36: the standing extension refuses a frontier that would shorten a served file
<to_id>MDPF_DEMQUE.TO-DQ-t36</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~28</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>EXTGUARD</workstream>
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-11 ~16:4xZ (row MDPF_DEMQUE-D1-W28-S1, BLOCKING; issuer defect in the AC2 check and this order's base arm; no `<paths>` change):** the order named `--today 2026-06-30` as a frontier "before every file's end". The store's latest `valid_to` is 2026-06-23, so 2026-06-30 is AFTER it and a plan for it is correct. The arm is `--today 2026-06-15` (before every file's end, 2026-06-22/23). Your guard is right and stays as built; only the day in the check and in this text changed.
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-36` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amended) |
**outcome_ref:** C-PRICES | **depends_on:** DQ-t-31 (merged @1961d4ee7a)

---

## WORKER FACE

### THE CELL

`DQ-t-36` (issuer defect in DQ-t-31, found by the issuer reading the merged bytes before signing its never-widen half). `extend_frontier.py`
(`data/mdpf/scripts/demque/`) takes the window end from `expected_last_trading_day(--today)` and `price_store.write` clips each file to the lock's
`[valid_from, valid_to]`. A manual `--today` earlier than a file's current end therefore plans a window that SHORTENS the served file, and `--apply`
would write that request and reset the pacer. The measured arm at the base: `extend_frontier.py --plan --today 2026-06-15` exits 0 and prints a plan
ending 2026-06-15, while every file ends 2026-06-22 or 2026-06-23.

**Build** (in `extend_frontier.py`, and a NEW test file):
1. `plan()` computes `latest_end = max(valid_to)` over the rows `price_store.index` returns (ISO dates). When `frontier < latest_end` it raises
   `SystemExit` with a message that names the frontier and `latest_end` ("frontier 2026-06-15 is before the store's latest valid_to 2026-06-23: the
   extension never shortens a served file"). `apply()` calls `plan()` first, so it writes no request file and resets no pacer entry in that case.
   A frontier equal to or after `latest_end` plans as before. No other behavior changes; the `--plan` JSON keys are unchanged.
2. NEW `test_demque_extend_guard.py` (pytest; a LOCAL store root under `tmp_path`, a pacer JSON and a queue folder in `tmp_path`, no network)
   with exactly these names: `test_plan_refuses_a_frontier_before_the_latest_valid_to_in_the_store`,
   `test_apply_writes_nothing_and_resets_nothing_when_the_plan_would_shorten_a_file` (the queue folder and the pacer JSON are byte-identical
   afterwards), `test_a_frontier_on_or_after_the_latest_valid_to_still_plans` (the day itself and the day after).
   `test_demque_extend_frontier.py` keeps passing UNEDITED (its stores end before its dates).

### ACCEPTANCE

<criterion id="DQ9-t36-AC1" cell_refs="DQ-t-36"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t36_tests.py</invocation><expect>GUARD-OK</expect></criterion>
<criterion id="DQ9-t36-AC2" cell_refs="DQ-t-36"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t36_real.py</invocation><expect>GUARD-REAL-OK</expect></criterion>
`DQ9-t36-AC1` -- the three named tests. `DQ9-t36-AC2` -- on the REAL served store (S3 read only): `--plan --today 2026-06-15` exits non-zero with no
JSON plan and names the store's latest `valid_to`; `--plan --today 2026-10-12` still prints a plan ending 2026-10-12 with 141 symbols.

<expected_criteria>DQ9-t36-AC1,DQ9-t36-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `GUARD-BAD no file ...`; `GUARD-REAL-BAD arms=early_refused,early_names_valid_to`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Read-only against S3; no write to the served store, the real pacer or queue, no AWS write, no Yahoo or Bloomberg call, no deploy.**
  `--apply` is never run against the real home.
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W28-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/extend_frontier.py
data/mdpf/scripts/demque/test_demque_extend_guard.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-36`.
<owned_cells>DQ-t-36</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t36-AC1, DQ9-t36-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~28/MDPF_DEMQUE.TO-DQ-t36.extension-never-shortens-a-file.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t36-AC1,DQ9-t36-AC2` BEFORE the flip.
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

Source: issuer defect in TO-DQ-t31 (the override-lands-or-is-covered rule, CLAUDE.md section 5 NEVER-move-served-output); decomposition round 9.
