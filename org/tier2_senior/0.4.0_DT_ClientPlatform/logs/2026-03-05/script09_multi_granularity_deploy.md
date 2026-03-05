# Script 09 Multi-Granularity Deploy — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-05
**Start Time:** 19:06
**End Time:** 19:20

## Objective

Deploy updated `09_generate_partner_analytics.py` (commit `605ca776`) to EC2 and run
production upload to generate all three granularity JSON files for the portal toggle feature.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Upload script to S3 code bucket | `s3://opal-data-bd/code/gold/09_generate_partner_analytics.py` (71.2 KB) |
| 2 | Dry-run on EC2 (cmd `c41f7f8b`) | PARTIAL PASS — quarterly OK, monthly/annual crashed |
| 3 | Diagnose crash | `KeyError: 'geo'` at line 1670 — `current` period skipped |
| 4 | Root cause identified | `_ts` for monthly/annual `current` set to future month/year-end (no data) |
| 5 | Hotfix: 2 lines — `current_month_end` / `current_year_end` -> `ref_date` | Commit `63fd0a93` |
| 6 | Re-upload fixed script + dry-run (cmd `26186d27`) | ALL 3 PASS |
| 7 | Production upload (cmd `8d5311e6`) | SUCCESS — 3 files uploaded |
| 8 | Push CLOUD | `63fd0a93` already at remote (carried by subsequent commits) |

---

## Verification

**S3 Output Files:**
```
s3://opal-data-bd/gold/partner_analytics/header_metrics_quarterly.json   1,870,520 bytes
s3://opal-data-bd/gold/partner_analytics/header_metrics_monthly.json     1,650,040 bytes
s3://opal-data-bd/gold/partner_analytics/header_metrics_annual.json      1,902,619 bytes
```

**Validation Summary (from dry-run stdout):**

| Granularity | Period | GEO AUA | NNA Net | NMNC | NMEC |
|-------------|--------|---------|---------|------|------|
| All | current (2026-03-02) | $1,551,965,529 | varies | varies | varies |
| Quarterly | q1 Q4'25 | $1,366,785,335 | $96,649,406 | $62,716,311 | $36,472,312 |
| Monthly | m1 Feb'26 | $1,415,327,158 | $39,224,091 | $14,722,787 | $25,297,506 |
| Annual | y1 2025 | $1,366,785,335 | $285,716,772 | $230,963,338 | $89,439,546 |

**Note on monthly current NMNC=$0:** Correct. Period start is 2026-02-28 and reference date
is 2026-03-02 — only 2 days of window. No new relationships onboarded in a 2-day window.

---

## Hotfix Applied (commit `63fd0a93`)

**Bug:** `_get_periods_monthly()` set `current._ts = current_month_end` (2026-03-31 — future).
`_get_periods_annual()` set `current._ts = current_year_end` (2026-12-31 — future).
`build_views()` looks up `client_performance` at `_ts`. No data for future dates → period
skipped → line 1670 `KeyError: 'geo'` when main() accessed `payload['views']['nna']['current']`.

**Fix:** Both monthly and annual `current._ts = ref_date` (matches quarterly pattern).
2 lines changed. No change to period structure or NMNC logic.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Diagnose and fix script 09 rather than deploying quarterly-only | User confirmed all three granularities required |
| Fix in DT hotfix commit (not escalate to DS) | Root cause clear, fix is 2 mechanical lines mirroring existing quarterly pattern |
| Dry-run before production upload | Validates all 3 variants without writing to S3 |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/09_generate_partner_analytics.py` | _ts fix for monthly/annual current | Yes — `63fd0a93` |

---

## Current State

**Status:** COMPLETE

All 3 header_metrics JSON files live in `s3://opal-data-bd/gold/partner_analytics/`.
DE has already deployed matching portal changes (`7855dea3`). Feature is end-to-end deployed.

---

## Next Steps

1. **[0.4.0_DE_ClientPlatform] Verify portal toggle** — confirm monthly/annual/quarterly toggles
   render correct NMNC/NMEC values in Assets Overview
2. **No further DT action required** — script is production-ready; runs on next scheduled cycle
