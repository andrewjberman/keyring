# 0.6.2_AE_PartnerETL — work_1415Z — 2026-06-09

## Session summary

**Tick type:** SUBSTANTIVE — ADVI_COTETL silver infra (Track B phase 1)

## Inbox

- **COO DRIVE dispatch received** (Andrew-direct): ADVI_COTETL silver — two tracks
  - Track A: monitor bronze run tonight 02:00Z/02:30Z
  - Track B: silver infra (SSM doc + S3 deploy + first silver run)

## Work executed — Track B Phase 1: opal-cot-silver-run SSM doc

**File edited:** `infra/aws/terraform/cot-pipeline/ssm.tf`
- Added `aws_ssm_document.cot_silver_run` (opal-cot-silver-run)
- Parameters: RunDate, DryRun
- Downloads `s3://opal-data-cot/code/silver/cot_silver_merge.py`
- Runs transactions then allocations sequentially with BD_S3_BUCKET=opal-data-cot, BD_FIRM_ID=cottonwood
- Logs to `opal-data-cot/logs/cot-exporter/silver-run/`

**Commit:** `d73de487b` — `feat(ADVI_COTETL): add opal-cot-silver-run SSM doc (silver merge, manual trigger v1)`

**Terraform apply:** 1 added, 0 changed, 0 destroyed
**0-diff verify:** PASS

**Tag:** `cot-pipeline-v0.3.1`
**Push:** CLOUD 50aff9f28..d73de487b + tag

## Pending — Track B Phase 2

Blocked on DS RAVC2 (0.4.0_DS committing `data/cot/scripts/silver/cot_silver_merge.py`):
- `aws s3 cp data/cot/scripts/silver/cot_silver_merge.py s3://opal-data-cot/code/silver/cot_silver_merge.py`

## Pending — Track B Phase 3

After bronze PASS tonight + DS script deployed:
- Manual trigger: `aws ssm send-command --document-name opal-cot-silver-run --instance-ids i-0643a5bee8a8feabf ...`
- Verify: silver/transactions/ + silver/allocations/ LastModified + row counts

## IAM note (banked for future)

Lambda `cot-bd-session-trigger` SendCommand policy (iam.tf:67-77) currently only covers
`opal-cot-bd-session-fetch`. When silver is wired to EventBridge (post-v1 validation),
`opal-cot-silver-run` ARN must be added to `SendSessionFetchCommand` Sid resource list.
Not blocking v1 (manual trigger only).
