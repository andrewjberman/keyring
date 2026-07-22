# Canonical Total-Return Account-Performance mechanism -- design proposal (Andrew-direct, 2026-07-21)

**By:** 2.0.0_SA_COO~A (read-only analysis + proposal; grounded in the 13-script dataflow trace @wf_6aec2ebf-646 + the Schwab silver fact tables). Not a build -- a proposal + field selection for CTO/DS to ratify.

## 1. Current state -- account performance was NOT designed as a total-return engine (confirmed)
Today's chain is `c00_account_gains -> c01_account_performance`. It is an **AUA-decomposition retrofitted into returns**, with these load-bearing defects (line-cited from source):
- **`market_growth` is a RESIDUAL PLUG** (`c00:113`: `d_aua - nna_total - income + fees_tax`). The biggest return component is not measured -- every misclassified/missing/mis-signed flow is absorbed into "growth." The identity assert is therefore tautological (`c00:145`).
- **Income = only `{DV,IN}`; fees = `{FE,WH,WD}`** (`c00:44`). Lumping **`WD` (a withdrawal = external flow)** with fees distorts both NNA and the return. No coupon/accrual concept.
- **Net-of-advisory-fee is impossible today**: the advisory fee + role weights are joined at a00 but **dropped before output** and never reach c01 (`c01:46` break; `a00` metatable-join drops all `*_split_pct`/`annual_fee_*` cols).
- **`total_return = d_aua/bmv` INCLUDES external flows** (`c01`) -- not a return; negative/near-zero BMV -> sign-inverted, uncapped compounding (`c01:114,141`); annualized on **calendar days** (`c01:118`).
- **Valuation = positions only** (`market_value_settled_unsettled`); cash-inclusion unverified; empty-position partition -> `d_aua = -bmv` absorbed into growth (`c00_runner` LOW break).

## 2. Design principles (fix the architecture, not the patches)
1. **Separate the three things the current design conflates:** (a) VALUATION (total account value = securities + cash), (b) CASH-FLOW CLASSIFICATION (every txn cleanly bucketed), (c) RETURN COMPUTATION.
2. **MEASURE market P&L, do not plug it.** Compute from lots/price-deltas; use the accounting identity as a *reconciliation guardrail*, not the definition of growth.
3. **Time-Weighted Return (TWR)**, daily-valued + geometrically linked -- the standard for advisor performance (removes external-flow timing distortion). Modified-Dietz day-weighting for the flow denominator.
4. **Gross AND net, both linked.** Gross = before advisory fee; Net = after advisory fee. Income is IN the return (internal); external flows are OUT.
5. **A methodology CONTRACT** (`dim_return_method`) pins the choices so the served number is reproducible + never-widen (a method change is a ratified edit, not a silent drift). This is the "performance_dim" you intuited.

## 3. Proposed tables

### 3a. `fact_account_return` -- daily-atomic, grain = (account_id, date)
| Field | Meaning |
|---|---|
| account_id, date, prev_date | key + prior valuation date |
| **bmv, emv** | beginning/ending TOTAL account value (securities + cash) |
| bmv_securities, bmv_cash, emv_securities, emv_cash | the split (cash-inclusion explicit + auditable) |
| **external_flow** | net client money movement (EXCLUDED from return): = flow_cash + flow_in_kind |
| flow_cash, flow_in_kind | cash flows (FI/FO/WD-cash/TA-cash) + valued security transfers (TA legs) |
| **income_dividend** | DV (equity dividends) |
| **income_interest** | IN on cash/MM assets |
| **income_coupon** | IN on fixed-income assets (asset-class split via dim_asset) |
| income_other, income_total | securities-lending etc.; sum |
| **fee_advisory** | accrued daily from the fee schedule (the gross<->net differentiator) |
| **fee_transaction** | commission + prime_broker_fee + trade_away_fee + redemption_fee + step_in_fee + research_fee + other_fee + debit |
| **tax_withholding** | WH (kept SEPARATE from fees) |
| **market_pnl** | MEASURED price P&L = realized (fact_lot_realized) + delta-unrealized (fact_lot_unrealized) + held-position price deltas |
| recon_residual | (emv-bmv) - (external_flow + income_total - fee_transaction - tax_withholding + market_pnl); ~0 = clean, else FLAG (replaces the growth-plug) |
| **total_return_gross** | (market_pnl + income_total - fee_transaction - tax_withholding) / bmv_adj |
| **total_return_net** | gross numerator - fee_advisory, / bmv_adj |
| cum_factor_gross, cum_factor_net | daily geometric link of BOTH |
| bmv_adj | Modified-Dietz denominator (bmv + day-weighted flows) |
| row_quality flags | valuation_complete, recon_within_tol, has_flow, negative_bmv (excluded not inverted), return_capped (winsorized) |

### 3b. `dim_return_method` -- the methodology contract ("performance_dim")
One canonical, ratified row pinning: return_method=`daily-TWR-geometric`; flow_timing=`modified-dietz-dayweight`; income_basis=`cash-when-received`; coupon_source=`IN x asset_class=fixed_income`; gross_def=`pre-advisory-fee`; net_def=`post-all-fees`; fee_advisory_source=`accrued-from-schedule`; annualization=`trading-day (252)`; winsor_cap=`<declared>`; cash_inclusion=`total-account`. A method change = an attributable ratified edit (never-widen at the performance layer).

### 3c. `fact_account_return_windowed` -- geometric link of daily gross+net over MTD/QTD/YTD/1Y/ITD per (account_id, period). Client/firm rollups re-link from the account daily series (never average account returns).

## 4. Field selection -> Schwab source mapping (all present in silver)
| Proposed field | Schwab silver source |
|---|---|
| bmv/emv securities | `fact_position.market_value_settled_unsettled` (prior EOD / EOD) |
| bmv/emv cash | `fact_position` cash sub-position (`quantity_cash`) -- **CONFIRM sweep/MM fully captured** |
| external_flow (cash) | `fact_transaction` sb_cd in {FI,FO} + WD + TA-cash legs x gross_amount x debit_credit |
| flow_in_kind | `fact_transaction` TA security legs (qty!=0), valued row-price-else-close |
| income_dividend | `fact_transaction` sb_cd=DV (cross-check `fact_tax_1099div`) |
| income_interest / income_coupon | `fact_transaction` sb_cd=IN, split by `dim_asset.asset_class` |
| fee_advisory | `dim_advisor_fee` (annual_fee_bps/flat_fee/fee_basis) -> ACCRUE daily; reconcile vs billed FE txns |
| fee_transaction | `fact_transaction` {commission, prime_broker_fee, trade_away_fee, redemption_fee, step_in_fee, research_fee, other_fee, debit} (all preserved, non-reductive) |
| tax_withholding | `fact_transaction` sb_cd=WH |
| market_pnl | `fact_lot_realized` (proceeds-cost/gain-loss) + `fact_lot_unrealized` (delta cost_basis-vs-MV) + position price deltas |

## 5. The classification corrections (vs today)
- **`WD` -> external_flow** (not fees_tax). A withdrawal is client money out, like FO.
- **Income split** dividend | interest | **coupon** (asset-class join), not `DV+IN` lumped.
- **`WH` withholding kept separate** from advisory/transaction fees (it is a tax, not a fee).
- **fee_advisory accrued daily** from the schedule (smooth), reconciled against lumpy billed `FE` transactions -- enables a true daily NET return.
- **market_pnl measured** from lots -> `recon_residual` becomes a data-quality guardrail, not the growth definition.

## 6. Open confirmations before build (route to CTO/DS)
1. **Cash completeness:** does Sum(`fact_position.market_value_settled_unsettled`) include the uninvested sweep/MM cash, or is a separate cash-balance source needed? (Total-return correctness hinges on this.)
2. **Coupon coding:** is bond coupon interest under `IN` (needs the asset-class split) or a distinct sb_cd?
3. **Advisory-fee basis:** accrue on `Total Value` per `fee_basis`, daily -- confirm the annualization (365 vs 252) + billed-vs-accrued reconciliation cadence.
4. **Gross convention:** confirm transaction costs + withholding live in BOTH gross and net (portfolio-inherent), advisory fee is the sole gross->net delta.

## 7. How it plugs into the runner
`fact_account_return` **supersedes** the c00-residual + c01-return conflation: c00's clean parts (valuation, flow/income/fee classification) feed it; market_pnl comes from the lot facts (new); c01's window/geometric-link machinery is reused but on gross+net measured returns; c02 client rollup re-links from the account daily series. The advisory-fee half the metatable drops at a00 must be wired through (the `c01:46` break) for net return. Group D reads gross+net + income breakdown from this one canonical layer.

**One-line:** measure market P&L instead of plugging it, classify WD/coupon/withholding correctly, wire the advisory fee through for net, value the whole account incl. cash, and pin the method in a contract -- and the served number becomes a defensible total return, gross and net, instead of an AUA residual.

---

## 8. REAL-DATA GROUNDING (2026-07-21) -- confirms resolved + classification CORRECTED
Sampled live partitions: dim_position/dim_transaction date=2026-07-20 (6,010 accts, $1.694B AUA); fact_lot_realized/unrealized + dim_asset (07-14). Findings REVISE section 5.

**Confirm #1 CASH -- RESOLVED (captured, one caveat).** Sum(`market_value_settled_unsettled`)=$1.694B includes cash: money-market sweep funds (SWGXX/SNVXX/SNSXX) + blank-cusip cash lines ($21.6M). `accounting_rule_code` tags every row CASH/MARGIN/SHORT. **CAVEAT:** `FC` "BANK SWEEP FR/TO BROKERAGE" rows show cash sweeping to Schwab Bank -- confirm the bank-side balance is in the RPS position file, not a separate feed, else a slice of cash is off-statement.

**Confirm #2 CLASSIFICATION -- the current {DV,IN}/{FE,WH,WD} taxonomy is INCOMPLETE + partly WRONG.** Decoded the real `sb_cd` x `transaction_detail_description`/`transaction_source_code_description`:
| sb_cd | n | what it REALLY is | correct bucket | current runner |
|---|---|---|---|---|
| TR | 630 | trades (buys/sells) | internal-trade | ok (ignored) |
| **FC** | **549** | BANK SWEEP fr/to brokerage (net-0, internal) + **BANK INTEREST (income)** + cash-in-lieu | split: sweep=internal / **bank-int=INCOME** | **UNHANDLED -> bank interest MISSED** |
| DV | 75 | cash dividends | income_dividend | ok |
| FI | 34 | deposits (employer contrib, rollover, MoneyLink) | external_flow_in | ok |
| TA | 32 | security transfers (account transfer) | flow_in_kind | ok |
| **RD** | **24** | **REINVESTED DIVIDEND** | **income_dividend** | **MISSED (income={DV,IN})** |
| FO | 21 | withdrawals (client request, Tfr to bank) | external_flow_out | ok |
| **JR** | 20 | journal / transfer between Schwab accts | flow (ambiguous) | **UNHANDLED** |
| FE | 11 | ADR mgmt fee | fee_transaction | ok |
| **WD** | 6 | **FOREIGN TAX PAID** (NOT a withdrawal) | tax_withholding | mislabeled "withdrawal" but tax-bucket is defensible |
| **RO** | 5 | redemption/conversion/split (e.g. a CALLED bond) | corporate-action | **UNHANDLED** |
| **IC** | 4 | conversion / shares-received-in | corporate-action (in-kind) | **UNHANDLED** |
| IN | 3 | credit/bank interest (incl. a called-bond final coupon) | income_interest/coupon | ok |
| WH | 3 | fed income tax withheld | tax_withholding | ok |
**Corrections to section 5:** (a) my "WD -> external_flow" was WRONG -- WD is FOREIGN TAX; **FO** is the real withdrawal. (b) income MUST add **RD** (reinvested dividends) + **bank interest inside FC** -- `{DV,IN}` alone understates income. (c) **classify from the DESCRIPTIONS + asset_class, not the 2-letter sb_cd** -- the codes are lossy (FC and JR each mix internal-sweep with real income/flow). (d) FC bank-sweep (net-0) must be recognized-and-excluded explicitly, not ignored by omission.

**Coupon:** no distinct code -- it is interest (`IN`, and bank-int in `FC`) on `dim_asset.asset_class='DEBT'` (132 debt securities in the sample). `lot_unrealized.accrued_interest` and `yield` are **empty (0 nonzero)** -> coupon is **CASH-BASIS only** (drop the accrual option from section 2).

**Measured market_pnl -- CONFIRMED feasible.** `fact_lot_realized.gain_loss_dollars` (+ `proceeds`, `cost_basis`, `disallowed_loss`, `federal_tax`/`state_tax`/`wh`) and `fact_lot_unrealized.unrealized` (+ `cost_basis`, `current_market`, `adjusted_cost`) give realized + unrealized P&L directly. **market_pnl = Sum(lot_realized.gain_loss_dollars for lots closed) + Delta Sum(lot_unrealized.unrealized)** -- a measured component, no residual plug. (Note: lots are keyed `lot_uid`/`lot_seq`; realized carries `close_event_id` for day attribution.)

**Net effect on the design:** section 3a's income fields become `income_dividend` = DV+RD, `income_interest` = IN(cash) + FC-bank-int, `income_coupon` = IN/FC-int where asset_class=DEBT; add a `corporate_action` handling lane (RO/IC/JR) so a called bond or share conversion is not silently a flow or a growth-plug; `tax_withholding` = WH+WD; `external_flow` = FI(in) + FO(out) + TA(in-kind), NOT WD. Everything else stands.

## 9. Convergence with the BD dashboard teardown (0.4.0_DS_ClientPlatform~Z, @efdb4dbd8) -- CORROBORATION + 3 refinements
~Z tore down the Black Diamond (Cottonwood tenant) dashboard toward REPLACING BD, and it independently VALIDATES this Schwab-native design (their `docs/research/bd_dashboard_teardown/`). Treat the BD-sourced items as ~Z-research to VERIFY against our ingested cot-BD feed, not yet fact -- but the direction is strongly corroborating:
- **BD's `performance/performancePeriod` endpoint IS a `fact_account_return`** -- TWR + money-weighted, net-of-fee, accrued MV, benchmark-relative, return-contribution attribution, Portfolio->Class->Segment->Account grain (~Z sec 4.1 maps BD fields -> our Schwab silver).
- **BD's transaction "affect vector"** (fileCode -> tuple `externalFlow/income/cash/unit/advisorFee/accrual`, e.g. "Cash Withdrawal (-1,0,0,0,0,-1)") **is the exact classification taxonomy section 8 reconstructed from descriptions.** Since we ingest the cot-BD feed, we can **lift BD's crosswalk as the classification source AND use it as the parity ORACLE** for our Schwab-native classifier -- the single highest-value fold (it de-risks the section-8 FC/RD/JR/RO/IC gaps).
- **BD's firm/globalsettings = `dim_return_method` verbatim** (Account365 / NetOfFees / Accrued / ClassSpecific), and it PRE-ANSWERS 3 of the 4 open confirms: cash first-class (confirm 1), fee-accrual basis = 365 (confirm 3), advisory fee = sole gross->net delta (confirm 4). **Only coupon coding on Schwab silver (confirm 2) remains** -- plus my bank-sweep-cash caveat (verify against our own position feed, not BD's word).

**3 refinements to fold into `fact_account_return` v0** (each stands on its own merit):
1. **Money-weighted return (MWR/Modified-Dietz) ALONGSIDE TWR** -- add `mwr_gross`/`mwr_net`; TWR for performance-reporting, MWR for the client's actual dollar experience.
2. **Return-contribution attribution up the grain tree** (account -> segment/class -> portfolio) -- a `contribution` field so "what drove the return" rolls up, not just the return level.
3. **Performing-vs-position-only BMV/EMV split** -- accounts without transaction history are EXCLUDED from the performance denominator (not sign-inverted) -- this cleanly resolves the c01:114 negative/zero-BMV defect via a `is_performing` gate rather than an abs() hack.
