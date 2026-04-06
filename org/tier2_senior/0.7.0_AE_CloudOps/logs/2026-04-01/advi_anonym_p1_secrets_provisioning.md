# ADVI_ANONYM P1 — Secrets Provisioning + IAM Grant -- 0.7.0_AE_CloudOps

**Date:** 2026-04-01
**Task Order:** ADVI_ANONYM.003.ae-secrets-provisioning
**Tag:** partners-api-v1.10.0

---

## Objective

Provision per-firm HMAC pseudonymization keys in AWS Secrets Manager and grant
the opal-partners-data Lambda IAM access to read and create them. Infrastructure
prerequisite for ADVI_ANONYM P1 before DS deploys the pseudonymizer module.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Scan opal-users-v2 for active firms | 2 firms: opal-capital, 49financial |
| 2 | Create opal/pseudonym/opal-capital | ARN: arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/pseudonym/opal-capital-w7wHIU |
| 3 | Create opal/pseudonym/49financial | ARN: arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/pseudonym/49financial-jggsn3 |
| 4 | Write infra/aws/terraform/partners-api/iam.tf | Role + inline policy + attachments |
| 5 | Commit f81ce119 | infra(ADVI_ANONYM P1): grant opal-partners-data access to pseudonym secrets |
| 6 | Import aws_iam_role.partners_lambda | partners-lambda-role |
| 7 | Import aws_iam_role_policy.partners_lambda_permissions | partners-lambda-role:partners-lambda-permissions |
| 8 | Import aws_iam_role_policy_attachment.partners_lambda_basic | AWSLambdaBasicExecutionRole |
| 9 | Import aws_iam_role_policy_attachment.partners_lambda_bd_securities | bd-securities-access |
| 10 | terraform plan | 0 to add, 2 to change, 0 to destroy (PseudonymSecrets SID + tag normalization) |
| 11 | terraform apply | Apply complete! Resources: 0 added, 2 changed, 0 destroyed |
| 12 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 13 | Verify secrets retrievable | OK: opal-capital (64-char hex), OK: 49financial (64-char hex) |
| 14 | Tag partners-api-v1.10.0 + push --follow-tags | Pushed |

---

## Firms Provisioned

| Firm ID | Secret Path | Status |
|---------|-------------|--------|
| opal-capital | opal/pseudonym/opal-capital | Created (32-byte random hex) |
| 49financial | opal/pseudonym/49financial | Created (32-byte random hex) |

Total: 2 firms. No existing secrets were overwritten (none pre-existed).

---

## IAM Changes

**Role:** partners-lambda-role
**Policy:** partners-lambda-permissions (inline)

Added statement:
```json
{
  "Sid": "PseudonymSecrets",
  "Effect": "Allow",
  "Action": [
    "secretsmanager:GetSecretValue",
    "secretsmanager:CreateSecret"
  ],
  "Resource": "arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/pseudonym/*"
}
```

Also brought partners-lambda-role under Terraform management for the first time
(previously created manually). iam.tf now tracks the role, inline policy, and
both managed policy attachments.

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| partners-api | partners-api-v1.10.0 | f81ce119 |

---

## Verification

```
OK: opal/pseudonym/opal-capital -- retrievable (64-char hex key)
OK: opal/pseudonym/49financial -- retrievable (64-char hex key)
```

Secrets confirmed retrievable via AWS CLI directly. Lambda execution role
can call GetSecretValue on opal/pseudonym/* per the applied IAM policy.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD
**Tag:** partners-api-v1.10.0

All secrets created. IAM policy applied and at 0-diff. Both secrets verified
retrievable. DS (.002) can now fetch opal/pseudonym/{firmId} keys at Lambda
runtime. DT can deploy the updated Lambda once DS completes.

---

## Next Steps

1. **[DS 0.4.0_DS_ClientPlatform]** Complete ADVI_ANONYM.002 pseudonymizer module
2. **[DT 0.4.0_DT_ClientPlatform]** Deploy updated Lambda after DS and AE both signal complete
3. **[AE 0.7.0_AE_CloudOps]** Monitor: if new firms are onboarded, create their opal/pseudonym/{firmId} secret manually or via automation (CreateSecret permission is now granted)
