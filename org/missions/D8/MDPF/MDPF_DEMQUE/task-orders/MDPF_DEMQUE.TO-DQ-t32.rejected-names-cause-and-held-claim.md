# TO MDPF_DEMQUE.TO-DQ-t32 -- round 9 DQ-t-32: the cause of each lock rejection is measured, and the existing files serve with claim `held`
<to_id>MDPF_DEMQUE.TO-DQ-t32</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~25</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-32` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT) |
**outcome_ref:** C-PRICES, FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-32` (CTO round-8 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round8.md` R2, read it; row `MDPF_DEMQUE-D1-S9`).
Fourteen names (LCEYX, FTHSX, HLMEX, IWS, IWP, IWN, IWO, VSEIX, PFORX, RPIFX, VSS, VWO, MISIX, PIMSX) each passed a lock on 2026-10-09 and were
REJECTED by `lock.py`'s 90 percent trade-agreement floor on the 2026-10-11 re-draw (agreement 79 to 88 percent; FTHSX, PFORX and RPIFX near 40).
**Ruled: the floor is NOT lowered and the band is NOT widened.** Their existing three-column files keep serving, with the lock record's claim
`held` and a reason; the cause is measured first. This order builds the two tools; the applying of the claim is the issuer's act.

**Build** (NEW files under `data/mdpf/scripts/demque/`; read `lock.py`, `redraw_stale.py`, `price_store.py` `_Store`, `yahoo_pull.py` and
`daily_draw.py` `on_result` first; import, do not copy):
1. `lock_cause.py`. For each name (`--names A,B,C`, default every name `redraw_stale.stale()` lists), with its CUSIP from the stale row:
   - `old` = the served file's `as_traded_close` by date (`price_store._Store(root).get("cusip=<C>/prices.parquet")`); `new` = a fresh
     `yahoo_pull.pull(symbol)` `prices` frame, paced by a `yahoo_pull.Pacer` whose state file is a scratch path under the system temp folder
     (the same rule and gaps, NEVER the real `pacer.json`); trades = `lock._load_transactions([cusip])` through `lock.trade_prices`, one median
     price per trade date; the tolerance and asset type are `lock.check`'s (`TOL_MUTUAL_FUND` for `Mutual Fund`, else `TOL_OTHER`; the asset
     type from the transactions' `Asset_Type`, as `daily_draw.on_result` reads it).
   - `agreement_old_pct` and `agreement_new_pct`: percent of trade dates (that have a close on that side) whose relative error is within the
     tolerance, one decimal; `n_checked` the dates compared on the new side.
   - `disagreeing`: the dates the NEW side fails, each `{"date", "trade_type", "near_exdiv", "near_split"}`: the trade type (`by`, `sl`, `dvr`)
     of that date's trades; `near_exdiv` / `near_split` true when an ex-dividend / split date from the pull lies within 3 calendar days.
   - `first_lock_at` the served `lock.json` `locked_at`; `first_lock_predates_floor` true when it is before `2026-10-09T03:35:00Z` (commit
     `52b8a3cca2`, the floor).
   - `cause`, exactly one of: `wrong-symbol` when both agreements are below 60; `draw-column` when `agreement_old_pct` >= 90 and
     `agreement_new_pct` < 90; `never-met-floor` when `agreement_old_pct` < 90 and `agreement_new_pct` >= 60; else `unclassified`.
   CLI `--names A,B --json` prints ONE JSON line `{"names": [row, ...]}` with the keys above plus `symbol`, `cusip`, `asset_type`; without
   `--json` a readable table. Read only: no S3 write.
2. `hold_lock_records.py`. For every name whose `prices.parquet` carries exactly `price_store.PRICE_COLS` (`--names` narrows), plan this change
   to its `cusip=<C>/lock.json`: `claim` becomes `"held"` and a new key `claim_reason` carries `"re-draw trade agreement below the 90 pct floor
   (row MDPF_DEMQUE-D1-S9); cause under measurement"`; EVERY other key is kept as it was. `--dry-run` prints ONE JSON line `{"planned":
   [{"cusip", "symbol", "claim_before", "claim_after", "claim_reason"}, ...]}` and writes nothing. `--apply` PutObjects each changed
   `lock.json` (idempotent: a record already `held` with that reason is skipped) and prints `{"written": n, "skipped": m}`; you do NOT run
   `--apply`.
3. NEW `test_demque_lock_cause.py` (pytest; a LOCAL store root under `tmp_path`, synthetic frames, a stub fetch, no network, no S3) with exactly
   these names: `test_agreement_is_computed_against_the_old_file_and_the_new_draw`,
   `test_disagreeing_dates_are_listed_with_exdiv_split_and_trade_type` (the cause classes of item 1 each reached once) and
   `test_hold_record_sets_claim_held_with_the_reason_and_keeps_every_other_key` (a second apply writes nothing).

### ACCEPTANCE

<criterion id="DQ9-t32-AC1" cell_refs="DQ-t-32"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t32_tests.py</invocation><expect>LC-OK</expect></criterion>
<criterion id="DQ9-t32-AC2" cell_refs="DQ-t-32"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t32_real.py</invocation><expect>LCAUSE-OK</expect></criterion>
<criterion id="DQ9-t32-AC3" cell_refs="DQ-t-32"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t32_hold.py</invocation><expect>HOLD-OK</expect></criterion>
`DQ9-t32-AC1` -- the three named tests. `DQ9-t32-AC2` -- the cause instrument on three REAL names (FTHSX, IWS, VWO; S3 and three paced Yahoo
reads): every field present, `agreement_new_pct` within 1.5 of 40.7, 83.3 and 87.2, `cause` in the closed set. `DQ9-t32-AC3` -- `hold_lock_records.py
--dry-run` on the REAL store plans exactly the names still on three columns, each `held` with the stated reason.
`AC3` is the cell's third check because `hold_lock_records.py` is a second tool with its own seam (the served lock records), not a variant of AC2.

<expected_criteria>DQ9-t32-AC1,DQ9-t32-AC2,DQ9-t32-AC3</expected_criteria>

Run each invocation from the worktree root (each is bounded under the 120 s limit; AC2 reads three names only). At the base: `LC-BAD no file
...`, `LCAUSE-BAD no file ...lock_cause.py`, `HOLD-BAD no file ...hold_lock_records.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No write to the served price store or any `lock.json` (local or S3), no write to the real pacer state or queue, no AWS write, no Bloomberg
  call, no deploy.** Yahoo is read through `yahoo_pull.pull`, one name at a time under the scratch pacer; no more than the three AC2 names in a
  run of yours.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W25-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/lock_cause.py
data/mdpf/scripts/demque/hold_lock_records.py
data/mdpf/scripts/demque/test_demque_lock_cause.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-32`.
<owned_cells>DQ-t-32</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t32-AC1, DQ9-t32-AC2, DQ9-t32-AC3. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~25/MDPF_DEMQUE.TO-DQ-t32.rejected-names-cause-and-held-claim.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t32-AC1,DQ9-t32-AC2,DQ9-t32-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the three AC2 rows verbatim, the `--dry-run` planned count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write by the worker; the S3 reads use the seat's existing read.
comp-adversary: DECLARED-NOT-APPLICABLE a read-only measuring tool and a planned-change tool; neither writes.
risk: LOCAL -- code and tests. The issuer's `hold_lock_records.py --apply` writes 14 served lock.json (SERVED; CTO half = round-8 analysis R2; rollback per key = the object's prior S3 version).
direct_act: false -- a worker order.
</preflight>

Source: CTO round-8 analysis @92a9b27704 R2; row D1-S9 (REMEDIATION_v7); decomposition round 9.
