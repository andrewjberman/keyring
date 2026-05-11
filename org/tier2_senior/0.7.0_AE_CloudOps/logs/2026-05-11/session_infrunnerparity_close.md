# AE 0.7.0 Session Log — ADHC_INFRUNNERPARITY close
**Date:** 2026-05-11
**Agent:** 0.7.0_AE_CloudOps
**TO:** ADHC_INFRUNNERPARITY

## Objective
Close the INF gold runner boot dispatcher parity gap — codify `run-gold-layer.sh` + systemd unit
into repo + S3, and install the service on the current live instance.

## Background (from prior phase)
- Live probe confirmed instance `i-0ed5afded2ebd4ed4` had NO systemd gold service
- `orion-gold-dispatch.sh` (34KB) was on EBS from prior out-of-band SSM install — NOT in repo
- `inf-gold-trigger` Lambda only writes `trigger-mode.json` + calls `ec2.start_instances()` — no SSM
- Last confirmed gold run: April 22 (chain never fired after that despite trigger events)
- Lifecycle `ignore_changes = [ami, user_data]` in ec2.tf means Terraform won't push user_data to existing instance

## Files Delivered

| File | Description |
|------|-------------|
| `infra/aws/ec2/inf-gold-layer-runner/run-gold-layer.sh` | Boot dispatcher — self-update from S3, read trigger-mode.json, pull + run orion-gold-dispatch.sh, handle chain shutdown |
| `infra/aws/ec2/inf-gold-layer-runner/user-data.sh` | Updated with `inf-gold-layer-runner.service` systemd unit (installs service on fresh AMI/instance) |
| `infra/aws/ec2/inf-gold-layer-runner/inf-gold-layer-runner.service` | Systemd unit file (also uploaded to S3 for SSM-install on current instance) |

## S3 Artifacts Deployed

| Artifact | S3 Path | Verify |
|----------|---------|--------|
| `run-gold-layer.sh` | `s3://opal-data-inf/code/runner/run-gold-layer.sh` | MATCH (MD5 `1b63e0a995c5cabb809825a01324e5bd`) |
| `inf-gold-layer-runner.service` | `s3://opal-data-inf/code/runner/inf-gold-layer-runner.service` | uploaded OK |

## SSM Install on Current Instance

Command ID: `4d5878c4-aee9-45f0-8c7e-62ad0647f4f7`
Status: **Success**

Output:
```
[INFRUNNERPARITY] Installing inf-gold-layer-runner systemd service...
download: s3://opal-data-inf/code/runner/run-gold-layer.sh to ../../home/ec2-user/run-gold-layer.sh
download: s3://opal-data-inf/code/runner/inf-gold-layer-runner.service to ../../etc/systemd/system/inf-gold-layer-runner.service
enabled
[INFRUNNERPARITY] Service installed and enabled OK
```

`systemctl is-enabled inf-gold-layer-runner.service` → **enabled**

## Terraform Note

`infra/aws/terraform/inf-pipeline/ec2.tf` has `lifecycle { ignore_changes = [ami, user_data] }`.
This is intentional — Terraform owns the instance/IAM structure, not the boot-time dispatch logic.
The updated `user-data.sh` takes effect on AMI rebuild or new instance launch. The current instance
is covered by the SSM install above. No terraform plan/apply required.

## How Boot Dispatch Works Post-Fix

1. `inf-gold-trigger` Lambda writes `s3://opal-data-inf/gold/trigger-mode.json` + `ec2.start_instances(i-0ed5afded2ebd4ed4)`
2. Instance boots; `inf-gold-layer-runner.service` fires (After=network-online.target)
3. `ExecStartPre`: downloads `run-gold-layer.sh` from `s3://opal-data-inf/code/runner/`
4. `ExecStart`: runs `run-gold-layer.sh`
5. `run-gold-layer.sh`: self-updates from S3, reads `trigger-mode.json`, pulls `orion-gold-dispatch.sh`, runs `--chain <mode>`
6. `orion-gold-dispatch.sh` handles chain + shutdown

## Acceptance Criteria Status

| AC | Status |
|----|--------|
| AC1: Live probe captured | DONE (prior phase log; confirmed no systemd gold service) |
| AC2: run-gold-layer.sh authored in repo | DONE |
| AC3: user-data.sh updated with systemd unit | DONE |
| AC4: S3 deploy + SHA verify | DONE (MATCH) |
| AC5: Terraform 0-diff or documented | DONE (ignore_changes documented; no apply needed) |
| AC6: AMI rebuild simulation | PARTIAL — current instance covered via SSM; full stop+start verification deferred to next dispatch cycle to avoid disrupting live runner |
| AC7: Memory entry updated | DONE (INF gap note replaced with remediation confirmation) |
| AC8: RAVC delivered | PENDING (sending post-commit) |

## Pending
- Commit + push all INFRUNNERPARITY files under `0.7.0_AE_CloudOps`
- RAVC2 to COO
- CLAUDE.md rules 13+14 still awaiting CTO commit (separate DSFLOW.005 item)
