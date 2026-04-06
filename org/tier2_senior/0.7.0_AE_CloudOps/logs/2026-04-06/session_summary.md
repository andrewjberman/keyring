# Session Summary — 2026-04-06

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-06

---

## 1. Gold Runner Enforcer Coverage + Watchdog Hardening (CTO Escalation)

**Trigger:** CTO urgent message — bd-gold-layer-runner (c6i.16xlarge, i-01003b035d2988dfb) idle for 4 days, ~$228 wasted compute.

**Root Cause:** Instance had `AutoShutdown=disabled` tag, causing enforcer Lambda to skip it (lambda_function.py:116). Watchdog timer likely failed because `aws s3 cp` check (no timeout) hung indefinitely, blocking the systemd oneshot service.

**Fixes:**
- Removed `AutoShutdown=disabled` tag from i-01003b035d2988dfb (AWS API)
- Hardened `watchdog-shutdown.sh`: added `timeout 10` on S3 check, narrowed process grep from `python3` to `run_gold_layer|gold_rebuild|build_gold`
- Uploaded hardened watchdog to `s3://opal-data-bd/code/runner/watchdog-shutdown.sh`

**Commit:** `10fb7dbc` | **Tag:** `bd-v2.20.1`

---

## 2. BD Data Freshness Analysis + EventBridge Schedule Optimization

**Trigger:** Andrew requested investigation into Black Diamond file refresh timing.

**Method:** Downloaded 24 XLSX files across all 4 BD data types (transactions, allocations, realized, unrealized) spanning 3+ weeks. Read Sheet 2 ("Timestamps") metadata to extract BD's internal Refresh and Created timestamps.

**Findings:** BD refreshes all data at ~4:33 PM ET. Files become available in order: Unrealized ~5:27, Realized ~5:34, Transactions ~5:43, Allocations ~5:50 PM ET. Our old schedule was firing BEFORE BD files were ready.

**Schedule Changes (eventbridge.tf):**

| Type | Old (UTC) | New (UTC) | New ET | Buffer After BD |
|------|-----------|-----------|--------|-----------------|
| Unrealized | 21:25 | 21:38 | 5:38 PM | +11 min |
| Realized | 21:32 | 21:45 | 5:45 PM | +11 min |
| Transactions | 21:40 | 21:53 | 5:53 PM | +10 min |
| Allocations | 21:48 | 22:00 | 6:00 PM | +10 min |

**Commit:** `10fb7dbc` | **Tag:** `bd-v2.20.1` | **0-diff verified**

---

## 3. RPS Ingestion Script

**Trigger:** Andrew requested canonical mechanism for Schwab RPS file upload + processing.

**Analysis:** Gold layer only uses LATEST silver/RPS partition. Batch uploads (e.g., 5 days at once) produce identical advisor intelligence output as daily uploads. No time series impact.

**Deliverable:** `data/black_diamond/scripts/bronze/rps_ingestion.py` — single command to find local CRS*.RPS files, upload to S3 bronze with SSE AES256, and run bronze->silver conversion. Idempotent. Tested.

**Commit:** `9f3fc4fb`

---

## 4. Infrastructure Technical Debt Audit (DEBT_1STRUN.001)

**Method:** Used `org/modules/perceive/filesystem_scanner` on `infra/aws/` (6,610 files, 1.87M lines). Cross-referenced AWS live state (Lambda, S3, DynamoDB, EC2, IAM) against repo source maps using `coverage_auditor` pattern.

**Headline Findings:**

| Resource | In AWS | Tracked | Coverage | Gap |
|----------|--------|---------|----------|-----|
| Lambda | 136 | 105 | 77% | 31 unmapped |
| EC2 | 13 | 10 | 62% | 8 untracked |
| S3 | 33 | 10 | 30% | 23 not in TF |
| DynamoDB | 30 | 18 | 60% | 12 not in TF |
| IAM Roles | 43 | 28 | 65% | 15 not in TF |

**Biggest finding:** Entire trade subsystem (10 Lambdas, 5 S3 buckets, 3 DynamoDB tables, 2 IAM roles) completely outside Terraform.

**Deliverable:** `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/DEBT_1STRUN.001_infrastructure_audit.md`

---

## 5. EC2 Instance Cleanup

**Terminated 4 disposable instances** (Andrew + CTO authorized):

| Instance | Name | Type |
|----------|------|------|
| i-0e418d2fc0b891235 | docker-builder-temp | t3.medium |
| i-040a8cbaaaf295d95 | bd-all-historical-snapshots | r6i.4xlarge |
| i-090ae819ddc8ee5ea | bd-snapshot-gen-v3 | r6i.4xlarge |
| i-06dfcb7dfbfa7f78b | bd-snapshot-PRODUCTION | r6i.4xlarge |

**Added to EC2_MANIFEST:** historical-prices-fetcher (i-05ad83c1c075de14b, t3.xlarge) — actively managed by historical-prices-scheduler Lambda.

---

## 6. AUTH Macro Code + Project

**Proposed and CTO-approved:** New macro code `AUTH` — Portal Authentication, Authorization, and Identity. Owners: 0.7.0_AE_CloudOps (infra) + 0.4.0_DT_ClientPlatform (app layer).

**Rationale:** Auth is the foundation layer every portal feature depends on, not advisor intelligence. Work was previously scattered across ADVI projects (ADVI_ANONYM, ADVI_APISCP). Different owners, risk profiles, and change cadences warrant a dedicated surface area.

**First project:** AUTH_TFIMPT — import all auth infrastructure into Terraform.

---

## 7. Portal Auth Terraform Imports (AUTH_TFIMPT)

Three deploy tags this session, progressively importing the entire auth stack:

### portal-auth-v1.7.0 — IAM + DynamoDB Auth Tables

| Resource | Details |
|----------|---------|
| `lambda-edge-execution-role` | IAM role + inline policy + managed policy |
| `opal-firms` | 2 items, provisioned 5/5 RCU/WCU |
| `opal-sessions` | 3.2M items, PAY_PER_REQUEST, GSI1 |
| `user-permissions` | 12 items, PAY_PER_REQUEST, by-permission GSI |
| `opal-offices` | 1 item, provisioned 5/5 RCU/WCU |

**Commit:** `3ed11fdf` | **0-diff verified**

### portal-auth-v1.8.0 — Lambda@Edge Functions

Built and uploaded 5 edge function artifacts to S3, then imported:

| Function | Purpose | Size |
|----------|---------|------|
| auth-validator-edge | JWT validation on every request | 20KB |
| tier-router-edge | Tier-based content routing | 20KB |
| cache-control-injector | Response security headers | 1KB |
| public-data-router | Unauthenticated path routing | 1KB |
| shared-advisor-router | Firm-scoped data routing | 4KB |

**Fix applied:** Added `@aws-sdk/client-secrets-manager` to package.json for auth-validator-edge and tier-router-edge (was imported in code but missing from deps, broke bun build `--external` detection).

**Lambda@Edge gating:** Added `var.enable_lambda_edge` (default true) so future imports can be staged without S3 artifact dependency blocking other operations.

**Commit:** `3e08affb` | **0-diff verified**

### portal-auth-v1.9.0 — User Tables, SES, Secrets (AUTH_TFIMPT.002)

| Resource | Details |
|----------|---------|
| `opal-users` | 12 items, PAY_PER_REQUEST, hash key = email |
| `opal-users-v2` | 37 items, PAY_PER_REQUEST, 2 GSIs (firmId-index, email-index) |
| `opalinvest.dev` | SES domain identity (verified) |
| `opal/auth/jwt-private-key` | Secrets Manager container (no value in state) |
| `opal/auth/jwt-public-key` | Secrets Manager container (no value in state) |

**Known gap:** opal-users also exists in us-east-2 (IAM policy references both regions). Cross-region import requires second provider block — deferred.

**Commit:** `4ff913c2` | **0-diff verified**

---

## Portal-Auth TF State — Cumulative Inventory

| Category | Resources | Count |
|----------|-----------|-------|
| Lambda Functions | opalinvest-auth-handler, opal-portal-authorizer, auth-validator-edge, tier-router-edge, cache-control-injector, public-data-router, shared-advisor-router | 7 |
| IAM | lambda-edge-execution-role (+ 2 policies), opalinvest-auth-lambda-role (+ 3 policies), opal-portal-lambda-role (data source) | 2 managed + 1 ref |
| DynamoDB | opal-firms, opal-sessions, user-permissions, opal-offices, opal-users, opal-users-v2 | 6 |
| SES | opalinvest.dev domain identity | 1 |
| Secrets Manager | jwt-private-key, jwt-public-key (containers only) | 2 |
| CloudFront | opal-scoped-advisor-by-firm cache policy | 1 |
| Log Groups | 7 Lambda log groups + 1 shared-advisor-router | 8 |

---

## Next Steps — AUTH_TFIMPT.001 (Staged for Next Session)

### Objective
Import CloudFront distribution EVTSA9VEHNZVH (opalinvest.dev) into portal-auth TF state.

### Why This Is High-Risk
- This distribution serves ALL portal traffic (opalinvest.dev)
- CloudFront distributions have dozens of behaviors, origins, cache policies, and Lambda@Edge associations
- One wrong attribute on `terraform apply` could break portal routing, auth, or CORS
- Lambda@Edge associations reference specific function versions (not $LATEST) — version mismatch causes 502

### Preparation Required
1. **Full config extraction:** `aws cloudfront get-distribution-config --id EVTSA9VEHNZVH` — capture entire JSON
2. **Map all behaviors:** Each CloudFront behavior has an origin, cache policy, viewer/origin request Lambda@Edge, and origin response Lambda@Edge. Must enumerate all of them.
3. **Map Lambda@Edge version ARNs:** Each association references a specific published version (e.g., `arn:aws:lambda:us-east-1:313476888478:function:auth-validator-edge:5`). TF must match exactly.
4. **Write TF incrementally:** Start with the distribution shell, then add behaviors one at a time, verifying 0-drift at each step.
5. **Import before apply:** `terraform import aws_cloudfront_distribution.portal EVTSA9VEHNZVH` — then plan to identify all drift.

### Risk Mitigation
- **Read-only import first** — never apply until plan shows 0 structural changes
- **Ignore computed fields** — ETag, last_modified_time, etc. via `lifecycle { ignore_changes }`
- **Test in a fresh TF workspace first** if needed — verify import succeeds without touching the live distribution
- **Have rollback plan** — CloudFront changes take 10-15 min to propagate, and reverting a bad change also takes 10-15 min

### Task Order
`org/tier2_senior/0.7.0_AE_CloudOps/task_orders/AUTH_TFIMPT.001.ae-cloudfront-distribution-import.md` (status: staged)

---

## Commits This Session

| Commit | Tag | Description |
|--------|-----|-------------|
| `10fb7dbc` | `bd-v2.20.1` | Watchdog hardening + EventBridge schedule optimization |
| `9f3fc4fb` | — | RPS ingestion script |
| `3ed11fdf` | `portal-auth-v1.7.0` | Import IAM + 4 DynamoDB auth tables |
| `3e08affb` | `portal-auth-v1.8.0` | Import 5 Lambda@Edge functions |
| `9053418b` | — | Session logs, infra audit, EC2 manifest, AUTH task orders |
| `4ff913c2` | `portal-auth-v1.9.0` | Import user tables, SES, Secrets (AUTH_TFIMPT.002) |
