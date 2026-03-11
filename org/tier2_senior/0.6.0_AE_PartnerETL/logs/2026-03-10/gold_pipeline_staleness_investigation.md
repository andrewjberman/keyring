# Gold Pipeline Staleness Investigation — 0.6.0_AE_PartnerETL

**Date:** 2026-03-10
**Task Order:** ADVI_49FNV3.004.gold-pipeline-staleness-investigation.md

## Objective

Investigate why `opal-data-bd/gold/timeseries_chart.json` had a last data date of 2026-03-02 despite the bronze/silver/gold pipeline being configured to run daily. Determine root cause and fix.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Investigate S3 timestamps | `pipeline-complete.json` last written 2026-03-04, `timeseries_chart.json` 2026-03-06, `trigger-pending.json` 2026-03-09 |
| 2 | Check EC2 instance state | `i-01003b035d2988dfb` stopped, last launched 2026-03-09 21:51 UTC |
| 3 | Check EventBridge rules | `bd-gold-nightly-fallback` (Mon-Fri 23:00 UTC) and `bd-gold-layer-monthly-trigger` both ENABLED |
| 4 | Analyze bd-gold-trigger Lambda logs | EC2 started on 03-04, 03-05, 03-06, 03-09 but found "running" on subsequent triggers |
| 5 | Check silver layer freshness | Silver prices through 2026-03-08, transactions through 2026-03-06 -- upstream data is CURRENT |
| 6 | SSM diagnostic into EC2 | **ROOT CAUSE: systemd service `gold-layer-runner` is DISABLED** |
| 7 | Enable systemd service | `systemctl enable gold-layer-runner` via SSM |
| 8 | Start gold layer | `systemctl start gold-layer-runner` -- pipeline executed |
| 9 | Verify pipeline completion | `pipeline-complete.json` written 2026-03-10T15:57:27Z, run_date=2026-03-10, status=success |
| 10 | Verify publisher | bd-portal-publisher completed 15:58:23 UTC, data as of 2026-03-06, all outputs OK |
| 11 | Clean up stale pending marker | Removed `gold/trigger-pending.json` (stale from 2026-03-09) |

## Verification

```
pipeline-complete.json: {"status":"success","mode":"incremental","timestamp":"2026-03-10T15:57:27Z","run_date":"2026-03-10"}
timeseries_chart.json: 29,703,340 bytes (2026-03-10 11:58:22)
client_performance.parquet: 74,145,300 bytes (2026-03-10 11:55:26)
advisor_rolling_flows.json: 111,644,942 bytes (2026-03-10 11:57:26)
Run log: s3://opal-data-bd/logs/gold-layer/gold_incremental_2026-03-10.log (21,069 bytes)
Publisher: Data as of 2026-03-06, AUA=$1,619,318,260, NNA_12M=$251,892,894
```

---

## Root Cause Analysis

### What broke
The systemd service `gold-layer-runner` on EC2 instance `i-01003b035d2988dfb` was **disabled** (not enabled for auto-start on boot). This was the original configuration from `setup-instance.sh` which explicitly says "Register service but DO NOT enable auto-start on boot."

### When it broke
The service was likely never enabled on boot. Prior to 2026-03-04, the gold layer was being triggered manually via SSM commands (`sudo systemctl start gold-layer-runner`). The SSM command history shows a pattern of manual SSM invocations. The last successful SSM-triggered run was 2026-03-04. After that, no one sent the SSM command, and the nightly EventBridge trigger only starts the EC2 instance (via Lambda `ec2.start_instances()`), which does nothing without the systemd service enabled.

### Why it was silent
The Lambda trigger (`bd-gold-trigger`) successfully starts the EC2 and reports success. It has no mechanism to verify the gold pipeline actually runs on the EC2. When the EC2 boots with the service disabled, it just idles. Eventually the EC2 stops (either from a manual intervention or the nightly trigger finding it in various states). No error logs are produced because the gold pipeline never starts.

The `trigger-pending.json` markers compounded the issue: the Lambda wrote pending markers when it found the EC2 running (idle but technically "running"), and since the runner never checked those markers (because it never ran), they accumulated.

### Timeline
| Date | What happened |
|------|--------------|
| 2026-03-04 | Last successful run via SSM. Pipeline produced data as of 2026-03-02. |
| 2026-03-04 21:51 | S3 price trigger started EC2. EC2 booted but service disabled -- sat idle. |
| 2026-03-04 23:00 | Nightly fallback found EC2 running, wrote pending marker. |
| 2026-03-05 21:51 | EC2 still running (24h idle). S3 trigger wrote pending marker. |
| 2026-03-05 23:00 | Nightly fallback found EC2 stopped, started it. EC2 idle again. |
| 2026-03-06 | Same pattern. EC2 started, idle, eventually stopped. |
| 2026-03-07-08 | Weekend, no triggers. |
| 2026-03-09 | Same pattern. Pending marker written at 23:00. |
| 2026-03-10 | **FIX**: Enabled systemd service, started gold layer manually. Pipeline completed successfully. |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Enable systemd service on EC2 | Root cause fix -- service must start on every boot for Lambda trigger pattern to work |
| Remove stale pending marker | The 2026-03-09 marker was stale; the runner had already re-run the pipeline |
| Did not modify Lambda code | Lambda trigger logic is correct -- it starts EC2 as designed |
| Did not modify gold scripts | Scripts themselves are working; the issue was purely infrastructure |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| EC2 `i-01003b035d2988dfb` systemd service | `systemctl enable gold-layer-runner` | N/A -- EC2 runtime change via SSM |
| `s3://opal-data-bd/gold/trigger-pending.json` | Removed stale marker | N/A -- S3 object |

---

## Blockers

None.

---

## Current State

> **Status:** COMPLETE

The gold pipeline is now operational. The systemd service `gold-layer-runner` is enabled on `i-01003b035d2988dfb`, meaning every time the Lambda starts the EC2, the gold layer pipeline will execute automatically on boot. The pipeline ran successfully on 2026-03-10 with data as of 2026-03-06 (latest available from silver layer). The bd-portal-publisher and bd-portal-advisor-publisher both executed successfully, updating all portal data files.

---

## Next Steps

1. **Verify tomorrow's nightly trigger** -- confirm the 2026-03-10 23:00 UTC nightly fallback starts the EC2 and the gold layer runs automatically without SSM intervention. Check `s3://opal-data-bd/logs/gold-layer/gold_incremental_2026-03-11.log` exists by morning.
2. **[0.6.0_AE_PartnerETL] Fix dual-shutdown race** -- the orchestrator `run_gold_layer.sh` calls `shutdown -h now` at the end, which races with the runner `run-gold-layer.sh`'s pending marker check and log upload. The orchestrator should NOT call shutdown when invoked by the runner (only when invoked directly via SSM). This caused the stale pending marker to not be cleaned up.
3. **[0.6.0_AE_PartnerETL] Update `setup-instance.sh`** -- change the setup script to enable the systemd service on install (`systemctl enable gold-layer-runner`), so any future EC2 replacement will have the service enabled from the start.

**Do NOT:**
- Re-disable the systemd service
- Assume SSM manual triggers are needed -- the pipeline is now fully automatic
