# TO MDPF_DEMQUE.TO-DQ-t1 -- round 1 DQ-t-1: a Cottonwood CUSIP is locked to one Yahoo symbol, per date range, against the client's own trade prices
<to_id>MDPF_DEMQUE.TO-DQ-t1</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~1</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `DQ-t-1` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 1) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-1`, hop 2 of the FWD-1 thread: before any price is shown for a Cottonwood security, its CUSIP is matched to one Yahoo Finance
symbol for a date range, and the match is PROVED against the prices the client actually traded at.

**Build** NEW `data/mdpf/scripts/demque/lock.py` (pandas; no vendor call; no write anywhere) with:

1. `trade_prices(transactions: DataFrame, cusip: str) -> DataFrame[date, price]`: from Commonwealth's own transaction rows for that CUSIP,
   only trade rows (transaction type `by`, `sl` or `dvr`) carrying a non-zero quantity and an amount; `price = abs(Amount / Quantity)`.
   Read the real column names from the data (step 3 below) -- do not guess them.
2. `check(cusip, symbol, prices, trades, asset_type, valid_from, valid_to, run_id, supersedes=None) -> dict`, where `prices` is a
   DataFrame `date, as_traded_close` (Yahoo, already as traded) and `trades` is step 1's output. Returns ONE lock row with exactly these
   keys: `cusip, yahoo_symbol, valid_from, valid_to, method, observations_checked, observations_passed, median_abs_error, state, claim,
   locked_at, run_id, supersedes`. The rule:
   - compare on every trade date that has an as-traded close; `abs_error = abs(close - trade_price) / trade_price`;
   - tolerance 0.005 when `asset_type` is a mutual fund (NAV trades at NAV), else 0.02 (listed equity, ETF, closed-end: intraday vs close);
   - `state = "LOCKED"`, `claim = "measured"` only when at least `min(3, available)` dates pass AND at least one passing date falls in the
     earliest third of `[valid_from, valid_to]`; otherwise `state = "REJECTED:PRICE_MISMATCH"`;
   - no trade dates at all -> `state = "LOCKED"`, `claim = "held"`, `observations_checked = 0` (a consumer can refuse it);
   - `method` is the candidate source you were given (`C1` Commonwealth Symbol is the only one this round builds).
3. A CLI `python lock.py --probe N`: reads the REAL Commonwealth silver transactions
   (`s3://opal-data-assets/commonwealth/cottonwood/silver/transactions/date=2026-06-23/`, all parquet parts, read-only) and the first N
   `source == YAHOO` rows of `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.csv`
   (columns `security_id,asset_class,source,first_date_needed,last_date_needed,days_needed`; `security_id` is the CUSIP), and prints
   exactly one line per CUSIP: `PROBE cusip=<cusip> symbol=<Commonwealth Symbol or -> trades=<count of trade_prices rows>`. rc 0.
   Use the AWS credentials already on the box (boto3 default chain; read-only `ListObjectsV2` / `GetObject` only). Print no account
   number, name or amount -- counts and CUSIP/symbol only.
4. NEW `data/mdpf/scripts/demque/test_demque_lock.py` (pytest, synthetic frames, no S3) with exactly these test names:
   `test_agreeing_series_locks_measured`, `test_recycled_ticker_rejected_on_early_third` (agrees only in the last two thirds -> REJECTED),
   `test_too_few_agreeing_dates_rejected`, `test_mutual_fund_uses_half_percent_band` (1% error passes a stock, fails a mutual fund),
   `test_no_trade_prices_locks_with_claim_held`, `test_trade_price_is_abs_amount_over_quantity_on_trade_rows_only`.

The module imports nothing from another cell. `lock.py` lives beside other cells' files in `data/mdpf/scripts/demque/`; do NOT create
`__init__.py` there (the issuer adds it at the merge).

### ACCEPTANCE

<criterion id="DQ1-t1-AC1" cell_refs="DQ-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R1_CHECKS/dq_t1_tests.py</invocation><expect>LOCK-OK</expect></criterion>
<criterion id="DQ1-t1-AC2" cell_refs="DQ-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R1_CHECKS/dq_t1_seam.py</invocation><expect>SEAM-OK</expect></criterion>
`DQ1-t1-AC1` -- the lock rule, by the six named tests. `DQ1-t1-AC2` -- the seam against the real Commonwealth transactions: five PROBE
lines, at least one with trades > 0.

<expected_criteria>DQ1-t1-AC1,DQ1-t1-AC2</expected_criteria>

Run each invocation from the worktree root. Both FAIL at the base: `LOCK-BAD no file ...`, `SEAM-BAD rc=127 probe_lines=0`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no vendor call (no Yahoo, no Bloomberg), no deploy.** Read-only S3 reads for the probe only.
- **No client data in any committed file:** tests use synthetic frames; the probe prints counts and identifiers only.
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-W1-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file
  below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/lock.py
data/mdpf/scripts/demque/test_demque_lock.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 1, the thread), cell `DQ-t-1`.
<owned_cells>DQ-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ1-t1-AC1, DQ1-t1-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~1/MDPF_DEMQUE.TO-DQ-t1.identity-lock-against-trade-prices.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ1-t1-AC1,DQ1-t1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE read-only S3 reads by the dell1 agent user (the same reads MDPF_SECHIST's R2 intake made on dell1).
comp-adversary: DECLARED-NOT-APPLICABLE thread round.
risk: LOCAL -- code and tests; read-only probe.
direct_act: false -- a worker order.
</preflight>

Source: PRD v0.2 FWD-1, C-IDENTITY; dell2 research s.1 (lock rule); decomposition round 1.
