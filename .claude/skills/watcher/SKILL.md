---
name: watcher
description: Ensure this seat is reachable: registered LIVE on the broker with exactly one persistent inbox Monitor armed for this session -- armed once at load, one notification per inbox message, survives compaction, never exits; no recurring loop. Run at session start, after a window exit or restart, or whenever reachability is in doubt. Self-scoped.
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

## ORPHAN HAZARD

**Read the arm banner** (`:159`, stderr, in the Monitor's output file): `parent-tied: pid <N>` = armed,
`parent-tied: OFF` = orphan-capable.

**An orphan is not inert — it is a thief**, and the source order is load-bearing:
```
inbox-watch.sh:120   mv "$msg" read/       <-- drains top-level. COMMITS THE THEFT.
inbox-watch.sh:124   echo "[INBOX] $base"  <-- the ONLY notification act, into a dead pipe.
```

- **`ps`, `u`, and the `read/` directory are BANNED as delivery oracles.** They are artifacts the
  *watcher* produces, and the watcher is the subject of the measurement. A file in `read/` observes
  **the watcher, not the agent** — three actors move files there (stream `:120`, legacy `:175`,
  `check_inbox(mark_read=True)`) and only the last implies an agent read anything.
- The only sound oracle for *"the agent heard it"* is one **only a live consumer can produce**: an
  agent-side ack, `TaskOutput(<monitor_task_id>) -> running`, or a broker receipt.

**Decisive reachability test — what it is NOT:** *do NOT use `TaskList`.* `TaskList`
lists `TaskCreate` to-do items, **not** Monitor/background tasks. If you never made
to-dos it returns "No tasks found" *regardless of whether your Monitor is alive* —
an empty `TaskList` is NOT evidence of a dead Monitor. Treating it as one is how
**An empty `TaskList` proves nothing about your watcher.**

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
   **A matching process is NOT proof of a live Monitor.** It proves a bash process
   exists — it says nothing about whether any Monitor task is reading its stdout.

**THE DISCRIMINATOR THAT COVERS BOTH CASES — ask WHOSE PID, not "is anything live":**
```
liveness PID == MY PID   -> IT IS MINE, ALIVE. Context-clear (or a forgotten arm). DO NOT KILL.
                            Confirm with TaskOutput(<id>) -> running if you still have the id.
liveness PID != MY PID   -> a LIVE PEER holds the serial. STOP: identity conflict -> Andrew/CTO.
serial STALE / absent    -> genuine orphan (predecessor died). Kill YOUR OWN serial's, then arm.
```

Only arm a new Monitor if **none** of these confirm a live one (genuinely fresh
session / restart / a death notification you actually saw). When unsure, check
(2) — the task-id check is the only one that observes a *consumer*. Never re-arm off
an empty `TaskList`, and never conclude "reachable" off (3) alone.

## Invocation forms

| Form | Behavior |
|---|---|
| `/watcher` | Arm-at-load check, **once**. Register if STALE; arm the Monitor if absent; pull inbox; report. **No loop is armed** — the persistent Monitor is the standing mechanism. |
| `/watcher status` | Report-only: registration + Monitor presence + inbox. No changes. |
| `/watcher rearm` | Force a clean re-arm: TaskStop the existing Monitor, **then find its bash child by WINPID and reap it with PowerShell `Stop-Process`** (Step 3.1 -- MSYS `kill` is KNOWN-INEFFECTIVE on an aged orphan here and FAILS SILENTLY), then arm a fresh stream Monitor and **VERIFY-AFTER on the arm banner's `parent-tied: pid <N>`**. **DO NOT SKIP THE CHILD KILL — `TaskStop` DOES NOT REAP IT.** |
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
- **Workspace abs path:** `<resolved-prefix>/Users/AndrewBerman/Desktop/ajb_workspace`
  — the Monitor command must use the **absolute** path (the bare-path guard hook
  blocks relative `org/mcp/inbox-watch.sh` launches), but **the drive prefix is NOT
  a constant on this box.** Resolve it per Step 3; do not hardcode `/c/` or
  `/cygdrive/c/` here.

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
   ```
   ⛔ **REAP BY WINPID WITH `Stop-Process`. MSYS `kill` AND `kill -9` ARE KNOWN-INEFFECTIVE ON AN AGED
   ORPHAN ON THIS BOX, AND THEY FAIL SILENTLY** -- no error, the process unchanged in `ps`, the seat arms a
   fresh Monitor and STAYS DEAF while the orphan keeps winning the `mv` race (`inbox-watch.sh:120` commits
   the theft, `:124` echoes into a dead pipe). `kill` is named here so nobody re-adds it as the "portable"
   form. Enumerate on the Windows plane, SCRIPT ROWS ONLY, with the START TIME that identifies an orphan:
   ```powershell
   Get-CimInstance Win32_Process -Filter "Name='bash.exe'" |
     Where-Object { $_.CommandLine -match 'inbox-watch\.sh {serial} stream' -and $_.CommandLine -notmatch ' -c ' } |
     Select-Object ProcessId, CreationDate | Sort-Object CreationDate
   # ONE row  = healthy. REAP NOTHING.
   # N>1 rows = REAP ONLY A SCRIPT ROW WHOSE CreationDate PREDATES YOUR CURRENT ARM. The live watcher is created
   #            BY the current arm, so this selector can never pick it (4.0.0_SA_CRO 98376).
   Stop-Process -Id <winpid-created-before-your-arm> -Force -Confirm:$false
   ```
   ⛔ **A DEAD PARENT IS NOT THE TEST -- IT IS THE NORMAL HEALTHY STATE.** The launching wrapper shell exits right
   after spawning the stream, so a LIVE watcher's script row reads `parent DEAD` seconds after arming. **The first
   version of this step (2026-09-19 @`138b3efd19`) defined an orphan as "a row whose parent no longer exists" and
   was broadcast to six seats; followed literally it kills the watcher the reader just armed, and its own
   VERIFY-AFTER then passes.** `2.0.0_SA_COO~O` (98368) and `4.0.0_SA_CRO` (98369) each ran the census, found
   their ONE live script row with a dead parent, and stopped before acting; `0.0.0_AB_MSTR`'s own live watcher
   reads the same. The exercise that justified the first version could not see it: that orphan was 3.5 DAYS old,
   where age and dead-parent agree. **THE DISCRIMINATOR IS AGE AGAINST YOUR LATEST ARM, AND IT IS A CONJUNCT, NOT
   AN ASIDE.** The `-notmatch ' -c '` filter drops the two wrapper shells, which match only because their `-c`
   string contains the script path. If you cannot say which row is newest-since-your-arm, REAP NOTHING and re-arm.
   **VERIFY-AFTER, never skip it:** re-run the census and require exactly ONE script row, the newest; then after
   arming (step 2) read the new Monitor's banner for `parent-tied: pid <N>` and confirm an `[INBOX]` event still
   arrives. ⚠ **TWO BOUNDS.** The banner names the WRAPPER it is tied to, never the script row -- a live wrapper
   certifies nothing about the script row's health (`2.0.0_SA_COO~G` 98372 verified the wrong row that way).
   And DELIVERY PROVES A LIVE CONSUMER EXISTS, NEVER WHICH ROW IT IS: beside an orphan the contest is a
   per-message race at `inbox-watch.sh:120`, so events can arrive while others are stolen. Delivery is a STOP
   ("events are arriving, do not reap blind"), not a SELECTOR; arm-time is the selector. A kill with no verify-after is exactly what let an orphan run for two days. Self-scoped only: YOUR
   serial's rows, never a peer's. Measured 2026-09-19:
   `2.0.0_SA_COO~G` (msg 98356, routed by `1.0.0_SA_CTO` 98359) -- orphan WINPID 16132 since 09-17, `kill`
   and `kill -9` both survived, one CTO message eaten for 33 h; `0.0.0_AB_MSTR` the same evening -- orphan
   WINPID 10352 since 09-16 07:14 (3.5 days, parent 25032 dead), reaped by `Stop-Process`, verified gone
   (MSTR did not re-test `kill`, so the ineffectiveness is one seat's measurement; the remedy is two).
   COST: one census + one read. NON-APPLICATION: a box with no aged watcher -- the census prints only live rows.
2. **Arm the Monitor** — use the **Monitor tool**, `persistent: true`,
   `timeout_ms: 3600000`:
   - **RESOLVE THE DRIVE PREFIX FIRST — DO NOT HARDCODE EITHER FORM.** Both may be mounted; `/c` is a
     non-`auto` user mount that has vanished at reboot; `/cygdrive/c` is the system-provided
     `auto,noumount` mount. The Monitor needs an **absolute** path (the guard hook blocks the relative
     form). Measure, then arm:
     ```bash
     test -d /cygdrive/c && echo /cygdrive/c/Users/AndrewBerman/Desktop/ajb_workspace \
                         || echo /c/Users/AndrewBerman/Desktop/ajb_workspace
     ```
   - command: `bash <resolved-prefix>/org/mcp/inbox-watch.sh {serial} stream`
   - **A wrong prefix does NOT fail like a wrong path — it fails as `exit 127` on a
     Monitor you have already been told is the standing mechanism.** The tool returns a
     task id and reports success; the death arrives separately as a
     `<task-notification status=failed>`.
   - **After arming, positively confirm it:** `TaskOutput(<id>, block=false)` →
     `running`. This is the one check that observes a *consumer*; do not skip it on the
     assumption that a returned task id means a live stream.
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

- `check-inbox` reads the **top-level** of your canonical inbox dir — base
  `org/mcp/inbox/{base}/`, lane `org/mcp/inbox/{base}/~{lane}/` (empty once the
  stream Monitor has mv'd a message to `read/`).
  **⛔ NEVER `org/mcp/inbox/{base}~{lane}/` (flat) — nothing in the fabric reads or
  writes it.** For a lane serial, `inbox/{serial}/` IS that dead flat path: split
  your serial into `{base}` + `~{lane}` rather than substituting it whole
  (LD-0202).
- `get_agent_status` surfaces **broker-channel** push messages.
- **Neither sees LD-0099 cross-org-root filesystem-direct ferry messages.** If you
  suspect one (a `[INBOX]` event fired but both probes are empty), scan
  `ls -t org/mcp/inbox/{base}/[~{lane}/]read/ | head` for the newest entry — the
  stream Monitor already delivered it there.

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
- Design + history: `org/XXX.md` Step 1b, `org/mcp/INBOX_WATCH_DESIGN.md`,
  and the LD record for the persistent-Monitor migration.
