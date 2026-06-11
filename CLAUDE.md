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

13. **DS owns the full commit→QA-deploy cycle for `data/*/scripts/{gold,silver,bronze}/*.py` — including `aws s3 cp`.** Cycle: commit → push to CLOUD → S3 upload → `comp-pipescript deployed` MATCH → SSM dispatch (or RAVC2 ACK to AE for PROD). DT/AE handle infrastructure, PROD triggers, multi-pipeline coordination only. **Structural enforcement: `.tools/safe-deploy.sh` runs the cycle atomically** — pre-push hook auto-fires on `git push`; bypass via `--allow-stale --reason "..."` audits to `org/safe-deploy-bypass-audit.log`. Why + history: `memory/feedback_ds_commits_ae_deploys.md`; design: `docs/architecture/ADHC_DSFLOW.md`. **Pipeline→bucket map (`safe_deploy_core.py` PIPELINE_MAP): `data/black_diamond/scripts/*`→`opal-data-bd`, `data/inf/scripts/*`→`opal-data-inf`, `data/cot/scripts/*`→`opal-data-cot`.** The `cot` (Cottonwood) pipeline is a COMPLETELY separate firm pipeline from `bd` (Andrew sovereign 2026-06-10, NFRA_DTAFLP): its gold tree is git-versioned at `data/cot/scripts/gold/` and deploys ONLY to `opal-data-cot/code/gold/` — never mirrored/synced from `opal-data-bd`. Cross-firm bucket refs are blocked at commit (`ds-precommit-check.py` cross-firm guard) and at runtime (IAM cross-bucket Deny on the cot/bd roles). See `memory/feedback_bd_cot_complete_script_separation_no_shared.md`.

14. **Pre-commit gate for every `.py` edit.** Run `.tools/ds-commit-gate.sh <files>` before `git add`/`git commit`. Three checks must exit 0: `python -m py_compile`, `.tools/ds-precommit-check.py` (AST undefined-name scanner + silver `coerce_silver_ids()` enforcement for any `build_*` in `data/*/scripts/silver/`), `ruff check --target-version py39` (pin 0.15.11). Universal — every DS agent, every Python edit, not just gold. **Why:** catches Class A latent bugs (missing imports, typos, rename misses) and PEP-604 syntax incompatibilities with Python 3.9 runners at commit time rather than SSM dispatch. Independent of the deploy-cycle gate (`.tools/safe-deploy.sh`, Rule 13) — two structural layers. History: `docs/architecture/ADHC_DSFLOW.md`.

14a. **Commit via `.tools/safe-commit.sh`. Do NOT pre-`git add` — the wrapper stages your declared pathspec itself.** Usage: `.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" -m "msg" -- <path1> <path2>` — list every path after `--`; no separate `git add` (including for new files under gitignored prefixes like `.tools/` — the wrapper force-adds them internally). Mechanism (commit-mutex v2, MSTR-approved 2026-05-29 `a62305eed`): the wrapper acquires a per-worktree mkdir-mutex, captures the staged baseline, **stages your pathspec inside the lock**, then runs `git commit --only -- <paths>` so scope is structural regardless of index state. The contamination guard now flags only files **this run** staged outside its pathspec — peers' concurrently-staged files are ignored (they're in the baseline, and `--only` can never commit them anyway), eliminating the false-abort under multi-agent load. `--force` still bypasses with a `FORCE-BYPASS` audit entry to `org/git-author-override-audit.log`; bare `git commit` allowed only when explicitly justified. **Why:** three CLASS-C sweep incidents 2026-04-27 + the 2026-05-29 out-of-band-`git add` false-abort race proved cultural "remember to use --only" + a commit-body-only mutex insufficient under multi-agent MCP cycles. `record-terraform-deploy.sh` invokes this wrapper too (explicit pathspec → inherits stage-inside-lock cleanly). History: `memory/feedback_commit_only_flag.md`; design: `docs/architecture/ADHC_OWNPTH.md` + `docs/briefs/ws-commit-mutex-staging-serialization-design-20260529.md`.

15. **Every `data/*/scripts/gold/*.py`, `data/*/scripts/silver/*.py`, and `data/*/scripts/bronze/*.py` MUST begin with `from __future__ import annotations` as its first import statement.** Enables PEP-604 union-type syntax (`str | None`) on Python 3.9 runners without runtime parse failure. Gate-enforced via `.tools/ds-precommit-check.py` (ADHC_DSFLOW.004). Ships with backfill sweep of all 71 gold scripts + silver/bronze.

16. **Local-runtime bash scripts must rely only on utilities present in Git Bash 3.6.7 default install.** Git Bash for Windows updated to 3.6.7-fb42d713 on 2026-03-29 dropped `pgrep`, `pkill`, `flock`, `pidof`, `setsid`, and `wget` from the default install. Any new local-runtime `.sh` script under `.tools/`, `org/mcp/`, `org/threads/`, `infra/aws/lambda/ci/`, or `infra/aws/terraform/` MUST work with the utilities that DO ship; if a missing utility is genuinely needed, include a `command -v <util>` guarded fallback (e.g., `pgrep` → `ps -ef | awk` fallback per the canonical pattern in `org/mcp/inbox-watch.sh` post-ADHC_BASHFIX.002). EC2-side scripts under `infra/aws/ec2/` and `data/*/scripts/` are exempt — they run on Amazon Linux where the utilities are present. Empirical incident 2026-04-29: `org/mcp/inbox-watch.sh` single-watcher guard silently fell through with 3 concurrent watchers running for `1.1.0_SA_CTO`. PRD: `docs/architecture/ADHC_BASHFIX.md`. Utility availability table:

    | MISSING (do not use without guarded fallback) | PRESENT (safe to use) |
    |---|---|
    | `pgrep`, `pkill`, `flock`, `pidof`, `setsid`, `wget` | `bash 5.3.9`, `ps`, `awk`, `sed`, `grep`, `find`, `timeout`, `curl`, `xargs`, `mktemp`, `realpath`, `stdbuf`, `tee`, `jq` (workspace-local), `git`, `python`/`python3`, `aws` (Python-installed), `envsubst` |

17. **Silver tier conversions perform ONLY deduplication + type standardization. NEVER slim fields. NEVER apply null-handling, fillna, default-substitution, or business-logic-specific row filtering.** Silver = clean shape, preserved content. Anything that requires judgment about *what fields matter*, *what null means*, or *which rows to drop* is business-logic and belongs in the **gold** tier. **Why:** today's ADVI_DWSPLT investigation 2026-05-13 empirically proved that NEW REST silver's `output_cols` projection (`data/inf/scripts/silver/convert_transactions_to_silver.py:216` narrowing 31-bronze-cols to 18-silver-cols) was the root cause of the dual-writer "different data" framing — REST bronze had the fields all along; silver-side slimming created a false data-divergence with LEGACY CSV silver. Generalizing: null-handling is consumer-aware (what NA means depends on the downstream business semantic — `fillna(0)` for an amount column vs `fillna(None)` for a status flag vs `dropna()` for a required key are all different correctness judgments). Silver doesn't know the consumer; gold does. **Andrew directive 2026-05-13: "it annoys me to no end when agents make silver scripts that pare down available fields, they need to not fucking do that."** DS~D probe doc-of-record: `docs/briefs/silver-transactions-rest-extension-probe-20260513.md`. **What silver IS permitted to do:** deduplicate exact-row duplicates; standardize dtypes (e.g., `coerce_silver_ids()` Int64 enforcement per ADVI_INFNNA.SILVER-ID-DTYPE-UNIFY); coerce string→numeric on columns whose source is unambiguously numeric; flatten obvious encoding artifacts (whitespace, leading zeros on integer keys). **What silver is NOT permitted to do:** `output_cols` lists or SELECT projections that drop bronze columns; `fillna()` with business-defaulted values; `dropna()` on rows missing optional fields; row-level filtering by business semantic (e.g., "drop rows where status=Cancelled"); column renames that bury upstream provenance. **Applies to all DS + AE work** on `data/*/scripts/silver/**` and `infra/aws/lambda/{pipeline}/{lambda-name}/` Lambda-bundled silver-script copies. Gold tier (`data/*/scripts/gold/*.py`) is the only place field-pruning + null-handling + business-row-filtering are structurally permitted. Existing legacy silver scripts with violating logic get migrated to passthrough on next touch (not a forced backfill; opportunistic during normal maintenance). History + reasoning: `memory/feedback_silver_no_field_slimming.md`.

18. **`terraform apply` goes through `safe-apply`; the deploy/push paths carry a STOP checkpoint.** Use `.tools/safe-apply.sh` instead of a bare `terraform apply` — it runs the HALTGT checkpoint (`.tools/halt-gate-check.sh`) immediately before the irreversible apply, the last reversible moment. The pre-push hook (`.tools/git-hooks/pre-push-safe-deploy.sh`), `.tools/safe-deploy.sh`, and `infra/aws/ec2/safe-ec2-deploy.sh` carry the same checkpoint as a second net. Behavior (PRD §3.2 tiered verdict): an empty inbox passes silently; a routine pending message surfaces (sender / subject / age) and requires `HALT_ACK=1` on re-invocation; a **STOP-class** message hard-blocks. STOP-class is identified by a `[STOP]` or `[HALT]` subject prefix — `docs/architecture/HALTGT_SEVERITY_CONVENTION.md`. A STOP hard-block is bypassable only via an audited override: `HALT_OVERRIDE="<reason>"`, which appends a forensic line to `org/halt-gate-override-audit.log` (a dedicated log, separate from the commit-scope `git-author-override-audit.log`). The checkpoint is non-interactive — it never reads stdin; `HALT_ACK` / `HALT_OVERRIDE` are env-var gates. If the checkpoint library is missing, `safe-apply` fails closed (refuses the apply) — the primary net never silently disables itself. **Why:** message delivery is reliable, but an interrupt arriving mid-`terraform apply` is the failure class — the checkpoint structuralizes the cultural "check inbox before landing" so a STOP issued during a long irreversible op is seen *before* it, not after. PRD: `docs/architecture/ADHC_HALTGT.md`. Project: ADHC_HALTGT.

19. **Portal main worktree always stays on `DEV`.** Promotions to `PROD` execute in an ephemeral `git worktree add` and clean up the temp worktree on exit; the main `portal/` tree never leaves DEV. If you discover the main tree on PROD (incident, prior promotion strand, manual checkout — any sequence): restore via `cd portal && git checkout DEV` before any other portal work. Do NOT work around a stranded main tree by running `bun run dev` from `.runtmp/portal-*` — that hides the strand and lets it persist. **Why:** 3 separate strand incidents 2026-05-22 → 2026-05-26 prove the cultural rule (memory `feedback_portal_prod_promotion_strands_main_tree`) is structurally insufficient. Silent footgun — `bun run dev` doesn't warn the branch is PROD; only a missing DEV-only feature reveals it (today's anchor: ADVI_DEMOV1.008 TO-008 demo-tenant connection shipped to portal/DEV, invisible at localhost because the main tree was on PROD). Structural enforcement scope (post-checkout hook + `.tools/portal-promote.sh` wrapper + `bun run dev` predev check, brief options A+B+C) PRD scribe deferred next session per CTO capacity flag 2026-05-26 ~17:30Z; cultural rule binds NOW. Brief: `docs/briefs/portal-main-tree-stays-on-dev-rule-20260526.md`.

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

**Querying the dependency graph — use the manifest (NFRA_GRAPHS).** Before writing code (or an agent workflow) that derives, rebuilds, or queries the dependency graph, consult `org/modules/graph/graph-call-manifest.yaml` and use the `canonical` call for your use-case. **Default to QUERY** (`comp-kuzu` Cypher for cloud/cross-layer; cached `comp-trace`/`comp-blast` for repo/trace) — these answer in milliseconds against the persisted graph. **REBUILD** (`comp-build --force`, `comp-aws derive`) **only** to preempt a staleness you just created, or on the scheduled refresh — never rebuild the full graph to answer a traversal a query can answer. The pre-commit gate `comp-manifest-check` flags a deprecated/ad-hoc graph access (advisory→blocking as manifest coverage fills). Why + design: `docs/architecture/NFRA_GRAPHS.md`.

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
| Finished gold run, about to signal AE | `comp-validate [script] --artifact /tmp/[file]` | **Exit 0 `PASS:`/`WAIVED:` = SAFE to signal. Exit 0 ADVISORY = read WARNs (regression sentinels are ERROR-class even when WARN). Exit 1 = BLOCKED. `NO_CONFIG` = UNVALIDATED, NOT a pass (absence != PASS — fail-closed default exit-2, LIVE 2026-06-03 per COMP_VALIDATE_PROTOCOL §10.1 / LD-0148); `ZERO_CHECKS` (config present but 0 checks ran, all SKIP/deferred) = also UNVALIDATED exit-2 (§10.1b, LIVE 2026-06-03; message names the per-config deferred validator); never signal SAFE on `NO_CONFIG`/`ZERO_CHECKS` — register a config, run the deferred validator (comp-pipescript), or add an explicit `validation: not_required` waiver (`--lenient` bypasses).** Config: `gold_validate_config.yaml`. Full retry / escalation / false-positive protocol: `docs/architecture/COMP_VALIDATE_PROTOCOL.md`. |
| Changed a fetch/endpoint | `comp-routes trace [fn]` | Full CF → auth → S3 key path |
| Any cross-layer question | `comp-trace [X] --direction both` | Full dependency chain from any node |
| What breaks if I change X? | `comp-blast [fn or artifact]` | Use function name, not script name — script nodes have no edges |
| React Query key safety | `comp-cache collisions` | Same key, different response types = cache corruption |
| PII exposure | `comp-pii audit` | Pseudonymized vs cleartext field audit |
| REGISTRY narrative drift vs JSON | `comp-registry sync ROW=N` or `--project CODE` or `--all` | Detects 5 drift classes (PHASE-LAG / COMMIT-CITATION-LAG / PRD-LABEL-LAG / STATUS-MISMATCH / ROW-MISSING). Read-only default; add `--apply` for safe-commit.sh write-back under CVO author line. |

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
