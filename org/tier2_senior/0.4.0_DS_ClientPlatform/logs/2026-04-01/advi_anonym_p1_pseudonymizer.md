# ADVI_ANONYM P1: pseudonymizer.py + Lambda Wiring -- 0.4.0_DS_ClientPlatform

**Date:** 2026-04-01
**Start Time:** 2:58 PM ET
**End Time:** 3:30 PM ET
**Project:** ADVI_ANONYM
**Task Order:** ADVI_ANONYM.002.ds-pseudonymizer-lambda.md

---

## Objective

Implement HMAC-based pseudonymization in the opal-partners-data Lambda. GO received
from COO at 2:58 PM ET. Create pseudonymizer.py and wire pseudonymize_response()
into all PII-bearing handler call sites.

---

## Work Completed

### 1. Full lambda_function.py Read

Read all 1,319 lines of lambda_function.py before writing any code. Identified all
handler functions, their response patterns, and which serve client-level PII.

### 2. Handler PII Audit

| Handler | PII Present | Action |
|---|---|---|
| handle_get_partners | No (firm metadata only) | No change |
| handle_timeseries (relationship) | Yes (relationship labels in JSON) | _pseudonymize_s3_response |
| handle_timeseries (other dimensions) | No (architect/geo aggregates) | No change |
| handle_snapshots | No | No change |
| handle_filters | No | No change |
| handle_client_growth | Yes (relationship names in growth entries) | _pseudonymize_s3_response |
| handle_tax_breakdown | Yes (relationship names) | _pseudonymize_s3_response |
| handle_tax_deferred | Yes (relationship names) | _pseudonymize_s3_response |
| handle_summary | No | No change |
| handle_partner_analytics | Yes (top_clients list with name field) | _pseudonymize_s3_response |
| handle_advisor_book | Yes (client list in advisor book.json) | _pseudonymize_s3_response |
| handle_health_check | No | No change |
| handle_books_timeseries (relationship/account) | Yes (entity_id is client/account key in response) | _pseudonymize_s3_response |
| handle_books_composition (relationship/account) | Yes (scope.relationship_id / scope.account_id) | _pseudonymize_s3_response |
| handle_books_composition (firm) | No (aggregate, already nocache) | No change |
| handle_advisor_composition | No (aggregate, already nocache) | No change |
| handle_advisor_timeseries | Yes (book_name / advisor identity) | _pseudonymize_s3_response |
| handle_advisor_mix_timeseries | No (aggregate mix pct, no names) | No change |
| handle_firm_mix_views | No (aggregate) | No change |
| handle_advisor_mix_views | No (aggregate) | No change |
| handle_firm_composition | No (aggregate, already nocache) | No change |
| handle_mix_timeseries | No (not in TO PII list) | No change |
| handle_concentration_timeseries | No (not in TO PII list) | No change |

**Finding: handle_adv_drill does not exist.** The TO references this handler for the
Distribution endpoint client-segment drill data, but it is not implemented in the
current lambda_function.py. When it is added, it will need pseudonymizer wiring at
the routing call site (PII: clients[].label + clients[].key, only client-segment
data not top-level architect/geo segments).

### 3. Implementation Approach

For serve_s3_json-based handlers (PII in pre-built S3 JSON files): applied
post-processing via `_pseudonymize_s3_response(handler_resp, ...)` at the routing
call site in lambda_handler. This avoids restructuring handler signatures while
achieving the same effect as pre-wrapping.

`_pseudonymize_s3_response`:
- Parses the response body JSON
- Calls pseudonymizer.pseudonymize_response() (no-op for internal/admin users)
- Always re-wraps with cors_response_nocache (no-store for ALL users, not just advisor-user)

For handle_books_timeseries and handle_books_composition (inline response_body):
same pattern applied at their routing call sites.

### 4. IAM Permissions -- BLOCKER for DT

**Missing:** `secretsmanager:GetSecretValue` and `secretsmanager:CreateSecret`
for `opal/pseudonym/*` on `partners-lambda-role`.

**Evidence:** Searched all partners-api Terraform (only main.tf and lambdas.tf).
The role is defined in shared-infra/main.tf. The only secretsmanager permission
present is `GetSecretValue` for `openai-api-key-*`.

**Required addition to shared-infra/main.tf (or a new policy attached to
`partners-lambda-role`):**
```
Action:   ["secretsmanager:GetSecretValue", "secretsmanager:CreateSecret"]
Resource: "arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/pseudonym/*"
```

This is a DT task -- I cannot modify iam.tf. Without this permission, the Lambda
will throw AccessDeniedException on first call to pseudonymizer._get_firm_key().

### 5. Files Created/Modified

| File | Change | Committed |
|---|---|---|
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/pseudonymizer.py` | New -- HMAC pseudonymizer with lazy key provisioning | Yes -- `3fdb9a51` |
| `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py` | Added import, user_role extraction, _pseudonymize_s3_response helper, 9 PII call site wrappers | Yes -- `3fdb9a51` |

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Post-process approach (_pseudonymize_s3_response) vs modifying handler signatures | Minimal code change; handler signatures don't need to change; consistent pattern across all 9 PII sites |
| nocache for ALL users (not just advisor-user) | The raw response bodies contain client PII regardless of who's viewing; caching them anywhere (CDN, browser) is unsafe |
| handle_adv_drill skipped | Handler does not exist in current code; cannot wire what isn't there |

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| This session log | This file | COO, DT |

---

## Current State

**Status:** COMPLETE (DS deliverable). DT deployment and IAM fix pending.
**Active branch:** `CLOUD`

pseudonymizer.py and lambda_function.py both committed at `3fdb9a51`. NOT pushed.
DT must (1) grant secretsmanager permissions on partners-lambda-role (via shared-infra
Terraform), (2) push and deploy via partners-api Terraform, (3) remove the P0 role
gate from auth-validator-edge AFTER verifying pseudonymizer end-to-end.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform]** Add secretsmanager IAM to partners-lambda-role in
   shared-infra/main.tf:
   `secretsmanager:GetSecretValue` + `secretsmanager:CreateSecret` for
   `arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/pseudonym/*`

2. **[0.4.0_DT_ClientPlatform]** Push CLOUD branch and deploy partners-api via Terraform.
   Run build-and-upload.sh, terraform plan, terraform apply, verify 0-diff.

3. **[0.7.0_AE_CloudOps / 0.4.0_DT_ClientPlatform]** Provision Secrets Manager keys
   for each firm (`opal/pseudonym/{firmId}`). The lazy provisioning fallback will create
   them on first request if AE hasn't pre-provisioned.

4. **[0.4.0_DT_ClientPlatform]** Remove P0 role gate from auth-validator-edge ONLY
   after pseudonymizer is verified end-to-end (test with advisor-user token, confirm
   hashed names in response).

5. **[0.4.0_DS_ClientPlatform]** Wire handle_adv_drill when that handler is implemented.

**Do NOT:**
- Push this branch before DT verifies the IAM permission is in place
- Remove P0 gate before pseudonymizer is tested end-to-end
- Apply pseudonymizer to architect (advisor) names -- the `_transform_field` function
  does NOT hash `advisor_name` fields, only `book_name` for navigation consistency
