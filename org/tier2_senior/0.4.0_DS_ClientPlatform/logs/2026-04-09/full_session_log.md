# Full Session Log -- 2026-04-09

**Agent:** 0.4.0_DS_ClientPlatform  
**Date:** 2026-04-09  
**Project:** ADVI_49PUSH  
**Status:** COMPLETE. All changes committed, pushed, deployed to S3.

---

## Overview

Live QA session with Andrew walking through the portal. Reactive fixes to observed data
correctness issues, followed by the D_00 refactor, then infrastructure/pipeline work.
No pre-assigned task orders -- all work was Andrew-directed based on what he saw.

17 commits this session. All deployed to S3.

---

## Work Log (chronological)

---

### 1. GEO Bell Curve Count vs Radial Sum Mismatch
**Commit:** `06074050` | **File:** D_01.partner_analytics.py

**Symptom:** Snapshot-GEO-AUA bell curve: 6,046 accounts. Sum of radial segments: 5,566.

**Root cause:** `total_dist` in `D_01.build_geo_view` used `acct_geo` (all accounts from the
left-merge, including ~480 with `client_state='Unknown'` or foreign states). The segment
loop only iterates `geo_day` (which filters out Unknown/empty/null). Bell curve included 480
accounts that appeared in no radial bucket.

**Fix:** `acct_geo_radial = acct_geo[acct_geo['client_state'].isin(known_states)]`. Both
`total_dist` and `metrics.account_count` now use this filtered set.

---

### 2. Add client_city to D_00 accounts_dimension Load
**Commit:** `d9d9401f` | **File:** D_00.portal_aggregates.py

Uncommitted working tree change from previous session (starter for city NNA drill follow-on).
Committed. No functional change to outputs -- just ensures `client_city` is available for
future work.

---

### 3. Continuous-GEO Stacked Bar vs Assets Overview Annual AUA Mismatch
**Commit:** `31fa6522` | **File:** D_04.client_portal_summary.py

**Symptom:** Every year except 2023 shows a discrepancy between the annual stacked bar and
the header AUA. 2025: bar=1.51B, header=1.46B. 2024: bar=1.23B, header=963m. 2023: exact
match. 2022: 130m vs 122m. 2021: 58.4m vs 59.2m.

**Root cause:** `_weekly_downsample` uses ISO year for week keys (`2026-W01`). Dec 29-31 of any
year that falls in ISO week 1 of the NEXT year gets stored under that next-year key. The last
kept point for Dec 2025 was Dec 28 (last Sunday of ISO week 52 of 2025, AUA=1.51B). The header
uses `_build_static_aua_periods` which snapshots Dec 31 directly (AUA=1.46B). 2023 matched
because Dec 31, 2023 was a Sunday (last day of its own ISO week).

**Investigated further:** The 2024 gap (1.23B vs 963m, ~$270M) was too large for a 2-day
boundary issue. Root-caused to `account_performance.parquet` having structurally inflated
AUA on every weekend and market holiday in 2024 Q2-Q4. Same account count each day, genuinely
different `total_aua` values -- BD pricing artifact from how historical data was constructed.
Not a gold script bug. Wrote investigation briefing at
`data/analysis/briefing_weekend_aua_oscillation_2024.md`.

**Fix:** After ISO-week downsampling, track the last data point per Gregorian year (`year_last`)
and force-include any that were absorbed into next year's ISO week. Dec 31 now appears as a
distinct point.

---

### 4. Leaderboard client_count and account_count: All-Role Fix
**Commit:** `e885f758` | **File:** D_00.portal_aggregates.py

**Symptom:** Travis Penfield: 218 clients, 224 accounts (known: ~514 accounts).

**Root cause (client_count):** `_employee_entries_for_window` computed client counts from
`cdim.groupby('primary_architect')` -- only relationships where the advisor is the primary
architect. Travis is tagged in all 5 roles across many more relationships.

**Root cause (account_count):** Came from C_08 fee-detail grain -- fee-bearing accounts only
(split_pct > 0). Non-fee accounts excluded.

**Fix:** Load `account_team` with all 5 role columns + relationship_id + total_aua. Melt to
(account_id, relationship_id, role, advisor) pairs, filter Unassigned. Compute tagged counts
across all roles, deduplicated at account level. Post-fix: Travis = 513 accounts, 207 relationships.

---

### 5. Exclude Unresolved/Unassigned from top_architects
**Commit:** `73c7ae21` | **File:** D_00.portal_aggregates.py

Per DE commit `68d14a3` which filtered them on the frontend. Added data-level fix:
filter `['Unresolved', 'Unassigned', '']` from `latest_adv` before `.nlargest()`. Promotes
the next real advisor into top-N. Their NNA/AUA still rolls into the aggregate.

---

### 6. Role Toggle AUA Fix -- role_breakdown Now Emits aua per Role
**Commit:** `2a9fb24a` | **File:** D_00.portal_aggregates.py

**Symptom:** Unchecking "architect" on the Advisors tab leaderboard didn't change AUA.

**Root cause:** Frontend reads `role_breakdown[role].aua` to compute filtered total. D_00 never
emitted `aua` in the role breakdown dict (computed `total_aua` in `role_detail` but didn't put
it in `rd`). `account_count` was fee-detail-only; `client_count` was the same advisor-total
duplicated across every role.

**Fix:** Used `at_role_breakdown` (from account_team melt) to populate per-role `aua`,
`account_count`, `client_count`. NNA/flows still from fee detail.

---

### 7. Leaderboard total_aua: Tagged AUA + Step 11 Clobber Fix
**Commit:** `afa7aed3` | **Files:** D_00.portal_aggregates.py, D_04.client_portal_summary.py

**Symptom:** Travis Penfield AUA dropped from 413m to 334m after D_00 re-ran.

**Root cause (1 -- D_00):** Entry `total_aua` came from C_08 fee-detail (fee-bearing accounts
only = ~334m). D_04's `build_leaderboard` was supposed to override with D_02's tagged AUA.

**Root cause (2 -- D_04):** Step 11 (firm pass-throughs) ran AFTER `build_leaderboard` and
wrote a verbatim copy of D_00's raw `employee_leaderboard.json` to
`platinum/firm/employee_leaderboard.json`, clobbering the corrected value.

**Fix (D_00):** Compute `tagged_aua_counts` from account_team melt (all-role, deduped). Use
as `total_aua` on every leaderboard entry. Fee-detail AUA now only used for `fee_breakdown.fee_paying.aua`.

**Fix (D_04):** Removed `employee_leaderboard.json` from Step 11's verbatim pass-through list.
`build_leaderboard()` owns that path exclusively.

---

### 8. Total | Fee-Paying | No Fee Toggle
**Commit:** `0024b53c` | **File:** D_00.portal_aggregates.py

Andrew confirmed toggle labels: **Total | Fee-Paying | No Fee**.

Added `fee_breakdown` dict to every leaderboard entry:
```json
{
  "fee_paying": { "aua": <C_08 fee AUA>, "account_count": <fee accts>, "nna": <fee NNA>, ... },
  "no_fee":     { "aua": <tagged - fee>, "account_count": <tagged - fee accts>, "nna": 0, ... }
}
```
`no_fee.nna = 0` (canonical NNA not yet split at fee grain). `client_count = 0` in both buckets
(fee/non-fee relationship mapping not yet available). DE issued companion task order for frontend
toggle (committed by DE as `c8e12cee`).

---

### 9. D_00 Refactor: Split into D_00 / D_00b / D_00c + lib/gold_utils.py
**Commit:** `9d824fc2` | **Files:** D_00, D_00b (new), D_00c (new), lib/gold_utils.py (new), gold_dispatch.sh

Andrew: "D_00 is getting so large I'm beginning to think we should break it up."

D_00 was 2,834 lines with 37 functions. Split into:

| File | Lines | Owns |
|------|-------|------|
| `D_00.portal_aggregates.py` | ~370 | clients_tab, header_metrics, filters, snapshots, view parquets |
| `D_00b.portal_timeseries.py` | ~490 | timeseries_chart.json (geo/adv/NNA/growth/CLA/aua_mix) |
| `D_00c.portal_leaderboard.py` | ~320 | employee_leaderboard.json (all role/fee breakdowns) |
| `lib/gold_utils.py` | ~100 | Shared: _load_parquet, _save_json, _safe_int, date helpers |

`gold_dispatch.sh` updated: downstream chain now `D_00 → D_00b → D_00c → D_01 → D_02 → D_03 → D_04`.
All three scripts independently load their own source parquets.

---

### 10. advisor_id on Leaderboard Entries
**Commit:** `7bd28205` | **Files:** D_00c.portal_leaderboard.py, D_04.client_portal_summary.py

Investigated DE commit `b0554bc` which reads `e.advisor_id` from leaderboard entries. D_04
had added `advisor_id` to `_LEADERBOARD_ENTRY_FIELDS` (commit `28727815`) but the value was
always `None` because D_00c never generated it. Stripped on every entry.

**Fix (D_00c):** Generate `advisor_id = _advisor_id(name)` slug on every entry (identical regex
to D_02: "Travis Penfield" → "travis_penfield").

**Fix (D_04 `build_leaderboard`):** Extract canonical `advisor_id` from the S3 key path of each
book.json file (`gold/entities/advisors/{advisor_id}/book.json` → folder name is authoritative).
Build `name_to_id` dict alongside `name_to_tagged`, override entry's `advisor_id` in trim loop.
Book.json files do NOT have an `advisor_id` field -- the folder name is the canonical ID.

---

### 11. gold_dispatch.sh Auto-Shutdown After Chain Runs
**Commit:** `be3b9912` | **File:** gold_dispatch.sh

Andrew observed: gold runner instance was idle for 30+ minutes after chain completed, burning
~$4/hr on a c6i.16xlarge. No shutdown logic existed in the dispatch script.

Added: after foreground chain execution + log upload, if `MODE="chain"` and not `--dry-run`:
```bash
sudo shutdown -h +2   # 2-minute delay so I/O can finish
```
Added `--no-shutdown` flag to suppress (for debugging/manual runs). Flag passes through to
background re-invocation. Single and group runs do NOT auto-shutdown.

Also investigated the timing issue: AE manually triggered a full chain at 21:21 UTC (5:21 PM ET)
before silver pipelines completed (realized/allocation fire at 21:38-22:00 UTC). This caused
D_00 to generate timeseries_chart.json with April 7 data. The nightly fallback at 23:00 UTC
regenerated D_00/D_01 with April 8 data. Resulted in header showing 1.60B (stale) while
snapshot/books showed 1.68B. See item 14 for full investigation.

---

### 12. MAX Window (Inception-to-Date) for Leaderboard
**Commit:** `8414688a` | **Files:** D_00c.portal_leaderboard.py, D_04.client_portal_summary.py

Per DE commit `a127b14`: frontend added Max toggle that maps to `"MAX"` key in leaderboard
windows dict, falls back to YTD if absent.

**D_00c:** `max_start = detail['date'].min()` -- earliest date in the advisor fee detail.
Calls `_employee_entries_for_window` with this start. `period_start_aua` = each advisor's
AUA at inception date (None if not yet active). NNA/inflows/outflows = cumulative since inception.

**D_04:** Added `'MAX'` to `_LEADERBOARD_WINDOWS` tuple so it passes through to platinum.
Frontend toggle will light up automatically after next gold run with no further frontend changes.

---

### 13. Weekend AUA Oscillation Investigation (2024 Q2-Q4)
**No code change.** | **Briefing:** `data/analysis/briefing_weekend_aua_oscillation_2024.md`

Andrew noticed 2024 bar gap was too large for a 2-day boundary issue. Confirmed $270M excess
on every non-trading day in 2024 Q2-Q4. Not duplicate rows. Same account count (~6,060),
genuinely different `total_aua` values per day. Consistent $270M, affects 64% of accounts.
Begins Q2 2024, gone by Q1 2025. Data quality issue from how historical data was constructed.
Briefing written for DS investigation.

---

### 14. AUA Discrepancy Investigation: 1.60B vs 1.68B
**No code change.** | **Investigation only.**

**Symptom:** Header + continuous chart: 1.60B. Snapshot (D_01) + Books tab: 1.68B.

**Root cause:** Two separate runs generated the artifacts using different account_performance
snapshots.

| Artifact | Generated at | data_as_of | AUA |
|----------|-------------|-----------|-----|
| timeseries_chart.json (header + continuous) | 22:00 UTC | Apr 7 | 1.60B |
| clients_tab.json (Books tab) | 23:05 UTC | Apr 8 | 1.68B |
| partner_analytics (snapshot) | 23:06 UTC | Apr 8 | 1.68B |

Manual chain at 21:22 UTC ran D_00 before silver had April 8 data. Nightly fallback at 23:00
UTC ran D_00/D_01 after silver completed, getting April 8. timeseries_chart.json was not
regenerated by the fallback. D_00b needs to run to fix the header and continuous charts.

**Silver AUA for April 8 (authoritative):** $1.6737B from
`silver/allocations/2026-04-08.parquet` (6,498 open accounts, 1 row/account). Account_performance
and account_team show $1.68-1.685B -- ~$9-11M above silver, consistent with pricing timing.

---

### 15. Gold Runner Instance Stopped
**No code change.** | **AWS action.**

Instance `i-01003b035d2988dfb` (`bd-gold-layer-runner`, c6i.16xlarge) had been idle for ~30
minutes after the last run completed at 23:00 UTC. Stopped via `aws ec2 stop-instances`.

---

## All Commits This Session (DS-authored)

| SHA | Description |
|-----|-------------|
| `06074050` | fix(D_01): geo bell curve count -- filter total_dist to known states |
| `d9d9401f` | fix(D_00): add client_city to accounts_dimension load |
| `31fa6522` | fix(D_04): weekly downsample preserves year-end points |
| `e885f758` | fix(D_00): leaderboard client_count and account_count -- all-role account_team |
| `73c7ae21` | fix(D_00): exclude Unresolved/Unassigned from top_architects |
| `2a9fb24a` | fix(D_00): role_breakdown emits aua/account_count/client_count per role |
| `afa7aed3` | fix(D_00/D_04): leaderboard total_aua tagged AUA; remove Step 11 clobber |
| `0024b53c` | feat(D_00): fee_breakdown for Total\|Fee-Paying\|No Fee toggle |
| `9d824fc2` | refactor(D_00): split D_00/D_00b/D_00c + lib/gold_utils.py |
| `008646a5` | log(0.4.0_DS): intermediate session log |
| `7bd28205` | fix(D_00c/D_04): emit advisor_id on leaderboard entries |
| `be3b9912` | feat(gold_dispatch): auto-shutdown after chain run |
| `8414688a` | feat(D_00c/D_04): MAX window (inception-to-date) |

---

## S3 Deployments

All scripts uploaded to `s3://opal-data-bd/code/gold/` after each fix.

Final deployed state:

| Script | Last committed SHA |
|--------|--------------------|
| D_00.portal_aggregates.py | `9d824fc2` |
| D_00b.portal_timeseries.py | `9d824fc2` (new) |
| D_00c.portal_leaderboard.py | `8414688a` |
| D_01.partner_analytics.py | `06074050` |
| D_04.client_portal_summary.py | `8414688a` |
| lib/gold_utils.py | `9d824fc2` (new) |
| gold_dispatch.sh | `be3b9912` |

---

## Compiler Tools

| Tool | Run | Result |
|------|-----|--------|
| comp-pipescript | `io D_00`, `io D_01` | Traced data sources for GEO and leaderboard fixes |
| comp-pipescript | `io D_04` | Confirmed Step 11 clobber path |
| Direct S3 query | boto3 on timeseries_chart.json, cumulative_chart.json, account_performance.parquet, account_team.parquet, silver/allocations/2026-04-08.parquet | Root-caused all AUA discrepancies with actual data |
| py_compile | All modified scripts | Clean on every change before commit |

---

## Pending (Needs Gold Run)

Next downstream run (`D_00 → D_00b → D_00c → D_01 → D_02 → D_03 → D_04`) will:

1. Regenerate `timeseries_chart.json` with April 8 data → header and continuous align at ~1.67B
2. D_00b and D_00c run for the first time as standalone scripts (first run since refactor)
3. Leaderboard: `advisor_id` on all entries, `fee_breakdown` (Fee-Paying/No Fee), `MAX` window
4. Role toggle: `aua` field now present in `role_breakdown` → unchecking architect actually drops AUA
5. GEO bell curve count matches radial sum
6. Annual stacked bars (2020-2025) all use Dec 31 snapshots

Run should happen via nightly fallback at 23:00 UTC (7 PM ET) after silver is complete.
Do NOT manually trigger before silver finishes.

---

## Open Issues

1. **Weekend AUA oscillation (2024 Q2-Q4):** $270M excess on non-trading days. Upstream data
   construction issue. Briefing at `data/analysis/briefing_weekend_aua_oscillation_2024.md`.
   Needs DS investigation.

2. **April 3-5, 2026 geo data shows 0.103B** (virtually nothing). Long weekend -- no data
   expected, Andrew confirmed. Investigate whether to exclude zero/sparse days from the
   timeseries or fill forward.

3. **fee_breakdown.client_count = 0:** Fee-paying vs non-fee relationship count not yet
   available (requires join of fee detail to account_team). Follow-on work.

4. **no_fee.nna = 0:** Canonical NNA not yet split by fee-bearing status. Would require
   joining canonical NNA parquet against fee detail account list. Follow-on work.
