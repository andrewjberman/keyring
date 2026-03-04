# BD Publisher adv_drill + cla Timeseries Implementation — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-04
**Start Time:** session start
**End Time:** in progress

## Objective

Implement ADVI-004 A1 (adv_drill) and A2 (cla timeseries) in bd-portal-publisher Lambda
per the binding contract agreed in ADVI-004 Pattern 0 thread receipt. Both are additive
keys on timeseries_chart.json. Update data_contract.xml as DC.1 gate before DT deploy.

---

## Work Completed

### 1. DC Task Order Assessment

DC task order (`data_contract.md`) already marked `complete` from 2026-03-02 — it was the
baseline contract creation. data_contract.xml was adequate to start A1+A2. adv_drill and
cla entries needed to be added as part of A1+A2's own DC.1 requirement.

### 2. A2.0 Pre-Check: primary_city Confirmed

Read `data/black_diamond/scripts/gold/04_build_client_dimension.py`. Confirmed:
- `primary_city` is defined at line 17 (schema comment) and written at lines 267-268.
- The Lambda's `load_all()` was NOT loading it (not in the cdim column prune list).
- CTO scope correction validated: `geo_city_drill` IS implementable as Lambda-only change.

### 3. A1: adv_drill Implementation

Added `adv_drill` to `build_timeseries_chart()` in
`infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py`.

Key decisions:
- Expanded `perf_cohort` merge to include `relationship_name`, `primary_architect`,
  `primary_state`, `primary_city` from cdim (one merge serves A1 + all CLA sub-views).
- Category key format: `"{relationship_name} ({relationship_id})"` (fallback to
  relationship_id if name absent) — collision-safe per ADVI-004 contract.
- `TOP_N_CLIENTS_PER_ARCH = 8` constant added.
- adv_drill keys iterate `adv_categories` (excluding "Other"); absent from result if empty.

### 4. A2: cla Implementation

Added `cla` dict to `build_timeseries_chart()` output.

Sub-views implemented:
- `cla.total`: firm-wide NMNC/NMEC AUA reusing `perf_cohort` (same cohort column).
- `cla.geo_drill`: per-state 2-series NMNC/NMEC; keys match `geo.categories` exactly.
- `cla.adv_drill`: per-architect 2-series NMNC/NMEC; keys match `adv.categories` exactly.
- `cla.geo_city_drill`: per-state-city NMNC/NMEC using `cdim.primary_city` (CTO correction).
  `MAX_CLA_CITIES = 9` constant added.
- Helper `_cla_view(df_subset)` DRYs the groupby/unstack pattern used by all 4 sub-views.

NMNC/NMEC rule: months_since_first <= 12, verified against existing aua view logic —
no new classification rule introduced.

### 5. data_contract.xml Updated (DC.1 Gate)

Added `adv_drill` and `cla` key definitions to the timeseries_chart.json source block
(Source 2) under AdvisorIntelligence page_contracts. Documented:
- adv_drill: structure, category key format, TOP_N_CLIENTS_PER_ARCH, data source files,
  note on primary_architect current-snapshot limitation.
- cla: all 4 sub-keys, NMNC/NMEC rule with exact formula, source files, geo_city_drill
  derivation from cdim.primary_city with script 04 line references.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Expand perf_cohort merge (not separate join) | One merge for all new views; avoids redundant S3 parquet reads |
| _cla_view() helper function | 4 sub-views share identical groupby/unstack pattern; DRY |
| primary_city NOT added to cdim for other outputs | Additive only — existing column prune preserved for memory |
| cla.geo_city_drill conditional on `if cla_geo_city_drill` | Omit key if no city data (consistent with geo_drill pattern) |
| adv_drill conditional on `if adv_drill` | Omit if no architects in top list |
| Iterate adv_categories (not top_architects) for adv_drill | adv_categories is the canonical list including ordering used by portal drillParent lookup |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` | Added TOP_N_CLIENTS_PER_ARCH + MAX_CLA_CITIES constants; primary_city to cdim load; expanded perf_cohort merge; adv_drill and cla blocks in build_timeseries_chart() | Yes — `5f60d30e` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/data_contract.xml` | Added adv_drill and cla key docs to timeseries_chart.json source block; updated date to 2026-03-04 | Yes — `5f60d30e` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI-004-adv_drill_cla.md` | Status: pending -> complete | Yes — `5f60d30e` |

---

## Blockers

None for A1+A2.

---

## Current State

**Status:** IN PROGRESS (A1+A2 complete; A3/A4/A5 pending)
**Active branch:** `CLOUD`

ADVI-004 A1+A2 committed at `5f60d30e`. Lambda syntax verified (ast.parse). data_contract.xml
updated and committed in same commit — DT deploy gate satisfied for Stream B1. Next work: A3
(ADVI-005 stacked_bar + rolling_1y in script 10), then A4 (script 09 bell curve verification),
then A5 (opal-users-v2 DynamoDB investigation).

---

## Next Steps

1. **[0.4.0_DS] Implement A3** — ADVI-005 task order: stacked_bar + rolling_1y in
   `data/black_diamond/scripts/gold/10_generate_advisor_rolling_flows.py`.
   Start with A3.0 pre-check (actual min date of parquet data).
2. **[0.4.0_DS] Verify A4** — script 09 bell curve abs() fix verification (commit 8247c6d0).
   Read script, inspect S3 thresholds.
3. **[0.4.0_DS] Investigate A5** — opal-users-v2 DynamoDB schema for JWT->advisor mapping.
4. **[0.4.0_DT_ClientPlatform] Deploy Stream B1** — bd-portal-publisher Lambda via Terraform
   after this session log is committed. Commit hash: `5f60d30e`.
   Follow Lambda Deployment Protocol. Run build-and-upload.sh for bd-portal-publisher,
   then terraform plan/apply in infra/aws/terraform/bd-pipeline/.

**Do NOT:**
- Re-enable the `build_partner_analytics()` call in lambda_handler (DISABLED comment is intentional).
- Add colorMap to timeseries_chart.json (explicitly excluded from ADVI-004 contract).
- Modify existing aua/nna/geo/adv/geo_drill keys.
