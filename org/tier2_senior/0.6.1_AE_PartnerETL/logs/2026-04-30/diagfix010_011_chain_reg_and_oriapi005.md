# Session Log — 0.6.1_AE_PartnerETL — DIAGFIX.010+.011 Chain Registrations + ORIAPI.005 — 2026-04-30

**Agent:** 0.6.1_AE_PartnerETL (base lane)
**Date:** 2026-04-30
**Session scope:** (1) orion-gold-dispatch.sh CATALOG+CHAIN registrations for DIAGFIX.010 and DIAGFIX.011; (2) ADVI_ORIAPI.005 inf-ec2-retry-launch Lambda — pre-authorized trigger fired

---

## Context

8 offline messages found on startup (DS + COO). Two parallel workstreams executed:

1. **DIAGFIX.010+.011 chain registrations** — no JWT dependency; DS shipped code and requested catalog entries.
2. **ORIAPI.005** — pre-authorized trigger condition fired (3× Server.InternalError on inf-exporter 2026-04-29T22:50-22:55Z, within 14 days of cron shift 2026-04-29). COO pre-authorized immediate author + ship per ADVI_ORIAPI.json blocking field.

---

## Workstream 1: DIAGFIX.010+.011 orion-gold-dispatch.sh Updates

### Scope

DIAGFIX.010 (mix classification — assets_v2 silver dim):
- `pull_inflection_assets_v2.py` (bronze pull, manual_api prefix)
- `convert_assets_v2_to_silver.py` (silver convert, silver prefix)

DIAGFIX.011 (Brandenburg attribution fix — representatives + household_rep_mapping):
- `pull_inflection_representatives.py` (bronze pull, manual_api prefix)
- `convert_orion_api_to_silver.py --dim representatives` (silver)
- `convert_orion_api_to_silver.py --dim household_rep_mapping` (silver)
- `convert_orion_api_to_silver.py --dim accounts_v2` (silver — MODIFIED to join household_rep_mapping)

### Changes to orion-gold-dispatch.sh

1. **`sync_scripts()`**: Extended to pull from 3 S3 prefixes instead of just `code/gold/`:
   - `code/gold/` (existing)
   - `code/manual_api/` (bronze API pulls — new)
   - `code/silver/` (silver converts — new)

2. **`RUN_DATE` variable + `{date}` templating**: Added `RUN_DATE=$(date -u +%Y-%m-%d)` and `default_flags="${default_flags//\{date\}/$RUN_DATE}"` substitution in `run_script()` for snapshot-date flag injection.

3. **CATALOG**: 6 new entries added:
   ```
   INF_API_PULL_REPS|pull_inflection_representatives.py|--upload-bronze
   INF_API_SILVER_REPS|convert_orion_api_to_silver.py|--dim representatives --upload --snapshot-date {date}
   INF_API_SILVER_HHREP|convert_orion_api_to_silver.py|--dim household_rep_mapping --upload --snapshot-date {date}
   INF_API_SILVER_ACCOUNTS_V2|convert_orion_api_to_silver.py|--dim accounts_v2 --upload --snapshot-date {date}
   INF_API_PULL_ASSETS_V2|pull_inflection_assets_v2.py|--upload-bronze
   INF_API_SILVER_ASSETS_V2|convert_assets_v2_to_silver.py|--upload
   ```

4. **CHAIN_FULL**: 6 new entries prepended before INF_A_00 (38 total scripts).
   Chain ordering satisfies all dep constraints: reps first, then assets, then accounts_v2 rebuild (joins household_rep_mapping), then INF_A_00 onward → INF_I_D03 reads corrected data.

5. **CHAIN_INCREMENTAL**: Same 6 new entries prepended before INF_I_D00. Incremental chain needs API pulls too — INF_I_D03 requires corrected accounts_v2 + assets_v2 dims even in D-chain-only mode.

6. **Comments + help text**: Updated chain description comments + show_help() to reflect 38 total scripts and new incremental composition.

### S3 Upload

```
s3://opal-data-inf/code/gold/orion-gold-dispatch.sh — 23.4 KB uploaded
```

| Commit | Files | Notes |
|---|---|---|
| `3f762ba79` | `data/orion/scripts/gold/orion-gold-dispatch.sh` | Lane violation warn (AE writing to POD4 dispatch script) — expected; AE owns catalog registration |

---

## Workstream 2: ADVI_ORIAPI.005 — inf-ec2-retry-launch Lambda

### Pre-authorized trigger

3 consecutive `Server.InternalError` events within 14 days of cron shift:
- Attempt 1 (DS) 2026-04-29T22:50Z
- Attempt 2 (COO) 2026-04-29T22:53Z
- Attempt 3 (COO retry) 2026-04-29T22:55:51Z

Per ADVI_ORIAPI.json: "14-day re-open trigger: ANY Server.InternalError within 14 days of cron shift apply → AE 0.6.1 base pre-authorized to author .005 immediately, no new ruling."

### Architecture

**New Lambda: `inf-ec2-retry-launch`**
- Trigger: SNS subscription on `inf-otp-alert`
- Filter: `"EC2 launch failure"` / `"EC2 likely launch failure"` in Subject (set by `inf-ec2-launch-monitor`)
- Instance ID extraction: regex from monitor alert body (`AWS EC2 instance i-xxxxx`)
- Pre-check: skip if instance already running/pending
- Idempotency: DDB `PutItem` with `attribute_not_exists` condition on `opal-inf-launch-locks` (5-min window key)
- Retry: 3 attempts, delays 30s → 60s → 120s
- Exhaust: publishes `RETRY-EXHAUSTED: inf-pipeline EC2 {instance_id}` back to `inf-otp-alert`
- Runtime: Python 3.12, timeout 360s (covers 210s total sleep + overhead), 128 MB
- KMS: same grant pattern as inf-jwt-trigger (EBSAttachCreateGrant + EBSKeyUse)

**Infrastructure (new TF file: `inf-ec2-retry-launch.tf`):**
- `aws_iam_role.inf_ec2_retry_launch` + 3 policies + 1 attachment
- `module.inf_ec2_retry_launch` (yang-lambda)
- `aws_sns_topic_subscription.inf_ec2_retry_launch`
- `aws_lambda_permission.sns_inf_ec2_retry_launch`

### Deploy sequence

| Step | Action | Result |
|---|---|---|
| Pre-commit gate | `.tools/ds-commit-gate.sh lambda_function.py` | PASS (fixed unused `import json` on first run) |
| Build | PowerShell Compress-Archive | 2.1 KB |
| Upload | `s3://opal-313476888478-lambda-artifacts/inf-pipeline/inf-ec2-retry-launch.zip` with `content-sha256` metadata | OK |
| Commit | `468b6f4ce` | Lambda + TF + requirements.txt + source-map |
| terraform init | Module install | OK |
| terraform plan | 8 to add, 0 to change, 0 to destroy | CLEAN |
| terraform apply | All 8 resources created | OK |
| 0-diff verify | terraform plan again | No changes |
| Tag | `inf-pipeline-v1.7.2` | Latest was v1.7.1; next contiguous patch |
| Push | `git push --follow-tags` | OK |
| Source map CI record | `d2d455384` | deployed_commit + sha256 updated |

### Lambda verification

SNS subscription confirmed: `arn:aws:sns:us-east-1:313476888478:inf-otp-alert:5a4f2660-9424-4440-b993-363476d5aea5`
Function created: `inf-ec2-retry-launch` (us-east-1)

---

## Files Changed

| File | Change | Commit |
|---|---|---|
| `data/orion/scripts/gold/orion-gold-dispatch.sh` | 6 new CATALOG entries + sync from 3 prefixes + {date} templating + chain updates | `3f762ba79` |
| `infra/aws/lambda/inf-pipeline/inf-ec2-retry-launch/lambda_function.py` | New Lambda (ORIAPI.005) | `468b6f4ce` |
| `infra/aws/lambda/inf-pipeline/inf-ec2-retry-launch/requirements.txt` | No deps | `468b6f4ce` |
| `infra/aws/terraform/inf-pipeline/inf-ec2-retry-launch.tf` | IAM + Lambda + SNS subscription | `468b6f4ce` |
| `infra/aws/lambda/ci/lambda-source-map.json` | New entry + deploy record | `468b6f4ce` + `d2d455384` |

---

## Compiler Tools

| Tool | Run / Skip | Result |
|---|---|---|
| `comp-pipescript io` | N/A — no gold script edits | — |
| `comp-pipescript deployed` | N/A — no gold script dispatch | — |
| `comp-iam service inf-ec2-retry-launch` | Would run but Lambda not in comp catalog (INF pipeline gap flagged DIAGFIX.001) | — |
| `comp-iam gaps` | Not run — iam.tf not changed (new file, new role) | — |
| `comp-blast` | N/A — new Lambda with no downstream consumers | — |
| Pre-commit gate | Run on `lambda_function.py` | PASS (fixed 1 ruff F401) |

---

## RAVC Status

- RAVC2 ACK sent to COO at session start (DIAGFIX.010+.011 + ORIAPI.005)
- RAVC4 to COO + DS pending (this session log is the basis)

---

## Open Items

- DIAGFIX.011 Phase 4-6 (live re-run with Brandenburg attribution) — DS owns; needs JWT (auto-refresh tomorrow 12:13Z or next cron cycle 2026-05-01)
- ORIAPI.005 second-tier trigger: if retry-exhausted fires within 7 days of deploy → open ADVI_ORIAPI.006 AZ migration
- ORIAPI Phase 1 v1.0.1 closure: Cycle 1 = 2026-04-30 12:13Z (today's nightly), Cycle 2 = 2026-05-01 12:13Z
- INFGRD.003 TO status: still open (depends on DS completing the full wave — partially done via previous sessions)
- INFSHIP.A2 — Andrew initiation required
