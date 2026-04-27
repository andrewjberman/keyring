# Session Log — ADVI_INFLEC.TO-A: Orion Infra Audit

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-27
**TO:** ADVI_INFLEC.TO-A.ae-orion-infra-audit
**Status:** COMPLETE
**Commits:** a070c3a9 (s3.tf lifecycle rule)
**Tag:** inf-pipeline-v1.5.2

---

## Audit Results

| # | Check | Result | Action |
|---|-------|--------|--------|
| 1 | orion/credentials Secrets Manager secret | PASS — exists, populated by Andrew | None |
| 2 | S3 lifecycle rule otp/ prefix on opal-data-inf | ABSENT on audit | ADDED + APPLIED (a070c3a9) |
| 3 | inf-otp-relay Function URL | CAPTURED | MCPed to COO + Andrew |
| 4 | inf-exporter IAM (otp/ + bronze/orion/) | PASS — verified via TF source | None |
| 5 | inf-otp-relay IAM (otp/ write) | PASS — verified via TF source | None |

---

## Check 1 — orion/credentials

```
aws secretsmanager describe-secret --secret-id orion/credentials
```

Secret exists. ARN: `arn:aws:secretsmanager:us-east-1:313476888478:secret:orion/credentials-jrq3yI`
LastChangedDate: 2026-04-22 (Andrew has populated credentials).
Tags: Project=OpalPortal, System=InflectionPipeline, ManagedBy=Terraform.

**Result: PASS**

---

## Check 2 — S3 Lifecycle Rule

```
aws s3api get-bucket-lifecycle-configuration --bucket opal-data-inf
```

Result: `NoSuchLifecycleConfiguration` — no lifecycle rule existed.

**Action taken:** Added `aws_s3_bucket_lifecycle_configuration.inf_data` to
`infra/aws/terraform/inf-pipeline/s3.tf`:
- Rule ID: `otp-prefix-expiry`
- Status: Enabled
- Filter prefix: `otp/`
- Expiration: 1 day

**Discrepancy:** TO-A spec said "expiration 600s (10 min)". S3 lifecycle rules
minimum granularity is 1 DAY. Sub-day expiry is not achievable via lifecycle rules.
Used 1 day as the minimum feasible safety-net. If 10-min expiry is truly required,
a separate mechanism (EventBridge + Lambda cleanup) is needed. Flagged to COO.

terraform plan: 1 to add, 0 to change, 0 to destroy.
terraform apply: 1 added. 0-diff confirmed post-apply.

**Result: ADDED + APPLIED**

---

## Check 3 — Function URL

```
aws lambda get-function-url-config --function-name inf-otp-relay
```

Function URL captured. AuthType=NONE (correct — resource policy shipped 01df38f1).
CORS: AllowMethods=[POST, GET], AllowOrigins=*.
URL MCPed to COO + Andrew (not logged here per TO-A do_not rule).

**Result: PASS**

---

## Check 4 — inf-exporter IAM

`comp-iam service inf-exporter` → "No service matching 'inf-exporter'"
(comp-iam indexes EC2 script ASTs, not IAM roles — expected behavior for EC2 service.)

Verified via TF source `infra/aws/terraform/inf-pipeline/iam.tf` lines 335-354:

`aws_iam_role_policy.inf_exporter_s3` (s3-scoped-inf-exporter):
- Actions: s3:PutObject, s3:GetObject, s3:DeleteObject, s3:HeadObject, s3:ListBucket
- Resources: opal-data-inf (bucket), opal-data-inf/bronze/orion/*, opal-data-inf/otp/*

`aws_iam_role_policy.inf_exporter_secrets` (secrets-manager-orion):
- Actions: secretsmanager:GetSecretValue
- Resources: orion/credentials-* (wildcard suffix for rotation)

All required permissions present: otp/ read+delete + bronze/orion/ write + Secrets Manager.

**Result: PASS**

---

## Check 5 — inf-otp-relay IAM

`comp-iam service inf-otp-relay` → "No service matching 'inf-otp-relay'" (Lambda, not EC2 script.)

Verified via TF source `infra/aws/terraform/inf-pipeline/lambda-otp-relay.tf` lines 25-40:

`aws_iam_role_policy.inf_otp_relay_s3` (s3-otp-rw):
- Actions: s3:PutObject, s3:GetObject, s3:DeleteObject, s3:HeadObject
- Resources: opal-data-inf/otp/*

s3:PutObject on otp/* present.

**Result: PASS**

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| comp-iam service | inf-exporter | "No service matching" — EC2 role, not EC2 script. Verified via TF source instead. |
| comp-iam service | inf-otp-relay | "No service matching" — Lambda role, not EC2 script. Verified via TF source instead. |
| terraform plan | inf-pipeline | 1 to add (lifecycle rule), 0 change, 0 destroy |
| terraform plan (0-diff) | inf-pipeline | No changes. Infrastructure is up-to-date. |

---

## Deployment

| Step | Action | Result |
|------|--------|--------|
| 1 | Edit infra/aws/terraform/inf-pipeline/s3.tf | aws_s3_bucket_lifecycle_configuration added |
| 2 | terraform plan | 1 to add |
| 3 | terraform apply | 1 added, clean |
| 4 | terraform 0-diff plan | No changes |
| 5 | git commit --only | a070c3a9 |
| 6 | git tag inf-pipeline-v1.5.2 + push --follow-tags | CLOUD pushed |

---

## Acceptance Criteria

| # | Criterion | Status |
|---|-----------|--------|
| 1 | orion/credentials secret exists | PASS |
| 2 | S3 lifecycle rule on otp/ prefix active | PASS (added + applied, a070c3a9) |
| 3 | Function URL captured + MCPed | PASS |
| 4 | comp-iam inf-exporter: otp/ + bronze/orion/ permissions present | PASS (TF source verified) |
| 5 | comp-iam inf-otp-relay: otp/ write present | PASS (TF source verified) |
| 6 | Session log with all command outputs | PASS (this log) |
| 7 | RAVC4 to COO with all findings | PASS (sent) |

**TO-A: COMPLETE**

---

## Next Steps

- TO-B: staged, gate = Andrew A1 (W0.3 pairing session)
- TO-C through TO-F: further gated on TO-B + Andrew A2
- ORNREN.002: still gated on DS ORNREN.001 MCP signal
- TRSB_TFIMPT.W3: still staged, gated on COO GO + Andrew SES
