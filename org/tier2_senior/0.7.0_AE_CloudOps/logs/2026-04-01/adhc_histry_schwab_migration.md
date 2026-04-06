# ADHC_HISTRY.007 -- Schwab File Migration -- 0.7.0_AE_CloudOps

**Date:** 2026-04-01
**Task Order:** ADHC_HISTRY.007.ae-schwab-file-migration
**DS Prerequisite:** 2c8a4470 (fix(ADHC_HISTRY.006): converter reads bronze/rps/ first)

---

## Objective

Migrate 22 March 2026 Schwab RPS files from workaround staging
(opal-data-bd/uploads/schwab/) to canonical location (opal-data-schwab/bronze/rps/).
Upload and run updated converter. Clean staging. Launch 01_raw/ archive.

---

## Execution Steps

| Step | Action | Result |
|------|--------|--------|
| 1 | git pull origin CLOUD | Already up to date. DS .006 at 2c8a4470 confirmed. |
| 2 | Count staging files | 22 files (CRS20260302.RPS - CRS20260331.RPS) |
| 3 | aws s3 cp staging -> canonical --sse AES256 | 22 files copied (1.5 GiB) |
| 4 | Verify canonical count | 22 files at s3://opal-data-schwab/bronze/rps/ |
| 5 | Upload converter to S3 | s3://opal-data-schwab/silver/scripts/convert_schwab_rps_to_parquet.py |
| 6 | Create SSM doc opal-schwab-rps-convert | v1 created |
| 7 | Run converter on bd-gold-layer-runner (i-01003b035d2988dfb) | CommandId: db91d44e-ab2b-4fa2-bcf3-2de7694a35ab |
| 8 | Converter output | Already converted: 556, To convert: 0 -- all March dates present |
| 9 | Verify silver/RPS/ March coverage | 20260302-20260331 (22 weekday dates) confirmed |
| 10 | Delete staging area | aws s3 rm s3://opal-data-bd/uploads/schwab/ --recursive -- 22 files deleted |
| 11 | Verify staging empty | No output (confirmed empty) |
| 12 | Create SSM doc opal-schwab-archive-01raw | v1 created |
| 13 | Launch 01_raw/ archive (background) | CommandId: 2015d13b-efa4-4afc-bfa4-72a350a59b2f |

---

## File Migration Details

| Source | Destination | Count | SSE |
|--------|-------------|-------|-----|
| s3://opal-data-bd/uploads/schwab/ | s3://opal-data-schwab/bronze/rps/ | 22 files (1.5 GiB) | AES256 |

---

## Converter Verification

**SSM Command:** db91d44e-ab2b-4fa2-bcf3-2de7694a35ab  
**EC2:** i-01003b035d2988dfb (bd-gold-layer-runner) -- bd-allocations (i-0800437d1dbb0b5cc) was stopped  
**Result:** Available STANDARD RPS dates: 556 | Already converted: 556 | To convert: 0

silver/RPS/ March 2026 coverage (all 22 weekday dates present):
20260302, 20260303, 20260304, 20260305, 20260306, 20260309, 20260310,
20260311, 20260312, 20260313, 20260316, 20260317, 20260318, 20260319,
20260320, 20260323, 20260324, 20260325, 20260326, 20260327, 20260330, 20260331

Total silver/RPS/ partitions: 556 (2024-01-12 through 2026-03-31)

---

## Staging Area Deletion

```
aws s3 rm s3://opal-data-bd/uploads/schwab/ --recursive
# 22 files deleted -- verified empty
```

---

## Background Archive Job

**SSM Command:** 2015d13b-efa4-4afc-bfa4-72a350a59b2f  
**Doc:** opal-schwab-archive-01raw  
**Action:** aws s3 cp s3://opal-data-schwab/01_raw/ s3://opal-data-schwab/_archive/01_raw/ --recursive --sse AES256  
**Status:** Running (6214+ files, timeout 2h)  
**Note:** Do NOT delete 01_raw/ until archive command confirms src==dst count.

---

## SSM Documents Created

| Document | Purpose |
|----------|---------|
| opal-schwab-rps-convert | Run RPS converter from S3 on any SSM-registered EC2 with bd-exporter-ec2-role |
| opal-schwab-archive-01raw | Background archive of 01_raw/ to _archive/01_raw/ |

---

## Archive Job Verification (post-run)

**SSM status:** Success  
**Transfer:** 75.4 GiB completed  
**src count:** 6214 | **dst count:** 3988 | **diff:** 2226

**Root cause:** 2226 files (dates 2025-01-02 through 2025-11-11) are in GLACIER storage class.
`aws s3 cp --recursive` silently skips GLACIER objects. They were NOT copied to `_archive/01_raw/`.

**01_raw/ is NOT safe to delete.** GLACIER files exist only in `01_raw/`.

To archive GLACIER files: initiate a Glacier restore request for 01_raw/ (STANDARD tier, 1-5 days),
then re-run the archive copy after restore completes.

---

## Current State

**Status:** COMPLETE (primary migration done; archive BLOCKED on GLACIER restore)
**Active branch:** CLOUD

All 22 March RPS files migrated to canonical location with SSE AES256.
Converter ran clean -- 556 silver partitions cover 2024-01-12 through 2026-03-31.
Staging area deleted and confirmed empty.
Archive: 3988 of 6214 files copied (STANDARD tier only). 2226 GLACIER files (2025-01-02 to 2025-11-11) not archived.

---

## Next Steps

1. **[AE 0.7.0_AE_CloudOps -- deferred]** Initiate Glacier restore for 01_raw/ GLACIER objects:
   `aws s3 cp s3://opal-data-schwab/01_raw/ ... --recursive` won't work for GLACIER.
   Must use `aws s3api restore-object` or a batch restore job for 2226 files.
   After restore (1-5 days), re-run archive copy for those dates.
2. **[DS 0.4.0_DS_ClientPlatform]** silver/RPS/ now has full March coverage -- ADHC_HISTRY gold rebuild can proceed.

**Do NOT delete 01_raw/ -- 2226 GLACIER files (2025-01-02 to 2025-11-11) are NOT yet archived.**
