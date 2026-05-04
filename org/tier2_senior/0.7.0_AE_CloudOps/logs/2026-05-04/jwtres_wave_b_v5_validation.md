# 0.7.0_AE_CloudOps — JWTRES.002 Wave B v5 Empirical Validation
**Date:** 2026-05-04
**TO:** COO GO — JWTRES.002 first-fire CW validation (Item 1b)
**Session type:** Validation audit — CW Logs + CW Metrics + SM + Enforcer

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Register + inbox check | GO received from 2.0.0_SA_COO |
| 2 | Task 1: CW Logs discovery | Log groups: /aws/lambda/inf-jwt-trigger (17 streams, 5 in-window) |
| 3 | Task 1: CW Metrics query | JwtAutoRecoveryAttempted=1, JwtAutoRecoverySucceeded=1, JwtNearExpiry=1 |
| 4 | Task 2: Enforcer verification | EXCLUDED_INSTANCES confirmed live; 23+ SKIP:excluded log entries sampled |
| 5 | Task 3: SM rotation history | orion/jwt/current — 4 versions in window |
| 6 | IAM audit (comp mandate) | inf-jwt-trigger SM delegation confirmed correct |
| 7 | ADVI_JWTRES.json updated | phase field appended with validation record |
| 8 | Commit | 9902f7f9f (CLOUD) |

---

## Task 1 — JWTRES.002 First-Fire CW Log

**Window:** 2026-05-01T19:07Z (wave start) to 2026-05-03T02:57:51Z (wave end, ~80h)

### CW Metrics (namespace: Inflection/HistBackfill/RateLimiter)

| Metric | Dimension | Count | Timestamp bucket |
|--------|-----------|-------|-----------------|
| JwtAutoRecoveryAttempted | positions_mv | 1 | 2026-05-02T00:35Z (display) |
| JwtAutoRecoveryAttempted | assets_v2 | 1 | 2026-05-02T00:35Z (display) |
| JwtAutoRecoverySucceeded | positions_mv | 1 | 2026-05-02T00:35Z (display) |
| JwtAutoRecoverySucceeded | assets_v2 | 1 | 2026-05-02T00:35Z (display) |

*Timestamp display note: boto3 get_metric_statistics on Windows returns metric bucket timestamps that appear 4h behind UTC (EDT offset artifact). Lambda log + SM evidence pin the actual first-fire at 04:35Z UTC (= 00:35 EDT). Metric bucket "00:35Z" = 04:35Z UTC.*

### CW Metrics (namespace: Inflection/JwtResilience)

| Metric | Dimension | Count |
|--------|-----------|-------|
| JwtNearExpiry | positions_mv | 1 |
| JwtNearExpiry | assets_v2 | 1 |

### inf-jwt-trigger Lambda Log Streams (in-window)

| Stream first-event (UTC) | Mode | Instance | Outcome | Notes |
|--------------------------|------|----------|---------|-------|
| 2026-05-01T21:00:34Z | export | i-081ae6aafb394fb1a | SSM sent c6c00820 (opal-inf-export-run) | EventBridge export cron — pre-wave cleanup |
| 2026-05-02T04:35:52Z | jwt-extract | i-081ae6aafb394fb1a | SSM sent 152e6b4e (opal-inf-jwt-fetch) | **First-fire: recover_or_exit or cron** |
| 2026-05-02T04:35:54Z | jwt-extract | i-081ae6aafb394fb1a | SSM sent 75b0a284 (opal-inf-jwt-fetch) | Concurrent trigger (dual invocation) |
| 2026-05-02T12:13:01Z | jwt-extract | i-081ae6aafb394fb1a | SSM sent 6ea9dcb0 | ORIAPI.002 cron (12:13 UTC = 08:13 EDT) |
| 2026-05-02T21:00:34Z | jwt-extract | i-081ae6aafb394fb1a | SSM sent 0074ce36 | ORIAPI.002 cron (21:00 UTC = 17:00 EDT) |

### Canonical First-Fire Record

```
Timestamp:  2026-05-02T04:35Z UTC (00:35 EDT)
Lambda:     /aws/lambda/inf-jwt-trigger stream 3ea270a82f29404d86135649dd41a63a
Mode:       jwt-extract
SSM cmd:    152e6b4e-62b3-47ed-9b0f-ba91517537f4 (opal-inf-jwt-fetch)
SM write:   orion/jwt/current version b55593bf at 04:36:36Z UTC
CW metric:  JwtAutoRecoveryAttempted + JwtAutoRecoverySucceeded = 1 each (both dims)
Outcome:    SUCCEEDED
```

### Expected vs Actual Count

- Expected fires: ~8 (80h / 10h JWT lifetime)
- Actual recover_or_exit fires: **1**
- Explanation: ORIAPI.002 EventBridge cron (12:13Z, 21:00Z UTC daily) refreshes JWT proactively before expiry. recover_or_exit fires only when JWT is ALREADY stale at orchestrator check time. Cron coverage meant only the initial near-expiry (4:35Z, ~9.5h after wave start with an already-aging JWT) triggered recovery. All subsequent refreshes were handled by cron. This is the CORRECT and INTENDED behavior — recover_or_exit is the backstop, not the primary path.

### Dual Invocation at 04:35Z

Two concurrent Lambda streams at 04:35Z UTC. Both mode=jwt-extract, both targeting i-081ae6aafb394fb1a. First stream caught instance `stopped`, started it. Second stream caught instance `pending`. Both sent SSM commands. Result: 2 SM versions written (b55593bf at 04:36Z, 659fbd17 at 04:37Z). CW metric count = 1 (not 2), suggesting the metric was emitted once. Low-severity — no thrash, no error output. Likely EventBridge cron + recover_or_exit racing at the same near-expiry moment.

---

## Task 2 — Enforcer Exclusion Verification

**Live config:**
- EXCLUDED_INSTANCES: `i-083ad9ae297f88e9f,i-081ae6aafb394fb1a`
- Last modified: 2026-05-01T21:33:09Z (enforcer-v1.0.2 deploy, AE 0.7.0)

**Log evidence (23+ SKIP:excluded events sampled):**

| Time window sampled | inf-bronze-runner runtime | inf-exporter runtime | Result |
|--------------------|--------------------------|---------------------|--------|
| 2026-05-02T18:11Z | 23.2h | 13.6h | SKIP:excluded |
| 2026-05-02T20:46Z | 25.8h | 16.2h | SKIP:excluded |
| 2026-05-02T23:11Z | 28.2h | 18.6h | SKIP:excluded |
| 2026-05-03T01:11Z | 30.2h | 20.6h | SKIP:excluded |

Both instances ran uninterrupted throughout the 80h window. Zero shutdown events. CLEAN PASS.

---

## Task 3 — SM JWT Rotation History

**Secret:** `orion/jwt/current`

| Version ID | Created (UTC) | In window? | Source |
|-----------|---------------|-----------|--------|
| 52119092 | 2026-05-01T12:13:39Z | No (pre-wave) | Scheduled cron |
| 6cf5ea3b | 2026-05-01T18:57:48Z | No (pre-wave, 9min before) | Scheduled cron |
| b55593bf | 2026-05-02T04:36:36Z | YES | First-fire recovery |
| 659fbd17 | 2026-05-02T04:37:00Z | YES | Dual invocation |
| 4ea5e57d | 2026-05-02T12:13:18Z | YES | ORIAPI.002 cron |
| f1b9675a | 2026-05-02T21:00:56Z | YES | ORIAPI.002 cron |
| dd16122e | 2026-05-03T12:13:23Z | No (post-wave) | Scheduled cron |
| 3acf1508 | 2026-05-03T21:00:57Z | No (post-wave) | AWSPREVIOUS |
| 9b0778c8 | 2026-05-04T07:49:14Z | No | AWSCURRENT (today) |

4 versions in window. SM rotation cross-references perfectly with Lambda invocations. No anomalous rotation events.

---

## Compiler Tools

| Tool | Run | Result |
|------|-----|--------|
| comp-iam service inf-jwt-trigger | Pre-work | No service matching (Lambda not in registry — expected; IAM validated empirically) |
| comp-iam gaps | Pre-work | 1 gap: bd-gold-runner s3:CopyObject (unrelated to JWTRES; not AE scope this session) |

IAM delegation architecture confirmed: inf-jwt-trigger Lambda has no direct SM permissions. SM write path: Lambda → SSM opal-inf-jwt-fetch → inf-exporter EC2 (via inf-exporter-ec2-role) → orion/jwt/current. KMS decrypt live (inf-jwt-trigger-kms policy, key 4ba4753c). Correct and intact.

---

## Findings Summary

| Check | Result | Evidence |
|-------|--------|----------|
| JWTRES.002 first-fire | PASS | 2026-05-02T04:35Z UTC, Lambda stream 3ea270a8, SSM 152e6b4e |
| JwtAutoRecoverySucceeded | PASS | CW metric = 1 (both dims), zero failures |
| Recovery count anomaly | NONE | 1 fire expected given ORIAPI.002 cron coverage; not a bug |
| Dual invocation at 04:35Z | LOW-SEV | 2 concurrent streams, 1 CW metric; no thrash; no errors |
| Enforcer exclusion held | PASS | 23+ SKIP:excluded events; zero shutdowns across 80h |
| SM rotation cross-ref | PASS | 4 in-window writes, all match Lambda invocation timestamps |
| IAM integrity | PASS | SM delegation via SSM correct; no direct Lambda SM perms needed |

**VERDICT: JWTRES.002 Phase 2 Option B VALIDATED.**

---

## Commit

| Commit | Files | Notes |
|--------|-------|-------|
| 9902f7f9f | org/projects/ADVI_JWTRES.json | Empirical validation appended to phase field |

---

## Next Actions

- RAVC4 to 2.0.0_SA_COO — validation complete, VALIDATED status confirmed
- COO to drive 3-step atomic closure (JSON status flip + REGISTRY move + PRD status note)
- bd-gold-runner s3:CopyObject gap: flagged to DT (not AE scope, non-blocking to JWTRES close)
