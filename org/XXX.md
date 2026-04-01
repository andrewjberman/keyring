# AGENT START HERE — Opal Capital Hierarchical Agent System

---

# ================================================================
# MANDATORY MCP STARTUP PROTOCOL — DO THIS BEFORE ANYTHING ELSE
# ================================================================
#
#  Skipping ANY of these four steps makes you invisible to the org.
#  Other agents cannot see you, message you, or send you GO signals.
#  Andrew cannot confirm you received work. You will miss activations.
#
#  Execute in this exact order, every session, no exceptions:
#
#  STEP A — Register (MCP tool call):
#    register_agent("{your_serial}", summary="Starting session")
#
#  STEP B — Check inbox for messages you missed while offline (synchronous):
#    bash org/mcp/check-inbox.sh {your_serial}
#    --> Prints all pending messages, marks them read, exits.
#    --> This catches GO signals sent between sessions.
#    --> inbox-watch.sh CANNOT catch these -- it only sees new arrivals.
#
#  STEP C — Start heartbeat poller (run_in_background: true, NO &):
#    python org/mcp/agent-poller.py {your_serial}
#    --> Writes last_seen_epoch every 2s. Without this you go STALE/DEAD.
#
#  STEP D — Start inbox watcher (run_in_background: true, NO &):
#    bash org/mcp/inbox-watch.sh {your_serial}
#    --> Polls every 5s. Exits on message delivery.
#    --> Exit fires a <task-notification> that interrupts you.
#    --> Re-launch it after EVERY notification.
#
#  DO NOT USE & WITH run_in_background. The & forks and the shell exits,
#  which may kill the child process. run_in_background handles backgrounding.
#
#  WHY FOUR TOOLS INSTEAD OF ONE:
#    register_agent  -- announces you, enables push; misses offline messages
#    check-inbox.sh  -- catches offline messages; misses future arrivals
#    agent-poller.py -- keeps you LIVE; does not touch inbox
#    inbox-watch.sh  -- real-time interrupt; misses pre-start arrivals
#    Each covers the failure mode of the others. All four are required.
#
# ================================================================

---

**You are an agent in the Opal Capital hierarchical organization. Follow these steps IN ORDER before doing anything else.**

**DO NOT SKIP STEP 1b.** After identifying yourself (Step 1), you MUST immediately register with MCP, start your background heartbeat poller (`agent-poller.py`), and start your inbox watcher (`inbox-watch.sh`). These are mandatory background processes. No exceptions. No asking. Just run them.

---

## CRITICAL: BANNED AGENTS - READ THIS FIRST

**ABSOLUTELY DO NOT USE THESE AGENTS - THEY PRODUCE FABRICATED INFORMATION:**

### BANNED: Explore Agent
- **Status:** COMPLETELY UNRELIABLE - Produces false information
- **What to do instead:** Use Glob, Grep, and Read tools directly to examine files

### BANNED: Task Agent
- **Status:** UNRELIABLE - Produces inconsistent and poor results
- **What to do instead:** Do the work directly yourself using standard tools

---

## ANTI-PATTERNS (NEVER DO THESE)

- **NEVER write code directly on EC2 instances** - Repo -> S3 -> EC2 pulls from S3 -> executes. Even diagnostic scripts.
- **NEVER push scripts or edits to the EC2 Docker image** - Script fixes happen in the local repo only.
- **Use Edit tool instead of `sed`** for file editing.
- **Use Write tool instead of `cat` with heredocs**.
- **Use Read/Edit/Write tools directly** instead of chaining bash commands for file operations.

---

## Git Workflow

**This workspace has two branching models:**

1. **Parent repo (ajb_workspace):** Single working branch `CLOUD`. All agent work happens here.
2. **Portal submodule (`portal/`):** Uses `DEV` -> `PROD` -> Server deployment workflow.

**Branch Definitions:**
- **`CLOUD`** (parent repo) = The one working branch for all infrastructure, Lambda, data, and docs work
- **`DEV`** (portal submodule only) = Portal development branch — all agent commits go here
- **`PROD`** (portal submodule only) = Portal production branch — **AGENTS NEVER COMMIT HERE**
- **`main`** = NOT USED anywhere. Ignore completely.

**PROD IS STRICTLY MERGE-ONLY:**
`PROD` only ever receives merge-forwards from `DEV`, issued explicitly by a DevOps team member (DT agent or Andrew). Agents never commit directly to `PROD`, never cherry-pick to `PROD`, and never push directly to `PROD` for any reason, including hotfixes. All work — including urgent bug fixes — goes to `DEV` first. A DT agent or Andrew merges to `PROD` when authorized.

Violating this rule corrupts the DEV→PROD audit trail and makes deployment history unreliable.

**No Pull Requests:** This is a single-developer workflow. Use direct push.

---

## MANDATORY: Deployment Reference Docs

All deployment reference docs are included in this org structure at `org/ref/`:

| Doc | Location | When You Need It |
|-----|----------|-----------------|
| Lambda Deployment Protocol | `org/ref/LAMBDA_DEPLOYMENT_PROTOCOL.md` | Any Lambda function work |
| EC2 Deployment Protocol | `org/ref/EC2_DEPLOYMENT_PROTOCOL.md` | Any EC2 service work |
| EC2 Code Deployment Standard | `org/ref/EC2_CODE_DEPLOYMENT_STANDARD.md` | Any code running on EC2 |
| Terraform Pipeline Strategy | `org/ref/TERRAFORM_PIPELINE_STRATEGY.md` | Any Terraform changes |
| CloudFront Deployment Checklist | `org/ref/deployment/cloudfront_deployment_checklist.md` | CloudFront changes |

**Base persona prompts** are at `org/ref/prompts/{role}.md`.

---

## Critical Deployment Rules (Non-Negotiable)

1. **Terraform is the only Lambda deployment mechanism.** Never use `aws lambda update-function-code`, `deploy.sh`, or the AWS console.
2. **Commit before apply.** Write code -> Terraform -> update source map -> git commit -> plan -> apply -> verify 0-diff -> tag -> push.
3. **Dependencies go in Lambda Layers.** No `pip install -t .` into Lambda source dirs.
4. **Update the source map.** Every Lambda must have an entry in `infra/aws/lambda/ci/lambda-source-map.json`.
5. **Run `record-terraform-deploy.sh` after 0-diff.** `bash infra/aws/lambda/ci/record-terraform-deploy.sh {pipeline} {pipeline}-v{X.Y.Z}` — updates `CHANGELOG.json`. Commit the result before tagging. Skipping this breaks COO audit visibility.
6. **Tag after deploy.** After 0-diff and `record-terraform-deploy.sh`: `git tag -a {pipeline}-v{X.Y.Z} -m "description"` and `git push --follow-tags`.
7. **Always use `safe-ec2-deploy.sh`.** Never run service-specific deploy scripts directly.
8. **EC2_MANIFEST.json is the source of truth.** Every EC2 service must be registered.
9. **No emojis in code.** Never use emoji characters in production code, debug logs, or any code that runs on AWS.

---

## Step 1: Identify Yourself

Your agent folder contains your identity. Read your folder's files:
1. `README.md` — Your ID, role, responsibilities, reporting chain
2. `prompt.md` — Your scoped persona prompt

Your folder location follows the pattern:
```
org/{tier_folder}/{agent_id}/
```

Tier folders:
- `tier1_exec/` — SA agents (Tier 1)
- `tier2_senior/` — DE, DT, DS, AE agents (Tier 2)
- `tier3_junior/` — RD agents (Tier 3)

---

## Step 1b: Register with MCP, Check Inbox, and Start Background Processes

**Do this NOW. Do not ask. Do not confirm. Just execute all three:**

**A. Register:**
```
register_agent({your_serial}, summary="Starting session")
```
Announces you to the org via MCP + broker. Until you call this, `get_org_summary`
shows you as DEAD and `send_message` cannot push notifications to you.

**B. Check inbox for offline messages (synchronous, not backgrounded):**
```bash
bash org/mcp/check-inbox.sh {your_serial}
```
Run this synchronously (no `run_in_background`). It makes one pass over your inbox
directory, prints all pending `.md` files, marks them read, and exits.

**This step is not optional.** `inbox-watch.sh` only catches messages that arrive
*after* it starts. Any GO signal, status update, or blocker sent while you were
offline is invisible to the watcher. `check-inbox.sh` is the only way to catch it.

**C. Start the background heartbeat poller:**
```bash
python org/mcp/agent-poller.py {your_serial}
```
Run via the Bash tool with `run_in_background: true` and **no `&`**. Updates
`last_seen_epoch` in `org/mcp/liveness.json` every 2 seconds. Without this you go
STALE after 2 minutes and DEAD after 10 -- other agents stop routing work to you.

**D. Start the background inbox watcher:**
```bash
bash org/mcp/inbox-watch.sh {your_serial}
```
Run via the Bash tool with `run_in_background: true` and **no `&`**. Polls your inbox
every 5 seconds. When a message arrives, prints ALL pending messages and **EXITS**.
The exit fires a `<task-notification>` in your conversation that interrupts you.

**Critical: re-launch after every notification.** When you receive a
`<task-notification>` from inbox-watch.sh:
1. Read the output file to see the message(s)
2. Act on them (execute task orders, respond, etc.)
3. Re-launch: `bash org/mcp/inbox-watch.sh {your_serial}` with `run_in_background: true`

The watcher exits on delivery because that is the ONLY way to interrupt an idle agent.
A persistent background script produces output nobody reads. An exiting task fires a
notification that forces a new conversation turn.

**Why `run_in_background: true` but NO `&`:**
The `&` operator forks the process into the shell's background and then the shell exits,
which may kill or orphan the child. `run_in_background: true` is Claude Code's native
backgrounding -- it manages the process lifecycle correctly.

**How the full system fits together:**

| Tool | Purpose | What it CANNOT do |
|------|---------|-------------------|
| `register_agent` | Announces you, enables push delivery | Does not retrieve offline messages |
| `check-inbox.sh` | Sweeps inbox for messages you missed offline | Does not catch future arrivals |
| `agent-poller.py` | Keeps `last_seen_epoch` current (stay LIVE) | Does not touch inbox at all |
| `inbox-watch.sh` | Real-time interrupt on new message arrival | Does not see pre-start messages |
| `mcp check_inbox` | Broker-side view; works without filesystem | Requires broker to be running |

Each tool covers the failure mode of the others. All four are required every session.

**E. Act on what you find:**

- **GO message in inbox** → Read the referenced task order, flip `<status>` from `staged` to `pending`, and begin execution immediately. The GO message IS your authorization. Do NOT ask Andrew for permission. Skip Steps 2-2b if the GO message gives you clear scope.
- **Inbox empty** → Proceed to Step 2.

Andrew runs agents in parallel across terminal windows. COO sends GO messages to
activate task orders. If you don't register, poll, and check inbox, you miss
the activation signal and force Andrew to manually relay the message.

---

## Step 2: Read Your Recent Logs (HIGHEST PRIORITY)

**THIS IS THE MOST IMPORTANT STEP.**

1. Check your logs folder: `{your_agent_folder}/logs/`
2. Find the most recent date folder
3. Read ALL logs from that date
4. Understand what you were working on, decisions made, blockers, next steps

**Why YOUR logs are CRITICAL:**
- You are continuing YOUR previous work - not starting fresh
- Your logs contain YOUR decisions, blockers, next steps
- Without this, you WILL lose context and repeat work

---

## Step 2b: Ground Truth Reconciliation (WRITE OPERATION)

**You are the startup OS process.** Your job is to reconcile declared state (task order
statuses, project JSON phases, registry rows) against actual state (agent logs, git
commits, deployed artifacts). Every discrepancy you find MUST be corrected immediately
using the Edit tool — before you present your oriented summary.

The outputs of this step are:
1. **All status documents updated to reflect reality** — task orders, project JSONs, registry
2. **A clear picture of what work is actually pending** — which agents, which task orders, what remains
3. **Uncommitted changes identified** — what exists locally but hasn't been pushed

### MANDATORY FIRST ACTION: MCP Server Must Be Running

The `opal-agent-comms` MCP server is the backbone of inter-agent communication.
**Before doing ANYTHING else in Step 2b, you must confirm the server is connected
and start it yourself if it is not.**

**Step A — Check if MCP tools are available:**

Use `ToolSearch` to look for `get_agent_status`. If the tool appears, the server
is connected — skip to Step B.

**Step B — If MCP tools are NOT available, start the server yourself:**

```bash
# Test that the server starts without errors (will hang on stdin — that is correct)
timeout 3 python org/mcp/server.py 2>&1 || true
```

If the test produces import errors, fix them (likely `pip install mcp`).
If the test produces no errors (clean exit after timeout), the server binary is healthy
but Claude Code has not connected to it. Tell Andrew:

> "The `opal-agent-comms` MCP server is healthy but not connected to this session.
> Run `/mcp` to check its status, or restart Claude Code so it reads `.mcp.json`
> on startup and prompts you to approve it."

**Do NOT proceed past this point until the MCP tools are available.** No fallback
to manual file reads. The MCP server exists to prevent agents from missing cross-agent
state — manual reads are error-prone, miss inbox messages, skip fuzzy serial resolution,
and produce inconsistent project queries. The correct action is to fix the connection,
not to work around it.

**Step C — Verify connectivity with a live call:**

Once MCP tools are available, run one test call to confirm end-to-end:
```
get_agent_status({your_serial})
```
If this returns your status, the server is fully operational. Proceed to Step D.

**Step D — Register as live (MANDATORY for all agents):**

Call `register_agent` with your serial and a brief summary of what you're about to work on.
This is NOT optional. It does three things:

1. **Makes you visible** to other agents via `get_live_agents` — they can see you're active
2. **Starts the broker** if it's not running — the broker routes messages between concurrent sessions
3. **Enables instant message delivery** — messages sent to you while you're live arrive via channel push instead of waiting for you to poll your inbox

```
register_agent({your_serial}, summary="Starting session: ground truth reconciliation for ADVI_PRICES")
```

Update your summary as your focus changes during the session:
```
set_summary({your_serial}, summary="Running gold layer, waiting on COO review")
```

Heartbeat and inbox polling are handled by the CronCreate loop you set up in Step 1b.
You do NOT need to manually call heartbeat — the cron job does it automatically.

Use these MCP tools for all cross-agent queries — do NOT ask Andrew to relay status questions.

### Protocol

**1. Check your own task orders**

Use `list_task_orders({your_serial})` to see all your pending and complete task orders.
For each PENDING task order: is the work actually done? If yes, edit the `<status>` field
from `pending` to `complete` immediately.

**STAGED task orders:** If a task order has `<status>staged</status>`, it is assigned to
you and scoped, but you MUST NOT begin work on it UNLESS you have a GO message in your
inbox from COO or CTO authorizing it. `staged` means "COO will send you a go message
when it is time to start." When you receive a go message (via `check_inbox` or broker
push), flip the status to `pending` and begin immediately — do NOT ask Andrew for
confirmation. The GO message IS the authorization.

**2. Audit all agents on active projects**

This is the core of the reconciliation. The purpose is to identify every agent who has
a pending task order and determine whether the work is actually done, actually pending,
or ambiguous.

For each active project in REGISTRY.md, run:

```
query_project({project_code})
```

This returns every task order across every agent for that project. For each **pending**
task order, check the assigned agent:

```
get_agent_status({agent_serial})
```

Then verify actual completion by examining evidence — not just the `<status>` field:
- **Their latest logs** — does the log describe the deliverable as done?
- **Their commits** — `git log --author="{agent_serial}" --oneline -10`
- **Deployed artifacts** — git tags (`git tag -l "{pipeline}-v*" | sort -V | tail -5`),
  S3 objects, terraform state
- **Uncommitted local changes** — `git diff --name-only` for files in their scope

The `<status>` field is a claim, not proof. An agent may have completed the work but
not marked their task order. Conversely, an agent may have marked `complete` without
the work actually being deployed or committed.

**For each pending task order, classify it:**

| Evidence | Classification | Action |
|----------|---------------|--------|
| Logs + commits confirm work is deployed/delivered | **Done** | Edit `<status>` to `complete`. Update project JSON phase. |
| Logs show work in progress, partial commits exist | **In flight** | Note in summary. No status change. |
| No logs, no commits, no evidence of activity | **Not started** | Note in summary as AMBIGUOUS. |
| Agent marked complete but no supporting evidence | **Unverified** | Flag in summary. Do NOT trust without evidence. |
| Status is `staged` — assigned but no go received | **Held** | Do NOT begin. Wait for COO go message. |

**3. Check upstream — agents who issued work to you**

For each PENDING task order in your `task_orders/` folder, check the `<issued_by>` agent:

```
get_agent_status({issuing_agent_serial})
```

Look for: did scope change? Did they issue new dependencies? Are they aware of your current blockers?

**4. Check dependencies — task orders you're waiting on**

For each `<dependency>` in your pending task orders, check the blocking agent:

```
list_task_orders({blocking_agent_serial}, project={project_code})
```

If the dependency task order is now `complete`, update the `<dependency status="">` field
in YOUR task order from `pending` to `complete`. If the dependency is delivered AND your
task order status is `pending`, proceed with your work. If your task order is `staged`,
do NOT begin — wait for a go message from COO even if dependencies are met.

**5. Update all status documents (Tier 1 and Tier 2 only)**

After steps 1-4, you have the actual state of every active project. Now reconcile
ALL status documents — not just your own, but every document that other agents or
Andrew will read on their next session.

**Project-level documents:**
- **Project JSON `phase`** — rewrite to match what you found (which TOs are done, which are pending, what milestone the project is actually at)
- **Project JSON `blocking`** — update to reflect actual current blockers, not historical ones
- **Project JSON `status`** — if ALL task orders are complete and deliverables verified, set to `"complete"`
- **REGISTRY.md** — update the Phase and Blocking columns to match the project JSON

**Exec-level documents (CTO responsibility):**
- **CTO `prompt.md` dashboard** — update Active Projects, Recently Completed, Pipeline Tags
- **COO `prompt.md` dashboard** — update the Pod Delivery Dashboard (Active Projects table,
  Pod status tables, Shared Services table) and Operational Health Checks (pipeline tags).
  The COO boots from these tables. If they are stale, the COO's first session starts with
  wrong assumptions about who is doing what. The CTO reconciliation must bring COO documents
  to parity so the next COO session inherits correct state.

### Rules

- **Write, don't report.** Every stale document found MUST be corrected before presenting
  your oriented summary. "Task order still marked pending" in your summary = you failed this step.
- **Logs and commits are ground truth.** The `<status>` field in a task order is a claim,
  not proof. Always verify against the agent's logs, git commits, and deployed artifacts
  before deciding whether work is actually done.
- **Identify uncommitted work.** Run `git status` and `git diff --name-only` to find
  changes that exist locally but haven't been committed or pushed. This is critical —
  unpushed work is invisible to other agents and to production.
- **Skip gracefully.** If you have no active projects and no pending task orders, skip this step.
- **Note gaps.** If a project-assigned agent has no logs or no recent entries, flag it as
  AMBIGUOUS in your Step 5 orientation summary — do not assume they are idle.

### MCP Tools Reference

| Tool | When to Use |
|------|-------------|
| `register_agent(serial, summary?)` | **MANDATORY on startup.** Registers you as live, starts broker, enables push messaging. |
| `heartbeat(serial, summary?)` | Handled by CronCreate loop from Step 1b — do not call manually |
| `set_summary(serial, summary)` | Update your work description visible to all agents |
| `get_live_agents(pod?)` | See who's currently online. Optional pod filter (e.g., pod="4") |
| `get_agent_status(serial)` | Quick check on any agent — liveness, summary, latest log, pending TOs, blockers |
| `read_agent_latest_log(serial)` | Full log content when you need completion evidence |
| `list_task_orders(serial, status?, project?)` | Check specific task order statuses |
| `query_project(code)` | See all task orders across all agents for a project |
| `send_message(from, to, subject, body)` | Send message to another agent — delivered via broker + channel push if they're live |
| `check_inbox(serial)` | Read messages left for you by other agents |
| `list_agents(tier?)` | All agents in org with liveness badges |
| `get_org_summary()` | Org-wide view of live agents, active projects, pending work |

### What this catches

- Task order marked `pending` but the work is actually done (agent forgot to update status)
- Task order marked `complete` but no commits or deploys support it (false completion)
- Work completed locally but never committed or pushed (invisible to production and other agents)
- Project JSON phase/blocking stale relative to actual agent progress
- Agent assigned to a project with no logs or activity (silent failure)
- Dependencies resolved but downstream agent hasn't noticed and is still waiting

Without this reconciliation on every startup, these gaps compound across sessions
until a human runs an explicit audit. The CTO startup IS that audit.

---

## Long-Running Operation Polling Protocol (SSM, gold runs, deploys)

When you dispatch a long-running operation (SSM command, gold layer run, deploy script,
any async process), you MUST poll for completion. Do not sleep. Do not wait silently.
Do not ask Andrew to check for you.

### Structure

The polling loop interleaves two operations:

1. **Status check** — poll the async operation (e.g., `aws ssm get-command-invocation`)
2. **MCP heartbeat + inbox check** — every other iteration to stay LIVE and receive messages

### Cadence

- Poll the operation every tool call cycle (~15-30s natural latency)
- Heartbeat every 2nd or 3rd poll to stay within the 2-minute LIVE window
- **No `sleep` commands** — the natural latency of tool calls IS the pacing
- Update your summary with current status: `set_summary(serial, "Gold run: 45 min elapsed, script 06b running")`

### Exit Conditions (SSM example)

| SSM Status | Action |
|------------|--------|
| `InProgress` | Continue polling |
| `Success` | Proceed to post-run validation |
| `Failed` | Pull `StandardOutputContent` + `StandardErrorContent`, diagnose |
| `Cancelled` | Report to COO via `send_message`, do not retry without instruction |
| `TimedOut` | Check if partial output was written to S3 log path, report |

### Post-Completion

On **Success**: immediately run validation checks (S3 ls for artifacts, download
spot-check files, cross-validate metrics). Report completion to COO via `send_message`.

On **Failed**: pull the last 500 lines of output:
```bash
aws ssm get-command-invocation --command-id "{id}" --instance-id "{id}" \
  --query '{Status:Status,StandardOutputContent:StandardOutputContent,StandardErrorContent:StandardErrorContent}' \
  --output json
```
SSM truncates output at 24KB. If truncated, pull the full log from the S3 path
embedded in the SSM command.

### SSM Command Template (gold layer runs)

```bash
cd /home/ubuntu/gold-layer/scripts \
  && aws s3 sync s3://opal-data-bd/code/gold/ . \
  && chmod +x *.sh *.py 2>/dev/null; \
  ./run_gold_layer.sh full 2>&1 \
  | tee /var/log/gold-full-run.log \
  && aws s3 cp /var/log/gold-full-run.log \
     s3://opal-data-bd/logs/gold-layer/gold_full_{task_slug}_$(date +%Y%m%d_%H%M%S).log
```

Key design choices:
- **S3 sync first** — pulls latest code from S3 artifact store (never runs stale code)
- **tee** — writes to local log AND stdout (SSM captures stdout)
- **S3 upload at end** — full log persisted even if SSM truncates
- **`$(date)` in S3 key** — prevents overwriting previous run logs
- **Timeout 7200s** (2 hours) — generous ceiling for full runs

### Why No Sleep

`sleep` creates dead time where you are unresponsive to inbox messages and invisible
to the org. The natural round-trip of tool calls (Bash for SSM check, MCP for heartbeat)
provides ~15-30s spacing automatically. This is sufficient for operations that take
minutes to hours.

---

## Step 3: Read Your Prompt

Read `{your_agent_folder}/prompt.md` and adopt that role. You should now:
- Think like that specialist
- Follow their principles and methodology
- Stay within your scoped responsibility
- Escalate to your reporting chain when needed

---

## Step 4: Understand Your Place in the Hierarchy

Read `org/ORG_CHART.md` to understand:
- Who you report to
- Who reports to you (if any)
- Your pod members
- Shared services available to you

**Escalation rules:**
- RD agents escalate to their pod's DE
- DE/DT/DS agents escalate to CTO (technical) or COO (resource/scheduling)
- AE agents escalate to CTO (technical) or COO (resource/scheduling)

---

## Step 4b: Check Daily Collaborative Log (Tier 1 and Tier 2 only)

If you are a Tier 1 or Tier 2 agent, check today's daily log:
```
org/daily_log/YYYY-MM-DD.md
```

This shows what other agents are working on, pushing, or deploying today. Before pushing, deploying, or committing to shared paths, add your own entry. See `org/CROSS_POD_COORDINATION.md` for the full daily log protocol.

---

## Step 5: Provide Oriented Summary

Give the user a brief summary. By this point, all stale documents MUST already be
corrected (Step 2b). Your summary should say "corrected N documents" — not "N documents
need correction."

```
Agent: [ID and name]
Role: [role type]
Pod: [pod name, if applicable]
Reports to: [manager agent ID]
Current priority: [from logs if any]
Key context: [from recent logs]
Corrections made: [N task orders / project files corrected — or "none needed"]
Downstream check: [what first-order agents did after your last handoff — or "no pending handoffs"]

Ready to work. What would you like me to focus on?
```

---

## Runtime Attribution Rule (MANDATORY)

Any project, task order, or deliverable where code was produced by the
ka_testing Docker runtime (org/ka_testing) MUST be marked with `[*runtime]`
in REGISTRY.md, project JSON phase fields, and session log Files Modified tables.

**Format:**
- REGISTRY.md Phase column: `Phase N: ... [*runtime on WS1, WS3]`
- Session log Files Modified: `path/to/file.py | Changed | Yes — `sha` [*runtime]`
- Project JSON `phase` field: append `[*runtime: WS1 DS, WS7 RD]`

**Why this matters:** Runtime agents produce code that is often partially
correct but may contain structural defects (duplicate bodies, syntax errors,
stub implementations, file overwrites). The asterisk is not a quality judgment —
it is an audit trail marker. It means the deliverable was produced autonomously
and must be verified before treating as human-reviewed production quality.

Performance baseline as of 2026-03-19:
- CLSUNI test: ~36% of final committed code unedited from runtime
- CLSPT2 test: ~67% of final committed code unedited from runtime

Runtime config and results live at: `org/ka_testing/`, `.runtime/results/`

---

## Session Logging Protocol

### Log Location

Logs go in YOUR agent folder:
```
{your_agent_folder}/logs/YYYY-MM-DD/descriptive_thesis_of_work.md
```

**Example:** `org/tier3_junior/0.1.1_RD_MarketPerformance/logs/2026-03-02/chart_component_refactor.md`

### Base Log Template

```markdown
# [Thesis Title] — [Agent ID]

**Date:** YYYY-MM-DD
**Start Time:** HH:MM
**End Time:** HH:MM

## Objective

[1-3 sentences: what was set out to accomplish and why. Name the feature, bug, or investigation.]

---

## Work Completed

[Organize into numbered sections for distinct pieces of work. Use tables where data is structured.]

### 1. [First work unit]

[Narrative + table or code block as appropriate. Be specific: function names, S3 paths, commit hashes, actual output.]

### 2. [Second work unit]

...

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| [What was decided] | [Why — include alternatives considered if significant] |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `path/to/file.py` | What changed | Yes — `abc1234` / No — local only |

---

## Blockers

- [Blocker description, impact, and who can unblock it]

**Before writing any blocker:** check the blocking agent's directory first.
See **Blocker Verification Protocol** below.

---

## Current State

> **Primary handoff point. Write as if briefing someone with zero prior context.**

**Status:** IN PROGRESS | COMPLETE | BLOCKED
**Active branch:** `CLOUD`

[2-4 dense sentences. Name specific files, functions, AWS resource names, commit hashes, S3 paths. Avoid vague summaries.]

---

## Next Steps

> Ordered list. Top-to-bottom execution order. Use the full agent serial in brackets for every
> cross-agent handoff. The serial format is what Step 2b uses to resolve the agent's log folder.
> Use `[role name]` only for Andrew or external actors with no agent folder.

1. **[Action verb] [specific thing]** — [why / what done looks like]
2. **[0.4.0_DE_ClientPlatform] [specific action]** — [cross-agent handoff]
3. **[0.4.0_DT_ClientPlatform] [specific action]** — [cross-agent handoff]

**Files to touch next:**
- `path/to/file.py` — [what change is needed]

**Do NOT:**
- [Specific anti-pattern to avoid — name the wrong command, wrong path, wrong approach]
- [Another gotcha]
```

---

### Role-Specific Log Additions

Each role extends the base template with additional sections suited to their work.

**DE (Dashboard Engineer) — add to header and Files Modified:**
```markdown
**Portal DEV commits:** `abc1234` → `def5678` → `ghi9012`
**Workspace CLOUD commit:** `jkl3456`
```
Files Modified table must include the commit hash in the Committed column. When work breaks something, embed a `## Postmortem` section between Work Completed and Decisions Made with: Root Cause, a table of shape/contract mismatches, and Resolution tracking.

**DS (Data Scientist) — add Briefs Written section before Current State:**
```markdown
## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| DevOps deploy instructions | `docs/briefs/devops-brief-{feature}.md` | DevOps |
| Data contract for DE | `docs/briefs/dashboard-engineer-{feature}-data-contract.md` | Dashboard Engineer |
| Investigation reference | `docs/briefs/data-scientist-{topic}-investigation.md` | Reference |
```
DS briefs are the formal cross-agent handoff artifact. Write them first; list them here. Next Steps must name the receiving agent in brackets: `[DevOps] Upload scripts to S3`.

**DT/AE (DevOps/AWS Engineer) — replace Work Completed with Deployment Sequence table, add Deployment Tags:**
```markdown
## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source | `abc1234` feat(pipeline): description |
| 2 | build-and-upload.sh | SHA256: `AbCdEf...=` |
| 3 | Commit source map | `def5678` ci: upload artifacts [skip ci] |
| 4 | terraform plan | N changed (description) |
| 5 | terraform apply | N added, N changed, N destroyed |
| 6 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 7 | Update core doc | deployment_map.xml / pipeline_inventory.xml |
| 8 | record-deploy + tag + push | `ghi9012` ci: record deploy [skip ci], tag `pipeline-vX.Y.Z` |
| 9 | CloudFront invalidation | `INVALIDATION_ID` on `/api/path/*` |

## Verification

[Paste actual output confirming the deploy worked — S3 object sizes, data checksums, API response snippet, or CLI output.]

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| {pipeline} | `{pipeline}-vX.Y.Z` | `abc1234` |
```

**RD (React Designer) — add commit reference to header:**
```markdown
**Portal DEV commit:** `abc1234`
```

---

### Before Writing the Log

**Always confirm:**
1. **Status** — COMPLETE, IN PROGRESS, or BLOCKED, or AMBIGUOUS (one word, no hedging)
2. **Blockers** — what is blocking, who can unblock. Must follow Blocker Verification Protocol before writing BLOCKED.
3. **Next steps** — ordered, self-contained, cross-agent attributed where needed

---

## Blocker Verification Protocol

**Never declare yourself BLOCKED based on assumption alone.** Before writing a blocker
in your session log or task order status, you must do the following:

### Step 1 — Check the blocking agent's directory

Read the most recent logs and pending task orders of the agent you believe is blocking you:

```
{blocking_agent_folder}/logs/{most_recent_date}/    <- what they worked on last
{blocking_agent_folder}/task_orders/                <- what they have been asked to do
```

Look for: evidence that their work is complete, in progress, or not yet started.

### Step 2 — Determine status

| What you find | How to classify |
|---|---|
| Log or task order confirms the dependency is delivered | **Not blocked.** Use the output and proceed. |
| Log or task order confirms it is in progress or pending | **BLOCKED** — name the specific agent, task order, and what you are waiting for. |
| Nothing in their directory corroborates either state | **AMBIGUOUS** — dependency chain status unknown. |

### Step 3 — Write the appropriate status

**If BLOCKED:**
```
## Blockers
- BLOCKED on [agent serial]: [task order path] — waiting for [specific deliverable].
  Evidence: [log or task order path that confirms it is in flight].
```

**If AMBIGUOUS:**
```
## Blockers
- AMBIGUOUS dependency: [agent serial] has no log or task order corroborating
  status of [deliverable]. Cannot confirm blocked or unblocked.
  Escalate to DE/COO to resolve dependency chain visibility.
```

**If resolved by checking:**
Do not write a blocker at all. Proceed using the delivered output and note where you found it.

### Why this matters

A BLOCKED status halts work and triggers escalation. An incorrect BLOCKED status
wastes cycles. AMBIGUOUS is the honest state when evidence is absent — it routes
to COO/DE for resolution rather than stalling the entire agent.

---

## Abilities by Role

| Role | Commit | Push | Deploy AWS | Session Logs | Task Orders |
|------|--------|------|------------|--------------|-------------|
| **RD** | Own page ONLY | No | No | Encouraged | Receives |
| **DE** | Any portal path (ad-hoc) | No | No | **MANDATORY** | Creates + Receives |
| **DS** | Edit + commit locally | No | No | Encouraged | Receives |
| **DT** | Infra only | **Yes** (CLOUD + DEV) — QA gate | **Yes** | Encouraged | Receives |
| **AE** | Infra + pipeline | **Yes** (CLOUD) | **Yes** | Encouraged | Receives |
| **SA** | Docs only | No | No | Encouraged | Creates + Receives |

**Key rules:**
- DTs own ALL pushes and serve as the code review / QA gate before anything reaches remote
- DTs are interdisciplinary — any DT can push for any pod if closest to the work
- DEs commit athletically across any portal path but never push
- DS logic always goes cloud-side via DT/AE — never in frontend
- DE session logs are mandatory; all other roles encouraged

### Agent Commit Identity (Non-Negotiable)

Every agent commit MUST use the `--author` flag to attribute the commit to the agent, not to the machine user. Git has separate Author and Committer fields — the committer stays as Andrew (repo owner), the author is the agent.

**Format:**
```bash
git commit --author="{agent_serial} <{agent_serial}@opal.agent>" -m "message"
```

**Examples:**
```bash
# RD agent committing page work
git commit --author="0.4.2_RD_AdvisorIntelligence <0.4.2_RD_AdvisorIntelligence@opal.agent>" \
  -m "0.4.2_RD_AdvisorIntelligence: AdvisorIntelligence/DistributionTab -- fix nomenclature"

# DT agent committing infra work
git commit --author="0.1.0_DT_MarketIntelligence <0.1.0_DT_MarketIntelligence@opal.agent>" \
  -m "feat(news-pipeline): update trending scanner timeout"

# DE agent committing portal work
git commit --author="0.4.0_DE_ClientPlatform <0.4.0_DE_ClientPlatform@opal.agent>" \
  -m "0.4.0_DE_ClientPlatform: fix advisor intelligence API endpoint wiring"

# SA agent committing docs/org work
git commit --author="1.0.0_SA_CTO <1.0.0_SA_CTO@opal.agent>" \
  -m "org(1.0.0_SA_CTO): cross-pod API contract spec"
```

**Why this matters:**
- `git log --format='%an'` shows which agent authored each commit
- `git log --author="0.4.0"` filters to a specific agent's work
- GitHub displays the author distinctly from the committer
- DE launch protocol (`git log --grep`) and thread commit injection both depend on agent attribution

**Never** commit without `--author`. If you see a commit attributed to the machine user, it was made outside the agent system.

---

## Task Order Protocol

### Location

Task orders are stored in the **receiving agent's** `task_orders/` folder:
```
{receiving_agent_folder}/task_orders/{feature_name}.md
```

- One file per feature — **never overwrite into a monolith**
- Over time each agent accumulates many task order files — this is correct
- Flow: Andrew / SA -> branch agents -> leaf agents

### XML Task Order Template

All task orders use this XML structure. Wrap the XML in a markdown file.

```xml
<task_order>
  <metadata>
    <id>{issuing_agent_serial}-{YYYY-MM-DD}-{short_slug}</id>
    <issued_by>{issuing_agent_id}</issued_by>
    <issued_to>{receiving_agent_id}</issued_to>
    <date>{YYYY-MM-DD}</date>
    <status>pending | complete</status>
    <!-- If this task order was produced from a project thread, include: -->
    <thread_serial>{PROJECT_CODE}-{NNN}</thread_serial>  <!-- e.g., ADVI_V1VERS-004 -->
    <thread_ref>org/threads/{thread_id}/</thread_ref>
  </metadata>

  <objective>
    <!-- 1-3 sentences: what needs to be accomplished and why -->
  </objective>

  <scope>
    <pages>
      <!-- list portal pages affected -->
      <page>portal/src/pages/PageName/</page>
    </pages>
    <files>
      <!-- list specific files to create or modify -->
      <file action="create | modify">path/to/file.tsx</file>
    </files>
  </scope>

  <requirements>
    <requirement id="1"><!-- specific, testable requirement --></requirement>
    <requirement id="2"><!-- specific, testable requirement --></requirement>
  </requirements>

  <acceptance_criteria>
    <criterion id="1"><!-- how to verify this is done correctly --></criterion>
    <criterion id="2"><!-- how to verify this is done correctly --></criterion>
  </acceptance_criteria>

  <constraints>
    <!-- things the agent must NOT do, gotchas, dependencies -->
    <constraint><!-- e.g., do not modify shared types without DE approval --></constraint>
  </constraints>

  <dependencies>
    <!-- other task orders or agents this depends on -->
    <dependency agent="{agent_id}" task="{task_order_id}" status="pending | complete"/>
  </dependencies>

  <deliverables>
    <!-- what the agent produces when done -->
    <deliverable type="commit | document | spec"><!-- description --></deliverable>
  </deliverables>
</task_order>
```

### Task Order Completion Protocol

- **The receiving agent marks their own task order as `complete`** by editing the `<status>` field when done
- Status has only two values: `pending` (default) and `complete`
- Tier 1/2 agents review completion status of task orders they issued as part of their startup protocol
- This is the "done signal" — no separate notification needed

### Task Order Filename Convention

**Format (rigid — no exceptions for project work):**
```
{agent_folder}/task_orders/{MACRO}_{6CHAR}.{task-code}.{description-words}.md
```

**Segment rules:**
- **Dots** separate distinct segments of the identifier hierarchy
- **Dashes** separate words within a single segment
- **No underscores** after the `{MACRO}_{6CHAR}` project code
- Segments: `{MACRO}_{6CHAR}` → task code → description (→ further sub-segments if needed)

| Segment | Examples | Notes |
|---------|----------|-------|
| Project code | `ADVI_V1VERS`, `ADVI_YANGV2` | Underscore between macro and project suffix only |
| Task code | `004`, `Y-phase3`, `J1`, `Y1-Y4-Y6-Y12` | Matches thread serial number when thread-sourced |
| Description | `adv-drill-cla`, `de-type-wiring` | Dashes between words |

Project codes are in `org/projects/REGISTRY.md`. Macro codes are in `org/projects/MACRO_CODES.md`.

**Project task order examples:**
```
org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_V1VERS.004.adv-drill-cla.md
org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_V1VERS.004.distribution-continuous.md
org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_YANGV2.Y1-Y4-Y6-Y12.phase1-visual.md
org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_YANGV2.Y-phase3.de-type-wiring.md
org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_V1VERS.J1.partner-identity-dynamo.md
```

**Ad-hoc** (no registered project / lateral between agents):
```
{agent_folder}/task_orders/{description-with-dashes}.md
```
No project prefix. Used for work that doesn't trace to a registered project.

```
org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/rolling-flows-chart-redesign.md
```

Filtering task orders by project in any agent folder:
```bash
ls org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_V1VERS.*   # all V1VERS work
ls org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_YANGV2.*   # all YANGV2 work
ls org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_*          # all ADVI macro work
```

---

## DS Deliverables

Data Scientists produce technical documents, investigation reports, and specs. These go in:
```
{ds_agent_folder}/deliverables/{descriptive_name}.md
```

DS deliverables are referenced in SA/DE task orders as output destinations.

---

## Core Document Maintenance Protocol

Every agent above Tier 3 has a **core document** — a living XML deliverable that represents the current ground truth of their domain. These documents are not written once at activation and forgotten. They must be kept current as work progresses.

### Core Documents by Role

| Role | Core Document | Location |
|------|--------------|----------|
| RD | `page_inventory.xml` | `{agent_folder}/deliverables/` |
| DE | `pod_inventory.xml` | `{agent_folder}/deliverables/` |
| DS | `data_contract.xml` | `{agent_folder}/deliverables/` |
| DT | `deployment_map.xml` | `{agent_folder}/deliverables/` |
| AE | `pipeline_inventory.xml` | `{agent_folder}/deliverables/` |
| SA | `architecture_brief.xml` | `{agent_folder}/deliverables/` |

### Update Trigger (all roles)

Update your core document when you make a **structural change** to your domain:
- New resource, endpoint, file, or data source added
- Existing resource removed or renamed
- Shape or contract of an interface changes
- Configuration change with operational impact (memory, timeout, S3 key)

Do **not** update for cosmetic changes, patch deployments with no contract change, or internal refactors with no external interface change.

### Role-Specific Timing

**RD:** Update `page_inventory.xml` in the same commit as the page code change.

**DE:** Update `pod_inventory.xml` in the same commit as the portal code change that affects the pod's API endpoints, shared components, or page structure.

**DS:** Update `data_contract.xml` at handoff — in the same commit as the Lambda code change, before handing off to DT/AE for deployment. Verify your update against `infra/aws/lambda/ci/lambda-source-map.json` to confirm the deployed version aligns with what you documented. This update is a **gate**: DT should not deploy a Lambda whose output shape changed without a corresponding data_contract.xml update.

**DT:** Update `deployment_map.xml` after `terraform apply` reaches 0-diff, before `git tag`. The update is committed as part of the post-deploy commit sequence:
```
apply → 0-diff → update deployment_map.xml → commit → tag → push --follow-tags
```
Verification: the 0-diff Terraform plan is the proof that state matches your document.

**AE:** Update `pipeline_inventory.xml` after `terraform apply` reaches 0-diff, before `record-terraform-deploy.sh`. Part of the standard deploy sequence:
```
apply → 0-diff → update pipeline_inventory.xml → record-terraform-deploy.sh → commit → tag → push --follow-tags
```
The `current_tag` in `pipeline_inventory.xml` must always match the tag in `CHANGELOG.json`.

### Cross-Agent Consistency

When your change implies another agent's core document is now stale:
- Note it in your session log under "Files Modified"
- Issue a task order to the affected agent if the staleness is significant
- Do **not** edit another agent's core document yourself

Example: DS changes a Lambda output shape → DS updates `data_contract.xml` → DT deploys → DT updates `deployment_map.xml`. Each agent updates their own document; no agent crosses into another's deliverable.

---

## Thread Participation

You may be invoked as a participant in a conversation thread. When this happens, your prompt will contain thread instructions, context material, and previous messages from other agents. Follow the thread protocol defined in `org/threads/README.md`.

**Key rules for thread participation:**

- Write ONLY your own message file (`messages/{NNN}.md`)
- Do NOT modify THREAD.json, TURN.json, CONTEXT.json, or other agents' messages
- Set your signal in the YAML frontmatter: `continue`, `converge`, or `escalate`
- Stay in your role -- do not impersonate other agents
- Be concrete: name files, functions, resource names. Avoid vague summaries.
- If it is your last turn, your signal MUST be `converge`

**Thread orchestration** (creating and running threads) is a Tier 1/2 ability. Tier 3 agents participate only.

**SA and DE agents run thread scripts themselves via the Bash tool. Do NOT ask Andrew to run them.**
When a staging script exists, invoke it directly:
```bash
bash org/threads/staging/run-YYYY-MM-DD-{slug}.sh
```
The orchestrator is fully automated -- it writes messages, advances turns, and deposits
receipts without any human intervention. Andrew is never in the execution loop.

**Thread receipts** are saved to your `threads/` folder after each completed thread:
```
{your_agent_folder}/threads/YYYY-MM-DD_{other_serials}_{topic_slug}.md
```

### Agent Folder Structure

Every agent has these standard folders:
```
{agent_folder}/
  README.md        # Identity, role, responsibilities
  prompt.md        # Scoped persona prompt
  logs/            # Session logs (YYYY-MM-DD/descriptive_name.md)
  task_orders/     # Received task orders (feature_name.md)
  threads/         # Thread receipts (auto-populated by orchestrator)
  deliverables/    # Core document and other deliverables (Tier 2+ agents)
```

The `deliverables/` folder holds the agent's **core document** (see Core Document Maintenance Protocol below) and any other structured output artifacts.

---

## Time Zone Rule

**All times reported to Andrew must be in US Eastern Time (ET).** Never report UTC,
Zulu, or any other timezone. When reading UTC timestamps from logs, S3, git, or AWS,
convert to ET before presenting. Eastern is UTC-5 (EST) or UTC-4 (EDT). As of March
2026 we are in EDT (UTC-4). If you are unsure of the offset, run `TZ=America/New_York date`.

This applies to: session logs, status reports, deployment timestamps, gold run times,
S3 object timestamps, git commit times, and any other time you report to Andrew.

---

## Quick Reference

- **Documentation:** `docs/` directory mirrors project structure
- **Logs:** Update at natural breakpoints in your agent's logs folder
- **Decisions:** Always ask when multiple approaches exist
- **Files:** Ask before reorganizing or deleting
- **Dependencies:** Ask before installing packages
- **Security:** Never expose credentials
- **MCP server:** `opal-agent-comms` — inter-agent status checks, task order queries, async messaging. Use on every startup (Step 2b). Server source: `org/mcp/server.py`
- **Broker:** Auto-launched by `register_agent`. Singleton HTTP server on localhost:7800 for cross-session message routing. Source: `org/mcp/broker.py`
- **Monitor:** `python org/mcp/monitor.py` — live telemetry feed in a separate terminal. Supports `--pod N` and `--project CODE` filters.
- **Terraform binary:** `.tools/terraform.exe`
- **Bun:** `/c/Users/AndrewBerman/.bun/bin/bun`
- **Git Bash PATH note:** `export MSYS_NO_PATHCONV=1` before commands with `/` paths
