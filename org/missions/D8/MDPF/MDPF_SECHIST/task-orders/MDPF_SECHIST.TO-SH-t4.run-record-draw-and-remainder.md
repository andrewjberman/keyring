# TO MDPF_SECHIST.TO-SH-t4 -- round 2 SH-t-4: the ETF daily pull's run record prints the backfill draw beside the budget remainder

<to_id>MDPF_SECHIST.TO-SH-t4</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~3</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `SH-t-4` (`decompositions/MDPF_SECHIST_DECOMP_R2.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SH-t-4`. FWD-7: an operator reads what history cost today against the shared Bloomberg budget.

**The code, read at the base.** `integrations/bloomberg/pipeline/etf_daily_pull.py`, the history depth backfill block (about lines 536-612):
- Before any request it reads `_bb.config()` and `_bb.spent()` from the ledger module `bbg_budget.py`, computes
  `_limit = daily_ceiling_rows - production_reserve_rows`, `_est = history_backfill_rows_estimate(...)` (ticker-weekdays), and sets
  `backfill_budget = {"estimate": _est, "limit": _limit, "spent_before": _used, "recorded": None}`. Over the limit it raises and fetches nothing.
- In `finally`, after a fetch was attempted, it sets `backfill_budget["recorded"]` from `_bb.record("backfill", _rows_got, ...)` (returned records).
- The manifest writes `"history_backfill_budget": backfill_budget` (about line 695).

**Build:**
1. In `etf_daily_pull.py`, once the block has finished (after the `finally`, wherever `backfill_budget` is not None), add two keys to
   `backfill_budget`: `spent_after` = `_bb.spent()` re-read from the ledger, and `remainder` = `max(limit - spent_after, 0)`. On the refusal
   path (nothing fetched) `spent_after` equals `spent_before`. A failure of that re-read leaves both keys `None` and logs a WARN; it never
   changes the exit code. Then log ONE line: `history backfill budget: estimate <E> rows (ticker-weekdays), drawn <R> rows (returned
   records), ledger remainder <M> of <L>`. Say "ledger remainder": other Bloomberg legs do not write this ledger yet, so it is not the
   day's whole Bloomberg remainder.
2. In `test_etf_daily_pull_history_plan.py`, add `test_run_record_prints_draw_and_remainder`, reusing `_run_budget_arm` and the fakes already
   there: for a run that draws, the manifest's `history_backfill_budget` has `spent_after == spent_before + recorded` and
   `remainder == limit - spent_after`; for a refused run, `spent_after == spent_before` and `remainder == max(limit - spent_before, 0)`.
   Keep every existing test passing unchanged.

### ACCEPTANCE

<criterion id="SH2-t4-AC1" cell_refs="SH-t-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R2_CHECKS/sh_t4_budget_tests.py</invocation><expect>BUDGET-TESTS-OK</expect></criterion>
`SH2-t4-AC1` -- the new test and the existing budget test both pass by name against the real pull module.

<expected_criteria>SH2-t4-AC1</expected_criteria>

Run the invocation from the worktree root. It FAILS at the base (2026-10-08): `BUDGET-TESTS-BAD not-passed=test_run_record_prints_draw_and_remainder`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No S3, no Bloomberg, no deploy, no run of the pull.** The tests are offline. Do not change the refusal rule, the ledger format, what is
  fetched, or the production pull.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_SECHIST-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, class OBSERVATION or BLOCKING) in the investigation file below, and do not
  weaken the test.

<paths>
integrations/bloomberg/pipeline/etf_daily_pull.py
integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py
org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R2.md</decomp_doc> (round 2), cell `SH-t-4`.
<owned_cells>SH-t-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH2-t4-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~3/MDPF_SECHIST.TO-SH-t4.run-record-draw-and-remainder.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SH2-t4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the diff summary, the test output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule change; the leg runs in the existing site Z daily task.
comp-iam: DECLARED-NOT-APPLICABLE no IAM; offline tests.
comp-adversary: RUN at the cut -- the remainder is labelled the ledger's, never the day's whole Bloomberg remainder (ruling 31292: other legs write 0 lines).
risk: LOCAL -- code and test; the site Z take is WORLD and is the issuer's act at the drain under a never-widen pair, after the FWD-1 acceptance pull.
direct_act: true -- one cell, under 300 lines, LOCAL.
</preflight>

Source: CTO round-1 analysis @0141533760 section 3 item 2; PRD v0.2 FWD-7.
