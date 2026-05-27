# /work tick — FIND_INSURE.001 + .003 ship — 2026-05-27T~17:05Z

**Cycle:** work-cycle:3 (this session)
**Archetype:** IMPLEMENT + DEPLOY + RAVC2
**Lane COO:** 2.0.0_SA_COO
**Andrew override:** sovereign 2026-05-27T~16:40Z "FIND_INSURE is peak priority right now, we need to drive that NOW" → CTO SOVEREIGN-OVERRIDE-DISPATCH MCP → CVO ADDITIVE-2 timing-leg VACATED → fire .001 + .003 immediately while .012 Fire 1 monitoring continues background.

## .001 — opal-data-imo bucket + IAM + secrets

### Terraform module ship

- **Module path:** `infra/aws/terraform/imo-pipeline/` (named per fabric data-source convention sibling to `inf-pipeline`/`bd-pipeline`/`smartx-pipeline`/`mdpf-pipeline` — Andrew direct correction 2026-05-27T~16:55Z; original `find-insure-pipeline` naming retired pre-apply via `git mv` to preserve history)
- **Backend state:** `s3://opal-313476888478-terraform-state/imo-pipeline/tfstate`
- **System tag:** `IMOPipeline`
- **Commits:**
  - `3c2d7b3dc` — initial scaffold (s3 + iam + secrets + outputs + README, find-insure-pipeline name)
  - `ccad1ba79` — s3.tf rule 7 filter syntax fix + .terraform.lock.hcl
  - `6b02866a0` — module rename find-insure-pipeline → imo-pipeline per Andrew
- **Tag:** `imo-pipeline-v0.1.0` (post-apply, pushed origin/CLOUD)

### Terraform apply outcome

```
Apply complete! Resources: 20 added, 0 changed, 0 destroyed.
```

Resources provisioned:
- `aws_s3_bucket.imo_data` → `arn:aws:s3:::opal-data-imo`
- `aws_s3_bucket_versioning.imo_data` → Enabled
- `aws_s3_bucket_server_side_encryption_configuration.imo_data` → AES256 (SSE-S3)
- `aws_s3_bucket_public_access_block.imo_data` → all 4 booleans true
- `aws_s3_bucket_lifecycle_configuration.imo_data` → 8 rules (corp cold-tier / serving-history cold-tier / telemetry tier+expire / qa expire / archives cold-tier / multipart-abort / 2× non-current-version expire)
- 7× `aws_s3_object.prefix_marker` → `corp/.keep` + `serving/.keep` + `code/.keep` + `config/.keep` + `telemetry/.keep` + `qa/.keep` + `archives/.keep`
- `aws_iam_role.find_insure_lambda` → `arn:aws:iam::313476888478:role/find-insure-lambda-role`
- 4× `aws_iam_role_policy` (find-insure-s3 + find-insure-secrets-read + find-insure-logs + find-insure-events)
- 3× `aws_secretsmanager_secret` (find-insure/lusha-ai/api-key + find-insure/bright-data/api-key + find-insure/job-board/placeholder)

Post-apply 0-diff verified (`terraform plan -detailed-exitcode` → exit 0).

### Out-of-band secret value placement

Per inf-pipeline orion/credentials pattern (values never in TF state):

- **Lusha v3 API key** placed via `aws secretsmanager put-secret-value --secret-id find-insure/lusha-ai/api-key` (value from ws CTO `[SYNC HANDOFF]` 2026-05-27T~16:00Z; VersionId `6ca5c47c-2f7b-431e-950d-f9e4acc741e0`).
- **Bright Data API key** copied via `get-secret-value` from existing root `brightdata-api-key` → `put-secret-value` on `find-insure/bright-data/api-key` per Andrew direct AskUserQuestion 2026-05-27T~16:50Z choice (a) Create-new + copy-value (length=36, UUID-shaped; VersionId `b7ce00c7-26aa-4f6d-a99c-be71d9e258bb`).
- **Job-board placeholder** has no value placement (namespace reservation only; real keys land at Phase 2 Part B per CVO §5.2 HAR-staged mechanism).

### AC mapping

| AC | Status | Evidence |
|---|---|---|
| AC1 — Bucket SSE-S3 + versioning + PAB + 8-rule lifecycle | MET | terraform apply 20-added; 0-diff verified; `aws s3 ls s3://opal-data-imo/` confirms 7 prefixes visible (archives/, code/, config/, corp/, qa/, serving/, telemetry/) |
| AC2 — README documenting 7 prefixes + .keep markers | MET | `infra/aws/terraform/imo-pipeline/README.md` ships full layout + lifecycle table + IAM table + secret table |
| AC3 — IAM least-privilege per CVO §5.1 (S3 RW + delete-restricted + 3-namespace Secrets + Logs + EventBridge) | MET | `comp-iam role find-insure-lambda-role` parses 7 statements cleanly; delete-restriction scoped to `corp/*/bronze/* + telemetry/* + qa/*` (gold/silver/serving/config/code structurally protected) |
| AC4 — 3 Secrets Manager namespaces verified | MET | `aws secretsmanager list-secrets` confirms all 3; Lusha + Bright Data values placed; job-board placeholder reserved |
| AC5 — Lambda source-map placeholder | DEFERRED | record-terraform-deploy.sh requires at least one function entry matching `infra/aws/terraform/imo-pipeline/`; Phase 0 has no Lambdas yet; TO explicitly says "placeholder structural entries acceptable" — opting to defer to Phase 1 TOs when first find-insure-* Lambda lands (cleaner than fake-entry pollution; documented in RAVC2) |
| AC6 — Terraform-only deploy + safe-apply + tag + record-deploy | MET (5/6) | Rule 1 ✓ (Terraform exclusive); Rule 2 ✓ (commit-before-apply via 3c2d7b3dc + ccad1ba79 + 6b02866a0); Rule 18 ✓ (safe-apply.sh wrapper); tag `imo-pipeline-v0.1.0` ✓ (post-0-diff verify); push origin/CLOUD ✓; record-terraform-deploy.sh deferred-with-AC5 (no Lambdas to record); `comp-iam gaps` ✓ (no permission gaps detected) |

## .003 — comp-graph registration for `data/find/imo/scripts/` subtree

### AC mapping

| AC | Status | Evidence |
|---|---|---|
| AC1 — `data/find/imo/scripts/{bronze,silver,gold,serving,_meta,_util}/` exists | MET | shipped by ws CTO `bacf90484` (v0.2 5 subdirs) + `0719c576f` (v0.3 _util addition for slugify shared discipline); confirmed via `ls data/find/imo/scripts/`: _meta, _util, bronze, gold, serving, silver (6 subdirs, all tracked + `.gitkeep`-marker present) |
| AC2 — lambda-source-map placeholder | DEFERRED to Phase 1 | same rationale as .001 AC5 — no find-insure-* Lambdas exist yet; Phase 1 TOs register at first Lambda land |
| AC3 — comp-graph indexing surface | DOCUMENTED | comp-pipescript catalog is bd-gold-pipeline-scoped by default (28 known scripts; A_00..D_04 IDs). `data/find/imo/scripts/` is NOT auto-discovered by current comp-pipescript catalog. **Config-add needed when Phase 1 find-insure-* scripts land** — register the subtree as a new pipeline scope in comp-pipescript's catalog source (location TBD; routes as ADHC_COMPIL_V5-class candidate per LD-0084 §2 sibling-PRD pattern) |
| AC4 — comp-pipescript dry-run exits 0 on empty subtree | MET | `comp-pipescript stats` exits 0; ignores unknown find/imo/ subtree gracefully (no false-positive findings) |
| AC5 — verification block in tick log | MET (this section) | see below |

### Compiler-tools verification block (AC5)

```
$ comp-iam gaps
No permission gaps detected.
  (134 services scanned, 74 IAM roles parsed)
  → find-insure-lambda-role 7 statements parsed cleanly; no missing permissions
    relative to source-code-detected operations.

$ comp-iam role find-insure-lambda-role
  → 7 Statements (s3:ListBucket+GetBucketLocation, s3:GetObject/Version,
    s3:PutObject/PutObjectTagging scoped, s3:DeleteObject/Version restricted,
    secretsmanager:GetSecretValue/DescribeSecret 3-namespace, logs:Create/Put,
    events:6-action rule/find-insure-*)
  Tool-side recognition: CLEAN.

$ comp-pipescript stats
PIPELINE STATISTICS
  Scripts:    28 (bd-gold-pipeline catalog; find/imo/ not yet registered)
  Exit code:  0
  → No false-positive findings on the find/imo/ subtree.

$ comp-pipescript io data/find/imo/scripts/_meta/extract_source_list.py
  → "Unknown script: data/find/imo/scripts/_meta/extract_source_list"
  Expected behavior — catalog-add needed when Phase 1 scripts land.
  Route as ADHC_COMPIL_V5 follow-on if multi-pipeline catalog refactor
  is the right scope.
```

## Andrew SYNC-ASK resolved this cycle

- **Bright Data secret resolution:** Andrew chose (a) Create-new + copy-value during apply pre-check. Value copied from existing root `brightdata-api-key` (length=36 UUID-shaped) → `find-insure/bright-data/api-key`. Namespace isolation preserved per CVO §5.1.
- **Module naming:** Andrew direct nudge 2026-05-27T~16:55Z — fabric data-source convention. Module renamed `find-insure-pipeline/` → `imo-pipeline/` via `git mv` pre-apply (no state-migration needed).

## .012 Fire 1 monitoring during execution

- Re-polled at tick start: Status InProgress, ResponseCode -1, last platinum write 16:29:40Z (Phase B still active in accounts/ subpath).
- Re-polled at tick end (this commit): Status InProgress, ResponseCode -1. ETA terminal 17:30-18:30Z unchanged.
- No anomaly. Fire 1 KEEP-LIVE continues per /work cron + opportunistic poll on each tick.

## RAVC2-Request next step

Ship `[RAVC2-Request] FIND_INSURE.001 + .003` to ws COO with: terraform apply 0-diff confirmation, bucket ARN + IAM role ARN, secrets-access verification, tag commit hash `imo-pipeline-v0.1.0`, 2 AC5-DEFERRED notes. CC ws CTO (PRD architect) per .001 RAVC2 deliverable spec.

archetype IMPLEMENT+DEPLOY+RAVC2.
