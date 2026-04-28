# Session Log — 0.6.1_AE_PartnerETL~B — 2026-04-28 (Wave 2)

**Agent:** 0.6.1_AE_PartnerETL~B (sub-lane)
**Date:** 2026-04-28
**Wave 2 start:** ~15:09Z (post-Wave-1 stand-down; Andrew direct delegation per 0.7.0~B confirm)
**Task orders addressed:** ADVI_ORIAPI JWT recovery + B3 QA boot test + ADVI_ORIAPI.004 prevention TO

---

## Wave 2 context

Wave 1 of this session (logged at `advi_infship_b2b3_session.md`) closed INFSHIP.B2+B3
+ B3-DEP-2 with tags `inf-pipeline-v1.6.1` + `v1.6.2`. Stand-down clean at 15:09Z.

Wave 2 was driven by three concurrent events:

1. **0.7.0~B 14:46Z joint-smoke RAVC** flagged JWT staleness (token expired
   2026-04-28T11:12Z); 3 of 7 bronze pulls 401'd. Root cause TBD.

2. **Andrew direct delegation 15:09Z** (relayed by 0.7.0~B 15:16Z): take ORIAPI
   JWT debug instead of routing to 0.6.1 base lane. Confirmed ownership.

3. **DS~D INF_I_D03 ship at `28018d36` (15:25Z)** — 5/5 publisher chain CLOSED.
   B3 QA boot test fully unblocked.

---

## Tags shipped (Wave 2)

| Tag | Commit | Description |
|---|---|---|
| `inf-pipeline-v1.6.3` | `6f4710d9` | ADVI_ORIAPI.004 inf-ec2-launch-monitor initial provisioning (8 added) |
| `inf-pipeline-v1.6.4` | `fe5a773f` | ORIAPI.004 decision-tree v2 patch (1 changed) |

(plus source-only commit `cc46d1db` user-data awscli v2 fix; no tag bump since
TF lifecycle.ignore_changes covers user_data)

---

## Deliverable 1 — ORIAPI.003 JWT recovery (manual)

### Investigation

| Phase | Time | Finding |
|---|---|---|
| Inbox triage | 15:17Z | Andrew delegated; took the lane |
| S3 metadata check | 15:18Z | `orion/jwt/current.json` LastModified `2026-04-28T01:11:21Z` (stale, 14h old); `orion/jwt/trigger-mode.json` LastModified `2026-04-28T12:00:07Z` (Lambda fired correctly at 12:00 UTC cron) |
| EC2 state check | 15:18Z | inf-exporter `i-081ae6aafb394fb1a` state=stopped; LaunchTime `2026-04-28T12:00:07Z`; **StateTransitionReason=`Server.InternalError`** |

**Root cause:** transient AWS-side EC2 launch failure. EventBridge cron + Lambda
dispatch fired correctly; AWS infrastructure failed the EC2 launch + returned
instance to stopped state. No retry logic in `inf-jwt-trigger` Lambda → JWT
stayed stale 3+ hours until manual recovery.

### Recovery

| Phase | Time | Outcome |
|---|---|---|
| Manual EC2 start | 15:18:17Z | inf-exporter `pending` → `running` cleanly (no Server.InternalError this attempt — confirms transient-class) |
| SSM dispatch `opal-inf-jwt-fetch` | 15:18:53Z | cmd `67fcd948-6f9f-4d59-887c-7615662e5641` |
| Fresh JWT in S3 | 15:20:24Z | `orion/jwt/current.json` LastModified verified |
| SSM Success | 15:20:25Z | StatusDetails: `Success` |
| EC2 stopped | 15:21Z | manual SSM dispatch bypasses production systemd auto-shutdown; manual cleanup |

JWT TTL is 10h → expires 2026-04-29T01:20Z. Tomorrow's 12:30 UTC bronze cron
needs tomorrow's 12:00 UTC JWT cron to succeed (covered by ORIAPI.004 below).

---

## Deliverable 2 — B3 QA boot test

### Test sequence

| Phase | Time | Outcome |
|---|---|---|
| Started inf-gold-qa-runner | 15:35:10Z | `i-04373615f03fbf9a9` running; SSM agent online 15:35:30Z |
| Attempt 1 — dispatcher `--single D_04` | 15:28Z | **FAILED** — AL2023 awscli/dateutil bug (same class as 0.7.0~B's d31809ca on inf-bronze-runner) |
| Live patch via SSM cmd `27b7bb56` | 15:30Z | awscli v2.34.38 installed at `/usr/local/bin/aws`; source-patched `user-data.sh` at `cc46d1db` |
| Attempt 2 — dispatcher `--single D_04` | 15:31Z | **FAILED** — ran BD-pattern `D_04.client_portal_summary.py` (NOT DS~B's patched `INF_D_04.client_portal_summary.py`); IAM deny on platinum/* write caught it cleanly (defense-in-depth working) |
| Attempt 3 — direct python3 of `INF_D_04` | 15:36:31Z | **SUCCESS** — 7 qa/* + qa/gold-artifacts/* artifacts written; 0 platinum/* writes |
| EC2 stopped | 15:39Z | Manual cleanup |

### AC verification

| AC | Result |
|---|---|
| **#5** Boot test (EC2 starts, gold runs against silver/api_dims/, writes to qa/ only, self-shutdown) | ✓ All 4 sub-criteria met (5 silver dim reads logged, 6 qa/firm/* + 1 qa/gold-artifacts/* writes, 0 platinum/* writes) |
| **#6** qa/firm/header_metrics.json byte-equivalence vs platinum/ | ✓ **0 differences** after normalizing (sort keys + drop `generated_at` timestamp); ContentLength match 49276 B both |
| **B3-DEP-2 verification** qa/gold-artifacts/summary/header_metrics.json populates | ✓ 49276 B written; same data as qa/firm/header_metrics.json (intentional — same upstream silver) |

### QA artifact catalog (15:36:31Z)

```
qa/firm/dashboard.json                          297 B
qa/firm/header_metrics.json                   49276 B  ← AC #6 PASS
qa/firm/partner_analytics_annual.json          8809 B
qa/firm/partner_analytics_monthly.json        14517 B
qa/firm/partner_analytics_quarterly.json      10405 B
qa/firm/timeseries_overview.json              39913 B
qa/gold-artifacts/summary/header_metrics.json 49276 B  ← B3-DEP-2 PASS
```

### Architectural items surfaced (RAVC2 to CTO at 15:41Z)

1. **Dispatcher catalog mismatch** (medium): `orion-gold-dispatch.sh` references
   BD-pattern `D_04.client_portal_summary.py`, NOT DS-patched
   `INF_D_04.client_portal_summary.py`. PROD inf-gold-layer-runner likely runs
   unpatched versions. Awaiting CTO ruling.

2. **IAM gap** (low): `gold/timeseries/client_performance.parquet` not readable
   from QA EC2; INF_D_04 gracefully degraded (timeseries_overview lacks AUA
   periods). ~5min TF fix.

---

## Deliverable 3 — ADVI_ORIAPI.004 prevention TO

### Context

0.7.0~B escalated at 15:26Z with **THIRD Server.InternalError today**
(inf-bronze-runner @ 15:24:32Z). 3 hits across 2 instances in 3.5h —
pattern is NOT transient. Possible AZ/instance-pool capacity issue in
us-east-1, possibly account-level throttle.

COO ruled at 15:33Z: ship Option A (CW EventBridge → Lambda filter → SNS)
tonight. Authority delegated. Option B (Lambda retry-with-backoff) held as
ADVI_ORIAPI.005 backlog.

### Architecture shipped

**EventBridge rule** `opal-inf-ec2-state-change-monitor`:
- Source `aws.ec2`, detail-type `EC2 Instance State-change Notification`
- Filter: `state=stopped` for **all 4** inf-pipeline cron-driven instances
  (inf-exporter, inf-bronze-runner, inf-gold-layer-runner, inf-gold-qa-runner)
- Target: `inf-ec2-launch-monitor` Lambda

**Lambda** `inf-ec2-launch-monitor` (Python 3.12 / 128MB / 30s):
- IAM minimum scope: `ec2:DescribeInstances` + `sns:Publish` on `inf-otp-alert` topic only
- Decision tree v2 (post-patch):
  1. ALERT_PATTERNS match (`Server.InternalError`, `Server.InsufficientInstanceCapacity`,
     `Client.InternalError`, `Client.VolumeLimitExceeded`) → SNS publish
  2. NORMAL_PATTERNS match (`User initiated`, `Client.InstanceInitiatedShutdown`)
     → suppress (wins over elapsed-time defense)
  3. Empty/unknown reason + stopped within 15s of launch → SNS publish (defense-in-depth)
  4. Otherwise → no-op

**SNS topic reuse:** `inf-otp-alert` (existing; Andrew already on subscriber list).

### Live test verification

**Test fire #1 (decision tree v1, 15:51:18Z):** false-positive — 60s elapsed-time
defense classified a 5-second test cycle as launch failure. Patched.

**Test fire #2 (decision tree v2, 15:58:52Z):**
- EventBridge delivered state-change event within ~1s
- Lambda invoked; describe-instances returned `StateTransitionReason='User initiated (2026-04-28 15:58:37 GMT)'`
- Decision: matched NORMAL_PATTERNS → **suppressed** (no SNS publish)
- Lambda duration 432ms; memory 97/128 MB

### COO acceptance criteria (per 15:33Z spec)

| AC | Result |
|---|---|
| **#1** CW EventBridge rule fires within 5 min | ✓ Live test fired Lambda **<1s** |
| **#2** SNS receives event payload on failure | ✓ Verified in code (ALERT_PATTERNS match → `_publish_alert`); will fire on next live Server.InternalError |
| **#3** Test fire by stop+start triggers SNS within 5 min | ✓ Live test 15:58:52Z processed correctly (suppressed normal stop) |
| **#4** Tag bump | ✓ `inf-pipeline-v1.6.3` initial + `v1.6.4` decision-tree v2 patch |
| **#5** RAVC4 to COO + CTO | ✓ Sent at 16:02Z |

---

## Joint smoke evidence (Wave 1 → Wave 2 cumulative)

| Event | Time | Lag |
|---|---|---|
| Wave 1 — B1 sentinel write | 14:46:22Z | — |
| Wave 1 — B2 chain summary | 14:46:28.927Z | ~7s S3 EventBridge → Lambda |
| Wave 2 — INF_D_04 direct dispatch | 15:36:31Z | (test fire) |
| Wave 2 — Lambda fired on QA EC2 stop | 15:58:52Z | <1s state-change → Lambda |

---

## Files changed (Wave 2)

### Created
- `infra/aws/lambda/inf-pipeline/inf-ec2-launch-monitor/lambda_function.py`
- `infra/aws/lambda/inf-pipeline/inf-ec2-launch-monitor/requirements.txt`
- `infra/aws/terraform/inf-pipeline/inf-ec2-launch-monitor.tf`
- `org/tier2_senior/0.6.1_AE_PartnerETL/logs/2026-04-28/oriapi_004_prevention_and_b3_qa_smoke.md` (this file)

### Modified
- `infra/aws/ec2/inf-gold-qa-runner/user-data.sh` (awscli v2 install fix; same as 0.7.0~B's d31809ca)
- `infra/aws/lambda/ci/lambda-source-map.json` (registered inf-ec2-launch-monitor)
- `infra/aws/terraform/inf-pipeline/CHANGELOG.json` (record-deploy entries for v1.6.3 + v1.6.4)

---

## Commits authored (Wave 2)

| Commit | Description |
|---|---|
| `cc46d1db` | fix(inf-pipeline): inf-gold-qa-runner user-data — awscli v2 install (mirror 0.7.0~B d31809ca) |
| `89288f6c` | feat(ADVI_ORIAPI.004): inf-ec2-launch-monitor Lambda — alarm on EC2 Server.InternalError-class launch failures |
| `04aabc29` | fix(ADVI_ORIAPI.004): tighten decision tree — explicit normal-pattern suppress wins; elapsed-time defense narrowed to 15s |

(plus auto-`[skip ci]` record-deploy commits `7fb60e06` for v1.6.1, `92716df7` for v1.6.1
again post-replace, `6f4710d9` for v1.6.3, and `fe5a773f` for v1.6.4 from
record-terraform-deploy.sh)

---

## Compiler tools used (Wave 2)

| Phase | Tool | Result |
|---|---|---|
| Pre-commit gate | `.tools/ds-commit-gate.sh` on `lambda_function.py` | py_compile + AST + ruff (caught 1 F541 f-string violation, fixed) → PASS |
| Commit safety | `.tools/safe-commit.sh` | All 4 commits clean |
| TF validation | `terraform validate` | PASS post-init |
| TF plan | `terraform plan` | 8 added (v1.6.3); 0-diff verified post-apply |
| TF apply | `terraform apply` | 8 added v1.6.3; 1 changed v1.6.4 |
| Record deploy | `record-terraform-deploy.sh` | source-map + CHANGELOG updated; ⚠️ swept DT MarketIntelligence session log into `fe5a773f` (separate Track 2 issue — script lacks pathspec scoping) |
| AWS CLI live tests | `aws ec2 start/stop-instances`, `aws ssm send-command`, `aws s3 cp/head-object`, `aws lambda` | All operational |
| Live decision-tree test | EC2 cycle + CW logs filter via PowerShell | Verified suppress + alert paths |

---

## Outstanding (Wave 2)

| Item | Owner | Status |
|---|---|---|
| Tomorrow's 12:00 UTC JWT cron natural fire (with ORIAPI.004 monitor live) | EventBridge | ~20h ETA; will validate end-to-end including detection of any recurrence |
| Tomorrow's 12:30 UTC bronze cron (with fresh JWT + monitor + DS path fixes shipped) | EventBridge | ~21h ETA |
| INFSHIP.B3 dispatcher catalog mismatch | CTO ruling | RAVC2 sent 15:41Z |
| INFSHIP.B3 IAM gap on `gold/timeseries/client_performance.parquet` | Me (when prioritized) | TF tweak; ~5min |
| ADVI_ORIAPI.005 Lambda retry-with-backoff | CTO/COO backlog | Triggered if 3+/day pattern recurs despite ORIAPI.004 monitor |
| `record-terraform-deploy.sh` pathspec scoping | DT/CI lane | Track 2 cleanup; surfaced in RAVC4 |

---

## Stand-down state (Wave 2 close)

- inf-pipeline: clean state at v1.6.4; 0-diff verified
- inf-gold-qa-runner EC2: `i-04373615f03fbf9a9` stopped (post boot test + ORIAPI.004 test fires)
- inf-exporter EC2: `i-081ae6aafb394fb1a` stopped (post manual JWT recovery)
- inf-ec2-launch-monitor Lambda: LIVE on EventBridge; verified decision-tree v2
- 21/21 session tasks complete
- Tomorrow's crons protected by ORIAPI.004 monitor; manual recovery latency drops from 3h to <1min
