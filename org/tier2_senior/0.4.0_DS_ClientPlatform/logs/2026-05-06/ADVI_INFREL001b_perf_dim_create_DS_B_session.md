# Session Log — ADVI_INFREL.001b DS~B: Create "Performance Dim" Orion Query

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-06
**GO received:** ~1943Z (CTO direct via Andrew ruling; relayed after context compaction)
**Session type:** Unblock execution — one-shot Orion ExcelReports catalog creator

---

## Summary

Created the "Performance Dim" saved query in the Orion ExcelReports catalog (database
ID 4698). This unblocks:
- AE 0.7 INFREL.010 Wave C2 performance backfill
- INFREL.001b daily cron forward bronze collection (tomorrow)

Also answered CTO catalog audit (active/stale query breakdown).

---

## Phase 0 — Reference Study

| Reference | Key Learning |
|-----------|--------------|
| `orion_tax_dim.py` | `_column_blob()`, `build_query_schema()`, `create_query()` patterns; `DATABASE_ID = 4698`; POST `ExcelReports/Verbose` endpoint |
| `pull_inflection_performance_dim.py` | Catalog GET `GET /api/v1/Reporting/Envision/ExcelReports`; verify by name lookup |
| `billing_dim_spike.verbose.json` | Schema structure, `userAccessRules` required for Orion save-permission gate |
| `convert_orion_api_to_silver.py` `build_performance()` | 24 exact header label strings |

---

## Phase 1 — Authoring

Authored `data/orion/manual_api/create_performance_dim_query.py`:

- Pattern: inline base schema (no file dependency — safe for EC2 /tmp execution)
- Idempotent: exits 0 if "Performance Dim" already exists in catalog
- 24 columns with labels EXACT-MATCH to build_performance() L137-162
- `userAccessRules`: Andrew userId=2592899 (canEdit=True, canRun=True, canDelete=True)
- Does NOT delete the query after creation (persistent catalog entry)
- Verifies creation by re-fetching catalog after POST

**PERF_COLUMNS (24):**
Account Id, Account Number, Account Name, Household Id, Representative Id, Representative Name,
Performance Value (percent), CalcMethod (string), TaxMethod (string), FeeMethod (string),
AnnualizedMethod (string), SharpeRatio (numeric), SortinoRatio (numeric), Drawdown (percent),
StandardDeviation (numeric), UpsideCaptureRatio (percent), DownsideCaptureRatio (percent),
BetaCoefficient (numeric), RSquared (percent), Mean (percent), Variance (numeric),
DateRange Name (string), DateRange StartDate (date), DateRange EndDate (date)

---

## Phase 2 — Pre-commit Gate

| Check | Result |
|-------|--------|
| ds-commit-gate.sh | Exit 0 — py_compile PASS, AST PASS, ruff py39 PASS (all 3 versions) |

---

## Phase 3 — Commit + Push + S3 Upload

| Step | Value |
|------|-------|
| Commit 1 (initial) | 3b48bb078 |
| Commit 2 (inline schema fix) | d6f1c847f |
| Commit 3 (userAccessRules fix) | d8177380e |
| Push | ebc1b2754..d8177380e CLOUD -> CLOUD |
| S3 key | s3://opal-data-inf/code/bronze-runner/manual_api/create_performance_dim_query.py |
| S3 ETag | 118b5e1f775616149fd11d48b16bf6c5 |
| S3 LastModified | 2026-05-06T20:03:36Z |

---

## Phase 4 — EC2 Dispatch + Verification

| SSM Run | Command ID | Result |
|---------|-----------|--------|
| v1 (initial) | e37ebca7-6240-43fc-97e5-5010f40c73a2 | FAIL exit=5: `/tmp/billing_dim_spike.verbose.json` not found |
| v2 (inline schema) | f22e671c-e515-408c-9e26-91365013c02e | FAIL exit=2: Orion 400 "must be allowed to edit" |
| v3 (userAccessRules) | 4b36378d-e440-44b0-bfbf-6dcd9662023b | SUCCESS exit=0 |

**Created query:**
- Query ID: `b22505ec-54e7-42e3-8a34-4e30dc22067c`
- Catalog verified: 20260506T20:03:55Z
- Catalog lookup by name: confirmed visible

---

## Catalog Audit RAVC to CTO

**INF_L1_tax_ queries:**
- `_193627Z` pair (unrealized + realized, same timestamp): ACTIVE — current/most recent Wave C1 run
- All others: STALE ORPHANS from failed runs — delete safe

**DS_B_unified_account_dim queries (141829Z, 142020Z May 6):** STALE — no pipeline uses this name. Delete safe.

**Generic named queries ("Billing Dim", "Tax", "Realize", "Geo"):** Do not delete. "Billing Dim" is active.

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/manual_api/create_performance_dim_query.py` | New — one-shot Performance Dim query creator |

---

## Current State

| Item | Status |
|------|--------|
| ADVI_INFREL.001b DS~B scope | COMPLETE — "Performance Dim" id=b22505ec created, RAVC to CTO + COO |
| AE 0.7 INFREL.010 Wave C2 | PENDING — awaiting AE 0.7 SSM dispatch (unblocked) |
| INFREL.001b daily cron | PENDING — arms tomorrow after first successful bronze pull |
| DS~B | IDLE — awaiting COO next TO dispatch |
