# 0.7.0_AE_CloudOps Session Log — 2026-06-09

## Session scope
NFRA_GLOBGRPH Wave-1 deployment (continued from context-compacted prior session).

## Work completed

### Pre-work: bd_versions lifecycle drift fix (completed prior session, logged here for completeness)
- Removed stale `aws_s3_bucket_lifecycle_configuration.bd_versions` from shared-infra/main.tf
- Committed `46e2be09f` — prevents shared-infra from overwriting bd-bucket-lifecycle Option B (Time Machine-safe)

### Wave-1 TF module build (completed prior session)
All 5 globgrph TF files written:
- `infra/aws/terraform/globgrph/main.tf` — backend, locals (VPC, S3, Nessie URI)
- `infra/aws/terraform/globgrph/nessie.tf` — ECS cluster, Fargate task def (ghcr.io/projectnessie/nessie:0.96.1), service, Cloud Map private DNS (nessie.opal-globgrph.local:19120), SG
- `infra/aws/terraform/globgrph/iam.tf` — nessie_task role (DynamoDB CRUD + S3), nessie_execution role, globgrph_incremental_updater role (CW Logs + SQS + S3 + 14-action describe + VPCAccess)
- `infra/aws/terraform/globgrph/vpc_endpoints.tf` — S3 gateway, DynamoDB gateway (free), CW Logs interface (~$7/mo)
- `infra/aws/terraform/globgrph/item2b.tf` — CW log group, SQS queue + DLQ, EB rule (14 services CloudTrail mgmt events), Lambda (Python 3.12, 512MB, 3min, in-VPC), ESM (batch=100, window=120s), pyiceberg-nessie layer

### Lambda source files
- `infra/aws/lambda/globgrph/incremental_updater/lambda_function.py` — bounded derive + pyiceberg upsert + Nessie ONE-commit-per-batch
- `infra/aws/lambda/layers/pyiceberg-nessie-deps/requirements.txt` — pyiceberg 0.8.1 + pyarrow + pydantic + tenacity

### comp_aws_cli.py extensions
- Added `_arn_to_cls(arn)` helper + `--resource <arn>` bounded-derive mode in `cmd_derive()`
- Added `cmd_iceberg_commit()` function + `iceberg-commit` subcommand in `main()`
- Pre-commit gate: PASS (ds-commit-gate.sh, 2 files)

### lambda-source-map.json
- Added `opal-globgrph-incremental-updater` entry (172 total functions)

### Artifact builds + S3 uploads
- Layer: `pip install -t python/ -r requirements.txt` → 56 MB ZIP → `s3://opal-313476888478-lambda-layers/pyiceberg-nessie-deps.zip`
- Lambda: `incremental_updater.zip` (3.9 KB) → `s3://opal-313476888478-lambda-artifacts/globgrph/incremental_updater.zip`

### Terraform deploy
- `terraform init` — OK, hashicorp/aws v5.100.0, backend s3 globgrph/tfstate
- `terraform plan` — 33 to add, 0 to change, 0 to destroy
- `safe-apply.sh` — HALTGT PASS (inbox empty), apply completed
- 0-diff verify — `No changes. Your infrastructure matches the configuration.`
- Tag: `globgrph-v0.1.0`
- Push: `4d83c65f7` HEAD on CLOUD

### Resources deployed (33 total)
Item-1 (Nessie-on-Fargate): ECS cluster, capacity providers, log group, task def, service, Cloud Map namespace + service, SG for Nessie
Item-2b (Lambda incremental): CW log group, SQS queue + DLQ + policy, EB rule + target, Lambda function + ESM, Lambda SG, pyiceberg layer
VPC endpoints: S3 gateway, DynamoDB gateway, CW Logs interface + SG
IAM: nessie_task role + 2 policies, nessie_execution role + attachment, globgrph_incremental_updater role + 4 policies + VPC attachment

## Status
Wave-1 DEPLOYED. 0-diff confirmed. Tag + push complete.

PENDING (Wave-2 / LD-0168 close):
- Item-2a: nightly Fargate derive-runner (runs full comp-aws derive → iceberg-commit)
- Verify Nessie health: `curl http://nessie.opal-globgrph.local:19120/q/health/ready` (from VPC)
- First Iceberg commit via `comp-aws iceberg-commit` → verify graph_nodes/graph_edges in Nessie
- AC7 (LD-0168 close): versioning + Cypher query working on real unioned graph data
