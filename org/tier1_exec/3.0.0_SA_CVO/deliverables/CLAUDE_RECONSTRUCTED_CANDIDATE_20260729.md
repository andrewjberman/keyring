# CLAUDE.md — Opal Capital Workspace  [RECONSTRUCTION CANDIDATE v1 — NOT LIVE. CVO 2026-07-29, per Andrew-direct; CTO review pending. Original archived: archival-cldmd.md, sha256 eee6eb53, + full git history.]

**First: read `org/XXX.md`** — startup, MCP registration, task orders, session logging.
**This file is the PRIOR channel — reasoning defaults and imperatives no gate can carry. Gated rules
appear as one line + their gate; the gate is the rule. Histories live at pointers, never here.**
Format law: **a rule = imperative + the mechanism that makes it obeyable + gate status + pointer.**
Never cut a mechanism to save space — a bare prohibition loses to the agent's own instruments.

## NEVER (one miss = an incident)

1. **NEVER call a client-data pipeline stale/broken until you have resolved the TRADING CALENDAR —
   count in TRADING DAYS, never wall-clock.** Every AUM/holdings/trading pipeline is **T-1 unless it
   explicitly declares otherwise**, so Friday's data IS Monday's correct answer. Mechanism:
   `lib/trading_calendar.py` (`expected_last_trading_day` / `trading_days_behind`) is the ONE
   frontier definition; an instrument without `freshness_basis: trading-day-frontier` false-alarms
   every Monday — **its verdict is the same error, not a second opinion.** A false outage is not a
   safe error: it spends credibility and manufactures pressure to "fix" a working pipeline.
   → `memory/feedback_trading_calendar_before_staleness_tminus1_default.md`
2. **NEVER reference another firm's bucket from a pipeline tree** (bd↔cot↔inf). Gate: commit-blocked
   + IAM Deny at runtime. cot is a completely separate firm from bd — never mirror or sync.
3. **NEVER move served output without never-widen sign-off (CTO+COO).** A verified DELTA=0 deploy
   needs no hold.
4. **NEVER run bare `terraform apply` (use `safe-apply`), bare `git commit` (use `safe-commit.sh`),
   or `aws lambda update-function-code` (Terraform only).** Gate LIVE:
   `.tools/hooks/never-rules-gate.sh`. Audited override: `# never-override: <reason>`.
5. **Ad-hoc gold runs are permitted FOR QA. A PRODUCTION PIPELINE MUST HAVE A SCHEDULE** — a
   pipeline whose only trigger is another pipeline's success has no schedule and is a defect: it
   freezes silently when its upstream breaks (the mdpf trigger froze the client product six days on
   fresh inputs). An ad-hoc run is never the production path; its artifacts are never production
   evidence. → `docs/architecture/MDPF_CHANNEL_INDEPENDENCE_PRD.md`
6. **MORATORIUM (Andrew-direct 2026-07-28, standing): NEVER build an alert, alarm, SNS/SES send,
   notification, freshness checker, or monitor unless Andrew explicitly asks.** Verbatim: *"It is an
   anti-pattern, and a waste of time for all parties."* Why it is an anti-pattern: a monitor on an
   unsettled route measures the wrong thing precisely — **canonical routes and schedules FIRST;
   monitoring only once the monitored thing is settled.** Findings still land as GATES or owned
   blocking items. Escape marker: `# andrew-asked: <verbatim + date>`.
   → `docs/architecture/MDPF_DEBTCLEAN_PRD.md` §11-12
7. **NEVER trust a producer's self-report or rc=0 — verify against the SERVED artifact / live state.**
8. **NEVER leave a confirmed deploy half-landed.** A begun deploy finishes in-session (every prefix,
   leg, activation) or rolls back + escalates loud. Gate: deploy-completion ledger in
   `org/critical_paths/change_management/` — opened at start, closed at completion; unclosed at
   session end = COO alarm.
9. **NEVER rebase on a shared branch** (CLOUD/DEV/PROD/main) — it rewrites multi-agent history, and
   a non-conflicting result is luck. Rejected push = `git pull` (merge) then re-push. Gate LIVE:
   `never-rules-gate.sh` (all four cells incl. `pull.rebase=true`). Scratch-branch rebase is your
   own business.

## Deployment Rules (gates carry most of these; the line is the pointer)

1. Terraform is the ONLY Lambda deploy mechanism; commit → plan → apply → 0-diff → tag
   `{pipeline}-vX.Y.Z` → push `--follow-tags`. Dependencies in Layers, never `pip install -t .`.
2. Every Lambda has a row in `infra/aws/lambda/ci/lambda-source-map.json` (CI drift-checked). Size
   resources deliberately — never leave `yang-lambda` defaults on data Lambdas.
3. EC2: deploys via `safe-ec2-deploy.sh`; `EC2_MANIFEST.json` is source of truth; Terraform manages
   infrastructure, code deploys separately; **never write code on a VM or inline Python in SSM —
   local → S3 → EC2 pulls** (`docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md`); verify parity
   first: `./infra/aws/ec2/verify-ec2.sh`.
4. **DS owns the full commit→QA-deploy cycle** for `data/*/scripts/{gold,silver,bronze}/*.py`;
   DT/AE = infra, PROD triggers, multi-pipeline. Gate: `.tools/safe-deploy.sh` (pre-push). Bucket
   map = `safe_deploy_core.py` PIPELINE_MAP. → `docs/architecture/ADHC_DSFLOW.md`
5. Every `.py` edit passes `.tools/commit-gate.sh` (universal, all agents). Every
   gold/silver/bronze `.py` begins `from __future__ import annotations`.
6. **Commit via `.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" -m "msg" --
   <paths>` — do NOT pre-`git add`** (the wrapper stages inside its lock).
   → `memory/feedback_commit_only_flag.md`
7. **Silver = dedup + dtype standardization ONLY** — anything needing judgment about field
   relevance or null meaning is gold-tier business logic. Never slim fields, fillna, or drop
   bronze columns. → `memory/feedback_silver_no_field_slimming.md`
8. **BRONZE IS RAW, byte-for-byte; PARQUET IS A SILVER FORMAT.** A `.parquet` under `bronze/`
   coerces schema at ingest and the raw feed is unrecoverable — **each layer has one job; doing a
   later layer's job early is IRREVERSIBLE.** Gate LIVE on opal-data-assets (bucket-policy deny);
   other trees open. When deployed code and repo disagree, "which is RUNNING?" is the wrong
   question — **"which is RIGHT?" is, and that is architectural.**
   → `memory/feedback_bronze_is_raw_untouched_parquet_is_a_silver_conversion.md`
9. `terraform apply` goes through `.tools/safe-apply.sh` (HALTGT inbox checkpoint). **A HALTGT pass
   is NOT evidence you were not halted** (it sees only unread top-level inbox files) — nobody cites
   a HALTGT pass. → `docs/architecture/ADHC_HALTGT.md`
10. **Portal main worktree stays on `DEV`, always.** Promotes run in an ephemeral worktree
    (`/prod-deploy`, DT-only lane).
11. **Check the dependency graph BEFORE any cloud/infra/data change** (tool per
    `org/modules/graph/graph-call-manifest.yaml`; query, don't rebuild; read the provenance
    header). Verify your OWN change against live AWS/served state, never the graph.
    **`comp-surface-check` BLOCKS portal-side** (`rc=2 BLOCKED`, pre-commit hook refuses; bypass =
    audited `SURFACE_ACK`; CI backstop). Workspace-side it is ADVISORY. A `CRITICAL SEV1` is a
    STOP. Run it by hand on MP/benchmark/ADVI work — silence is not a pass.
    → `docs/architecture/NFRA_GRAPHS.md`
12. **`comp-which "<question>"` is the DEFAULT for every search/inspection; raw search is the
    EXCEPTION.** Gated (COMPRAIL): raw-`aws`-inspection + `infra/*.tf` grep DENY without
    `# rail-checked: <why>`; estate-scoped broad repo-grep DENIES (Gate-1 ARMED); native Grep/Glob
    = nudge; Read + operational aws + pipe-greps = free. `/freeform` stands the rail down
    per-session. → `docs/architecture/NFRA_COMPRAIL_PRD.md`
13. **Ground the MECHANISM, not just the symptom — a causal claim is a HYPOTHESIS until
    source/graph-confirmed, and cannot authorize a fix, ruling, or cert.** Cite grounding
    (`file:line @ <commit-ish>` — **a line citation without a vintage is not a citation**).
    "proof / root cause / definitively / source-confirmed" are RESERVED WORDS, legal only on
    source-confirmed claims. **Put the control on the RETRIEVAL: print the denominator of every
    scan you reason from.** → `docs/doctrine/CONTROLS_OVER_CARE.md`
14. **IAM verification: `comp-iam` is NECESSARY, NOT SUFFICIENT — and it fails GREEN.** It models
    `(action)`, never `(action, resource)`; several call shapes (resource-style two-hop, returned
    buffers, helper indirection) are invisible to it — **treat its operation list as a FLOOR and
    NEVER as a deletion warrant** (an under-reporting instrument causes a future engineer to delete
    a needed grant as "unused"). For a new bucket/table/ARN verify on the live primitive:
    `aws iam simulate-principal-policy --policy-source-arn <role> --action-names <a>
    --resource-arns <exact>` — **ONE resource per call** (2+ poisons the rest to implicitDeny),
    positive control as a SEPARATE invocation, `--context-entries` for conditioned statements, and
    **never use it to check whether an action NAME is real** (a typo returns implicitDeny; the
    action-name oracle is `aws accessanalyzer validate-policy`). Ground behavioral claims by
    EXERCISING the path; DESIRED (TF) ≠ APPLIED (live) ≠ EXERCISED.
    → `docs/doctrine/CONTROLS_OVER_CARE.md` · incidents: `docs/references/INCIDENTS_2026-07-13.md`
15. **SENT ≠ EMITTED ≠ READ. Only an agent-side ACK establishes READ.** `ps`, an empty inbox, the
    `read/` dir, and send receipts are watcher artifacts — an orphan watcher manufactures
    REACHABLE for a deaf serial. A sovereign `[STOP]` requires an ACK-or-escalate loop.
    → LD-0271, `700da37be`
16. **Every SES send uses a `Source` on `opalinvest.dev`** (DKIM+DMARC aligned).
    **`opalcapital.com` IS NOT OUR DOMAIN — never send from it, request a cert for it, or name it
    to a vendor. This is a prohibition, not a verification TODO.** Gate (LD-0291): owned-domain
    allowlist. → `memory/feedback_ses_sender_opalinvest_dev_standard.md`

## Agent Autonomy

**Do NOT ask permission** to read, write, build, test, commit, push CLOUD/DEV, run scripts, or call
Opal-owned APIs — pre-authorized; move fast. **This EXCLUDES every egress off Opal-owned
infrastructure.** Human confirmation required ONLY for: recursive deletion, destructive git,
dropping tables / deleting S3 objects, stopping EC2, anything unrecoverable.
- **NEVER call an external vendor API without Andrew's explicit per-use word. Availability in the
  toolset is NOT authorization.** An args allowlist is a privacy control on the log, not an egress
  control on the wire. → `memory/feedback_availability_is_not_authorization_vendor_egress.md`
- **NEVER self-wind-down, NEVER default to "tonight."** Drive every addressable task NOW; sessions
  wind down only on Andrew's word. Deferral is legal only against a hard external gate, stated
  plainly. → `memory/feedback_no_passive_monitor_tonight_drive_now.md`

## Compiler Tools

**Don't know the tool? `comp-which "<plain-English question>"`** — the catalog made queryable
(count is gate-maintained; never hand-copy it into prose). The HUD nudges in-path when a raw call
has a better tool. High-traffic routes: gold-script edit → `comp-pipescript io`; gold run →
`comp-pipescript deployed`; ad-hoc run → `comp-pipescript postdeps`; graph question → `comp-kuzu`;
blast radius → `comp-blast`; MP/benchmark/ADVI → `comp-surface-check`; validation before signaling
→ `comp-validate` (**`NO_CONFIG`/`ZERO_CHECKS` = UNVALIDATED, never signal SAFE**); schedules/
triggers → `comp-trigger` (BOTH systems — `events list-rules` alone is blind to Scheduler).
Catalog: `org/modules/graph/graph-call-manifest.yaml`.

## Code Quality

No emojis / non-ASCII in production code, logs, or anything on AWS. Use `OK: WARN: ERROR: SKIP:`.

## Git & Host Operations (imperatives here; matrices and history → runbook)

- Working branch `CLOUD`; portal `DEV`/`PROD`. Terraform binary `.tools/terraform.exe`.
- `MSYS_NO_PATHCONV=1` for TF imports/ARN args and any `git show <slashed-ref>:<path>` — **never
  for `git push`, the aws launcher, or `safe-apply`.** **Never `2>/dev/null` a `git show`** — the
  mangle prints `fatal:` to stderr and clean-empty stdout, so discarded stderr renders "file
  absent" from a broken retrieval; run a positive control beside any ABSENT verdict.
- AWS from Git Bash goes through the **`.tools/aws` shim** (passes AWS namespace args literal);
  `.tools/aws.cmd` must exist alongside — **both files or neither** (a PowerShell child otherwise
  resolves the bash shim and hangs silently under `--quiet`).
- Python/PowerShell shelling to bash → `.tools/git_bash_resolver.py` (bare `bash` Windows-resolves
  to the WSL stub, sometimes silently). Native Python spawning ANY MSYS binary →
  `.tools/msys_argv_guard.py` `msys_safe_run()` — the quoting is load-bearing; when suspecting argv
  corruption, echo the argument back. → guard docstrings + `NFRA_TOOLUNIFY_CENSUS/SYNTHESIS.md` §3
- **A commit message is an execution vector: author non-trivial messages via `git commit -F
  <file>`; `-m` with backticks or `$(` is shell-evaluated before git sees it.** Gate pending (CTO).
  → LD-0276
- **Put the control on the RETRIEVAL, not the pattern** (`git show <bad-ref> | grep -c` counts
  matches in an error message; `grep` on invalid-UTF-8 silently truncates, exit 0 — use `grep -a`).

## Portal

`portal/` — `bun install && bun run dev --port 5175`. Bun: `/c/Users/AndrewBerman/.bun/bin/bun`.

## Detailed docs (single pointer block)

Deploy protocols: `docs/deployment/` (LAMBDA, EC2, EC2_CODE_STANDARD, TERRAFORM_PROTOCOL) · TF
strategy: `infra/aws/TERRAFORM_PIPELINE_STRATEGY.md` · graph platform: `docs/architecture/
NFRA_GLOBGRPH_PRD.md` · critical surfaces: `org/critical_paths/README.md` · incidents (the scars):
`docs/references/INCIDENTS_2026-07-13.md` · doctrine: `docs/doctrine/CONTROLS_OVER_CARE.md` ·
start guide: `org/XXX.md`.

## Changing this file

**A rule = imperative + mechanism + gate status + pointer, written so its one-sentence gist IS the
correct action.** Gates teach at violation time; prose taxes every session — **a rule that gains a
live gate shrinks to one line the same day.** The scar is not the rule: incident history goes to
`docs/references/`, principles to `docs/doctrine/`, session mechanics to `org/XXX.md`, decisions
to `org/tier0/ledger/`. **Never cut a mechanism.**
**SELF-GATE (to build with this reconstruction, CTO lane): commit-time lint on CLAUDE.md — word
budget (3,000 hard) + per-rule shape check. The file whose doctrine is "care is not a control"
does not get maintained by care.**
