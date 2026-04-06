# EC2 Auto-Shutdown Audit — All Instances

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-02
**TO:** ec2-auto-shutdown-audit-all-instances
**Status:** COMPLETE

---

## Audit Summary

| # | Instance | Lifecycle | Run Scripts | Shutdown Mechanism | Systemd Timers | Gap? |
|---|----------|-----------|-------------|--------------------|----------------|------|
| 1 | **moltbot** | Persistent (always-on) | Claude Code AI agent, setup-github.sh | None -- explicitly banned in CLAUDE.md and settings.json | None | No -- always-on by design |
| 2 | **smartx-exporter** | Ephemeral (daily job) | `run-all-portfolios.sh` via SSM from `smartx-ec2-autostart` Lambda (EventBridge weekdays ~5 PM ET) | `sudo shutdown -h now` at end of `run-all-portfolios.sh` (line 279). IAM `self-shutdown` policy grants `ec2:StopInstances`. | None | No |
| 3 | **seeking-alpha-scraper** | Persistent (always-on) | `run_scraper.sh` via cron daily 7 AM ET | None -- instance stays running permanently. Cron runs scraper, scraper exits, instance stays up. | None | **YES** -- instance runs 24/7 for a job that takes minutes. ~$50-70/month wasted (t3.medium). |
| 4 | **bd-gold-layer-runner** | Ephemeral (per-job) | `run_gold_layer.sh` via systemd on boot; `ssm-run-gold.sh` for manual SSM runs. Triggered by `bd-gold-trigger` Lambda (S3 event / EventBridge). | `shutdown -h now` in `run_gold_layer.sh` + **watchdog-shutdown.timer** (GLDRST.015, every 5 min). | `watchdog-shutdown.timer` (5 min interval, checks for idle+uptime>30m+no keep-alive) | No -- baseline reference, dual shutdown (script + watchdog) |
| 5 | **bd-exporter** | Persistent (always-on) | `merge-daily-incremental.py` (silver merge). No SSM trigger in Terraform -- appears to be manually run or cron. | None in scripts or user-data. | None | **YES** -- instance stays running. No automated shutdown. If it's truly always-on, billing is continuous (~$30-50/month for t3.medium). |
| 6 | **bd-allocations** | Ephemeral (daily job) | 3 SSM docs run on same instance in sequence (21:25-21:48 UTC weekdays): `opal-bd-unrealized-download`, `opal-bd-realized-download`, `opal-bd-allocation-download`. Each started by its own Lambda trigger. | `shutdown -h +2` at end of each SSM doc. Unrealized/realized cancel pending shutdowns (`shutdown -c`) before starting, then schedule their own `+2`. Last doc (allocation, 21:48) schedules final shutdown. | None | No -- cascading shutdown with cancel/reschedule pattern works correctly |
| 7 | **bd-transactions** | Ephemeral (daily job) | `opal-bd-transaction-download` SSM doc at 21:40 UTC weekdays, started by `bd-transactions-trigger` Lambda. | `shutdown -h +2` at end of SSM doc. | None | No |
| 8 | **bd-price-runner** | N/A (shares bd-allocations instance) | `bd_price_update.py` invoked at end of `opal-bd-allocation-download` SSM sequence. | Covered by bd-allocations shutdown (`shutdown -h +2` after allocation download completes, which is after price update). | None | No |
| 9 | **bd-gold-detail-generator** | Ephemeral (per-job) | `user-data.sh` baked at launch (scripts 07, 09, 10, 11). Started by Step Functions. | `shutdown -h now` at end of `user-data.sh` (line 101), with 60s grace period. Terraform: `instance_initiated_shutdown_behavior = "stop"`. | None | No |

---

## Gaps Identified

### Gap 1: seeking-alpha-scraper -- no shutdown (MITIGATED: instances are stopped)

- **Instance:** `seeking-alpha-scraper` (2x t3.medium: i-07ebae29a16e43ed1, i-06376c11d8b3c3443)
- **Current state:** Both STOPPED since 2026-02-17. No active billing.
- **Problem (latent):** No shutdown mechanism in scripts. If restarted, instance would run indefinitely.
- **Estimated waste:** $0/month currently. Risk only if instances are restarted without adding shutdown.
- **Remediation options (if reactivated):**
  - A) Add `shutdown -h now` at end of cron job, convert to Lambda-triggered start (like smartx)
  - B) Add a watchdog timer (like GLDRST.015 pattern)
  - C) EventBridge stop-instance rule N minutes after expected cron completion

### Gap 2: bd-exporter -- no shutdown, unclear if truly persistent

- **Instance:** `bd-exporter` (instance_id not in manifest, appears legacy)
- **Problem:** No shutdown mechanism in any script. User-data scripts (`beast_user_data.sh`, `uploader_user_data.sh`) are setup-only, no auto-stop. No SSM trigger in Terraform -- `run-daily-downloads.sh` references cron but no shutdown after completion.
- **Estimated waste:** If running 24/7: ~$30-50/month (t3.medium). May already be stopped -- no instance_id in EC2_MANIFEST suggests it could be decommissioned/unused.
- **Remediation options:**
  - A) Confirm if this instance is actually running (check AWS console)
  - B) If active: add watchdog timer or post-job shutdown
  - C) If unused: remove from EC2_MANIFEST

---

## Baseline Confirmation

**bd-gold-layer-runner** (GLDRST.015): Watchdog timer ACTIVE. Dual shutdown: `run_gold_layer.sh` self-shutdown + `watchdog-shutdown.timer` safety net (every 5 min). SSM-safe via `ssm-run-gold.sh` nohup wrapper. This is the gold standard for ephemeral instances.

---

## Sources Audited

| File | Instance(s) |
|------|-------------|
| `infra/aws/ec2/EC2_MANIFEST.json` | All 9 |
| `infra/aws/ec2/moltbot/claude-config/CLAUDE.md` | moltbot |
| `infra/aws/ec2/smartx-exporter/run-all-portfolios.sh` | smartx-exporter |
| `infra/aws/lambda/smartx-ec2-autostart/lambda_autostart_v2.py` | smartx-exporter |
| `infra/aws/terraform/smartx-pipeline/iam.tf` (self-shutdown policy) | smartx-exporter |
| `infra/aws/ec2/seeking_alpha_scraper/run_scraper.sh` | seeking-alpha-scraper |
| `infra/aws/ec2/bd-gold-layer-runner/watchdog-shutdown.sh` | bd-gold-layer-runner |
| `infra/aws/ec2/bd-gold-layer-runner/setup-instance.sh` | bd-gold-layer-runner |
| `data/black_diamond/scripts/gold/ssm-run-gold.sh` | bd-gold-layer-runner |
| `infra/aws/ssm/opal-bd-allocation-download.json` | bd-allocations |
| `infra/aws/ssm/opal-bd-transaction-download.json` | bd-transactions |
| `infra/aws/ssm/opal-bd-unrealized-download.json` | bd-allocations |
| `infra/aws/ssm/opal-bd-realized-download.json` | bd-allocations |
| `infra/aws/lambda/bd-pipeline/bd-allocation-trigger/lambda_function.py` | bd-allocations |
| `infra/aws/lambda/bd-pipeline/bd-gold-trigger/lambda_function.py` | bd-gold-layer-runner |
| `infra/aws/ec2/bd-gold-detail-generator/user-data.sh` | bd-gold-detail-generator |
| `infra/aws/terraform/bd-pipeline/ec2.tf` | bd-allocations, bd-transactions, bd-gold-detail-generator |
| `infra/aws/ec2/bd-exporter/src/stepwise/run-daily-downloads.sh` | bd-exporter |
| `infra/aws/ec2/bd-exporter/terraform/scripts/beast_user_data.sh` | bd-exporter |
| `infra/aws/ec2/bd-exporter/terraform/scripts/uploader_user_data.sh` | bd-exporter |
