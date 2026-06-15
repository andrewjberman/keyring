# MDPF_SCOPED.S3 — Phase-0 Investigation Log

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-28
**TO:** MDPF_SCOPED.S3.multifirm-daily-parsed-data-architecture.md
**Status:** Phase-0 complete — interim surface to COO pending approval before emit build

---

## Phase-0: Current Architecture Trace

### Portal consumer chain

```
portal/src/api/endpoints/aum.ts
  getMdpfAggregateAUATimeSeries()
    -> portal-proxy.ts: publicApiRequest('/api/general/mdpf/aggregate-aua-timeseries.json')
       -> CloudFront -> s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua_timeseries.json

portal-proxy.ts:
  getModelPortfolioBenchmarks()
    -> /api/general/benchmarks/model_portfolio_benchmarks.json
  getNonModelAssets()
    -> /api/general/portfolios/non_model_assets.json  [legacy — superseded by aggregate artifact]
```

The **new** path (currently in use for the Global view):
- `aum.ts:getMdpfAggregateAUATimeSeries()` is the primary MDPF consumer.
- Single consolidated artifact at `platinum/mdpf/aggregate_aua_timeseries.json` (294KB, updated 2026-05-28).

### Producing script + pipeline

**Gold script:** `data/mdpf/scripts/gold/mdpf_aggregate_aua.py`
- Reads feeder parquets from `s3://opal-data-mdpf/mdpf/feeds/{artifact}/{firm_id}/{date}.parquet`
- Emits per-date JSONs to `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json`
- Triggered daily by `mdpf-daily-trigger` Lambda → `mdpf-daily-runner` EC2

**Per-date S3 files:**
- `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json` — going back to 2024-11-01
- `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua_timeseries.json` — consolidated full-history blob

**Backfill/consolidation scripts:**
- `data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py` — assembles timeseries from per-date JSONs

### Current cohort-split structure

The gold script already decomposes data by `firm_id`. The `aggregate_aua_timeseries.json` structure (per `MdpfAggregateAUATimeSeries` TS interface):

```json
{
  "dates": ["2024-11-01", ...],
  "aggregate": {
    "opal_aggregate_aua": [...],
    "model_aua": [...],
    "sma_aua": [...],
    "non_model_aua": [...]
  },
  "partners": {
    "49financial": {
      "model_aua": [...], "sma_aua": [...], "non_model_aua": [...],
      "partner_custody_total": [...],
      "by_model": { "opal_short_term": { "model_value": [...] }, ... }
    },
    "inflection": {
      "model_aua": [...], "sma_aua": [...], "non_model_aua": [...],
      "partner_custody_total": [...],
      "by_model": { ... }
    }
  }
}
```

**Key insight:** The artifact is already per-firm decomposed. The `partners` field IS the per-firm view. The 3 S1 modes map to:
- Global = `aggregate.opal_aggregate_aua`
- 49 Financial = `partners['49financial']`
- Inflection = `partners['inflection']`

### Cohort logic location

The cohort-splitting logic is in the feeders + model registry — NOT in the aggregation gold script:
- `build_mdpf_wsc_inflection_feeder.py` — Inflection model positions (Eclipse → convergent schema)
- `wsb_49f_smartx_model_aua.py` — 49F SmartX model positions
- `build_mdpf_wse_49f_non_model_aua.py` — 49F non-model AUA
- `mdpf_model_registry.json` — canonical model_key → native-id mapping

The gold script (`mdpf_aggregate_aua.py`) **never branches on firm_id** — it loops over whatever `firm_id`s are in the feeders. This is the "shared parsing" design already in place.

### Shared-parsing: already achieved

Adding Cottonwood or another partner:
1. Add feeder scripts that emit to `opal-data-mdpf/mdpf/feeds/{artifact}/cottonwood/{date}.parquet`
2. Add Cottonwood's native-id column to `mdpf_model_registry.json`
3. The gold script picks it up automatically — zero central-logic edits

---

## Design: Per-firm S3 Artifact Structure

### Current state

All partner data lives inside one blob: `platinum/mdpf/aggregate_aua_timeseries.json`

The S3 workstream (S3) calls for exposing per-firm scoped artifacts so S1's dropdown modes
can fetch the artifact for the selected firm directly, rather than the FE filtering client-side
from the global blob.

### Proposed prefix convention (Q4 answer)

```
s3://opal-data-portal-v2/platinum/mdpf/
  aggregate_aua_timeseries.json            [EXISTING — keep, backward-compat for any consumers]
  aggregate_aua/{date}.json                [EXISTING — per-date daily, keep]
  
  global/aggregate_aua_timeseries.json     [NEW — cohort-aggregated Global view]
  49financial/aggregate_aua_timeseries.json [NEW — 49F scoped]
  inflection/aggregate_aua_timeseries.json  [NEW — Inflection scoped]
```

firm_id keys match the canonical `firmAccess.ts` namespace already used by ADVI:
`global` / `49financial` / `inflection`. No new namespace.

Cottonwood onboarding = add `platinum/mdpf/cottonwood/aggregate_aua_timeseries.json` — no prefix logic change.

### Per-firm artifact schema (minimal slice)

Each per-firm file is a subset of the global blob:
```json
{
  "firm_id": "49financial",
  "dates": [...],
  "model_aua": [...],
  "sma_aua": [...],
  "non_model_aua": [...],
  "partner_custody_total": [...],
  "by_model": { "opal_short_term": { "display_name": "Short-Term", "model_value": [...] }, ... },
  "meta": { "generated_at": "...", "methodology_version": "v0_9_1" }
}
```

Global artifact:
```json
{
  "firm_id": "global",
  "dates": [...],
  "opal_aggregate_aua": [...],
  "model_aua": [...],
  "sma_aua": [...],
  "non_model_aua": [...]
}
```

### Emit approach (additive, no existing artifact change)

The timeseries consolidation script (`build_aggregate_aua_timeseries.py`) already assembles
the full timeseries. The change is:
1. After building the full global timeseries, slice `partners['49financial']` → emit to `49financial/aggregate_aua_timeseries.json`
2. Slice `partners['inflection']` → emit to `inflection/aggregate_aua_timeseries.json`
3. Slice `aggregate.*` → emit to `global/aggregate_aua_timeseries.json`

Alternatively: add per-firm emit to the daily gold script (`mdpf_aggregate_aua.py`) so per-day per-firm JSONs are available at `platinum/mdpf/{firm_id}/{date}.json`, then consolidate.

### S2 Inflection rolling-365d data assessment

The Inflection feeder (`build_mdpf_wsc_inflection_feeder.py`) pulls Eclipse data.
The gold script has `INFLECTION_PARTNER_ONBOARD_DATE = "2026-05-18"` — Inflection was
added as an MDPF partner on 2026-05-18.

**Risk:** Pre-5/18 Inflection data (rolling-365d goes back to ~2025-05-28) may not be
in the feeders — the Inflection feeder may only go back to 5/18 or later.

**S2 requirement:** the chart needs rolling-365d daily Non-Model AUA for Inflection.
Pre-5/18 = all non-model (zero model_aua). This requires either:
- Orion/Eclipse daily Inflection custody AUA going back 365d from 5/18, OR
- A backfill of Inflection's non-model AUA using the weekly AUA reference data
  (`data/mdpf/reference/andrew_weekly_aua_20260518.csv` — already exists for this purpose)

**Action needed:** DS~B needs to verify the Inflection feeder's date coverage before S2 can be GO'd.

---

## Q4 Surface to COO: Prefix Proposal

**Q4 answer:** `platinum/mdpf/{firm_id}/aggregate_aua_timeseries.json`
- firm_ids: `global`, `49financial`, `inflection` (matches firmAccess.ts canonical namespace)
- Backward-compat: existing `platinum/mdpf/aggregate_aua_timeseries.json` stays
- CloudFront routing: new `/api/general/mdpf/{firm_id}/aggregate-aua-timeseries.json` paths (AE adds CF rules, or portal-data-proxy Lambda handles path routing — coordinate with AE 0.7.0_AE_CloudOps)

---

## Compiler Tool Output

```
comp-pipescript io <script>  -- pending (will run before any edits to build_aggregate_aua_timeseries.py)
```

---

## Phase-1 Build (COMPLETE)

**Commit:** `6b21c8cf4` pushed to CLOUD (`f7fc01088`)
**Script:** `data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py`
- Added `slice_per_firm()` — data-driven, loops over `artifact["partners"]`, no firm_id branching
- `--upload` now also emits per-firm slices
- `--out-per-firm-dir` for local dry-run

**S3 artifacts uploaded:**
```
platinum/mdpf/global/aggregate_aua_timeseries.json       36KB
platinum/mdpf/49financial/aggregate_aua_timeseries.json  91KB
platinum/mdpf/inflection/aggregate_aua_timeseries.json   64KB
platinum/mdpf/aggregate_aua_timeseries.json             294KB (rebuilt, backward-compat)
```

## S2 Granularity Finding

- `andrew_weekly_aua_20260518.csv`: 1 Inflection data point (2026-05-15, $203.87M total, weekly)
- Inflection feeder: starts 2026-05-18 (10 days only)
- Platinum artifact: null for Inflection pre-5/15/2026 across full 400-date window
- **No pre-5/18 Inflection AUA data (daily or weekly) in any MDPF source**
- Andrew decision needed: accept null pre-5/18 OR source Orion daily history backfill (~1-2 day DS effort)

## Current State

RAVC2-Request sent to COO (CC CTO) at 20260528T202456Z.
Awaiting COO RAVC2-Accept + AE CF routing + Andrew S2 data-granularity decision.

## Next Steps

- [COO] RAVC2-Accept on S3 per-firm emit
- [AE 0.7.0_AE_CloudOps] Add CF/Lambda routing for `/api/general/mdpf/{firm_id}/aggregate-aua-timeseries.json` (TF-only)
- [Andrew via COO] S2 decision: accept null pre-5/18 OR Orion daily backfill
- [RD/FE] S1 can wire 49F/Inflection mode fetches against live per-firm artifacts once AE routes CF
