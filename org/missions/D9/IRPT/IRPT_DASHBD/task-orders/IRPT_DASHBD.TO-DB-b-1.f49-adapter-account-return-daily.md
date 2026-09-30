# TO IRPT_DASHBD.TO-DB-b-1 -- The 49 Financial reporting adapter: Schwab silver -> gold `account_return_daily` under its contract, with the guard and the measured method row

<to_id>IRPT_DASHBD.TO-DB-b-1</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.4.0_DS_ClientPlatform~S</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** PRD `org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md` @84cff9014b section 2
hop 1, CONTRACTS C-TIERS, C-SHAPE, C-COVERAGE (as superseded by ADDENDUM ruling 12), C-ADAPTERS, C-METHOD, C-GUARD, C-VALUE, C-FEERAIL,
C-NAMES, C-SOURCES; rulings 6.1-6.5; ADDENDUM v0.2 rulings 12-13; CTO 103260 | **Decomp cell:** `DB-b-1` (decomposition section 1) |
**outcome_ref:** FWD-1 (hop 1), FWD-8, FWD-9 | **depends_on:** none

---

## WORKER FACE

**The cell.** Build the 49 Financial adapter as a DS-lane gold script beside IRPT_BCKEND's holdings producer and emit the first Opal-shape
reporting gold, `account_return_daily`, for the round-1 sample over its full history, under a written contract, with the guard applied.

**Where things are (read them; every path is repo-relative from your worktree root).**
- The pattern to follow: `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` (its docstring is the method it
  fixes; `sources.json` beside it declares the custody source `schwab_08335338` -- bucket `opal-data-assets`, prefixes
  `schwab/08335338/silver/dim_position/` and `.../dim_balance/`, identifier/date/value/price/quantity columns and the cash carrier;
  the firm scope is `lookup(registry_key)['firm']`, never a typed token; the trading-day axis is `lib/trading_calendar.py`).
- Your new script: `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` + `data/assets/scripts/gold/irpt_reporting/sources.json`
  (declare `schwab_08335338` with the same fields PLUS `transactions_prefix` `schwab/08335338/silver/fact_trn/`). Same CLI shape as the
  holdings producer: `--source schwab_08335338`, `--start/--end` or `--date`, `--accounts` (a QA thread), `--dry-run`/`--upload`.
- Silver you read (all under `opal-data-assets`, partition `date=YYYY-MM-DD/data.parquet`, register
  `docs/briefs/irpt-holdings-basis-silver-inventory-brief-20260928.md:75-97`): `dim_position` (positions with `closing_price`,
  `market_value_settled_unsettled`, 559 partitions from 2024-07-08), `dim_balance` (`net_mv_plus_cash` = the whole-account value
  incl. cash, the C-VALUE carrier), `fact_trn` (about 130 columns; the money column is `gross_amount` signed by `debit_credit` on
  CASH rows, `tr_cd == FC`; `net_amount` is $0.00 on 1.9M cash rows and must never be read -- `data/assets/scripts/gold/runners_49f/c00_flow_ledger.py`
  docstring, the MONEY LAW and the IC TRAP).
- The classification table AS DATA: `org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`
  (187 rows keyed `tran_srcde, tr_cd, sb_cd` with `category`, `rule`, `partition`; loaded by
  `data/assets/scripts/gold/runners_49f/a05_ref_txn_classification.py:load_table`, which you may call or reproduce; the flow classes
  EXTERNAL / INTERNAL / FEE-MANAGEMENT / FEE-ADMIN / UNRESOLVED and the pair-match rule are `c00_flow_ledger.py`'s, read as data).
  PRD ruling 6.4: NO import of `c02_twr_engine.py`; the retiring engine's arithmetic is prior art, not a module.
- The guard rail (C-GUARD): IRPT_BCKEND's gold `holdings_performance_daily` at
  `address("irpt","49financial","gold","holdings_performance_daily","date=<D>")` + `/data.parquet`, columns `account_id, business_date,
  daily_return, account_value, excluded_count, excluded_weight, status, leveraged, negative_value, held_count`; the price-only daily return
  is `daily_return` where `status == OK`.
- Every address from `lib/opal_naming.address()`, every name from `name()`; at the cut they answered (printed in the decomposition):
  `address("irpt","49financial","gold","account_return_daily","date=2026-09-29")` ->
  `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=2026-09-29`;
  `address("irpt","49financial","gold","dim_return_method","method_version=1")` -> `.../gold/dim_return_method/method_version=1`.
  A builder refusal is a registry row to add, never a hand-typed key.

**The method you implement (C-METHOD, verbatim in scope; the PRD is the authority, this is its operative reading).**
- Daily valuation of the whole account: `V_t` = `dim_balance.net_mv_plus_cash` on trading day t (C-VALUE). Verify per account that
  `V` contains cash: on the first sample day, `V_t - sum(dim_position market value)` equals the balance table's cash line (record it).
- `r_t = (V_t - F_t) / V_(t-1) - 1`, `F_t` = the net EXTERNAL flow (capital-in positive, capital-out negative) from `fact_trn`
  rows whose class is EXTERNAL under the code table and the pair-match rule (a CASH leg matched on (business_date, |gross|) across
  DIFFERENT accounts with opposite `debit_credit` is INTERNAL; unmatched is EXTERNAL by default). Flows at END of day
  (`flow_convention END`; DB-b-3 measures START/END/MIDPOINT and may move it).
  **THE SKIPPED-DAY RULE (row IRPT_BCKEND-S237, `0.4.0_DS_ClientPlatform~S` @58a8c9e489, read at the cut):** the trading calendar is
  the PERFORMANCE axis, but the custodian's book moves on bank days the calendar skips (2025-01-09, an NYSE closure, carried a
  $1,125,000 deposit that the retiring engine read as +56.10% on 01-10 because it summed flows at `date=D` only). So `F_t` is the sum of
  EXTERNAL flows over EVERY custodian partition day strictly after the prior VALUATION day t-1 up to and including t (the flows of a
  skipped day belong to the next performance day, never to no day), and `income_received` is summed the same way. Record the count of
  such carried days per account in the deliverable. The guard would only FLAG this shape (FLOW_UNRECONCILED); this rule COMPUTES it.
- Income (`income_received`) is recognised on CASH RECEIPT: the code table's income categories (dividends, interest, coupons) on
  `tr_cd == FC` rows; reinvested dividends count once (the reinvestment purchase is INTERNAL); Schwab bank-sweep interest counts only
  where the code is clearly classified interest, the rest is UNRESOLVED and not income (ruling 6.5); foreign-tax `WD` is withholding,
  not a withdrawal. `income_return = income_received / V_(t-1)`.
- Corporate actions (RO/IC/JR lanes) are their own class: neither flow nor income. In-kind transfers valued at quantity x same-day
  close; an unpriced leg sets `day_quality FLOW_UNRECONCILED` rather than a zero-buried flow.
- The guard (C-GUARD), every day: `holdings_price_return` = the holdings gold's `daily_return` for (account, day) where its status is OK
  (null with `holdings_price_return_reason` otherwise). If `|r_t - (holdings_price_return + income_return)| > tolerance` the day is
  `day_quality FLOW_UNRECONCILED`, `total_return_daily = holdings_price_return + income_return`, `return_basis HOLDINGS_INCOME_FALLBACK`.
  `|F_t| / V_(t-1) > large_flow_share` marks `day_quality LARGE_FLOW` (the value still enters). `V_(t-1) <= 0`, or `r_t` outside the
  plausibility band, is `day_quality NOT_MEASURABLE`, `return_basis NOT_MEASURABLE`, `total_return_daily` null (the link breaks with a
  stated gap; nothing compounds). Otherwise `day_quality MEASURED`, `return_basis TWR`.
- THE THREE NUMBERS ARE MEASURED, NOT INVENTED (C-GUARD, ruling 6.2): compute the distribution of `|r_t - (price + income)|`, of
  `|F_t| / V_(t-1)` and of `r_t` over the five sample accounts' full history with a first pass; set `tolerance` at the 99th
  percentile of the reconciled-day differences (state the value and the percentile), `large_flow_share` at the 99th percentile of
  the flow share, the plausibility band at [-0.5, +0.5] daily unless the data's own p99.9 says otherwise (state it); write the
  three into `dim_return_method` and the method contract with the distribution figures beside them.
- GROSS of advisory fees: `fee_amount` null with `fee_amount_reason FEE_RAIL_UNUSED`; `fee_basis GROSS_ONLY` (C-FEERAIL). No net return.
- `dim_return_method` (one partition `method_version=1`, one row): `method_version 1`, `method TWR_DAILY_GEOMETRIC`, `flow_convention END`,
  `income_basis cash_when_received`, `fee_basis GROSS_ONLY`, `tolerance`, `large_flow_share`, `plausibility_band_low/high`,
  `day_count Account365`, `tieout_tolerance_proposed` null (DB-b-3 fills it), `gips_alignment "GIPS-aligned, not GIPS-compliant"`.

**The contract files (C-SHAPE, annex 17c, ADDENDUM ruling 12), written BEFORE the first upload:**
- `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`: `contract_version "0.1.0"`, `project`, `prd`, `table`,
  `grain "account x trading day"`, `partition "date=YYYY-MM-DD"`, `columns` (list of `{name, type, nullable, meaning}` with the pyarrow
  type name exactly as written -- e.g. `string`, `date32[day]`, `double`, `int64`): `firm`, `account_id`, `business_date`,
  `market_value_eod`, `external_flow`, `income_received`, `income_return`, `total_return_daily`, `return_basis`, `holdings_price_return`,
  `holdings_price_return_reason`, `fee_amount`, `fee_amount_reason`, `day_quality`, `history_scope`, `method_version`, `schema_version`;
  `enums`: `history_scope [FULL, PARTIAL_HISTORY]`, `day_quality [MEASURED, FLOW_UNRECONCILED, LARGE_FLOW, NOT_MEASURABLE, SOURCE_LAG]`,
  `return_basis [TWR, HOLDINGS_INCOME_FALLBACK, NOT_MEASURABLE]`, `fee_amount_reason [FEE_RAIL_UNUSED]`, `holdings_price_return_reason
  [NO_HOLDINGS_ROW, HOLDINGS_NOT_OK]`; `rule24_record` (the four postulates + a word-boundary token census of each enum value over
  `data/`, `infra/aws/lambda`, `portal/src`, run with the Grep tool or `comp-find`, denominators printed); `schema_hash` = sha256 over the
  sorted `"name:type"` lines joined by newline (the check recomputes it). A firm-specific column is a violation; no `sb_cd`, no Schwab
  code survives into the table.
- `org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json`: same header shape; `columns` as the row above (`method_version int64`,
  `tolerance double`, `large_flow_share double`, `plausibility_band_low/high double`, `flow_convention string`, `income_basis string`,
  `fee_basis string`, `day_count string`, `tieout_tolerance_proposed double` nullable, `gips_alignment string`, `measured_at string`);
  `method_versions: [ {the version-1 values with the measured distribution figures} ]`; `schema_hash` likewise.
- NO policy row for the gold tables (ISSUER AMENDMENT 2, 2026-09-30 ~18:1xZ, on 1.0.0_SA_CTO RULING 103361 = PRD v0.3 addendum
  ruling 16 @c812be9885, answering the seat's row IRPT_DASHBD-S1 @85863e9b5a): `infra/logic/registry/reporting_policies.json` records
  retention of client-facing state and platinum artifacts, not an internal parquet table; rule 30 holds for the gold tables on
  `address()` and `name()` output alone. The policy file is NOT edited by this cell (the platinum rows are DB-b-2's).

**The emit (ISSUER AMENDMENT 1, 2026-09-30 ~17:1xZ, on the seat's message 103331: the five roster accounts are 2026 TaxSMA books,
first positive value 2026-03-16 .. 2026-07-08).** The sample is SIX accounts: the five roster accounts (from
`s3://opal-data-assets/blackdiamond/49f/_ops/taxsma_roster.json`, field `schwab_account`, `status active`; they are the tie-out sample
DB-b-3 needs) PLUS ONE THREAD ACCOUNT chosen by census -- the 49 Financial account with the MOST days of positive `net_mv_plus_cash`
across the 560 `dim_balance` partitions that also carries `fact_trn` rows (print the top five candidates with their day counts and pick
the first; a tie is broken by the larger last-day value). Record it as `{"thread_account": "<id>", "census": [...]}` in
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.4.0_DS_ClientPlatform~S/THREAD_ACCOUNT.json` BEFORE the emit; every round-1 check reads
the thread account from that file. Emit `--accounts <the six> --upload` over every trading day from 2024-07-09 to the frontier, writing
`date=<D>/data.parquet` under the builder's address with ONLY those accounts' rows (a QA thread; the all-accounts scheduled run is round
2). A day BEFORE an account's first positive value is NOT emitted (no row; the account's rows carry `history_scope PARTIAL_HISTORY` and
the manifest will carry `first_data_date`); `NOT_MEASURABLE` is for a day INSIDE the book that cannot be measured, never for a day before
the book exists. The three guard numbers are measured over days that can carry a real return, denominators printed (the seat's default,
accepted). No gate limb graded this modification (the L6 gate grades new orders); the CTO reads it at the round-1 analysis. Ledger BEFORE the first upload: `python .tools/deploy_ledger.py open --slug irpt-dashbd-account-return-daily-49f-r1-20260930
--title "<one line>" --author 0.4.0_DS_ClientPlatform~S --leg "C1|verify|the two contract files|both written with schema_hash and the rule-24 record"
--leg "M1|verify|the three guard numbers measured|distribution figures recorded in dim_return_method"
--leg "W1|activation|gold written for the 6 sample accounts, full history|partition count, first/last date, schema hash == contract"`;
`close-leg` each with its proof; `close`. Commit the entry AND the sentinel `org/critical_paths/.open_deploys/irpt-dashbd-account-return-daily-49f-r1-20260930.json`.

<criterion id="DB-1-AC1" cell_refs="DB-b-1"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_1_ac1_gold_under_contract.py" .</invocation><expect>DB-1-AC1 PASS</expect></criterion>
`DB-1-AC1` -- both contract files exist with a recomputable `schema_hash` and the rule-24 record; the naming builder loads the registry
(amendment 2 removed the gold policy-file half, ruling 16); >= 250 date partitions exist at the builder's address, five sampled partitions hash to the contract and
carry the thread account; `dim_return_method/method_version=1` has one row with every method column non-null. Base: FAIL (no contract).

<criterion id="DB-1-AC2" cell_refs="DB-b-1"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_1_ac2_guard_seam.py" .</invocation><expect>DB-1-AC2 PASS</expect></criterion>
`DB-1-AC2` -- the seam against the REAL neighbour: over 40 sampled partitions, `holdings_price_return` equals IRPT_BCKEND's gold
`daily_return` per (account, day) where that row is OK; MEASURED days sit within the tolerance and carry a positive `market_value_eod`;
FLOW_UNRECONCILED days carry `HOLDINGS_INCOME_FALLBACK`. Base: FAIL (no gold).

<criterion id="DB-1-AC3" cell_refs="DB-b-1"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_ledger_closed.py" . irpt-dashbd-account-return-daily-49f-r1-20260930 DB-1-AC3</invocation><expect>DB-1-AC3 PASS</expect></criterion>
`DB-1-AC3` -- the ledger entry is CLOSED with every leg proven and no sentinel. Base: FAIL (no entry).

<expected_criteria>DB-1-AC1,DB-1-AC2,DB-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **AWS writes admitted:** objects under `irpt/49financial/gold/account_return_daily/` and `irpt/49financial/gold/dim_return_method/`
  in `opal-data-49financial` only. No other prefix, no other bucket, no Terraform, no Lambda.
- **No vendor call of any kind** (C-TIEOUT; Andrew's per-use word is absent and not asked here).
- **Refusal clause.** A method question the PRD does not answer is a surprise row (`IRPT_DASHBD-S<k>`, the project's channel), with the
  default you took stated; a builder or validator refusal stops that limb only. Never weaken a check.

<paths>
data/assets/scripts/gold/irpt_reporting/
data/assets/scripts/gold/irpt_holdings_performance/
data/assets/scripts/gold/runners_49f/a05_ref_txn_classification.py
data/assets/scripts/gold/runners_49f/c00_flow_ledger.py
data/assets/scripts/lib/stream_parquet.py
org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json
org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json
org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json
lib/opal_naming.py
lib/trading_calendar.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-dashbd-account-return-daily-49f-r1-20260930.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 1 (round 1, workstream B), cell `DB-b-1`.
<owned_cells>DB-b-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB-1-AC1, DB-1-AC2, DB-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.4.0_DS_ClientPlatform~S/IRPT_DASHBD.TO-DB-b-1.f49-adapter-account-return-daily.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB-1-AC1 DB-1-AC2 DB-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO~P` (one message, under 150 words): the commit hashes, each criterion's last line, the three measured numbers,
the partition count and the C-VALUE cash verification, and any surprise row id. Say "gold landed" in the subject: that is the GO for
the publisher's worker.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in round 1 (the adapter's scheduled fire is a round-2 cell under its own ledger, as IB-er-203 followed IB-er-202).
comp-iam: DECLARED-NOT-APPLICABLE -- the DS seat writes with its own credentials to the firm bucket; no role changes.
comp-blast: RUN -- a NEW gold table and a NEW dim in the 49F bucket; 0 existing readers (comp-estate: 0 of 135 chains name account_return_daily).
comp-routes: DECLARED-NOT-APPLICABLE -- no route.
comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- DB-1-AC1 base FAIL (no contract); DB-1-AC2 base FAIL (no gold); DB-1-AC3 base FAIL (no entry); the ledger checker's positive control on the CLOSED W24 entry PASS.
seating: 0.4.0_DS_ClientPlatform~S holds no other project (TO-IB-pr-263 superseded @ed0be5b557); Andrew's seating of 2.0.0_SA_COO~P on this backend is PRD section 5.
lane: the <paths> block IS the grant; the policy file is named so a refusal there is a row, not a wall.
</preflight>
