# Session Summary -- 0.7.0_AE_CloudOps

**Date:** 2026-04-01
**Start:** ~14:46 UTC
**End:** ~18:07 UTC

---

## Task Orders Executed

| TO | Project | Description | Status | Tag |
|----|---------|-------------|--------|-----|
| ADVI_ANONYM.003 | ADVI_ANONYM | Secrets Manager key provisioning + IAM grant | COMPLETE | partners-api-v1.10.0 |
| ADHC_HISTRY.007 | ADHC_HISTRY | Schwab RPS file migration + converter + cleanup | COMPLETE | -- |
| ADVI_ANONYM.009 | ADVI_ANONYM | DynamoDB tier migration + MockADV + test accounts | COMPLETE | -- |

---

## ADVI_ANONYM.003 — Secrets Manager + IAM

**Detail log:** `advi_anonym_p1_secrets_provisioning.md`

- Queried opal-users-v2 for active firms: `opal-capital`, `49financial`
- Created `opal/pseudonym/opal-capital` and `opal/pseudonym/49financial` in Secrets Manager (32-byte random hex, us-east-1)
- Created `infra/aws/terraform/partners-api/iam.tf` — brought `partners-lambda-role` under Terraform management for the first time; added `PseudonymSecrets` SID (GetSecretValue + CreateSecret on `opal/pseudonym/*`)
- Imported 4 existing AWS resources into Terraform state, applied, confirmed 0-diff
- Both secrets verified retrievable via CLI
- Commit: `f81ce119` | Tag: `partners-api-v1.10.0` | Pushed

---

## ADHC_HISTRY.007 — Schwab RPS Migration

**Detail log:** `adhc_histry_schwab_migration.md`

- DS prerequisite 2c8a4470 confirmed on CLOUD
- Copied 22 March RPS files (1.5 GiB) from `opal-data-bd/uploads/schwab/` to `opal-data-schwab/bronze/rps/` with `--sse AES256`
- Uploaded converter `convert_schwab_rps_to_parquet.py` to `s3://opal-data-schwab/silver/scripts/` (DS .006 version reads bronze/rps/ first)
- Created SSM doc `opal-schwab-rps-convert`, ran on `bd-gold-layer-runner` (i-01003b035d2988dfb) — bd-allocations was stopped
- Converter result: 556 partitions already converted (2024-01-12 through 2026-03-31), all 22 March dates confirmed in silver/RPS/
- Deleted staging area `opal-data-bd/uploads/schwab/` — confirmed empty
- Launched background archive job: `opal-schwab-archive-01raw` SSM doc, CommandId `2015d13b`, copying `01_raw/` → `_archive/01_raw/` (~6214 files, 2h timeout)
- **Pending:** verify archive cmd `2015d13b` src==dst count before deleting `01_raw/`

---

## ADVI_ANONYM.009 — DynamoDB Migration + Test Accounts

**Detail log:** `advi_anonym_p3_dynamo_migration.md`

- Tier migration: 13 opal-capital users updated from tier=internal to tier=advisor (andrew@opalinvest.com skipped per constraint; FIRM META not a user)
- FIRM#mockadv created: s3Bucket=opal-data-bd, tier=advisor, domain=mockadv.test
- 3 test accounts created and verified:
  - `user@opalinvest.com` — advisor/user/opal-capital
  - `travis.penfield@49financial.com` — advisor/admin/49financial
  - `chase.bertrand@49financial.com` — advisor/user/49financial, advisorId="Chase Bertrand"
- Chase Bertrand advisorId confirmed against gold data: `s3://opal-data-bd/gold/advisors/Chase Bertrand/` folder exact match

---

## AWS Resources Created This Session

| Resource | Type | Notes |
|----------|------|-------|
| opal/pseudonym/opal-capital | Secrets Manager | 32-byte hex HMAC key |
| opal/pseudonym/49financial | Secrets Manager | 32-byte hex HMAC key |
| partners-lambda-role (Terraform import) | IAM Role | Now TF-managed |
| partners-lambda-permissions + PseudonymSecrets SID | IAM Inline Policy | Added GetSecretValue + CreateSecret |
| FIRM#mockadv | DynamoDB item | opal-users-v2 |
| USER#user@opalinvest.com | DynamoDB item | opal-users-v2 |
| USER#travis.penfield@49financial.com | DynamoDB item | opal-users-v2 |
| USER#chase.bertrand@49financial.com | DynamoDB item | opal-users-v2 |
| opal-schwab-rps-convert | SSM Document | v1 |
| opal-schwab-archive-01raw | SSM Document | v1 |

---

## Commits This Session

| Commit | Description |
|--------|-------------|
| f81ce119 | infra(ADVI_ANONYM P1): grant opal-partners-data access to pseudonym secrets |

---

## Current State

**Status:** All TOs COMPLETE. Archive job running in background.
**Active branch:** CLOUD
**Tag pushed:** partners-api-v1.10.0

---

## Next Steps

1. **Check archive job** — `aws ssm get-command-invocation --command-id 2015d13b-efa4-4afc-bfa4-72a350a59b2f --instance-id i-01003b035d2988dfb --query "StandardOutputContent" --output text` -- confirm src==dst before deleting `01_raw/`
2. **[DT 0.4.0_DT_ClientPlatform]** Deploy updated opal-partners-data Lambda when DS .002 and .007 signal complete (AE prereqs done)
3. **Deferred from 2026-03-30:** Terraform for opal-infrastructure-monitor
4. **Deferred from 2026-03-30:** SmartX supervisor deploy (S3+SSM rewrite)

**Do NOT delete `01_raw/`** until archive job `2015d13b` confirms src==dst count.
