# ADVI_MVP318.001 DS Commits — WS1, WS2+WS3a, WS3c, WS5 — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-18
**Start Time:** session start
**End Time:** session end

## Objective

Commit all pending DS deliverables for the ADVI_MVP318 sprint: WS1 bd-portal-publisher
fix, D4+WS3a bd-portal-advisor-publisher (architect override + advisor timeseries writers),
WS3c opal-partners-data new advisor route handlers, and WS5 script 10 confirmation.

---

## Work Completed

### 1. WS1 — bd-portal-publisher diff verification and commit

Read the uncommitted diff (+17 lines) in `bd-portal-publisher/lambda_function.py`.

**Finding:** The diff is NOT WS1 Prescription A (geo_us_for_snap date anchor fix in
`build_snapshots()`). The actual changes are ADVI_MVPLVL.006 leaderboard window additions:
- Added MTD calendar window (`mtd_start = pd.Timestamp(year, month, 1)`) to
  `build_architect_leaderboard()`
- Renamed `qtd` -> `QTD` and `ytd` -> `YTD` in `windows_data` and `available_windows`
- Updated comment references accordingly

Prescription A (geo_us_for_snap logic in `build_snapshots()`) was **not pre-staged**.
DT must use WS1-A diagnostic result to decide whether Prescription A is needed before
deploying bd-portal-publisher.

Committed the MVPLVL.006 changes anyway (they are valid and pending). Commit message
explicitly calls out that this is NOT Prescription A.

| Commit | SHA | Description |
|--------|-----|-------------|
| WS1/MVPLVL.006 | `eb70758d` | feat(bd-portal-publisher): add MTD window + uppercase QTD/YTD to architect_leaderboard |

### 2. WS2+WS3a — bd-portal-advisor-publisher: D4 architect override + advisor timeseries

D4 changes were already in the working tree (+32 lines uncommitted). Verified they
implement the architect override correctly per PRD:
- `load_sources()` loads `gold/views/rel_architect_lookup.parquet` with graceful Exception fallback
- `lambda_handler()` left-joins lookup onto acct, overwrites `architect` field where
  `resolved_architect` is non-null, non-empty, and not 'Unresolved'

Added WS3a code BEFORE committing (D4+WS3a batched into one commit per DT constraint):

**`build_advisor_timeseries(acct, cdim) -> None`**
- Groups post-override acct by `(date, architect)`, aggregates sum of total_aua,
  cum_inflows, cum_outflows, nna and count of unique relationship_ids per group
- Writes `gold/advisors/{advisor_id}/timeseries.json` per architect
- Shape: `{advisor_id, advisor_name, data_as_of, data: [{date, total_aua, cum_inflows, cum_outflows, nna}]}`

**`build_advisor_mix_timeseries(acct, relationship_ids_by_advisor) -> None`**
- For each advisor, loads `gold/client_timeseries/{rel_id}.json` from S3 per relationship
- Computes AUA-weighted average of equity/fixed_income/structured_notes/cash/other per date
- All pct fields 0-1 convention
- Writes `gold/advisors/{advisor_id}/mix_timeseries.json`
- Missing relationship files silently skipped (06b AP gate)
- Memory: clears date_agg per advisor; gc.collect() at end

**`build_advisor_books` refactored** to return `(books, relationship_ids_by_advisor)` tuple
(previously returned `books` list only). `lambda_handler` unpacks the tuple and passes
`relationship_ids_by_advisor` to `build_advisor_mix_timeseries`.

Steps in lambda_handler renumbered 1–7 (added Steps 5: advisor timeseries, 6: advisor mix timeseries).

| Commit | SHA | Description |
|--------|-----|-------------|
| D4+WS3a | `a3903a03` | feat(bd-portal-advisor-publisher): D4 architect override + WS3a advisor timeseries artifacts |

### 3. WS3c — opal-partners-data: advisor route handlers

Read the existing routing structure. Books endpoint parses
`/scoped/partners/books/{entity_type}/{entity_id}/{action}`. Previously only handled
`relationship`, `account`, `firm` entity types.

Added:

**`_filter_window(data_list, window) -> list`**
- Filters list of `{date, ...}` dicts to trailing window from today
- Window map: 3M=90d, 6M=180d, 1Y=365d, 2Y=730d, 3Y=1095d
- Unrecognized window returns full list unchanged
- Uses `datetime.utcnow() - timedelta(days=days)` — added `timedelta` to import

**`handle_advisor_timeseries(bucket, advisor_id) -> dict`**
- Validates advisor_id (no `/` or `..`)
- Serves `gold/advisors/{advisor_id}/timeseries.json` via `serve_s3_json`

**`handle_advisor_mix_timeseries(bucket, advisor_id, window) -> dict`**
- Validates advisor_id
- Serves `gold/advisors/{advisor_id}/mix_timeseries.json`
- If `window` param present and response 200, unwraps body JSON, filters `data` list,
  rewraps body

**Routing update in `lambda_handler`:**
- `entity_type` validation extended to include `'advisor'`
- Advisor routes dispatched BEFORE generic `timeseries` fallback to avoid collision
  with `handle_books_timeseries`
- New routes:
  - `GET /api/scoped/partners/books/advisor/{id}/timeseries?firmId=xxx`
  - `GET /api/scoped/partners/books/advisor/{id}/mix-timeseries?firmId=xxx&window=1Y`
- Version bumped from 2.6 to 2.7

| Commit | SHA | Description |
|--------|-----|-------------|
| WS3c | `6234d50c` | feat(opal-partners-data): advisor timeseries + mix-timeseries route handlers |

### 4. WS5 — Script 10 confirmation + Script 09 status

**Script 10 (`10_generate_advisor_rolling_flows.py`):**
```
git log --oneline -- data/black_diamond/scripts/gold/10_generate_advisor_rolling_flows.py
```
Result: MTD/QTD/YTD changes are committed at `9563a38d feat(bd): enrich script 10 with
MTD/QTD/YTD summary, growth, rank changes`. WS5 is **confirmed committed**. AE can upload
script 10 as-is.

**Script 09 (`09_generate_partner_analytics.py`):**
Checked for MTD/QTD/YTD window patterns. Script 09 uses quarterly/monthly/annual
granularity periods — not a rolling-window leaderboard. It does NOT produce
`architect_leaderboard.json`. The architect leaderboard is produced by
`bd-portal-publisher` Lambda (already handled in WS1/MVPLVL.006 commit above).
**Script 09 does NOT need MTD/QTD/YTD additions.** No changes required.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Commit bd-portal-publisher diff even though it is NOT Prescription A | Changes are valid MVPLVL.006 work; task order says "commit regardless — DT simply won't deploy it if Root Cause B". Commit message explicitly documents the mismatch. |
| Dispatch advisor routes BEFORE generic timeseries in routing | `action == 'timeseries'` is a generic catch-all; advisor must be checked first to avoid routing advisor timeseries requests into `handle_books_timeseries`. |
| _filter_window uses `datetime.utcnow()` not timezone-aware | Consistent with other date calculations in this Lambda; dates in data are YYYY-MM-DD strings, comparison is lexicographic. |
| build_advisor_mix_timeseries silently skips missing rel JSON | 06b AP gate may not have run for all relationships; caller cannot know which are present. |

---

## Briefs Written

None written this session — all deliverables are Lambda commits that go directly to DT
for deploy. No new output shapes or gold script changes requiring a separate data contract brief.

Data contract: `build_advisor_timeseries` and `build_advisor_mix_timeseries` output shapes
are defined in the PRD WS3 endpoint contracts. DT should reference PRD WS3 for shape.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` | MTD window + QTD/YTD uppercase in build_architect_leaderboard | Yes — `eb70758d` |
| `infra/aws/lambda/bd-pipeline/bd-portal-advisor-publisher/lambda_function.py` | D4 architect override (pre-staged) + WS3a build_advisor_timeseries + build_advisor_mix_timeseries + build_advisor_books refactor | Yes — `a3903a03` |
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py` | _filter_window helper + handle_advisor_timeseries + handle_advisor_mix_timeseries + routing + version 2.7 | Yes — `6234d50c` |

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Three commits on CLOUD: `eb70758d` (bd-portal-publisher MVPLVL.006 leaderboard windows),
`a3903a03` (bd-portal-advisor-publisher D4+WS3a), `6234d50c` (opal-partners-data WS3c
advisor route handlers). WS5 script 10 confirmed committed at `9563a38d`. Script 09
confirmed no changes needed. Task order ADVI_MVP318.001 marked complete.

**WS1 flag for DT:** The bd-portal-publisher commit `eb70758d` does NOT contain Prescription A
(geo_us_for_snap in build_snapshots). DT should run the WS1-A diagnostic before deciding
whether to deploy bd-portal-publisher. If Root Cause A, Prescription A still needs to be
written and committed separately.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Deploy bd-portal-advisor-publisher** — gate commit `a3903a03`
   on CLOUD. Batch WS2+WS3b into one deploy. build-and-upload.sh bd-pipeline bd-portal-advisor-publisher.
2. **[0.4.0_DT_ClientPlatform] Deploy opal-partners-data (partners-api)** — gate commit
   `6234d50c` on CLOUD. Deploy as partners-api v1.4.0 per WS3d.
3. **[0.4.0_DT_ClientPlatform] WS1-A diagnostic** — run `.tmp_segment_analytics_diag.py`
   to determine Root Cause A vs B. If Root Cause A, flag to DS for Prescription A code.
4. **[0.6.0_AE_PartnerETL] Upload script 10** — `10_generate_advisor_rolling_flows.py`
   confirmed committed at `9563a38d`. Upload to S3 per AE gold run task order.
5. **If Root Cause A:** DS must write Prescription A (geo_us_for_snap in build_snapshots)
   to bd-portal-publisher and commit before DT deploys that Lambda.

**Files to touch next:**
- `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` — Prescription A
  fix in `build_snapshots()` if WS1-A diagnostic confirms Root Cause A

**Do NOT:**
- Deploy bd-portal-publisher until WS1-A diagnostic result is known
- Commit bd-portal-advisor-publisher again — D4+WS3a are complete, file is frozen for DT
- Modify opal-partners-data — WS3c is complete, file is frozen for DT
