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
the broker; launch `/watcher`; read `CONSTITUTION.md` + `STAKES_MATRIX.md` +
`DIRECTIVES.md` in full; then invoke `/govern`. MSTR has no standard agent home
folder — `org/tier0/` is its domain and the Constitution is its persona. If no
ignition-valid Directive exists, `/govern` scans and reports only — it originates
nothing.

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

**Canonical launch form (2026-05-12):** use `inbox-watch {your_serial}` (PATH wrapper) or, fallback, `bash /c/Users/AndrewBerman/Desktop/ajb_workspace/org/mcp/inbox-watch.sh {your_serial}`. **BANNED:** `bash org/mcp/inbox-watch.sh {your_serial}` (relative path). Auto-respawn propagates `$0`, so a relative launch creates bare-path PPID=1 zombies that survive session death and short-circuit the *next* session's tracked launch via the single-watcher guard — Claude Code surfaces that guard-exit-0 as a misleading **exit 143** in the task output. Diagnose: `ps -ef | grep "inbox-watch\.sh {serial}$" | grep -v eval` → kill PPID=1 zombie → relaunch via PATH wrapper. Mechanism + history: `org/mcp/INBOX_WATCH_DESIGN.md` § "Failure mode: 143 / zombie short-circuit".

**BANNED: `bash org/mcp/inbox-watch.sh {serial} &`** — bare shell `&` looks
identical but is completely broken. The task-notification that interrupts the
agent ONLY fires for processes launched via the Bash tool with
`run_in_background: true`. A `&` process runs invisibly, exits invisibly, and
the agent is deaf for the rest of the session. Incident: 0.6.0_AE 2026-04-20.

**BANNED: untracked auto-respawns.** If an `inbox-watch.sh` process is running
that you did NOT launch via the Bash tool with `run_in_background: true` this
session (respawn from a stale CronCreate, a prior session's orphan, or any
other auto-spawn mechanism), it is **deaf** — its stdout is disconnected from
the Claude Code task tracker, so its exit will NOT fire a task-notification
and inbox files it wins via the atomic `mv` race are silently swallowed. An
untracked watcher appears to be working but is silently masking missed
deliveries.

**Required response when you observe an untracked watcher:** kill the untracked
PID, then immediately launch a tracked watcher in the same turn so it shows up
in the session task tracker. Steps:

1. Identify the orphan PID via `ps -ef | grep '[i]nbox-watch'`.
2. `kill <pid>` (or `kill <pid1> <pid2>` for multiple PIDs).
3. Relaunch via the Bash tool with `run_in_background: true` (NOT shell `&`).

Two simultaneous watchers = orphan race (one wins the atomic `mv`; the others'
deliveries are lost). Correct state is exactly one tracked watcher, OR zero
watchers + `check_inbox` pulled at the top of every turn. Untracked watchers
are ALWAYS WRONG, even when they look like they are running fine.
Andrew empirical 2026-05-05: "the respawn auto-launched at 334721. I need to
kill that too, then immediately launch a tracked watcher via run_in_background
so it shows in the session." This rule formalizes that pattern.

**Post-LD-0034 unified broker + inbox migration (2026-05-24).** ALL agents
(ws + CL combined) use the ws-rooted `inbox-watch` PATH wrapper, which polls
the unified inbox at `ajb_workspace/org/mcp/inbox/{serial}/`. CL serials
(`1.1.0_SA_CTO`, `1.1.0`/`1.2.0`/`1.3.0`/`1.4.0_DS_CompLearns`, `2.1.0_SA_COO`,
`2.1.0_SC_CompLearns`, `3.1.0_SA_CVO`) all have inbox directories under that
unified path; the legacy `feature_clb/org/mcp/cl_inbox/` path is orphaned.
The prior CL-specific carve-out (`cl-inbox-watch.sh` against the legacy CL
path) is **retired**. Empirically confirmed twice 2026-05-24 by CL CTO + CL
CVO: agents following the old carve-out launch deaf watchers against an empty
directory and never fire task-notifications. Outbound MCP still works
(broker push routes by serial-prefix on the unified channel) + `check_inbox`
/ `get_agent_status` still surface inbound on next pull, but the real-time
watcher-exit task-notification never fires. The `kill-orphans` hook's
`cmdline contains $WORKSPACE` filter does NOT classify ws-rooted CL watchers
as stale (the prior "Why" paragraph misread the filter polarity — it KEEPS
workspace-matching cmdlines, not kills them); empirically validated by CL
agents running cleanly on ws-rooted watchers across many cycles since
LD-0034. Full cross-channel architecture: `docs/architecture/AGENT_COMMS_ARCHITECTURE.md`.

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

**Autonomous /loop agents — CronCreate backstop (Option 2):**
If you will be running in `/loop` mode for an extended session, add a periodic re-registration
cron immediately after your initial inbox-watch launch. This replaces untracked auto-respawn
copies with tracked instances every 15 minutes, restoring full interrupt coverage without
requiring perfect relaunch discipline after every notification:

```python
# Run once at session startup, after initial inbox-watch launch
CronCreate(
    interval=900,
    prompt="Relaunch inbox-watch for interrupt coverage: use the Bash tool with run_in_background=true to run bash org/mcp/inbox-watch.sh {your_serial}"
)
```

The cron is a backstop, not a replacement for Option 1 (relaunch after every notification).
Use both. Full design rationale: `org/mcp/INBOX_WATCH_DESIGN.md`.

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
| `0.0.0_AB_MSTR` | `CronCreate /mstr-review 12h` (ONLY periodic loop) + `/watcher 10m` heartbeat; `/mstr-charter` + `/compiler-ferry` + 3 other MSTR skills event-triggered on inbox match | per LD-0069 ratification 2026-05-25 (`04f705733`) /govern periodic loop RETIRED; MSTR = 1 loop + 5 event-triggered skills; /mstr-review 12h is the sole MSTR cron |
| `1.0.0_SA_CTO` (ws) | `CronCreate /ws-charter 30m` | LD-0062 30m symmetric cadence + LD-0066 3-way split; ws is direction-only + REPAIR-AMENDMENT (CVO-finding gate) per LD-0065 |
| `1.x.0_SA_CTO` (CL) | `CronCreate /cl-charter 30m` | LD-0066 3-way split; CL is queue-pull + sequential PRD authoring; consumes Input 1/2/3 cascade |
| `2.x.0_SA_COO` | `CronCreate /drive 20m` | already operational pattern per LD-0056 |
| `3.x.0_SA_CVO` | `CronCreate /spot-check 20m` + event-trigger arming for `/verify-channel` | event-based per LD-0062 trigger refinement; 2h scan body |
| `0.x.0` / Tier-2 worker | per-role basis as defined in `prompt.md`; default = `/watcher 10m` only (already armed in section A) | no primary cron unless prompt.md specifies one |

**Run the skill ONCE immediately after arming** to fire the first cycle (avoids the cron-interval gap before first fire):

```
CronCreate /<skill> <interval>
# then in same turn:
/<skill>   # runs first cycle now; cron picks up at next interval
```

**Two-loop guard (already in `/watcher` SKILL.md):** if a primary cron is armed for your role, `/watcher` MUST NOT also arm a separate ScheduleWakeup chain — it folds inline (Steps 1-5 only). Same principle applies across all loop skills: arm exactly ONE primary cron per agent; other skills fold inline OR are event-triggered. Per LD-0062 loop body skeleton: `/watcher` Steps 1-5 fold into the primary cron tick; standalone `/watcher` loop is for agents NOT otherwise looping (Tier-2 default).

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
   `inbox-watch.sh` appends every delivered message filename here on exit —
   including deliveries the untracked auto-respawn copy made silently with no
   task-notification. If the file exists and is non-empty, for EACH filename:
   read it from the sibling `read/` folder, take any required action (RAVC ack /
   execute / validate), then once ALL are processed delete the sentinel
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

**The never-stop rule (Tier-0 ignition law).** Agents NEVER stop at a fork. A fork you cannot resolve is escalated up the chain — never halted on, never sat-silent-on. The chain is built so something always moves: COO unblocks, MSTR resolves, Andrew rules. Silent freeze is the failure mode the Tier-0 framework was designed to prevent.

**Escalation ladder for worker agents (DS / DE / DT / AE / any ~Z tilde lane):**
`blocking peer agent` → `2.0.0_SA_COO` → `0.0.0_AB_MSTR` (Tier-0 terminal resolver) → Andrew (sovereign). COO is the unblock arbiter for operational/work-side calls. **MSTR is the terminal resolver** — authorized to make the principal's call in Andrew's absence, bounded by active Directives + the Stakes Matrix. Do NOT jump past COO unless COO is unavailable or explicitly defers; do NOT jump past MSTR to Andrew unless the call is sovereign (new product strategy, new Directive, S3 / S4 procurement) or MSTR is unreachable.

- **Got a real blocker** (ambiguity in TO, destructive op required, cross-agent wait, missing dep, compiler mandate can't pass, flex interpretation needed) → step 1: MCP the blocking peer agent. Step 2: if no response in 1 wake cycle, **MCP COO with blocker summary** — COO unblocks or escalates. Step 3: if COO defers or is unavailable, **MCP MSTR** with the blocker + COO's response (if any) — MSTR is authorized to resolve in-Directive operational forks. Step 4: only MCP Andrew directly if MSTR explicitly defers to sovereign judgment, or both COO and MSTR are unreachable. Never sit silent on a blocker for >2 wake cycles without an MCP out.
- **3 consecutive idle wakes with no observable state delta** (no message, no TO status change, no commit in your lane) → MCP COO: "3 idle cycles, appear to be waiting on external input — is there a blocker or reassignment?" COO either unblocks or flips you to idle/closed. Do NOT stop the loop autonomously; do NOT surface to Andrew directly on idle cycles.
- **Ambiguous TO language / expected value mismatch / acceptance-flex needed** → MCP COO FIRST (they own TO scope). CTO gets the flex-MCP separately per acceptance-flex rules, but COO remains the routing hub.
- **Context compacted mid-loop** → first wake after compaction: re-run full Step 1b startup (register + inbox-watch + check_inbox + both paths). Don't trust the compacted summary's "inbox empty" claim.

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
.tools/safe-commit.sh --author="{serial} <{serial}@opal.agent>" -m "message" -- file1 file2 file3
```
Author = the agent. Committer = Andrew. Only alphanumeric, `.`, `_`, `@` in author fields.

**Use `.tools/safe-commit.sh` (ADHC_OWNPTH.007) for every commit.** The wrapper checks the staged index against your declared pathspec, aborts on contamination (or logs `--force` bypasses to `org/git-author-override-audit.log`), then runs `git commit --only -- <paths>`. Documented fallback when the wrapper is unavailable in your worktree: bare `git commit --only --author="..." -m "..." -- <paths>` — but you lose the index-contamination guard. Verify the wrapper exists in your tree before relying on the fallback.

## Commit Scope Discipline (Non-Negotiable)

**Commit ONLY the files your task order told you to touch. Never sweep the working tree.**

- **BANNED:** `git add -A`, `git add .`, `git add --all`, `git commit -a`, `git commit --all`, `git add <files>` followed by a bare `git commit` — any pattern that uses the shared index.
- **REQUIRED:** `.tools/safe-commit.sh --author "..." -m "..." -- <file1> <file2> ...` — list every path explicitly after `--`. The wrapper aborts if the staged index contains anything outside the pathspec, then runs `git commit --only -- <paths>` so the commit is scoped regardless of what else is staged.
- **Documented fallback** (only when wrapper unavailable): `git commit --only -- <file1> <file2> ...`. List every path explicitly after `--`; no prior `git add` needed (`--only` reads the working tree directly). You forfeit the contamination guard — be certain about your pathspec.
- **If you see dirty files outside your scope:** leave them alone. Do not stash, do not commit "to clean up", do not include them "while you're at it". Another agent is probably working on them right now.
- **One task order = one logical commit scope.** If your work spans multiple task orders, make multiple commits, each scoped to its own TO.

**Why the wrapper is mandatory:** During hectic multi-agent MCP sessions, multiple agents have dirty working trees and staged files at the same time. Bare `git commit` (even after `git add <specific files>`) commits the entire shared index — sweeping in any files another agent staged in the window between your `git add` and your `git commit`. Even disciplined `git commit --only -- <paths>` fails silently if you typo a path or miss one — the wrapper's pre-commit diff catches that. Three CLASS-C incidents on 2026-04-27 (DT `record-terraform-deploy.sh` 13:04Z; AE 0.7 partial restore; COO `f84c2df4` 17:49Z) had `--only` discipline at the *intent* level but missed at the *mechanical* level. The wrapper makes the mechanical check structural.

**Gotcha — gitignored prefixes need `git add -f`:** `safe-commit.sh --only` only commits files git already tracks. New files under gitignored directories (e.g. `.tools/`) need an explicit `git add -f <path>` first so the wrapper's pre-commit diff sees them. Caught AE during the wrapper bootstrap commit `1998340f`.

The only exception to the wrapper requirement is a commit whose explicit purpose is a bulk cleanup (rare, and must be called out in the commit message).

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
