# TO ADVI_COTBKF.TO-CB-bq-3.close-vs-trade-scan -- round 69 CB-bq-3: every security's close against its traded price: how many series are mis-scaled or stepped

<to_id>ADVI_COTBKF.TO-CB-bq-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~108</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>69</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bq-3` (`decompositions/ADVI_COTBKF_DECOMP.round69.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT. You change no code.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_69_20261011.md` section 2 item 4; the round-68 record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~105/OUTLIERS_ON_A_REAL_BASE.json` and its `.md` (classes 8 and 9:
one security sold at a price 20.2 times away from the store's close, and one whose whole close series sits about 6.6 times below its
traded price on all four trades checked); `data/assets/scripts/silver/commonwealth_daily_valuation.py` (`as_traded_store`,
`split_plan`, `apply_splits`).

**Why.** A store with one known wrong series and no scan is a store with an unknown number of them.

**Your item.**

1. **The two series to compare, per security and date.** The build's close: `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet` (columns
   cusip, date, price, store; the served run's table). The traded price: from the silver transactions cache
   `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/trade_year=*/*.parquet` (read its schema), `abs(Amount) / abs(Quantity)` on buy and sell rows of that CUSIP
   with a non-zero quantity and amount, one price per (cusip, date) as the quantity-weighted mean; say which transaction types you
   took as trades and why, and drop fixed income and options or report them separately (their unit is not a share price).
2. **The ratio** close / traded price for every (cusip, date) that has both. Print the denominator: securities with at least one
   comparable date, and comparable (cusip, date) pairs.
3. **Class every security** by its ratios: `AGREES` (median within 2 percent of 1 and no date beyond 10 percent), `CONSTANT_SCALE`
   (the ratio is stable, within 5 percent of its own median, and that median is beyond 10 percent from 1: the whole series is
   mis-scaled), `STEP` (the ratio is about 1 on one side of a date and a stable other value on the other: an adjustment applied or
   missed at an event), `ISOLATED` (one or two dates beyond 10 percent, the rest agree: a bad print or a bad trade row), `NOISY`
   (none of these), `TOO_FEW` (fewer than 3 comparable dates). For CONSTANT_SCALE and STEP: the factor, the date span, and how many
   of the security's priced holding-days sit on the wrong side.
4. **Reach.** For each CONSTANT_SCALE and STEP security: account-days that hold it while it is priced, and how many of those are
   MEASURED days in `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/daily_returns.parquet` (counts only).
5. Confirm the two known cases appear (the round-68 record names them by ticker in its `.md`), and say which class each falls in.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~108/CLOSE_VS_TRADE_SCAN.json` and a `.csv` beside it listing every CONSTANT_SCALE and STEP security (cusip, ticker, class, factor,
   first_date, last_date, comparable_dates, holding_days_affected, measured_account_days_affected; no account column). Top-level
   keys, exactly: `securities_compared`, `pairs_compared`, `classes` (each of the six names with its count), `constant_scale` and
   `step` (lists), `known_cases` (a list of `{"ticker", "found", "class", "factor"}`), `measured_account_days_affected`,
   `not_established`.

### ACCEPTANCE

<criterion id="CB69bq3-AC1" cell_refs="CB-bq-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~108/CLOSE_VS_TRADE_SCAN.json',encoding='utf-8'));c=d['classes'];k=d['known_cases'];print('CLOSE-VS-TRADE-SCAN-RECORD securities_compared=%d pairs_compared=%d class_sum=%d constant_scale=%d step=%d isolated=%d known_cases_found=%d/%d measured_account_days_affected=%d'%(d['securities_compared'],d['pairs_compared'],sum(c.values()),c['CONSTANT_SCALE'],c['STEP'],c['ISOLATED'],sum(1 for x in k if x['found']),len(k),d['measured_account_days_affected']))"</invocation><expect>CLOSE-VS-TRADE-SCAN-RECORD securities_compared=</expect></criterion>
`CB69bq3-AC1` -- the scan is recorded with its denominator, its six classes summing to the securities compared, and whether the two
known cases were found. The CTO reads the counts.

<criterion id="CB69bq3-AC2" cell_refs="CB-bq-3" judgment="true"/>
`CB69bq3-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the traded price is a share price for the kinds
compared; the classes follow from the ratios shown; both known cases are found, or the scan says why not; the reach is counted on the
served table.

<expected_criteria>CB69bq3-AC1,CB69bq3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local; no network call.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write.** Read-only S3 gets, heads and listings are allowed where the cell
  says so. No push. No `--refresh`. No vendor call (no Yahoo, no Bloomberg).
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, tickers, a security's price,
  ratios, version ids, ETags and reason codes only. A build log line carrying `read_account=` is never echoed: filter it out.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W108-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round69.md</decomp_doc> (round 69), cell `CB-bq-3`.
<owned_cells>CB-bq-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB69bq3-AC1, CB69bq3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~108/ADVI_COTBKF.TO-CB-bq-3.close-vs-trade-scan.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB69bq3-AC1,CB69bq3-AC2` BEFORE the flip. Mechanical: CB69bq3-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the transaction types taken as trades and the kinds left out; the denominator (securities and pairs compared); the six class counts; each CONSTANT_SCALE and STEP security with its factor, span and reach; the two known cases and their classes; the `CLOSE-VS-TRADE-SCAN-RECORD` line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the two known cases are the positive control: a scan that does not find them is wrong; the denominator is printed; kinds whose unit is not a share price are kept out or separate; TOO_FEW and NOISY are legal classes; BLIND: a security never traded by any account has no traded price and is not compared.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-69 analysis @e0f9682779 (msg 5206), section 3 item 3, and PRD ADDENDUM v0.6 @df488019bf (msg 5217); `3.0.0_SA_CVO` REMEDIATION_v39 @22e2566c22.
