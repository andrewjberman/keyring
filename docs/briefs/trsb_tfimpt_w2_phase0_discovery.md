# TRSB_TFIMPT.W2 Phase 0 Discovery Report

**Date:** 2026-04-24
**Authors:** 0.7.0_AE_CloudOps (sections A, B, C, F-CloudOps) + 0.5.0_AE_OpalETL (sections D, E, F-SES)
**Status:** DRAFT — sections A–F complete, pending CTO+COO signoff before Phase 1
**TO:** `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_TFIMPT.W2.ae-lambda-code-reclamation-11-functions.md`

---

## Section A: Lambda Configuration Manifest (11 Functions)

**Authored by: 0.7.0_AE_CloudOps | Evidence run: 2026-04-24**

All configs pulled via `aws lambda get-function-configuration`. LastModified on all 11: 2026-04-06T18:54:33Z — bulk deployment date. No VPC on any function.

| # | Function | Runtime | Handler | Memory | Timeout | Role | Layers | CodeSize | TF Drift |
|---|---------|---------|---------|--------|---------|------|--------|----------|---------|
| 1 | trade-auth-handler | python3.11 | auth_handler.lambda_handler | 256 MB | 30s | trade-submission-lambda-role | None | 281 KB | None |
| 2 | trade-authorizer | python3.11 | authorizer.lambda_handler | 128 MB | 10s | trade-submission-lambda-role | None | 1.2 KB | None |
| 3 | trade-dashboard-api | python3.11 | dashboard_api.lambda_handler | 512 MB | 60s | trade-submission-lambda-role | None | 843 KB | None |
| 4 | trade-identifier-cache | python3.11 | identifier_cache.lambda_handler | 256 MB | 30s | trade-submission-lambda-role | None | 2.3 KB | None |
| 5 | trade-parquet-batch-export | python3.11 | parquet_exporter.lambda_handler | 1024 MB | 300s | trade-submission-lambda-role | **pandas-pyarrow-layer:1** | 4.1 KB | Layer present in both live AND lambdas.tf (lines 136-138). No drift. ✓ |
| 6 | trade-submission-handler | python3.11 | submission_handler.lambda_handler | 256 MB | 30s | trade-submission-lambda-role | None | 7.1 KB | None |
| 7 | trade-workflow-handler | python3.11 | workflow_handler.lambda_handler | 1024 MB | 120s | trade-submission-lambda-role | None | 47.9 MB | None |
| 8 | trade-recon-api | python3.11 | recon_api.lambda_handler | 256 MB | 60s | trade-recon-lambda-role | None | 3.6 KB | None |
| 9 | trade-recon-auth | python3.11 | auth_handler.lambda_handler | 256 MB | 30s | trade-recon-lambda-role | None | 281 KB | None |
| 10 | trade-recon-authorizer | python3.11 | authorizer.lambda_handler | 128 MB | 10s | trade-recon-lambda-role | None | 1.2 KB | None |
| 11 | trade-recon-processor | python3.11 | recon_processor.lambda_handler | 1024 MB | 300s | trade-recon-lambda-role | None | 29.7 MB | None |

**TF field-level findings:**
- Runtime, Handler, Memory, Timeout, Role: all match lambdas.tf for all 11. ✓
- Architectures: x86_64 (all 11). lambdas.tf omits arch block — defaults to x86_64. Consistent. ✓
- Layers: **trade-parquet-batch-export** has `pandas-pyarrow-layer:1` in both live AND lambdas.tf (lines 136-138 of lambdas.tf). No config drift. The `ignore_changes` mask prevented TF from tracking code changes, but the layers block was always present in TF state. Phase 1 can remove `ignore_changes` directly without any layers block addition.
- EnvVars: `trade-parquet-batch-export` shows `null` (no env vars set). Falls back to hardcoded config.py defaults (SUBMISSIONS_TABLE=`trade-submissions`, S3_BUCKET=`opal-data-trade-submissions`). Functional but unmanaged.
- Two IAM roles: `trade-submission-lambda-role` (7 functions) + `trade-recon-lambda-role` (4 functions). Consistent with lambdas.tf.

**Source spot-check (via zip download):**
- trade-authorizer (1.2 KB): Custom HMAC-based JWT auth. `JWT_SECRET` backed by env var (`os.environ.get('JWT_SECRET', 'trade-form-secret-change-in-prod')`). No hardcoded secrets if env var is set. Verify `JWT_SECRET` is set in Lambda console.
- trade-parquet-batch-export: 2 files (parquet_exporter.py + config.py). Clean. Two modes: real-time on COMPLETE + nightly batch.
- trade-submission-handler: 3 files (config.py + email_utils.py + submission_handler.py). SES sandbox TODO in source. `EMAIL_FROM` defaults to `trades@opalcapital.com` (differs from lambdas.tf env var `trades@opalinvest.dev` — verify which is live).
- trade-workflow-handler: 5 files + openpyxl-3.1.5 vendored (47.9 MB). Clean. Has excel_generator.py.
- trade-recon-auth: 281 KB (same pattern as trade-auth-handler). Likely shares auth_handler.py codebase.

---

## Section B: Dormancy Matrix

**Authored by: 0.7.0_AE_CloudOps | Evidence run: 2026-04-24**
**Windows:** 30d = 2026-03-25→2026-04-24 | 90d = 2026-01-24→2026-04-24

### B.1 — Lambda Invocations

| # | Function | Invocations 30d | Invocations 90d | Classification | Notes |
|---|---------|----------------|----------------|---------------|-------|
| 1 | trade-auth-handler | 0 | 0 | **COLD** | Authorizer triplet member |
| 2 | trade-authorizer | 0 | 0 | **COLD** | Authorizer triplet member |
| 3 | trade-dashboard-api | 0 | 506 | **DORMANT** | Last active ~60-90 days ago; dropped off |
| 4 | trade-identifier-cache | 0 | 0 | **COLD** | |
| 5 | trade-parquet-batch-export | **90** | 202 | **ACTIVE** | Only ACTIVE Lambda; direct invocation (not API GW) |
| 6 | trade-submission-handler | 0 | 0 | **COLD** | Confirmed by W1 Phase 1 probe (0 inv/30d) |
| 7 | trade-workflow-handler | 0 | 0 | **COLD** | |
| 8 | trade-recon-api | 0 | 0 | **COLD** | |
| 9 | trade-recon-auth | 0 | 0 | **COLD** | |
| 10 | trade-recon-authorizer | 0 | 0 | **COLD** | Authorizer triplet member |
| 11 | trade-recon-processor | 0 | 0 | **COLD** | |

**Summary: 1 ACTIVE / 1 DORMANT / 9 COLD**

**> 5+/11 non-active threshold triggered: 10/11 COLD or DORMANT. Per TO compiler mandate — flag to COO + CTO as candidate for consolidated deprecation assessment PRD amendment.**

### B.2 — API Gateway Method Triangulation

Two HTTP APIs (V2) found: `trade-submission-api` (w8jnzvs21g) + `trade-recon-api` (77005oklok).

| API | 30d Count | 90d Count | Classification |
|-----|----------|----------|---------------|
| trade-submission-api | 0 | 0 | **IDLE** |
| trade-recon-api | 0 | 0 | **IDLE** |

**Orphan-method analysis:** Both APIs have Count=0 in 30d and 90d. `trade-parquet-batch-export` has 90 Lambda invocations in 30d but API GW Count=0 — confirms it is invoked **directly** (not via HTTP API). Trigger source is not API GW; likely direct Lambda invoke (EventBridge, Step Functions, or nightly cron). No "API GW Count > 0 AND Lambda Invocations = 0" orphan-method condition found. Both APIs are simply idle end-to-end.

**API routes found (for documentation completeness):**
- trade-submission-api: POST /submit, POST /auth, GET /submissions/* (excel, list, proxy+), POST /workflow, GET /users — full trade submission lifecycle
- trade-recon-api: POST /reconcile, POST /upload/requests, POST /upload/confirms, GET /jobs/*, GET /health, POST /auth, POST /auth/verify, GET /auth/me — full recon workflow

---

## Section C: Per-Lambda Option Recommendation

**Authored by: 0.7.0_AE_CloudOps | Based on: Sections A + B**

| # | Function | Dormancy | Code Size | Recommendation | Rationale |
|---|---------|---------|---------|---------------|-----------|
| 1 | trade-auth-handler | COLD | 281 KB | **(b) EXCEPTION** | COLD authorizer. Bundled deps (281KB). Dormant subsystem. |
| 2 | trade-authorizer | COLD | 1.2 KB | **(b) EXCEPTION** | COLD authorizer triplet. Tiny handler but 0 invocations in 90d. If trade submission resumes, revisit. |
| 3 | trade-dashboard-api | DORMANT | 843 KB | **(a) RECLAIM** | Was active within 90d (506 inv). Dashboard APIs can resume unexpectedly. 843KB likely has recoverable source. |
| 4 | trade-identifier-cache | COLD | 2.3 KB | **(b) EXCEPTION** | COLD. Trivial size but no activity justification. |
| 5 | trade-parquet-batch-export | **ACTIVE** | 4.1 KB | **(a) RECLAIM** | Only ACTIVE Lambda (90 inv/30d). Must be in source control. Pandas-pyarrow layer TF drift also requires lambdas.tf fix. |
| 6 | trade-submission-handler | COLD | 7.1 KB | **(b) EXCEPTION** | COLD. SES-dependent flow; sandbox constraint is a blocker regardless. Revisit after SES prod-access granted. |
| 7 | trade-workflow-handler | COLD | 47.9 MB | **(b) EXCEPTION** | COLD. 47.9MB with openpyxl vendored makes S3-backed migration heavier. Not justified for dormant function. |
| 8 | trade-recon-api | COLD | 3.6 KB | **(b) EXCEPTION** | COLD. Recon subsystem entirely dormant. |
| 9 | trade-recon-auth | COLD | 281 KB | **(b) EXCEPTION** | COLD. Authorizer-pattern code. |
| 10 | trade-recon-authorizer | COLD | 1.2 KB | **(b) EXCEPTION** | COLD authorizer triplet. |
| 11 | trade-recon-processor | COLD | 29.7 MB | **(b) EXCEPTION** | COLD. 29.7MB — large vendored-dep bundle. No justification for reclaim while dormant. |

**Option count: 2 option-(a) / 9 option-(b)**

**> 5+/11 option-(b) threshold triggered (9/11). Per TO compiler mandate: flag to COO + CTO as candidate for consolidated deprecation assessment. This is a qualitatively different rollout — 9 of 11 Lambdas essentially represent a dormant subsystem, not just a few edge cases. COO + CTO should consider whether a "TRSB deprecation assessment" PRD amendment is warranted before Phase 1 fires.**

**Authorizer triplet disposition:**
All three authorizers (trade-auth-handler, trade-authorizer, trade-recon-authorizer) are COLD. Per TO: "IF all three authorizers are DORMANT/COLD — option-(b) formal exception for all three; DT 0.3 security review SKIPPED with rationale documented." DT 0.3 review is NOT required for this W2 scope.

**Phase 1 scope (if approved as-is):**
- Reclaim: trade-parquet-batch-export + trade-dashboard-api
- trade-parquet-batch-export Phase 1 note: `layers` block already present in lambdas.tf (lines 136-138, `pandas-pyarrow-layer:1`). Phase 1 removes `ignore_changes` and swaps `filename` → `s3_bucket`/`s3_key`/`source_code_hash` only. No layers block addition required.
- Exception doc: 9 functions with Known Issues rows in trade-pipeline README.md

---

## Section D: Smoke-Test Build-vs-Skip Recommendation

**Authored by: 0.5.0_AE_OpalETL | Evidence run: 2026-04-24**

### D.1 — Fixture Inventory

**Repo search:** Grepped `tests/`, `docs/`, `infra/` for `trades@opalinvest.dev`, `trade.*fixture`, `test.*trade`, `synthetic.*trade`, `opal-trade-submissions` refs.

| Location | Finding |
|---|---|
| `tests/` | No trade-specific test files. Directory contains: cloudfront perf test, gold_lib unit tests, comp_tools tests, exec_summary tests. No trade payload fixtures. |
| `infra/aws/lambda/trade-pipeline/` | **Directory does not exist.** All 11 trade Lambdas are EXTERNAL — no source in repo. Confirms W2 scope is valid. |
| `docs/architecture/TRSB_TFIMPT.md §8 Q4` | PRD explicitly flags "synthetic trade fixture" as an open question: *"For the W2 smoke test, is there a canonical synthetic trade we can submit without spamming trades@opalinvest.dev downstream recipients? If not, W2 closeout needs a pre-prod test route."* — confirms no fixture was resolved pre-rescope. |
| `logs/sessions/2026-01-06/aws_engineer/trade_submission_frontend_deployment.md` | Manual UI-based testing instructions from the original 2026-01-06 deployment: login → click "+ New Trade" → fill form → observe dashboard state transitions. No programmatic payload documented. |
| `infra/aws/terraform/trade-pipeline/lambdas.tf` | `EMAIL_FROM = "trades@opalinvest.dev"` at lines 167 and 198. Confirms sender identity. No test-route ENV var. |

**Conclusion:** No programmatic synthetic-trade fixture exists in repo. The only documented testing path is UI-manual (2026-01-06 instructions). No JSON payload, no `pytest` fixture, no seed script.

### D.2 — Build-vs-Skip Recommendation

**Resolved (based on Section B dormancy matrix):**

| Function | Status | Smoke action |
|---|---|---|
| trade-parquet-batch-export | **ACTIVE, option-(a) RECLAIM** | **BUILD direct-invoke smoke.** See below. |
| trade-dashboard-api | DORMANT, option-(a) RECLAIM | **SKIP** — dormant; acceptance = TF plan 0-diff + `comp-iam service` real result. |
| trade-submission-handler | COLD, option-(b) EXCEPTION | **MOOT** — not reclaimed in Phase 1. Original TO criterion #7 (submit → DDB → SES → workflow) does not apply. |
| All other 8 COLD | option-(b) EXCEPTION | **MOOT** — not reclaimed. No smoke needed. |

**Smoke fixture for trade-parquet-batch-export:**

`trade-parquet-batch-export` is invoked **directly** — API GW triangulation (Section B.2) confirms both trade APIs have 0 invocations in 30d + 90d while this Lambda has 90 invocations in 30d. Trigger is EventBridge cron or direct Lambda invoke, not HTTP.

The smoke fixture is therefore NOT a "trade submission JSON payload" — it is a direct `aws lambda invoke` call:

```bash
aws lambda invoke \
  --function-name trade-parquet-batch-export \
  --payload '{}' \
  /tmp/parquet_smoke_response.json
# Expect: StatusCode 200 + S3 write to opal-data-trade-submissions
cat /tmp/parquet_smoke_response.json
```

Phase 1 micro-deliverable: add `tests/trade_pipeline/smoke_parquet_export.sh` with the above invoke + S3 write verification. This is scope-appropriate — no trade-submission flow, no SES dependency, no API GW required.

**SES constraint note:** SES dependency is only relevant for option-(b) exception functions (trade-submission-handler, trade-workflow-handler). Since those are not reclaimed in Phase 1, SES sandbox restriction does NOT block Phase 1 smoke testing. Phase 1 smoke is purely parquet-export — no email triggered.

---

## Section E: SES Sandbox→Prod Readiness

**Authored by: 0.5.0_AE_OpalETL | Evidence run: 2026-04-24**

### E.1 — Account Status

| Field | Value |
|---|---|
| AWS Account | 313476888478 |
| Region | us-east-1 |
| Mode | **SANDBOX** |
| Max24HourSend | 200 emails/day |
| MaxSendRate | 1 email/second |
| SentLast24Hours | 1 |
| Configuration Sets | None |

**Sandbox impact on trade pipeline:** Sandbox restricts outbound email to SES-verified recipients only. In production, trade approval emails need to reach approvers and executors regardless of their SES verification status. Sandbox mode makes the trade workflow non-functional for any recipient not individually verified in SES.

### E.2 — Identity Status

| Identity | Type | Verification | DKIM Enabled | DKIM Status | Notes |
|---|---|---|---|---|---|
| `opalinvest.dev` | Domain | **Success** | **Yes** | **Success** | Primary trade-pipeline sender domain |
| `support@opalinvest.dev` | Email | Failed | Yes (inherits domain) | Success | Not a trade-pipeline sender; low priority |
| `yang@opalinvest.com` | Email | Success | No | Not Started | Trade workflow recipient |
| `manav@opalinvest.com` | Email | Success | No | Not Started | Trade workflow recipient |
| `wade@opalinvest.com` | Email | Success | No | Not Started | Trade workflow recipient |
| `menachem@opalinvest.com` | Email | Success | No | Not Started | Trade workflow recipient |
| `aj@opalinvest.com` | Email | Success | No | Not Started | Trade workflow recipient |
| `austin@opalinvest.com` | Email | Success | No | Not Started | Trade workflow recipient |
| `andrew@opalinvest.com` | Email | Success | No | Not Started | Trade workflow recipient |
| `lauren@opalinvest.com` | Email | Success | No | Not Started | Trade workflow recipient |
| `keith@opalinvest.com` | Email | Success | No | Not Started | Trade workflow recipient |
| `adam@opalinvest.com` | Email | **Failed** | No | Not Started | Sandbox blocks sending TO this address |
| `jim@opalinvest.com` | Email | **Failed** | No | Not Started | Sandbox blocks sending TO this address |
| `wayne@opalinvest.com` | Email | **Failed** | No | Not Started | Sandbox blocks sending TO this address |
| `jeanette@opalinvest.com` | Email | **Failed** | No | Not Started | Sandbox blocks sending TO this address |

### E.3 — Configured Sender

`trades@opalinvest.dev` is the `EMAIL_FROM` value hardcoded in `infra/aws/terraform/trade-pipeline/lambdas.tf` (lines 167 + 198). This address is covered by the domain-level identity `opalinvest.dev` (Verified, DKIM Success). No individual SES identity entry for `trades@opalinvest.dev` is needed.

### E.4 — SPF / MAIL FROM Status

Custom MAIL FROM is not configured (`BehaviorOnMXFailure: UseDefaultValue`). Email MAIL FROM header shows `amazonses.com` rather than `opalinvest.dev`. DKIM alignment is in place. Full DMARC alignment requires a custom MAIL FROM; this is a deliverability improvement, not a blocking production-access requirement.

### E.5 — Gap Summary and Required Actions

| Item | Status | Blocking? | Action |
|---|---|---|---|
| Domain `opalinvest.dev` verified | DONE | N/A | None |
| DKIM enabled + verified | DONE | N/A | None |
| SES configuration set (bounce/complaint feedback) | **MISSING** | **Yes** | Create configuration set before production access approval; attach to trade Lambda env vars. AWS expects bounce/complaint handling to be demonstrated. |
| Custom MAIL FROM for SPF alignment | MISSING | No (recommended) | Set `mail.opalinvest.dev` as custom MAIL FROM post-approval. |
| Production access request packet | **COMPLETE** | N/A | At `infra/aws/ses/trade-pipeline-prod-access-request.md` — Console-ready for Andrew |

### E.6 — Production Access Packet Location

Full packet for Andrew's Console submission: `infra/aws/ses/trade-pipeline-prod-access-request.md`

Contains: use-case description, daily volume estimate, compliance attestation (bounce/complaint/unsubscribe), DKIM/SPF status per identity, identity list, content readiness note, and raw AWS CLI evidence.

**Andrew action:** After W2 commits the packet, open AWS Console > SES > Account Dashboard > Request Production Access, copy-paste from the packet file. Configuration set creation (Section E.5 gap) should happen before submission or concurrently.

---

## Section F: Phase 1 Scope Proposal

**Authored by: 0.7.0_AE_CloudOps + 0.5.0_AE_OpalETL | Combined findings from A–E**

### F.1 — Reclamation Plan

**Option-(a) reclaim (2 functions):**
1. `trade-parquet-batch-export` — ACTIVE (90 inv/30d). Source: 2 files (parquet_exporter.py + config.py). Layer: pandas-pyarrow-layer:1 already in lambdas.tf. Phase 1 removes ignore_changes + swaps to S3-backed deploy via build-and-upload.sh.
2. `trade-dashboard-api` — DORMANT (506 inv/90d, 0/30d). Source: 843KB (larger, likely has multi-file structure). S3-backed deploy. No layer.

**Option-(b) formal exception (9 functions):**
trade-auth-handler, trade-authorizer, trade-identifier-cache, trade-submission-handler, trade-workflow-handler, trade-recon-api, trade-recon-auth, trade-recon-authorizer, trade-recon-processor. All receive Known Issues rows in README.md with dormancy classification + explicit ownership note.

### F.2 — Authorizer Triplet

All three (trade-auth-handler, trade-authorizer, trade-recon-authorizer) are COLD. DT 0.3 security review: **SKIPPED** — all dormant, option-(b) exception path, no code deploy. Rationale documented.

### F.3 — Smoke-Test Plan

One option-(a) Lambda is ACTIVE (trade-parquet-batch-export). Per Section D: **BUILD direct-invoke smoke fixture** — add `tests/trade_pipeline/smoke_parquet_export.sh` as Phase 1 micro-deliverable. This is a direct `aws lambda invoke` + S3 write verification, NOT a trade submission JSON payload (parquet-batch-export is triggered directly, not via API GW — confirmed by Section B.2 API GW triangulation).

SES sandbox constraint does **not** affect Phase 1 smoke — trade-submission-handler (SES-dependent) is option-(b) exception and will not be reclaimed. The parquet export smoke has no SES dependency.

### F.4 — SES Actions (Andrew + AE)

**Pre-Phase-1 (blocking for trade pipeline production use, non-blocking for W2 commit):**
- AE: Create SES configuration set with bounce + complaint tracking before submitting production access request
- Andrew: Submit production access request using `infra/aws/ses/trade-pipeline-prod-access-request.md`

**Post-approval (recommended):** Configure custom MAIL FROM `mail.opalinvest.dev` for full DMARC alignment.

**4 failed identities** (adam, jim, wayne, jeanette @opalinvest.com): resolve or remove. Inbox failures prevent delivery to these individuals even post-production-access.

### F.5 — PRD Amendment Flag (COO+CTO Decision Required)

**10/11 Lambdas are COLD or DORMANT.** 9/11 are option-(b). Per TO mandate, this triggers the "5+/11 flag" — the scale of exception exceeds what a normal W2 reclaim covers. COO + CTO should decide:

- **Option X:** Proceed as-is — reclaim 2, formally except 9. Phase 1 tag = `trade-pipeline-v1.4.0`. Low-effort close.
- **Option Y:** Amend PRD to add a "TRSB deprecation assessment" wave. Walk the 9 COLD functions and determine which are permanently decommissioned vs. latent-but-needed. Defer Phase 1 until after that assessment.

AE recommendation: **Option X** (proceed as-is). The 2 reclaim targets are clear; the 9 exceptions are adequately characterized as dormant-subsystem. A deprecation assessment can be a separate PRD if needed, but it should not block W2 close when the active function (parquet-batch-export) is clearly high value.

### F.6 — Tag

`trade-pipeline-v1.4.0` (after W1 `trade-pipeline-v1.3.0`). Verify: `git tag -l "trade-pipeline-v*" | sort -V | tail -5`.
