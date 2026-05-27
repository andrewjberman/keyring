---
name: cloud-ops
description: Operational reference + permissions profile for AE_CloudOps agents. Loads when the agent will be running AWS CLI, Terraform, EC2/SSM operations, or any other cloud-infrastructure work. Pre-approves the wildcards in .claude/settings.json so the agent is not interrupted with permission prompts for routine cloud ops. Confirms the CLAUDE.md non-negotiables that pre-approval does NOT override.
---

# cloud-ops

**Refreshed:** 2026-05-27 (ws CTO hygiene pass; CLAUDE.md Rules 1-19 cross-reference + LD-0034 / 0049 / 0066 / 0072 / 0082 / 0084 / 0090 / 0113 / 0115 / 0116 operating-doctrine pointers + current pipeline + bucket + secrets + KMS inventory snapshot)

You are operating in a pre-approved cloud-ops profile. The wildcards in `.claude/settings.json` cover the routine AWS / Terraform / EC2 / SSM / CloudFormation / .tools surfaces. Run them autonomously — do not pause to ask the user "should I run this?" for any pattern that already matches.

## What's pre-approved (you don't need permission)

- `aws *` — all AWS CLI commands (Bash + PowerShell)
- `terraform *` (any binary path: `.tools/terraform.exe`, `terraform`, `terraform.exe`) — plan, apply, refresh, init, import, state ops
- `.tools/*` — full canonical set (the wildcard covers all; named for reference):
  - **Compiler tools**: `comp-blast`, `comp-pipescript`, `comp-iam`, `comp-routes`, `comp-transform`, `comp-cache`, `comp-validate`, `comp-platinum`, `comp-pii`, `comp-trace`, `comp-build`, `comp-registry sync`
  - **Commit + deploy discipline**: `safe-commit.sh`, `safe-apply.sh`, `safe-deploy.sh`, `safe-ec2-deploy.sh`, `ds-commit-gate.sh`, `halt-gate-check.sh`, `record-terraform-deploy.sh`
  - **Misc**: `jq`, `terraform.exe`, `git-hooks/install-*.sh`
- EC2 lifecycle ops via SSM (`aws ssm send-command`, `aws ssm get-command-invocation`, `aws ssm list-commands`)
- S3 list / cp / sync via Bash and PowerShell
- CloudWatch Logs queries (`aws logs filter-log-events`, `describe-log-streams`, `get-log-events`, `put-log-events`, `describe-metric-filters`)
- CloudWatch Alarms (`aws cloudwatch describe-alarms`, `get-metric-statistics`)
- EventBridge inspect (`aws events describe-rule`, `list-rules`, `list-targets-by-rule`)
- Lambda inspect (`aws lambda get-function-configuration`, `get-function`, `list-functions`)
- DynamoDB read (`aws dynamodb query`, `get-item`, `scan`)
- IAM read (`aws iam get-role`, `get-role-policy`, `list-attached-role-policies`)
- CloudTrail inspect (`aws cloudtrail describe-trails`, `get-event-selectors`)
- git workflow (status, diff, log, add, commit via safe-commit.sh, tag, push, fetch, pull)
- Standard PowerShell file ops (Test-Path, New-Item, Get-ChildItem, Out-File, Set-Content)

If your task hits a tool the user has not pre-approved, ask once briefly — don't loop on retry.

## What is NEVER pre-approved (CLAUDE.md non-negotiables, ask first)

- `aws lambda update-function-code` / `update-function-configuration` — **violates Rule 1**. Lambda code deploys ONLY via terraform apply.
- `deploy.sh` shortcut scripts for Lambdas, AWS console deploys
- Direct EC2 code writes (`aws s3 cp ... s3://opal-data-*/code/...` is fine; SCP/SSH to write code on a VM is not — see Rule 12)
- `terraform destroy` of any resource without explicit instruction
- `git reset --hard`, `git push --force` (especially to main/master), `git tag -d -r`, force-deletion ops
- `rm -rf` of anything outside `/tmp` or workspace `.runtmp/` / `.frontend-dev/`
- Stop/terminate EC2 instances unless the workflow explicitly calls for it (e.g., a known-stale runner)
- `aws s3 rm --recursive`, `aws s3api delete-bucket`, `aws dynamodb delete-table` — irreversible
- Anything that drops/empties a database table, deletes S3 objects in opal-data-* buckets, or modifies CI/CD pipelines without an authoring TO
- **Bare `terraform apply` — banned by Rule 18.** Use `.tools/safe-apply.sh` (HALT-gate checkpoint immediately pre-irreversible-apply; STOP-class inbox messages hard-block; `HALT_OVERRIDE="<reason>"` audited bypass).
- **Bare `git commit` — banned by Rule 14a.** Use `.tools/safe-commit.sh --author "..." -m "..." -- <paths>` (concurrent-agent index-contamination guard).
- **`.py` edits without `.tools/ds-commit-gate.sh` — banned by Rule 14.** Three sub-gates must exit 0: `py_compile` + `ds-precommit-check.py` (AST + `coerce_silver_ids` enforcement + Rule-15 future-annotations check) + `ruff check --target-version py39`.
- **Silver-tier field-slimming / null-handling / business-row-filtering — banned by Rule 17.** Silver = clean shape, preserved content. Business logic belongs in gold.

For these, surface the command + the reason + ask before running.

## Current CLAUDE.md rule cross-reference (refreshed 2026-05-27)

CLAUDE.md is canonical for all the deployment + commit + code-quality rules. Snapshot of the rules that bind AE 0.7 specifically:

| Rule | Substance | Binding tool |
|---|---|---|
| **1** | Terraform-only Lambda deploy | `.tools/safe-apply.sh` (NOT `aws lambda update-function-code`) |
| **2** | Commit before apply | `safe-commit.sh` -> push -> `terraform plan` -> `safe-apply.sh` -> verify 0-diff -> tag -> `push --follow-tags` |
| **3** | Dependencies in Lambda Layers | NOT `pip install -t .` into Lambda source |
| **4** | Update source map | `infra/aws/lambda/ci/lambda-source-map.json` entry per Lambda |
| **5** | Size Lambda resources deliberately | Set `memory_size` + `timeout`; don't leave yang-lambda module defaults |
| **6** | Tag after deploy | `git tag -a {pipeline}-v{X.Y.Z}` + `git push --follow-tags` |
| **7** | `safe-ec2-deploy.sh` wrapper for EC2 | `EC2_MANIFEST.json` source of truth |
| **8** | `EC2_MANIFEST.json` source of truth | Every EC2 service registered |
| **9** | Terraform manages EC2 infra, not code | TF owns instance/IAM/SG; code via `safe-ec2-deploy.sh` or SSM |
| **10** | Never push code directly to EC2 Docker | Script fixes in local repo; Docker via deploy cycle |
| **11** | `verify-ec2.sh` before EC2 work | Drift check between local source + deployed code |
| **12** | S3 is artifact store for EC2 code | Write locally -> S3 -> EC2 pulls. No inline Python in SSM. |
| **13** | DS owns commit→QA-deploy cycle for gold/silver/bronze; `.tools/safe-deploy.sh` enforces atomically | Pre-push hook auto-fires; bypass `--allow-stale --reason "..."` audits to `org/safe-deploy-bypass-audit.log` |
| **14** | Pre-commit gate `.tools/ds-commit-gate.sh` for every `.py` edit | py_compile + ds-precommit-check.py + ruff |
| **14a** | Commit via `.tools/safe-commit.sh` | `--force` audits to `org/git-author-override-audit.log` |
| **15** | `from __future__ import annotations` as FIRST import in every `data/*/scripts/{gold,silver,bronze}/*.py` | Enables PEP-604 on Python 3.9 runners |
| **16** | Local-runtime bash scripts use Git Bash 3.6.7 utilities only | `pgrep`/`pkill`/`flock`/`pidof`/`setsid`/`wget` MISSING; use `ps`/`awk`/`grep`/`timeout` |
| **17** | Silver = clean shape, preserved content. No field slimming, no fillna, no business-row filtering. | Field-pruning + null-handling + business-logic belongs in gold |
| **18** | `terraform apply` via `.tools/safe-apply.sh` (HALT-gate checkpoint); `HALT_OVERRIDE="<reason>"` audited bypass | Audited to `org/halt-gate-override-audit.log` |
| **19** | Portal main worktree stays on DEV; PROD promotions via `git worktree add` ephemeral | Andrew direct ratify; check `cd portal && git checkout DEV` if stranded |

Read CLAUDE.md if unsure — this skill is a refresher, not a substitute.

## Pre-flight checklist (before any cloud apply)

For Terraform applies on `infra/aws/terraform/{pipeline}/`:

1. `git tag -l "{pipeline}-v*" | sort -V | tail -5` — find the actual latest tag (CRITICAL: don't assume next version).
2. `terraform plan` — read the diff before applying. If a `-target` is needed because of P3 module S3 artifact gaps, target the specific resource. Note targeting in the RAVC.
3. RAVC1 to CTO + COO with the plan diff for any non-trivial change. For trivial in-place attribute updates (state flips, env var bumps), surface plan + apply in one RAVC if pre-authorized by a TO; otherwise wait for GO.
4. **`.tools/safe-apply.sh` (Rule 18) — NOT bare `terraform apply`.** The HALT-gate checkpoint fires immediately before the irreversible apply: empty inbox passes silently; routine pending message surfaces (sender/subject/age) and requires `HALT_ACK=1` on re-invocation; **STOP-class** message (`[STOP]` or `[HALT]` subject prefix) hard-blocks. Override only via `HALT_OVERRIDE="<reason>"` (audited to `org/halt-gate-override-audit.log`). If the checkpoint library is missing, safe-apply fails closed.
5. After apply, `terraform plan` again for 0-diff verification.
6. Tag `{pipeline}-v{X.Y.Z}`, push `--follow-tags`.
7. RAVC2 with apply confirmation + AWS state check (e.g., `aws events describe-rule`, `aws lambda get-function-configuration`).

**For EC2 code deploys (Rule 12):** write locally → upload to `s3://opal-data-{firm}/code/...` → EC2 pulls from S3 → execute. Never write code directly on a VM. Even ad-hoc diagnostic scripts go through S3. Use `.tools/safe-ec2-deploy.sh` (Rule 7) — never service-specific deploy scripts directly.

**For DS-owned scripts (Rule 13):** `.tools/safe-deploy.sh` runs the commit→push→S3-upload→deployed-MATCH→SSM-dispatch cycle atomically. Pre-push hook auto-fires on `git push` for `data/*/scripts/{gold,silver,bronze}/*.py` paths. Bypass via `--allow-stale --reason "..."` (audited). AE coordinates with DS but DS owns the cycle.

## Compiler tools (run when the situation matches — full table in CLAUDE.md)

CLAUDE.md `## Compiler Tools (comp-*)` table is canonical — read it. AE 0.7-relevant high-frequency subset:

- `comp-pipescript io <script>` — column-gap audit before editing gold/silver scripts
- `comp-pipescript deployed <script>` — verify EC2/Lambda runner has your code (MATCH/STALE/MISSING)
- `comp-pipescript postdeps <script>` — show required post-steps before ad-hoc runs
- `comp-blast <node>` — blast-radius before TO authoring or risky changes
- `comp-iam service <lambda>` — flag missing IAM permissions before deploy (catches s3/secrets/dynamodb/sns/kms gaps)
- `comp-iam gaps` — full cross-reference of all Lambda/EC2 ops vs Terraform policies (run after iam.tf changes)
- `comp-validate <script> --artifact /tmp/<file>` — gold script post-run validation; exit 0 all-pass = SAFE to signal
- `comp-routes behaviors` / `comp-routes trace <fn>` — CloudFront / Lambda@Edge debugging
- `comp-registry sync ROW=N` / `--project CODE` / `--all` — REGISTRY-vs-JSON narrative drift detection (read-only default; `--apply` writes under CVO author line)
- `comp-pii audit` — pseudonymized vs cleartext field audit

After ANY `iam.tf` change → `comp-iam gaps`. After any new boto3 call → `comp-iam service <lambda>`.

## Commit + deploy hygiene

**Every commit via `.tools/safe-commit.sh` (Rule 14a):**
```bash
.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" -m "msg" -- <pathspec>
```
Wrapper aborts if staged index contains files outside declared pathspec (concurrent-agent contamination guard). `--force` bypasses but audits to `org/git-author-override-audit.log`. Never use bare `git commit -a`. Three CLASS-C sweep incidents 2026-04-27 prove the structural guard is required. **Concurrent-agent contamination is common during multi-agent MCP windows** — when safe-commit aborts on contamination, run `git reset HEAD -- <extras>` to unstage strays, then retry. Feature, not bug.

**Every `.py` edit via `.tools/ds-commit-gate.sh <files>` BEFORE `git add` (Rule 14):**
- `python -m py_compile`
- `.tools/ds-precommit-check.py` — AST undefined-name scanner + silver `coerce_silver_ids()` enforcement + Rule-15 `from __future__ import annotations` check
- `ruff check --target-version py39` (pin 0.15.11)

All three must exit 0. Catches Class A latent bugs at commit time vs SSM dispatch.

**Every DS-owned gold/silver/bronze deploy via `.tools/safe-deploy.sh` (Rule 13):**
Commit→push→S3-upload→`comp-pipescript deployed` MATCH→SSM dispatch (or RAVC2 ACK to AE for PROD). Pre-push hook auto-fires on `git push` for `data/*/scripts/{gold,silver,bronze}/*.py`. Bypass via `--allow-stale --reason "..."` audits to `org/safe-deploy-bypass-audit.log`. AE coordinates with DS but DS owns the cycle.

**Every Terraform apply via `.tools/safe-apply.sh` (Rule 18):**
HALT-gate checkpoint immediately pre-irreversible-apply (see Pre-flight §4). Bare `terraform apply` is BANNED.

**Every EC2 deploy via `.tools/safe-ec2-deploy.sh` (Rule 7):**
Tracks deployments in `EC2_MANIFEST.json`. Never run service-specific deploy scripts directly.

## Failure handling

- TF state drift: investigate with `terraform refresh` first; never `terraform state rm` without surfacing.
- Apply error mid-run: capture full stderr, RAVC2 to CTO + COO, do not retry blindly.
- Pre-commit gate fails on a Python edit: read the gate output, fix the issue, re-stage, NEW commit (never `git commit --amend` after a hook failure).
- `record-terraform-deploy.sh` tooling failure: known issue (CHANGELOG.json writer + owned-paths-hook on Andrew identity); reset the spurious source-map.json changes and surface in RAVC.
- **HALT-gate `STOP`-class blocks `safe-apply`**: read the inbox message in full, route the requested action (or coord with CTO if unclear), then `HALT_OVERRIDE="<reason>"` only if Andrew/CTO/MSTR explicitly clears.
- **`safe-commit.sh` aborts on contamination**: `git reset HEAD -- <extras>` to unstage the concurrent-agent files (DS/COO/CVO commonly stage own session logs in the shared index during multi-agent MCP windows), then retry. NOT `--force` unless wrapper bypass is genuinely needed (audited).
- **Inbox watcher `AUTO-RESPAWN-INTERRUPT-LOST` VERDICT**: kill the listed PID + relaunch via Bash tool with `run_in_background: true` (NEVER bare shell `&`). Watcher state in `.unread-deliveries` sentinel survives the relaunch.

## Operating doctrine pointers (LD cycle binding)

These ledger decisions bind AE 0.7 operating discipline. Cite in commit messages where relevant.

- **LD-0034** — unified `opal-agent-comms` broker + ws-rooted `inbox-watch` PATH wrapper for all serials (ws + CL). Legacy `feature_clb/org/mcp/cl-inbox-watch.sh` retired.
- **LD-0049** — Concurrency cap 8→16 raise; ceiling-not-target + reallocation-before-spawn discipline.
- **LD-0066** — 3-way /charter split: /ws-charter (ws CTO) + /cl-charter (CL CTO) + /mstr-charter (MSTR rare-use). Workers `/work` per LD-0072.
- **LD-0072** — `/work` skill body as universal Tier-2/3 worker-loop body; 20m cron cadence; workers self-classify blockers + MCP lane COO with `[BLOCKED-ASK]`.
- **LD-0082** — Deterministic loop arming at session start; primary cron arming per role-class.
- **LD-0084 §2** — Sibling-PRD pattern for deferred sub-deliverables (e.g., `.003` comp-graph deferred to Phase 1 first-Lambda land).
- **LD-0090** — ALWAYS-PROCEED operating principle (Constitution Art. XVI): ALWAYS proceed / NEVER delay / 1-turn-no-response = proceed. Sovereign-class reservation (S3/S4) preserved.
- **LD-0113** — Workspace-shared skills sync via `sync-skills-to-worktree.sh` (ws → CL idempotent + sha256 drift detection).
- **LD-0115** — Concurrency cap 16→20 raise (2026-05-27); cross-fabric combined counting per Constitution Art. XV.
- **LD-0116** — Chain-of-command edict (2026-05-27): **Tier-2/3 workers shall NOT MCP MSTR directly**. Workers route to lane COO; T1 routes upward. MSTR bounces violations + CCs responsible T1. Enforced structurally via `/work` SKILL.md §4a.1 ladder.

## Current pipeline + bucket inventory (snapshot 2026-05-27)

**Buckets AE 0.7 owns / operates:**
- `opal-data-bd` — Black Diamond (49 Financial); SSE-S3
- `opal-data-inf` — Inflection; SSE-S3
- `opal-data-demo` — Demo tenant; SSE-S3
- `opal-data-cottonwood` — Cottonwood firm (post-LD-0049 mid-May onboard)
- `opal-data-imo` — FIND_INSURE IMO research (2026-05-27 today; `imo-pipeline-v0.1.0`); SSE-S3 baseline + SSE-KMS upgrade pending `imo-pipeline-v0.X.0` per PRD v0.4 §3.1 (PII-scope prefixes)
- `opal-data-mdpf` — Partner ETF Ownership
- `opal-data-etfs` / `opal-data-aaii-v2` / `opal-data-pm` — sibling pipelines
- `opal-313476888478-lambda-artifacts` — Lambda packaging bucket (root)

**Terraform pipelines AE 0.7 owns:**
- `infra/aws/terraform/inf-pipeline/` — Inflection
- `infra/aws/terraform/bd-pipeline/` — Black Diamond
- `infra/aws/terraform/mdpf-pipeline/` — MDPF
- `infra/aws/terraform/imo-pipeline/` — FIND_INSURE (today)
- `infra/aws/terraform/shared-infra/` — KMS / OAI / cross-pipeline shared
- `infra/aws/terraform/portal-auth/` — Portal Cognito + L@E
- `infra/aws/terraform/orion-pipeline/` — Orion JWT pattern
- `infra/aws/terraform/smartx-pipeline/` — SmartX REST integration

**Secrets Manager namespaces AE 0.7 operates:**
- `orion/jwt/*`, `orion/credentials/*`
- `smartx/jwt/*`, `smartx/credentials/*`
- `find-insure/bright-data/*`, `find-insure/lusha-ai/*`, `find-insure/job-board/*` (today)
- `brightdata-api-key` (root; copied to find-insure/bright-data/ per Andrew AskUserQuestion choice (a) 2026-05-27)

**KMS keys (post-LD upgrade):**
- `find-insure-data-key` (PRD v0.4 binding; AE provisions in `imo-pipeline-v0.X.0`; key-policy = `find-insure-lambda-role` decrypt-grant only at v0.1; annual rotation enabled)

You're cleared. Move fast within the rails.
