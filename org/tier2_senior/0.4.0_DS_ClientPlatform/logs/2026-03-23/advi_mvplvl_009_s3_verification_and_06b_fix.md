# ADVI_MVPLVL.009 S3 Verification + 06b Advisor ID Fix -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-23
**Branch:** CLOUD
**Task Order:** ADVI_MVPLVL.009-ds (verify S3 data)

---

## Objective

Verify that gold layer S3 artifacts exist and are well-formed for the two broken views
(Mix toggle + Books composition), then investigate and fix any discrepancies found.

## Work Completed

### Phase 1: S3 Verification (all 3 artifacts exist)

| Artifact | S3 Key | Status | generated_at |
|----------|--------|--------|-------------|
| firm_mix_views.json | `gold/firm_mix_views.json` | EXISTS | 2026-03-20T22:24:58Z |
| firm_composition.json | `gold/views/firm_composition.json` | EXISTS | 2026-03-20T23:31:36Z |
| Per-advisor mix.json | `gold/advisors/{name}/mix.json` | 19 files | 2026-03-20 |
| Per-advisor composition.json | `gold/advisors/{id}/composition.json` | 20 files | 2026-03-20 |

### Phase 2: Issues Discovered

#### Issue 1 (HIGH): Taxonomy mismatch -- deployed script 12 uses `structured_notes` instead of `alternatives`
- **firm_composition.json** has 5 classes: equity, fixed_income, **structured_notes**, cash, other
- Expected 4-class taxonomy: equity, fixed_income, **alternatives**, cash (+ other residual)
- **Root cause:** The deployed version of script 12 on S3 (`s3://opal-data-bd/code/gold/12_build_composition_artifacts.py`, uploaded 2026-03-19 11:07) is the **pre-ETFClassifier** version with inline classification that produces `structured_notes`. The repo version was migrated to ETFClassifier (commit `5c6fd9d0`, CLSPT2.003) which correctly produces `alternatives`, but **was never deployed to EC2**.
- DynamoDB `bd-securities` table has only: equity (2994), fixed_income (1407), alternatives (802). No `structured_notes`.
- **Fix:** Deploy the current repo version of script 12 to S3 and re-run gold.

#### Issue 2 (HIGH): Advisor ID format inconsistency between scripts 06b and 12
- Script 06b writes: `gold/advisors/Josh Henson/mix.json` (raw display name with spaces)
- Script 12 writes: `gold/advisors/josh_henson/composition.json` (snake_case via `_advisor_id()`)
- Lambda uses a single `advisor_id` from URL path for both files. One format will always 404.
- **Root cause:** Script 06b passes raw architect name as `advisor_id` to `_write_advisor_mix()` without sanitization.
- **Fix applied:** Added `_advisor_id()` function to 06b (matching script 12 exactly), and updated the `_write_one_advisor()` call site to sanitize before writing to S3.

#### Issue 3 (MEDIUM): Only 1 period per granularity in firm_mix_views.json
- quarterly=1, monthly=1, annually=1 (all same data point: 2026-Q1/2026-03/2026)
- Stacked bar will render but with no historical depth.
- **Root cause:** Script 06b ran in incremental mode with only 1 partition available. Full run (or accumulated incremental runs over time) would produce more periods.
- **Not a code bug.** Needs a full rebuild.

#### Issue 4 (MEDIUM): Cash=0.0 in firm_mix_views.json despite $24M cash in composition
- Script 06b classifies into `_MIX_ASSET_CLASSES = ['equity', 'fixed_income', 'alternatives']` with everything defaulting to equity. Cash is then computed as `total_aua - classified_sum` which equals 0 when positions sum = total.
- Script 12 has explicit cash classification via keyword matching (CASH, SWEEP, MONEY MARKET).
- **Design difference between scripts.** Script 06b's cash-as-residual approach will show 0 cash when position values fully account for total AUA. Script 12's explicit classification shows $24M. The scripts are inconsistent.

### Phase 3: Code Fix Applied

**File modified:** `data/black_diamond/scripts/gold/06b_build_client_mix_timeseries.py`

Changes:
1. Added `import re` (needed for `_advisor_id()`)
2. Added `_advisor_id()` function matching script 12's sanitization exactly:
   - `name.lower().strip()` -> replace non-alphanumeric/underscore with `_` -> strip leading/trailing `_` -> truncate to 60 chars
   - Matches ClientsTab.tsx:383 JavaScript equivalent
3. Updated `_write_one_advisor()` to use `_advisor_id(adv_name)` for S3 key and daily file reads, while preserving raw name as `advisor_name` in the JSON payload
4. Updated stale docstrings: `structured_notes` -> `alternatives` in output schema docs (3 occurrences)

## Decisions Made

- **Decision:** Fix advisor ID format in 06b to match script 12's snake_case convention.
  **Rationale:** Script 12 was written more recently and its `_advisor_id()` sanitization matches the frontend's JavaScript equivalent. The Lambda serves both files using the same path parameter, so they must agree.

- **Decision:** Do NOT fix Cash=0 discrepancy now.
  **Rationale:** Requires deeper analysis of whether 06b should adopt script 12's explicit cash classification or whether the residual approach is intentional. The frontend already needs to merge cash->Other for display per task order constraints.

## Files Modified

- `data/black_diamond/scripts/gold/06b_build_client_mix_timeseries.py` -- added `_advisor_id()`, fixed advisor S3 keys, updated docstrings

---

## Current State
> **This section is the primary handoff point for the moltbot continuity agent.**

**Status:** IN PROGRESS
**Active branch:** `CLOUD`

Script 06b has been fixed locally (advisor ID format + stale docstrings). The fix is uncommitted.
The deployed version of script 12 on S3 is stale (pre-ETFClassifier, uses `structured_notes`
instead of `alternatives`). The repo version is correct but needs to be deployed.

Both scripts need to be deployed to S3 and a full gold rerun is needed to regenerate all
artifacts with the correct taxonomy and consistent advisor IDs.

## Next Steps
> **Ordered list. Execute top-to-bottom.**

1. **Commit the 06b fix** -- `git add data/black_diamond/scripts/gold/06b_build_client_mix_timeseries.py && git commit --author="0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>" -m "fix(bd-gold): normalize 06b advisor IDs to snake_case (ADVI_MVPLVL .009)"`
2. **[AE_PartnerETL] Deploy BOTH scripts 06b and 12 to S3** -- upload current repo versions to `s3://opal-data-bd/code/gold/` (replaces stale pre-ETFClassifier script 12)
3. **[AE_PartnerETL] Run full gold rebuild** -- scripts 06b and 12 must both run to regenerate all artifacts with:
   - Correct `alternatives` taxonomy (not `structured_notes`)
   - Consistent snake_case advisor IDs across mix.json and composition.json
   - Ideally multiple periods in firm_mix_views.json (full mode with historical partitions)
4. **[AE_PartnerETL] Clean up orphaned display-name advisor folders** -- old `gold/advisors/Josh Henson/` paths should be deleted after new snake_case paths are confirmed
5. **[DS] Re-run S3 verification** -- confirm all 3 artifacts have correct taxonomy and consistent advisor IDs post-rebuild
6. **[DE/RD] Proceed with frontend wiring fixes** -- per MVPLVL-006 thread consensus (remove fetchComposition, normalize cash->Other, add L3/L4 per-class Other)

**Files to touch next:**
- None (06b fix is complete; remaining work is deployment + gold rerun owned by AE)

**Do NOT:**
- Deploy the old S3 version of script 12 (it uses `structured_notes`)
- Run gold incremental-only (need full rebuild for historical periods and to regenerate all advisor folders with new IDs)
