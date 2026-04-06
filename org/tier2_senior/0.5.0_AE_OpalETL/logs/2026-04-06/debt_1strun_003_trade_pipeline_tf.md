# DEBT_1STRUN.003 -- Trade Pipeline Terraform Module

**Date:** 2026-04-06
**Agent:** 0.5.0_AE_OpalETL
**Task Order:** DEBT_1STRUN.003.ae-trade-subsystem-tf-pipeline.md
**Project:** DEBT_1STRUN
**Status:** COMPLETE

---

## Summary

Created new TF pipeline `infra/aws/terraform/trade-pipeline/` for the entire trade subsystem. Imported 63 AWS resources into TF state. Achieved 0-drift after apply.

---

## Resources Imported (63 total)

| Type | Count | Details |
|------|-------|---------|
| Lambda functions | 11 | trade-auth-handler, trade-authorizer, trade-dashboard-api, trade-identifier-cache, trade-parquet-batch-export, trade-submission-handler, trade-workflow-handler, trade-recon-api, trade-recon-auth, trade-recon-authorizer, trade-recon-processor |
| CloudWatch log groups | 11 | One per Lambda |
| S3 buckets | 5 | opal-trade-form-ui, opal-trade-recon-ui, opal-trade-recon-confirms, opal-trade-recon-reports, opal-trade-recon-requests |
| S3 sub-resources | 22 | versioning (5), encryption (5), public-access-block (5), website (2) |
| DynamoDB tables | 3 | trade-recon-jobs, trade-security-identifiers, trade-users (with by-role GSI) |
| IAM roles | 2 | trade-submission-lambda-role, trade-recon-lambda-role |
| IAM inline policies | 3 | trade-submission-policy, opal-users-v2-access, trade-recon-access |
| IAM policy attachment | 1 | AWSLambdaBasicExecutionRole on trade-recon |

## Architecture Decisions

1. **JWT_SECRET as sensitive variable** -- `var.jwt_secret` with `sensitive = true`, no default. Pass via `-var` or `.auto.tfvars` (gitignored). No secrets in git.

2. **lifecycle ignore_changes on code** -- All 11 Lambdas use `ignore_changes = [filename, source_code_hash]` since code is EXTERNAL (deployed via console/legacy scripts, no repo source).

3. **pandas-pyarrow-layer:1** -- Used by trade-parquet-batch-export. Hardcoded ARN (same pattern as openpyxl-layer in yang-pipeline).

4. **trade-submissions table** -- Referenced in IAM policy but does NOT exist in AWS. Policy is stale; TF matches the live policy exactly.

## Apply Results

- First plan: 0 add, 33 change, 0 destroy
- Changes: log retention (0->14d), standard tags, versioning on recon-ui bucket, JWT value alignment
- Post-apply plan: **No changes. 0-drift.**

## Commits

| Commit | Message |
|--------|---------|
| `20bed5b8` | feat(trade-pipeline): create TF module for trade subsystem (pre-import) |
| `320e4999` | infra(trade-pipeline): import 63 resources, 0-drift verified |

## Tag

`trade-pipeline-v1.0.0`

## Files

| File | Purpose |
|------|---------|
| infra/aws/terraform/trade-pipeline/main.tf | Provider + S3 backend |
| infra/aws/terraform/trade-pipeline/lambdas.tf | 11 Lambda functions |
| infra/aws/terraform/trade-pipeline/s3.tf | 5 S3 buckets |
| infra/aws/terraform/trade-pipeline/dynamodb.tf | 3 DynamoDB tables |
| infra/aws/terraform/trade-pipeline/iam.tf | 2 IAM roles + policies |
| infra/aws/terraform/trade-pipeline/variables.tf | jwt_secret variable |
| infra/aws/terraform/trade-pipeline/IMPORT_COMMANDS.sh | Import script (documentation) |
