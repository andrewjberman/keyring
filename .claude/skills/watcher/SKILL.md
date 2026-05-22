---
name: watcher
description: Self-check and self-heal an agent's inbox-watcher and broker registration. Verifies the agent is registered LIVE on the opal-agent-comms broker, that exactly ONE inbox-watch process is running for its serial AND was launched by the CURRENT session (tracked, not a prior-session orphan), kills orphan / relative-path / double / wrong-channel watchers, relaunches one tracked watcher, and pulls both inbox paths. Run at session start (Step 1b), on any fresh /loop wake, after a window exit or machine restart, after context compaction, or whenever watcher health is in doubt. Self-scoped — repairs only the invoking agent's own watcher and registration; never touches a peer's. Adapted for ajb_workspace; encodes the inbox-watch failure modes documented in org/XXX.md and org/mcp/INBOX_WATCH_DESIGN.md.
---

# /watcher — Inbox-Watcher & Registration Self-Check

Confirms you are **reachable**: registered LIVE on the broker, with exactly one
**tracked** `inbox-watch` process running for your serial. Detects and repairs
every documented watcher failure mode. **Self-scoped** — it fixes only *your*
watcher and registration. It never kills a peer's watcher (that causes the
atomic-`mv` race it exists to prevent).

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

## Step 0 — Identify yourself

- **Serial:** the full serial you registered under this session, **including any
  `~B`/`~C`/`~D` lane suffix**. (`SERIAL=` in `.comp-graph/.agent_context` or
  `$OPAL_AGENT_SERIAL` are fallbacks, but they can be stale or shared between
  lanes — trust the serial from your own session registration first.)
- **Channel:** CL-channel agents — the COMP_LEARNS team (`1.1.0_SA_CTO`,
  `1.1.0`/`1.2.0`/`1.3.0`/`1.4.0_DS_CompLearns`, `2.1.0_SA_COO`,
  `2.1.0_SC_CompLearns`) — use `feature_clb/org/mcp/cl-inbox-watch.sh`. Every
  other agent uses the `ajb_workspace` `inbox-watch`. The helper auto-detects
  this; just know which one you are.

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
  - VERDICT `MULTIPLE` / `ORPHAN` / `RELATIVE-PATH` / `WRONG-CHANNEL` → a stray
    watcher coexists with yours → **Step 4** to clear the strays.

## Step 4 — Remediate (KILL FIRST, THEN LAUNCH — order is mandatory)

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
   - ws agents: `inbox-watch {serial}`
   - CL agents: `bash /c/Users/AndrewBerman/Desktop/feature_clb/org/mcp/cl-inbox-watch.sh {serial}`
   - **BANNED:** `bash org/mcp/inbox-watch.sh {serial}` (relative path → PPID=1
     zombie that short-circuits the next session); any `&` form (runs invisibly,
     fires no notification — you go deaf for the session).
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

Call `heartbeat("{serial}", summary="<one-line current state>")`, then print a
fixed three-line report:

```
/watcher {serial}
  REGISTRATION: <OK, LIVE> | <re-registered: was STALE>
  WATCHER:      <OK, tracked task <id>> | <relaunched: killed <pids>, new task <id>>
  INBOX:        <empty> | <N message(s): acted — ...>
```

---

## Failure-mode reference

| Helper VERDICT | What it means | Fix |
|---|---|---|
| `NONE` | No watcher process for your serial | Step 4 launch (no kill needed) |
| `ORPHAN` | Watcher has no live eval-launcher parent (PPID=1 / dead / reparented) — a prior-session leftover | Step 4: kill, then launch |
| `MULTIPLE` | >1 watcher for your serial — atomic-`mv` race, deliveries lost | Step 4: kill ALL, then launch one |
| `RELATIVE-PATH` | Launched via banned `bash org/mcp/inbox-watch.sh` — PPID=1 zombie risk | Step 4: kill, relaunch via PATH wrapper |
| `WRONG-CHANNEL` | CL agent on the ajb watcher (or vice-versa) — watches the wrong inbox; the `kill-orphans` hook may also kill it mid-session | Step 4: kill, relaunch via the correct-channel form |
| `PROCESS-OK` | Process tree healthy — **but** confirm Step 3. A prior session's watcher also reads `PROCESS-OK` | If Step 3 = NO → Step 4 anyway |

## Notes

- **Self-scoped only.** Do not kill a watcher for a serial that is not yours.
  Fabric-wide orphan cleanup for *dead* agents is the `kill-orphans` hook's job.
- **Belt-and-suspenders.** A watcher is event-push; it is not a substitute for
  pulling `check_inbox` + `get_agent_status` at the top of a turn when you are
  expecting a near-term reply.
- **Autonomous `/loop` agents** may additionally keep the `CronCreate` 15-min
  re-registration backstop from `org/XXX.md` Step 1b — `/watcher` and the cron
  are complementary, not alternatives.
- Design + history: `org/XXX.md` Step 1b, `org/mcp/INBOX_WATCH_DESIGN.md`.
