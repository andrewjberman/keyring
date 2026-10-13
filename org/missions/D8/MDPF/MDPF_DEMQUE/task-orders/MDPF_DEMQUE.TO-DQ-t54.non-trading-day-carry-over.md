# TO MDPF_DEMQUE.TO-DQ-t54 -- round 9 DQ-t-54: a non-trading day's history room carries over the trading-day cells production left unused, read from the site Z budget ledger at run time
<to_id>MDPF_DEMQUE.TO-DQ-t54</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~46</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>CARRYOVER</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-54` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 18) |
**outcome_ref:** C-RESERVE, C-PRIORITY, FWD-3, FWD-4 | **depends_on:** DQ-t-27, DQ-t-34, DQ-t-44 (merged)

---

## WORKER FACE

### THE CELL

Andrew-direct 2026-10-13 ~20:0xZ (CTO msgs 5130 and 5134; record in [the queue form](file:///C:/dev/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md),
repo-relative `org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md`, the ~20:0xZ section): "We did not hit our limit this morning." The 10-13 miss was Bloomberg not
logged in, not quota. **History pulls on non-trading days are EXPANDED commensurately, cell by cell, with the trading-day allowance those days do not use.** A quota-limit claim is made only on
evidence. CTO ruling: the site Z drawer READS the `bbg_budget` ledger at run time (a read; no alarm, no monitor); the dell1 quote stays at zero carried over; each draw's receipt prints the
carried-over figure.

Today (`standing_drawer.py`, `bbg_quote.py`): a backfill is quoted over NON-trading days only at the measured history ceiling (5,858 cells a day, `bbg_allowance.json`), and a trading
day's backfill allowance is 0 because production draws history on trading days. Production does not use its whole trading-day ceiling, and that unused allowance is never spent on backfill.
This cell lets a non-trading-day fire spend it. **No vendor call is made by this cell; nothing is drawn.**

**Build** (read `standing_drawer.py` `run` / `_drawn_history_today` / `main`, `data/etfs/scripts/rivalfunds/bbg_budget.py` `ledger_dir` / `spent` / `_ledger_file`, `drawer_schedule.py`,
`lib/trading_calendar.py` first; import, do not copy):
1. **`carry_over(day, budget_dir=None) -> dict`** in `standing_drawer.py`: `ceiling` = the allowance file's history ceiling (int); `trading_days` = the NYSE trading days strictly after the previous
   fire day and strictly before `day` (the previous fire day is the last non-trading day before `day`; use `drawer_schedule` for the fire days); `spent[d]` = the sum of `rows` in that UTC day's budget
   ledger (`bbg_budget_<d>.jsonl` in `budget_dir`, default `bbg_budget.ledger_dir()`), a missing or unreadable file reading 0 and marking the figure absent; `carried_over` = the sum over
   trading days of `max(ceiling - spent[d], 0)` (never negative; an overspent day carries 0); `room` = `ceiling + carried_over`; `claim` = `"measured"` when at least one trading day's ledger was
   read, else `"absent"` (then `carried_over` is 0). No ledger present reads carried_over 0 and claim `absent`.
2. **The drawer uses it.** In `run`, a non-trading-day fire's room for the day = `room - drawn_today` (it was `ceiling - drawn_today`); the receipt printed for the run gains `carried_over`, `carry_claim` and
   `trading_days_read`. If the ledger cannot be read the run draws on the old room and says `carry_claim: absent` (never stops a draw). `--carry-over --day D [--budget-dir DIR]` prints the line of item 1
   as ONE JSON line (read only).
3. **The quote does NOT change.** `bbg_quote.quote` stays at zero carried over (CTO msg 5134): do not edit `bbg_quote.py`. A request therefore finishes no later than quoted.
4. NEW `test_demque_carry_over.py` (pytest; a temp budget directory, stub ledgers, no network) with exactly these names:
   `test_a_non_trading_day_room_is_the_measured_ceiling_plus_the_trading_day_cells_production_left_unused`,
   `test_a_trading_day_production_overspent_carries_nothing_and_never_a_negative`,
   `test_an_absent_or_unreadable_budget_ledger_carries_zero_and_the_receipt_says_so`.
   Existing drawer tests keep passing unedited; a drawer test that pins `room == ceiling - drawn` takes the stub's empty budget directory and NOTHING else.

### ACCEPTANCE

<criterion id="DQ9-t54-AC1" cell_refs="DQ-t-54"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t54_tests.py</invocation><expect>CARRY-OK</expect></criterion>
<criterion id="DQ9-t54-AC2" cell_refs="DQ-t-54"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t54_real.py</invocation><expect>CARRY-REAL-OK</expect></criterion>
`DQ9-t54-AC1` -- the three named tests. `DQ9-t54-AC2` -- three arms against temp ledger directories and the real default directory: an empty directory carries 0 and says absent; a synthetic week
(Monday 1,000, Wednesday ceiling + 500, the rest 0) carries (ceiling - 1000) + 0 + ceiling + ceiling; the real directory on this device (no site Z ledger) carries 0 and does not raise.
Report the whole folder `pytest data/mdpf/scripts/demque` once.

<expected_criteria>DQ9-t54-AC1,DQ9-t54-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `CARRY-BAD no file ...`; `standing_drawer.py: error: unrecognized arguments: --carry-over ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO Bloomberg call, no Yahoo call, no write to S3, the real budget ledger, the actuals ledger, the queue or any pacer state; no AWS write; no deploy; no timer. `standing_drawer.py --apply` is never
  run.** The only files you create outside tests are temp directories under the system temp.
- **Build no alarm, monitor or notification** (standing moratorium): the carried-over figure is printed in the draw's receipt, nothing more.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W46-S<k>`, `fabric` `dell1`, `surfaced_at` =
  `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY. Do NOT merge `box/dell1` (it is blocked by a foreign row);
  append your rows at the end of your own branch's copy and the issuer unions at the drain.

<paths>
data/mdpf/scripts/demque/standing_drawer.py
data/mdpf/scripts/demque/test_demque_carry_over.py
data/mdpf/scripts/demque/test_demque_standing_drawer.py
data/mdpf/scripts/demque/test_demque_standing_drawer_close.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-54`.
<owned_cells>DQ-t-54</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t54-AC1, DQ9-t54-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~46/MDPF_DEMQUE.TO-DQ-t54.non-trading-day-carry-over.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t54-AC1,DQ9-t54-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, each arm's line verbatim, the receipt line a run now prints, how the previous fire day is found, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed; the standing drawer's existing task runs the merged code at site Z.
comp-iam: DECLARED-NOT-APPLICABLE a read of a device-local budget ledger by the drawer that already writes it; no grant is requested or changed.
comp-adversary: DECLARED-NOT-APPLICABLE a bounded-room computation; the draw still stops on the first vendor limit warning or refusal.
risk: LOCAL -- code and tests. The next non-trading-day fire (2026-10-17) at site Z runs it: that fire is an act of ~ZQ's task under the existing draw hold, and spends nothing the existing allowance did not.
direct_act: false -- a worker order.
</preflight>

Source: Andrew-direct ~20:0xZ 2026-10-13 via CTO msgs 5130, 5134; decomposition round 9.
