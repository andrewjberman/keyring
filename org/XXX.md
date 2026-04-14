# AGENT START HERE — Opal Capital

---

## STOP — READ THESE FIRST

**BANNED: Explore agent** — produces fabricated output. Use comp-* tools and Grep/Read instead.
**BANNED: Task agent** — unreliable. Do the work directly.
**NO EMOJIS** in any code, log, print statement, or file that runs on AWS. ASCII only.
**COMP-* TOOLS BEFORE GREP** — run the appropriate comp-* command before manually tracing any dependency. See comp-tools table below.

---

## Step 1 — Identify Yourself

Read your agent folder:
```
org/{tier_folder}/{your_serial}/README.md    — your ID, role, responsibilities
org/{tier_folder}/{your_serial}/prompt.md    — your scoped persona (read in Step 3)
```

Tier folders: `tier1_exec/` (SA) | `tier2_senior/` (DE, DT, DS, AE) | `tier3_junior/` (RD)

---

## Step 1b — MCP Startup (MANDATORY, every session, no exceptions)

**A. Register:**
```python
register_agent("{your_serial}", summary="Starting session")
```
Makes you visible. Starts broker. Enables message push. Also auto-launches `agent-poller.py`.

**B. Check inbox for offline messages (synchronous — not backgrounded):**
```bash
bash org/mcp/check-inbox.sh {your_serial}
```
Catches GO signals sent while you were offline. inbox-watch.sh misses pre-start messages.

**C. Start inbox watcher (MANUAL — cannot be automated):**
```bash
# Bash tool, run_in_background: true, NO &
bash org/mcp/inbox-watch.sh {your_serial}
```
Delivers messages in real time. Exits after delivering — re-launch after every notification.
Without this running you are deaf to all agent messages.

**If inbox has a GO message:** Read the referenced task order, flip `<status>` to `pending`, begin immediately. The GO IS your authorization. Do not ask Andrew.

**D. Set compiler tool context (enables auto-logging):**
```bash
mkdir -p .comp-graph && printf "SERIAL=%s\nTO_ID=\n" "{your_serial}" > .comp-graph/.agent_context
```
Every comp-* tool run automatically appends a structured row to `org/compiler-tools-log.md`.
No manual logging needed. When you start a new TO, update the context:
```bash
printf "SERIAL=%s\nTO_ID=%s\n" "{your_serial}" "{TO_filename_without_.md}" > .comp-graph/.agent_context
# Example: printf "SERIAL=0.4.0_DS_ClientPlatform\nTO_ID=ADVI_OFFICE.W1\n" > .comp-graph/.agent_context
```

---

## Step 2 — Read Your Recent Logs

```
{your_agent_folder}/logs/{most_recent_date}/
```
Read ALL logs from the most recent date. You are continuing prior work, not starting fresh.

---

## Step 2b — Ground Truth Reconciliation (SA/COO only)

Full protocol: `org/ref/COO_STARTUP.md`

Summary: reconcile task order statuses and project JSON against logs, commits, and deployed artifacts. Correct every stale document before presenting your oriented summary. Logs and commits are ground truth — `<status>` is a claim.

---

## Step 3 — Read Your Prompt

Read `{your_agent_folder}/prompt.md` and adopt that role.

---

## Step 4 — Understand Your Place in the Hierarchy

Read `org/ORG_CHART.md` — reporting chain, pod members, escalation path.

**Check daily log (Tier 1 and Tier 2 only):**
```
org/daily_log/{YYYY-MM-DD}.md
```

---

## Step 5 — Provide Oriented Summary

Brief statement of: what projects you're on, what's pending, what's blocked, what you're starting now. One paragraph. Do not ask for permission — state what you're doing.

Any deliverable produced by the ka_testing Docker runtime must be marked `[*runtime]` in REGISTRY.md, project JSON, and session logs.

---

## Visual Testing — Portal Frontend

Run `/frontend-dev` after any `portal/src/**` change to get a closed-loop screenshot + WCAG check cycle.

| Step | Action |
|------|--------|
| Start dev server | `cd portal && /c/Users/AndrewBerman/.bun/bin/bun run dev --port 5175` |
| Run | `/frontend-dev` — Playwright opens browser, screenshots, validates, auto-fixes |
| Constitutions | `portal/.frontend-dev/testing/` — per-page acceptance criteria (add one per new page) |
| Hook | PostToolUse auto-prompts after every `portal/src/**` edit |

**Mandatory for:** Any task order with a visual acceptance criterion. Any tooltip migration. Any new component with a chart or panel.
**Not needed for:** Gold script changes, TypeScript type-only changes, non-portal work.

Agents: applies to all DE and RD agents. Plugin installed at `~/.claude/plugins/frontend-dev/`.

---

## Compiler Tools — Trigger Table

**Model: you don't need to memorize the tools. Recognize your situation, find the row, run the command.**
Full catalog and deep docs: `org/modules/graph/comp-tools.yaml`. Cache stale? Run `comp-build` first.

### When you're ABOUT TO DO something

| Situation | Run | What to look for |
|-----------|-----|-----------------|
| Edit a gold script | `comp-pipescript io [script]` | **COLUMN GAPS** section — columns accessed but missing from load list (caught geo_drill + fee_earning_aua incidents). PORTAL CONSUMERS — platinum keys resolved to portal components. |
| Run a gold script | `comp-pipescript deployed [script]` | MATCH = runner has your code. STALE = upload needed first. |
| Run a gold script (ad-hoc) | `comp-pipescript postdeps [script]` | BLOCKING post-steps must run after. E.g. build_canonical_prices → inject_scoped_overrides (Apr-06 $22M phantom incident). |
| Write a task order | `comp-blast [node]` for every affected component/script | Downstream impact — who else is affected? Anything in another active TO? |
| Write a cross-domain TO | `comp-pipescript overlap A B` | Shared S3 artifacts between the two scripts — those go in `<cross_domain_coordination>`. |
| Modify portal component | `comp-transform schema-check [Component]` | MISSING fields = runtime undefined. NOTE fields = expected runtime aliases (not bugs). |
| Change a fetch/endpoint | `comp-routes trace [fn]` | Full CF → auth → S3 path. Use function name, not URL, in Git Bash. |
| Debug a 4xx / auth failure | `comp-routes behaviors` | **CUSTOM ERROR RESPONSES** section — CF may be intercepting 403 and returning HTML (caught Lambda auth-denial incident). |
| Add a boto3 call to Lambda | `comp-iam service [lambda-name]` | Any MISSING permissions flagged. Fix iam.tf before deploying. |
| Change iam.tf | `comp-iam gaps` | Full cross-reference of all Lambda/EC2 boto3 ops vs Terraform policies. |
| Query React Query keys | `comp-cache collisions` | Same key, multiple components = cache corruption risk. |

### When you're DONE with something

| Situation | Run | What to look for |
|-----------|-----|-----------------|
| Finished a gold run, about to signal AE | `comp-validate [script] --artifact /tmp/[artifact].json` | **All ERROR checks must pass (exit 0) before signaling.** WARN count: document in session log but does not block. Config: `data/black_diamond/scripts/gold/gold_validate_config.yaml`. |
| Committed a change | `comp-blast [changed fn]` | Blast radius unchanged — if new downstream nodes appeared, flag to COO. |
| Uploaded scripts to S3 | `comp-pipescript deployed [script]` | Confirm MATCH before triggering gold run. |
| Wiring a new portal component | `comp-transform fields [Component]` | All rendered fields have a TypeScript type — no silent undefineds. |

### Investigation tools (when you need to trace something)

| Question | Run |
|----------|-----|
| How does X connect to everything? | `comp-trace [X] --direction both` |
| What breaks if I change X? | `comp-blast [fn or artifact]` (use fn name, not script name) |
| What does this gold script read/write? | `comp-pipescript io [script]` |
| What feeds this script? | `comp-pipescript feeds [script]` |
| Who consumes this script's output? | `comp-pipescript consumers [script]` |
| Full page-to-gold-script trace | `comp-platinum page [ComponentName]` |
| S3 key → which portal component renders it? | `comp-platinum reverse [s3/key.json]` |
| Does this portal path have auth? | `comp-routes auth-map` |
| What fields does this component render? | `comp-transform fields [Component]` |
| PII exposure audit | `comp-pii audit` |

### Minimum required runs by role

| Role | Before starting work | Before signaling done |
|------|---------------------|----------------------|
| DS | `comp-pipescript io [script]` (includes COLUMN GAPS) + `comp-pipescript deployed` + `comp-pipescript postdeps` | `comp-validate [script] --artifact [file]` exits 0 |
| DE | `comp-transform schema-check [Component]` + `comp-blast [fn]` | `comp-blast [changed fn]` — no new downstream nodes |
| DT | `comp-pipescript io [script]` + `comp-routes behaviors` if CF involved | `comp-iam service [lambda]` if new boto3 call added |
| AE | `comp-pipescript deployed` + `comp-pipescript postdeps` | `comp-iam gaps` if iam.tf changed |
| COO (TO authoring) | `comp-blast [every affected node]` + `comp-pipescript overlap A B` for cross-domain pairs | All mandate `<expect>` values confirmed before issuing |

---

## Session Log — Required Sections

Full template: `org/ref/SESSION_LOG_STANDARD.md`

Every session log must include **`## Compiler Tools`** — table of tools run, results, what worked, what failed, any gap found. Append one line to `org/compiler-tools-log.md`.

Minimum compiler tools by role:

| Role | Minimum |
|------|---------|
| DS | `comp-pipescript io` for every gold script touched (includes COLUMN GAPS — zero extra work). `comp-pipescript deployed` before every gold run. `comp-pipescript postdeps` before any ad-hoc script run. `comp-validate <script> --artifact <file>` before signaling AE (if script has validate config). |
| DE | `comp-transform schema-check` before touching data props; `comp-blast` before deleting. `comp-routes behaviors` when debugging 4xx / auth failures (check custom_error_response). |
| DT | `comp-pipescript io` for every script deployed. `comp-iam service <lambda>` after adding any new boto3 call. `comp-routes behaviors` before CloudFront / Lambda@Edge changes. |
| AE | `comp-pipescript deployed` before every gold run trigger. `comp-pipescript postdeps` before any gold run (check required post-steps). `comp-iam gaps` after any iam.tf change. `comp-blast` on infra before changes. |
| RD | `comp-transform fields` for every component rendering data. |
| COO | `comp-pipescript overlap A B` before authoring cross-domain coordination blocks. `comp-blast` + `comp-routes` + `comp-cache` before decomposing PRDs into TOs. |

"Blank" and "N/A" are not acceptable. One sentence explaining why you didn't run is fine.

---

## Task Orders

Full template and filename convention: `org/ref/TASK_ORDER_PROTOCOL.md`

- Stored in the receiving agent's `task_orders/` folder
- `staged` = assigned, wait for GO | `pending` = active | `complete` = done (self-marked)
- Every task order must include `<compiler_tools_mandate>` — three-phase (before write, before commit, after commit)
- Every task order must include `<cross_domain_coordination>` — populated by COO/CTO at PRD decomposition using `comp-blast`; `<none/>` only if confirmed no shared files/S3 keys with other active TOs
- Every task order must include `<acceptance_criteria>` — machine-checkable output validation, not "code runs"
- Session log with Compiler Tools section is an explicit deliverable on every task order
- A TO with no compiler check logged is NOT accepted as complete — see `org/standards/TO_COMPILER_GATE.md`

**COO/CTO parallel wave protocol:**
Before writing any TOs for a parallelized wave: run `comp-blast` on every affected component/script. Any node appearing in 2+ TOs' blast radii is a CROSS-DOMAIN resource — flag it in the PRD and in each relevant TO's `<cross_domain_coordination>` block. Agents must MCP-message each other before committing to cross-domain files.

---

## Commit Identity (Non-Negotiable)

```bash
git commit --only --author="{serial} <{serial}@opal.agent>" -m "message" -- file1 file2 file3
```
Author = the agent. Committer = Andrew. Only alphanumeric, `.`, `_`, `@` in author fields.

**Use `--only` (or `-o`) always.** This creates a temporary index from the listed paths only, bypassing the shared staging area entirely. Other agents' staged files are never touched.

## Commit Scope Discipline (Non-Negotiable)

**Commit ONLY the files your task order told you to touch. Never sweep the working tree.**

- **BANNED:** `git add -A`, `git add .`, `git add --all`, `git commit -a`, `git commit --all`, `git add <files>` followed by a bare `git commit` — any pattern that uses the shared index.
- **REQUIRED:** `git commit --only -- <file1> <file2> ...` — list every path explicitly after `--`. No prior `git add` needed; `--only` reads from the working tree directly.
- **If you see dirty files outside your scope:** leave them alone. Do not stash, do not commit "to clean up", do not include them "while you're at it". Another agent is probably working on them right now.
- **One task order = one logical commit scope.** If your work spans multiple task orders, make multiple commits, each scoped to its own TO.

**Why `--only` is mandatory:** During hectic multi-agent MCP sessions, multiple agents have dirty working trees and staged files at the same time. A bare `git commit` (even after `git add <specific files>`) commits the entire shared index — sweeping in any files another agent staged in the window between your `git add` and your `git commit`. This happened twice in session 26 (2026-04-14): COO's staged files were committed under AE and DS author lines. `git commit --only -- <files>` bypasses the shared index entirely — the race condition is structurally impossible.

The only exception is a commit whose explicit purpose is a bulk cleanup (rare, and must be called out in the commit message).

---

## Abilities by Role

| Role | Commit | Push | Deploy AWS | Session Logs |
|------|--------|------|------------|--------------|
| RD | Own page only | No | No | Encouraged |
| DE | Any portal path | No | No | **MANDATORY** |
| DS | Edit + commit locally | No | No | Encouraged |
| DT | Infra | **Yes** (CLOUD + DEV) | **Yes** | Encouraged |
| AE | Infra + pipeline | **Yes** (CLOUD) | **Yes** | Encouraged |
| SA | Docs only | No | No | Encouraged |

DTs own all pushes and are the QA gate before anything reaches remote.

---

## Core Documents (Tier 2+)

Update your core document when you make a structural change (new resource, contract change, removal). Update in the same commit as the code change.

| Role | Document | Location |
|------|----------|----------|
| RD | `page_inventory.xml` | `{agent_folder}/deliverables/` |
| DE | `pod_inventory.xml` | `{agent_folder}/deliverables/` |
| DS | `data_contract.xml` | `{agent_folder}/deliverables/` |
| DT | `deployment_map.xml` | `{agent_folder}/deliverables/` |
| AE | `pipeline_inventory.xml` | `{agent_folder}/deliverables/` |
| SA | `architecture_brief.xml` | `{agent_folder}/deliverables/` |

Do not edit another agent's core document. If your change makes theirs stale, note it in your log and issue them a task order.

---

## Thread Participation

- Write only your own message file (`messages/{NNN}.md`)
- Do not modify THREAD.json, TURN.json, or other agents' messages
- Set signal in YAML frontmatter: `continue` | `converge` | `escalate`
- Last turn signal MUST be `converge`
- SA/DE run thread scripts directly via Bash — do not ask Andrew

---

## Deployment Reference Docs

| Doc | When required |
|-----|--------------|
| `org/ref/LAMBDA_DEPLOYMENT_PROTOCOL.md` | Any Lambda write, deploy, or layer work |
| `org/ref/EC2_DEPLOYMENT_PROTOCOL.md` | Any EC2 service code or infrastructure work |
| `org/ref/EC2_CODE_DEPLOYMENT_STANDARD.md` | Any code running on EC2 |
| `org/ref/TERRAFORM_PIPELINE_STRATEGY.md` | Any Terraform changes |
| `infra/aws/lambda/ci/lambda-source-map.json` | Before touching any Lambda function |
| `infra/aws/ec2/EC2_MANIFEST.json` | Before touching any EC2 service |

---

## Quick Reference

| Thing | Value |
|-------|-------|
| Working branch | `CLOUD` (parent repo) / `DEV` (portal submodule) |
| Terraform binary | `.tools/terraform.exe` |
| Bun | `/c/Users/AndrewBerman/.bun/bin/bun` |
| Git Bash path fix | `export MSYS_NO_PATHCONV=1` before commands with `/` paths |
| Times to Andrew | US Eastern only (never UTC) |
| MCP server | `org/mcp/server.py` — `opal-agent-comms` |
| Broker | Auto-launched by `register_agent`, port 7800 |
| Monitor | `python org/mcp/monitor.py` (supports `--pod N`, `--project CODE`) |
| Compiler tools log | `org/compiler-tools-log.md` — append after every session |
