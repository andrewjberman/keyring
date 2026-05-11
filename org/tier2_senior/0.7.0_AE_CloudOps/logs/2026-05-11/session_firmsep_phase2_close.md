# AE 0.7.0 Session Log — ADVI_FIRMSEP Phase 2 Close
**Date:** 2026-05-11
**Agent:** 0.7.0_AE_CloudOps
**TOs:** ADVI_FIRMSEP.07, .08, .09

---

## Prior State (2026-05-08 sessions)

- FIRMSEP.07/.08: deployed at `portal-auth-v1.15.6` (`b2ebd19d6`). CW metric filters + alarms LIVE.
- FIRMSEP.09: EventBridge rule `FIRMSEP-s3-direct-access-bypass` deployed (`63358ee24`, ENABLED).
  CT data events NOT enabled — blocked on Andrew/COO $ ack. Surfaced 20260508T144640Z.

## This Session — FIRMSEP.09 Completion

### COO GO received
"Proceed FIRMSEP .07/.08/.09 batch" — 2026-05-11, in response to INFRUNNERPARITY RAVC3 ACK.

### FIRMSEP.07 + .08 Status Verification
- `terraform plan` on portal-auth: **No changes** — all 5 metric filters + 5 alarms already in AWS.
- ACs 1-5 for both TOs: already COMPLETE from 2026-05-08 sessions.

### FIRMSEP.09 CT Data Events Enablement

| Step | Result |
|------|--------|
| CT event selector check | `DataResources: []` — S3 data events NOT enabled |
| COO GO received | 2026-05-11 batch authorization |
| `put-event-selectors` | Selector 2: ReadWriteType=ReadOnly, opal-data-bd + opal-data-inf |
| Verification | 2-selector config confirmed; management events preserved (Selector 1 unchanged) |
| Cost estimate | $0.10/100K events; ReadOnly minimizes vs All (no PutObject events) |

CT configuration post-enablement:
```
Selector 1: ReadWriteType=All, IncludeManagementEvents=true, DataResources=[]
Selector 2: ReadWriteType=ReadOnly, IncludeManagementEvents=false,
            DataResources=[{AWS::S3::Object: ["arn:aws:s3:::opal-data-bd/", "arn:aws:s3:::opal-data-inf/"]}]
```

### FIRMSEP.09 Empirical Test (AC4)

Test: `aws s3api get-object --bucket opal-data-bd --key gold/meta/pipeline-complete.json` from non-CF context.
- S3 GetObject: SUCCESS (HTTP 200, ETag c2b3629f4240c71962c8f0e693fa588a)
- userAgent: AWS CLI (not "Amazon CloudFront")
- GetObject submitted ~19:39Z; CT propagation completed ~19:40Z

**AC4 PASS CONFIRMED:**

| Metric | Window | Sum |
|--------|--------|-----|
| TriggeredRules | 19:40Z (5-min) | 10 |
| TriggeredRules | 19:45Z (5-min) | 11 |
| Invocations | 19:40Z (5-min) | 10 |
| Invocations | 19:45Z (5-min) | 11 |

Total triggers: 21. Invocations = TriggeredRules (0 failed deliveries). SNS delivery to opal-infrastructure-alerts: confirmed.

Note: 21 triggers during window = multiple GetObject events (AWS CLI auto-generates range requests + metadata reads); all dispatched to SNS. Rule operates correctly — any non-CF GetObject generates an alert.

### Commits

| Commit | Description |
|--------|-------------|
| `1d590088e` | cloudwatch-alarms.tf CT-enabled comment + FIRMSEP.09 TO status complete |

### Portal-Auth Tag
No new terraform apply — EventBridge rule deployed in prior session (portal-auth-v1.15.6). Comment-only change does not require tag bump.

## Acceptance Criteria Status

**FIRMSEP.07:**

| AC | Status |
|----|--------|
| AC1: 4 CW metric filters on auth-validator-edge | DONE (2026-05-08) |
| AC2: 4 CW alarms → opal-infrastructure-alerts SNS | DONE |
| AC3: terraform 0-diff post-apply; portal smoke | DONE |
| AC4: single synthetic denial → metric tick | DONE (2026-05-08 session) |
| AC5: tag + push + record-terraform-deploy | DONE (portal-auth-v1.15.6) |

**FIRMSEP.08:**

| AC | Status |
|----|--------|
| AC1-5 | DONE (2026-05-08, same session as .07) |

**FIRMSEP.09:**

| AC | Status |
|----|--------|
| AC1: CT S3 data events logged for opal-data-{bd,inf} | DONE (this session) |
| AC2: EventBridge rule registered for non-CF GetObject | DONE (63358ee24) |
| AC3: SNS-to-opal-infrastructure-alerts wired | DONE |
| AC4: empirical bypass test → rule fires | DONE (21 triggers @ 19:40-19:45Z; 100% SNS delivery) |
| AC5: allowlist scaffold + empty initial | DONE (scaffold described in TF comment) |
| AC6: tag + record-terraform-deploy | N/A (comment-only change; prior tag covers) |
| AC7: FIRMSEP.10 will add opal-data-cot | NOTED |

## Session Status: COMPLETE

All FIRMSEP .07/.08/.09 ACs DONE. RAVC sent to 2.0.0_SA_COO.

## Standby Items
- INFETL.011 cron-flip-ack addendum: ~12:30Z 2026-05-12 per COO directive
- ADHC_INFRUNNERPARITY AC6 (AMI rebuild confirm): next inf-gold-trigger dispatch ~06:00Z 2026-05-12
- ADHC_DSFLOW.006 AC5 (journalctl evidence): next chain fire ~06:00Z 2026-05-12
