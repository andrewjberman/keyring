# Canon Interlock System Deploy (DRFR_PTMCH P6a) -- 0.5.0_AE_OpalETL

**Date:** 2026-03-12

## Objective

Deploy the Canon Interlock system for Yang data_pkl (Phase 6a). Adds a passive
observation layer to the Yang pipeline that compares each new PKL upload against
established canonical values, flags changes in the overlap region, and maintains
an incremental historical record. Never blocks or gates any pipeline step.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source (Lambda, TF, SFN, tools) | `47b55ae2` feat(yang-pipeline): add yang-canon-interlock Lambda + Branch E |
| 2 | build-and-upload.sh yang-pipeline yang-canon-interlock | SHA256: `8+OqvpzUBjkfssYqH1aGtJnqazL7/7CCF9/eCcBjDTU=` |
| 3 | Commit source map | `336551da` ci: upload yang-canon-interlock artifact [skip ci] |
| 4 | terraform init | Initialized canon_interlock module from yang-lambda |
| 5 | terraform plan | 2 to add (Lambda + log group), 1 to change (SFN definition) |
| 6 | terraform apply | 2 added, 1 changed, 0 destroyed |
| 7 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 8 | Fix: adapt Lambda to actual PKL structure | `4a733cd2` fix(yang-pipeline): adapt canon interlock to actual data_pkl structure |
| 9 | Rebuild + upload v2 | SHA256: `4Ly1yRDTy2fiMV9fOezNJ6OZtxFsNapTZHExBRXKwZ0=` |
| 10 | terraform apply (code update) | 0 added, 1 changed, 0 destroyed |
| 11 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 12 | record-deploy + tag + push | `f54f9569`, tag `yang-v2.3.0` |
| 13 | Backfill: 21 historical PKLs | 688s, 185,341 lifetime flags |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| yang-pipeline | `yang-v2.3.0` | `f54f9569` |

## Verification

- Terraform 0-diff confirmed after both applies
- Lambda `yang-canon-interlock` created: 1024MB, 120s, python3.11, pandas-pyarrow-layer:1
- Step Functions `YangDataPipeline` updated with Branch E (RunInterlock + InterlockFallback)
- Backfill completed successfully: 21 PKLs, canon frontier 2026-03-06
- S3 structure verified: `canon/data_pkl/{return_daily,return_monthly,price_monthly}/values/*.parquet`
- Interlock reports: `canon/data_pkl/interlock-reports/*.json` (21 reports)
- Archives: `canon/archive/data_pkl/*.pkl` (21 files)
- Control plane: `canon/state/control-plane.json` with data_pkl source entry

## PKL Structure Discovery

PRD assumed `dc_master['combined']` as a single wide-format DataFrame with DateTimeIndex.
Actual structure is a dict of long-format DataFrames:
- `return_daily`: (date, index_name, bbg_ticker, price, return, price_return) -- ~103K rows
- `return_monthly`: (date, index_name, bbg_ticker, dy, eps_ltm, eps_ntm, ...) -- ~28K rows, 17 cols
- `price_monthly`: (date, index_name, bbg_ticker, price) -- ~30K rows
- `asset_correlations`: dict of correlation matrices (not interlocked in P6a)

All DataFrames use RangeIndex with `date` as a column (not DateTimeIndex).
Composite key for row identity: `(date, index_name, bbg_ticker)`.

## Backfill Flag Profile

| PKL | return_daily | return_monthly | price_monthly | Status |
|-----|-------------|----------------|---------------|--------|
| 20251128 | initial | initial | initial | initial |
| 20251205-20260125 (7 files) | 0 | 0 | 0 | clean |
| 20260131 | 0 | 35,474 | 0 | flagged |
| 20260208 | 0 | 34,316 | 0 | flagged |
| 20260216 | 9 | 37,484 | 104 | flagged |
| 20260221 | 0 | 43,573 | 0 | flagged |
| 20260223-20260226 (2 files) | 0 | 0 | 0 | clean |
| 20260302 | 5 | 9,947 | 84 | flagged |
| 20260305 | 0 | 0 | 0 | clean |
| 20260308 | 298 | 12,010 | 40 | flagged |

**Key insight:** `return_daily` (price/return) is highly stable -- only a handful of flags
across 21 uploads. `return_monthly` (valuation metrics: PE, EPS, P/B, RSI, etc.) changes
frequently -- Bloomberg revises these retroactively. This is expected behavior, not a data
quality issue. The 2dp tolerance catches these valuation revisions correctly.

**Total lifetime flags: 185,341** (dominated by return_monthly valuation column revisions)

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Proceeded with P6a despite P5 pending status | P6a adds a new parallel SFN branch + new Lambda. P5 patches yang-time-machine code and creates portal-time-machine in data-refresh. No overlapping resources. Sequential terraform applies on different sessions avoid state conflicts. |
| Adapted to long-format PKL structure (not PRD's wide-format assumption) | PRD assumed `dc_master['combined']` which doesn't exist. Actual structure is dict of long-format DataFrames. Adapted interlock to use composite key (date, index_name, bbg_ticker) and compare numeric columns per sub-table. |
| Moved tag yang-v2.3.0 after code fix | Initial deploy had wrong PKL parsing. Fixed in same session, tag moved to final commit to keep single tag per feature. |
| Interlock all 3 sub-tables (not just return_daily) | return_monthly has the most change activity -- interlocking only return_daily would miss the most interesting signal. price_monthly included for completeness. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/v2_portal/yang_pipeline/canon/yang-canon-interlock/lambda_function.py` | New Lambda -- canon interlock for data_pkl | Yes -- `47b55ae2`, `4a733cd2` |
| `infra/aws/terraform/yang-pipeline/lambdas.tf` | Added canon_interlock module (1024MB, 120s, pandas layer) | Yes -- `47b55ae2` |
| `infra/aws/terraform/yang-pipeline/yang-pipeline-definition.json` | Added Branch E (RunInterlock + InterlockFallback) to ProcessFileTypes | Yes -- `47b55ae2` |
| `infra/aws/lambda/ci/lambda-source-map.json` | Added yang-canon-interlock entry | Yes -- `336551da`, `f755c4c1`, `f54f9569` |
| `tools/canon/backfill_interlock.py` | New script -- replay historical PKLs to establish canon baseline | Yes -- `47b55ae2`, `4a733cd2` |
| `tools/canon/canon_surgery.py` | New script -- CLI for manual canon correction with dry-run | Yes -- `47b55ae2`, `4a733cd2` |
| `org/tier2_senior/0.5.0_AE_OpalETL/deliverables/pipeline_inventory.xml` | Added yang-canon-interlock Lambda, updated tag to yang-v2.3.0 | Yes -- `0347815b` |
| `infra/aws/terraform/yang-pipeline/CHANGELOG.json` | Added yang-v2.3.0 entry | Yes -- `f54f9569` |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

The Canon Interlock system is deployed as `yang-v2.3.0`. The Lambda `yang-canon-interlock`
runs as Branch E of ProcessFileTypes in YangDataPipeline Step Functions, parallel to all
generators. If it fails, InterlockFallback (Pass state) activates and generators continue
normally. Backfill established canon from 21 historical PKLs with frontier at 2026-03-06.
The next live Yang pipeline execution will run the interlock against established canon.

Canon S3 structure:
- `canon/data_pkl/return_daily/values/{year}.parquet` (2020-2026)
- `canon/data_pkl/return_monthly/values/{year}.parquet` (1990-2026)
- `canon/data_pkl/price_monthly/values/{year}.parquet` (1989-2026)
- `canon/data_pkl/interlock-reports/{date}_{version}.json` (21 reports)
- `canon/archive/data_pkl/{filename}.pkl` (21 archived uploads)
- `canon/state/control-plane.json` (global + data_pkl source state)

---

## Next Steps

1. **Verify next live pipeline run** -- after the next Yang pipeline execution (nightly or manual),
   confirm the interlock branch runs, writes a report, and all generators complete normally.
   Check CloudWatch `Opal/CanonInterlock` namespace for the metric.
2. **[2.0.0_SA_COO] Mark P6a task order complete** -- all acceptance criteria met.
3. **[2.0.0_SA_COO] Phase 6b planning** -- extend interlock to model_pkl, peer_excel,
   attribution_excel, cma_excel. The Lambda already has extension points for future tables.

**Do NOT:**
- Modify any existing generator Lambda to read from `canon/`
- Add `canon/` reads to any pipeline critical path
- Gate any deployment or release on canon state
