# ADHC_HISTRY: RPS Injection + Diagnostics Full Session -- 0.4.0_DS_ClientPlatform

**Date:** 2026-04-01
**Start Time:** 1:11 PM ET
**End Time:** 7:30 PM ET
**Project:** ADHC_HISTRY
**Task Orders:** ADHC_HISTRY.002, .006

---

## Objective

Phase 1 diagnostic (adhc_histry_005) confirmed Schwab RPS as viable injection authority.
COO issued Phase 2 GO. This session implements Phase 2 (scripts 02+03 RPS injection),
extends coverage to March RPS data, runs diagnostics .007/.008/.009, and identifies
two separate structural problems in BD's transaction feed.

---

## Work Completed

### 1. Phase 2: Schwab RPS Injection in Gold Scripts 02 + 03

Implemented Schwab RPS-based two-sided injection for 6,510 mapped accounts.

**Core logic (both scripts):**
- Load latest RPS partition (silver/RPS/) as ground truth
- Map Schwab account_id → BD account_id via schwab_bd_account_mapping.parquet
- Build CUSIP→asset_name bridge from unrealized (open) + realized compact (sold)
- For each (mapped account, asset_name): gap = rps_units - fifo_units
  - RPS > FIFO → synthetic buy injection
  - FIFO > RPS → synthetic sell (rotation correction)
- Unmapped accounts fall back to existing RC2 unrealized-based injection

**Extension (commit 80ec50e9):** Extended CUSIP bridge to BD transaction CUSIPs
if the `cusip` column exists in silver/transactions/. Enables zero-check on
"vanished" positions (in FIFO but absent from both unrealized and realized).
BD transactions confirmed to NOT have cusip column -- extension gracefully returned
empty, fallback to unrealized+realized bridge.

**Commits:**
| Hash | Description |
|---|---|
| `2666dc1f` | Phase 2 initial -- RPS injection in scripts 02+03 |
| `80ec50e9` | CUSIP bridge extended to transactions (no-op but safe) |
| `0a1fc2ba` | 1901 date clamp + synthetic positions index |

### 2. Silver/RPS/ Extended to March 31

AE ran convert_schwab_rps_to_parquet.py.
- Feb 27 result: 534 partitions (2024-01-12 to 2026-02-27)
- March files found via Andrew's investigation: 22 additional RPS files
- March upload required --sse AES256 header (bucket policy, not a blanket deny)
- Extended: 556 partitions (2024-01-12 to 2026-03-31)

**Converter fix (commit 2c8a4470):** SRC_PREFIXES updated to read bronze/rps/ first,
then 01_raw/ as fallback. Staging script convert_rps_march_staging.py deleted.

### 3. Gold Layer Full Rebuild

**SSM command:** 52237778-eaea-429d-8e49-172c500fa554
**Instance:** i-01003b035d2988dfb (c6i.16xlarge, 60 workers)
**Mode:** Full rebuild
**Scripts:** 80ec50e9

**Result:**
- Total AUA: $1,582,318,409 (silver: $1,587,368,576 -- $5M / 0.3% gap)
- RPS injection: 75,106 events across 5,422 accounts
- Transaction CUSIP bridge: 0 (BD transactions lack cusip column)
- AUA lock maintained through full RPS injection

### 4. .007 Transaction Coverage Audit

Diagnostic: adhc_histry_007_transaction_coverage_audit.py (commit 770e4d93)
Classified every (mapped account, CUSIP) gap into 5 categories.

**Coverage results (March 31 snapshot, 6,510 mapped accounts):**

| Category | Positions | MV |
|---|---|---|
| MATCHED (BD correct) | 33,063 | -- |
| PARTIAL_BUY_GAP | 29,491 | $456,285,729 |
| COMPLETE_MISS | (included above) | (included above) |
| PHANTOM_SELL | 61,473 | $1,285,919,541 |
| VANISHED | (included above) | (included above) |

- **Gross undershoot:** $456M (29,491 positions) -- BD missing buys
- **Gross overshoot:** $1,285M (61,473 positions) -- phantom positions
- **Minimum missing buy transactions:** 29,491
- **Minimum missing sell transactions:** 61,473
- **Total minimum missing transactions:** 90,964

Key insight: The injection is doing $1.74B of bilateral work ($1.29B phantom sells +
$456M missing buys) to net down to $5M gap. Gross bilateral exposure is much larger
than the net AUA difference suggests.

**Model mix (Part B, Opal 49F vs targets):**
Sum of absolute deviations: $537M. Significant flags:
- PATHFINDER DISCIPLINED: +5.49pp overweight (6.98% vs 1.5% target)
- PATHFINDER FOCUSED: +5.07pp overweight (6.55% vs 1.5% target)
- QQQ: -3.95pp underweight (0.85% vs 4.8% target)
- VUG (Vanguard Growth): -4.85pp underweight (0.15% vs 5.0% target)
Note: PATHFINDER overweights may reflect stale model weights in diagnostic.
Requires validation against current Opal positioning.

### 5. .008 Failure Timing Diagnostic

Diagnostic: adhc_histry_008_failure_timing.py (commit 42ca6ede)
Scanned all 556 RPS partitions to timestamp when each gap first appeared.

**KEY FINDING: BD has TWO separate feed problems.**

**Buy gaps -- $456M total:**

| Quarter | MV | % |
|---|---|---|
| 2024-Q1 | $20M | 4.4% |
| 2024-Q2 | $51M | 11.1% |
| 2024-Q3 | $78M | 17.0% |
| 2024-Q4 | $32M | 7.1% |
| **2025-Q4** | **$259M** | **56.7%** |
| 2026-Q1 | $17M | 3.7% |
| 2025-Q1/Q2/Q3 | ~$0 | ~0% |

**2025-Q4 represents 56.7% of all missing buy transactions.** This is an active,
ongoing delivery failure separate from the 2024 onboarding. Something changed in
BD's feed in Q4 2025. The $17M already in 2026-Q1 suggests it is still occurring.

**Sell gaps -- $495M total:**

| Quarter | MV | % |
|---|---|---|
| **2024-Q2** | **$279M** | **56.3%** |
| 2024-Q3 | $76M | 15.3% |
| 2024-Q4 | $80M | 16.2% |
| 2025-Q4 | $23M | 4.6% |
| 2026-Q1 | $38M | 7.6% |

Sell gaps are predominantly a 2024 event (~88% from 2024). This was the onboarding
rotation where BD failed to deliver sell transactions for liquidated old-model positions.
Already handled by the realized sell injection in script 02.

### 6. .009 Model Coverage Diagnostic

Diagnostic: adhc_histry_009_model_coverage.py (commit 42ca6ede)
Classified every 49F holding by category using RPS as ground truth.

**49F AUM composition ($1,363,617,954 total):**

| Category | MV | % AUM |
|---|---|---|
| ACTIVE_MODEL | $1,041,557,786 | **76.38%** |
| NON_MODEL | $291,533,094 | **21.38%** |
| CASH_EQUIVALENT | $16,758,297 | 1.23% |
| OPAL_ETF | $7,991,663 | 0.59% |
| TRANSITIONAL | $5,777,114 | 0.42% |

**76.4% model-aligned.** Transitional rotation nearly complete ($5.8M, 39 accounts).

NON_MODEL $291.5M breaks into three buckets:
- ~$100M: short-duration fixed income ETFs (VCSH, Dimensional, T-bill ETFs) --
  likely deliberate liquidity/tax management outside model
- ~$50M: individual large-cap stocks (AAPL $6.2M, MSFT $5.1M, NVDA $3.9M, GOOGL $3.6M)
  -- legacy brokerage accounts not fully converted
- ~$140M: long tail of 1,600+ assets, small account-specific holdings

### 7. Infrastructure Fixes

**1901 partition cleanup:**
- Positions cube had 43,500+ partitions from 1901-01-01 through 2019-12-31
- Caused downstream scripts (05, 05b, etc.) to scan 45,742 partitions instead of ~2,200
- 05b reported processing 45,742 partitions during today's gold rebuild
- Root cause: BD transaction feed contains NULL/sentinel dates parsed as 1901-01-01
- Fix: load_transactions() now clamps trade_date < 2019-01-01 to 2020-01-01
- AE queued to delete pre-2020 S3 partitions

**Converter SSE fix:**
- opal-data-schwab bucket policy requires ServerSideEncryption: AES256 on all PutObject
- Was misidentified as blanket write deny; is actually an encryption header requirement
- Converter already had SSE on write path (line 168); only callers were missing --sse flag
- DT (ADHC_HISTRY.005) documented bucket policy; DS fixed SRC_PREFIXES

---

## Key Findings Summary

| Finding | Severity | Status |
|---|---|---|
| $259M in buy gaps from Q4 2025 -- active BD delivery failure | CRITICAL | Requires BD investigation |
| $279M in sell gaps from 2024-Q2 -- onboarding event | KNOWN | Handled by realized sell injection |
| 76.4% of 49F AUM in active Opal model | INFORMATIONAL | Expected; 23.6% non-model under review |
| PATHFINDER ETFs significantly overweight vs 1.5% model targets | NEEDS VALIDATION | Model weights in diagnostic may be stale |
| 1901 partition bloat -- 43,500 bad partitions | FIXED | AE cleaning up |
| AUA lock maintained: $1,582M vs silver $1,587M (0.3% gap) | GOOD | |

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Use March 31 RPS instead of Feb 27 | Full coverage, no stale-date risk for zero-check |
| NNA/market growth to be rederived from canonical holdings timeseries | Current mismatch (NNA from raw txns, AUA from injected cube) creates distorted market appreciation; both must come from same source |
| Clamp 1901 dates in load_transactions() | Bad sentinel dates cause 45K partition bloat and slow pipelines |
| Synthetic positions index written to S3 | Enables script 05 to separate synthetic AUA from organic AUA when NNA rearchitecture proceeds |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `gold/02_build_positions_cube.py` | Phase 2 RPS injection, CUSIP bridge extension, 1901 clamp, synthetic index write | `2666dc1f`, `80ec50e9`, `0a1fc2ba` |
| `gold/03_build_holdings_lots.py` | Phase 2 RPS synthetic lots | `2666dc1f`, `80ec50e9` |
| `bronze/convert_schwab_rps_to_parquet.py` | SRC_PREFIXES: bronze/rps/ first | `2c8a4470` |
| `bronze/convert_rps_march_staging.py` | Deleted (dead code) | `2c8a4470` |
| `diagnostics/adhc_histry_007_transaction_coverage_audit.py` | Coverage audit + model mix | `770e4d93` |
| `diagnostics/adhc_histry_008_failure_timing.py` | RPS time series scan, quarterly failure dating | `42ca6ede` |
| `diagnostics/adhc_histry_009_model_coverage.py` | 49F model coverage by category | `42ca6ede` |

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| Architecture direction: NNA/market growth from canonical holdings | MCP message to AE | AE, COO |
| S3 cleanup instructions | MCP message to AE | AE |

---

## Current State

**Status:** DIAGNOSTIC PHASE COMPLETE. Two action items open.
**Active branch:** CLOUD

Gold rebuild with March 31 RPS complete. AUA at $1,582M (0.3% from silver).
.007/.008/.009 diagnostics all complete and results delivered to Andrew.

**Open items:**

1. **BD Q4 2025 buy gap investigation** -- $259M of buy transactions delivered by Schwab
   in Q4 2025 were never received by BD's feed. This is the most urgent finding.
   Requires BD (Black Diamond) to investigate what changed in their feed delivery
   mechanism in Q4 2025. Not a DS/AE fix -- needs vendor escalation.

2. **NNA/market growth rearchitecture** -- Architecture direction approved by Andrew.
   Market growth to be derived from canonical holdings timeseries, not from parallel
   transaction analysis. Synthetic injection to be booked as "AUA Reconciliation"
   line item. Script 05 update pending scope definition.

3. **Pathfinder model weight validation** -- PDFE at 6.98% and PFOE at 6.55% of 49F AUM
   vs 1.5% model targets in diagnostic. May reflect stale model weights in the diagnostic
   script. Validate against current Opal positioning before treating as an issue.

4. **positions_cube S3 cleanup** -- AE deleting ~43,500 pre-2020 partitions. Will restore
   normal pipeline run times.

---

## Next Steps

1. **[Andrew / BD vendor]** Investigate Q4 2025 buy transaction delivery failure with
   Black Diamond. Why did BD stop delivering buy transactions in Q4 2025?
   Specific question: was there a feed configuration change, API version update, or
   account setup change that caused BD to stop delivering ~$259M of buy transactions?

2. **[Andrew]** Validate PATHFINDER model weights -- are PDFE/PFOE at 1.5% still current,
   or has Opal's 49F model been updated to a higher Pathfinder allocation?

3. **[0.4.0_DS_ClientPlatform]** On confirmation from Andrew: scope NNA/market growth
   rearchitecture task order. Compute NNA from canonical holdings timeseries, book
   synthetic injection as AUA Reconciliation.

4. **[0.6.0_AE_PartnerETL]** Complete positions_cube pre-2020 partition cleanup.
   Upload updated script 02 (0a1fc2ba) to S3.

**Do NOT:**
- Deploy RC3/RC4 -- superseded by RPS authority injection
- Run incremental gold rebuild until 1901 partition cleanup is complete
- Trust PATHFINDER overweight flags until model weights are validated
