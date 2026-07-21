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
