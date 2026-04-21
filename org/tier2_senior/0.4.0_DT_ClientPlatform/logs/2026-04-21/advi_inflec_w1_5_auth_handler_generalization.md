# Session Log -- 2026-04-21 -- ADVI_INFLEC.W1.5 auth-handler generalization

| Field | Value |
|-------|-------|
| Agent | 0.4.0_DT_ClientPlatform |
| Date  | 2026-04-21 |
| TO    | ADVI_INFLEC.W1.5.dt-auth-handler-generalization |
| Issued by | 2.0.0_SA_COO |
| Authorization | COO GO efe74984 |

---

## Objective

Generalize auth-handler to support Inflection as a second partner firm: dynamic opal-partner-${firmId} table lookup (already present via lib/partner), add IAM wildcard grant for all opal-partner-* tables, add structured ResourceNotFoundException logging in db.ts.

---

## Compiler Tools

| Tool | Phase | Run | Result | Notes |
|------|-------|-----|--------|-------|
| `comp-iam service opalinvest-auth-handler` | 1 (before) | Run | No MISSING permissions flagged | Pre-check clean |
| `comp-iam gaps` | 3 (after apply) | Run | No regressions | IAM wildcard verified clean |

---

## Key Finding: Code Already Generalized

Pre-existing state: `db.ts:getPartnerIdentity` already called `getPartnerProfile(email, firmId)` via `lib/partner` — NO hardcoded `PARTNER_TABLE_49FIN` constant. The lib/partner canonical source (`infra/aws/lambda/lib/partner/tableName.ts`) returns `opal-partner-${normalized}` dynamically.

Actual work performed:
1. Added try/catch for `ResourceNotFoundException` in `db.ts:getPartnerIdentity` with structured log: `partner_table_missing firmId=${firmId}` (graceful null return instead of hard throw)
2. Added IAM wildcard statement to `infra/aws/terraform/portal-auth/iam.tf` `auth_permissions` policy: `dynamodb:GetItem` on `arn:aws:dynamodb:*:${local.account_id}:table/opal-partner-*`
3. Built and uploaded new `opalinvest-auth-handler` artifact via `build-nodejs-lambda.sh`
4. Updated `infra/aws/lambda/ci/lambda-source-map.json` artifact SHA

---

## Terraform Apply

| Field | Value |
|-------|-------|
| Workspace | portal-auth |
| Resources changed | 4 (aws_iam_role_policy.auth_permissions, aws_lambda_function.auth_handler, aws_lambda_function.auth_validator_edge[0], aws_lambda_function.shared_advisor_router[0]) |
| Post-apply plan | 0-diff confirmed |
| Tag | portal-auth-v1.14.0 |

Note: auth_validator_edge and shared_advisor_router were co-deployed due to AE's W1.6+W1.7 FIRM_BUCKET_MAP change (c9f6c7e6) being in HEAD at apply time. 4-change apply was correct and expected.

---

## Files Modified

| File | Action |
|------|--------|
| `infra/aws/opalinvest_dev/lambda/auth-handler/src/db.ts` | Modified — ResourceNotFoundException try/catch in getPartnerIdentity |
| `infra/aws/terraform/portal-auth/iam.tf` | Modified — opal-partner-* wildcard IAM grant |
| `infra/aws/lambda/ci/lambda-source-map.json` | Modified — artifact SHA updated |
| `infra/aws/terraform/portal-auth/CHANGELOG.json` | Modified — v1.14.0 entry appended |

---

## Commits

| Commit | Description |
|--------|-------------|
| `efe74984` | feat(ADVI_INFLEC): W1.5 auth-handler partner table generalization + IAM wildcard |
| `0807d80c` | ci: upload opalinvest-auth-handler artifact [skip ci] |
| `e801a170` | ci: record deploy portal-auth @ 8de4a3a3 [skip ci] |

Tag: `portal-auth-v1.14.0`

---

## Acceptance Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | auth-handler uses dynamic firmId for partner table lookup (no hardcoded constant) | PASS | lib/partner/tableName.ts already generic; verified |
| 2 | ResourceNotFoundException handled gracefully with structured log | PASS | efe74984 db.ts try/catch |
| 3 | IAM wildcard covers all opal-partner-* tables | PASS | iam.tf wildcard Resource added |
| 4 | Build artifact uploaded + source map updated | PASS | 0807d80c artifact SHA = pbX4ExbfZNYuJAqJoTJMaBFeD+wv3Cm+/uhwd7Jn0SY= |
| 5 | 0-diff plan confirmed post-apply | PASS | "No changes. Your infrastructure matches the configuration." |
| 6 | Tagged + pushed | PASS | portal-auth-v1.14.0 |

---

## Current State

- W1.5 complete and deployed.
- Inflection partner identity lookup is live; auth-handler will read opal-partner-inflection on login.
- W5.6 (auth flow validation) requires 15+ min Lambda@Edge CloudFront propagation (from W1.6+W1.7 c9f6c7e6 deploy at same apply).
