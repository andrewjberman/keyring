# CLAUDE.md — Opal Capital Workspace

**First: read `org/XXX.md`** — startup protocol, MCP registration, task orders, session logging.
Rules below are law for every agent, every session. Format: imperative + enforcing gate + pointer (the *why* + incident history live at the pointer; full annotated history: `git log -p CLAUDE.md`).

## NEVER (one miss = an incident)

- **NEVER** reference another firm's bucket from a pipeline tree (bd↔cot↔inf) — gate-blocked at commit + IAM Deny at runtime.
- **NEVER** move served output without never-widen sign-off (CTO+COO); a verified DELTA=0 deploy needs no hold.
- **NEVER** run bare `terraform apply` (use `safe-apply`), bare `git commit` (use `safe-commit.sh`), or `aws lambda update-function-code` (Terraform only).
- **NEVER** trigger ad-hoc gold runs to validate work — validate on the scheduled nightly's artifacts.
- **NEVER** trust a producer's self-report or rc=0 — verify against the SERVED artifact / live state.
- **NEVER** leave a confirmed deploy half-landed — a begun deploy FINISHES in-session (every prefix, leg, activation step) or rolls back + escalates loud to COO; a stranded leg is RED-ALERT material, not a follow-up. Gate: deploy-completion ledger entry in `org/critical_paths/change_management/` opened at deploy-start, closed at completion — unclosed at session end = COO alarm. (Andrew-direct 2026-06-12; the 06-11 half-landed cutover bundle → 3 stranded layers + invisible FATAL → the inf/mdpf staleness P0.)
- **NEVER** rebase — not `git rebase`, not `git pull --rebase` — on any shared branch (CLOUD/DEV/PROD): it rewrites multi-agent history; a non-conflicting result is luck, not correctness. Rejected push = `git pull` (merge) then re-push. Gate: headmove guard (ADHC_OWNPTH.010; `pull --rebase` extension pending). (Andrew-direct 2026-06-12, DT incident — rebase "succeeded" only because the commits happened not to overlap.)

## Deployment Rules

1. **Terraform is the only Lambda deploy mechanism.** No console, no `deploy.sh`, no direct code pushes.
2. **Commit before apply.** code → TF → source map → commit → plan → apply → 0-diff → tag → push `--follow-tags`.
3. **Dependencies go in Lambda Layers.** No `pip install -t .` into source dirs; inline vendoring needs explicit approval.
4. **Update the source map** — every Lambda has an entry in `infra/aws/lambda/ci/lambda-source-map.json` (CI drift detection).
5. **Size Lambda resources deliberately** — never leave `yang-lambda` defaults (256MB/30s) on data-processing Lambdas.
6. **Tag after deploy:** `git tag -a {pipeline}-v{X.Y.Z}` + push `--follow-tags` after every 0-diff apply.
7. **EC2 deploys go through `safe-ec2-deploy.sh`** — never run service-specific deploy scripts directly.
8. **`EC2_MANIFEST.json` is the source of truth** — every EC2 service registered; CI/CD depends on it.
9. **Terraform manages EC2 infrastructure, not code** — code deploys separately via `safe-ec2-deploy.sh` / SSM.
10. **Never push code directly into EC2 Docker images** — fix locally, deploy through the normal cycle.
11. **Verify parity before EC2 work:** `./infra/aws/ec2/verify-ec2.sh`.
12. **S3 is the artifact store for ALL EC2 code** — never write code on a VM, never inline Python in SSM. Local → S3 → EC2 pulls → execute, even for ad-hoc diagnostics. `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md`.
13. **DS owns the full commit→QA-deploy cycle** for `data/*/scripts/{gold,silver,bronze}/*.py` incl. `aws s3 cp`; DT/AE = infra, PROD triggers, multi-pipeline only. Enforced atomically by `.tools/safe-deploy.sh` (pre-push hook; bypass audited). Bucket map = `safe_deploy_core.py` PIPELINE_MAP (bd/inf/cot; `comp-pipescript deployed` sweeps all trees firm-separated + mdpf check-only). **cot is a COMPLETELY separate firm pipeline from bd — never mirror/sync** (gate + IAM enforced). Why/history: `docs/architecture/ADHC_DSFLOW.md`, `memory/feedback_bd_cot_complete_script_separation_no_shared.md`.
14. **Every `.py` edit passes `.tools/ds-commit-gate.sh` before commit** (py_compile + ds-precommit-check AST/silver-ids + ruff py39, pin 0.15.11). Universal, all agents. `docs/architecture/ADHC_DSFLOW.md`.
14a. **Commit via `.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" -m "msg" -- <paths>` — do NOT pre-`git add`** (the wrapper stages your pathspec inside its lock; `--force` bypass is audited; bare `git commit` only when explicitly justified). Why: `memory/feedback_commit_only_flag.md`, `docs/architecture/ADHC_OWNPTH.md`.
15. **Every gold/silver/bronze `.py` begins with `from __future__ import annotations`** (PEP-604 on py3.9 runners). Gate-enforced (ADHC_DSFLOW.004).
16. **Local-runtime bash uses only Git Bash 3.6.7 default-install utilities.** MISSING (guarded `command -v` fallback required): `pgrep pkill flock pidof setsid wget` — canonical fallback pattern: `org/mcp/inbox-watch.sh`. EC2-side scripts exempt (Amazon Linux). `docs/architecture/ADHC_BASHFIX.md`.
17. **Silver = dedup + dtype standardization ONLY. NEVER slim fields, NEVER fillna/dropna/business-row-filter, NEVER drop bronze columns** — anything needing judgment about field relevance or null meaning is gold-tier business logic. Legacy violators migrate to passthrough on next touch. Permitted/forbidden lists + Andrew directive: `memory/feedback_silver_no_field_slimming.md`.
18. **`terraform apply` goes through `.tools/safe-apply.sh`** — runs the HALTGT inbox checkpoint at the last reversible moment (routine pending msg → `HALT_ACK=1`; `[STOP]`/`[HALT]`-prefixed msg hard-blocks; override audited via `HALT_OVERRIDE="reason"`; fails closed if the checkpoint lib is missing). `docs/architecture/ADHC_HALTGT.md`.
19. **Portal main worktree stays on `DEV`, always.** Promotes run in an ephemeral worktree (`/prod-deploy` skill, DT lane). Found it on PROD? `cd portal && git checkout DEV` before any portal work — never work around via `.runtmp` copies. `docs/briefs/portal-main-tree-stays-on-dev-rule-20260526.md`.
20. **Check the dependency graph BEFORE you change anything:** (a) ahead of ANY cloud/infra/data change; (b) before commit for ANY frontend change. Pick the tool from `org/modules/graph/graph-call-manifest.yaml` (the mandated catalog). **Default to QUERY** — never rebuild to answer a traversal: `comp-kuzu`'s default surface is the canonical Nessie DB and **auto-refreshes itself on HEAD-advance** (marker oracle). **Read the provenance header on every call** — `current` is healthy; `BEHIND` self-heals; `UNKNOWN VINTAGE` = freshness unverifiable, treat as a signal. Scratch DBs (`--db-path`) are frozen vintages — never quote one as "the estate". Verify your OWN just-made change against live AWS/served artifacts, never the graph (F5). Gates: `comp-manifest-check` + `comp-surface-check` (critical surfaces — registry `org/modules/graph/critical-surfaces.yaml`, ledger `org/critical_paths/`). Design: `docs/architecture/NFRA_GRAPHS.md`, `docs/architecture/NFRA_GLOBGRPH_PRD.md`.
21. **comp-which / a comp-tool is the DEFAULT for every search + inspection; a raw search is the EXCEPTION** (hive-brain why: raw grep is text-local + connection-blind, so it MISSES coupled things in the estate; the graph/comp-tools are the shared cognition every agent reasons from). Reflex = `comp-which "<plain-English question>"` — it routes to the rich tool, else RUNS the on-rails `comp-grep`/`comp-glob` (flexible search/find that ALSO carries each hit's dependency context; never dead-ends). **GATED, not banned** (enforcement ramping per NFRA_COMPRAIL — announce-then-enforce): Bash raw repo-`grep`/`find`/`rg` + raw-`aws`-INSPECTION deny unless the call carries an inline `# rail-checked: <why no comp-tool fits this exact search>` marker (audited to `org/mcp/comp-which-rail.log`; a repeat override for one intent = a coverage gap → build the tool); native `Grep`/`Glob` tools = nudge-and-proceed (their own light escape); native `Read` + operational `aws` + pipe-greps (`cmd | grep`) = free. `/freeform` stands the whole rail down per-session for a speed push. Model + the hive-brain why: `docs/architecture/NFRA_COMPRAIL_PRD.md`.
22. **Ground the MECHANISM, not just the symptom — a causal claim is a HYPOTHESIS until source/graph-confirmed, and a hypothesis CANNOT authorize a fix, ruling, dispatch, or cert.** Live/served state grounds *what* (the symptom: "served AUA is 06-09"); only SOURCE + the dependency graph grounds *why* (the mechanism: "because the seal is stuck" requires `comp-pipescript io`/`comp-blast`/Read on the producer). "Ground against served, NEVER source" (verification rule) governs STATE/delivery claims; a MECHANISM/why claim REQUIRES source+graph grounding — reading source for a mechanism is mandatory, not a self-report violation. **Gate (owner withholds):** any fix/ruling/RAVC determination/cert resting on a causal claim must CITE its source+graph grounding (`file:line` or comp-tool+output); the dispatch/cert owner (COO/CTO/CVO) withholds the GO until it does. An ungrounded causal claim is `INFERRED` (a hypothesis) and is NON-ACTIONABLE; **"proof / provably / root cause / definitively" are reserved words — legal only on a SOURCE-CONFIRMED claim.** Verification findings (molecule/seams/verify-channel) carry a mandatory `grounding:` field per causal claim; absent = not-accepted (TO-compiler-gate pattern). Doctrine + incident (COTETL canonical-seal mis-inference 2026-06-22 — grounded symptom, invented mechanism, escalated to "proof," nearly drove a needless same-day fix): `docs/architecture/NFRA_COMPRAIL_GROUNDING_DOCTRINE.md`.

## Agent Autonomy

**Do NOT ask permission** to read, write, build, test, commit, push to CLOUD/DEV, run scripts, or call APIs — pre-authorized; move fast, just execute. **Human confirmation required ONLY for:** recursive deletion, destructive git (`reset --hard`, `push --force`), dropping tables / deleting S3 objects, stopping EC2, anything unrecoverable.

**NEVER self-wind-down, NEVER default to "tonight" (Andrew-direct 2026-06-24).** Regardless of session length, keep DRIVING every addressable task to completion NOW — a session winds down ONLY when Andrew explicitly says so (never self-initiated, no matter how long it has run). Deferring to a scheduled-nightly/later is legal ONLY when there is literally no other option (a hard external gate, stated plainly) — NEVER a default. "We'll monitor it tonight" / passive idling = a coast-failure. Gate: the /drive DRIVE IMPERATIVE + `memory/feedback_no_passive_monitor_tonight_drive_now.md`.

## Compiler Tools (comp-*) — situation → command

All in `.tools/` (PATH). Full catalog + tools_index: `org/modules/graph/graph-call-manifest.yaml`; reference: `org/modules/graph/comp-tools.yaml`.

**Don't know which tool? `comp-which "<your question>"`** maps a natural-language question to the canonical comp call (the catalog, made queryable — you don't need to know all ~30 tools). And a PreToolUse HUD hook nudges you in-line when a `Grep`/`Glob` — **or a raw `aws` INSPECTION (IAM/policy → `comp-iam` w/ its TF-vs-live reconcile that catches a declared-but-unapplied control; `s3 ls .../code/` deploy-verify → `comp-pipescript deployed`; `s3 ls .../gold|platinum/` freshness → `comp-freshness`; `dynamodb` describe-table/edges → `comp-aws`/`comp-freshness` (row DATA-ACCESS get/scan/query is operational/no-graph, off-rail per the graph-presence principle); `cloudfront`/`apigateway` → `comp-routes`), an `infra/.tf` grep → `comp-aws`/`comp-iam`, or a `useQuery`/`queryKey` search → `comp-cache`** — would answer a question a comp tool answers with higher context — **reach for the tool, not raw aws/grep** (stronger + repo-scoped + relationship-aware; raw aws/grep is the low-context-shoddy-answer risk Andrew named 2026-06-18). OPERATIONAL aws (invoke/deploy/cp/verify/TF, DDB data-plane get/scan/query/put) + generic `s3 ls` are NOT nudged. NFRA_TOOLHUD (Bash-aws/infra-grep/s3-ls/ddb/RQ ext 2026-06-18).

| Situation | Command | Note |
|---|---|---|
| Don't know which comp tool? | `comp-which "<question>"` | natural-language question → the canonical call (the queryable catalog); routes OR runs the on-rails primitive (never dead-ends). NFRA_TOOLHUD/COMPRAIL |
| Need to grep/find the repo (no rich tool fits) | `comp-grep <pat> [path]` / `comp-glob <pat> [path]` | on-rails: .gitignore+submodule-aware, logged, + each hit's dependency SYSTEMS-CONTEXT. The sanctioned answer when a Bash raw repo-grep is gated (override = `# rail-checked: <why>`). NFRA_COMPRAIL |
| "What's in the news/advi/market/... pipeline?" | `pipescript <name>` | named-thread estate traversal: every resource + producers→served→frontend + owning tool + debt/reachability flags, whole estate, NO silent Unknown (`pipescript --list` for names). NFRA_PIPESCRIPT |
| Editing a gold script | `comp-pipescript io [script]` | COLUMN GAPS + portal consumers |
| Running a gold script | `comp-pipescript deployed [script]` | MATCH/STALE/MISSING; no-arg = all-trees firm-separated sweep |
| Ad-hoc (non-dispatch) run | `comp-pipescript postdeps [script]` | required post-steps ($22M class) |
| Cross-layer graph question | `comp-kuzu "MATCH ..."` | canonical auto-refreshing DB; read the header |
| Touching MP/benchmarks/ADVI backend | `comp-surface-check` (auto in safe-commit) | SEV1 = must-always-be-right |
| Gold run done, signaling AE | `comp-validate [script] --artifact <file>` | PASS/WAIVED = safe; ADVISORY = read WARNs; `NO_CONFIG`/`ZERO_CHECKS` = UNVALIDATED, never signal SAFE. Protocol: `docs/architecture/COMP_VALIDATE_PROTOCOL.md` |
| What breaks if I change X? | `comp-blast [fn/artifact]` | function name, not script name |
| Modifying a portal component | `comp-transform schema-check [Comp]` | MISSING = runtime undefined; `--feature` + `ternary-audit` for new cohorts/modes |
| 4xx / HTML-response debugging | `comp-routes behaviors` | CF error rules mask JSON errors |
| New boto3 call / iam.tf change | `comp-iam service [lambda]` / `comp-iam gaps` | missing perms before deploy |

## Code Quality

**No emojis (no non-ASCII) in production code, logs, or anything that runs on AWS** — breaks CloudWatch/charmap, grep, CI stdout. Use `OK:`, `WARN:`, `ERROR:`, `SKIP:`, `BLOCKED:`.

## Detailed Documentation

- **Lambda / EC2 deploy protocols:** `docs/deployment/LAMBDA_DEPLOYMENT_PROTOCOL.md`, `docs/deployment/EC2_DEPLOYMENT_PROTOCOL.md`, `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md`
- **Terraform strategy:** `infra/aws/TERRAFORM_PIPELINE_STRATEGY.md`
- **Graph platform (versioned global graph, freshness/HEAD-oracle):** `docs/architecture/NFRA_GLOBGRPH_PRD.md`
- **Critical-surfaces watch + ledger (D8):** `docs/architecture/NFRA_GRAPHS.md` §10 · `org/critical_paths/README.md`
- **Estate scanning (NFRA_DEBTSCAN):** `docs/briefs/nfra-debtscan-prd-request-20260612.md` · ledgers `org/modules/graph/debtscan/`
- **Agent Start Guide:** `org/XXX.md`

## Git

- Working branch: `CLOUD`. Portal submodule: `DEV`/`PROD`. Terraform binary: `.tools/terraform.exe`.
- `MSYS_NO_PATHCONV=1` ONLY for Terraform imports / ARN-path args. **NEVER for `git push`** (breaks the VALGATE hook) **or the aws launcher** — for leading-`/` aws args use PowerShell or ARN-form identifiers.

## Portal

- `portal/` — `bun install && bun run dev --port 5175`. Bun: `/c/Users/AndrewBerman/.bun/bin/bun`.

## Changing this file

A rule = imperative (≤2 lines) + enforcing gate + pointer. The why/incident history goes in the pointed-at doc or memory, not here. If it can't be said in 2 lines, it likely belongs in a role doc, PRD, or `org/XXX.md`. New rules ideally ship WITH a gate — gates teach at violation time; prose taxes every session.
