# TO MDPF_DEMQUE.TO-DQ-t13 -- round 4 DQ-t-13: within a tier, what matters most is drawn first, and each item says why
<to_id>MDPF_DEMQUE.TO-DQ-t13</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~12</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-13` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 4) |
**outcome_ref:** FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-13` (CTO msg 1519 item 3; dell2 research s.6; Andrew's Yahoo record: a former client's unmatchable fund "is not a priority to
get"). Andrew's tiers already order the queue (`data/mdpf/scripts/demque/demand_queue.py` draws by `tier`, then file order). Within a tier, rank the securities.

**Build** NEW `data/mdpf/scripts/demque/rank.py`:
1. Priority from Commonwealth's silver crosswalk (read-only; address from the builder:
   `lib.opal_naming.address("commonwealth","cottonwood","silver","crosswalk","date=2026-06-23")`, file `crosswalk.parquet`, column
   `status` (`MATCHED` / `NOT_MATCHED`), key `commonwealth_account`, with `reason_code`): **P1 living client** -- at least one holding
   account MATCHED; **P2 match open** -- none MATCHED but a holder is not resolved as gone (read the `reason_code` values and state the
   mapping in a docstring); **P3 gone** -- every holder resolved as gone.
2. Score within a priority: held days x holding accounts x largest single purchase amount, from Commonwealth's silver transactions
   (`address("commonwealth","cottonwood","silver","transactions","date=2026-06-23")`, columns `Account_Number, Cusip, Transaction_Type,
   Quantity, Amount, Trade_Date`; read only the columns needed).
3. `rank(securities, crosswalk_df, tx_df) -> list` ordered P1, P2, P3, then score descending; each item `{cusip, symbol, priority,
   score, rank, reason}` (reason in plain words). A P3 security with no symbol is `not pursued` (excluded, listed with that reason).
4. In `data/mdpf/scripts/demque/demand_queue.py`: the draw orders requests by `tier`, then the request's optional `rank` (lower first; absent = last), then file
   order; within a request, securities by their optional `rank`. Keep every existing test passing.
5. CLI `python rank.py --probe N`: ranks the first N YAHOO rows of
   `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.csv` and prints one line each, best first:
   `RANK <n> cusip=<cusip> priority=<P1|P2|P3> score=<number> reason=<text>`. Print no account number or name.
6. NEW `data/mdpf/scripts/demque/test_demque_rank.py` (synthetic frames) with exactly these names: `test_living_client_outranks_match_open_outranks_gone`,
   `test_within_priority_score_is_held_days_times_accounts_times_largest_purchase`, `test_gone_client_unmatchable_fund_is_not_pursued`,
   `test_draw_order_is_tier_then_rank`, `test_each_item_carries_its_rank_and_reason`.

### ACCEPTANCE

<criterion id="DQ4-t13-AC1" cell_refs="DQ-t-13"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R4_CHECKS/dq_t13_tests.py</invocation><expect>RANK-OK</expect></criterion>
<criterion id="DQ4-t13-AC2" cell_refs="DQ-t-13"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R4_CHECKS/dq_t13_seam.py</invocation><expect>KSEAM-OK</expect></criterion>
`DQ4-t13-AC1` -- the five named tests. `DQ4-t13-AC2` -- the ranking on the REAL crosswalk and transactions: 10 lines, P1 before P2 before P3, scores non-increasing within a priority.

<expected_criteria>DQ4-t13-AC1,DQ4-t13-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `RANK-BAD no file ...`, `KSEAM-BAD no file ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No vendor call, no AWS write, no deploy.** Read-only S3 reads of the two Commonwealth objects only.
- **No client data in any committed file;** tests use synthetic frames.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W12-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/rank.py
data/mdpf/scripts/demque/test_demque_rank.py
data/mdpf/scripts/demque/demand_queue.py
data/mdpf/scripts/demque/test_demque_queue.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 4), cell `DQ-t-13`.
<owned_cells>DQ-t-13</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ4-t13-AC1, DQ4-t13-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~12/MDPF_DEMQUE.TO-DQ-t13.within-tier-ranking.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ4-t13-AC1,DQ4-t13-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL code.
risk: LOCAL -- code, config and tests.
direct_act: false -- a worker order.
</preflight>

Source: PRD v0.3 FWD-9, C-PRIORITY; CTO msg 1519 item 3; dell2 research s.6; decomposition round 4.
