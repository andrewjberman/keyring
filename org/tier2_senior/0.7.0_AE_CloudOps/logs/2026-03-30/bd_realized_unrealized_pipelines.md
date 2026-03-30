# BD Realized + Unrealized Capital Gains Pipelines -- 0.7.0_AE_CloudOps

**Date:** 2026-03-30
**Task Order:** bd-realized-unrealized-runners (from 1.0.0_SA_CTO)
**Tag:** bd-v2.20.0

---

## Objective

Build daily BD realized and unrealized capital gains report runners following
the existing bd-allocations pipeline pattern. Two new BD Data Mining templates
(Realized_Template, Unrealized_Template) need bronze ingestion (XLSX download
from BD portal to S3), silver conversion (XLSX to daily parquet partitions),
and the S3 folder structure to support both.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Study reference implementation (bd-allocation-trigger, SSM doc, merge script, eventbridge, lambdas.tf, iam.tf) | Pattern fully understood |
| 2 | Create Lambda triggers: bd-realized-trigger, bd-unrealized-trigger | Patterned after bd-allocation-trigger, reuse EC2 i-0800437d1dbb0b5cc |
| 3 | Create SSM documents: opal-bd-realized-download, opal-bd-unrealized-download | Shell scripts with BD download + silver merge |
| 4 | Create TypeScript downloaders: download-daily-realized.ts, download-daily-unrealized.ts | Patterned after download-daily-allocation.ts, templates Realized_Template and Unrealized_Template |
| 5 | Extend merge-daily-incremental.py with --realized and --unrealized flags | Realized dedup: (account_id, asset_name, trade_date, unit_cost). Unrealized dedup: (account_id, asset_name) |
| 6 | Add Lambda modules in lambdas.tf (realized_trigger, unrealized_trigger) | yang-lambda module, 128 MB, 600s timeout |
| 7 | Add EventBridge rules in eventbridge.tf | Unrealized 21:25 UTC, Realized 21:32 UTC Mon-Fri |
| 8 | Update IAM policy in iam.tf | Added opal-bd-realized-download and opal-bd-unrealized-download SSM doc ARNs |
| 9 | Register in lambda-source-map.json | Both new Lambdas registered |
| 10 | Commit 158a0026 | All code |
| 11 | Upload .ts downloaders to s3://opal-data-bd/scripts/src/stepwise/ | Both uploaded |
| 12 | Upload merge-daily-incremental.py to s3://opal-data-bd/scripts/ | Updated |
| 13 | Create SSM documents in AWS | opal-bd-realized-download v1, opal-bd-unrealized-download v1 |
| 14 | Build + upload Lambda zips via build-and-upload.sh | Both zips in s3://opal-313476888478-lambda-artifacts/bd-pipeline/ |
| 15 | Commit 077958e6 (source map artifacts) | Artifact SHAs recorded |
| 16 | terraform plan | 10 to add, 1 to change, 0 to destroy |
| 17 | terraform apply | Apply complete! Resources: 10 added, 1 changed, 0 destroyed |
| 18 | terraform plan (0-diff) | No changes. Infrastructure is up-to-date. |
| 19 | record-terraform-deploy.sh | 16 functions recorded, commit 37855578 |
| 20 | Tag bd-v2.20.0 + push --follow-tags | Pushed |

---

## Test Results

### Test 1: Unrealized Trigger (first attempt -- FAILED)

SSM command aab2ea6b -- download succeeded, merge failed:
```
ModuleNotFoundError: No module named 'lib'
```
Root cause: merge-daily-incremental.py imports `from lib.config import S3_BUCKET` but
the SSM doc only downloaded the merge script, not the lib/ directory.

Fix: Updated both SSM docs to sync s3://opal-data-bd/scripts/lib/ before running merge.
Uploaded lib/config.py and lib/__init__.py to S3. Updated SSM documents to v2.
Commit e4610e93.

### Test 2: Unrealized Trigger (retry -- SUCCESS)

SSM command 4ce82fcf:
- Downloaded UNREALIZED_DAILY_2026-03-27.xlsx (25 MB) from BD Unrealized_Template
- Deduped 315,197 rows by (account_id, asset_name)
- Wrote silver/unrealized/2026-03-27.parquet (93,270 rows, 16 cols)
- Shutdown +2 scheduled

### Test 3: Realized Trigger (SUCCESS)

SSM command 094fa5f3:
- Downloaded REALIZED_DAILY_2026-03-27.xlsx (426 KB) from BD Realized_Template
- Deduped 167 rows by (account_id, asset_name, trade_date, unit_cost)
- Wrote silver/realized/2026-03-27.parquet (8,286 rows, 15 cols)
- Shutdown +2 scheduled

---

## Timestamps Sheet -- Canonical Data Date Fix

Andrew identified that all BD Data Mining exports have a second sheet called
'Timestamps' with metadata including Start Date and End Date. The existing
approach parsed the date from the filename, which was set by the TypeScript
downloader using getPriorTradingDay(). This breaks on weekends and holidays.

Fix: Added read_timestamps_date() helper to merge-daily-incremental.py that
reads End Date from the Timestamps sheet as the canonical as-of date. Applied
consistently to ALL FOUR report types: transactions, allocations, realized,
unrealized. Filename parsing is fallback only.

End Date (not Start Date) is canonical because for multi-day ranges it gives
the most recent trading day covered.

Commits: 233f7282, 4a823bcf.

---

## Retroactive Date Audit

Audited all 89 existing XLSX files across all four report types:
- transactions: 41 files
- allocations: 46 files
- realized: 1 file
- unrealized: 1 file

Result: 88 OK, 1 mismatch.

Mismatch: TXN_DAILY_2026-02-21.xlsx -- filename said Feb 21 (Saturday),
Timestamps End Date says Feb 19 (Friday). Classic weekend edge case.

Fix: Renamed silver/transactions/2026-02-21.parquet to 2026-02-19.parquet.
Updated incremental_manifest.json.

---

## S3 Artifacts Created

| Path | Type | Size |
|------|------|------|
| s3://opal-data-bd/forwardfill_v2/realized/REALIZED_DAILY_2026-03-27.xlsx | Bronze | 426 KB |
| s3://opal-data-bd/forwardfill_v2/unrealized/UNREALIZED_DAILY_2026-03-27.xlsx | Bronze | 25 MB |
| s3://opal-data-bd/silver/realized/2026-03-27.parquet | Silver | 8,286 rows |
| s3://opal-data-bd/silver/unrealized/2026-03-27.parquet | Silver | 93,270 rows |
| s3://opal-data-bd/silver/incremental_realized_manifest.json | Manifest | -- |
| s3://opal-data-bd/silver/incremental_unrealized_manifest.json | Manifest | -- |
| s3://opal-data-bd/scripts/src/stepwise/download-daily-realized.ts | Script | -- |
| s3://opal-data-bd/scripts/src/stepwise/download-daily-unrealized.ts | Script | -- |
| s3://opal-data-bd/scripts/lib/config.py | Script | -- |
| s3://opal-data-bd/scripts/lib/__init__.py | Script | -- |

---

## AWS Resources Created

| Resource | Type |
|----------|------|
| bd-realized-trigger | Lambda (128 MB, 600s) |
| bd-unrealized-trigger | Lambda (128 MB, 600s) |
| /aws/lambda/bd-realized-trigger | CloudWatch Log Group |
| /aws/lambda/bd-unrealized-trigger | CloudWatch Log Group |
| bd-realized-pipeline-trigger | EventBridge Rule (cron 32 21 ? * MON-FRI *) |
| bd-unrealized-pipeline-trigger | EventBridge Rule (cron 25 21 ? * MON-FRI *) |
| opal-bd-realized-download | SSM Document (v2) |
| opal-bd-unrealized-download | SSM Document (v2) |
| bd-daily-trigger-policy | IAM Policy (updated -- 2 new SSM doc ARNs) |

---

## Daily Schedule (Mon-Fri, all on bd-allocations EC2 i-0800437d1dbb0b5cc)

| UTC | ET | Report | Notes |
|-----|-----|--------|-------|
| 21:25 | 5:25 PM | Unrealized (snapshot) | shutdown -c at start, shutdown -h +2 at end |
| 21:32 | 5:32 PM | Realized (incremental) | shutdown -c at start, shutdown -h +2 at end |
| 21:40 | 5:40 PM | Transactions (different EC2) | Unchanged |
| 21:48 | 5:48 PM | Allocations | Unchanged, shutdown -h +2 at end |

---

## Commits

| Commit | Description |
|--------|-------------|
| 158a0026 | Add daily BD realized + unrealized capital gains pipelines |
| 077958e6 | ci: upload artifacts for bd-realized-trigger and bd-unrealized-trigger |
| 37855578 | ci: record deploy bd-pipeline @ 077958e6 [skip ci] |
| e4610e93 | Fix SSM docs -- add lib/config.py download for merge script |
| 233f7282 | Use BD Timestamps sheet for canonical data date in realized/unrealized merge |
| 4a823bcf | Use Timestamps End Date consistently across all BD merge functions |

---

## Notifications Sent

| To | Subject |
|----|---------|
| 0.4.0_DS_ClientPlatform | BD realized + unrealized pipelines LIVE -- test results |
| 1.0.0_SA_CTO | BD realized + unrealized pipelines DEPLOYED AND TESTED -- bd-v2.20.0 |
| 2.0.0_SA_COO | BD realized + unrealized pipelines DEPLOYED -- bd-v2.20.0 |

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD
**Tag:** bd-v2.20.0

All code committed and pushed. All S3 artifacts uploaded. SSM documents created
and updated to v2. Lambda zips built and deployed. Terraform at 0-diff.
Retroactive date audit completed with 1 fix applied. Merge script updated
across all four report types for canonical Timestamps-based data dating.

---

## Next Steps

1. **Monitor first automated run** -- pipelines fire Mon 2026-03-31 at 5:25 PM ET.
   Check CloudWatch logs for bd-realized-trigger and bd-unrealized-trigger.
2. **Mark task order complete** -- bd-realized-unrealized-runners status -> complete.
3. **Deferred:** Create Terraform for opal-infrastructure-monitor (from prior session).
4. **Deferred:** SmartX supervisor deploy -- needs deploy-to-ec2.sh rewrite to S3+SSM.
