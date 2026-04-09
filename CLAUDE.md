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

## Agent Autonomy Rules

14. **Agents operate autonomously.** Do NOT ask for permission to read files, write code, run builds, run tests, commit, or execute any non-destructive operation. Just do it. The only operations that require human confirmation are:
    - `rm -rf` or any recursive deletion
    - `git reset --hard`, `git push --force`, or other destructive git operations
    - Dropping database tables or deleting S3 objects
    - Stopping/terminating EC2 instances
    - Any operation that destroys data that cannot be recovered

    Everything else — reading, writing, editing, building, committing, pushing to CLOUD/DEV, running scripts, calling APIs — is pre-authorized. Move fast. Do not ask "should I proceed?" or "shall I continue?" — just execute.

## Compiler Tools (comp-*)

Before tracing data paths, dependencies, or system connections manually, use the compiler tools. They build a full-stack graph covering ALL layers (React components, API endpoints, Lambdas, S3 artifacts, gold scripts, EventBridge, CloudFront) in <2s.

- `comp-trace <query>` — trace connections up/down/both from any node in the system
- `comp-blast <query>` — blast radius: everything downstream of a change
- `comp-diff` — map git changes to system-wide impact
- `comp-xref` — diff the dependency graph against a baseline snapshot
- `comp-build` — force rebuild
- `comp-pipescript` — gold script I/O, pipeline DAG, feeds/consumers, chain order (authoritative: parses s3_layout.py + gold_dispatch.sh)
- `comp-routes` — full serving path: S3 artifact -> CloudFront -> auth -> Lambda/S3 -> frontend component (authoritative: parses cloudfront-distribution.tf + Lambda@Edge + API GW)
- `comp-transform` — client-side data flow: fetch -> response type -> useMemo/useCallback chains -> rendered JSX fields. Key: `schema-check` cross-references rendered fields against TypeScript types (adapter-aware, catches missing fields)
- `comp-platinum` — full-stack trace: page -> component -> fetch -> CloudFront -> auth -> S3 key -> gold script -> upstream deps. Also: `reverse` (S3 key -> route -> component), `tab-audit` (all ADVI tabs at once)
- `comp-cache` — React Query cache key map, collision detection, type mismatch flags across components
- `comp-pii` — PII field detection + `sweep` for hardcoded account numbers. Cross-references pseudonymizer target list with rendered fields, flags [HASHED] vs [CLEARTEXT], warns on S3-direct PII exposure

Use these BEFORE Explore agents or manual grepping for any cross-layer question. `comp-pipescript` for pipeline/gold questions, `comp-routes` for serving/auth questions, `comp-transform` for "what fields does this component render?", `comp-platinum` for full end-to-end page audits, `comp-cache` for query key issues, `comp-trace`/`comp-blast` for everything else. Full reference: `org/modules/graph/comp-tools.yaml`. All tools in `.tools/` (in PATH).

## Code Quality Rules

13. **No emojis in code.** Never use emoji characters (Unicode above U+007F) in production code, debug logs, diagnostic queries, print statements, or any code that runs on AWS. Emojis break CloudWatch log queries on Windows (charmap codec truncates at first non-ASCII), break log parsing tools (grep, sed, awk), and corrupt CI/CD pipelines that capture stdout. Use plain ASCII prefixes instead (e.g., `OK:`, `WARN:`, `ERROR:`, `SKIP:`, `BLOCKED:`).

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
