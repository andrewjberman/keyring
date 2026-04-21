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

14. **Pre-commit gate for every `.py` edit.** Before `git add`/`git commit` on any Python file, run `.tools/ds-commit-gate.sh <files>`. The gate runs `python -m py_compile` + `.tools/ds-precommit-check.py` (stdlib AST undefined-name scanner). Both must exit 0. Catches Class A latent bugs (missing imports, typos, rename-propagation misses) — same-class defense as 081223b5 B_00 `NameError: defaultdict` + 035352c3 D_02 `KeyError` incidents. Zero pip deps; ~300 ms on a typical gold script. Tool shipped in `b6e0c154` + exec-bit fix `7b7381ac` (ADHC_DSFLOW.001). Andrew 2026-04-21: "you need to make sure its part of your prompt that you run py compile post every script edit pre commit to make sure they work." Universal rule — applies to every DS agent, every pod, every Python edit, not just gold scripts.

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
| Finished gold run, about to signal AE | `comp-validate [script] --artifact /tmp/[file]` | **Must exit 0 before signaling.** Config: `gold_validate_config.yaml`. Catches zero-valued fields, missing keys, wrong sums. |
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
