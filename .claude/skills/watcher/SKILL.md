---
name: watcher
description: Self-check and self-heal an agent's inbox-watcher and broker registration, then keep checking on a recurring loop. Verifies the agent is registered LIVE on the opal-agent-comms broker, that exactly ONE inbox-watch process is running for its serial AND was launched by the CURRENT session (tracked, not a prior-session orphan), kills orphan / relative-path / double / wrong-channel watchers, relaunches one tracked watcher, pulls both inbox paths, then re-arms itself to run again. `/watcher` loops every 10m by default; `/watcher 5m` / `/watcher 30m` / `/watcher 1h` set the interval; `/watcher once` runs a single check; `/watcher off` ends the loop. Run at session start, on a fresh /loop wake, after a window exit or restart, after context compaction, or whenever watcher health is in doubt. Self-scoped — repairs only the invoking agent's own watcher; never touches a peer's. Encodes the inbox-watch failure modes from org/XXX.md and org/mcp/INBOX_WATCH_DESIGN.md.
---

# /watcher — Inbox-Watcher & Registration Self-Check (with health loop)

Confirms you are **reachable**: registered LIVE on the broker, with exactly one
**tracked** `inbox-watch` process running for your serial. Detects and repairs
every documented watcher failure mode — then **re-arms itself** so the check
recurs on an interval. **Self-scoped** — it fixes only *your* watcher and
registration. It never kills a peer's watcher (that causes the atomic-`mv` race
it exists to prevent).

## Invocation forms

| Form | Behavior |
|---|---|
| `/watcher` | Run the check, then loop — re-check **every 10 minutes** (default). |
| `/watcher 5m` / `30m` / `1h` / `90s` | Run the check, then loop at the given interval. |
| `/watcher once` | Run the check **once** — no loop. |
| `/watcher off` (or `stop`) | Run a final check and **end the loop** — do not re-arm. |

## When to invoke

- Session start (the `org/XXX.md` Step 1b MCP startup), and after any context compaction.
- Any fresh `/loop` wake, or after a window exit / machine restart.
- Whenever you cannot positively confirm you launched a watcher **this session**.
- Inside a CTO/COO supervision sweep, dispatched to each live agent to run on itself.

## The core principle (read this first)

A watcher only delivers messages to the session that launched it **via the Bash
tool with `run_in_background: true`**. A watcher process can look perfectly
healthy in `ps` — correct path, live parent — and still be **deaf**: if a *prior*
session launched it, its exit notification fires into a dead session and the
inbox file it wins via the atomic `mv` race is silently swallowed.

> **The decisive test is your own session task list, not `ps`.**
> If you did not launch a background `inbox-watch` task *this session*, you have
> no tracked watcher — no matter what `ps` shows.

---

## Step 0 — Parse the argument, identify yourself

**Parse the invocation argument** into a mode + interval:

- No argument → **loop mode**, interval **600s (10m)**.
- `once` → **single mode** (run Steps 1-6, skip Step 7).
- `off` / `stop` → **stop mode** (run Steps 1-6, skip Step 7, report the loop ended).
- An interval token → **loop mode** at that interval. Accept `Nm` (minutes),
  `Nh` (hours), `Ns` (seconds), or a bare `N` (minutes). Convert to seconds and
  **clamp to [60, 3600]** — the `ScheduleWakeup` range. If the request fell
  outside the range, say so in the report (e.g. `2h -> clamped to 60m`).

**Identify yourself:**

- **Serial:** the full serial you registered under this session, **including any
  `~B`/`~C`/`~D` lane suffix**. (`SERIAL=` in `.comp-graph/.agent_context` or
  `$OPAL_AGENT_SERIAL` are fallbacks, but they can be stale or shared between
  lanes — trust the serial from your own session registration first.)
- **Channel:** post-LD-0034 unified broker + inbox migration (`opal-agent-comms`
  canonical; `complearns-agent-comms` retired) — **ALL agents (ws + CL) use the
  ws-rooted `inbox-watch` PATH wrapper**, which polls the unified inbox at
  `ajb_workspace/org/mcp/inbox/{serial}/`. CL serials have inbox directories
  under that unified path; the legacy `feature_clb/org/mcp/cl_inbox/` path is
  orphaned. The prior CL-specific carve-out (`cl-inbox-watch.sh` against the
  legacy CL path) is retired. Empirically confirmed twice 2026-05-24 by CL CTO
  + CL CVO: agents following the old carve-out launch deaf watchers against an
  empty directory and never fire task-notifications.

## Step 1 — Registration check

Call `get_agent_status("{serial}")`.

- **LIVE, last seen < 120s, summary reflects current work** → registration OK.
- **STALE, absent, or stale summary** → call
  `register_agent("{serial}", summary="<current work>")`. A window exit always
  drops you to STALE — re-registering is expected, not exceptional.
- Lane agents (`~B`/`~C`/`~D`): register under the **full suffixed serial**.
  Registering under the base serial means your lane inbox is never watched.

## Step 2 — Watcher process scan

Run the diagnostic (Bash tool, **foreground**):

```bash
bash org/mcp/watcher-status.sh {serial}
```

Read the `VERDICT:` line. It is `NONE`, `WRONG-CHANNEL`, `MULTIPLE`, `ORPHAN`,
`RELATIVE-PATH`, or `PROCESS-OK`.

## Step 3 — The tracked-ness test (decisive)

Ask yourself one question:

> **Did I launch an `inbox-watch` via the Bash tool (`run_in_background: true`)
> in THIS session, and have I NOT since seen its completion task-notification?**

- **NO** → you have no tracked watcher. Go to **Step 4 (full remediation)**
  regardless of the helper VERDICT — even if it says `PROCESS-OK` (that watcher
  belongs to a dead session).
- **YES** → you have a tracked watcher.
  - VERDICT `PROCESS-OK` with exactly one watcher → healthy. Skip to **Step 5**.
  - VERDICT `ORPHAN` with exactly one watcher AND your latest tracked task's
    completion task-notification has NOT yet fired → this is likely your tracked
    watcher whose launcher shell detached (PPID reparented to 1); the watcher
    itself is still polling correctly. Treat as PROCESS-OK-equivalent. Skip to
    **Step 5**.
  - VERDICT `ORPHAN` with exactly one watcher AND your latest tracked task's
    completion task-notification HAS fired → that single PID is the legitimate
    auto-respawn copy spawned by `inbox-watch.sh:130-135` after delivery
    (still polling but deaf — no Claude Code interrupt path). **Step 4** to
    kill + launch a fresh tracked watcher to restore interrupt coverage.
  - VERDICT `MULTIPLE` / `RELATIVE-PATH` / `WRONG-CHANNEL` → strays coexist with
    yours → **Step 4** to clear.

> On a **recurring loop cycle**: a watcher you launched earlier in the *same*
> session and have not seen complete still counts as tracked — most loop cycles
> will pass Step 3 = YES and land on `PROCESS-OK`. That is the healthy steady
> state; the cycle is then a ~10s no-op. The loop earns its keep on the cycle
> *after* a watcher silently dies or a window exit drops your registration.

## Step 4 — Remediate (KILL FIRST, THEN LAUNCH — order is mandatory)

**Step 4 fires only when Step 3 disambiguation says "stray exists" or "interrupt
coverage lost".** Single-PID `ORPHAN` with no task-notification yet seen = your
own tracked watcher in a legit detached state — skip Step 4 (the kill would
churn your tracked watcher unnecessarily, then the relaunch's single-watcher-
guard would race against the killed PID's exit). Single-PID `ORPHAN` after
task-notification fired = legitimate auto-respawn copy (deaf to interrupts);
Step 4 kills it + launches fresh tracked to restore interrupt path.

`inbox-watch.sh` has a single-watcher guard: if **any** watcher for your serial
is already running, a new launch exits 0 immediately. Claude Code surfaces that
guard-exit as a misleading **exit 143**, and you are left with only the stale
(deaf) watcher. So strays must die *before* you launch.

1. **Kill every watcher PID** the helper listed for your serial:
   ```bash
   kill <pid> [<pid> ...]
   ```
2. **Verify they are gone** — re-run `bash org/mcp/watcher-status.sh {serial}`
   and confirm `VERDICT: NONE`. If a PID survives, `kill -9 <pid>`.
3. **Launch exactly ONE tracked watcher** — Bash tool, `run_in_background: true`,
   **no trailing `&`**:
   - **ALL agents (ws + CL, post-LD-0034 unified broker + inbox):**
     `inbox-watch {serial}` (PATH wrapper exec's the ws-rooted absolute path
     `bash /c/Users/AndrewBerman/Desktop/ajb_workspace/org/mcp/inbox-watch.sh {serial}`
     which polls the unified inbox).
   - **BANNED:** `bash org/mcp/inbox-watch.sh {serial}` (relative path → PPID=1
     zombie that short-circuits the next session); any `&` form (runs invisibly,
     fires no notification — you go deaf for the session); the retired
     `feature_clb/org/mcp/cl-inbox-watch.sh` legacy CL-channel script (polls
     orphaned `feature_clb/org/mcp/cl_inbox/` post-LD-0034 — deaf watcher).
4. The Bash tool returns a **background task ID**. That ID is your proof of
   tracking — note it. When it later completes, that is a new-message signal:
   pull the inbox (Step 5) and relaunch the watcher (one delivery = one relaunch).

## Step 5 — Inbox pull (both paths, always)

```bash
check-inbox {serial}
```
```python
get_agent_status("{serial}")
```

`check-inbox` reads the filesystem inbox; `get_agent_status` surfaces
broker-channel messages. Either can hold a message the other misses — run both.
**Act on anything found this turn** (ack, do the work, or validate evidence) —
no silent "standing by".

## Step 6 — Heartbeat and report

Call `heartbeat("{serial}", summary="<one-line current state>")`, then print the
fixed report:

```
/watcher {serial}
  REGISTRATION: <OK, LIVE> | <re-registered: was STALE>
  WATCHER:      <OK, tracked task <id>> | <relaunched: killed <pids>, new task <id>>
  INBOX:        <empty> | <N message(s): acted — ...>
  LOOP:         <next check in <interval> (re-armed)> | <single run> | <loop ended>
```

When a loop cycle finds everything healthy and unchanged, keep the report to
exactly these lines — no extra prose. A quiet loop should be quiet.

## Step 7 — Re-arm the loop (loop mode only)

**Skip this step entirely in `once` and `off`/`stop` mode** — that is what ends
the loop.

In loop mode, re-arm the next cycle as the **last action of the turn**:

```
ScheduleWakeup(
  delaySeconds = <interval in seconds>,
  reason       = "/watcher health loop -- next inbox-watcher + registration check in <interval>",
  prompt       = "/watcher <interval as the user typed it, or bare /watcher for the 10m default>"
)
```

Passing the same interval back as the `prompt` is what makes the cadence
persist — each firing re-runs this skill, which re-arms again. Exactly one
wakeup is ever pending, so there is no cron build-up to clean.

**Guard — do not stack ScheduleWakeup chains.** If you are *already* running a
primary loop driven by a `ScheduleWakeup` chain (another /watcher invocation in
loop mode, a self-paced `/loop` body), do **not** arm a separate /watcher
ScheduleWakeup — only one ScheduleWakeup is ever pending, so a second arming
clobbers the first. Treat this invocation as `once` mode and make sure the
primary loop body runs the /watcher check each tick.

**CronCreate-driven primary loops are EXEMPT from the stack guard** (LD-0082
pattern). MSTR + Tier-1 execs run CronCreate-armed primary loops (`/mstr-review
12h`, `/ws-charter 30m`, `/drive 20m`, `/spot-check 20m`); arming a separate
`/watcher 10m` ScheduleWakeup alongside one of these is permitted — CronCreate
schedules don't interfere with ScheduleWakeup pending state. Two separate
mechanisms, no collision. The no-stack guard is for ScheduleWakeup chains only.

The standalone `/watcher` loop is for agents **not** otherwise looping; it
doubles as a lightweight keep-alive.

**To stop a running loop:** invoke `/watcher off`. The cycle that is currently
pending will fire once more; respond to it with `/watcher off` (or just let that
final cycle run and not re-arm). The loop then ends.

---

## Failure-mode reference

| Helper VERDICT | What it means | Fix |
|---|---|---|
| `NONE` | No watcher process for your serial | Step 4 launch (no kill needed) |
| `ORPHAN` | Watcher has no live eval-launcher parent (PPID=1 / dead / reparented). THREE sub-cases: (1) prior-session leftover; (2) THIS-session tracked watcher whose launcher shell detached (task-notification not yet fired); (3) THIS-session auto-respawn copy from `inbox-watch.sh:130-135` post-delivery (task-notification fired, untracked respawn polling without interrupt path). Disambiguate via Step 3. | (1)/(3): Step 4 kill + relaunch (restore interrupt path). (2): PROCESS-OK-equivalent; skip Step 4. |
| `MULTIPLE` | >1 watcher for your serial — atomic-`mv` race, deliveries lost | Step 4: kill ALL, then launch one |
| `RELATIVE-PATH` | Launched via banned `bash org/mcp/inbox-watch.sh` — PPID=1 zombie risk | Step 4: kill, relaunch via PATH wrapper |
| `WRONG-CHANNEL` | Watcher launched against the retired `feature_clb/org/mcp/cl-inbox-watch.sh` legacy CL path (orphaned post-LD-0034 unified broker + inbox migration); polls empty directory, deaf to deliveries | Step 4: kill, relaunch via the ws-rooted `inbox-watch {serial}` PATH wrapper (all agents, ws + CL, use the unified path post-LD-0034) |
| `PROCESS-OK` | Process tree healthy — **but** confirm Step 3. A prior session's watcher also reads `PROCESS-OK` | If Step 3 = NO → Step 4 anyway |

## Notes

- **Self-scoped only.** Do not kill a watcher for a serial that is not yours.
  Fabric-wide orphan cleanup for *dead* agents is the `kill-orphans` hook's job.
- **Belt-and-suspenders.** A watcher is event-push; it is not a substitute for
  pulling `check_inbox` + `get_agent_status` at the top of a turn when you are
  expecting a near-term reply. The loop is a third layer under both.
- **The loop interacts with messages.** If a watcher-exit task-notification
  arrives between loop cycles, handle it immediately (pull inbox + relaunch the
  watcher) — do not wait for the next `/watcher` cycle. The loop is a backstop,
  not the primary delivery path.
- Design + history: `org/XXX.md` Step 1b, `org/mcp/INBOX_WATCH_DESIGN.md`.
