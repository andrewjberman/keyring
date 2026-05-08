---
name: cloud-ops
description: Operational reference + permissions profile for AE_CloudOps agents. Loads when the agent will be running AWS CLI, Terraform, EC2/SSM operations, or any other cloud-infrastructure work. Pre-approves the wildcards in .claude/settings.json so the agent is not interrupted with permission prompts for routine cloud ops. Confirms the CLAUDE.md non-negotiables that pre-approval does NOT override.
---

# cloud-ops

You are operating in a pre-approved cloud-ops profile. The wildcards in `.claude/settings.json` cover the routine AWS / Terraform / EC2 / SSM / CloudFormation / .tools surfaces. Run them autonomously — do not pause to ask the user "should I run this?" for any pattern that already matches.

## What's pre-approved (you don't need permission)

- `aws *` — all AWS CLI commands (Bash + PowerShell)
- `terraform *` (any binary path: `.tools/terraform.exe`, `terraform`, `terraform.exe`) — plan, apply, refresh, init, import, state ops
- `.tools/*` — comp-blast, comp-iam, comp-pipescript, comp-routes, comp-iam, safe-commit.sh, ds-commit-gate.sh, jq, terraform.exe
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

- `aws lambda update-function-code` / `update-function-configuration` — **violates deployment rule 1**. Lambda code deploys ONLY via terraform apply.
- `deploy.sh` shortcut scripts for Lambdas, AWS console deploys
- Direct EC2 code writes (`aws s3 cp ... s3://opal-data-*/code/...` is fine; SCP/SSH to write code on a VM is not — see deployment rule 12)
- `terraform destroy` of any resource without explicit instruction
- `git reset --hard`, `git push --force` (especially to main/master), `git tag -d -r`, force-deletion ops
- `rm -rf` of anything outside `/tmp` or workspace `.runtmp/` / `.frontend-dev/`
- Stop/terminate EC2 instances unless the workflow explicitly calls for it (e.g., a known-stale runner)
- `aws s3 rm --recursive`, `aws s3api delete-bucket`, `aws dynamodb delete-table` — irreversible
- Anything that drops/empties a database table, deletes S3 objects in opal-data-* buckets, or modifies CI/CD pipelines without an authoring TO

For these, surface the command + the reason + ask before running.

## Pre-flight checklist (before any cloud apply)

For Terraform applies on infra/aws/terraform/{pipeline}/:

1. `git tag -l "{pipeline}-v*" | sort -V | tail -5` — find the actual latest tag (CRITICAL: see memory rule about not assuming next version)
2. `terraform plan` — read the diff before applying. If a `-target` is needed because of P3 module S3 artifact gaps, target the specific resource. Note targeting in the RAVC.
3. RAVC1 to CTO + COO with the plan diff for any non-trivial change. For trivial in-place attribute updates (state flips, env var bumps), surface plan + apply in one RAVC if pre-authorized by a TO; otherwise wait for GO.
4. Apply, then `terraform plan` again for 0-diff verification.
5. Tag `{pipeline}-v{X.Y.Z}`, push `--follow-tags`.
6. RAVC2 with apply confirmation + AWS state check (e.g., `aws events describe-rule`, `aws lambda get-function-configuration`).

For EC2 code deploys: write locally → upload to `s3://opal-data-{firm}/code/...` → EC2 pulls from S3 → execute. Never write code directly on a VM. Even ad-hoc diagnostic scripts go through S3.

## Compiler tools (run when the situation matches — see CLAUDE.md table)

- `comp-pipescript io <script>` — column-gap audit before editing gold/silver scripts
- `comp-pipescript deployed <script>` — verify EC2 runner has your code
- `comp-blast <node>` — blast-radius before TO authoring or risky changes
- `comp-iam service <lambda>` — IAM gap check after adding boto3 calls
- `comp-validate <script> --artifact /tmp/<file>` — gold script post-run validation

## Commit hygiene

ALWAYS use `.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" -m "msg" -- <pathspec>`. The wrapper aborts if extra files would be swept in. Never use bare `git commit -a` in this workspace. Multiple incidents (2026-04-27, 2026-04-22) prove the structural guard is needed.

## Failure handling

- TF state drift: investigate with `terraform refresh` first; never `terraform state rm` without surfacing.
- Apply error mid-run: capture full stderr, RAVC2 to CTO + COO, do not retry blindly.
- Pre-commit gate fails on a Python edit: read the gate output, fix the issue, re-stage, NEW commit (never `git commit --amend` after a hook failure).
- record-terraform-deploy.sh tooling failure: known issue (CHANGELOG.json writer + owned-paths-hook on Andrew identity); reset the spurious source-map.json changes and surface in RAVC.

You're cleared. Move fast within the rails.
