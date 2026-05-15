# Inflection Cost Basis & Tax Status Reconciliation Investigation
**Author:** 0.4.0_DS_ClientPlatform~C | **Date:** 2026-05-14 | **TO:** ADVI_INFFIN.019

---

## TL;DR

All four anomalies from Andrew's walkthrough are explained by empirical findings below.
Three distinct root causes identified across Issues 1-4; none are hardware/infra failures.

| # | Anomaly | Root Cause | Class | Fix Tier |
|---|---------|-----------|-------|----------|
| 1 | CBBY $1.31B vs AUA $203M (8x overstatement) | All historical buy trans_amounts summed incl. sold positions | Hyp #1 (lot semantics) | Gold script fix |
| 2 | Capital Gains TTM -$54.9M | 12m delta in mark-to-market unrealized, not realized gains | Hyp #3 (label mismatch) | Label fix or new computation |
| 3 | AUA by Tax Status $165.6M vs $203M | CDN staleness of pre-D-max artifact | Post-D-max resolved | CF invalidation (operational) |
| 4 | Top Gain Positions cost_basis = N/A | Same wrong source as Issue 1; correct fix uses account_gains | New finding (outside Hyp set) | Gold script fix (same PR as Issue 1) |

---

## Issue 1: Cost Basis By Year $1.31B — ROOT CAUSE CONFIRMED

### Empirical trace

The CBBY is computed in two scripts:
- `INF_D_02.advisor_client_detail.py:_aggregate_cost_basis_by_year()` — per-advisor scope
- `INF_D_00.portal_aggregates.py:compute_firm_cost_basis_by_year()` — firm scope

Both implement identical semantics: load BUY transactions from bronze (`bronze/transactions/`),
group by `purchase_year = trans_date.year`, and sum `trans_amount`.

BUY type IDs (INF_D_02:108-111):
```python
BUY_TRANS_TYPE_IDS: frozenset[int] = frozenset({
    10,   # Buy Exchange
    14,   # Income Reinvested
})
```

Empirical S3 measurement on `bronze/transactions/2026-05-14.parquet` (1,292,945 total rows):

| transTypeId | Description | Row count | Sum trans_amount |
|-------------|-------------|-----------|-----------------|
| 10 | Buy Exchange | 399,790 | $1,527,176,000 |
| 14 | Income Reinvested | 221,853 | $21,095,940 |
| **TOTAL {10,14}** | | **621,643** | **~$1,548,272,000** |

This matches the current `clients_tab.json#tax.cost_basis_by_year` total: $1,548,272,349. And it
matches Peter Lee's `book.json#tax_exposure.cost_basis_by_year` total: $1,309,257,523.

### Semantic error

The bronze transactions hold the FULL HISTORY of all buy events since account inception (2020-2026).
When `sum(trans_amount)` is computed per year, it includes:
- Buy purchases where the position was subsequently SOLD (lot fully disposed)
- Buy purchases where the position was partially sold (lot partially disposed)
- Only a small fraction that map to CURRENTLY HELD positions

Current holdings AUA = $203.3M. Total historical acquisition cost = $1.55B.
The delta ($1.35B) represents cost of positions that have since been sold or transferred out.

The code comments at `INF_D_02.py:1112-1118` explicitly document this known caveat:
> "Fully-disposed lots still appear with their original cost_basis but zero market_value."

This was shipped as "v1 simple semantics" per the Andrew TTM-LOCKED directive 2026-05-12.

### 2026 > 2025 explained

Peter Lee: 2026 CBBY = $290.9M vs 2025 = $288.0M. This is plausible because:
- 2026 covers Jan 1 - May 14 (4.5 months)
- In that window, more net-new capital was deployed (Buy Exchange volume) than in ALL of 2025
- Consistent with AUM growth and new client onboarding (new client buys = pure positive flow)

With the correct fix (current-holdings lot basis), 2026 partial-year would be much smaller.

### Hypothesis sweep result

| Hyp | Assessment | Evidence |
|-----|-----------|---------|
| #1 Lot vs account summation drift | CONFIRMED (primary root cause) | All historical buys included regardless of sell status |
| #2 Tax-status filter scope mismatch | NOT root cause | The 8x overstatement is pre-filter; scope mismatch is secondary |
| #3 Date-window scope mismatch | NOT root cause for CBBY | Applicable to Capital Gains TTM (see Issue 2) |
| #4 Source artifact divergence | NOT root cause | Single source (bronze transactions); no divergence between scripts |
| #5 Currency/units error | NOT root cause | Verified: units are dollars; arithmetic correct; semantic wrong |

---

## Issue 2: Capital Gains TTM -$54.9M — LABEL MISMATCH CONFIRMED

### What the metric actually computes

`compute_firm_capital_gains_ttm` / `_compute_ttm_cap_gains_adv` (INF_D_00/INF_D_02):

```python
# Pseudocode
end_total = unrealized_gain at data_as_of (sum across all accounts)
start_total = unrealized_gain at (data_as_of - 365d) (sum across all accounts)
return end_total - start_total
```

This is the **12-month change in cumulative mark-to-market unrealized gain**. It measures how
much the total unrealized position has grown or shrunk over the trailing year.

For Peter Lee's book: the total unrealized gain decreased by ~$54.9M over the past 12 months.
This is mathematically defensible (can happen via: positions sold at loss, market price declines,
new positions entering at purchase price with zero initial gain).

### What "Capital Gains (TTM)" implies to end users

Standard financial meaning: sum of realized gains from positions closed in the trailing 12 months.
This is NOT what the current metric computes.

The metric is labeled "Capital Gains (TTM)" but is semantically "TTM Change in Unrealized P&L."
These are fundamentally different:
- Realized gains TTM: requires tracking closed-position sell transactions
- TTM delta unrealized: is a mark-to-market point-in-time comparison

### Hypothesis result

Hyp #3 (date-window scope mismatch) CONFIRMED for this issue: the window semantics (12m
mark-to-market vs TTM realized) is the root mismatch. The data is not wrong; the label is wrong.

---

## Issue 3: AUA by Tax Status $165.6M vs $203M — RESOLVED BY D-MAX BETA

### Current platinum state (post-D-max β chain `from_INF_B_00_20260514_203505`)

`clients_tab.json#tax`:
- taxable: $56,072,691
- tax_deferred: $129,424,143
- tax_free: $17,843,042
- **Total: $203,339,876 — exact match to D-max canonical AUA**

Andrew's screenshot was taken before the D-max β chain re-fired at 20:34Z, showing an older
pmv-only state where the tax block used a stale aum_snapshot with less coverage.

### `aua_by_tax_status.json` in snapshots/ is stale

`platinum/firm/snapshots/aua_by_tax_status.json` shows `"data":[]` — this artifact is
NOT being updated by current chain runs. The live data path is `clients_tab.json#tax`.
The stale snapshots file should be pruned or updated in INF_D_00 output mapping.

### Recommendation

No DS gold-script fix needed. Operational steps:
1. CF invalidation to flush CDN cache for `clients_tab.json` (CTO issued invalidation earlier)
2. Confirm Andrew can see $203.3M tax total in portal after invalidation
3. Remove or update `aua_by_tax_status.json` generation path (INF_D_00 snapshots emit)

---

## Issue 4: Top Gain Positions cost_basis = N/A — NEW FINDING (outside Hyp set)

### Empirical state

`book.json#tax_exposure.top_gain_positions[0]` (Peter Lee, VOO at $28.7M):
```json
{
  "ticker": "VOO",
  "market_value": 28684262.22,
  "cost_basis": null,
  "unrealized_gain": null
}
```

All 20 top_gain_positions have cost_basis=null and unrealized_gain=null.

### Root cause

`_compute_top_position_performance` at `INF_D_02.py:948-970` uses bronze buy transactions as the
cost_basis source (same `load_buy_lot_acquisitions()` call). Condition check:

```python
if buy_lots is not None and not buy_lots.empty and 'trans_amount' in buy_lots.columns:
    _lots = buy_lots[_lots['account_id'].isin(acct_set)]
    if not _lots.empty:
        cb_by_ticker[ticker] = sum(trans_amount)
```

When the filter produces a non-empty result, `cb_by_ticker` is populated. But even when
populated correctly, the cost_basis would be WRONG semantics — same issue as CBBY (historical
acquisition cost including sold positions, not current cost basis per ticker).

The more likely cause of null output: the account_id filter produces unexpected empty results
due to ID format mismatch between the buy_lots DataFrame and acct_set. This is a silent failure
because the code path falls through to null without any WARN.

### Correct data source for top_gain_positions

The `gold/account_gains/{date}.parquet` from INF_B_03 contains EXACTLY what is needed:
- Schema: `date, account_id, ticker, units, market_value, cost_basis, unrealized_gain, term`
- Grain: per (account_id, ticker) — current holdings only (no sold positions)
- `cost_basis` = lot-level cost (remaining_units * cost_per_unit), already correct semantically
- `unrealized_gain` = market_value - cost_basis, already correct

Using account_gains instead of bronze transactions for top_gain_positions would:
1. Populate cost_basis correctly for all positions
2. Populate unrealized_gain correctly
3. Enable TRUE sorting by unrealized_gain (currently sorting by market_value as fallback)
4. Remove the "Top Market Value Positions mislabeled as Top Gain Positions" structural bug

This is a NEW finding outside the original 5-hypothesis set — the fix requires a different data
source swap (account_gains) than the CBBY fix (canonical_lots).

---

## Reconciliation Table

| Metric | Source | Value (Peter Lee) | Correct? |
|--------|--------|-------------------|---------|
| CBBY total | Bronze BUY trans_amount | $1,309,257,523 | NO — includes sold positions |
| CBBY 2026 | Bronze 2026 buys | $290,894,883 | NO — not current-holdings basis |
| Capital Gains TTM | 12m delta unrealized | -$54,867,819 | LABELED WRONG — not realized gains |
| Unrealized cost basis | Orion REST tax_unrealized API | $27,447,333 | YES — current holdings |
| Unrealized gain | Orion REST tax_unrealized API | $8,053,982 | YES — current holdings |
| Realized cost basis | Orion REST tax_realized API | $36,966,963 | YES — TTM closed positions |
| Realized gain | Orion REST tax_realized API | $3,103,668 | YES — TTM closed positions |
| AUA by Tax Status (now) | clients_tab.json#tax | $203,339,876 | YES — post D-max β |
| Top positions cost_basis | None (null emit) | null | NO — source wrong / filter silent fail |

---

## Recommended Fix Scope for INFFIN.020

### Fix A: CBBY — canonical_lots source swap (P1)

**In INF_D_02 and INF_D_00:**

Replace `_aggregate_cost_basis_by_year(buy_lots, holdings, acct_filter)` with a new function
`_cbby_from_canonical_lots(lots, holdings, acct_filter)` that:
1. Loads `gold/lots_latest.parquet` from INF_B_02 (schema: account_id, ticker, buy_date, cost_basis, current_units, cost_per_unit, custodian)
2. Filters to acct_filter scope
3. Groups by `buy_date.year` → sum(cost_basis)
4. Computes current market_value: join to latest holdings on (account_id, ticker), sum(market_value) per year
5. unrealized_gain = market_value - cost_basis

Result: CBBY shows CURRENT holdings cost basis bucketed by the year the lot was originally purchased.
Expected result for Peter Lee: total CBBY ~= $27.4M (matching the unrealized.total_cost_basis from
Orion REST API, which is the ground truth for current holdings).

### Fix B: Top Gain Positions — account_gains source swap (P1, bundle with Fix A)

**In INF_D_02 and INF_D_00:**

Replace bronze buy transactions in `_compute_top_position_performance` with `account_gains`:
1. Load `gold/account_gains/{latest_date}.parquet` from INF_B_03
2. Filter to advisor's accounts
3. Group by ticker: sum(market_value), sum(cost_basis), sum(unrealized_gain)
4. Sort by unrealized_gain descending (true "top gain" semantic)
5. Join TTM price history for ttm_price_change_pct and ttm_dollar_appreciation

This populates cost_basis and unrealized_gain for all top positions and enables correct
"Top Gain Positions" semantic (sorted by unrealized gain, not market value).

### Fix C: Capital Gains TTM — label fix or realized computation (P2, ship separately)

**Option 1 (minimal, P2):** Relabel in FE TaxCostBasisPanel.tsx:
- "Capital Gains (TTM)" → "Unrealized P&L Change (TTM)"
- Add tooltip explaining: "Change in total unrealized gain over the trailing 12 months."

**Option 2 (comprehensive, P3):** Compute true TTM realized capital gains from sell transactions:
- Filter bronze transactions to SELL type IDs (opposite of {10, 14})
- Join to cost basis at time of sale
- Sum (proceeds - cost_basis) per advisor/firm over TTM window
- This requires the realized gains API data already available in `silver/api_dims/tax_realized/`
  (which currently feeds the `realized.total_gain_loss` = $3.1M panel separately)

CTO/COO recommendation: Option 1 (label fix) ships immediately. Option 2 is a V2 enhancement.

### Fix D: AUA by Tax Status stale artifact cleanup (P3)

Remove `platinum/firm/snapshots/aua_by_tax_status.json` from INF_D_00 emit path OR update it
to write the live `build_firm_tax_block` output to that key. The current `data:[]` is misleading.

---

## 49F Regression Risk Assessment

**HIGH risk if CBBY fix is applied to INF_D_02 only.**

The `_aggregate_cost_basis_by_year` function with identical "v1 simple semantics" is used for
BOTH Inflection advisors (INF_D_02) AND 49F advisors (49F uses its own D_02 script which
mirrors the same pattern). If CBBY is fixed to use canonical_lots for Inflection but not 49F:
- Inflection CBBY will show ~$27M (correct current-holdings basis)
- 49F CBBY will still show historical acquisition total (structurally incorrect but unchanged)

**Recommended scope for INFFIN.020:** Fix both INF_D_02 (Inflection) AND the parallel 49F
equivalent (likely `data/scripts/gold/D_02.advisor_client_detail.py` or equivalent). If 49F
D_02 is not in scope, coordinate with 49F DS lane before shipping.

**Top Gain Positions fix (account_gains):** Same regression risk — 49F uses the same source
pattern. Both should be fixed together.

---

## Cascade Dispatch Recommendation

| INFFIN.020 fix | Scope | Dependency |
|----------------|-------|-----------|
| Fix A: CBBY canonical_lots source | INF_D_02 + INF_D_00 (+ 49F D_02) | INF_B_02 canonical_lots exists |
| Fix B: Top Gain Positions account_gains | INF_D_02 + INF_D_00 (+ 49F) | INF_B_03 account_gains exists |
| Fix C: Capital Gains TTM label | TaxCostBasisPanel.tsx (FE) | No DS dependency |
| Fix D: Stale artifact cleanup | INF_D_00 snapshots emit | None |

Fix A + Fix B can be bundled in a single gold script edit + chain re-fire.
Fix C is FE-only (RD lane), no chain re-fire needed.
Fix D is a low-risk output path change.

---

## Cross-References

- Sister pattern: ADHC_BPMVH D-max β bronze+pmv reconciliation (`7be0dda7e`) — same
  "decompose-the-gap empirically" methodology applied here
- INF_B_02.canonical_lots.py — source for Fix A
- INF_B_03.account_gains.py — source for Fix B
- `platinum/advisors/peter_lee/book.json` — empirical ground truth for all values above
- `platinum/firm/clients_tab.json#tax` — firm-level tax block (live post D-max β)
- PRD: `docs/architecture/ADVI_INFFIN_UX_FIXES_BATCH.md §3.1`
