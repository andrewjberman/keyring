# ADVI_49PUSH Phase 1 Platinum Validation Report

**Task Order:** ADVI_49PUSH.006
**Validator:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-09
**Data As Of:** 2026-04-02
**Platinum File Count:** 14,628
**Overall Result:** CONDITIONAL PASS -- one critical number consistency issue

---

## Summary

| Requirement | Description | Result |
|---|---|---|
| REQ 1 | Firm-level files (dashboard, mix_summary) | PASS |
| REQ 2 | Advisor spot-check (10 advisors) | PASS |
| REQ 3 | Client spot-check (50 clients) | PASS |
| REQ 4 | Account spot-check (100 accounts) | PASS |
| REQ 5 | Number consistency (firm = sum advisors) | **FAIL** |
| REQ 6 | Timeseries spot-check (5 clients) | PASS |

---

## REQ 1: Firm-Level Files -- PASS

**platinum/firm/dashboard.json** (224 bytes, split mode):
- `headline.total_aua`: $1,617,911,901.98
- `headline.account_count`: 6,025
- `headline.client_count`: 2,823
- Sections: headline, split flag (leaderboard + fee_efficiency in separate files)

**platinum/firm/mix_summary.json** (8.8 KB):
- Sections: mix (4-class), mix_periods (5 quarters), concentration (top 10), composition
- All sections populated with valid data

**Additional firm files (Phase 3):**
- fee_efficiency.json (281 KB)
- leaderboard.json (148 KB)
- partner_analytics_quarterly/monthly/annual.json (~5 MB each)
- cumulative_chart.json (1.4 MB)
- timeseries_overview.json (64 KB)
- Total: 9 firm-level files

---

## REQ 2: Advisor Spot-Check -- PASS

10 advisors sampled (seed=42). All AUA values match gold/entities/advisors/{id}/book.json exactly:

| Advisor | Platinum AUA | Gold AUA | Match |
|---|---|---|---|
| david_farrell | $87,371,618.12 | $87,371,618.12 | MATCH |
| 49f_house | $25,423,619.13 | $25,423,619.13 | MATCH |
| nick_bishop | $892,709.34 | $892,709.34 | MATCH |
| dean_dillenberg | $81,367,641.18 | $81,367,641.18 | MATCH |
| zach_hawkins | $39,173,340.78 | $39,173,340.78 | MATCH |
| tim_rodgers | $69,437,403.81 | $69,437,403.81 | MATCH |
| brandon_lanz | $65,919,963.78 | $65,919,963.78 | MATCH |
| unassigned | $194,744.52 | $194,744.52 | MATCH |
| boston_prachyl | $15,941,011.45 | $15,941,011.45 | MATCH |
| mitch_roper | $418,511.25 | $418,511.25 | MATCH |

Platinum advisor summary structure: `book` (name, counts, aua, nna, growth, clients), `mix` (4-class), `mix_periods` (5Q), `concentration` (top 10), `fee_summary`, `tax_exposure`.

---

## REQ 3: Client Spot-Check -- PASS

50 clients sampled. All AUA values match gold/entities/clients/{id}/detail.json within $1 tolerance.

- AUA match: 50/50
- All expected sections present: detail, mix, mix_periods, concentration, decomposition_90d
- Client summary structure: `detail.total_aua` (not `headline.total_aua`)

---

## REQ 4: Account Spot-Check -- PASS

100 accounts sampled from 6,127 total platinum account files.

- All 100 have valid 3-class mix (equity/fixed_income/alternatives)
- All have top holdings or concentration data

---

## REQ 5: Number Consistency -- FAIL

### Firm AUA vs Sum of Advisor AUA

| Metric | Firm Dashboard | Sum of 32 Advisors | Difference |
|---|---|---|---|
| Total AUA | $1,617,911,901.98 | $1,629,900,612.05 | **$11,988,710.07** |
| Account Count | 6,025 | 6,343 | **+318** |
| Client Count | 2,823 | 3,055 | **+232** |

**Tolerance:** <$1. **Actual difference:** $11,988,710.07. **FAIL.**

### Advisor AUA vs Sum of Client AUA (sub-check)

5 advisors sampled -- all pass within rounding (<$0.05):

| Advisor | Advisor AUA | Sum Client AUA | Diff |
|---|---|---|---|
| patrick_mundlin | $83,700,346.95 | $83,700,346.96 | $0.01 |
| zach_hawkins | $39,173,340.78 | $39,173,340.76 | $0.02 |
| liv_shin | $7,944,971.47 | $7,944,971.49 | $0.02 |
| boston_prachyl | $15,941,011.45 | $15,941,011.46 | $0.01 |
| matt_foxhall | $46,444,708.55 | $46,444,708.59 | $0.04 |

### Root Cause Analysis

The firm dashboard reads its headline from `clients_tab.json` (D_00), which applies ghost account exclusion and AP gate filtering. The advisor summaries read from D_02 `book.json` files, which include ALL accounts (no ghost/insurance filtering).

**Evidence:**
- `clients_tab.headline.total_aua` = $1,617,911,901.98 (matches dashboard exactly)
- Sum of D_02 book.json across 32 advisors = $1,629,900,612.05
- The 318 extra accounts and $11.99M difference are ghost/insurance-excluded accounts

**Fix:** D_04 `build_advisor_summaries()` must apply the same ghost/insurance exclusions to the advisor-level aggregation that D_00 applies at the firm level. Either:
1. Re-aggregate advisor AUA after applying exclusions to the client list, or
2. Read the excluded account IDs and subtract them from each advisor's book

---

## REQ 6: Timeseries Spot-Check -- PASS

5 clients sampled. All mix_timeseries.json and concentration.json files match gold C_06 full envelope exactly:

| Client | Points | Date Samples Checked | Result |
|---|---|---|---|
| z08349391 | 206 | 3 dates | All MATCH (equity, fi, mv exact) |
| z08343814 | 228 | 3 dates | All MATCH |
| z08282644 | 739 | 3 dates | All MATCH |
| z0880649 | 1,886 | 3 dates | All MATCH |
| z08258962 | 1,400 | 3 dates | All MATCH |

Point counts match gold exactly. Sampled first, middle, and last dates -- all equity pct, fixed_income pct, and total_mv values are identical.

---

## File Inventory

| Prefix | Count | Description |
|---|---|---|
| platinum/firm/ | 9 | Dashboard, mix, leaderboard, fee_eff, partner_analytics x3, cumulative, timeseries_overview |
| platinum/advisors/ | 32 | One summary.json per advisor |
| platinum/clients/ | ~8,466 | summary.json + mix_timeseries.json + concentration.json per client (~2,822 x 3) |
| platinum/accounts/ | ~6,127 | One summary.json per account |
| **Total** | **14,628** | Matches COO-reported count |

---

## Recommendation

The only blocking issue is REQ 5 (number consistency). This is a **D_04 code bug**, not a data quality issue -- the underlying gold data is consistent. The fix is localized to `build_advisor_summaries()` in D_04. All other checks pass cleanly.

Recommend: issue a fix TO for D_04 to apply ghost/AP-gate exclusions at the advisor level, then re-run D_04 and re-validate REQ 5.
