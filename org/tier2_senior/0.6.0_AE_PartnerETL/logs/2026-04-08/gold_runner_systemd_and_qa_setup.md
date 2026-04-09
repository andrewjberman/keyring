# Session Log: Gold Runner Systemd Fix + QA Runner + B_01b Deploy + Chain Fix

**Agent:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-08
**Tag:** bd-v2.21.5, bd-v2.21.6

---

## Summary

Fixed the bd-gold-layer-runner EC2 so it actually auto-runs on boot via systemd (was never enabled). Added S3-based mode passing from Lambda to EC2. Set up bd-gold-qa-runner as a production-sized duplicate with no auto-start/shutdown. Deployed B_01b auto-classification (DS script) with IAM fix for OpenAI Secrets Manager access. Fixed CHAIN_FULL to include Group A in nightly incremental runs.

---

## 1. Gold Runner Systemd Fix (bd-v2.21.5)

### Problem
Andrew asked to verify the runner was configured for systemd auto-start on boot with shutdown at completion. Audit found four gaps:

| # | Issue | Severity |
|---|-------|----------|
| 1 | `systemctl enable gold-layer-runner` never called in setup-instance.sh | CRITICAL -- runner never auto-started on boot |
| 2 | Inline runner in setup-instance.sh referenced `run_all.sh` (stale) | HIGH -- first boot would fail |
| 3 | user-data.sh referenced `git clone` and `run_all.sh` (completely stale) | MEDIUM -- only matters for new instances |
| 4 | Lambda had no mechanism to pass mode (incremental/full) to EC2 | MEDIUM -- monthly full rebuild didn't work |

### Fixes

**setup-instance.sh:**
- Replaced stale inline runner with thin S3 bootstrap (pulls real runner, execs it)
- Added `systemctl enable gold-layer-runner` after daemon-reload

**run-gold-layer.sh:**
- Added S3 trigger-mode.json detection: CLI arg > S3 marker > default incremental
- Runner reads marker, deletes it, runs in requested mode

**bd-gold-trigger Lambda:**
- Writes `gold/trigger-mode.json` to S3 before `start_instances()`
- Monthly EventBridge passes `mode: "full"`, nightly fallback defaults to `incremental`

**user-data.sh:**
- Replaced git-clone bootstrap with S3-based setup (pulls setup-instance.sh from S3)

### Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | py_compile gate | PASS |
| 2 | Manual zip + S3 upload (Lambda) | SHA: `8BZxE/Hg+Eh0BrLOKinLTxrlWinj9a9+jgD85F1UnoU=` |
| 3 | S3 upload (EC2 scripts) | run-gold-layer.sh, setup-instance.sh, watchdog-shutdown.sh |
| 4 | Source map update | SHA updated for bd-gold-trigger |
| 5 | terraform plan | 1 to change (Lambda code hash) |
| 6 | terraform apply | 0 added, 1 changed, 0 destroyed |
| 7 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 8 | Start EC2 (i-01003b035d2988dfb) | SSM: `systemctl enable gold-layer-runner` -> enabled |
| 9 | SSM: pull updated scripts from S3 | run-gold-layer.sh + watchdog confirmed on instance |
| 10 | Stop EC2 | stopped |
| 11 | record-deploy + tag + push | `bd-v2.21.5` |

### Note on build-and-upload.sh
`node` is not installed on this machine. `bun` cannot resolve MSYS2 temp paths for the JS helper scripts in build-and-upload.sh. Had to build the Lambda zip manually (PowerShell Compress-Archive + aws s3 cp with --metadata). The python3 fallback in build-and-upload.sh exists but the script finds bun first and fails. Future fix: either install node or make the script prefer python3 when bun fails.

---

## 2. QA Runner Setup

### bd-gold-qa-runner (i-0090b823a4a0997e3)

Created as a production duplicate with two differences:
- **No systemd auto-start** -- manual SSM dispatch only
- **GOLD_KEEP_ALIVE=1** -- no auto-shutdown, stays alive for debugging

Initially launched as c6i.2xlarge, resized to **c6i.16xlarge** (same as production) because large partition loads timed out on the smaller instance.

### Files Created
- `infra/aws/ec2/bd-gold-qa-runner/setup-instance.sh` -- same deps, systemd NOT enabled, GOLD_KEEP_ALIVE=1 in service unit
- `infra/aws/ec2/bd-gold-qa-runner/user-data.sh` -- bootstrap from `s3://opal-data-bd/code/runner-qa/`
- `infra/aws/ec2/bd-gold-qa-runner/launch-instance.sh` -- updated with correct instance type and user-data

### Live Instance Provisioned
- SSM: setup-instance.sh ran (deps installed, systemd unit created but not enabled)
- SSM: runner + watchdog scripts pulled from S3
- EC2_MANIFEST.json updated
- Instance stopped after setup

---

## 3. B_01b Auto-Classification Deploy (bd-v2.21.6)

### Context
DS (0.4.0) asked where to wire automatic security classification. 28 misclassified structured products in bd-securities DynamoDB were root cause of Assets Overview vs Books alternatives divergence.

### Design (coordinated with DS via MCP)
- **Hook point:** After B_01 (holdings_lots), before C_00
- **Dedup:** Ticker-first PK via existing `normalize_key()`, no CUSIP available
- **Watermark:** Simple `classify_watermark.json` with last scanned holdings_lots date
- **Script:** DS committed `B_01b.classify_new_securities.py` at `e71fe8fe`

### IAM Fix
`bd-exporter-ec2-role` was missing `openai-api-key-*` in secretsmanager:GetSecretValue allowed list. The classifier reads from Secrets Manager, not env var. Added the ARN pattern to `iam.tf`.

### Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | py_compile B_01b | PASS |
| 2 | IAM policy update (iam.tf) | Added `openai-api-key-*` |
| 3 | Commit | `94a243e6` |
| 4 | terraform plan | 1 to change (IAM policy) |
| 5 | terraform apply | 0 added, 1 changed, 0 destroyed |
| 6 | 0-diff plan | No changes |
| 7 | Upload B_01b.py + gold_dispatch.sh to S3 | code/gold/ |
| 8 | record-deploy + tag + push | `bd-v2.21.6` |

---

## 4. CHAIN_FULL Fix -- Group A in Nightly Incremental

### Problem
`CHAIN_FULL` was defined as `CHAIN_CANONICAL + CHAIN_DOWNSTREAM` (B through D only). Group A (advisor assignments, fee rate history, positions cube, client dimension) only ran in `rebuild` mode (monthly). New clients, advisor changes, and fee updates were invisible for up to 30 days.

### Fix
Changed `CHAIN_FULL` to `CHAIN_FOUNDATION + CHAIN_CANONICAL + CHAIN_DOWNSTREAM` (A through D). `CHAIN_REBUILD` is now an alias for `CHAIN_FULL`. The `--incremental` flag still applies per-script (watermark-gated), so Group A won't redundantly reprocess unchanged data.

Commit `b3409d25`, uploaded to S3, pushed.

---

## Infrastructure State

| Instance | ID | Type | State |
|----------|-----|------|-------|
| bd-gold-layer-runner | i-01003b035d2988dfb | c6i.16xlarge | STOPPED |
| bd-gold-qa-runner | i-0090b823a4a0997e3 | c6i.16xlarge | STOPPED |

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| BD | bd-v2.21.5 | c3f901ea |
| BD | bd-v2.21.6 | 609a1e63 |

---

## Next Steps

- [AE] Tonight's nightly trigger will be the first full A-D incremental with B_01b classification. Monitor logs at `s3://opal-data-bd/logs/gold-layer/`.
- [AE] Verify B_01b watermark file created after first run: `gold/manifests/classify_watermark.json`
- [AE] If build-and-upload.sh is needed again: either install node or add python3 priority over bun in the script
- [DS] 31 misclassified DynamoDB entries already fixed manually by DS. Next gold run will reflect correct classifications.
- [AE] STAGED task orders (ADVI_GLDRST.010, .014, ADVI_REBORN.W1-003) still awaiting GO from COO.
