# EC2 Deploy Transport Audit — 0.7.0_AE_CloudOps

**Date:** 2026-03-10
**Start Time:** 17:30
**End Time:** 17:45

## Objective

Audit all EC2 service deploy scripts to confirm transport mechanism (SSH/SCP vs SSM vs S3-pull)
following Andrew's confirmation that all port access has been removed from all VMs. Identify which
deploy scripts are non-functional and document the remediation path.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read session context + prior log | Full context established |
| 2 | Audit all EC2 deploy scripts in infra/aws/ec2/ | 5 scripts found |
| 3 | Check EC2_MANIFEST.json for all registered services | 9 services mapped |
| 4 | Classify each by transport mechanism | 2 SSH-based (broken), 1 S3-pull (correct), rest SSM/null |

---

## Work Completed

### 1. Deploy Script Inventory

Five deploy scripts exist under `infra/aws/ec2/`:
- `safe-ec2-deploy.sh` — wrapper/orchestrator (correct; no SSH)
- `smartx-exporter/deploy-to-ec2.sh` — SCP-based (broken)
- `smartx-exporter/build-and-deploy.sh` — not audited in detail (secondary script)
- `seeking_alpha_scraper/deploy_hybrid.sh` — SCP-based (broken)
- `bd-gold-layer-runner/deploy-to-ec2.sh` — S3 sync (correct)

### 2. Full Service Transport Matrix

| Service | Deploy Script | Transport | Port Required | Status |
|---------|--------------|-----------|---------------|--------|
| `smartx-exporter` | `smartx-exporter/deploy-to-ec2.sh` | SCP + SSH | 22 | **DEAD — port closed** |
| `seeking-alpha-scraper` | `seeking_alpha_scraper/deploy_hybrid.sh` | SCP + SSH | 22 | **DEAD — port closed** |
| `bd-gold-layer-runner` | `bd-gold-layer-runner/deploy-to-ec2.sh` | S3 sync (aws s3 cp) | None | Correct |
| `bd-allocations` | null (SSM: `opal-bd-allocation-download`) | SSM RunCommand | None | Correct |
| `bd-transactions` | null (SSM: `opal-bd-transaction-download`) | SSM RunCommand | None | Correct |
| `bd-price-runner` | null (SSM: same as allocations) | SSM RunCommand | None | Correct |
| `bd-exporter` | null | N/A | None | No deploy needed |
| `moltbot` | null | GitHub pull (agent) | None | No SCP deploy |
| `bd-gold-detail-generator` | null (ephemeral user-data.sh) | AMI bake | None | No persistent deploy |

### 3. Broken Script Details

**smartx-exporter/deploy-to-ec2.sh**
- Copies `run-all-portfolios.sh` to EC2 via `scp -i [key] [file] ubuntu@[IP]:[path]`
- Then runs SSH commands to set permissions
- Hardcodes no IP — script requires IP as `$1` argument
- EC2_MANIFEST.json `ec2_host: null` (no Elastic IP) — would fail at manifest-read stage first
- Service is currently running reliably without a recent code deploy; Andrew has confirmed do not
  touch SmartX unless actively needed.

**seeking_alpha_scraper/deploy_hybrid.sh**
- Copies `seeking_alpha_scraper_hybrid.py` via `scp -i ~/.ssh/seeking-alpha-scraper-key.pem`
- Hardcoded IP: `44.201.69.3`
- Runs SSH commands to activate venv and pip install openai
- Port 22 closed → entire script non-functional
- EC2_MANIFEST.json has `instance_id: null` for this service

### 4. Root Finding

`safe-ec2-deploy.sh` (the wrapper) is transport-agnostic — it only validates manifest registration,
checks branch, runs the service's deploy script, then records the deployment commit. The wrapper
itself has no SSH. All transport issues are in the service-specific deploy scripts.

The correct pattern (per EC2_CODE_DEPLOYMENT_STANDARD.md) is already implemented in
`bd-gold-layer-runner/deploy-to-ec2.sh`: upload to S3, EC2 syncs from S3 on boot or
on-demand. The broken scripts predate this standard.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Document only, no code changes | Andrew's directive for this session |
| SmartX deploy script: note only | Service is running reliably; Andrew has confirmed do not touch |
| Seeking alpha: note only | Same directive — document and defer |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| This log | Audit findings documented | No — local only |

---

## Blockers

None blocking this documentation. The two broken deploy scripts are an operational gap
but not actively breaking anything (both services are running, no deploy needed imminently).

---

## Current State

**Status:** COMPLETE (audit only; no code changes made)
**Active branch:** `CLOUD`

All EC2 services audited. Two deploy scripts (`smartx-exporter/deploy-to-ec2.sh` and
`seeking_alpha_scraper/deploy_hybrid.sh`) use SCP/SSH and are non-functional because port 22
is closed on all VMs. The correct S3-pull and SSM patterns are already in use for all
BD pipeline services. SmartX and Seeking Alpha are working at runtime; the broken deploy
scripts only matter if code changes need to be pushed to those instances. No code was changed
this session.

---

## Next Steps

1. **[0.7.0_AE_CloudOps] Rewrite smartx-exporter deploy script** — if/when a code change to
   `ai-supervisor-v2.py` or `run-all-portfolios.sh` needs to reach the EC2 instance, the deploy
   script must be rewritten to: upload source to `s3://opal-313476888478-lambda-artifacts/` (or
   a dedicated EC2 artifact bucket), then trigger EC2 to pull via SSM RunCommand
   (`aws ssm send-command --instance-ids i-06ebcb27395eb3f49`). Do not use SSH. Per
   EC2_CODE_DEPLOYMENT_STANDARD.md. **Do not do this preemptively** — only when a deploy
   is actually needed.

2. **[0.7.0_AE_CloudOps] Rewrite seeking-alpha deploy script** — same pattern: replace SCP with
   S3-upload + SSM pull. `seeking_alpha_scraper/deploy_hybrid.sh` also does a pip install over
   SSH which must become an on-instance bootstrap step (venv + requirements baked in, or pulled
   from S3 artifact). EC2_MANIFEST.json also needs `instance_id` populated (currently null).

3. **[0.7.0_AE_CloudOps] Create Terraform module for opal-infrastructure-monitor** — deferred
   from previous session. Code changes from commit `1f6bc00e` are in repo but Lambda in AWS
   still runs old version. Module must be created at `infra/aws/terraform/infrastructure-monitor/`
   (S3-backed, same pattern as other pipelines), artifact zip built with both
   `lambda_function.py` + `openai_cost_tracker.py`, then `terraform import` existing resources
   + deploy. Prerequisite for OPENAI COST section going live in morning report.

**Files to touch next (when actioned):**
- `infra/aws/ec2/smartx-exporter/deploy-to-ec2.sh` — rewrite to S3 + SSM
- `infra/aws/ec2/seeking_alpha_scraper/deploy_hybrid.sh` — rewrite to S3 + SSM
- `infra/aws/ec2/EC2_MANIFEST.json` — populate `instance_id` for seeking-alpha-scraper
- `infra/aws/terraform/infrastructure-monitor/` — new module to create (deferred)

**Do NOT:**
- Use `scp` or `ssh` in any deploy script (port 22 closed on all VMs)
- Run `aws lambda update-function-code` for infrastructure-monitor (CLAUDE.md rule 1)
- Touch SmartX EC2 instance proactively (service is working reliably)
