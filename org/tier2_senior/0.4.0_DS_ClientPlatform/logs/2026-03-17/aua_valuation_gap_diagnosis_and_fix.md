# AUA Valuation Gap Diagnosis and Fix -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-17

## Objective

Cross-validate the GRO (Growth Decomposition) panel values in the AdvisorIntelligence Assets Overview by independently checking that AUA, NNA, and market components reconcile. Discovered a systematic gold-vs-silver AUA gap of +$37.5M across 35 accounts. Diagnosed root causes at position level and implemented fixes for the two highest-impact categories.

---

## Work Completed

### 1. GRO Decomposition Identity Validation

Wrote `.tmp_gro_validation.py` to verify: `AUA(end) = AUA(start) + Market(month) + NNA(month)`.

Result: Identity holds perfectly across all months (tautological by construction in the Lambda). Monthly market-as-%-of-AUA values are within expected ranges (-7.2% to +8.9%). The decomposition math is correct.

However, gold-vs-silver cross-check at month boundaries revealed large gaps:
- Feb 26: Gold $1.52B vs Silver $1.63B (-$114M / -7.0%)
- Jan 29: Gold $1.60B vs Silver $1.57B (+$25M / +1.6%)
- Mar 13: Gold $1.62B vs Silver $1.58B (+$39M / +2.4%)

### 2. Account-Level Gap Distribution

Wrote `.tmp_gap_distribution.py` to bucket account-level gaps.

- 35 accounts with abs(gap) > $1M: net +$37.5M (92% of total gap)
- 587 accounts with abs(gap) > $100K: net +$41.5M
- 5,280 accounts with abs(gap) < $100K: largely cancel out

### 3. Position-Level Drill on All 35 Accounts

Wrote `.tmp_position_drill.py` to show every position in gold vs silver's account MV for the top 35.

Identified 9 distinct root cause categories:

| RC | Description | Net Impact |
|----|-------------|------------|
| RC1 | Wrong ticker resolution (structured notes priced as parent equity) | +$25.3M |
| RC2 | Model portfolio sleeves at wrong NAV (Brinker Capital Destinations) | +$20.3M |
| RC3 | Position misattribution within household (nets to ~$0 at relationship level) | -$1.5M |
| RC4 | Private/alternative funds at $1.00 or stale NAV | -$2.0M |
| RC5 | Account missing from positions cube (new onboard) | -$4.9M |
| RC6 | Ghost/stale positions for closed/zeroed accounts | +$7.2M |
| RC7 | Incomplete position data (SMA/wrap/401k) | -$9.3M |
| RC8 | Systematic ETF/bond pricing gap (canonical vs BD) | -$6.7M |
| RC9 | Real estate / non-custodied assets in silver only | -$3.75M |

### 4. Fix Implementation (RC1/RC2 + RC6)

**New file: `data/black_diamond/scripts/gold/aua_overrides.json`**

JSON configuration with two sections:
- `price_overrides`: 5 asset names to zero-price. Removes +$43.9M phantom overvaluation.
  - BNP PARIBAS SA (structured deposit priced as BNPQF equity at $97)
  - DESTINATIONS LARGE CAP EQUITY I (model sleeve at wrong NAV $546)
  - DESTINATIONS INTERNATIONAL EQUITY I (model sleeve at wrong NAV $384)
  - NATIONAL BANK OF CANADA (structured note priced as NTIOF equity at $138)
  - BBVA GLOBAL SECS B V 0% 09/16/2030 (structured note)
- `ghost_accounts`: 4 account IDs to exclude. Removes +$7.4M stale AUA.
  - z0812933851, z0818413191, z0819915221, z0815983871

**Modified: `data/black_diamond/scripts/gold/05_build_client_performance.py`**

- Added `import json`, `AUA_OVERRIDES_PATH` constant
- Added `load_aua_overrides()` function
- `process_date_partition()`: new params `price_override_actions`, `ghost_accounts`
  - Ghost accounts: filtered before pricing
  - Price overrides: force `price=0.0, source='override_zero'` for matched assets
- `build_client_performance()`: passes overrides to partition processor
- `main()`: new Step 1b loads overrides

### 5. DT Briefing

Wrote `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/briefing-aua-valuation-fixes-v1.md` with full deployment instructions, expected impact, and validation steps.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Zero-price instead of silver fallback for RC1/RC2 | Silver MV is account-level only (no position breakdown). Cannot attribute silver's value to specific positions. Zeroing is conservative: understates AUA by the true value of these instruments, but eliminates the 10x-1200x overvaluation. |
| Exclude ghost accounts entirely (RC6) | Silver says $0, gold has $2-3M of stale positions. No intermediate option: either include phantom AUA or exclude it. |
| Defer RC8 (ETF pricing gap) to Phase 2 | Systematic 15-27% gap across standard ETFs suggests a price timing issue (T-1 vs T close). Needs investigation of canonical price timestamps before designing a fix. A silver-calibration fallback risks circular dependency. |
| Config file instead of hardcoded overrides | `aua_overrides.json` is human-readable, version-tracked, and extensible. Adding new overrides doesn't require code changes. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/aua_overrides.json` | New -- price overrides + ghost accounts config | Pending |
| `data/black_diamond/scripts/gold/05_build_client_performance.py` | Load overrides, apply in partition processing | Pending |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/briefing-aua-valuation-fixes-v1.md` | New -- DT deployment briefing | Pending |

---

## Blockers

None. Code changes are self-contained. Deployment requires DT to run the updated script on EC2 and propagate downstream.

---

## Current State

**Status:** COMPLETE (pending commit + DT deployment)
**Active branch:** `CLOUD`

The updated `05_build_client_performance.py` loads `aua_overrides.json` at startup, zeroes 5 mispriced asset names, and excludes 4 ghost accounts from the positions cube before computing AUA. Expected to reduce the gold-vs-silver gap from +3.5% to <1.5%. NNA flows are unaffected.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Commit** all three files to CLOUD
2. **[0.4.0_DT_ClientPlatform] Deploy** updated script + config to EC2 via `safe-ec2-deploy.sh`
3. **[0.4.0_DT_ClientPlatform] Run** `05_build_client_performance.py --upload` to regenerate gold parquet
4. **[0.4.0_DT_ClientPlatform] Run** `05c_validate_aua_vs_silver.py` to confirm gap reduction
5. **[0.4.0_DT_ClientPlatform] Run** downstream scripts (07-10) to propagate into portal JSON
6. **[0.4.0_DS_ClientPlatform] Phase 2** -- investigate RC8 (ETF price timing gap) by comparing canonical_prices timestamps against BD allocation `as_of_date`

**Files to touch next:**
- `silver/prices/canonical_prices.parquet` -- investigate T vs T-1 close timing for RC8

**Do NOT:**
- Implement silver-calibration fallback without confirming the price timing root cause
- Remove ghost accounts from the exclusion list without verifying they are still closed in silver
