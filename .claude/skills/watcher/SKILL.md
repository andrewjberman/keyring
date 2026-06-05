---
name: watcher
description: Ensure this agent is reachable — registered LIVE on the broker with exactly one persistent inbox Monitor armed for this session. Post-LD persistent-Monitor model: the watcher is a long-running Monitor task armed ONCE at load that streams one chat notification per inbox message, survives in-session compaction, handles batches, and never exits. There is no recurring watcher loop anymore — a fresh session re-arms at startup; within a session the Monitor just keeps running. Run at session start, after a window exit / restart, or whenever reachability is in doubt. Self-scoped — only touches the invoking agent's own watcher.
---

# /watcher — Inbox Reachability (persistent-Monitor model, arm-at-load)

Confirms you are **reachable**: registered LIVE on the broker, with exactly one
**persistent inbox Monitor** streaming your inbox for this session. **Self-scoped**
— it only ever touches *your* watcher and registration.

## The model (read this first)

The inbox watcher is a **persistent Monitor task** running
`inbox-watch.sh <serial> stream`. The Monitor tool turns every stdout line the
script emits (`[INBOX] <file>`) into a chat notification, so you are interrupted
**per message while you keep working** — and the script **never exits**.

This replaces the old exit-on-delivery bash watcher (launched under Bash
`run_in_background`, which re-launched itself after every delivery). That design
was the entire reason `/watcher` used to be a recurring loop: the bash watcher
silently died, orphaned, went deaf to a prior session, or short-circuited on its
own single-watcher guard (the misleading exit-143), so it needed periodic
re-checking. The persistent Monitor removes the OLD bash-watcher failure modes:

| Old failure mode | Why it's gone |
|---|---|
| ORPHAN / PPID=1 zombie | Monitor is a harness-tracked background task, not a detached bash process |
| MULTIPLE / atomic-mv race | atomic `mv` on emit makes any overlap exactly-once anyway |
| AUTO-RESPAWN-INTERRUPT-LOST | no exit-on-delivery respawn loop; on the rare SIGTERM death you re-arm once (see caveat) |
| "deaf prior-session watcher" | a session's Monitor dies with the session; a fresh session arms its own |
| exit-143 guard short-circuit | no exit-on-delivery, no guard race (this OLD guard-race exit-143 is gone; a DIFFERENT exit-143 SIGTERM still occurs — see caveat) |
| missed 2nd+ message in a batch | the poll loops over **all** `*.md` each cycle |
| dies on compaction | a persistent Monitor normally survives in-session compaction |

**EMPIRICAL CAVEAT (2026-06-05, LD-0146 amend — supersedes the "never-off" claim).** The Monitor
is NOT "never-off." It is **self-healing, not immortal.** Corroborated across 3 agents (ws CTO /
MSTR / CVO) in one session: the stream Monitor receives **exit-143 (SIGTERM) at irregular intervals
(~18–133 min)** from an **undetermined source** (NOT a cross-agent watcher kill — the guards are
exact-serial-scoped and a stream cmdline ends in `stream`, not the serial; candidates: harness
background-task lifecycle / resource pressure / Monitor-tool interaction — likely the Claude Code
layer, not these scripts). **Delivery integrity held: 0 messages lost** across every death — the
death-notification + re-arm + `check_inbox` backstop works. So treat death as EXPECTED-and-handled:
when you see a `<task-notification status=failed>` for your Monitor's task id, run Step 2→3 (confirm
no orphan, pull inbox, re-arm). **Residual risk:** an idle/compacting agent that misses the
death-notification goes deaf until its next `check_inbox` — bounded for looped agents (every
loop body folds a turn-top `check_inbox`/`get_agent_status` pull, so max-deafness ≤ one loop
interval). SIGTERM-source investigation is LOW-priority (lossless self-heal); do not chase it as a
fire.

**Decisive reachability test — what it is NOT:** *do NOT use `TaskList`.* `TaskList`
lists `TaskCreate` to-do items, **not** Monitor/background tasks. If you never made
to-dos it returns "No tasks found" *regardless of whether your Monitor is alive* —
an empty `TaskList` is NOT evidence of a dead Monitor. Treating it as one is how
agents double-arm a second watcher on top of a healthy first (empirically observed
across multiple agents 2026-06-03). **An empty `TaskList` proves nothing about your watcher.**

**Decisive reachability test — what it IS** (any one of these, in order of convenience):
1. **Death-notification rule (primary, harness-native):** a persistent Monitor runs
   until it dies, and when it dies it fires a `<task-notification>` with status
   `failed`/`completed` for its task id. So: *if you armed a Monitor this session and
   have NOT seen a death notification for its task id → it is alive. Do nothing.*
2. **Positive check by task id:** `TaskOutput(<monitor_task_id>, block=false)` →
   `<status>running</status>` confirms alive. (You get the task id from the Monitor
   tool's return when you arm it, or from the `/tasks` CLI command.)
3. **OS-level check (task-id-independent — use after compaction when you may not
   recall the id):** `ps -ef | grep 'inbox-watch.sh <serial> stream' | grep -v grep`.
   A matching process = alive. This is reliable structural truth and the right
   fallback — *not* a discouraged heuristic.

Only arm a new Monitor if **none** of these confirm a live one (genuinely fresh
session / restart / a death notification you actually saw). When unsure, check
(2) or (3) — never re-arm off an empty `TaskList`.

## Invocation forms

| Form | Behavior |
|---|---|
| `/watcher` | Arm-at-load check, **once**. Register if STALE; arm the Monitor if absent; pull inbox; report. **No loop is armed** — the persistent Monitor is the standing mechanism. |
| `/watcher status` | Report-only: registration + Monitor presence + inbox. No changes. |
| `/watcher rearm` | Force a clean re-arm: TaskStop any existing inbox Monitor for this serial, kill any legacy bash watcher, arm a fresh stream Monitor. |
| `/watcher off` / `stop` / `Nm` / `10m` (legacy interval forms) | **Deprecated, accepted gracefully.** There is no loop to start or stop. Run the one-shot check, then if a stale `/watcher` CronCreate job exists, cancel it (Step 5) and say so. |

## When to invoke

- Session start (`org/XXX.md` Step 1b startup), and after any context compaction
  (the Monitor should still be live across compaction — this just confirms it).
- After a window exit / machine restart / fresh `/loop` wake (the prior session's
  Monitor died with it — this arms a new one).
- Whenever you cannot positively confirm a live inbox Monitor (via the death-notification
  rule + a `ps`/`TaskOutput` check — **not** TaskList).

---

## Step 0 — Identify yourself

- **Serial:** the full serial you registered under this session, **including any
  `~B`/`~C`/`~D` lane suffix**. Lane agents watch their nested dir; registering or
  arming under the base serial means your lane inbox is never watched.
- **Workspace abs path:** `/c/Users/AndrewBerman/Desktop/ajb_workspace` (the
  Monitor command must use the absolute path — the bare-path guard hook blocks
  relative `org/mcp/inbox-watch.sh` launches).

## Step 1 — Registration check

Call `get_agent_status("{serial}")`.

- **LIVE, last seen < 120s, summary reflects current work** → registration OK.
- **STALE, absent, or stale summary** → `register_agent("{serial}", summary="<current work>")`.
  A window exit always drops you to STALE — re-registering is expected.
- Lane agents register under the **full suffixed serial**.

## Step 2 — Monitor presence check (decisive — do NOT use TaskList)

Determine whether a live inbox Monitor exists, using the death-notification rule
plus a positive check. **Never** use `TaskList` here — it does not track Monitors
(see "Decisive reachability test" above) and returns empty even when your Monitor
is alive.

1. **Did you arm an inbox Monitor this session and NOT see a death notification for
   it?** → it's alive. Confirm positively if you want: `ps -ef | grep
   'inbox-watch.sh {serial} stream' | grep -v grep` (matching process = alive), or
   `TaskOutput(<task_id>, block=false)` → `running`. Reachable → skip to Step 4.
2. **No process found by `ps` AND no Monitor armed this session** (fresh session,
   restart, post-compaction with nothing running) → go to Step 3 to arm one.
3. **`/watcher rearm`** → `TaskStop` the existing Monitor (by its task id) first,
   then Step 3.

Steady state — including right after a compaction — is case 1: the persistent
Monitor is still running and `ps` confirms it. Re-arm only when `ps` shows none.

## Step 3 — Arm the persistent inbox Monitor

1. **Clear any legacy bash watcher** for this serial (transition hygiene — an old
   exit-on-delivery watcher and the new stream Monitor both mv to `read/`, so
   delivery stays exactly-once, but the legacy one is redundant). Enumerate +
   kill:
   ```bash
   bash org/mcp/watcher-status.sh {serial}   # lists any legacy watcher PIDs
   kill <pid> [<pid> ...]                     # if any were listed
   ```
2. **Arm the Monitor** — use the **Monitor tool**, `persistent: true`,
   `timeout_ms: 3600000`:
   - command: `bash /c/Users/AndrewBerman/Desktop/ajb_workspace/org/mcp/inbox-watch.sh {serial} stream`
   - The tool returns a **task id** — note it; that id is what you pass to
     `TaskOutput(<id>, block=false)` (positive liveness check) or `TaskStop(<id>)`
     (clean teardown). It is **not** visible in `TaskList`. Each `[INBOX] <file>`
     event it later emits is a new-message signal: read the file from
     `org/mcp/inbox/<agent>/read/` (the script already mv'd it there) and act.
     **You do not relaunch anything** — the Monitor keeps running.

   **BANNED:** launching `inbox-watch.sh {serial} stream` under Bash
   `run_in_background` (the Bash tool only notifies on *exit*, and stream mode
   never exits → you go silent for the session). It MUST run under the Monitor
   tool. Equally banned: the legacy bare-path relative launch (guard-hook blocked).

## Step 4 — Inbox pull (BOTH probes + ferry check)

Even with the Monitor live, pull once at load to catch anything delivered before
it armed:

```bash
check-inbox {serial}
```
```python
get_agent_status("{serial}")
```

- `check-inbox` reads **top-level** `org/mcp/inbox/{serial}/` (empty once the
  stream Monitor has mv'd a message to `read/`).
- `get_agent_status` surfaces **broker-channel** push messages.
- **Neither sees LD-0099 cross-org-root filesystem-direct ferry messages.** If you
  suspect one (a `[INBOX]` event fired but both probes are empty), scan
  `ls -t org/mcp/inbox/{serial}/read/ | head` for the newest entry — the stream
  Monitor already delivered it there.

**Act on anything found this turn** — no silent "standing by".

## Step 5 — Cancel any stale `/watcher` loop, heartbeat, report

The recurring `/watcher` loop is **retired**. If you (or a prior startup) armed
one, clean it up:

- `CronList` → if a `/watcher` job exists, `CronDelete` it.
- If you have a pending `ScheduleWakeup` chain whose prompt is `/watcher ...`,
  do **not** re-arm it (just let it lapse / re-point it at your real loop body).

Then `heartbeat("{serial}", summary="<one-line current state>")` and print:

```
/watcher {serial}
  REGISTRATION: <OK, LIVE> | <re-registered: was STALE>
  MONITOR:      <OK, live task <id>> | <armed: task <id>> | <re-armed: stopped <old>, killed legacy <pids>, task <id>>
  INBOX:        <empty> | <N message(s): acted — ...>
  LOOP:         <none — persistent Monitor is the standing mechanism> | <cancelled stale /watcher cron <id>>
```

When everything is already healthy, keep it to these lines — no extra prose.

## Notes

- **Self-scoped only.** Never TaskStop or kill a watcher for a serial that isn't
  yours.
- **No loop to keep alive.** A persistent Monitor IS the standing mechanism; the
  only re-arm trigger is a brand-new session, handled by arming at load. Do not
  add a `/watcher` ScheduleWakeup/CronCreate loop — it's obsolete and would just
  re-run an idempotent no-op.
- **Survives compaction.** The Monitor is a session task; in-session compaction
  does not end it. After a compaction, Step 2 should find it still running.
- **Belt-and-suspenders.** The Monitor is event-push; still pull `check-inbox` +
  `get_agent_status` at the top of a turn when you're expecting a near-term reply.
- Design + history: `org/XXX.md` Step 1b, `org/mcp/INBOX_WATCH_DESIGN.md`,
  and the LD record for the persistent-Monitor migration.
