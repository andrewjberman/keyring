# ADVI_PRICES.003 -- Deployment Session (Partial) -- 0.6.0_AE_PartnerETL

**Date:** 2026-03-24
**Task Order:** ADVI_PRICES.003.ae-price-update-and-gold-rerun.md
**Status:** IN PROGRESS -- blocked on R0 (historical_prices backfill)

---

## Actions Taken

### 1. Requirement 7 -- IYF Ticker Correction (COMPLETE)

**Commit:** `1c7bbb4a`
**Author:** `0.6.0_AE_PartnerETL`

Added 9th ticker correction to `_TICKER_CORRECTIONS` in both pricing scripts:
- `ISHARES U.S. FINANCIALS ETF`: XLF -> IYF
- XLF is State Street Financial Select Sector SPDR (~$49)
- IYF is iShares U.S. Financials ETF (~$59)
- DS flagged -16.5% error in diagnostic but did not include in commit `61b34f77`
- Also updated comment from "8 mismatches" to "9 mismatches" in both files

**Files modified:**
| File | Change |
|------|--------|
| `data/black_diamond/scripts/silver/bd_price_update.py` | Added IYF to `_TICKER_CORRECTIONS`, updated count comment |
| `data/black_diamond/scripts/silver/build_canonical_prices_v2.py` | Same -- kept in sync per header instruction |

---

### 2. Requirement 1 -- S3 Code Upload (COMPLETE)

Uploaded both pricing scripts with the IYF correction to S3:
```
aws s3 cp data/black_diamond/scripts/silver/bd_price_update.py s3://opal-data-bd/code/silver/bd_price_update.py
aws s3 cp data/black_diamond/scripts/silver/build_canonical_prices_v2.py s3://opal-data-bd/code/silver/build_canonical_prices_v2.py
```

Both uploads confirmed successful.

---

### 3. Requirements 3+4 -- ticker_lookup.json Patch (COMPLETE)

Downloaded `s3://opal-data-bd/config/ticker_lookup.json` (10,116 records), patched all 9 corrections, re-uploaded.

| Asset Name | Old Ticker | New Ticker |
|-----------|-----------|-----------|
| BNP PARIBAS SA | BNPQF | UNKNOWN (removed) |
| SONY FINL GROUP INC UNSPONSERED ADS | SONY | UNKNOWN (removed) |
| FIRST TRUST MULTI CAP GROWTH ALPHADEX FUND | FNDA | FNX |
| ABRDN PHYSICAL PRECIOUS METALS BASKET SHARES ETF | GLDM | GLTR |
| ISHARES S&P MID-CAP 400 GROWTH ETF | IJH | IJK |
| VANGUARD SMALL CAP VALUE INDEX ADMIRAL | VBR | VSIAX |
| VANGUARD DEVELOPED MARKETS INDEX ADMIRAL | VEA | VTMGX |
| VANGUARD MID CAP INDEX INSTITUTIONALPLUS | VO | VMCPX |
| ISHARES U.S. FINANCIALS ETF | XLF | IYF |

7 tickers corrected, 2 removed. Re-uploaded to same S3 key.

---

### 4. EC2 Runner Start (COMPLETE)

Started persistent runner `i-01003b035d2988dfb` (was stopped). Confirmed SSM-ready.

---

### 5. Canonical Prices Rebuild -- PREMATURE (NEEDS RE-RUN)

**SSM command:** `60a4c0df-178b-4562-ab3b-aeb31b039baa`

Ran `build_canonical_prices_v2.py` on EC2. Completed in 116s:
- 10,446,207 rows, 9,972 assets
- 9 ticker corrections applied
- Source distribution: 82.3% linear_interpolation, 15.8% yahoo_finance, 1.9% transaction_observed

**BNP canary verified:** BNP PARIBAS SA shows `ticker=None`, `price=$1.02` (linear_interpolation, not $95 yahoo). Correct -- scoped_override only applies in bd_price_update.py.

**PROBLEM:** COO discovered that historical_prices.parquet is incomplete for several critical tickers:
- PFDE: completely missing
- IDVZ, PFOE: stale since 2026-02-12 (5 weeks)
- GLTR, VTMGX: missing (new tickers from corrections)

This rebuild ran BEFORE fixing historical_prices, so those tickers fell through to transaction_observed or carry_forward. **Must re-run after R0 backfill.**

---

### 6. Historical Prices Fetch Script (WRITTEN, NOT YET DEPLOYED)

**Local file:** `C:\Users\AndrewBerman\AppData\Local\Temp\fetch_missing_tickers.py`

Script to fetch full yfinance history for 6 tickers (GLTR, VTMGX, PFDE, IDVZ, PFOE, IYF), append to existing historical_prices.parquet, deduplicate, and upload back to S3.

NOT yet uploaded to S3 or executed. Awaiting COO approval.

---

## Current State

| Requirement | Status | Notes |
|------------|--------|-------|
| R0 (historical_prices backfill) | BLOCKED | Script written, not deployed. COO added this as prerequisite after discovering stale/missing tickers |
| R1 (deploy scripts to S3) | DONE | Both pricing scripts uploaded with IYF correction |
| R2 (BNP canary) | NEEDS RE-VERIFY | Premature rebuild confirmed BNP at $1.02 (correct), but must re-verify after R0 backfill + second rebuild |
| R3 (GLTR+VTMGX in scheduler) | DONE (partially) | ticker_lookup.json patched on S3 (scheduler reads this). But historical_prices still needs backfill |
| R4 (ticker_lookup.json patch) | DONE | 9 corrections applied and uploaded |
| R5 (gold rerun) | NOT STARTED | Gated on R0 + canonical rebuild |
| R6 (reconciliation) | NOT STARTED | Gated on R5 |
| R7 (IYF correction) | DONE | Commit `1c7bbb4a` |

---

## EC2 State

- Runner `i-01003b035d2988dfb`: RUNNING (started this session)
- canonical_prices.parquet on S3: rebuilt but needs second pass after historical_prices fix

---

## Next Steps

1. COO approves fetch_missing_tickers.py -> upload to S3 -> run via SSM
2. Verify all 6 tickers have current data in historical_prices.parquet
3. Re-run canonical_prices rebuild (build_canonical_prices_v2.py)
4. Verify BNP canary ($0.75 scoped_override in bd_price_update output)
5. Full gold rerun (run_gold_layer.sh full)
6. Reconciliation diagnostic (recon_lots_vs_allocations.py)
7. Stop EC2 runner
