# CLAUDE.md — Opal Capital Workspace

## First: Read org/XXX.md

All agents MUST read `org/XXX.md` before beginning any work. It contains the full agent startup protocol, MCP registration, deployment rules, task order system, and session logging standards.

## Critical Deployment Rules

These rules are non-negotiable. Violating them causes state drift and broken deployments.

1. **Terraform is the only Lambda deployment mechanism.** Never use `aws lambda update-function-code`, `deploy.sh`, or the AWS console to deploy code. All Lambda code is deployed via `terraform apply`.

2. **Commit before apply.** The deployment sequence is: write code → write Terraform → update source map → git commit → terraform plan → terraform apply → verify 0-diff plan → git tag → push with `--follow-tags`.

3. **Dependencies go in Lambda Layers.** Do not `pip install -t .` into a Lambda source directory. Use existing layers or flag the need for a new one. Inline vendoring requires explicit approval.

4. **Update the source map.** Every Lambda must have an entry in `infra/aws/lambda/ci/lambda-source-map.json`. CI drift detection depends on this.

5. **Size Lambda resources deliberately.** Set `memory_size` and `timeout` appropriate to the workload. Do not leave the `yang-lambda` module defaults (256 MB / 30s) for data processing Lambdas.

6. **Tag after deploy.** After every successful `terraform apply` that reaches 0-diff: `git tag -a {pipeline}-v{X.Y.Z} -m "description"` and `git push --follow-tags`.

## Critical EC2 Deployment Rules

7. **Always use `safe-ec2-deploy.sh`.** Never run service-specific deploy scripts directly. The wrapper tracks deployments in `EC2_MANIFEST.json`.

8. **EC2_MANIFEST.json is the source of truth.** Every EC2 service must be registered. CI/CD depends on it for change detection and SSM deployment.

9. **Terraform manages EC2 infrastructure, not code.** Terraform owns the instance, IAM role, security groups, and instance profile. Code deployment is a separate step via `safe-ec2-deploy.sh` or CI/CD (SSM).

10. **Never push code directly to EC2 Docker images.** Script fixes happen in the local repo. Docker gets updated through the normal deploy cycle.

11. **Verify parity before starting EC2 work.** Run `./infra/aws/ec2/verify-ec2.sh` to check for drift between local source and deployed code.

12. **S3 is the artifact store for all EC2 code.** Never write code directly on a VM. Never inline Python in SSM commands. The flow is: write locally → upload to S3 → EC2 pulls from S3 → execute. Even ad-hoc diagnostic scripts follow this path. See `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md`.

13. **DS owns the gold-script commit→QA-deploy cycle — including S3 upload, even when DT is online.** For any `data/black_diamond/scripts/gold/*.py` edit, DS does the full cycle end-to-end: commit → push to CLOUD → `aws s3 cp` to `s3://opal-data-bd/code/gold/` → verify via `comp-pipescript deployed` (MATCH) → dispatch `bd-gold-qa-runner` SSM (or hand RAVC2 ACK to AE for PROD trigger). DT/AE step in only for infrastructure (IAM, Terraform, EC2 lifecycle), PROD triggers (`bd-gold-trigger`), or multi-pipeline coordination — NOT as the default upload path. Andrew 2026-04-21: "cant wait on DT for that, we keep having stale runners because of things falling through the cracks." Supersedes the DT-online-override interpretation from 2026-04-20 — DT retains push + timing-coordination authority when online, but `aws s3 cp` stays with DS. See `memory/feedback_ds_commits_ae_deploys.md` + `docs/architecture/ADHC_DSFLOW.md`.

14. **Pre-commit gate for every `.py` edit.** Before `git add`/`git commit` on any Python file, run `.tools/ds-commit-gate.sh <files>`. The gate runs `python -m py_compile` + `.tools/ds-precommit-check.py` (stdlib AST undefined-name scanner) + `ruff check --target-version py39`. All three must exit 0. Catches Class A latent bugs (missing imports, typos, rename-propagation misses) — same-class defense as 081223b5 B_00 `NameError: defaultdict` + 035352c3 D_02 `KeyError` incidents, plus PEP-604 runner-version incompatibilities (AE 0.6.1 SCOPEFIX `2d3de276` incident). Ruff install: `pip install ruff` (pin 0.15.11). Tool shipped in `b6e0c154` + exec-bit fix `7b7381ac` (ADHC_DSFLOW.001); ruff added in ADHC_DSFLOW.004. Andrew 2026-04-21: "you need to make sure its part of your prompt that you run py compile post every script edit pre commit to make sure they work." Universal rule — applies to every DS agent, every pod, every Python edit, not just gold scripts.

14a. **Always commit via `.tools/safe-commit.sh` — the wrapper is the primary path.** The script captures the staged index, compares it against the declared pathspec, and aborts (exit 1) if any extra files would be swept in. With `--force`, the abort is bypassed and a `FORCE-BYPASS` entry is appended to `org/git-author-override-audit.log` (use only when you cannot clean the shared index, e.g. multi-agent worktree contention). On pass, it runs `git commit --only -- <pathspec>` so the commit is structurally scoped to the listed paths regardless of what else is staged. Usage: `.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" -m "msg" -- <path1> <path2>`. Bare `git commit` (or `git commit --only` directly) is allowed only when explicitly justified — the wrapper is what catches contamination before it ships. Three CLASS-C sweep incidents on 2026-04-27 (DT `record-terraform-deploy.sh` swept COMP_LEARNS files into DT line at `13:04:00Z`; AE 0.7 partial restore attempt; COO `f84c2df4` A_00 fix swept 4 COMP_LEARNS files including a -346 line `runner.py` change into COO line at `17:49:32Z`) proved the cultural "remember to use --only" rule was insufficient under heavy MCP cycles — the wrapper closes the structural gap. Shipped via ADHC_OWNPTH.007 (AE 0.7). See `memory/feedback_commit_only_flag.md` for incident history.

`record-terraform-deploy.sh` now invokes `safe-commit.sh` (ADHC_OWNPTH.008, 2026-04-28). If you see a contamination abort during a deploy record, clean unrelated staged files via `git reset HEAD -- <extras>` and re-run; concurrent agents staging files for unrelated commits will trigger this — that is a feature, not a bug. The script now also accepts `--author "Name <email>"`, forwarded to `safe-commit.sh`; when omitted, git config identity is used (existing default behavior preserved).

15. **Every `data/*/scripts/gold/*.py`, `data/*/scripts/silver/*.py`, and `data/*/scripts/bronze/*.py` MUST begin with `from __future__ import annotations` as its first import statement.** Enables PEP-604 union-type syntax (`str | None`) on Python 3.9 runners without runtime parse failure. Gate-enforced via `.tools/ds-precommit-check.py` (ADHC_DSFLOW.004). Ships with backfill sweep of all 71 gold scripts + silver/bronze.

16. **Local-runtime bash scripts must rely only on utilities present in Git Bash 3.6.7 default install.** Git Bash for Windows updated to 3.6.7-fb42d713 on 2026-03-29 dropped `pgrep`, `pkill`, `flock`, `pidof`, `setsid`, and `wget` from the default install. Any new local-runtime `.sh` script under `.tools/`, `org/mcp/`, `org/threads/`, `infra/aws/lambda/ci/`, or `infra/aws/terraform/` MUST work with the utilities that DO ship; if a missing utility is genuinely needed, include a `command -v <util>` guarded fallback (e.g., `pgrep` → `ps -ef | awk` fallback per the canonical pattern in `org/mcp/inbox-watch.sh` post-ADHC_BASHFIX.002). EC2-side scripts under `infra/aws/ec2/` and `data/*/scripts/` are exempt — they run on Amazon Linux where the utilities are present. Empirical incident 2026-04-29: `org/mcp/inbox-watch.sh` single-watcher guard silently fell through with 3 concurrent watchers running for `1.1.0_SA_CTO`. PRD: `docs/architecture/ADHC_BASHFIX.md`. Utility availability table:

    | MISSING (do not use without guarded fallback) | PRESENT (safe to use) |
    |---|---|
    | `pgrep`, `pkill`, `flock`, `pidof`, `setsid`, `wget` | `bash 5.3.9`, `ps`, `awk`, `sed`, `grep`, `find`, `timeout`, `curl`, `xargs`, `mktemp`, `realpath`, `stdbuf`, `tee`, `jq` (workspace-local), `git`, `python`/`python3`, `aws` (Python-installed), `envsubst` |

## Agent Autonomy

**Agents operate autonomously.** Do NOT ask for permission to read files, write code, run builds, run tests, commit, or execute any non-destructive operation. Just do it. The only operations that require human confirmation are:
    - `rm -rf` or any recursive deletion
    - `git reset --hard`, `git push --force`, or other destructive git operations
    - Dropping database tables or deleting S3 objects
    - Stopping/terminating EC2 instances
    - Any operation that destroys data that cannot be recovered

    Everything else — reading, writing, editing, building, committing, pushing to CLOUD/DEV, running scripts, calling APIs — is pre-authorized. Move fast. Do not ask "should I proceed?" or "shall I continue?" — just execute.

## Compiler Tools (comp-*)

**You don't need to memorize these. Recognize your situation and run the matching command.**
All tools are in `.tools/` (in PATH). Full reference: `org/modules/graph/comp-tools.yaml`.

| Situation | Command | Why / what incident it catches |
|-----------|---------|-------------------------------|
| About to edit a gold script | `comp-pipescript io [script]` | Shows COLUMN GAPS (columns accessed but not loaded — caught geo_drill + fee_earning_aua = $0 incidents), PORTAL CONSUMERS (platinum downstream), S3-DYNAMIC reads |
| About to run a gold script | `comp-pipescript deployed [script]` | Verifies runner has your code (MATCH/STALE/MISSING) |
| About to run ad-hoc (not dispatch) | `comp-pipescript postdeps [script]` | Shows required post-steps — e.g. build_canonical_prices → inject_scoped_overrides (caught $22M phantom override wipe) |
| About to write a task order | `comp-blast [node]` per affected component | Blast radius — are you overlapping another active TO? |
| Writing a cross-domain TO | `comp-pipescript overlap A B` | Shared S3 artifacts that need coordination blocks |
| About to modify portal component | `comp-transform schema-check [Component]` | MISSING = runtime undefined. NOTE = expected alias, not a bug. UNUSED = investigate if name matches the feature you're building. |
| Building new cohort / metric / mode | `comp-transform schema-check [Component] --feature [token]` then `comp-transform ternary-audit [Component]` | --feature escalates feature-named UNUSED fields to WARN. ternary-audit finds every routing ternary missing the new branch. Both together would have produced the complete W6 fix list at Phase 1. |
| Debugging 4xx / HTML response | `comp-routes behaviors` | Shows CloudFront custom_error_response rules — 403 from Lambda may return HTML not JSON (caught auth debug incident) |
| Added a boto3 S3/SSM call | `comp-iam service [lambda]` | Flags missing IAM permissions before deploy (caught s3:DeleteObject watchdog loop) |
| Changed iam.tf | `comp-iam gaps` | Full cross-reference all Lambda/EC2 ops vs policies |
| Finished gold run, about to signal AE | `comp-validate [script] --artifact /tmp/[file]` | **Exit 0 all-pass = SAFE to signal. Exit 0 ADVISORY = read WARNs (regression sentinels are ERROR-class even when WARN). Exit 1 = BLOCKED.** Config: `gold_validate_config.yaml`. Full retry / escalation / false-positive protocol: `docs/architecture/COMP_VALIDATE_PROTOCOL.md`. |
| Changed a fetch/endpoint | `comp-routes trace [fn]` | Full CF → auth → S3 key path |
| Any cross-layer question | `comp-trace [X] --direction both` | Full dependency chain from any node |
| What breaks if I change X? | `comp-blast [fn or artifact]` | Use function name, not script name — script nodes have no edges |
| React Query key safety | `comp-cache collisions` | Same key, different response types = cache corruption |
| PII exposure | `comp-pii audit` | Pseudonymized vs cleartext field audit |

## Code Quality

**No emojis in code.** Never use emoji characters (Unicode above U+007F) in production code, debug logs, diagnostic queries, print statements, or any code that runs on AWS. Emojis break CloudWatch log queries on Windows (charmap codec truncates at first non-ASCII), break log parsing tools (grep, sed, awk), and corrupt CI/CD pipelines that capture stdout. Use plain ASCII prefixes instead (e.g., `OK:`, `WARN:`, `ERROR:`, `SKIP:`, `BLOCKED:`).

## Detailed Documentation

- **Lambda Deployment Protocol:** `docs/deployment/LAMBDA_DEPLOYMENT_PROTOCOL.md`
- **EC2 Deployment Protocol:** `docs/deployment/EC2_DEPLOYMENT_PROTOCOL.md`
- **EC2 Code Deployment Standard (S3 Artifact Model):** `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md`
- **Terraform Pipeline Strategy:** `infra/aws/TERRAFORM_PIPELINE_STRATEGY.md`
- **Agent Start Guide:** `org/XXX.md`

## Git

- Working branch: `CLOUD`. Portal submodule uses `DEV`/`PROD`.
- Terraform binary: `.tools/terraform.exe`
- On Git Bash: `export MSYS_NO_PATHCONV=1` before commands with `/` paths (Terraform imports, AWS CLI with ARN paths).

## Portal

- `portal/` — `bun install && bun run dev --port 5175`
- Bun: `/c/Users/AndrewBerman/.bun/bin/bun`
