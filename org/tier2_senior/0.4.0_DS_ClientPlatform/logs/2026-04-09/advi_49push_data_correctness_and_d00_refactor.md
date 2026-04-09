# ADVI Data Correctness Fixes + D_00 Refactor

**Agent:** 0.4.0_DS_ClientPlatform  
**Date:** 2026-04-09 (afternoon/evening session)  
**Project:** ADVI_49PUSH  
**Status:** COMPLETE. All changes committed, pushed, and deployed to S3.

---

## Summary

Live QA session with Andrew -- he walked through the portal and flagged a series of data
correctness bugs. Fixed all of them in sequence, then closed by refactoring D_00 which had
grown to 2,834 lines. No new task orders -- all fixes were reactive to observed portal state.

---

## Fixes

### 1. GEO Bell Curve Count vs Radial Sum Mismatch
**Symptom:** Snapshot-GEO-AUA bell curve showed 6,046 accounts; summing radial segments gave 5,566.

**Root cause:** `total_dist` in `D_01.build_geo_view` was computed from `acct_geo` (all accounts
after left-merge including ~480 with `client_state = 'Unknown'` or foreign states). The segment
loop only iterates `geo_day` (which strips Unknown/empty/null states). Bell curve included 480
accounts that appeared in no radial bucket.

**Fix:** Introduced `acct_geo_radial = acct_geo[acct_geo['client_state'].isin(known_states)]`.
Both `total_dist` and `metrics.account_count` now use this filtered set. Bell curve count now
equals the sum of all segment account_counts.

**Commit:** `06074050` | **File:** D_01.partner_analytics.py

---

### 2. Continuous-GEO Stacked Bar vs Assets Overview Annual AUA Discrepancy
**Symptom:** Assets Overview header showed 1.46B for 2025; Continuous-GEO stacked bar showed 1.51B.
Pattern across all years: every year where Dec 31 falls mid-ISO-week showed a discrepancy. 2023
was an exact match because Dec 31, 2023 was a Sunday (last day of an ISO week).

**Root cause:** `_weekly_downsample` in D_04 keys on `{iso_year}-W{iso_week}`. Dec 29-31 of any
year that fall in ISO week 1 of the NEXT year get stored under that next-year key (e.g. Dec 31,
2025 → `2026-W01`). The actual point stored for `2026-W01` uses date `2026-01-04` (last day in
that ISO week with data). So Dec 31 is absent from the downsampled data as a 2025 Gregorian date.
The stacked bar's Y8 frontend aggregation takes the last data point per Gregorian year, landing on
Dec 28 (the last Sunday of Dec 2025, key `2025-W52`). The header uses `_build_static_aua_periods`
which snapshots the actual Dec 31 date. Same source, different snapshot dates.

**Investigated further:** The 2024 bar showed an even larger discrepancy (1.23B vs 963m). Traced
this to the underlying `account_performance.parquet` which has a structural data quality issue:
every weekend and market holiday in 2024 Q2-Q4 shows ~$270M more AUA than adjacent weekdays.
Not duplicate rows -- same account count, genuinely different total_aua values. This is an upstream
data construction issue (the platform was built Feb-Apr 2026 and 2024 historical data was loaded
with an artifact affecting non-trading days). Wrote a briefing for DS investigation at
`data/analysis/briefing_weekend_aua_oscillation_2024.md`.

**Fix (boundary issue):** After ISO-week downsampling, track the last data point per Gregorian year
and force-include any that were absorbed into next year's ISO week. Ensures Dec 31 appears as a
distinct point; frontend Y8 annual aggregation picks it as the last 2025 entry.

**Commit:** `31fa6522` | **File:** D_04.client_portal_summary.py

---

### 3. Advisors Tab: Travis Penfield Client/Account Count Wrong
**Symptom:** Travis showed 218 clients, 224 accounts. Known: ~514 accounts, more clients than
account count suggests (clients should be a multiple less than accounts, not almost equal).

**Root cause (client_count):** `_employee_entries_for_window` computed `client_counts` from
`cdim.groupby('primary_architect')` -- only relationships where the advisor is the primary
architect. Travis is tagged in 5 roles across many more relationships.

**Root cause (account_count):** Came from C_08 fee-detail grain -- only fee-bearing accounts
with split_pct > 0. Doesn't cover accounts where Travis is tagged but earns no fee.

**Fix:** Load `account_team` with all 5 role columns + relationship_id + total_aua. Melt to
`(account_id, relationship_id, role, advisor)` pairs, filter Unassigned. Compute:
- `tagged_account_counts`: distinct accounts per advisor across all roles (deduped)
- `tagged_client_counts`: distinct relationships per advisor across all roles
- `tagged_aua_counts`: sum of full account AUA across all roles (deduped at account level)
- `at_role_breakdown`: per-role {aua, account_count, client_count} from account_team snapshot

After fix: Travis = 513 accounts (matches Andrew's ~514), 207 relationships.

**Commit:** `e885f758` | **File:** D_00.portal_aggregates.py

---

### 4. Advisors Tab Role Toggle AUA Did Nothing
**Symptom:** Unchecking "architect" on the Advisors tab leaderboard didn't change AUA/counts.

**Root cause:** The frontend reads `role_breakdown[role].aua` to compute the filtered total.
D_00's `_employee_entries_for_window` computed `total_aua` in `role_detail` (from fee detail)
but never emitted it into the `rd` dict. `aua` was missing entirely. Also, `account_count` and
`client_count` per role were wrong: `account_count` came from fee-detail grain (only fee-bearing),
and `client_count` was the SAME advisor-total duplicated across every role.

**Fix:** Used `at_role_breakdown` (from account_team melt) to populate per-role `aua`,
`account_count`, `client_count` in the role breakdown dict. NNA/flows still from fee detail.

**Commit:** `2a9fb24a` | **File:** D_00.portal_aggregates.py

---

### 5. Leaderboard total_aua Dropped to 334m (Fee-Bearing Only)
**Symptom:** Travis Penfield AUA dropped from 413m to 334m after D_00 re-ran.

**Root cause (1):** D_00's leaderboard entry `total_aua` came from the fee detail (C_08), which
only covers fee-bearing accounts. D_04's `build_leaderboard` was supposed to override this with
D_02's tagged AUA. But D_04 Step 11 ran AFTER `build_leaderboard` and wrote a verbatim pass-through
of D_00's raw `employee_leaderboard.json` to `platinum/firm/employee_leaderboard.json`, clobbering
the corrected value.

**Root cause (2):** Even without the clobber, D_00's raw leaderboard had fee-bearing AUA not tagged.

**Fix (D_00):** Compute `tagged_aua_counts` from the account_team melt (same dedup logic as tagged
client/account counts). Use it as `total_aua` in the leaderboard entry. Fee-detail AUA is now only
used for `fee_breakdown.fee_paying.aua`.

**Fix (D_04):** Removed `employee_leaderboard.json` from Step 11's verbatim pass-through list.
`build_leaderboard()` owns that platinum path; Step 11 was clobbering it.

**Commit:** `afa7aed3` | **Files:** D_00.portal_aggregates.py, D_04.client_portal_summary.py

---

### 6. Total | Fee-Paying | No Fee Toggle (New Feature)
**Feature:** Andrew requested a three-way toggle on the Top Performers panel. Labels confirmed:
`Total | Fee-Paying | No Fee`.

**Implementation:** Added `fee_breakdown` dict to every leaderboard entry:
```python
'fee_breakdown': {
    'fee_paying': { aua, account_count, client_count, nna, inflows, outflows },
    'no_fee':     { aua, account_count, client_count, nna=0, inflows=0, outflows=0 }
}
```
- `fee_paying.aua` = C_08 fee-detail AUA (accounts with split_pct > 0)
- `no_fee.aua` = tagged_aua - fee_paying_aua
- `no_fee.nna` = 0 (canonical NNA not yet split at fee-grain; DE task to note in tooltip)
- `client_count` = 0 in both buckets (fee/non-fee relationship mapping not yet available)

**Commit:** `0024b53c` | **File:** D_00.portal_aggregates.py  
**DE follow-on:** Task order issued (committed separately by DE) for frontend toggle implementation.

---

### 7. Unresolved/Unassigned in top_architects
**Fix:** Filtered `['Unresolved', 'Unassigned', '']` from `latest_adv` before `.nlargest()` call
in `build_timeseries_chart`. Promotes the next real advisor into the top-N instead of Unresolved
occupying a named slot. Unresolved NNA still rolls into the aggregate (correct behavior, per DE
commit `68d14a3` which handled the frontend side).

**Commit:** `73c7ae21` | **File:** D_00.portal_aggregates.py

---

### 8. D_00 Refactor: Split into D_00 / D_00b / D_00c
**Motivation:** D_00 had grown to 2,834 lines with 37 functions. Andrew requested the split.

**Result:**

| File | Lines | Responsibility |
|------|-------|----------------|
| `D_00.portal_aggregates.py` | ~370 | clients_tab, header_metrics, filters, snapshots, view parquets |
| `D_00b.portal_timeseries.py` | ~490 | timeseries_chart.json (geo/adv/NNA/growth/CLA/aua_mix) |
| `D_00c.portal_leaderboard.py` | ~320 | employee_leaderboard.json (fee detail + all breakdowns) |
| `lib/gold_utils.py` | ~100 | Shared: _load_parquet, _save_json, _safe_int, date helpers |

`gold_dispatch.sh` updated: downstream chain is now `D_00 → D_00b → D_00c → D_01 → D_02 → D_03 → D_04`.
GROUP_D and CATALOG updated to include D_00b and D_00c.

All three scripts independently load their own source parquets (no intermediate S3 pass). Shared
utilities live in `lib/gold_utils.py` which all three import; fixes propagate to all in one place.

**Commit:** `9d824fc2` | **Files:** D_00, D_00b, D_00c, lib/gold_utils.py, gold_dispatch.sh

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| comp-pipescript | `comp-pipescript io D_00` | Used to understand I/O before refactor; confirmed 5 outputs (2 to D_04, 3 view parquets) |
| comp-pipescript | `comp-pipescript io D_01` | Traced geo bell curve data source; confirmed D_01 reads accounts_dimension |
| Manual S3 query | Python boto3 queries on `timeseries_chart.json` and `cumulative_chart.json` | Root-caused the annual AUA discrepancy to ISO week boundary in `_weekly_downsample` |

---

## Files Modified

| File | Change |
|------|--------|
| `D_01.partner_analytics.py` | geo bell curve total_dist filtered to known_states |
| `D_04.client_portal_summary.py` | _weekly_downsample year-end enforcement; Step 11 clobber removed |
| `D_00.portal_aggregates.py` | All leaderboard fixes + refactor (clients/header/filters/snapshots only) |
| `D_00b.portal_timeseries.py` | NEW -- timeseries chart extracted from D_00 |
| `D_00c.portal_leaderboard.py` | NEW -- leaderboard extracted from D_00 |
| `lib/gold_utils.py` | NEW -- shared utilities |
| `gold_dispatch.sh` | Added D_00b, D_00c to catalog, chains, and groups |
| `data/analysis/briefing_weekend_aua_oscillation_2024.md` | NEW -- investigation brief for DS |

---

## S3 Deployments

All scripts uploaded to `s3://opal-data-bd/code/gold/` after each fix and after the refactor.

| Script | SHA | Status |
|--------|-----|--------|
| D_01 | 06074050 | Deployed |
| D_04 | 31fa6522 | Deployed |
| D_00 | 9d824fc2 | Deployed (final post-refactor) |
| D_00b | 9d824fc2 | Deployed (new) |
| D_00c | 9d824fc2 | Deployed (new) |
| lib/gold_utils.py | 9d824fc2 | Deployed (new) |
| gold_dispatch.sh | 9d824fc2 | Deployed |

---

## Pending (AE re-run needed)

All changes require AE to trigger a gold run. Correct order:
```
D_00 → D_00b → D_00c → D_01 → D_02 → D_03 → D_04
```
Or via dispatch: `bash /tmp/gold_dispatch.sh --chain downstream --bg`

After re-run, verify:
- GEO bell curve count == sum of radial segment account_counts
- Annual stacked bar for 2025 shows 1.46B (not 1.51B); 2024 shows 963m (not 1.23B)
- Travis Penfield: 513 accounts, 207 clients, 413m AUA
- Role toggle changes AUA (architect uncheck should drop by ~architect-role AUA)
- Total|Fee-Paying|No Fee toggle functional in Top Performers panel

---

## Open Investigations

- **Weekend AUA oscillation (2024 Q2-Q4):** $270M excess on every non-trading day. Data quality
  issue in `account_performance.parquet` for that date range. Not a gold script bug. Brief filed at
  `data/analysis/briefing_weekend_aua_oscillation_2024.md`. Needs DS investigation into the
  historical data construction pipeline.
