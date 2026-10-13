# TO MDPF_DEMQUE.TO-DQ-t44 -- round 9 DQ-t-44: every Bloomberg request declares its need class and window; the queue refuses what reaches past the 2012 floor or its class window; the TR remainder and the P1 window follow
<to_id>MDPF_DEMQUE.TO-DQ-t44</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~36</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>NEEDCLASS</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-44` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 9) |
**outcome_ref:** C-QUOTE, C-PRIORITY, C-RESERVE, FWD-4 | **depends_on:** DQ-t-43 (merged @b956c6307e)

---

## WORKER FACE

### THE CELL

Law, Andrew-direct 2026-10-13 (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_141xZ_BACKFILL_FLOOR_2012_AND_EARLIEST_CLIENT_RECORD.md`, read it
including ADDENDUM 1 and 2): (1) a client-history window is `[max(earliest client record, 2012-01-01), today]` intersected with the dates the security was held;
(2) a non-client need (rival funds, research, ETF positioning, market context) takes **365 days back from its need date**; (3) the 2012-01-01 floor binds both;
(4) **every request DECLARES its need class and window start, and the queue REFUSES an undeclared or over-window request, never trimming silently.**
This cell lands that rule for the Bloomberg side, re-windows the CARD-A P1 slice, and makes the already-trimmed TR comparison draw only what it has not
drawn. **It makes NO Bloomberg call and arms nothing.**

**Build** (read `data/mdpf/scripts/demque/bbg_quote.py` `_validate` / `quote`, `standing_drawer.py` `open_requests` / `run` / `PRIOR_OUTPUTS`, `card_a_slice.py`, and
the record above first):
1. **Declarations.** A Bloomberg request carries `need_class` (`"client"` or `"non_client"`), `window_start` (ISO date, or `null` for a `reference` or
   `model_block` channel that has no date window), and, for `non_client` with a history or bql channel, `need_date` (ISO). A standing request may carry
   `window_rule: "365_days_before_run_date"` in place of `window_start`/`need_date` (a rule the producer applies each run).
2. **Refusal in `bbg_quote._validate` (and so `quote`).** `ValueError`, naming the request id and the rule, when: `need_class` is missing or not one of
   the two; `window_start` is missing on a history/bql channel (and no `window_rule`); `window_start` or any security's own `start` is before
   2012-01-01; any security's `start` is before the request's `window_start`; `non_client` and `window_start` is more than 365 days before `need_date`.
   It never trims or rewrites a window. Existing requests that satisfy the rule keep their exact old cells.
3. **`bbg_quote.py --check-declared DIR`** (read only): over every `*.json` in DIR that has a `securities` list and vendor `bloomberg` (or no vendor and a
   Bloomberg channel), run the same validation; print ONE JSON line `{"checked": N, "refused": [{"request_id", "why"}], "accepted": N}`.
4. **Declare the existing requests.** In each of these files under `org/missions/D8/MDPF/MDPF_DEMQUE/requests/` add exactly these keys (nothing else changes):
   - `SITEZ-SIGNIN-PREFLIGHT-REFDATA-20261009.json`: non_client, need_date 2026-10-09, window_start null.
   - `MDPF_SECHIST-SHT8-TR-FIELD-CONFIRM-20261009.json`: non_client, need_date 2026-10-09, window_start 2026-10-08.
   - `MDPF_SECHIST-SHT8-TR-FIELD-HISTORY-20261009.json`: non_client, need_date 2026-10-09, window_start 2026-09-28.
   - `AMGT_RESAPP-493c-ICT-IDENTITY.json`: non_client, need_date 2026-10-09, window_start null.
   - `AMGT_RESAPP-S14-CRNCY-SCANNER-US.json` and `AMGT_RESAPP-S14-CRNCY-SCANNER-US-SLICE1.json`: non_client, need_date 2026-10-11, window_start null.
   - `AMGT_RESAPP-107a-ABNB-MODEL-BLOCK.json`: non_client, need_date 2026-10-09, `window_start` = the producer's `HIST_START` (read it from the producer named by
     `bbg_quote.PRODUCER_PATH`). If the rule REFUSES it, do not weaken the rule: file a BLOCKING surprise row and leave the file declared as read.
   - `ETFS_RIVALS-HISTORY-OWED-DAILY.json`: non_client, `window_rule` `365_days_before_run_date`.
   - `MDPF_SECHIST-CARD-A-COT-BBG-HISTORY.json`: client, window_start 2013-04-03, and add `"superseded_by": "MDPF_SECHIST-CARD-A-P1-SLICE"` (it has no securities
     list; the P1 slice is its priced successor).
   - `DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json`: non_client, need_date 2026-10-09, window_start 2025-10-09, `start` 2025-10-09 (was 2021-10-01), `end` unchanged
     2026-10-08, and `"window_trim": "Andrew-direct 2026-10-13 addendum 2 (CTO msg 4889): drawn rows kept; only the in-window remainder draws"`.
5. **The TR remainder by identity (`standing_drawer.py`).** The drawer prices and draws the remainder as the set of (security, date) rows INSIDE the request's
   window that are not already stored in the prior output folders (`PRIOR_OUTPUTS` and the standing output folder, the `history-*.parquet` files with columns
   `date, <fields>, security`), never as `quoted cells - drawn cells`. Rows outside the window that were already drawn stay stored and are never re-drawn or
   deleted. Add `--plan --request ID [--day D]` (read only, no Bloomberg call): print ONE JSON line `{"request_id", "window_start", "remaining_cells",
   "securities": [...]}` where `securities` are the securities with at least one undrawn in-window row.
6. **The P1 window (`card_a_slice.py`).** Replace the card's 2013-04-03 floor with 2012-01-01 and the end 2026-06-23 with the last trading day on or before
   today (`lib/trading_calendar.expected_last_trading_day`): a name's window is `[max(first transaction Trade_Date, 2012-01-01), end]` where `end` = that
   frontier when the name is still HELD (net quantity, buys minus sells over every account, is positive at the last transaction) and its last `Trade_Date`
   when it is not. State in the docstring how held is read; if the transactions carry no sign, treat every name as held and set the printed `claim` to
   `inferred`. The written request declares `need_class` `"client"` and `window_start` = the earliest start in it. The `--quote` line keeps its keys; `window_end`
   becomes the frontier. The request still carries CUSIPs and dates only, no account key.
7. NEW `test_demque_need_class.py` (pytest; stubs, no network, no S3) with exactly these names:
   `test_a_bloomberg_request_without_a_declared_need_class_or_window_start_is_refused`,
   `test_a_window_before_2012_or_a_non_client_start_beyond_365_days_of_its_need_date_is_refused_never_trimmed`,
   `test_the_card_a_slice_window_ends_at_the_frontier_for_a_held_name_and_at_the_last_trade_for_a_sold_one`,
   `test_a_request_whose_start_moves_later_draws_only_the_undrawn_in_window_rows_by_identity`.
   Existing demque test files keep passing; if one needs a stub request to carry the new declarations, change only that stub and nothing else in the file.

### ACCEPTANCE

<criterion id="DQ9-t44-AC1" cell_refs="DQ-t-44"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t44_tests.py</invocation><expect>CLASS-OK</expect></criterion>
<criterion id="DQ9-t44-AC2" cell_refs="DQ-t-44"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t44_real.py</invocation><expect>CLASS-REAL-OK</expect></criterion>
`DQ9-t44-AC1` -- the four named tests. `DQ9-t44-AC2` -- on the REAL files and drawn rows (S3 read only): every Bloomberg request file under `requests/` passes the
rule (none refused), the TR comparison plans exactly 1,004 remaining cells on MO and XOM from window start 2025-10-09, and the P1 slice's window ends at the
frontier and declares client. Report the whole folder `pytest data/mdpf/scripts/demque` once (151 passed at the t-43 merge, plus these 4).

<expected_criteria>DQ9-t44-AC1,DQ9-t44-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `CLASS-BAD no file ...`; `bbg_quote.py: error: unrecognized arguments: --check-declared ...`.


### AMENDED 2026-10-13 ~15:4xZ (issuer; no gate limb graded it, no new order added) -- rulings on rows D1-W36-S1 to S9, and the re-seated slot

Your first pass (commits `0b5d4015f1`, `d8588dab05`) stands as inherited state. The grant above now ALSO names ten more files. Rulings:
- **S1 (ABNB refused): the refusal STANDS.** The producer's `HIST_START` 2016-01-01 is beyond 365 days of the need date; the queue refuses and never trims. The request stays
  declared as read and UNDRAWN until the CTO or Andrew rule. The real check's arm 1 now allows exactly this one refusal (reason must name 365 days).
- **S2 (bbg_backfill, ARMED, disarmed by the issuer):** its CLI is unreachable (`--apply` plus date 2026-10-10 only; evidence
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/DISARM_EVIDENCE_D1_W36_S2_20261013.md`). In `bbg_backfill.run()` add the same stored-row identity check
  as the standing drawer (skip every (security, date) already stored in the output folders), so the function is safe on its own; update its tests accordingly.
- **S3 to S6:** update the named failing tests in the files now granted: add the declarations a stub needs (`need_class`, `window_start`, `need_date` as the
  rule requires), move pinned TR-window figures to the re-windowed request's real figures, update the card-A assertions to the 2012 floor and the frontier end, and
  change the drawer test to the identity remainder (16 cells, not quoted minus drawn). Change ONLY what the failures require; every other assertion stays.
- **S7 (held rule):** find the transaction type code meanings (search `docs/` and the Commonwealth silver transactions' own mapping; name your source). Classify each
  code as adds-to or removes-from a position; `by` and `trfi`/`li`-type codes add, `sl` and `trfo`/`lo`-type codes remove, only where the source says so. Any code you cannot
  classify leaves the name HELD and the printed `held_claim` `inferred`.
- **S8:** out of this cell (the Yahoo side, t-45).
- **S9:** the TR quote file is re-frozen by the issuer at the merge.
- **The investigation file:** the HEAD copy carried account ids at one line (row D1-S13, now redacted at `84bb84909c` on box/dell1). Merge `box/dell1` into
  your branch first (a MERGE, never a rebase) so the file is clean, then append your rows; do not edit an existing row.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: no Bloomberg call, no write to S3, the ledger, the queue, any pacer state or the drawer's output folders; no AWS write, no deploy, no timer or
  background task. `standing_drawer.py --apply` is never run.** The Yahoo side (`demand_queue.py`, `extend_frontier.py`) is NOT in this cell.
- **Account ids never enter a committed file.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W36-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, and do
  not weaken a check or the refusal rule. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/bbg_quote.py
data/mdpf/scripts/demque/standing_drawer.py
data/mdpf/scripts/demque/card_a_slice.py
data/mdpf/scripts/demque/test_demque_need_class.py
data/mdpf/scripts/demque/test_demque_card_a_slice.py
data/mdpf/scripts/demque/test_demque_bbg.py
data/mdpf/scripts/demque/test_demque_standing_drawer.py
org/missions/D8/MDPF/MDPF_DEMQUE/requests/SITEZ-SIGNIN-PREFLIGHT-REFDATA-20261009.json
org/missions/D8/MDPF/MDPF_DEMQUE/requests/MDPF_SECHIST-SHT8-TR-FIELD-CONFIRM-20261009.json
org/missions/D8/MDPF/MDPF_DEMQUE/requests/MDPF_SECHIST-SHT8-TR-FIELD-HISTORY-20261009.json
org/missions/D8/MDPF/MDPF_DEMQUE/requests/AMGT_RESAPP-493c-ICT-IDENTITY.json
org/missions/D8/MDPF/MDPF_DEMQUE/requests/AMGT_RESAPP-S14-CRNCY-SCANNER-US.json
org/missions/D8/MDPF/MDPF_DEMQUE/requests/AMGT_RESAPP-S14-CRNCY-SCANNER-US-SLICE1.json
org/missions/D8/MDPF/MDPF_DEMQUE/requests/AMGT_RESAPP-107a-ABNB-MODEL-BLOCK.json
org/missions/D8/MDPF/MDPF_DEMQUE/requests/ETFS_RIVALS-HISTORY-OWED-DAILY.json
org/missions/D8/MDPF/MDPF_DEMQUE/requests/MDPF_SECHIST-CARD-A-COT-BBG-HISTORY.json
org/missions/D8/MDPF/MDPF_DEMQUE/requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json
data/mdpf/scripts/demque/bbg_backfill.py
data/mdpf/scripts/demque/test_demque_bbg_backfill.py
data/mdpf/scripts/demque/test_demque_ceiling.py
data/mdpf/scripts/demque/test_demque_nontrading.py
data/mdpf/scripts/demque/test_demque_quote_remaining.py
data/mdpf/scripts/demque/test_demque_refreeze.py
data/mdpf/scripts/demque/test_demque_reserve.py
data/mdpf/scripts/demque/test_demque_reserve_ledger.py
data/mdpf/scripts/demque/test_demque_standing_drawer_close.py
data/mdpf/scripts/demque/test_demque_tier_quote.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit; another file that needs a change is a surprise row asking for the grant,
not an edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-44`.
<owned_cells>DQ-t-44</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t44-AC1, DQ9-t44-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~36/MDPF_DEMQUE.TO-DQ-t44.floor-2012-need-class-refusal-and-identity-remainder.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t44-AC1,DQ9-t44-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, each arm's line verbatim, the `--plan` line for the TR comparison, the P1 `--quote` line, any refused request and why,
how held is read, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed; the standing drawer's next fire is the first non-trading day, after this lands.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a validation rule, a read-only plan and request declarations; nothing draws or serves.
risk: LOCAL -- code, tests and request declarations. The draw is a site-Z act under the queue's budget and the Terminal sign-in (Andrew's).
direct_act: false -- a worker order.
</preflight>

Source: Andrew-direct 2026-10-13 14:1xZ and addenda (CTO msgs 4881, 4884, 4889, 4892); QUEUE_QUALIFICATION_20261013.md @ac96e00cbd; decomposition round 9.
