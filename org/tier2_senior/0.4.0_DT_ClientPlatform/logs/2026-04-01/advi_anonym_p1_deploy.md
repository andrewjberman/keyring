# ADVI_ANONYM P1 Full Deployment -- 0.4.0_DT_ClientPlatform

**Date:** 2026-04-01
**Start Time:** 10:45 AM ET
**End Time:** 11:21 AM ET

## Objective

Execute ADVI_ANONYM.004: deploy pseudonymizer Lambda, attach auth-validator-edge to partners CloudFront behaviors, and remove P0 role gate. Three tracks, sequential safety ordering.

---

## Work Completed

### Track B -- CloudFront Behaviors 13+14 (DONE)

Attached auth-validator-edge:8 to CloudFront behaviors:
- Behavior 13: `/api/scoped/partners/*`
- Behavior 14: `/api/partners`

Both previously had no Lambda@Edge (added in DT session 2026-03-31 without auth).

| Metric | Value |
|--------|-------|
| ETag before | `E3PD1DBIXH44AJ` |
| ETag after | `E3PDIZ4U73Y3BG` |
| Distribution status | Deployed |
| Verification | unauth curl -> 401 on both paths |

### Track A -- opal-partners-data Lambda Deploy (DONE)

Deployed opal-partners-data with DS pseudonymizer module.

| Metric | Value |
|--------|-------|
| DS commit | `3fdb9a51` (pseudonymizer.py + lambda_function.py wiring) |
| Source map fix | Added `pseudonymizer.py` to files list (was missing) |
| Zip SHA256 | `/op/PBG5m8CgIiRFvk/szFMJd9zAWk7CpLVoam+7xPg=` |
| Zip size | 28K |
| Terraform | apply 0-diff confirmed |
| Tag | `partners-api-v1.11.0` |
| DT commit | `4485ec1c` |

Verification:

| Endpoint | Tier/Role | Status | Result |
|----------|-----------|--------|--------|
| partner-analytics | advisor/user | 200 | Hashed: `Client aa304c3b`, `id ef9b0465` |
| partner-analytics | internal/admin | 200 | Cleartext: `Non-Qualified`, `taxable` |
| firm composition | advisor/user | 200 | Ticker symbols (no client PII -- correct) |
| summary | internal/admin | 200 | Cleartext |

No Secrets Manager cold-start failures -- AE IAM (partners-api-v1.10.0) is live.

### Track C -- P0 Role Gate Removal (DONE)

Removed interim admin-only gate from auth-validator-edge (lines 58-66 of v8).

| Metric | Value |
|--------|-------|
| New version | auth-validator-edge:9 |
| ARN | `arn:aws:lambda:us-east-1:313476888478:function:auth-validator-edge:9` |
| Behaviors updated | All 10 (from :8 to :9) |
| ETag after | `E1YMMKG9CKL5TK` |
| Distribution status | Deployed |
| DT commit | `92ae074c` |

Track C verification:

| Endpoint | Tier/Role | Status | Before Track C |
|----------|-----------|--------|----------------|
| summary | advisor/user | 200 | Was 403 (gate blocked) |
| summary | internal/admin | 200 | Was 200 (unchanged) |

ADVI_ANONYM.001 task order archived.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Added pseudonymizer.py to source map files list | DS created the file but lambda-source-map.json wasn't updated -- build excluded it |
| Updated all 10 auth-validator-edge behaviors to v9 (not just 2+5) | All behaviors should run the same version; leaving :8 on some creates version skew |
| Used PowerShell for zip (not zip CLI) | zip not available in Git Bash; established pattern for Lambda@Edge builds |

---

## Files Modified

| File | Change | Commit |
|------|--------|--------|
| `infra/aws/lambda/ci/lambda-source-map.json` | Added pseudonymizer.py to opal-partners-data files + new artifact SHA | `4485ec1c` |
| `infra/aws/lambda-edge/auth-validator-edge/index.mjs` | Removed P0 role gate (lines 58-66), added v9 version comment | `92ae074c` |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_ANONYM.001.dt-deploy-auth-validator-v8.md` | Status: complete -> archived | `92ae074c` |

## AWS Resources Modified

| Resource | Change |
|----------|--------|
| CloudFront EVTSA9VEHNZVH behaviors 13+14 | Added auth-validator-edge LFA |
| CloudFront EVTSA9VEHNZVH all 10 behaviors | Updated auth-validator-edge :8 -> :9 |
| Lambda opal-partners-data | New code with pseudonymizer.py |
| Lambda auth-validator-edge:9 | Published v9 (P0 gate removed) |

---

## Deployment Tags

| Pipeline | Tag | Source |
|----------|-----|--------|
| partners-api | `partners-api-v1.11.0` | `4485ec1c` |

---

## Current State

> **Status:** COMPLETE
> **Active branch:** CLOUD

ADVI_ANONYM P1 is fully deployed and verified. All three tracks (A, B, C) complete. CloudFront distribution EVTSA9VEHNZVH has auth-validator-edge v9 on all 10 auth-requiring behaviors. opal-partners-data Lambda includes pseudonymizer module. advisor/user tier now gets 200 with HMAC-hashed client names instead of 403.

## Next Steps

1. **[Monitor]** Watch CloudWatch logs for `auth-validator-edge` and `opal-partners-data` for any errors in the first 24 hours -- especially Secrets Manager lazy provisioning on first advisor/user request per firm.
2. **[ADVI_ANONYM P2+]** If future phases require additional pseudonymization fields or handler coverage, DS reviews handler audit notes from .002 task order.
3. **[Terraform import consideration]** CloudFront distribution EVTSA9VEHNZVH remains console-managed. 14 behaviors now, growing -- consider Terraform import to prevent drift.

**Do NOT:**
- Re-add the P0 role gate -- it is replaced by the pseudonymizer
- Modify portal_authorizer -- it already returns role correctly (deployed 2026-03-04)
- Assume auth-validator-edge covers behavior 1 (`/api/scoped/advisor-intelligence/clients/*`) -- it does NOT have Lambda@Edge attached
