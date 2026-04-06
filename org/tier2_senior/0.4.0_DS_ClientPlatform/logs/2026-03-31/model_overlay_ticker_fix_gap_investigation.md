# Model Overlay Ticker Fix and Gap Investigation -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-31
**Start Time:** 11:00 PM ET
**End Time:** 12:35 AM ET (2026-04-01)
**Project:** ADVI_PRICES (model overlay accuracy)

---

## Objective

Cross-reference Opal model portfolio weights against BD gold layer holdings to identify
why the 49F Books tab shows ~3% DIVZ vs 13% target, ~4% SPYM vs 9% target, etc.
Uncover all tickerization errors, attribution mismatches, and injection gaps.

---

## Work Completed

### 1. Ticker Authority Fix (8 tickers corrected)

Daily price files on S3 carried stale tickers from before `ticker_overrides.py` corrections
were applied. `canonical_prices.parquet` was rebuilt with correct tickers but daily files
were not. Script 03 `load_latest_prices()` selected the daily file (most recent date),
propagating wrong tickers to holdings_lots.

| Correct | Was Wrong | Asset Name | BD MV |
|---------|-----------|------------|-------|
| SPYM | SPLG | SPDR Portfolio S&P 500 ETF | $63.4M |
| CLIP | BIL | Global X 1-3 Month T-Bill ETF | $14.4M |
| BSCR | BSCN | BulletShares 2027 Corp Bond | $7.2M |
| UTEN | TLT | US Treasury 10 Year Note ETF | $6.9M |
| BSCQ | BSCN | BulletShares 2026 Corp Bond | $2.6M |
| LONZ | BKLN | Pimco Senior Loan Active ETF | $1.4M |
| BSJQ | BSJK | BulletShares 2026 HY Corp Bond | $265K |
| QBER | TUSC | TrueShares Quarterly Bear Hedge | $96K |

Fix: Added canonical ticker authority override in `load_latest_prices()` (commit 68d40369).
Also updated `s3://opal-data-bd/config/ticker_lookup.json` (8 entries corrected).
Both script 03 and ticker_lookup.json deployed to S3.

### 2. Full Gold Layer Rerun

SSM command `cbbcc933-d5be-4af4-8a36-f3e6a6e683e4` on `i-01003b035d2988dfb` (c6i.16xlarge).
All 8 ticker fixes verified in new `holdings_lots/2026-03-31.parquet`.
Pipeline completed at 11:48 PM ET.

### 3. Gap Decomposition ($244M model overlay shortfall)

Opal Positioning target weights vs BD gold actual:

| Ticker | Target% | Gold% | Gap | Missing MV |
|--------|---------|-------|-----|-----------|
| IEFA | 10.1% | 6.6% | -3.5pp | $55M |
| DIVZ | 9.7% | 3.1% | -6.6pp | $104M |
| SPYM | 6.8% | 4.0% | -2.8pp | $44M |
| IDVZ | 8.2% | 7.4% | -0.8pp | $13M |
| Others | 20.6% | 19.2% | -1.4pp | $28M |

Total: $934M actual vs $1,178M expected = $244M gap.

### 4. Root Cause Analysis (5 independent causes, $244M fully attributed)

**RC1 ($109M): DIVZ asset_name split (Feb 17, 2026)**
BD renamed "OPAL DIVIDEND INCOME ETF" to "POLEN DIVIDEND INCOME ETF".
Script 02 keys FIFO on (account_id, asset_name). Post-rename transactions
create a new FIFO chain with zero initial units. POLEN-only accounts avg $2,927
MV vs OPAL-only $27,775 -- a 10x difference confirming the split.

**RC2 ($63M): Buy injection blocked by phantom positions**
59% of gold MV in negative-residual accounts comes from positions that BD's
unrealized report does NOT list as open. These phantom positions inflate
gold_mv > silver_mv, causing residual <= 0, which blocks injection entirely.
Affected: 1,425 SPYM accounts, 964 IEMG, 542 IEFA, 310 DIVZ.

**RC3 ($10M): Accounts missing from silver allocations**
784 accounts in unrealized but not in allocations. Injection has no silver MV
reference and skips them.

**RC4 ($15M): Price-weighted injection distribution**
When injection fires, it distributes residual as `price / sum(prices)` which
equals equal-unit allocation, not model-weight allocation. Low-price ETFs
(DIVZ $37) get systematically under-allocated vs high-price ETFs (IEFA $80).

**RC5 ($47M): Transitional positions (not a bug)**
$174M in historical model tickers (VTV $30M, IQLT $33M, JEPI $24M, COWZ $20M)
across model accounts. These are accounts still mid-transition from old-model
to new-model allocations.

### 5. Cross-Checks Performed

- RC1: Confirmed POLEN-only accounts 10x smaller avg MV than OPAL-only. Transaction
  files show clean cutover Feb 16->17. 306 accounts have split positions under both names.
- RC2: Sampled 200 neg-residual SPYM-missing accounts. 59% of their gold MV is from
  positions BD unrealized doesn't list as open (phantom). Cannot disprove.
- RC5: Verified VTV/IQLT/JEPI/COWZ are historical Opal model tickers (all 5 models).
  These are expected transitional positions.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Deploy ticker fixes immediately | 8 tickers affected, code-only change, no risk |
| Full gold rerun (not incremental) | Ticker fix in script 03 needs full lot rebuild |
| Use canonical_prices as ticker authority | Daily files carry stale tickers; canonical is rebuilt with corrections |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `gold/03_build_holdings_lots.py` | Canonical ticker authority in load_latest_prices | Yes -- `68d40369` |
| `s3://opal-data-bd/config/ticker_lookup.json` | 8 tickers corrected (SPLG->SPYM, BIL->CLIP, etc.) | Deployed to S3 |
| `s3://opal-data-bd/code/gold/03_build_holdings_lots.py` | Deployed updated script | Deployed to S3 |

---

## Current State

**Status:** COMPLETE (investigation). Fixes pending (RC1-RC4).
**Active branch:** `CLOUD`

Full $244M gap between Opal model weights and BD gold layer is attributed to 5 root causes.
Ticker fixes (8 tickers) deployed and verified. Gold rerun completed with correct tickers.
Portal Books tab confirmed matching gold output. Gap is structural: DIVZ name split ($109M),
phantom-blocked injection ($63M), transitional positions ($47M), plus smaller factors.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] RC1 fix: DIVZ name aliasing in script 02** -- Map "OPAL DIVIDEND INCOME ETF" and "EVENTIDE HIGH DIVIDEND ETF" to "POLEN DIVIDEND INCOME ETF" before FIFO computation. Single biggest impact ($109M). Code-only change.
2. **[0.4.0_DS_ClientPlatform] RC2 fix: Per-position injection** -- Redesign `_load_synthetic_buy_events` to inject per missing position using unrealized lot count as unit authority, rather than distributing account-level residual. Eliminates phantom position masking.
3. **[0.4.0_DS_ClientPlatform] RC4 fix: Model-weight injection prior** -- When injection fires, use Tier A observed weights (R^2=0.96 vs model) instead of price-weighting. Amplifies RC2 fix.
4. **[0.6.0_AE_PartnerETL] Gold rerun after RC1+RC2 fixes** -- Full mode required.
5. **[Andrew] Validate expected Opal AUM** -- The $1.178B number should be cross-checked against SmartX enrollment data to confirm scope.

**Do NOT:**
- Re-enable the old SPLG/BSCN/BSJK/BKLN/TUSC/TLT ticker mappings
- Apply injection fixes without rerunning the full gold layer
- Modify the sell injection logic (phantom sells) -- that's working correctly
- Merge RC1 name aliasing into ticker_overrides.py -- it's a FIFO issue, not a pricing issue
