# NNA Canonicalization Fix Deploy + EC2 Incremental Trigger — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-04
**Start Time:** ~17:00 ET
**End Time:** ~17:30 ET

---

## Objective

Deploy DS commit `4ba82ffc` (NNA canonicalization fixes) across two streams:
- Fix 1 (EC2 script 09): Remove Unknown state exclusion from GEO NNA view
- Fix 2 (Lambda): Align Q4 period start date in `_quarter_nna`

Then investigate why the B2 EC2 run (started at 15:47 UTC) never executed, and trigger
the incremental run manually.

---

## DS Commit Summary (4ba82ffc)

| # | File | Change |
|---|------|--------|
| 1a | `09_generate_partner_analytics.py` | Remove `state != 'Unknown'` from geo_end filter -- Unknown now named segment |
| 1b | same | Remove same exclusion from distribution filter |
| 2 | `lambda_function.py` (bd-portal-publisher) | `_quarter_nna`: start baseline changed from q_start (Oct 1) to q_start - 1 day (Sep 30) |

Expected outcome: GEO, ADV, and Overview NNA views within $1.00 of each other for Q4 '25.

---

## Deployment Sequence

### Fix 2 — Lambda (bd-portal-publisher)

| Step | Action | Result |
|------|--------|--------|
| 1 | build-and-upload.sh bd-pipeline bd-portal-publisher | SHA: `LvElsxI9sjFZqCA1Je5SZGLRZtI9TQgvgu/hlGTAs78=`, 16K |
| 2 | Commit source map | `d2c2c989` ci: upload bd-portal-publisher artifact [skip ci] |
| 3 | terraform plan | 1 resource changed (SHA only) |
| 4 | terraform apply | 0 added, 1 changed, 0 destroyed |
| 5 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 6 | record-terraform-deploy.sh | `f0994f64` ci: record deploy bd-pipeline @ d2c2c989 [skip ci] |
| 7 | Update deployment_map.xml | bd-portal-publisher deployed_tag -> bd-v2.15.2 |
| 8 | Commit + tag + push | `dab7c6fc` deployment_map, tag bd-v2.15.2 |

**Status: LIVE**

### Fix 1 — EC2 Script 09 (bd-gold-layer-runner)

| Step | Action | Result |
|------|--------|--------|
| 1 | safe-ec2-deploy.sh bd-gold-layer-runner | Bronze (4), silver (6), gold (14) scripts synced to s3://opal-data-bd/code/ |
| 2 | EC2_MANIFEST.json auto-commit | `5d2d83fa` Deploy EC2 bd-gold-layer-runner @ dab7c6fc |
| 3 | aws ec2 start-instances i-01003b035d2988dfb | State: running -> running (ALREADY RUNNING -- no-op) |
| 4 | Update deployment_map.xml + tag + push | `3204bf27` deployment_map, tag bd-v2.15.3 |

**Scripts deployed to S3.** Run did not execute (see Investigation below).

---

## EC2 Investigation

### Finding 1: Instance was already running at start-instances call

LaunchTime `2026-03-04T15:47:33Z` (B2 run trigger). When Fix 1 start-instances was called,
state was running -> running. No reboot occurred.

### Finding 2: gold-layer-runner systemd service is INACTIVE / DISABLED

The run mechanism is NOT user-data on boot. It is a systemd service
(`gold-layer-runner.service`) triggered externally by `bd-gold-trigger` Lambda
via SSM send-command (`sudo systemctl start gold-layer-runner`).

Because the service is disabled, starting the EC2 instance alone does NOT trigger a run.
The B2 start-instances call (and the Fix 1 call) both left the instance running but idle.

### Finding 3: No gold layer run occurred today

- `/var/log/gold-layer-runner.log` last entry: 2026-02-25
- S3 `logs/gold-layer/`: last file dated 2026-03-02
- `ps aux` on instance: only system Python processes (networkd-dispatcher, unattended-upgrade-shutdown)
- No gold scripts in memory

### Finding 4: Self-updating runner

`run-gold-layer.sh` is self-updating -- on each invocation it pulls the latest version
from `s3://opal-data-bd/code/runner/run-gold-layer.sh` before running. It then syncs
gold scripts from `s3://opal-data-bd/code/gold/` into `$SCRIPTS_DIR`. This means
scripts deployed via safe-ec2-deploy.sh are picked up automatically on the next run
without any additional deploy step.

### Trigger Architecture (confirmed)

```
silver completion
  -> bd-gold-trigger Lambda
  -> SSM send-command "sudo systemctl start gold-layer-runner"
  -> run-gold-layer.sh (self-updates from S3, then syncs gold scripts, then runs)
  -> run_gold_layer.sh incremental
  -> scripts 02, 05, 07, 08, 09, 10 (sequential)
  -> pipeline-complete.json sentinel
  -> instance shuts down
```

---

## Manual Incremental Trigger

Since no run occurred today, incremental run fired manually via SSM:

```bash
aws ssm send-command \
  --instance-ids i-01003b035d2988dfb \
  --document-name "AWS-RunShellScript" \
  --parameters 'commands=["sudo systemctl start gold-layer-runner"]' \
  --region us-east-1 \
  --comment "incremental -- NNA fix 4ba82ffc -- 0.4.0_DT"
```

**SSM Command ID:** `18f0f7e3-e25c-436e-bf9d-17ba420a4985`
**Dispatched:** 2026-03-04 ~17:25 ET

The run will:
1. Self-update runner from `s3://opal-data-bd/code/runner/`
2. Sync gold scripts from `s3://opal-data-bd/code/gold/` (picks up fixed `09_generate_partner_analytics.py`)
3. Run incremental: 02 -> 05 -> 07 -> 08 -> 09 -> 10
4. Write `gold/partner_analytics/header_metrics.json` and `gold/summary/header_metrics.json`
5. Write `pipeline-complete.json` sentinel (triggers bd-portal-publisher + bd-portal-advisor-publisher)
6. Shut down instance

**To verify completion:**
```bash
aws s3 ls s3://opal-data-bd/logs/gold-layer/ --recursive | sort | tail -3
```

**To run 3-view NNA verification after completion:**
```python
import boto3, json
s3 = boto3.client('s3', region_name='us-east-1')
pa = json.loads(s3.get_object(Bucket='opal-data-bd', Key='gold/partner_analytics/header_metrics.json')['Body'].read())
geo_nna = pa['views']['nna']['q1']['geo']['metrics']['nna']
adv_nna = pa['views']['nna']['q1']['adv']['metrics']['nna']
hm = json.loads(s3.get_object(Bucket='opal-data-bd', Key='gold/summary/header_metrics.json')['Body'].read())
overview_nna = hm['total']['q1']['nna']
print(f"GEO NNA Q4:      {geo_nna:>14,.2f}")
print(f"ADV NNA Q4:      {adv_nna:>14,.2f}")
print(f"Overview NNA Q4: {overview_nna:>14,.2f}")
assert abs(geo_nna - adv_nna) < 1.0,      "GEO vs ADV still diverged"
assert abs(adv_nna - overview_nna) < 1.0, "ADV vs Overview still diverged"
print("OK: all three views within $1 of each other")
```

---

## Manual Trigger Commands (Reference)

**Incremental run** (standard -- picks up current data):
```bash
aws ssm send-command \
  --instance-ids i-01003b035d2988dfb \
  --document-name "AWS-RunShellScript" \
  --parameters 'commands=["sudo systemctl start gold-layer-runner"]' \
  --region us-east-1
```

**Full rebuild** (clean reset of all gold parquets):
```bash
aws ssm send-command \
  --instance-ids i-01003b035d2988dfb \
  --document-name "AWS-RunShellScript" \
  --parameters 'commands=["sudo /home/ubuntu/gold-layer/run-gold-layer.sh full"]' \
  --region us-east-1
```

---

## Deployment Tags

| Pipeline | Tag | Commit | Notes |
|----------|-----|--------|-------|
| bd-pipeline (Lambda) | `bd-v2.15.2` | `dab7c6fc` | bd-portal-publisher _quarter_nna fix |
| bd-pipeline (EC2) | `bd-v2.15.3` | `5d2d83fa` | script 09 Unknown state fix (scripts in S3) |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Manual SSM trigger instead of waiting for Lambda | Service disabled, instance already running, no auto-start on boot. Manual trigger is the correct path for an unscheduled run. |
| Incremental (not full) | Only script 09 output changes. No upstream parquet corruption. Full rebuild not warranted. |
| Tag bd-v2.15.3 before run completes | Tag certifies code was deployed to S3 (deploy concern). Run output is runtime concern. |

---

## Current State

**Status:** COMPLETE (deploy) / IN PROGRESS (runtime -- incremental run triggered)
**Active branch:** CLOUD

Lambda fix is live. EC2 scripts synced. Incremental run dispatched via SSM.
Instance will complete run, write sentinel, trigger publishers, and shut down.

---

## Do NOT

- Run full mode unless clean reset is explicitly requested
- Re-trigger incremental before current run completes (check instance state first)
- Modify `architects`/`implementors` legacy keys (backward compat required)
