# DS~D Session Log — 2026-05-08 — ADVI_INFNNA.TAX-ENDING-MV-REPAIR

**Agent:** `0.4.0_DS_ClientPlatform~D`
**Date:** 2026-05-08
**Session focus:** ADVI_INFNNA.TAX-ENDING-MV-REPAIR — restore Ending MV column dropped from Orion tax bronze 2026-05-07+

---

## Summary

Received COO GO on ADVI_INFNNA.TAX-ENDING-MV-REPAIR. Identified two root causes for the missing Ending MV (see Root Cause Analysis below). Fixed `create_tax_dim_queries.py` in two commits: (1) added Ending MV as an activity-type column (activityOptionId=1), (2) corrected dateRangeId to 9 (Since Inception) after discovering the Billing Dim clone's Rolling 3-Year window was understating Ending MV by ~$60M for accounts onboarded less than 3 years ago. Final bronze 2026-05-08 Inflection Ending MV = $202M, matching pre-regression 2026-05-06 baseline ($200.8M) within 2 days of market movement. Silver rebuilt and uploaded. Two commits pushed to CLOUD.

**Ancillary fix:** `INFLECTION_REP_IDS` bumped `[3, 11, 12]` → `[3, 6, 11, 12]` in the same script — required by comp-constants drift gate (SEED-INF drift, noted in RAVC).

---

## Compiler Tools — Phase 1 (Before Write)

| Tool | Run | Result |
|------|-----|--------|
| `aws s3 cp s3://opal-data-inf/bronze/orion-api/2026-05-08/tax_unrealized.csv` | Mandate 1 — confirm 32 cols pre-fix | **PASS** — 32 columns returned, "Ending MV" ABSENT at position 10. Column 10 = "LT Cost Basis". |
| `aws s3 cp s3://opal-data-inf/bronze/orion-api/2026-05-06/tax_unrealized.csv` | Mandate 2 — confirm pre-regression baseline | **PASS** — 33 columns, "Ending MV" present at position 10 (between "Tax Transitioning" and "LT Cost Basis"). `grep -c "Ending MV"` = 1. |
| `git log --oneline data/orion/manual_api/pull_inflection_performance_dim.py` | Mandate 3 — confirm PERFDIM-CREATOR anchor | **PASS** — commit `94c624901` present. |

All Phase 1 mandates PASS.

---

## Root Cause Analysis

### Root Cause 1: Column Missing from TAX_COLUMNS

`create_tax_dim_queries.py` `TAX_COLUMNS` had 32 entries — "Ending MV" was entirely absent. When the saved query was recreated (between 2026-05-06 and 2026-05-07 by the cron Lambda), the schema never requested the column, so Orion returned 32-column CSVs without it. Pre-regression CSVs had 33 columns because an older version of the saved query (or the original hand-built query) included Ending MV.

**Important distinction:** "Ending MV" in the Orion tax dim is NOT a simple path column like `Tax.Total.GainLoss`. It is an **activity-type** column (`activityOptionId=1`, path=`Activity.Value`), as confirmed by `create_unified_account_dim_query.py` (which uses the same mechanism). The `_column_blob()` function in the original script only handled simple-path columns. Fix required adding `_activity_blob()` and `_column_value()` dispatcher, and changing TAX_COLUMNS to 4-tuples `(label, kind, path_or_opt_id, ftype)`.

### Root Cause 2: Rolling 3-Year Window Understates Ending MV

After the column was restored, a fresh bronze pull returned $140M for Inflection reps vs. $200.8M pre-regression. Investigation:

- Pre-regression 2026-05-06, Inflection reps filtered: **$200.8M** (856 rows)
- Post-fix (activityOptionId=1, Rolling 3-Year), Inflection reps: **$140M** (858 rows)
- Gap: ~$60M; proportional across ALL reps (firm total: $672M → $458M)
- Rep 3 dropped from $251K → $0 despite having 22 accounts in both pulls
- Accounting identity check: Cost Basis + G/L ≈ $128M in both periods (stable) — confirmed Ending MV is NOT derivable from tax-specific fields; it represents total account portfolio value for context

**Hypothesis (confirmed by Andrew):** `Activity: Ending MV` with Rolling 3-Year computes: Beginning Balance (3 years ago) + all flows = Ending MV. Accounts onboarded to Orion less than 3 years ago have no beginning balance snapshot at the 3-year window start, so the roll begins from $0 and only accumulates within-window flows — understating or zeroing out those accounts' Ending MV.

**Fix:** Orion `additionalOptions` group [3] "Date Ranges" has `optionId: 9` = "Inception" (`startDateMethod: "Inception"`, `useInception: true`, `dataMustExistOnRangeStartDate: false`). Setting `contextChange.dateRangeId = 9` anchors each account's period start to its own inception date, so all accounts compute correctly regardless of age.

Verified: Since Inception bronze pull returned $202M for Inflection reps. `Period Start: 9/26/2019` (earliest account in DB); `Period End: 5/8/2026` (today). Rep 3 restored to $252K.

---

## Compiler Tools — Phase 3 (After Commit)

| Tool | Run | Result |
|------|-----|--------|
| Fresh bronze pull column check | `pulls/20260508_tax_unrealized.csv` after first fix | **PASS** — 33 columns, Ending MV at position 10 (0-indexed). |
| Ending MV sum check (Rolling 3-Year) | Post-commit-1 bronze | **FAIL (value wrong)** — Inflection $140M vs $200.8M baseline. Root cause 2 triggered investigation. |
| Ending MV sum check (Since Inception) | Post-commit-2 bronze | **PASS** — Inflection $202M. All-firm $676M vs $672M pre-regression (2-day market movement). |
| `INF_PREFER_S3=true python build_tax_dim.py --snapshot-date 2026-05-08 --upload` | Silver rebuild | **PASS** — 858 rows, `ending_mv=$202,062,830.31`, `total_cost_basis=$34,504,196`, `total_unrealized_gl=$13,055,620`. Uploaded to silver S3. |

---

## Commits

| SHA | Description |
|-----|-------------|
| `f9c9b3a1a` | `fix(ADVI_INFNNA.TAX-ENDING-MV-REPAIR)`: restore Ending MV column — activity blob + _column_value dispatcher + INFLECTION_REP_IDS [3,6,11,12] |
| `a88d6f357` | `fix(ADVI_INFNNA.TAX-ENDING-MV-REPAIR)`: set dateRangeId=9 (Since Inception) — corrects ~$60M understatement on Rolling 3-Year |

Both pushed to `CLOUD`.

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/manual_api/create_tax_dim_queries.py` | TAX_COLUMNS: 32→33 entries (added Ending MV as activity type); 3-tuple→4-tuple format; added `_activity_blob()`, `_column_value()` dispatcher; renamed `_column_blob`→`_simple_blob`; INFLECTION_REP_IDS [3,11,12]→[3,6,11,12]; dateRangeId override to 9 in `build_query_schema()` |

---

## Saved Query GUIDs (Final)

| Query | GUID | cbo |
|-------|------|-----|
| Tax Unrealized Dim | `0e102e7a-8ce8-4436-bd00-4d18763fc222` | 0 (unrealized) |
| Tax Realized Dim | `556c7add-b8e1-4306-aff4-cf35182a34c8` | 1 (realized) |

Prior GUIDs (deleted by --force across two iterations):
- Unrealized v1 (pre-investigation): `9b9e21a6-95c3-45d5-b610-364cc26a19a1`
- Realized v1 (pre-investigation): `3c9a9f81-e8b8-464a-9ff8-dbcc1b1aed07`
- Unrealized v2 (Rolling 3-Year, wrong): `39a60692-27d1-4827-995c-218e90f045b9`
- Realized v2 (Rolling 3-Year, wrong): `3c9a9f81-e8b8-464a-9ff8-dbcc1b1aed07`

---

## Flags for RAVC / Follow-On

| Flag | Detail |
|------|--------|
| INFLECTION_REP_IDS drift | `[3, 11, 12]` → `[3, 6, 11, 12]` fixed in `create_tax_dim_queries.py` per comp-constants gate. Same drift exists in `orion_tax_dim.py` (Generate call entityIds) — verify separately. |
| Silver 2026-05-07 ending_mv=0 | Bronze for 2026-05-07 was pulled with the broken saved query (32 cols, Ending MV absent). Silver parquet for that date has ending_mv=0. Optional backfill: `ORION_PULL_DATE=2026-05-07 python orion_tax_dim.py --upload-bronze` then rebuild silver. COO to decide. |
| activityOptionId=1 interaction with costBasisOptionId | Tax dim contextChange has both activityOptionId=1 and costBasisOptionId=0/1. Verified empirically that Ending MV resolves to total portfolio value (matching unified_account_dim's $199M) — not restricted to taxable positions. No further action needed. |

---

## Final State

| Item | Status |
|------|--------|
| Ending MV column | RESTORED — 33 columns in bronze |
| Ending MV value (Inflection) | CORRECT — $202M, matches $200.8M pre-regression baseline |
| Silver 2026-05-08 | REBUILT — ending_mv=$202M, uploaded to S3 |
| Silver 2026-05-07 | ending_mv=0 (known gap, optional backfill, flagged to COO) |
| Commits pushed | `f9c9b3a1a` + `a88d6f357` on CLOUD |
| TO status | complete (pending RAVC2 to COO) |
