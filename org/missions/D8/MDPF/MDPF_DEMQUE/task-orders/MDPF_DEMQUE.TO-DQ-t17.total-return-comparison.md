# TO MDPF_DEMQUE.TO-DQ-t17 -- round 5 DQ-t-17: Bloomberg against Yahoo under the total-return method, before any TR column
<to_id>MDPF_DEMQUE.TO-DQ-t17</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~15</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-17` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 5 -- CUT) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-17` (PRD `prd/MDPF_DEMQUE_PRD.md` ADDENDUM v0.5, C-PRICES; CTO round-4 analysis
`org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round4.md` item 3). Andrew's word (record
`org/tier1_exec/2.0.0_SA_COO~Q1/deliverables/ANDREW_DIRECT_20261009_054xZ_PRICES_ARE_TOTAL_RETURN_STORE_PRICE_DIVIDEND_TR_PER_DAY.md`):
every price used is the dividend/interest-inclusive total return, with price and cash kept apart for audit; and compare Yahoo to Bloomberg
on clear dividend payers "to see how Yfinance handles corporate actions, dividends, interest income, and etc." This cell runs BEFORE any
total-return column is built; its finding fixes the method.

**Sources (read only):**
- **Bloomberg:** `s3://opal-data-etfs/bbg/<YYYY-MM-DD>/history_topup.parquet`, one per run day (34 partitions 2026-08-20..2026-10-07),
  columns `date, PX_LAST, DAY_TO_DAY_TOT_RETURN_GROSS_DVDS, security`. Union them; where two partitions hold the same (security, date),
  keep the later partition and count the conflicts. About one year (2025-09-30..2026-10-07) exists for ED, BX, CSCO, BBY and DG.
  `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` is Bloomberg's daily total return in PERCENT, gross dividends reinvested on the ex-date.
- **Yahoo:** `data/mdpf/scripts/demque/yahoo_pull.py` `pull(symbol)` (read it): the as-traded Close, dividends (cash per share on the
  ex-date) and splits. Yahoo's `Adj Close` is never used.

**Build:**
1. NEW `data/mdpf/scripts/demque/tr_compare.py`:
   - `daily_tr(close, dividends, splits) -> Series`: Yahoo daily total return on trade date t =
     `(P_t + D_t) / (P_{t-1} / s_t) - 1`, with `P` the as-traded close, `D_t` the cash per share going ex on t (0 otherwise) and `s_t`
     the split ratio effective on t (1 otherwise), so a split day is not a return.
   - `compare(name)`: align Bloomberg and Yahoo on their COMMON trade dates only; per name, `days_compared`, `median_abs_daily_diff_bp`,
     `p95_abs_daily_diff_bp`, `cum_tr_bloomberg` and `cum_tr_yahoo` (compounded over the common dates), and `events`: every ex-date and
     split in the window with the amount and both returns that day, plus the 10 largest daily differences with their dates.
   - CLI `--names A,B,... --out <json>` writes `{"names": {name: {...}}, "basis": ..., "window": ...}`; Bloomberg tickers map by the
     `security` column (state how).
2. NEW `data/mdpf/scripts/demque/test_demque_tr_compare.py` (pytest; synthetic frames, no network) with exactly these names:
   `test_daily_tr_from_as_traded_close_and_exdate_cash`, `test_split_day_is_not_a_return`,
   `test_comparison_aligns_on_common_trade_dates_only`.
3. Run it on every name with about a year of stored Bloomberg history (at least ED, BX, CSCO, BBY, DG; also any income fund among the
   stored names, for the interest question, if one exists). Write `TR_COMPARISON.json` and `TR_COMPARISON.md` in your deliverables folder.
   The `.md` answers, per finding, from the numbers: does Yahoo's ex-date cash match Bloomberg's gross return on ex-dates; how a special
   or variable distribution (BX) shows; how a split shows; whether any name pays interest-type income and how it appears; and the
   method recommended for the TR column. A finding the numbers do not show is written as not shown.

### ACCEPTANCE

<criterion id="DQ5-t17-AC1" cell_refs="DQ-t-17"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R5_CHECKS/dq_t17_tests.py</invocation><expect>TRM-OK</expect></criterion>
<criterion id="DQ5-t17-AC2" cell_refs="DQ-t-17"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R5_CHECKS/dq_t17_run.py</invocation><expect>TRCMP-OK</expect></criterion>
`DQ5-t17-AC1` -- the three named tests. `DQ5-t17-AC2` -- the REAL comparison on ED, BX and CSCO: at least 200 common days each, the
numbers present, an events list. The written finding in `TR_COMPARISON.md` is a JUDGMENT criterion graded at L9, never self-graded.

<expected_criteria>DQ5-t17-AC1,DQ5-t17-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `TRM-BAD no file ...`, `TRCMP-BAD no file ...tr_compare.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No Bloomberg call** (the stored history is read from S3), **no AWS write, no deploy, no write to any price store.** Yahoo is read
  through `yahoo_pull.pull`, paced politely (one name at a time).
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W15-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/tr_compare.py
data/mdpf/scripts/demque/test_demque_tr_compare.py
org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~15/TR_COMPARISON.json
org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~15/TR_COMPARISON.md
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 5), cell `DQ-t-17`.
<owned_cells>DQ-t-17</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ5-t17-AC1, DQ5-t17-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~15/MDPF_DEMQUE.TO-DQ-t17.total-return-comparison.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ5-t17-AC1,DQ5-t17-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the per-name table, the findings, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write; S3 reads use the seat's existing read.
comp-adversary: DECLARED-NOT-APPLICABLE research code and a report; nothing served.
risk: LOCAL -- research code, tests and a report; Yahoo and S3 are read only.
direct_act: false -- a worker order.
</preflight>

Source: PRD ADDENDUM v0.5 @6c538a0bfd; CTO rulings batch C (`CTO_RULINGS_BATCH_20261009T0550Z.md`); CTO round-4 analysis @91f3ee9da6
item 3; decomposition round 5. The 6-name extension (KO, JNJ, T, VZ, MO, XOM) re-runs this script when the queued draw
`requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json` lands.
