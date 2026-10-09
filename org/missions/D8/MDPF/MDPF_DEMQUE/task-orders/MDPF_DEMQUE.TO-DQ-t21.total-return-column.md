# TO MDPF_DEMQUE.TO-DQ-t21 -- round 6 DQ-t-21: the total-return column in the price store, with both guards
<to_id>MDPF_DEMQUE.TO-DQ-t21</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~18</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-09 ~13:0xZ (row MDPF_DEMQUE-D1-W18-S1; issuer defects):** (1) GRANTED `data/mdpf/scripts/demque/test_demque_store.py`: its exact three-column assertion becomes the three original columns FIRST and unchanged, followed by `cash, total_return, tr_source, flags`; no other assertion changes; the full demque suite must pass. (2) GRANTED `data/mdpf/scripts/demque/daily_draw.py`: the scheduled draw passes each security's Bloomberg stored TR (via `tr_compare.py`'s loader; none when the name has none) and its money-market membership (`money_market.csv`) into `price_store.write`, so both guards fire in the draw, not only in the CLI. No criterion changes; the order stays open until both are done and AC1/AC2 re-pass.
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-21` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 6 -- CUT) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-21` (PRD `prd/MDPF_DEMQUE_PRD.md` ADDENDUM v0.5, C-PRICES; CTO round-5 analysis
`org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round5.md` R2; row `MDPF_DEMQUE-D1-S3`). Andrew's word: every stored Yahoo row
carries the as-traded price, the dividend/interest cash on its ex-date and a total-return value; every consumer reads the total return,
and the parts stay stored for audit. The method is fixed by DQ-t-17
(`org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~15/TR_COMPARISON.md`, graded MET):
`TR_t = (P_t + D_t) / (P_{t-1} / s_t) - 1`, P the as-traded close, D the cash going ex on t, s the split ratio on t.
`data/mdpf/scripts/demque/tr_compare.py` already implements `daily_tr`; reuse it, do not copy it.

Today the store (`data/mdpf/scripts/demque/price_store.py`, read it; contract
`org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~5/PRICE_STORE_CONTRACT.md`) writes per CUSIP `prices.parquet`
(`date, close_served, as_traded_close`), `splits.parquet` and `dividends.parquet`. dell2's ADVI_COTBKF reads `prices.parquet`.

**Build:**
1. NEW `data/mdpf/scripts/demque/tr_column.py`: `build(symbol, result, bbg=None, money_market=False) -> DataFrame` with columns `date`,
   `cash` (cash per share going ex that day, 0 otherwise), `total_return` (float or null), `tr_source` (`yahoo` | `bloomberg` |
   `accrual` | null) and `flags` (list of strings). Two guards, BOTH inside the build:
   - **(a) missing cash:** where Bloomberg's stored `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` (percent; `s3://opal-data-etfs/bbg/<date>/history_topup.parquet`,
     read only, via `tr_compare.py`'s loader) exists for the name, a non-ex-date day whose Yahoo TR differs from Bloomberg's by more
     than 1 bp is flagged `missing_cash` (the threshold is stated in the module).
   - **(b) money market:** for a symbol listed in NEW `data/mdpf/scripts/demque/money_market.csv` (columns `symbol, cusip, basis`; seed
     FXFXX and SALXX with the basis "DQ-t-17: $1.00 NAV, Yahoo TR 0"), `total_return` comes from Bloomberg's stored TR (`tr_source`
     `bloomberg`), else from an accrual you state (`accrual`), else null with flag `money_market_tr_unavailable` -- never Yahoo's 0.
   CLI `--names A,B --out <json>` writes `{"names": {symbol: [row, ...]}}` (no store write).
2. `price_store.py`: `prices.parquet` gains `cash`, `total_return`, `tr_source`, `flags` AFTER the existing columns; `date`,
   `close_served` and `as_traded_close` stay byte-identical for the same input. Update `PRICE_STORE_CONTRACT.md` with the four columns
   and the two guards.
3. NEW `data/mdpf/scripts/demque/test_demque_tr_column.py` (pytest; synthetic frames, no network) with exactly these names:
   `test_tr_is_close_plus_exdate_cash_over_prior_close_split_safe`, `test_missing_cash_flag_on_non_exdate_gap_against_bloomberg`,
   `test_money_market_tr_from_bloomberg_never_yahoo_zero`, `test_existing_price_columns_unchanged`. Keep the existing
   `test_demque_*.py` passing.

### ACCEPTANCE

<criterion id="DQ6-t21-AC1" cell_refs="DQ-t-21"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R6_CHECKS/dq_t21_tests.py</invocation><expect>TRC-OK</expect></criterion>
<criterion id="DQ6-t21-AC2" cell_refs="DQ-t-21"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R6_CHECKS/dq_t21_run.py</invocation><expect>TRCOL-OK</expect></criterion>
`DQ6-t21-AC1` -- the four named tests, including the unchanged existing columns. `DQ6-t21-AC2` -- the REAL column on LNVGY (2025-12-11
flagged `missing_cash`) and FXFXX (total return from Bloomberg, never Yahoo).

<expected_criteria>DQ6-t21-AC1,DQ6-t21-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `TRC-BAD no file ...`, `TRCOL-BAD no file ...tr_column.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No write to the served price store** (local or S3), **no AWS write, no Bloomberg call, no deploy.** The new columns reach the store
  at the next scheduled draw; that run is the issuer's. Yahoo is read through `yahoo_pull.pull`, one name at a time.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W18-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/tr_column.py
data/mdpf/scripts/demque/test_demque_tr_column.py
data/mdpf/scripts/demque/money_market.csv
data/mdpf/scripts/demque/price_store.py
data/mdpf/scripts/demque/test_demque_store.py
data/mdpf/scripts/demque/daily_draw.py
org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~5/PRICE_STORE_CONTRACT.md
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 6), cell `DQ-t-21`.
<owned_cells>DQ-t-21</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ6-t21-AC1, DQ6-t21-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~18/MDPF_DEMQUE.TO-DQ-t21.total-return-column.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ6-t21-AC1,DQ6-t21-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the LNVGY flag row and the FXFXX rows' sources, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed; the existing daily draw (22:30 local) writes the new columns from its next run.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write by the worker; S3 reads use the seat's existing read.
comp-adversary: DECLARED-NOT-APPLICABLE additive columns; the existing three columns are proven byte-identical by AC1.
risk: SERVED -- prices.parquet (read by ADVI_COTBKF) gains four columns at the next scheduled draw; existing columns DELTA=0.
direct_act: false -- a worker order.
</preflight>

Source: PRD ADDENDUM v0.5 @6c538a0bfd; CTO round-5 analysis @7732d73c04 R2; row D1-S3; DQ-t-17 TR_COMPARISON.md; decomposition round 6.
