# AGENT START HERE — Opal Capital

---

## STOP — READ THESE FIRST

**BANNED: Explore agent** — produces fabricated output. Use comp-* tools and Grep/Read instead.
**BANNED: Task agent** — unreliable. Do the work directly.
**NO EMOJIS** in any code, log, print statement, or file that runs on AWS. ASCII only.
**COMP-* TOOLS BEFORE GREP** — run the appropriate comp-* command before manually tracing any dependency. See comp-tools table below.

---

## RAVC Protocol — Read First (Non-Negotiable)

Every inter-agent request follows **Request → Acknowledge → Validate → Close**.
Full spec: `org/ref/RAVC_PROTOCOL.md`.

- If a registered agent asks you to do something: acknowledge immediately, do it,
  report back with evidence (commit hash, artifact path, tool output).
- If you asked another agent for something: validate their evidence before
  closing the loop. REWORK requests must be specific — tie the gap back to the
  original expected evidence.
- Silent receipt and silent completion are both violations.
- CTO and COO own driving every loop to close during "go time" and only
  escalate to Andrew on the five triggers listed in the spec.

---

## Step 1 — Identify Yourself

Read your agent folder:
```
org/{tier_folder}/{your_serial}/README.md    — your ID, role, responsibilities
org/{tier_folder}/{your_serial}/prompt.md    — your scoped persona (read in Step 3)
```

Tier folders: `tier1_exec/` (SA) | `tier2_senior/` (DE, DT, DS, AE) | `tier3_junior/` (RD)

---

## Context Compaction / Session Resume — CRITICAL

If your context was compacted (you see a conversation summary at the start of your session),
**treat this as a fresh session start.** The summary is a snapshot from BEFORE compaction.

- Inbox state in the summary is STALE. Messages may have arrived during or after compaction that
  you never saw. "Inbox was empty" in the summary does NOT mean your inbox is empty now.
- PID changed on resume. Your prior registration is gone — broker shows you as stale/offline.
- GOs dispatched while you were compacted are sitting in your inbox unread.

**ALWAYS re-run the full Step 1b startup sequence before reading or acting on any summary content.**
Skipping startup because the summary says "no pending work" is the failure mode. Don't do it.

---

## Step 1b — MCP Startup (MANDATORY, every session, no exceptions)

**A. Register — use your FULL serial, including ~suffix:**
```python
register_agent("{your_serial}", summary="Starting session")
```
Makes you visible. Starts broker. Enables message push. Also auto-launches `agent-poller.py`.

**Lane agents (~B/~C/~D): register as `0.4.0_DS_ClientPlatform~C`, NOT as `0.4.0_DS_ClientPlatform`.**
Registering under the base serial means your `~C` inbox directory is never checked — you will
silently miss all GOs and MCP messages addressed to your lane serial.

**B. Check inbox for offline messages — two paths, both required:**
```bash
check-inbox {your_serial}   # filesystem path: reads inbox/{serial}/ + inbox/{base}/
```
```python
get_agent_status("{your_serial}")  # broker path: surfaces messages delivered via broker channel
```
These cover different delivery paths. `send_message` writes to filesystem AND broker — but
`check-inbox` only reads filesystem, and broker-channel messages only surface via `get_agent_status`.
Run BOTH to avoid missing messages. `check-inbox` alone is insufficient.

**C. Start inbox watcher (MANUAL — cannot be automated):**
```bash
# Bash tool, run_in_background: true, NO &
inbox-watch {your_serial}
```
Delivers messages in real time. Exits after delivering. **One launch = one
delivery = one relaunch.** Agents MUST relaunch the watcher via the Bash tool
(`run_in_background: true`) after every notification. No self-respawn (removed
2026-04-14 after the orphan-race-condition incident — orphans' stdout was
disconnected from the Claude Code task tracker, so messages were silently
swallowed when an orphan won the atomic `mv` race).

**BANNED: `bash org/mcp/inbox-watch.sh {serial} &`** — bare shell `&` looks
identical but is completely broken. The task-notification that interrupts the
agent ONLY fires for processes launched via the Bash tool with
`run_in_background: true`. A `&` process runs invisibly, exits invisibly, and
the agent is deaf for the rest of the session. Incident: 0.6.0_AE 2026-04-20.

**When you get a watcher-exit task-notification, that IS the signal that a new
message arrived.** Your required response:

1. Call `check_inbox({your_serial})` AND `get_agent_status("{your_serial}")` **immediately**.
   `check_inbox` reads the filesystem path; `get_agent_status` reads the broker channel.
   Both are required — either can have messages the other misses.
2. Act on the message this turn — ack (RAVC step 2), do the work, or validate
   the evidence (RAVC step 4). No "standing by" silence.
3. Relaunch `inbox-watch {your_serial}` via the Bash tool with
   `run_in_background: true`. Every delivery must be followed by a new
   Bash-tool-tracked watcher so the next message fires a notification.

**Belt-and-suspenders:** after sending a message where you expect a near-term
reply, call BOTH `check_inbox` AND `get_agent_status` at the top of each turn. `inbox-watch` is
event-push; `check_inbox` is authoritative pull. Do both.

Without a running watcher you are deaf to real-time pushes.
Both commands are in `.tools/` (in PATH) and work from any directory.

**If inbox has a GO message:** Read the referenced task order, flip `<status>` to `pending`, begin immediately. The GO IS your authorization. Do not ask Andrew.

**If the GO lists a SEQUENCE of TOs:** You are authorized to execute ALL of them in order without waiting for a new GO between steps. If a TO in the sequence is already complete when you reach it, move immediately to the next one. Keep going until you hit a blocked TO (deps unmet) or the list is exhausted. Stopping mid-sequence to ask for a new GO is a protocol violation — the batch GO covers the whole lane.

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

## /loop — Universal Watchdog Mode (ALL agents)

Andrew can fire `/loop` at any agent, not just CTO/COO. Two forms:

| Form | Recipients | Semantic |
|------|-----------|----------|
| `/loop` (bare) | Any agent | **Watchdog mode** — self-nudge for inbox / watcher health / TO queue / heartbeat. Never auto-exits. |
| `/loop {PROJECT_CODE}` | CTO + COO only | **Project-driver mode** — operator→validator→closure. See CTO/COO prompt.md "/loop dynamic mode" section. |

### Watchdog mode — what to do on each wake (workers)

Every wake, run this checklist in order. Keep it tight — the loop is supposed to be cheap.

1. **Inbox pull (authoritative):**
   ```python
   check_inbox("{your_serial}")
   get_agent_status("{your_serial}")
   ```
   Both paths. Act on any message this turn (RAVC ack / execute / validate). No "standing by" silence.

2. **Watcher health — DO NOT launch a new watcher on every wake.**
   Only relaunch if the prior watcher has CERTAINLY exited. The only reliable exit signal is a `<task-notification>` with status `completed` for your most recent `inbox-watch` Bash task ID. If you've seen that notification this session since your last launch → it exited → relaunch exactly once. Otherwise → leave it alone.

   Decision table:

   | Observation | Action |
   |-------------|--------|
   | Received task-notification for your last `inbox-watch` task ID since last relaunch | Relaunch **once** via Bash tool `run_in_background: true` |
   | No task-notification since last relaunch | Watcher is still alive — **DO NOT relaunch** |
   | Can't remember your last task ID / uncertain | **DO NOT relaunch**; rely on Step 1 `check_inbox` for this wake |
   | Fresh session (no prior launch) | Launch exactly one |

   `check_inbox` in Step 1 is the authoritative pull — it catches messages whether the watcher is alive or not. The watcher is a real-time-push optimization, not a correctness requirement. If you're unsure, skip. Duplicate watchers = orphan race (see 2026-04-14 incident banned in Step 1b).

   `kill-orphans --stale --force` is the cleanup escape hatch if duplicates accumulate — but that's exec-level, not something workers self-invoke.

3. **Broker registration:**
   If `get_agent_status` said NOT REGISTERED, re-register:
   ```python
   register_agent("{your_serial}", summary="<current work>")
   ```

4. **Heartbeat + summary refresh:**
   ```python
   heartbeat("{your_serial}", summary="<one-line current state>")
   ```
   Keeps your status visible to the org (prevents "stale" state).

5. **TO queue scan:**
   Read `{your_agent_folder}/task_orders/`. For each TO:
   - `<status>pending</status>` + dependencies met → if not already mid-work, start it.
   - `<status>staged</status>` → do NOT start; waiting for GO signal (exec dispatch).
   - `<status>complete</status>` → skip.
   If you're mid-TO, continue it.

6. **Schedule next wake:**
   - **Active** (mid-TO, expecting near-term reply from another agent, or recent message requires follow-up): `ScheduleWakeup(delaySeconds=60)`.
   - **Idle** (no active TO, no expected reply, queue quiet): `ScheduleWakeup(delaySeconds=270)`. Inside 5-min cache TTL.
   - **Never 300s.** Worst-of-both — cache-miss + immediate refire.

**Never auto-exit.** The loop runs until Andrew stops it (he manages lifecycle). If the queue is empty and there's nothing to do, still `ScheduleWakeup(delaySeconds=270)` and surface a one-line status to Andrew so he can decide whether to stop or redirect.

### Escalation signals while looped

- **3 consecutive idle wakes with no observable state delta** (no message, no TO status change, no commit in your lane) → surface to Andrew with "looks like I'm waiting on something external — is there a blocker?" Do NOT stop the loop.
- **Got a real blocker** (ambiguity, destructive op required, cross-agent wait) → MCP the blocking agent first; if no response in 1 wake cycle, surface to Andrew.
- **Context compacted mid-loop** → first wake after compaction: re-run full Step 1b startup (register + inbox-watch + check_inbox + both paths). Don't trust the compacted summary's "inbox empty" claim.

### What watchdog mode does NOT do

- Does NOT execute TOs autonomously without the normal GO dispatch / RAVC protocol — it's a health-check loop, not an autonomous driver.
- Does NOT edit files on behalf of absent agents.
- Does NOT substitute for the operator/validator project-driver (that's CTO/COO only via `/loop {PROJECT}`).
- Does NOT skip compiler mandates or acceptance-flex rules.

### For CTO/COO specifically

Bare `/loop` still works as the watchdog. `/loop {PROJECT}` is the project-driver. See your prompt.md "/loop dynamic mode" for the operator→validator→closure phase logic. Both co-exist; Andrew picks which he fires.

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
| Modify portal component | `comp-transform schema-check [Component]` | MISSING = runtime undefined. NOTE = expected runtime alias. UNUSED = typed but not rendered — if name matches your feature, investigate. |
| Adding new cohort / metric / mode | `comp-transform schema-check [Component] --feature [token]` then `comp-transform ternary-audit [Component]` | --feature escalates feature-named UNUSED to WARN with routing ternary hint. ternary-audit finds every `cohort ===` chain missing the new branch. Would have produced the complete W6 fix list at Phase 1 of W3. |
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
| DE | `comp-transform schema-check [Component]` + `comp-blast [fn]` | `comp-blast [changed fn]` — no new downstream nodes. **When adding a new cohort/metric/mode:** also run `schema-check --feature [token]` + `ternary-audit [Component]` at Phase 1. |
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
| DE | `comp-transform schema-check` before touching data props; `comp-blast` before deleting. `comp-routes behaviors` when debugging 4xx / auth failures. **Adding a new cohort/metric/mode:** `schema-check --feature [token]` + `ternary-audit [Component]` at Phase 1 — mandatory after W3 OFC incident. |
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

## Closure Discipline (Non-Negotiable — SA/COO/CTO only)

Closing a project is a **3-step atomic operation**, not a single JSON edit. All three steps happen in the same commit:

1. **JSON status flip.** `org/projects/{CODE}.json` → `"status": "complete"` + add `"completed": "YYYY-MM-DD"` + rewrite `phase` narrative as closure summary + set `blocking` to "None" (or "None — {reason}" if superseded/absorbed).
2. **REGISTRY row move.** `org/projects/REGISTRY.md` → delete the row from "Active Projects" (or "Inactive / On Hold") table. Insert a new row at the TOP of "Completed / Archived Projects" table (newest-first convention) with `Completed` date column + closure notes citing ship evidence (commits, tags, supersession path).
3. **PRD status note.** PRDs stay in `docs/architecture/` — do NOT archive active PRDs. But if the PRD has a top-of-file `Status:` line, update it to `Status: COMPLETE — {date}` or `Status: SUPERSEDED BY {project_code}`.

**Why all three:** we've observed JSON-flipped projects whose REGISTRY row stayed in Active for days (ADVI_ROLGAT 2026-04-17→2026-04-21; discovered in joint audit `f959fbcb`). Any one step alone is silent-drift to the other two. Authors of closure commits MUST edit all three in one `git commit --only` so the atomicity is structural.

**Closure triggers:**
- **Complete** — all authored TOs status=complete; no authored-but-unshipped work; final-deploy mechanical only. Use when the project achieved its stated goal.
- **Complete-as-superseded** — scope fully absorbed into another active project or PRD. JSON `phase` cites the successor explicitly. Use when the work is done but not under this project's banner.
- **Cancelled** — explicit Andrew or CTO directive cancelled the work. JSON `phase` cites the directive. Different from superseded (no successor work).
- **Inactive / On Hold** — blocked by external dependency (Andrew/IT, vendor, regulatory). Stays in On Hold table; do NOT move to Completed until the external blocker clears or cancellation call is made.

**Anti-pattern — single-step closure:** flipping JSON status alone while REGISTRY + PRD lag. Always 3-step, always one commit.

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
| DS | Commit + push + gold-script S3 upload (committed-ref) + qa-runner SSM dispatch | No (PROD) | QA-runner only | Encouraged |
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
