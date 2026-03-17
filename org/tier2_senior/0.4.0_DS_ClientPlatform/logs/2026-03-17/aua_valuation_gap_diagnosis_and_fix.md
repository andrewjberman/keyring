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

v1 zeroed assets (creates cliff). v2 used silver tape (only covers Jan+). v3 (final): reverse-engineer per-unit prices from silver and inject into canonical_prices.parquet as `source='scoped_override'`. Covers full history back to each asset's inception.

**New file: `data/black_diamond/scripts/silver/inject_scoped_overrides.py`**

Manages a scoped override registry of 5 assets. Removes wrong-source rows, injects daily scoped_override rows from inception to latest date. Idempotent. Dry run: 1,721 rows injected, 5,799 wrong rows removed, zero duplicates.

| Asset | Wrong Price | Correct Price | Inception | Method |
|---|---|---|---|---|
| Waldrop Donor Advised Fund | $1.00 | $1.95 | 2023-09-13 | Silver-implied NAV (std $0.03) |
| BNP PARIBAS SA | $97.16 (BNPQF) | $0.75 | 2024-12-06 | 75c on dollar face value |
| DESTINATIONS LARGE CAP EQUITY I | $546.00 | $13.30 | 2025-10-02 | Blended silver-implied |
| DESTINATIONS INTERNATIONAL EQUITY I | $384.00 | $13.30 | 2025-10-02 | Blended silver-implied |
| JPMORGAN CHASE FINL CO LLC 0% 2029 | $1.00 | $2.55 | 2024-04-10 | 255c on dollar structured note |

**Simplified: `data/black_diamond/scripts/gold/aua_overrides.json` (v3.0.0)**

RC6-only. Silver tape section removed.

**Simplified: `data/black_diamond/scripts/gold/05_build_client_performance.py`**

Stripped silver tape infrastructure. Now only loads ghost account exclusions. RC1/RC2 fix is entirely in canonical_prices.

### 5. AE Task Order

Wrote `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/aua-scoped-price-overrides-deploy.md` with full deployment sequence for inject -> rebuild -> validate -> propagate.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Scoped overrides in canonical_prices instead of silver tape or zeroing | Zeroing creates a cliff; silver tape only covers Jan+ (2 months of silver data). Reverse-engineering the per-unit price and injecting into canonical_prices covers the full history back to inception. The override is inline -- no separate runtime lookup needed. |
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
