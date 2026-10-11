# TO MDPF_DEMQUE.TO-DQ-t25 -- round 8 DQ-t-25: the history quote keys on the request's TIER, not on claim states
<to_id>MDPF_DEMQUE.TO-DQ-t25</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~21</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-25` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 8 -- CUT) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-25` (FWD-3, FWD-4; CTO round-7 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round7.md` R1, read it; rows
`MDPF_DEMQUE-D1-W19-S1` and `MDPF_DEMQUE-D1-S5`). `quote()` in `data/mdpf/scripts/demque/bbg_quote.py` (the history branch, near line 240)
walks non-trading days only when the history ceiling's claim is `measured` AND the reserve's claim is not. Two defects follow: measuring the
reserve would silently send backfills back to the weekday rule, and a tier-1 PRODUCTION history request is quoted as a backfill (the SHT8
request quoted for Monday 2026-10-12 reads `allowance_today` 0 and finish 2026-10-17).

**Build: ONE change to that branch.** Key on the request's `tier` (an int 1-5; a missing or non-int tier is a backfill, never production):
1. **Tier 1 (production).** It draws against the history reserve on ANY day. Room per calendar day = the history reserve figure (claim `held`
   or `measured`); today's room = max(reserve - drawn_today, 0). Every calendar day counts, trading or not. `finish_date` = the first calendar
   day (today counts) by which the cumulative room covers the cells. Set `allowance_today` to today's room, `finish_date_claim` to the
   reserve's claim, and `basis` to a new module constant `HISTORY_TIER1_BASIS` stating the rule. A reserve that is absent: `finish_date` None,
   `allowance_gap` `"history.reserve absent"`, `allowance_today` None.
2. **Tier 2 or above, or no tier (a backfill).** If the history ceiling's claim is `measured`: the existing non-trading-day walk
   (`_finish_non_trading`, `HISTORY_BASIS`) whatever the reserve's claim, `finish_date_claim` `measured`. If the ceiling's claim is NOT
   `measured`: `finish_date` None, `allowance_today` 0, and `allowance_gap` = the gap `_channel_finish` returns for the history channel (when it
   returns one) joined with `"; "` to the sentence `"history ceiling not measured (claim <claim>)"`. A backfill NEVER falls back to the weekday
   rule: the ceiling is only ever a measured figure.
3. Reference, bql and model_block are unchanged. Replace the module docstring's "History on non-trading days" paragraph (it still says a measured
   reserve keeps the weekday rule) with this rule.

**Tests.**
- NEW `data/mdpf/scripts/demque/test_demque_tier_quote.py` (pytest; no network; `sys.path.insert` of its own folder as
  `test_demque_nontrading.py` does) with exactly these names:
  - `test_tier2_history_with_both_claims_measured_still_walks_non_trading_days`: tier 2, 250 cells, ceiling 100 `measured`, reserve 125
    `measured`, quoted on Friday 2026-10-09 finishes 2026-10-17 with `allowance_today` 0 and `claims` both `measured`.
  - `test_tier1_history_reads_positive_allowance_today_on_a_trading_day_and_finishes_that_day`: tier 1, 16 cells, reserve 125 `held`, ceiling
    100 `measured`, quoted on Monday 2026-10-12: `allowance_today` 125, `finish_date` 2026-10-12, `finish_date_claim` `held`; and with
    `drawn_today` 120, `allowance_today` 5.
  - `test_tier2_history_ceiling_not_measured_has_null_finish_with_reason_and_zero_on_trading_day`: tier 2, ceiling `held`: `finish_date` None,
    `"not measured"` in `allowance_gap`, `allowance_today` 0 on Monday 2026-10-12 (trading) and on Saturday 2026-10-10.
- `data/mdpf/scripts/demque/test_demque_bbg.py`: `test_allowance_known_gives_finish_date_above_the_reserve` asserts the WEEKDAY rule on a history
  request, which is now the backfill rule. Keep its assertions as they are but move them to a `bql` request (same dates, `_allow("bql", 15, 5)`,
  `_req("bql", ("AAA",), ("F1",), "2026-10-05", "2026-10-30")`; the weekday rule still governs bql), and ADD a history version (tier 3, both claims
  `measured`, ceiling 15, reserve 5, 20 cells): quoted Thursday 2026-10-08 finishes 2026-10-11, with 5 drawn today still 2026-10-11, quoted
  Saturday 2026-10-10 with 0 drawn 2026-10-11, and ceiling 5 / reserve 5 finishes 2026-10-18 with `allowance_gap` None. No other assertion in the
  file changes.
- `test_demque_nontrading.py`, `test_demque_reserve_ledger.py` and every other `test_demque_*.py` must keep passing UNEDITED (the
  reserve_ledger "not positive" assertion survives because the gap keeps `_channel_finish`'s sentence). Run the folder as
  `pytest data/mdpf/scripts/demque --ignore data/mdpf/scripts/demque/test_demque_land.py` (that file fails to collect for an unrelated reason,
  row D1-S7, a later cell) and report a failure outside this order's paths as a surprise row; do not edit it.

### ACCEPTANCE

<criterion id="DQ8-t25-AC1" cell_refs="DQ-t-25"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t25_tests.py</invocation><expect>TQ-OK</expect></criterion>
<criterion id="DQ8-t25-AC2" cell_refs="DQ-t-25"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t25_quote.py</invocation><expect>TQQ-OK</expect></criterion>
`DQ8-t25-AC1` -- the three named tests. `DQ8-t25-AC2` -- the REAL requests: the 15,720-cell tier-4 TR request with both claims `measured`
quoted on Friday 2026-10-09 still finishes 2026-10-17 with `allowance_today` 0; the tier-1 SHT8 history request quoted on Monday 2026-10-12 reads
a positive `allowance_today` and finishes 2026-10-12; the same tier-4 request with the ceiling `held` reads `finish_date` null with
"not measured", and on trading Monday 2026-10-12 `allowance_today` 0 (the negative arm).

<expected_criteria>DQ8-t25-AC1,DQ8-t25-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `TQ-BAD no file ...`; `TQQ-BAD arms=a,b,c1,c2`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Bloomberg call, no deploy, no edit to `bbg_allowance.json`.** The quote reads files and the trading calendar only.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W21-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/bbg_quote.py
data/mdpf/scripts/demque/test_demque_tier_quote.py
data/mdpf/scripts/demque/test_demque_bbg.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 8), cell `DQ-t-25`.
<owned_cells>DQ-t-25</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ8-t25-AC1, DQ8-t25-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~21/MDPF_DEMQUE.TO-DQ-t25.tier-keyed-history-quote.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ8-t25-AC1,DQ8-t25-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the four quotes of AC2 verbatim, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the quote reads files and the trading calendar.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL quote code and its tests.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order.
</preflight>

Source: CTO round-7 analysis @f5553ca3d5 R1; rows D1-W19-S1, D1-S5 (REMEDIATION_v6); decomposition round 8.
