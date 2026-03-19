# ADVI_BKSCMP.001 — Script 12 + Lambda v2.8 Composition Routes — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-19
**Start Time:** session start

## Objective

Implement ADVI_BKSCMP WS1 + WS2: pre-compute per-class top-9 holdings composition
artifacts for firm (N1) and all advisors (L2), then wire two new no-cache S3-proxy routes
in opal-partners-data. Unblocks `ConsolidatedOverviewPanel` which currently shows
"No allocation data" / "No holdings data" at N1 and L2 because composition endpoints
return 404.

---

## Work Completed

### 1. Task Order Audit (session start)

Reviewed all task orders before starting. Three were pending/status-unknown:
- **ADVI_MVPLVL.007** — confirmed complete (delivered under ADVI_MVP318 WS3a+WS3c: `a3903a03`,
  `6234d50c`). DE verified shape is correct (`data` key end-to-end). Marked complete.
- **ADVI_MVPLVL.008** — confirmed complete (delivered at `14b3be3d`, deployed `aef01b14`).
  Marked complete.
- **ACAT_ALLOCATIONS_RECONCILIATION-001** — confirmed superseded by NNAVAR/AUAVAR
  investigations. Marked complete/superseded.

### 2. WS1 — `12_build_composition_artifacts.py`

**File created:** `data/black_diamond/scripts/gold/12_build_composition_artifacts.py`

Key decisions:
- `_OPAL_ETF_OVERRIDES` sourced from `silver/build_canonical_prices_v2.py` (NOT 06b —
  confirmed absent by DT S-Report 2026-03-19; task order req 1 corrected by COO).
  Dict maps DIVZ/IDVZ/PFDE/PFOE/PCHI by BD asset name string to ticker.
- `classify_series()` called vectorized: `classify_series(df['ticker'], df['asset_name'])`
  (clarified by DT S-Report — task order said "per row" which was imprecise).
- Classification logic (`ETF_CLASSIFICATIONS`, `ASSET_NAME_TO_TICKER`, `classify_series`,
  regex patterns) inlined verbatim from 06b with header comment: "mirrored from 06b — keep in sync".
- `advisor_id` sanitization: `re.sub(r'[^a-z0-9_]+', '_', name.lower().strip()).strip('_')[:60] or 'unknown'`
  matches `ClientsTab.tsx:383` exactly (cross-agent consistency requirement).

Pct conventions (per PRD ADVI_BKSCMP §3):

| Field | Denominator |
|-------|-------------|
| `mix[i].pct` | `total_market_value` |
| `mix[i].top_holdings[j].pct` | `mix[i].market_value` (class AUM) |
| `top_holdings[j].pct` (root) | `total_market_value` |
| `other.pct` (root) | `total_market_value` |
| `mix[i].other.pct` | `mix[i].market_value` |

Algorithm:
1. Discover latest holdings_lots parquet (non-backfill), filter `is_open == True`
2. Apply `_OPAL_ETF_OVERRIDES` to fix null tickers
3. `classify_series(df['ticker'], df['asset_name'])` → `asset_class` column
4. Load `rel_architect_lookup.parquet` (08b output); fallback to `client_dimension.primary_architect`
5. Left-join lookup onto holdings by `relationship_id`
6. Build firm composition (all rows) → write `gold/views/firm_composition.json`
7. Loop over architects → per-advisor composition → write `gold/advisors/{id}/composition.json`
8. Skip advisors with 0 open holdings (do not write empty JSON)

Error handling: rel_architect_lookup missing → WARN + fallback; holdings_lots missing → ERROR + exit 1.

### 3. WS1 — `run_gold_layer.sh` update

Inserted `run_script "$SCRIPTS_DIR/12_build_composition_artifacts.py"` after 08b and before
06b in BOTH sections:
- Incremental: between lines 114 (08b) and 115 (06b) → now line 115
- Full: between lines 158 (08b) and 159 (06b) → now line 159

Rationale: 12 reads `rel_architect_lookup.parquet` written by 08b. Does not need account_performance
or client_performance. Does not block 06b. In incremental mode, 12 reads the holdings_lots parquet
from the last full run (script 03 is full-only) — composition artifacts update with latest architect
attribution on every daily run.

Dependency chain comments updated in both sections.

### 4. WS2 — `opal-partners-data` Lambda v2.8

Four changes:

**A. `cors_response_nocache()`** — inserted after `cors_response()` (line 119):
Identical structure, `Cache-Control: no-store, no-cache, must-revalidate`.
Position-level AUM data must not be cached anywhere in the request path.

**B. `serve_s3_json_nocache()`** — inserted after `serve_s3_json()` (line 335):
Structural copy — same S3 logic, same error handling, all `cors_response()` calls replaced
with `cors_response_nocache()`. Zero logic changes.

**C. `handle_firm_composition(bucket)`** — after `handle_advisor_mix_views`:
`return serve_s3_json_nocache(bucket, 'gold/views/firm_composition.json')`

**D. `handle_advisor_composition(bucket, advisor_id)`** — after `handle_firm_composition`:
Validates `advisor_id` (no `/` or `..`), returns `serve_s3_json_nocache(bucket, f'gold/advisors/{advisor_id}/composition.json')`.
On invalid id: `cors_response_nocache(400, {'error': 'Invalid advisor_id'})`.

**Routing** — split the existing `elif action == 'composition'` into three branches:
```
composition + entity_type==firm    → handle_firm_composition  (new, before fallback)
composition + entity_type==advisor → handle_advisor_composition (new, before fallback)
composition (all others)           → handle_books_composition (existing L3/L4, unchanged)
```
Firm/advisor dispatch appears BEFORE the generic fallback — same pattern as timeseries dispatch.

Version bumped 2.7 → 2.8. Docstring + available_routes + 404 error list updated.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| `_OPAL_ETF_OVERRIDES` from silver, not 06b | Confirmed absent from 06b by DT S-Report. Sourced from build_canonical_prices_v2.py line 69. COO corrected task order req 1 before execution. |
| classify_series vectorized call | Clarified by DT S-Report. Vectorized (Series args) not row-wise. More efficient for large holdings parquet. |
| Script 12 in incremental sequence | 12 reads rel_architect_lookup (08b output, updated daily) and holdings_lots (from last full 03 run). Composition stays current with daily architect changes without needing a full run. |
| serve_s3_json_nocache is a structural copy | Avoids logic divergence. Single responsibility: the no-cache wrapper changes ONLY the cache header. All S3 error handling, validation, and timeouts are preserved identically. |
| firm/advisor routing before generic fallback | Prevents generic fallback from routing firm/advisor to handle_books_composition (which does in-Lambda parquet compute — times out for large scopes). |

---

## Briefs Written

None — all deliverables are Lambda/gold commits routed directly to DT/AE via commit SHAs.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/12_build_composition_artifacts.py` | New script — firm+advisor composition artifacts | Yes — `1e08fc1a` |
| `data/black_diamond/scripts/gold/run_gold_layer.sh` | Insert script 12 after 08b in incremental + full | Yes — `1e08fc1a` |
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py` | v2.8 — cors_response_nocache, serve_s3_json_nocache, handle_firm_composition, handle_advisor_composition, routing split | Yes — `885719e3` |

---

## Briefs Written

None required — all gates are commit SHAs, no separate data contract changes.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Two commits on CLOUD: `1e08fc1a` (WS1 — script 12 + run_gold_layer.sh) and `885719e3`
(WS2 — opal-partners-data v2.8). Task order ADVI_BKSCMP.001 marked complete.
Also audited and closed MVPLVL.007, MVPLVL.008, ACAT_ALLOCATIONS_RECONCILIATION-001.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Deploy opal-partners-data v2.8** — gate commit `885719e3`.
   build-and-upload.sh partners-api opal-partners-data → terraform plan/apply (partners-api)
   → 0-diff → tag partners-api-v1.5.0 → push --follow-tags.

2. **[0.6.0_AE_PartnerETL] Deploy script 12 + run_gold_layer.sh, run gold** — gate commit
   `1e08fc1a`.
   - Upload `12_build_composition_artifacts.py` to `s3://opal-data-bd/code/gold/`
   - Upload updated `run_gold_layer.sh` to `s3://opal-data-bd/code/`
   - Run gold incremental (12 will execute after 08b, writes firm_composition.json +
     gold/advisors/{id}/composition.json)
   - Verify: `aws s3 ls s3://opal-data-bd/gold/views/firm_composition.json`

3. **[0.4.2_RD_AdvisorIntelligence] WS3 frontend adapter** — types.ts + ConsolidatedOverviewPanel
   holdings block (PRD §WS3). Can work in parallel — frontend gracefully falls back to synthesis
   until Lambda routes return 200. No DS gate.

4. **DS has no further action on ADVI_BKSCMP.** All DS deliverables delivered.

**Do NOT:**
- Modify `handle_books_composition` — L3/L4 path must remain untouched
- Change the `advisor_id` sanitization in script 12 without coordinating with RD
  (`ClientsTab.tsx:383` must stay in sync — cross-agent consistency requirement)
