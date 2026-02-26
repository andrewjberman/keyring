# CLAUDE.md — Opal Capital Workspace

## First: Read START_HERE.md

All agents MUST read `START_HERE.md` at the repo root before beginning any work. It links to mandatory deployment protocols and infrastructure documentation.

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

## Code Quality Rules

13. **No emojis in code.** Never use emoji characters (Unicode above U+007F) in production code, debug logs, diagnostic queries, print statements, or any code that runs on AWS. Emojis break CloudWatch log queries on Windows (charmap codec truncates at first non-ASCII), break log parsing tools (grep, sed, awk), and corrupt CI/CD pipelines that capture stdout. Use plain ASCII prefixes instead (e.g., `OK:`, `WARN:`, `ERROR:`, `SKIP:`, `BLOCKED:`).

## Detailed Documentation

- **Lambda Deployment Protocol:** `docs/deployment/LAMBDA_DEPLOYMENT_PROTOCOL.md`
- **EC2 Deployment Protocol:** `docs/deployment/EC2_DEPLOYMENT_PROTOCOL.md`
- **EC2 Code Deployment Standard (S3 Artifact Model):** `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md`
- **Terraform Pipeline Strategy:** `infra/aws/TERRAFORM_PIPELINE_STRATEGY.md`
- **Agent Start Guide:** `START_HERE.md`

## Git

- Working branch: `CLOUD`. Portal submodule uses `DEV`/`PROD`.
- Terraform binary: `.tools/terraform.exe`
- On Git Bash: `export MSYS_NO_PATHCONV=1` before commands with `/` paths (Terraform imports, AWS CLI with ARN paths).

## Portal

- `portal/` — `bun install && bun run dev --port 5175`
- Bun: `/c/Users/AndrewBerman/.bun/bin/bun`
