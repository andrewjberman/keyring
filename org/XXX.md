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

## Compiler Tools — Run Before Tracing Anything Manually

| Tool | Command | Use when |
|------|---------|----------|
| `comp-pipescript io` | `comp-pipescript io D_00` | What a gold script reads/writes |
| `comp-pipescript consumers` | `comp-pipescript consumers D_00` | What consumes a script's output |
| `comp-blast` | `comp-blast D_00.portal_aggregates.py` | Blast radius before any change |
| `comp-trace` | `comp-trace artifact_name --direction both` | Cross-layer dependency path |
| `comp-platinum` | `comp-platinum reverse platinum/firm/dashboard.json` | S3 key → routes → components |
| `comp-transform` | `comp-transform schema-check ClientsTab` | Component field/type audit |
| `comp-routes` | `comp-routes trace getEmployeeLeaderboard` | Full serving path (use fn name, not URL path in Git Bash) |
| `comp-cache` | `comp-cache collisions` | React Query key collisions |
| `comp-pii` | `comp-pii audit` | PII field detection |

Full reference: `org/modules/graph/comp-tools.yaml`
Cache stale? Run `comp-build` first.

---

## Session Log — Required Sections

Full template: `org/ref/SESSION_LOG_STANDARD.md`

Every session log must include **`## Compiler Tools`** — table of tools run, results, what worked, what failed, any gap found. Append one line to `org/compiler-tools-log.md`.

Minimum compiler tools by role:

| Role | Minimum |
|------|---------|
| DS | `comp-pipescript io` for every gold script touched |
| DE | `comp-transform schema-check` before touching data props; `comp-blast` before deleting |
| DT/AE | `comp-pipescript io` for every script deployed |
| RD | `comp-transform fields` for every component rendering data |

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
git commit --author="{serial} <{serial}@opal.agent>" -m "message"
```
Author = the agent. Committer = Andrew. Only alphanumeric, `.`, `_`, `@` in author fields.

## Commit Scope Discipline (Non-Negotiable)

**Commit ONLY the files your task order told you to touch. Never sweep the working tree.**

- **BANNED:** `git add -A`, `git add .`, `git add --all`, `git commit -a`, `git commit --all`, any pattern that stages files you did not deliberately choose.
- **REQUIRED:** `git add <exact/path/to/file1> <exact/path/to/file2>` — list every path by name.
- **Before every commit:** run `git status` and visually confirm each staged file belongs to your task order. If a file you didn't touch is staged, unstage it (`git restore --staged <file>`).
- **If you see dirty files outside your scope:** leave them alone. Do not stash, do not commit "to clean up", do not include them "while you're at it". Another agent is probably working on them right now.
- **One task order = one logical commit scope.** If your work spans multiple task orders, make multiple commits, each scoped to its own TO.

**Why this rule exists:** During hectic multi-agent MCP sessions, several agents have dirty working trees at the same time. An agent that runs `git add -A` sweeps up other agents' in-flight work into their own commit — the author line lies, the TO attribution is wrong, and downstream reviewers cannot tell who changed what. This has corrupted the audit trail more than once. Selective staging is mandatory, not a preference.

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
