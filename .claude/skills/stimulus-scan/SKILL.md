---
name: stimulus-scan
description: Action-oriented meta-supervisor scan for the Opal multi-agent fabric. Reads peer-agent state from the opal-agent-comms broker, classifies each agent by staleness, cross-references inboxes for unresolved blockers, and **dispatches work to fix blockers and redirect idle capacity**. NOT a reporting tool — every STALE / STANDING_BY / BLOCKED agent receives a TO or nudge in the same scan. For CTO/COO use, primarily inside the `/loop` body. Trigger: sooner-of (~45min since last scan) OR (watcher down / fresh wake). Adapted for ajb_workspace from corporeal's stimulus-scan — agent state is the broker, not telemetry files.
---

# /stimulus-scan

Scans peer-agent state + inbox, classifies each agent, and **dispatches work to fix the gaps**. Run from the CTO/COO `/loop` body on the sooner-of (~45min elapsed) OR (fresh wake / watcher relaunched). This is the operational skill behind the COO Step-0.5 active-push discipline.

## When to invoke

- Inside the `/loop` body: when `now - mtime(org/mcp/.last-stimulus-scan) >= 2700s` (~45min) OR on a fresh wake after the watcher exited.
- On-demand for a fabric health + action sweep.

## Purpose

This is NOT a reporting tool (that is `/status`). It exists to:
1. **Restructure capacity** — idle agents redirected to validation / audit / scaffold work.
2. **Fix blockers** — an agent with an unread inbox or an unanswered escalation gets the missing dependency routed NOW.
3. **Keep agents working** — no agent leaves a scan in STALE / STANDING_BY state without a dispatch.

Per scan: at LEAST one outbound action per non-ACTIVE agent. No "flagged for review" — the dispatch IS the review. The only acceptable scan with zero dispatches is one where every in-scope agent is ACTIVE or legitimately gated on a tracked external signal (an in-flight SSM chain, a deploy, an Andrew gate).

## What it does (procedure)

Run each step in order. Use the MCP broker tools + Bash; emit findings as a markdown table AND fire the dispatches via `mcp__opal-agent-comms__send_message` in the same scan.

### Step 1 — Read agent state (the broker is the source)

ajb_workspace agent state lives in the `opal-agent-comms` broker, not in telemetry files:

- `get_live_agents()` — every registered agent: serial, LIVE/STALE flag, last-seen age, one-line work summary. This is the primary staleness signal.
- `get_org_summary()` — active projects + every agent with pending task orders.

For an in-scope agent with no broker registration at all, classify `NOT_REGISTERED` (the agent may be offline this cycle, or crashed mid-session — a meta-signal; do not invent activity for it).

### Step 2 — Compute staleness per agent (the broker summary is LOW-FIDELITY — cross-check with git)

**CRITICAL — heartbeat-drift:** a broker "Working on" summary is aspirational and updated only when the agent calls `heartbeat()`. An agent heads-down in a long generation, an SSM chain, or composing a multi-file commit can look stale while productively working. **git is ground truth.**

**Before classifying any agent IDLE/STALE, cross-check:**

```bash
# Commits in the last 30 min (the all-branches view; CLOUD is multi-agent)
git log --all --oneline --since="30 minutes ago" --pretty=format:"%h %an %s"
```
```bash
# That agent's most recent inbox traffic (sent/received)
ls -t org/mcp/inbox/*/read/*<SERIAL>* 2>/dev/null | head -3
```
Also consider `aws ssm list-commands --max-items 20` if a remote chain may own the agent's critical path.

If git OR inbox shows recent activity -> the agent is **WORKING** regardless of a stale broker summary. Treat as ACTIVE.

Classify:

| Bucket | Signal | Meaning |
|---|---|---|
| ACTIVE | broker LIVE + recent heartbeat/commit/SSM (< ~10 min) | working — no action |
| IDLE | LIVE but no work signal ~10-30 min | between tasks — eligible for capacity routing |
| STALE | LIVE but no heartbeat/commit/inbound ~30+ min | no observable progress — REQUIRES re-dispatch or a blocker trace |
| NOT_REGISTERED | absent from `get_live_agents()` | offline this cycle / crashed — meta-signal |

**Posture (Andrew directive):** "Standing by for X" is never an acceptable terminal state. An idle agent always routes to ready work — there is concurrent generative work available (audits on un-audited surfaces, validator pre-staging, scaffolds for ratified PRDs, pre-stage of a downstream of an about-to-ship peer). Tolerating IDLE/STALE because the "next deliverable is gated" is a supervisor failure.

Skip the scanning agent itself (don't scan-self).

### Step 3 — For each STALE / IDLE agent, classify the cause

```bash
check_inbox("<SERIAL>")           # (MCP) unread messages — is the agent blocked on an unread dependency?
get_agent_status("<SERIAL>")      # (MCP) latest log summary + pending TOs + blockers
```

Decision tree:

| Classification | Detection | Action |
|---|---|---|
| `BLOCKED` | unread inbox > 0, OR a pending unanswered escalation from the agent | route the missing dependency / answer the escalation / reassign the dep; escalate to CTO if it needs an architectural call |
| `STUCK_MID_CLOSEOUT` | no commit but `git status` shows the agent's files staged-not-committed, or a TO `active` > 2 wakes with no commit | nudge with the exact files — the agent executed but never ran `git commit`; have them finish the commit |
| `STARVED` | inbox empty, no pending dep, a `pending`/`staged` TO with gates met | flip + GO the staged TO, or dispatch the next-phase TO from the project plan |
| `STANDING_BY_REDIRECT` | last log/heartbeat said "standing by" but >= ~30 min elapsed | **dispatch generative work** — never accept terminal standby (Step 3.5) |
| `NOT_REGISTERED` | absent from broker | check whether the agent should be live this cycle; if a phantom lane (e.g. a `~C` serial with no live agent), re-route its TOs to the live base/lane agent — do not leave a TO orphaned |

### Step 3.5 — Hot-work assessment (MANDATORY before dispatch)

Before picking any dispatch, ask "what's hot right now?" An idle agent should **parallelize the critical path**, not chew generic backlog. Gather signals:

```bash
git log --all --oneline --since="20 minutes ago"      # what just shipped
list_task_orders("<SERIAL>", status="staged")          # (MCP) staged TOs with gates maybe met
```
Then, for the idle agent, ask in order:
1. **Critical-path unblock** — is a peer blocked on something this agent could resolve (an audit, a second pair of eyes, a parallel probe)?
2. **Pre-stage downstream** — is a peer about to ship something with an immediate downstream this agent could scaffold/test now?
3. **Parallel branch** — is a hot workstream serial today that a second agent could take a defined slice of?
4. **Specialization fit** — does the agent's role/domain make them the right hands for an in-flight thread?

Only if all 4 return "nothing fits" -> the role-fallback menu below.

**Role-fallback generative work** (used only when hot-work returns nothing):
- **DE** -> portal component schema-audits (`comp-transform schema-check`); cross-page consistency sweeps; pre-stage wiring for a ratified PRD.
- **DS** -> gold/silver script COLUMN-GAP audits (`comp-pipescript io`); validator pre-staging; backfill-freshness sweeps.
- **DT** -> deployment-map drift checks; CloudFront/route behavior audits (`comp-routes behaviors`); IAM gap sweeps (`comp-iam gaps`).
- **AE** -> pipeline IAM/least-privilege audits; alarm-coverage gaps; cold-start / post-apply verification sweeps.
- **RD** -> page-inventory field-coverage checks (`comp-transform fields`).

### Step 4 — Emit the classification table

```
## Stimulus Scan — <UTC timestamp>

| Agent | State | Staleness | Inbox | Class | Action |
|---|---|---|---|---|---|
| 1.0.0_SA_CTO | ACTIVE | 2m | 0 | ACTIVE | none |
| 0.4.0_DE_ClientPlatform | STALE | 34m | 1 unread | BLOCKED | route the dep |
| 0.2.0_DS_PortfolioAnalytics | IDLE | 18m | 0 | STARVED | dispatch parallel audit TO |
```

### Step 5 — DISPATCH (mandatory; hot-work fit first)

For every non-ACTIVE agent, FIRE the action in this same scan via `mcp__opal-agent-comms__send_message`:

- `BLOCKED` -> route the missing dependency / answer the escalation.
- `STUCK_MID_CLOSEOUT` -> nudge with the exact staged files so they finish the commit.
- `STARVED` -> flip+GO the gates-met staged TO, OR a hot-work parallelization TO (Step 3.5).
- `STANDING_BY_REDIRECT` -> a hot-work parallelization TO; fallback to the role menu.
- `NOT_REGISTERED` -> re-route orphaned TOs; flag a phantom lane.

**Dispatch quality check (per TO):** does it connect to an in-flight workstream (not generic backlog)? does it have a clear RAVC2 deliverable returnable in a bounded window? does it match the agent's role/domain? does it parallelize something serial OR unblock a peer OR pre-stage a downstream? If 3+ are "no," it is backlog-chew — acceptable only as a genuine fallback.

Then update the scan timestamp:
```bash
date -u +%s > org/mcp/.last-stimulus-scan
```

**No "suggested action" without firing.** A scan that observes 3 STALE agents produces 3 dispatches in the same turn.

## Discipline / risk mitigations

- **False-positive STALE** — an agent in a long generation / S3 read / SSM wait may not heartbeat for >10 min. Mitigation: the git + inbox + SSM cross-check in Step 2. When in doubt, dispatch a *non-blocking* parallel-track TO (audit / scaffold), not a nudge on the current work.
- **Lane discipline** — a `~B`/`~C`/`~D` lane agent takes dispatch only from same-lane exec; do not cross-dispatch. A phantom `~lane` (no live agent) means its TOs re-route to the live base agent — surface that, do not leave the TO orphaned.
- **Self-loop** — never scan-self.
- **Gated ≠ idle** — an agent correctly monitoring a healthy in-flight chain/deploy is WORKING; do not disturb it. Only redirect genuine idle.
- **RAVC + compiler mandates still bind** — every dispatched TO carries a structured `<compiler_tools_mandate>` and follows RAVC; stimulus-scan drives the loop faster, it does not relax any rule.

## Configuration

State file: `org/mcp/.last-stimulus-scan` (unix-epoch of the last scan). Agent state source: the `opal-agent-comms` broker (`get_live_agents` / `get_agent_status` / `get_org_summary`). Inbox: `org/mcp/inbox/<serial>/`.
