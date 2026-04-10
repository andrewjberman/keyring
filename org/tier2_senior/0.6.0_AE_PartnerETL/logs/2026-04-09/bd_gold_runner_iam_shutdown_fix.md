# 0.6.0_AE Log: Gold Runner Watchdog Loop RCA + IAM Fix
**Date:** 2026-04-09
**Agent:** 0.6.0_AE_PartnerETL
**Tag:** bd-v2.21.7

## Context

DT identified that the production gold runner (i-01003b035d2988dfb) was staying up
for 2+ hours after gold runs today. Andrew asked AE to investigate and fix.

## Root Cause

**Bug:** `bd-exporter-ec2-role` lacked `s3:DeleteObject` on `opal-data-bd/*`.

**Effect chain:**
1. bd-price-runner writes `silver/prices/YYYY-MM-DD.parquet` (normal daily schedule, ~22:04 UTC)
2. S3 trigger fires -> bd-gold-trigger Lambda -> instance already running -> Lambda writes `gold/trigger-pending.json`
3. Gold runner completes main run, finds pending marker, calls `aws s3 rm gold/trigger-pending.json` -> **SILENT FAILURE** (no DeleteObject permission)
4. Runner runs pending incremental anyway (correct behavior)
5. Runner calls `shutdown -h now` (confirmed works as root via SSM test)
6. Watchdog fires 5 min later: gold process stopped, uptime > threshold, no keep-alive -- but check 4 `aws s3 cp gold/trigger-pending.json` SUCCEEDS (marker still in S3, never deleted)
7. Watchdog: "SKIP: pending trigger marker exists" -- refuses to shut down
8. Instance stays up indefinitely. Pending marker never cleaned up.
9. On next boot (triggered by Andrew killing and Lambda restarting), same cycle repeats.

## Verification

SSM diagnostic confirmed on running instance:
- Runner runs as uid=0 (root) -- shutdown has permissions
- `shutdown -h +1` + cancel worked -- binary is functional
- `aws s3 rm s3://opal-data-bd/gold/trigger-pending.json` failed from EC2 -- confirmed IAM bug
- Same delete succeeded immediately from local machine (Andrew's creds)
- Watchdog log showed continuous "SKIP: pending trigger marker exists" from 19:56-20:38 UTC
  corresponding exactly to the 57-minute overstay after run 1 completed at 19:45 UTC
- Watchdog IS installed, IS active, IS enabled on the instance (confirmed via SSM)

## Actions

1. Deleted stale `gold/trigger-pending.json` from S3 using local credentials (Andrew's IAM)
2. Stopped production instance (started for diagnostics)
3. Added `s3:DeleteObject` to `bd_exporter_s3` policy in `infra/aws/terraform/bd-pipeline/iam.tf`
4. Also: Terraform detected that `bd-gold-nightly-fallback` EventBridge rule was DISABLED
   (DT had attempted to disable via CLI earlier today before being stopped). Re-enabled it.
5. Applied both changes via terraform apply

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Start i-01003b035d2988dfb for diagnostics | running |
| 2 | SSM: stop gold-layer-runner service immediately | stopped |
| 3 | SSM: diagnostic -- watchdog state, shutdown test, pending marker | watchdog installed, shutdown works, s3 rm fails |
| 4 | SSM: watchdog log pull | confirmed pending marker loop pattern |
| 5 | Delete stale pending marker (local creds) | s3://opal-data-bd/gold/trigger-pending.json deleted |
| 6 | Stop instance | stopping |
| 7 | Edit iam.tf: add s3:DeleteObject to bd_exporter_s3 | done |
| 8 | terraform plan | 2 changes: IAM + EventBridge rule re-enable |
| 9 | terraform apply | 0 added, 2 changed, 0 destroyed |
| 10 | 0-diff plan | No changes |
| 11 | git commit + push | 60f38c7a |
| 12 | record-deploy + tag + push | bd-v2.21.7, 17675246 |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| BD | bd-v2.21.7 | 17675246 |

## Current State

- IAM: bd-exporter-ec2-role now has s3:DeleteObject on opal-data-bd/* 
- Pending marker: deleted from S3
- Production instance: stopped
- Nightly fallback rule: ENABLED (was accidentally disabled by failed DT CLI call)
- Watchdog: confirmed installed, active, enabled on the instance

## Next Steps

- Tonight's nightly fallback (23:00 UTC Mon-Fri) will trigger an incremental run
- Runner will now successfully delete pending markers after consuming them
- Watchdog should fire within 10 min of run completion and shut down the instance cleanly
- Monitor tomorrow morning: check S3 logs for tonight's run + instance stopped on its own
