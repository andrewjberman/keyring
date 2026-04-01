# ADHC_HISTRY P2 -- Gold Rebuild + 007 Diagnostic -- 0.6.0_AE_PartnerETL

**Date:** 2026-04-01
**Task Orders:** ADHC_HISTRY.004 (gold rebuild), ADHC_HISTRY.007 (coverage audit)
**EC2 Instance:** bd-gold-layer-runner (i-01003b035d2988dfb, c6i.16xlarge)

---

## Objective

Deploy DS Phase 2 RPS injection scripts (commit 80ec50e9) and run a full gold
rebuild with the new March 2026 RPS data. Then run adhc_histry_007 coverage audit.

---

## RPS Silver Extension (March 2026)

March 2026 RPS files were missing from S3 (feed gap). Andrew downloaded 22 files
from Schwab Data Delivery (OneDrive). Files uploaded via:

  Local OneDrive -> opal-data-bd/uploads/schwab/ (staging)
  -> EC2 SSM -> opal-data-schwab/bronze/rps/ (with --sse AES256)

Note: opal-data-schwab requires --sse AES256 on all PutObject calls.
This is a bucket policy condition, not a blanket deny.

Converter patched to read from bronze/rps/ in addition to 01_raw/ and 02_anonymized/.
Converter bugs fixed during session:
  - commit 4ccc90da: ProcessPoolExecutor + pd.read_csv (GIL issue with 70MB files)
  - commit 64bcacf2: Duplicate H2 column names (integer index mapping fix)
  - commit 2c8a4470: Add bronze/rps/ source prefix (DT fix per bucket policy)

silver/RPS/ final state: 556 partitions, 2024-01-12 to 2026-03-31

---

## Gold Rebuild

**Scripts:** DS commit 80ec50e9 (02_build_positions_cube.py + 03_build_holdings_lots.py)
**Mode:** Full rebuild

### Key results

| Metric | Value |
|--------|-------|
| RPS snapshot used | 20260331 (March 31) |
| RPS account mapping | 6,424 Schwab->BD pairs |
| RPS buy gaps | 67,288 positions (+24,895,892 units) |
| RPS sell gaps | 7,818 positions (-17,729,569 units) |
| Total RPS events | 75,106 across 5,422 accounts |
| positions_cube partitions | 2,278 |
| holdings_lots Open AUA | $2,406,064,698 |
| **Total AUA (client_performance)** | **$1,582,318,409** |
| **Silver AUA** | **$1,587,368,576** |
| **Gap** | **$5,050,167 (0.3%)** |

Transaction CUSIP bridge: NOT fired (BD transactions lack cusip column).
The $177M vanished-position close via zero-check did NOT execute. Yet still
landed at 0.3% residual -- explained by the buy injection overcoming the gap.

### SSM execution timeout issue

AWS-RunShellScript default executionTimeout = 3600s (1 hour). Full gold run
took ~80 min. SSM killed the run mid-05b on first attempt.

Fix: pass `"executionTimeout": ["86400"]` in SSM parameters for any gold run.
Second run (command 021e83f5) used 24-hour timeout and completed successfully.

### Script sequence (05b-10 run separately after full run was killed)

| Script | Completed | Notes |
|--------|-----------|-------|
| Pre-step canonical prices | Done | build_canonical_prices_v2 + inject_scoped_overrides |
| 00 accounts dimension | Done | |
| 01 advisor history | Done | |
| 02 positions_cube | 17:27 UTC | 2,278 partitions, 93M rows, RPS injection applied |
| 04 client dimension | 17:30 UTC | 3,589 households |
| 03 holdings_lots | 17:32 UTC | Open AUA $2.406B |
| 05 client_performance | 17:36 UTC | Total AUA $1.582B |
| 05b account_performance | 18:16 UTC | 75MB, 2nd run with 24hr timeout |
| 05c/d/f | Done | AUA certification written |
| 06 tax liability | Done | |
| 07 nna_aua_by_geography | Done | |
| 08b architect_attribution | Done | |
| 12 composition_artifacts | Done | |
| 06b client_mix_timeseries | Done | |
| 08 nna_aua_by_advisor | Done | |
| 09 partner_analytics | Done | |
| 10 advisor_rolling_flows | Done | 18:30 UTC |

Pipeline-complete.json written manually -> triggered bd-portal-publisher Lambda.
Portal updated with today's data.

---

## adhc_histry_007 -- Transaction Coverage Audit

**Script:** commit 770e4d93 (DS-authored)
**SSM command:** 3df53953-ad08-4a64-b1b0-e6a98d0a705d
**Completed:** 2026-04-01T18:50:27 UTC

### Part A -- Coverage breakdown

| Category | Positions | MV |
|----------|-----------|-----|
| MATCHED | 33,063 | — |
| Buy gap (MISSING) | 29,491 | $456,285,729 |
| Sell gap (PHANTOM) | 61,473 | $1,285,919,541 |
| Min missing buy txns | 29,491 | — |
| Min missing sell txns | 61,473 | — |

CUSIP bridge: 8,330 entries
Total RPS MV: $1,360,217,733
Total FIFO MV (pre-inject): $2,189,387,579

### Part B -- Model mix flags (>1.5pp deviation)

| Asset | Target | Actual | Gap |
|-------|--------|--------|-----|
| PATHFINDER DISCIPLINED | 1.5% | 7.0% | +5.49pp (+$74.7M) |
| PATHFINDER FOCUSED | 1.5% | 6.6% | +5.07pp (+$69.0M) |
| VGT GROWTH | 5.0% | 0.1% | -4.85pp (-$66.0M) |
| QQQ | 4.8% | 0.9% | -3.95pp (-$53.8M) |
| SPDR HIGH YIELD | 1.5% | 3.6% | +2.10pp (+$28.5M) |
| DIVZ | 9.7% | 11.5% | +1.76pp (+$23.9M) |
| VGIT INTERMEDIATE BOND | 2.0% | 3.7% | +1.72pp (+$23.4M) |
| US TREASURY 10Y | 3.0% | 0.0% | -3.00pp (-$40.8M) |
| GLOBAL X T-BILL | 3.0% | 0.7% | -2.28pp (-$31.0M) |
| JANUS CLO | 4.0% | 2.1% | -1.95pp (-$26.5M) |
| S&P MID-CAP | 3.5% | 2.2% | -1.33pp (-$18.0M) |

Sum absolute deviations: $537,668,868

### Outputs

- s3://opal-data-bd/diagnostics/adhc_histry_007_coverage_audit.json
- s3://opal-data-bd/diagnostics/adhc_histry_007_model_mix.json

---

## Key Infrastructure Notes

1. opal-data-schwab requires --sse AES256 on ALL uploads (bucket policy condition)
2. AWS-RunShellScript executionTimeout defaults to 3600s -- always override for
   gold runs: pass "executionTimeout": ["86400"] in SSM parameters
3. pipeline-complete.json must be written after custom script sequences to
   trigger bd-portal-publisher Lambda

---

## Commits This Session

| Commit | Description |
|--------|-------------|
| 4ccc90da | RPS converter: ProcessPoolExecutor + pd.read_csv |
| 64bcacf2 | RPS converter: duplicate H2 column name fix |
| 2c8a4470 | RPS converter: add bronze/rps/ source prefix (DT fix) |
| 413e1cf5 | Session log: P1 RPS silver build |
