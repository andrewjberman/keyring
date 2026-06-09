# AGENT START HERE — Opal Capital

---

## STOP — READ THESE FIRST

**BANNED: Explore agent** — produces fabricated output. Use comp-* tools and Grep/Read instead.
**BANNED: Task agent** — unreliable. Do the work directly.
**NO EMOJIS** in any code, log, print statement, or file that runs on AWS. ASCII only.
**COMP-* TOOLS BEFORE GREP** — run the appropriate comp-* command before manually tracing any dependency. See comp-tools table below.
**HOT-REGISTRY SCOPE — MANDATORY (Andrew direct 2026-06-09):** Agents MUST NOT self-initiate work on any project that is not `"status": "active"` in `org/projects/*.json`. The hot registry is the ONLY authorized work surface. A TO in your task_orders/ folder for a non-active project is NOT a work authorization — do NOT execute it. Surface it to COO with subject `[SCOPE-VIOLATION]` (project code + TO ref + what you found) and hold. Exceptions: (a) Andrew-direct verbal instruction in the current session authorizes that specific action; (b) an explicit MSTR directive via a Tier-1 dispatch naming the non-hot project with stated justification. Applies equally to /work ticks, /drive ticks, and any autonomous TO queue scan.

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
- **Issuing a STOP / halt:** an exec halting a long irreversible operation MUST
  prefix the message subject with `[STOP]` (or the synonym `[HALT]`) as the first
  characters of the subject text. This is the signal the HALTGT deploy checkpoint
  classifies against — see `docs/architecture/HALTGT_SEVERITY_CONVENTION.md`. A
  routine message MUST NOT begin its subject with either token (do not use them
  for emphasis — they hard-block deploys). For non-blocking urgency use plain
  words (`URGENT`, `ESCALATION`).

---

## Tier 0 — `0.0.0_AB_MSTR` and the authority hierarchy

The fabric has a Tier-0 agent: **`0.0.0_AB_MSTR`** (MSTR) — the autonomous
principal-proxy. It stands in for Andrew among the agents: it originates
strategy, charters, and the decomposition of work, and directs the fabric
through Tier 1. It is governed by its own constitution at `org/tier0/`
(`CONSTITUTION.md`, `STAKES_MATRIX.md`, `DIRECTIVES.md`).

**Authority hierarchy:**

> **Andrew (sovereign) › MSTR / Tier 0 (principal-proxy) › CTO · COO / Tier 1 › Tier 2 (DE/DT/DS/AE) › Tier 3 (RD)**

- A **Tier-0 directive outranks Tier-1 planning.** A charter MSTR delegates to
  CTO/COO carries near-Andrew authority — treat it accordingly.
- Tier 1 **may push back on a Tier-0 charter on operational grounds** — reject or
  request clarification on feasibility. That is the org working, not
  insubordination. MSTR sets *what* and *why*; Tier 1 informs *whether* and *how*.
- **Andrew remains sovereign.** A real-Andrew instruction overrides any MSTR
  directive. MSTR is a proxy, never a replacement.
- **CVO independence:** the CVO (`3.0.0_SA_CVO`) sits in Tier 1, but when it
  exercises its Constitution Article XIV ratification or review authority it is
  **constitutionally independent** — it does **not** ratify as MSTR's subordinate.
  MSTR outranks Tier 1 for strategic direction; it does **not** outrank a CVO
  ratification verdict.
- **The never-stop rule.** Agents NEVER stop at a fork. A fork you cannot
  resolve is escalated up the chain — never halted on, never sat-silent-on.
  The chain is built so something always moves. Silent freeze is the failure
  mode the Tier-0 framework was designed to prevent.
- **The escalation chain.** worker (Tier 2/3) → CTO / COO (Tier 1) → MSTR
  (Tier 0, terminal resolver) → Andrew (sovereign). **MSTR is the terminal
  resolver of the escalation chain** — authorized to make the principal's
  call in Andrew's absence, bounded by active Directives + the Stakes
  Matrix. Andrew only gets the forks MSTR explicitly defers to sovereign
  judgment (new product strategy, new Directive, S3 / S4 procurement). The
  chain runs only upward, never sideways.

**MSTR startup** (only `0.0.0_AB_MSTR` runs this): register as `0.0.0_AB_MSTR` on
the broker; launch `/watcher` (arms the persistent inbox Monitor ONCE at load —
no watcher cron, LD-0166); arm **NO governance cron** — MSTR now arms ZERO crons
(LD-0164 retired `/mstr-review` to ad-hoc; LD-0166 struck the `/watcher` cron;
`/govern` is not auto-armed per LD-0147); read
`CONSTITUTION.md` + `STAKES_MATRIX.md` + `DIRECTIVES.md` in full; run
`/mstr-review` once at startup as an ad-hoc pass to fire the first cycle (this also fires AC7 LD-0087 if
LD-0089 PAVC AC7 is pending); pull `get_live_agents()` and spawn missing
canonical Tier-1 agents (`1.0.0_SA_CTO`, `2.0.0_SA_COO`, `3.0.0_SA_CVO`,
`1.1.0_SA_CTO`, `2.1.0_SA_COO`, `3.1.0_SA_CVO`) via `.tools\spawn-agent.ps1`
(use `$env:FORCE_SPAWN = "post-reboot Tier-1 bring-up per Andrew direct"`
when rate cap blocks the canonical 6-agent set on a clean post-reboot boot);
then, at Andrew's discretion, invoke `/govern` (Andrew-discretion only, not
auto-armed — LD-0147). MSTR has no standard agent home folder — `org/tier0/`
is its domain and the Constitution is its persona. If no ignition-valid
Directive exists, `/govern` scans and reports only — it originates nothing.

**Tab-title default for spawned agent windows (Andrew direct 2026-05-26).**
Every PowerShell window launched via `.tools\spawn-agent.ps1` MUST display
the agent serial in its tab/title bar at session start (e.g., loading
`1.0.0_SA_CTO` literally displays `1.0.0_SA_CTO` in the Windows Terminal tab).
Mechanism: OSC 0 escape sequence + `$Host.UI.RawUI.WindowTitle` set BOTH in
`spawn-agent.ps1` outer-shell pre-`ajb` dot-source AND in `ajb.ps1`
`ajb`-function pre-`& claude` invocation (last-write-wins for Windows
Terminal). `/mstr-review` Step 2 spawn-mechanism-discipline verification
fires `spawn_mechanism_drift` finding on any operator-observed
serial-not-in-tab case.

**Other agents:** MSTR does not normally dispatch to you directly — it works
through Tier 1. A Tier-0-originated charter reaching you via CTO/COO carries the
authority above.

---

## Step 1 — Identify Yourself

Read your agent folder:
```
org/{tier_folder}/{your_serial}/README.md    — your ID, role, responsibilities
org/{tier_folder}/{your_serial}/prompt.md    — your scoped persona (read in Step 3)
```

Tier folders: `tier1_exec/` (SA) | `tier2_senior/` (DE, DT, DS, AE) | `tier3_junior/` (RD)

---

## Step 1a — Verify your cwd matches your fabric (LD-0088 A.1+A.2)

Cross-fabric agents launch into different worktree cwds per LD-0088 A.1 (Andrew sovereign `5c39327f` + LD-0089 AC1 implementation):

| Fabric | Serials | Expected cwd |
|---|---|---|
| **ws** (ajb_workspace) | `0.0.0_AB_MSTR`, `1.0.0_SA_CTO`, `2.0.0_SA_COO`, `3.0.0_SA_CVO`, `0.x.x_(DE\|DT\|DS\|AE\|RD)_*`, all ws lanes | `C:\Users\AndrewBerman\Desktop\ajb_workspace` |
| **CL** (feature_clb worktree) | `1.1.0_SA_CTO`, `2.1.0_SA_COO`, `3.1.0_SA_CVO`, `2.1.0_SC_CompLearns`, `1.[1-4].0_DS_CompLearns` | `C:\Users\AndrewBerman\Desktop\feature_clb` |

`.tools/ajb.ps1` Get-AgentLoopDirective + the cwd-routing block at the top of the `ajb` function enforce this automatically when the agent is launched via `ajb` / `spawn-agent.ps1`. If you find yourself in the wrong cwd (e.g. an Andrew-direct manual launch placed you in ajb_workspace as a CL serial), this is acceptable per LD-0088 standing-authorization-via-AC-enumeration (Andrew direct overrides the wrapper) — your fabric attribution still resolves via your serial.

**Why cwds differ:** Each cwd carries different `.mcp.json` + `.claude/skills/` content. The cwd determines which MCP server config Claude Code loads + which skills are discoverable. Post-LD-0034 unified-broker + LD-0089 AC1 A.3 (`f6bd29067`), both cwds reach the same `opal-agent-comms` canonical broker, but the local config files differ:

- `ajb_workspace/.claude/skills/` — full ws skill set (ws-charter, mstr-*, drive, work, etc. + workspace-shared)
- `feature_clb/.claude/skills/` — CL-native skills (cl_cto, cl_program, cl-charter, cl-subject, continuous-cycle) + 9 workspace-shared skills synced from ws per LD-0089 AC1 A.4-EXT (`ba1f914c3`)

Workspace-shared skills propagate ws → CL via `.tools/sync-skills-to-worktree.sh` (idempotent + sha256 drift detection; run on each session-start in feature_clb or after `git pull`).

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

**A.1 — Write session-id-keyed serial file (LD-0070 §7.2):**
```bash
mkdir -p org/mcp/sessions
if [ -n "${CLAUDE_CODE_SESSION_ID:-}" ]; then
    echo "{your_full_suffixed_serial}" > "org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"
fi
```
Enables the PostToolUse hook to resolve agent serial via per-session deterministic source (tilde-lane-safe; broker-outage-resilient; survives `.comp-graph/.agent_context` race). Hook applies once WB-1.1 patch lands; this file write is harmless ~50-byte data until then. Env var name is `$CLAUDE_CODE_SESSION_ID` (with `_CODE_` infix) — empirically verified set by Claude Code at session start. Files are per-session ephemeral; gitignored at `org/mcp/sessions/*.serial`; GC'd 24h post-last-activity per spec §7.4.

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

**C. Arm the persistent inbox Monitor (ONCE at load — `/watcher` does this):**

Run `/watcher`. It arms a **persistent Monitor task** running
`inbox-watch.sh {your_serial} stream`. The Monitor tool turns each `[INBOX] <file>`
line the script emits into a chat notification, so you are interrupted **per
message while you keep working** — and the script **never exits**. Arm it once;
it is the standing delivery mechanism for the whole session.

If arming manually (what `/watcher` does internally) — use the **Monitor tool**,
`persistent: true`, `timeout_ms: 3600000`:
```
Monitor(
  command="bash /c/Users/AndrewBerman/Desktop/ajb_workspace/org/mcp/inbox-watch.sh {your_serial} stream",
  persistent=true, timeout_ms=3600000)
```

**Decisive reachability test — do NOT use `TaskList`.** `TaskList` lists `TaskCreate`
to-do items, NOT Monitor/background tasks; it returns "No tasks found" even when your
Monitor is alive, so an empty `TaskList` is NOT evidence of a dead watcher (treating
it as one makes agents double-arm — observed across multiple agents 2026-06-03). The
real check: (1) **death-notification rule** — a Monitor runs until it dies and fires a
`<task-notification>` (status `failed`/`completed`) for its task id; if you armed one
this session and saw no such notification, it's alive; (2) positive check
`TaskOutput(<task_id>, block=false)` → `running`; (3) task-id-independent fallback
`ps -ef | grep 'inbox-watch.sh {serial} stream' | grep -v grep`. This replaces the
old exit-on-delivery model and its failure-mode catalog (ORPHAN / PPID=1 zombie /
MULTIPLE / AUTO-RESPAWN-INTERRUPT-LOST / the misleading exit-143 / deaf-prior-session
watcher / dropped 2nd-message-in-a-batch). The persistent Monitor: survives in-session
compaction, loops over **all** `*.md` each poll (batch-safe), and never turns off.
**You never relaunch** — there is no exit-and-relaunch cycle anymore.

**BANNED:**
- Launching `inbox-watch.sh {serial} stream` under Bash `run_in_background` — the
  Bash tool only notifies on *exit*, and stream mode never exits, so you go silent
  for the session. It MUST run under the **Monitor tool**.
- The legacy bare-path relative launch `bash org/mcp/inbox-watch.sh ...` (guard-hook
  blocked — use the absolute path in the Monitor command above).
- A recurring `/watcher` cron/ScheduleWakeup loop — obsolete; the persistent
  Monitor is the standing mechanism, armed once at load.

**Legacy exit-on-delivery mode** (`inbox-watch.sh {serial}` with no `stream` arg)
is retained only so already-running pre-migration agents aren't broken; do not use
it for new launches.

**Post-LD-0034 unified broker + inbox (2026-05-24).** ALL agents (ws + CL) use the
ws-rooted inbox at `ajb_workspace/org/mcp/inbox/{serial}/`. CL serials all have
inbox dirs under that unified path; the legacy `feature_clb/org/mcp/cl_inbox/` path
and the `cl-inbox-watch.sh` carve-out are **retired**. Full cross-channel
architecture: `docs/architecture/AGENT_COMMS_ARCHITECTURE.md`.

**When an `[INBOX] <file>` event fires, that IS a new message.** Your required
response:
1. Read the message from `org/mcp/inbox/{your_serial}/read/<file>` (the stream
   watcher already mv'd it there) — or call `check_inbox` / `get_agent_status` if
   you want the broker-channel view too.
2. Act on it this turn — ack (RAVC step 2), do the work, or validate the evidence
   (RAVC step 4). No "standing by" silence.
3. **Do not relaunch anything** — the Monitor keeps running.

**Belt-and-suspenders:** after sending a message where you expect a near-term
reply, still call BOTH `check_inbox` AND `get_agent_status` at the top of the turn.
The Monitor is event-push; `check_inbox` is authoritative pull. Both are in
`.tools/` (PATH) and work from any directory. Full design: `org/mcp/INBOX_WATCH_DESIGN.md`.

**If inbox has a GO message:** Read the referenced task order, flip `<status>` to `pending`, begin immediately. The GO IS your authorization. Do not ask Andrew.

**If the GO lists a SEQUENCE of TOs:** You are authorized to execute ALL of them in order without waiting for a new GO between steps. If a TO in the sequence is already complete when you reach it, move immediately to the next one. Keep going until you hit a blocked TO (deps unmet) or the list is exhausted. Stopping mid-sequence to ask for a new GO is a protocol violation — the batch GO covers the whole lane.

**D. Owned-paths hook (install if absent):**
```bash
# owned-paths hook — installs if absent (ADHC_OWNPTH)
test -L .git/hooks/pre-commit || bash .tools/git-hooks/install-owned-paths.sh
```
Wires the lane-enforcement pre-commit hook on first use. Idempotent — safe to re-run. On Windows Git Bash the `-L` test always fails (no true symlinks), so the install script runs each session but exits 0 immediately once the hook is present.

**D2. Commit hygiene (use safe-commit.sh — ADHC_OWNPTH.007):**
Use `.tools/safe-commit.sh --author "..." -m "..." -- <paths>` for every commit. The wrapper aborts if the staged index contains any file outside your declared pathspec — the exact failure mode that produced three CLASS-C sweep incidents on 2026-04-27. With `--force`, the wrapper still runs but logs a `FORCE-BYPASS` audit entry to `org/git-author-override-audit.log` (use only when you cannot clean the shared index — e.g. multi-agent worktree contention). Bare `git commit` is allowed only when explicitly justified in the commit message.

**D3. Destructive-HEAD-move guard (install if absent — ADHC_OWNPTH.010):**
```bash
# git() destructive-HEAD-move guard — wires into ~/.bashrc if absent (ADHC_OWNPTH.010)
grep -qF "ADHC_OWNPTH.010 headmove-guard" ~/.bashrc 2>/dev/null || bash .tools/git-hooks/install-headmove-guard.sh
```
Installs a `git()` shell-shadow function that gates destructive `git reset` / `git rebase` / `git commit --amend` (moves that discard or rewrite local-only commits). Idempotent — safe to re-run. Override an intentional destructive move with `FORCE_HEADMOVE=1` (audited to `org/git-author-override-audit.log`). Covers Bash-tool shells that source `~/.bashrc`; NOT PowerShell or `command git`.

**E. Set compiler tool context (enables auto-logging):**
```bash
mkdir -p .comp-graph && printf "SERIAL=%s\nTO_ID=\n" "{your_serial}" > .comp-graph/.agent_context
```
Every comp-* tool run automatically appends a structured row to `org/compiler-tools-log.md`.
No manual logging needed. When you start a new TO, update the context:
```bash
printf "SERIAL=%s\nTO_ID=%s\n" "{your_serial}" "{TO_filename_without_.md}" > .comp-graph/.agent_context
# Example: printf "SERIAL=0.4.0_DS_ClientPlatform\nTO_ID=ADVI_OFFICE.W1\n" > .comp-graph/.agent_context
```

**F. Arm role-appropriate primary loop (per LD-0062 §materialization-chain step 5):**

Per LD-0062 ratification 2026-05-25T~20:05Z (Andrew sovereign via "go with your recommendation"), each agent arms a role-appropriate primary cron loop at session start. Run the matching CronCreate command at the END of Step 1b, AFTER A-E above:

| Serial-class | Primary loop arming | Notes |
|---|---|---|
| `0.0.0_AB_MSTR` | **NO cron — MSTR arms ZERO crons (LD-0164 + LD-0166, Andrew direct 2026-06-08).** `/watcher` arms the persistent inbox Monitor ONCE at load (no watcher cron — LD-0166). | `/mstr-review` is **ad-hoc** (LD-0164): runs once at MSTR session startup per the deterministic startup directive, then on Andrew call / closeout-class signals / on-demand — NOT a 12h cron. `/govern` is Andrew-discretion only, not auto-armed (LD-0147); LD-0090 ALWAYS-PROCEED discipline still governs `/govern` WHEN Andrew loads it. `/mstr-charter` + `/compiler-ferry` + remaining MSTR skills event-triggered on inbox match. If a stale `/mstr-review` / `/watcher` cron exists from a prior session, `CronList`→`CronDelete` it. |
| `1.0.0_SA_CTO` (ws) | **NO loop — do NOT arm `/ws-charter` cron (LD-0157, Andrew direct 2026-06-05, supersedes the LD-0062 30m auto-arm).** Reachability = persistent inbox Monitor (`/watcher`, section C). | ws CTO is **event-driven** (Andrew directives + CVO findings arrive via the Monitor) + **ad-hoc** `/ws-charter` when there is charter work. The 30m self-tick wasted ticks; COO `/drive`+`/fabric-check` is the centralized tick driver. If a `/ws-charter` cron is live from a prior session, `CronList`→`CronDelete` it. |
| `1.x.0_SA_CTO` (CL) | `CronCreate /cl-charter 30m` | LD-0066 3-way split; CL is queue-pull + sequential PRD authoring; consumes Input 1/2/3 cascade |
| `2.x.0_SA_COO` | `CronCreate /drive 20m` | already operational pattern per LD-0056 |
| `3.x.0_SA_CVO` | **NO cron — do NOT arm `/spot-check` cron (LD-0164, Andrew direct 2026-06-08, supersedes the LD-0062 20m auto-arm).** `/watcher` arms the persistent inbox Monitor once at load (section C). | CVO is **event-driven** + **ad-hoc**: `/spot-check` (alignment-sweep, 2h scan body) and `/verify-channel` (project-scope verify) both fire on-demand / at closeout-class signals, not on a fixed tick. If a `/spot-check` cron is live from a prior session, `CronList`→`CronDelete` it. |
| `0.x.0_(DS\|AE\|DE\|DT\|RD)_*` Tier-2/3 worker (+ tilde-lanes) | **NO loop — do NOT arm `/work` cron (LD-0157, Andrew direct 2026-06-05, supersedes LD-0072).** `/watcher` arms the persistent inbox Monitor once at load (section C) — that is the worker's only standing mechanism. | Workers are **event-driven**: act on Monitor-delivered dispatches/TOs as they arrive; keep your broker summary an accurate status (`WORKING: <task>` / `IDLE: available` / `BLOCKED: <what>` / `BLOCKED-SOVEREIGN: <decision>`) so COO's centralized `/drive`+`/fabric-check` finds blocks. No self-ticking, no `[BLOCKED-ASK]` polling-announce — your STATUS carries the block; COO is the single tick driver. If you have a live `/work` cron from a prior session, `CronList`→`CronDelete` it. |
| `0.x.0` non-worker / unspecified | per-role basis as defined in `prompt.md`; reachability = `/watcher` arms the persistent inbox Monitor once at load (section C) | no primary cron unless prompt.md specifies one |

**Run the skill ONCE immediately after arming** to fire the first cycle (avoids the cron-interval gap before first fire):

```
CronCreate /<skill> <interval>
# then in same turn:
/<skill>   # runs first cycle now; cron picks up at next interval
```

**Loop hygiene (LD-0157 + LD-0164 + LD-0166 — self-tick + governance loops retired):** the fabric now runs on **event-driven** work (the persistent inbox Monitor is effective) + **ONE centralized standing operational loop: COO `/drive`** (which runs `/fabric-check` to find blocks across all agents). The retired self-tick loops — **`/work` (workers)** and **`/ws-charter` (ws CTO)** (LD-0157, 2026-06-05) — plus the retired governance loops — **`/mstr-review` (MSTR)** and **`/spot-check` (CVO)** (LD-0164, Andrew direct 2026-06-08) — are **NOT armed at launch**; all four remain **ad-hoc invocable** (governance review fires on Andrew call / closeout-class signals / on-demand). `/watcher` arms the persistent inbox Monitor once at load (not a loop — LD-0166 struck the `/watcher` cron; MSTR + CVO now arm ZERO crons). Rationale: agents do not need to self-tick to announce blocks — their broker STATUS carries the block and COO's centralized `/drive`+`/fabric-check` resolves it; governance review is event-shaped (a window worth reviewing is created by activity, not by the clock). If you find a stale `/watcher` / `/work` / `/ws-charter` / `/mstr-review` / `/spot-check` CronCreate job from a prior session, cancel it (`CronList` → `CronDelete`).

**CL fabric inheritance:** CL agents (`feature_clb/`) inherit this convention via cwd=ajb_workspace per LD-0033/0034 unified-broker substrate; org/XXX.md is workspace-canonical (no CL-side mirror needed). The CL CTO `/charter 30m` arming matches ws CTO arming under the LD-0062 symmetric-cadence ruling.

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
| `/loop {INPUT_SPEC}` | CTO + COO only | **Project-driver mode** — operator→validator→closure. Input spec accepts any combination of macro codes (`ADVI`), 6-char project suffixes (`ROLLUP`), and macro_project codes (`ADVI_ROLLUP`), space- or comma-separated. Resolved via `.tools/loop-resolve` to active-project list; driven one project per wake (active-first selection). See CTO/COO prompt.md "/loop dynamic mode" section for full spec. |

### Watchdog mode — what to do on each wake (workers)

Every wake, run this checklist in order. Keep it tight — the loop is supposed to be cheap.

**Steps 0 and 0.5 are deterministic gates — run them BEFORE anything else.** They
exist because the watchdog body is prescriptive enough ("inbox quiet + watcher
alive → end turn") that an agent can be pre-empted by a wake tick before it has
processed a delivered message or executed work it committed to. Both gates read
an external-observer sentinel file, so they catch the lapse without relying on
the agent remembering. (Ported from corporeal's `/loop` v0.2 body, 2026-05-11.)

0. **Deterministic delivery gate (`.unread-deliveries` sentinel):**
   ```bash
   cat org/mcp/inbox/{your_agent_folder}/.unread-deliveries 2>/dev/null
   ```
   (Tilde lanes: `org/mcp/inbox/{your_agent_folder}/~{lane}/.unread-deliveries`.)
   The persistent inbox Monitor (`inbox-watch.sh stream`) appends every delivered
   message filename here as it mv's it to `read/`. This sentinel is the failsafe
   for the case where you saw the `[INBOX]` Monitor notification but ended the turn
   without processing the message. If the file exists and is non-empty, for EACH
   filename: read it from the sibling `read/` folder, take any required action
   (RAVC ack / execute / validate), then once ALL are processed delete the sentinel
   (`rm` the file). Only then proceed.

0.5. **Active-commitment gate (`.active-commitments` ledger):**
   ```bash
   cat org/mcp/inbox/{your_agent_folder}/.active-commitments 2>/dev/null
   ```
   The `post-send-commitment.sh` PostToolUse hook appends `<ISO>|<description>`
   here automatically whenever you send a message carrying commitment language
   ("next turn I'll…", "standing by on…", "ETA…"). If the file exists and is
   non-empty, you ended a prior turn with committed work that has not run. For
   EACH line oldest-first, parse `<ISO>|<description>` and **execute the
   committed work in this turn** (do not end-turn — the watchdog is deferring to
   your active obligations), then clear it:
   ```bash
   bash org/mcp/complete-commitment.sh {your_serial} <ISO>
   ```
   Only proceed once every commitment is processed. (Manual `append-commitment.sh`
   is the fallback for a commitment the hook missed.)

1. **Inbox pull (authoritative):**
   ```python
   check_inbox("{your_serial}")
   get_agent_status("{your_serial}")
   ```
   Both paths. Act on any message this turn (RAVC ack / execute / validate). No "standing by" silence.

2. **Watcher health — the persistent inbox Monitor (DO NOT relaunch on every wake).**
   The watcher is a persistent Monitor task running `inbox-watch.sh {serial} stream`,
   armed ONCE at load. It never exits and survives in-session compaction, so on a
   normal wake there is nothing to do. **Do NOT use `TaskList` to check it** — `TaskList`
   tracks `TaskCreate` to-dos, not Monitors, and returns empty even when the Monitor
   is alive; an empty `TaskList` is NOT a dead-watcher signal (that false read makes
   agents double-arm). Check it this way instead:

   | Observation | Action |
   |-------------|--------|
   | You armed a Monitor this session and saw NO `<task-notification>` death for it (confirm: `ps -ef \| grep 'inbox-watch.sh {serial} stream'` shows a process, or `TaskOutput(<id>, block=false)` → running) | Reachable — **do nothing** |
   | `ps` shows no stream process AND none armed this session (fresh / restart) | Run `/watcher` to arm exactly one |
   | Uncertain | Run `ps` (above) first; only run `/watcher` if no process is found |

   `check_inbox` in Step 1 is the authoritative pull — it catches messages whether the
   Monitor is live or not. The Monitor is a real-time-push optimization, not a
   correctness requirement. There is no relaunch cycle, no orphan race, and no exit-143
   to diagnose anymore (that whole catalog belonged to the retired exit-on-delivery model).

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

4.5. **Git-commits ground truth check (MANDATORY each wake):**
   Heartbeat-summary-drift makes self-reports unreliable. **Heartbeat = aspirational; git = ground truth.** Run:
   ```bash
   git log --all --oneline --since="<last-wake>" --pretty=format:"%h %ai %an %s" | head -20
   git status --short
   ```
   Cross-reference against your work:
   - Commit landed under your serial since last wake → continuing forward; nothing additional needed.
   - **No commit but you're "mid-TO" → run `git status --short` for your own staged-not-committed state.** Stuck post-`git add` is a real failure mode (workers finishing execution but not running `git commit` before the watchdog tick fires). Self-catch and finish the commit, OR surface to COO if the commit is blocked.
   - Upstream commits affecting your work landed → review them before continuing; reset assumptions if needed.
   Andrew 2026-04-29 directive (post-Wave-2 Lane 1 stuck-post-git-add incident): "we need to make sure part of the tier 1 loop function is checking commits." Same check applies to workers — your own ground-truth check catches stuck-mid-closeout before it compounds.

5. **TO queue scan:**
   Read `{your_agent_folder}/task_orders/`. For each TO:
   - **HOT-REGISTRY SCOPE CHECK (mandatory, per-TO):** Before starting or continuing any TO, verify the parent project is `"status": "active"` in `org/projects/<PROJECT_CODE>.json`. If the project is NOT active (dormant, on-hold, completed, or absent from the registry), do NOT execute the TO — surface to COO as `[SCOPE-VIOLATION]` and skip. This check applies even if the TO itself is `<status>pending</status>` with all deps met.
   - `<status>pending</status>` + dependencies met + project active in hot registry → if not already mid-work, start it.
   - `<status>staged</status>` → do NOT start; waiting for GO signal (exec dispatch).
   - `<status>complete</status>` → skip.
   If you're mid-TO, confirm the project is still active before continuing (projects can be closed mid-TO).

6. **Schedule next wake:**
   - **Active** (mid-TO, expecting near-term reply from another agent, or recent message requires follow-up): `ScheduleWakeup(delaySeconds=60)`.
   - **Idle** (no active TO, no expected reply, queue quiet): `ScheduleWakeup(delaySeconds=270)`. Inside 5-min cache TTL.
   - **Never 300s.** Worst-of-both — cache-miss + immediate refire.

**Never auto-exit.** The loop runs until Andrew stops it (he manages lifecycle). If the queue is empty and there's nothing to do, still `ScheduleWakeup(delaySeconds=270)` and surface a one-line status to Andrew so he can decide whether to stop or redirect.

### Escalation signals while looped

**The never-stop rule (Tier-0 ignition law).** Agents NEVER stop at a fork. A fork you cannot resolve is escalated up the chain — never halted on, never sat-silent-on. The chain is built so something always moves: COO unblocks, MSTR resolves, Andrew rules. Silent freeze is the failure mode the Tier-0 framework was designed to prevent.

**Escalation ladder for worker agents (DS / DE / DT / AE / any ~Z tilde lane):**
`blocking peer agent` → `2.0.0_SA_COO` → `0.0.0_AB_MSTR` (Tier-0 terminal resolver) → Andrew (sovereign). COO is the unblock arbiter for operational/work-side calls. **MSTR is the terminal resolver** — authorized to make the principal's call in Andrew's absence, bounded by active Directives + the Stakes Matrix. Do NOT jump past COO unless COO is unavailable or explicitly defers; do NOT jump past MSTR to Andrew unless the call is sovereign (new product strategy, new Directive, S3 / S4 procurement) or MSTR is unreachable.

- **Got a real blocker** (ambiguity in TO, destructive op required, cross-agent wait, missing dep, compiler mandate can't pass, flex interpretation needed) → step 1: MCP the blocking peer agent. Step 2: if no response in 1 wake cycle, **MCP COO with blocker summary** — COO unblocks or escalates. Step 3: if COO defers or is unavailable, **MCP MSTR** with the blocker + COO's response (if any) — MSTR is authorized to resolve in-Directive operational forks. Step 4: only MCP Andrew directly if MSTR explicitly defers to sovereign judgment, or both COO and MSTR are unreachable. Never sit silent on a blocker for >2 wake cycles without an MCP out.
- **3 consecutive idle wakes with no observable state delta** (no message, no TO status change, no commit in your lane) → MCP COO: "3 idle cycles, appear to be waiting on external input — is there a blocker or reassignment?" COO either unblocks or flips you to idle/closed. Do NOT stop the loop autonomously; do NOT surface to Andrew directly on idle cycles.
- **Ambiguous TO language / expected value mismatch / acceptance-flex needed** → MCP COO FIRST (they own TO scope). CTO gets the flex-MCP separately per acceptance-flex rules, but COO remains the routing hub.
- **Context compacted mid-loop** → first wake after compaction: re-pull `check_inbox` + `get_agent_status` (both paths) and re-`heartbeat`. Don't trust the compacted summary's "inbox empty" claim. The persistent inbox Monitor **survives compaction** — confirm it via Step 2 (`ps -ef | grep 'inbox-watch.sh {serial} stream'`, NOT TaskList) rather than relaunching. Only re-arm (via `/watcher`) if `ps` shows no stream process.

**Why this chain shape:** workers surfacing every blocker directly to Andrew floods his context; COO has org-wide work-side visibility; MSTR has whole-fabric strategic visibility. The chain ensures (a) each rung resolves what it can, (b) Andrew only sees what genuinely requires sovereign judgment, and (c) work never stalls because every fork has a next-hop target.

**CTO / COO / CVO exception:** the Tier-1 execs escalate to MSTR (Tier-0 terminal resolver) for operational + architectural judgment calls in-Directive; they escalate to Andrew (sovereign) for new-Directive / S3-S4 / strategy calls. MSTR's role is to keep the org moving without requiring Andrew at the keyboard for every fork.

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

*Compiler tools trigger table: see CLAUDE.md § "Compiler Tools (comp-*)".*

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

### Archetype tag — required from 2026-05-25T00:00 UTC

Every substantive session-log entry includes a single-line `**archetype:** TAG` header immediately after the title. Pick one of eight: `EXPLORE` / `TRACE` / `DIAGNOSE` / `VALIDATE` / `DEPLOY` / `IMPLEMENT` / `COORDINATE` / `SCRIBE`, or `MIXED` if dominant archetype is genuinely unclear. Optional `**secondary_archetypes:** A, B` line for high-mixed cases. ~5 sec per emission; no scoring; under-classify is fine. Canonical taxonomy + weights + aggregation logic: `org/tier0/COMPILER_ARCHETYPES.md`.

The tag feeds MSTR's cross-fabric stimulus-scan signal class 6 (high-cost-archetype clusters). Compiler-tooling R&D's highest-leverage target is COST, not BUGS — archetype aggregation surfaces where time is being paid (leading indicator) rather than waiting for bites to surface (lagging). Forward-only cutover from named date; no retroactive tagging.

Heartbeat-only entries, watcher self-checks, and minor housekeeping commits do not require tags (would dilute signal).

Per LD-0043 + Opal CTO + MSTR working-session lock 2026-05-24T19:45Z. Canonical for both fabrics per CONSTITUTION Art. XV.

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

**Author + GO pairing — Non-Negotiable (Andrew directive 2026-05-23, MSTR CY-0017 finding, COO suffix-routing refinement):**

Every TO commit MUST be paired with an MCP `send_message` GO to the assignee — **addressed to the EXACT registered serial including any `~lane` suffix** — within the same operational window. A TO file landing on disk via `git commit` alone does **NOT** fire a broker push to the assignee's session, and a GO MCP addressed to the wrong serial (base when assignee registered `~C`, or vice versa) is functionally equivalent to no GO at all because the broker push routes by exact-serial channel match.

**Two failure modes the rule covers:**

1. **Missing GO** — TO file committed, no MCP send_message fired. Assignee only sees the file on next filesystem poll (polling-cadence-dependent delay, can be minutes to hours).
2. **Wrong-channel GO** — MCP fired, but addressed to the base serial when the assignee is registered under a `~lane` suffix (or vice versa). Per the MCP suffix-strip semantic, the broker push lands on the base channel; the `~lane` watcher only fires on `~lane`-channel push, so the push doesn't trigger their session — same effective gap as missing GO. Filesystem inbox still gets the write (visible on next poll), but the real-time delivery fails.

**The TO author is responsible for the GO AND for addressing it correctly.** The commit IS the authoring; the MCP GO IS the dispatch; the exact-serial addressing IS what makes the broker push reach the assignee's session. Check `<issued_to>` in the TO file; address the MCP to that exact string.

Empirical anchor: `ADVI_DEMOV1.005` commit `2991f63ea` 2026-05-23 06:50Z sat ~20 min before AE~C session-side processing. COO DID fire a paired GO MCP — but addressed to `0.7.0_AE_CloudOps` (base) while AE~C was registered as `0.7.0_AE_CloudOps~C`. Broker push followed suffix-strip semantics, landing on the base channel; AE~C's watcher (listening on `~C` channel) didn't fire. AE~C only saw the message on next filesystem poll. MSTR's CY-0017 stimulus-scan classified AE~C STALE with a convergent ask and surfaced the structural pattern.

A **structural git post-commit hook** that auto-sends GO on every `org/tier*/task_orders/*.md` commit — suffix-aware: parses `<issued_to>` exactly and addresses the MCP to that string verbatim — is a planned follow-on infra task. Until that lands, the discipline is procedural.

**COO/CTO parallel wave protocol:**
Before writing any TOs for a parallelized wave: run `comp-blast` on every affected component/script. Any node appearing in 2+ TOs' blast radii is a CROSS-DOMAIN resource — flag it in the PRD and in each relevant TO's `<cross_domain_coordination>` block. Agents must MCP-message each other before committing to cross-domain files.

---

## Closure Discipline (Non-Negotiable — SA/COO/CTO only)

Closing a project is a **2-step atomic operation**, not a single JSON edit. Both steps happen in the same commit:

1. **JSON status flip.** `org/projects/{CODE}.json` → `"status": "complete"` + add `"completed": "YYYY-MM-DD"` + rewrite `phase` narrative as closure summary + set `blocking` to "None" (or "None — {reason}" if superseded/absorbed).
2. **REGISTRY row move.** `org/projects/REGISTRY.md` → delete the row from "Active Projects" (or "Inactive / On Hold") table. Insert a new row at the TOP of "Completed / Archived Projects" table (newest-first convention) with `Completed` date column + closure notes citing ship evidence (commits, tags, supersession path).

**PRDs are NOT a close-step (amended 2026-06-03 — CVO P3 finding / CTO doctrine; CC MSTR for LD-ratification).** PRDs stay in `docs/architecture/` — do NOT archive active PRDs, and do NOT bump their top-of-file `Status:` line on close. The PRD is an authored-once design artifact; `org/projects/{CODE}.json` status is the single authoritative close-state (`org/projects/REGISTRY.md` §"Closing a project" is the canonical 2-step, which this section now matches). The older "3-step atomic close" convention (a vestigial PRD-`Status:` bump, still echoed in some completed-row narratives like YALP_FACTOR/POSITN) is **RETIRED** — bumping PRD Status created the systemic PRD-Status-lag CVO repeatedly flagged as drift when it was never authoritative.

**Why both:** we've observed JSON-flipped projects whose REGISTRY row stayed in Active for days (ADVI_ROLGAT 2026-04-17→2026-04-21; discovered in joint audit `f959fbcb`). Either step alone is silent-drift to the other. Authors of closure commits MUST edit both in one `git commit --only` so the atomicity is structural.

**Closure triggers:**
- **Complete** — all authored TOs status=complete; no authored-but-unshipped work; final-deploy mechanical only. Use when the project achieved its stated goal.
- **Complete-as-superseded** — scope fully absorbed into another active project or PRD. JSON `phase` cites the successor explicitly. Use when the work is done but not under this project's banner.
- **Cancelled** — explicit Andrew or CTO directive cancelled the work. JSON `phase` cites the directive. Different from superseded (no successor work).
- **Inactive / On Hold** — blocked by external dependency (Andrew/IT, vendor, regulatory). Stays in On Hold table; do NOT move to Completed until the external blocker clears or cancellation call is made.

**Anti-pattern — single-step closure:** flipping JSON status alone while the REGISTRY row lags. Always 2-step (JSON + REGISTRY), always one commit.

---

*Commit identity and scope discipline: see CLAUDE.md Rules 14 / 14a.*

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
