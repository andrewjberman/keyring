# ADVI-J1: opal-partner-49financial DynamoDB Table Deploy -- 0.7.0_AE_CloudOps

**Date:** 2026-03-04

## Objective

Create the opal-partner-49financial DynamoDB table and IAM read policy in
shared-infra Terraform, deploy to AWS, tag shared-infra-v1.3.0. This table is
the identity bridge between portal users (opal-users-v2) and the BD gold layer
advisor identity. Unblocks DT J2/J3 auth stream.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Write Terraform (DynamoDB table + IAM policy) | `shared-infra/main.tf` -- 2 new resources |
| 2 | Commit source | `1b918471` feat(shared-infra): opal-partner-49financial DynamoDB table + IAM read policy (ADVI-J1) |
| 3 | terraform plan | 2 to add, 0 to change, 0 to destroy |
| 4 | terraform apply | 2 added, 0 changed, 0 destroyed (table created in 25s) |
| 5 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 6 | Update core doc | pipeline_inventory.xml -- added dynamodb_tables section, IAM policy, updated tag to v1.3.0 |
| 7 | Commit core doc | `77a874f1` infra(shared-infra): update pipeline_inventory.xml for shared-infra-v1.3.0 |
| 8 | Tag + push | `shared-infra-v1.3.0` pushed to CLOUD |

## Verification

```
aws dynamodb describe-table --table-name opal-partner-49financial
{
    "TableName": "opal-partner-49financial",
    "TableArn": "arn:aws:dynamodb:us-east-1:313476888478:table/opal-partner-49financial",
    "KeySchema": [{"AttributeName": "email", "KeyType": "HASH"}],
    "GSI": [{"IndexName": "ByAdvisorRole", "KeySchema": [{"AttributeName": "advisorRole", "KeyType": "HASH"}], "ProjectionType": "ALL"}],
    "BillingMode": "PAY_PER_REQUEST",
    "Status": "ACTIVE"
}
```

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| shared-infra | `shared-infra-v1.3.0` | `77a874f1` |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Added DynamoDB table + IAM to shared-infra (not a new module) | Task order specified shared-infra; table is shared infrastructure consumed by auth-handler across partners |
| Used PAY_PER_REQUEST billing | Table is tiny (~20-30 records); on-demand avoids provisioned capacity overhead |
| IAM policy on opalinvest-auth-lambda-role by name string | Same pattern as existing portal_lambda_ec2_snapshot policy; role name confirmed at portal-auth/iam.tf:16 |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/terraform/shared-infra/main.tf` | Added aws_dynamodb_table.opal_partner_49financial + aws_iam_role_policy.partner_identity_read | Yes -- `1b918471` |
| `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/pipeline_inventory.xml` | Added dynamodb_tables section, IAM policy, updated tag | Yes -- `77a874f1` |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI-J1-partner-identity-dynamo.md` | Status: pending -> complete | This session (uncommitted) |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

opal-partner-49financial DynamoDB table is live in us-east-1 (ACTIVE, PAY_PER_REQUEST,
email PK, ByAdvisorRole GSI). IAM inline policy PartnerIdentityReadPermissions is attached
to opalinvest-auth-lambda-role granting dynamodb:GetItem + dynamodb:Query. Tag
shared-infra-v1.3.0 applied and pushed. Table is empty -- population is a separate manual
admin step at advisor onboarding time.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Begin J2** -- auth-handler Lambda update to read opal-partner-49financial by email at login. Table ARN: `arn:aws:dynamodb:us-east-1:313476888478:table/opal-partner-49financial`. IAM is already attached to `opalinvest-auth-lambda-role`.
2. **[0.4.0_DT_ClientPlatform] Begin J3 after J2** -- portal-authorizer passthrough of firmId, advisorKey, advisorRole claims.
3. **[Andrew] Populate table** -- manual DynamoDB PutItem for each 49 Financial advisor once portal accounts are created.

**Do NOT:**
- Modify opal-users-v2 schema -- partner identity lives in partner-specific tables only
- Add data to opal-partner-49financial in this stream -- population is a separate admin operation
