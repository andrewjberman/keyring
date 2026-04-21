# Session Log -- 2026-04-21 -- ADVI_INFLEC.W5.5 User Provisioning

| Field | Value |
|-------|-------|
| Agent | 0.4.0_DT_ClientPlatform |
| Date  | 2026-04-21 |
| TO    | ADVI_INFLEC.W5.5.dt-user-provisioning |
| Issued by | 2.0.0_SA_COO |
| Authorization | COO GO (in-session) |

---

## Objective

Provision first Inflection portal users per ONBOARDING.md §2. Two writes per user: opal-users-v2 master row + opal-partner-inflection partner row.

---

## Test User Note

No real Inflection user emails are available yet (gold pipeline not yet run; Andrew has not provided email list). Per TO: "If no real Inflection users yet, provision a test user for smoke testing only -- clearly labeled as test." Provisioned one test admin user to unblock W5.6/W5.7.

advisorKey note: `inflection_test_admin` is a test-only slug, not derived from I_D00c (which has not run for Inflection yet). Real advisorKey values from I_D00c will be: jeremy_keil, dan_sinnen, tim_demuth, john_kurcz, peter_lee, patrick_scanlan, daria_zalewska (derived deterministically by `_advisor_key()` in convert_orion_to_silver.py). Replace test user when real Inflection users are provisioned.

---

## Provisioning

### User: test-admin@inflectionwealthmgmt.com

**Step 1 -- opal-users-v2**

```
aws dynamodb put-item --table-name opal-users-v2 \
  --item {PK: USER#test-admin@inflectionwealthmgmt.com, SK: PROFILE, firmId: inflection, role: user, ...} \
  --condition-expression "attribute_not_exists(PK)"
```

Exit: 0 (success)

**Step 2 -- opal-partner-inflection**

```
aws dynamodb put-item --table-name opal-partner-inflection \
  --item {email: test-admin@inflectionwealthmgmt.com, advisorKey: inflection_test_admin, advisorRole: architect, firmRole: admin} \
  --condition-expression "attribute_not_exists(email)"
```

Exit: 0 (success)

---

## Verification (get-item output)

### opal-partner-inflection

```json
{
    "Item": {
        "advisorRole": {"S": "architect"},
        "advisorName": {"S": "Inflection Test Admin"},
        "advisorKey": {"S": "inflection_test_admin"},
        "email": {"S": "test-admin@inflectionwealthmgmt.com"},
        "firmRole": {"S": "admin"},
        "createdBy": {"S": "0.4.0_DT_ClientPlatform"},
        "createdAt": {"S": "2026-04-21T21:19:37.98Z"}
    }
}
```

### opal-users-v2

```json
{
    "Item": {
        "PK": {"S": "USER#test-admin@inflectionwealthmgmt.com"},
        "SK": {"S": "PROFILE"},
        "email": {"S": "test-admin@inflectionwealthmgmt.com"},
        "firmId": {"S": "inflection"},
        "role": {"S": "user"},
        "tier": {"S": "advisor"},
        "mustChangePassword": {"BOOL": true},
        "status": {"S": "active"},
        "createdBy": {"S": "0.4.0_DT_ClientPlatform"},
        "createdAt": {"S": "2026-04-21T21:19:37.98Z"}
    }
}
```

---

## Acceptance Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | At least one opal-users-v2 USER row with firmId=inflection | PASS | PK=USER#test-admin@inflectionwealthmgmt.com, firmId=inflection |
| 2 | Corresponding opal-partner-inflection row (advisorKey note: test slug, I_D00c not yet run) | CONDITIONAL PASS | advisorKey=inflection_test_admin; real keys TBD from I_D00c |
| 3 | At least one user has firmRole=admin | PASS | firmRole=admin in partner row |
| 4 | condition-expression "attribute_not_exists" used on both writes | PASS | Both put-item calls used condition-expression |
| 5 | Session log with get-item verify output | PASS | This file |

---

## Current State

- Test admin user provisioned. Auth flow validation (W5.6) unblocked.
- Real Inflection users to be provisioned when Andrew provides email list (post gold-pipeline run).
- Lambda@Edge CloudFront propagation from W1.6+W1.7 was deployed in the same terraform apply as W1.5. Sufficient time has elapsed for propagation -- proceeding to W5.6.
