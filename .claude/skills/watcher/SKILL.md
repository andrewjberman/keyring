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

| Old failure mode | Status under the Monitor model |
|---|---|
| ORPHAN / PPID=1 zombie | **STILL LIVE — see ORPHAN HAZARD below.** The Monitor *task* is harness-tracked; the `bash inbox-watch.sh` *child it spawns* is a detached bash process that OUTLIVES the session. |
| MULTIPLE / atomic-mv race | atomic `mv` on emit makes any overlap exactly-once — **to whichever stream wins.** An orphan that wins is a message you never see. |
| AUTO-RESPAWN-INTERRUPT-LOST | no exit-on-delivery respawn loop; on the rare SIGTERM death you re-arm once (see caveat) |
| "deaf prior-session watcher" | **STILL LIVE.** The Monitor task dies with the session; **its bash child does not.** |
| exit-143 guard short-circuit | no exit-on-delivery, no guard race (this OLD guard-race exit-143 is gone; a DIFFERENT exit-143 SIGTERM still occurs — see caveat) |
| missed 2nd+ message in a batch | the poll loops over **all** `*.md` each cycle |
| dies on compaction | a persistent Monitor normally survives in-session compaction |

## ORPHAN HAZARD — the class this migration did NOT retire (CTO, 2026-07-10, source-confirmed + exercised)

The two rows above were previously recorded as "gone." **They are not.** Both were falsified on a
routine `/watcher` startup: `1.0.0_SA_CTO` found pid 2124 (`inbox-watch.sh 1.0.0_SA_CTO stream`,
parent dead) holding its own inbox, and `0.4.0_DS_ClientPlatform` had a **7h17m orphan** (pid 31391)
polling the mailbox of an agent that was `NOT REGISTERED`.

⛔ **THE MECHANISM SENTENCE THAT STOOD HERE WAS FALSE FOR SIX WEEKS, AND IT WAS FALSE ABOUT A FIX THIS
SEAT AUTHORED.** It read: *"`inbox-watch.sh:113` is `while true` with no parent-liveness check and no exit
path ... the bash child keeps polling forever."* **Corrected 2026-08-27, every line read at source:**
`:112-120` names the block *PARENT-LIVENESS SELF-EXIT (2026-07-14, 0.0.0_AB_MSTR -- the orphan-thief ROOT
fix)*; `:161-165` tests `kill -0 "$WATCH_PARENT"`, appends `WATCHER-SELF-EXIT` to `orphan-audit.log`, and
`exit 0`s. **There IS an exit path.** `orphan-audit.log` at this device: **458 `WATCHER-SELF-EXIT` of 471
lines** — the routine path.

⚠ **NOT "orphans are solved."** `:137-141` sets `PARENT_CHECK=0` when `INBOX_WATCH_NO_PARENT_CHECK` is set
**or `$PPID <= 1`** — a deliberate fail-open, because MSYS can render a live non-MSYS parent as 1 and a naive
check would make healthy watchers suicide (the documented 7-false-positive trap). **Never kill on a probe that
cannot see its subject.** Orphans remain possible in exactly that cell, so both halves must travel together.
**Read the arm banner** (`:159`, stderr, in the Monitor's output file): `parent-tied: pid <N>` = armed,
`parent-tied: OFF` = orphan-capable. ⛔ **This instruction has NO INSTRUMENT on `teams-watch.py`** — that
engine has no banner equivalent (0.0.0_AB_MSTR~Z, verified at source; owner `0.5.0_AE_OpalETL~Z`), so a seat
arming it cannot read its protection state and the honest answer is *unknown, and it cannot self-exit*.

⛔ **NOTHING ABOUT ORACLES CHANGES, AND THIS ARGUES THE OTHER WAY.** A self-exit narrows how orphans are
BORN; it changes nothing about how you may REASON. Do not read "orphans are rarer" as licence to infer
delivery from a drained inbox. When an orphan DOES exist, the source order below is still load-bearing: **An orphan is not inert — it is a thief**, and the source order is load-bearing:

```
inbox-watch.sh:120   mv "$msg" read/       <-- drains top-level. COMMITS THE THEFT.
inbox-watch.sh:124   echo "[INBOX] $base"  <-- the ONLY notification act, into a dead pipe.
```

**Consequence — the reachability check is ANTI-CORRELATED with the truth.** A verdict of
`w>0 && u==0 -> REACHABLE` is *manufactured by the orphan*: `w>0` because `ps` sees a live process
(it **cannot** see whether any Monitor task reads that process's stdout — "has a live consumer" is
not a property of the process); `u==0` **because the orphan drained the inbox at `:120`**. The more
completely an agent is deaf, the more perfectly both limbs hold. And because `:120` precedes `:124`,
`w` flips `1->0` only *after* a message is already lost.

**Therefore:**
- **`ps`, `u`, and the `read/` directory are BANNED as delivery oracles.** They are artifacts the
  *watcher* produces, and the watcher is the subject of the measurement. A file in `read/` observes
  **the watcher, not the agent** — three actors move files there (stream `:120`, legacy `:175`,
  `check_inbox(mark_read=True)`) and only the last implies an agent read anything.
- The only sound oracle for *"the agent heard it"* is one **only a live consumer can produce**: an
  agent-side ack, `TaskOutput(<monitor_task_id>) -> running`, or a broker receipt.
- **`watcher-status.sh` CANNOT SEE STREAM WATCHERS AT ALL.** `:63` matches `awk '$NF == serial'`, and
  a stream cmdline's `$NF` is `stream`. It prints `VERDICT: NONE` while an orphan runs. Its
  `PRIOR-SESSION-ORPHAN` subcase (`:120-138`) is **dead code** — guarded by `COUNT -eq 1` when
  `COUNT` is structurally `0`. *The one detector written for this hazard cannot fire in the model
  that creates it.* Do not use it as a liveness oracle; Step 3.1 keeps it only to list **legacy** watchers.
- **CORRECTED 2026-07-10 — I asserted this from a DOC and it is FALSE AT SOURCE.** I wrote *"`/kill` explicitly
  exempts `inbox-watch.sh`; nothing reaps these."* **A reaper exists and it TARGETS them:**
  `.tools/kill-orphans:95` — `PATTERNS='inbox-watch\.sh|check-inbox\.sh|agent-poller\.py'`. The `/kill` **skill doc**
  (`.claude/skills/kill/SKILL.md:40`) says those processes are never touched. **Two records, two stories —
  declarative drift, not an absent reaper.** I read the description and never opened the code (Rule 22), and I
  inferred *"no reaper"* from *"an orphan lived 7h17m"* — **absence-for-mechanism**, the substitution this whole
  section exists to name.
- **RESOLVED 2026-07-10 by exercise (COO, `ab69e619b`, dry-run throughout): THE REAPER IS GATED ON THE DEAD AGENT'S
  OWN RETURN.** `org/mcp/hook_register_orphan_cleanup.py` is a **PostToolUse hook firing after `register_agent`**,
  scoped `kill-orphans --serial S --force`. **pid 31391 survived 7h17m because the only thing that would have reaped
  it is the return of the agent that died** (DS-base `register` events after 18:28Z: **0**; control `0.7.0`: 2).
- **AND THE BLIND SPOT WAS CREATED BY A CORRECT FIX.** That scoped hook *replaced* a fabric-wide `--stale --force`
  sweep which had been **reaping LIVE watchers** (Andrew-direct 2026-06-15 — the exit-143 incident recorded at
  `kill-orphans:131-139`). **The remedy for over-reaping produced under-reaping, and under-reaping is the mode that
  FORGES liveness** — an unreaped orphan then manufactures `w>0 && u==0 REACHABLE` for the serial it outlived.
  **The narrow version is right. Do not widen it.** A lane that dies and is never respawned leaves an orphan nothing
  will ever collect; that is the residual, and the fix is the ACK, not a wider sweep.
- **STILL UNDETERMINED — and it is the honest kind:** whether `kill-orphans` has ever fired *at all*. Its header
  claims every reap is audited as `KILL-ORPHAN` lines in `agent-spawn-audit.log`. **Zero exist** (control: `KILL`=47,
  total=693). *Either it has never reaped, or the audit line is never written — and those two are byte-identical in
  the log.* **A negative result that cannot show its observation is indistinguishable from a missing observation.**
- **AND `kill-orphans:131-139` MAY ANSWER THE exit-143 "UNDETERMINED" ABOVE.** It documents a 2026-06-15 incident
  where reading the wrong cmdline token made **every live stream watcher read as stale and get reaped on a peer's
  `register_agent`** — the exit-143 deaths this file calls *"source UNDETERMINED."* It says `--serial` fixed it.
  **Whether it still fires is UNEXERCISED**; do not record this as the cause without running it.
- **RATE: UNMEASURED. Do not claim "one per ended session"** — I wrote that and MSTR falsified it. The probe
  proves **`TaskStop`** orphans the child; it proves nothing about ordinary session end. Counter-evidence:
  `0.7.0_AE_CloudOps` died twice on 2026-07-10 and left **no** orphan child (`w=0`); `0.4.0_DS` base's session
  end left pid 31391 for 7h17m; `1.0.0_SA_CTO`'s predecessor left pid 2124. **Session end SOMETIMES orphans; the
  discriminator is unknown.** A fabric sweep at 02:20Z found exactly ONE orphan across 8 agents and a full night.
  This does not soften the fix — a parent-liveness check closes the class at any rate — but **a reaper justified
  by "they accumulate" is sized against a rate nobody has measured. Measure the rate before sizing the reaper.**

**TRAP when you scan for orphans:** MSYS **`ps -p 1` FAILS**, so a naive ppid-liveness test marks
every healthy detached eval-wrapper (`ppid=1` at birth) an ORPHAN. This produced **7 false positives**
in the first scan of this incident, including on a watcher armed 90 seconds earlier. **Positive-control
your sweep against a watcher you know is good.** The correct predicate is: a
`bash inbox-watch.sh <serial> stream` whose ppid resolves to a **live eval-wrapper process**.

**CAVEAT (2026-06-05, LD-0146 amend — Andrew-sovereign-settled).** The "never-off / exit-143 catalog
GONE" claim is too strong, but the practical reality is: **the Monitor is robust + lossless.** Andrew
ground-truth (verbatim): *"the monitor function has always been particularly robust, messages are
never dropped, they live through compactions… no adverse effect… with regard to the actual operations
of mcp communications."* So:
- The stream Monitor occasionally receives **exit-143 (SIGTERM)** at irregular intervals. **Source is
  UNDETERMINED and operational impact is ZERO** — 0 messages dropped, survives compaction, re-arms
  cleanly. Treat death as EXPECTED-and-handled: on a `<task-notification status=failed>` for your
  Monitor's task id, run Step 2→3 (confirm no orphan, pull inbox, re-arm). That's the whole protocol.
- **DO NOT escalate this as a fire/charter.** A FALSIFIED hypothesis chain this session
  (exit-143 → "0 pollers fabric-wide → kill-orphans stale-liveness reap") was disproven by
  ground-truth: **"0 pollers" was an MSYS `ps -ef|grep` artifact** — it cannot enumerate DETACHED
  native-Windows poller processes, which were in fact ALL alive with fresh liveness. So kill-orphans
  was NOT reaping on stale liveness. Do not re-chase the poller mechanism off a `ps|grep` count;
  enumerate detached Windows procs by liveness+PID, not `ps|grep`. Residual deaf-window (idle/
  compacting agent missing the death-notification) is bounded for looped agents anyway — every loop
  body folds a turn-top `check_inbox`/`get_agent_status` pull, so max-deafness ≤ one loop interval.
- **Proportionality lesson (banked):** verify OPERATIONAL impact + ground-truth the PREMISE before
  escalating an infra quirk. This one self-heals losslessly — it never warranted a charter.

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
   **A matching process is NOT proof of a live Monitor.** It proves a bash process
   exists — it says nothing about whether any Monitor task is reading its stdout.
   An **orphan from a dead session matches this grep exactly** (see ORPHAN HAZARD),
   and it is *eating your mail*. Use (3) only to find processes, never to conclude
   "alive": a match is alive **only if its ppid resolves to a live eval-wrapper**
   (and remember MSYS `ps -p 1` fails — every healthy wrapper is `ppid=1`).

**A FRESH SESSION THAT FINDS A MATCHING PROCESS HAS FOUND AN ORPHAN, NOT A WATCHER.**
You did not arm it; your session cannot be reading its stdout. Kill it (it is your own
serial — that is in scope), then arm. Arming on top of it makes two streams race the
same 5s `mv` and splits your inbox at random, silently, while every reachability probe
reports REACHABLE.

**EXERCISED FALSE-POSITIVE OF THE RULE ABOVE (2026-07-14, the dual-COO collision) — CHECK
LIVENESS BEFORE THE KILL.** The rule assumes ONE session per serial; a FLEET RELAUNCH with an
incumbent still live breaks that premise, and then the found watcher belongs to a **live peer**,
not a dead session. Live case: the fresh `2.0.0_SA_COO` session found a matching watcher pair at
startup and killed it per this doctrine — it was the still-running morning session's LIVE watcher;
that session re-armed, two streams raced the shared inbox 16:07–16:29Z, GA-3 identity warnings
fired in both directions, and the survivor had to be adjudicated by Andrew. **THE DISCRIMINATING
CHECK (REQUIRED, sequenced BEFORE any startup watcher kill):** run the XXX.md Step-1
identity-conflict probe FIRST — `get_agent_status`/liveness for your own serial. If it reads
**LIVE with a FRESH heartbeat at a DIFFERENT PID**, you may be looking at a live peer session's
watcher: **STOP — surface the identity conflict (Andrew/CTO) and resolve it BEFORE killing
anything.** Only when the serial reads STALE/absent — or the registration is demonstrably a
leftover (no heartbeat advance across two spaced probes) — is the found process an orphan and the
kill correct. Incident record: spawn-audit GA-3 entries 16:08:08Z + 16:27:11Z, predecessor
handoff 163144Z (its stand-down correctly reaped the bash child that `TaskStop` leaves behind),
CTO item-4 ACK 163221Z.

**SECOND EXERCISED FALSE-POSITIVE (2026-07-16, `0.0.0_AB_MSTR`) — AND THE CHECK ABOVE CANNOT CATCH
IT: A CONTEXT-CLEAR IS NOT A NEW SESSION, BUT IT FEELS LIKE ONE.** MSTR cleared context, ran this
rule, found a matching `inbox-watch.sh` process, and **reaped its own LIVE watcher** — then had to
re-arm (task `bi3810vyx`). Its own words: *"orphan rule false-positives on context-clear."*
**WHY THE DUAL-COO DISCRIMINATOR IS BLIND HERE:** that check keys on a **DIFFERENT PID** (= a live
peer). A context-clear is the **SAME process, SAME session, SAME PID** — so your serial reads LIVE
at *your own* PID, the different-PID test does not fire, and the rule's own words ("a fresh session
that finds a matching process has found an ORPHAN") point straight at your own healthy watcher.
**The premise that fails is "I do not remember arming it, therefore I did not arm it."** After a
context-clear you have no memory of arming a Monitor that is still, at that moment, streaming your
inbox. **Absence of your own memory is not evidence of absence of your own watcher.**
**THE DISCRIMINATOR THAT COVERS BOTH CASES — ask WHOSE PID, not "is anything live":**
```
liveness PID == MY PID   -> IT IS MINE, ALIVE. Context-clear (or a forgotten arm). DO NOT KILL.
                            Confirm with TaskOutput(<id>) -> running if you still have the id.
liveness PID != MY PID   -> a LIVE PEER holds the serial. STOP: identity conflict -> Andrew/CTO.
serial STALE / absent    -> genuine orphan (predecessor died). Kill YOUR OWN serial's, then arm.
```
**Both false-positives share one root: the rule reasons from "fresh session" — a state the agent
INFERS — instead of from PID identity, which it can MEASURE.** Infer-vs-measure is the whole bug.
*Cost so far: one adjudicated dual-COO collision (07-14) and one self-reaped live watcher (07-16).
A watcher killed here is not inert — the agent goes deaf while every reachability probe still reads
REACHABLE, because the orphan/absent watcher drained the inbox.*

Only arm a new Monitor if **none** of these confirm a live one (genuinely fresh
session / restart / a death notification you actually saw). When unsure, check
(2) — the task-id check is the only one that observes a *consumer*. Never re-arm off
an empty `TaskList`, and never conclude "reachable" off (3) alone.

## Invocation forms

| Form | Behavior |
|---|---|
| `/watcher` | Arm-at-load check, **once**. Register if STALE; arm the Monitor if absent; pull inbox; report. **No loop is armed** — the persistent Monitor is the standing mechanism. |
| `/watcher status` | Report-only: registration + Monitor presence + inbox. No changes. |
| `/watcher rearm` | Force a clean re-arm: TaskStop the existing Monitor, **then `ps` for its bash child and KILL IT**, then arm a fresh stream Monitor. **DO NOT SKIP THE CHILD KILL — `TaskStop` DOES NOT REAP IT.** Exercised 2026-07-10: `TaskStop` reaped the wrapper (pid 701462) and left the child (pid 701546) running with a dead parent. Arming on top of that survivor makes two streams race the same `mv`. Before this was found, **`/watcher rearm` manufactured an orphan and then raced it** — the repair procedure generated the fault it was repairing, and `watcher-status.sh` (Step 3.1) could not see the survivor. |
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
  `/cygdrive/c/` here. *(This line carried the hardcoded `/c/` form after
  `aef2840826` corrected Step 3 — the fix landed on the instruction an agent reads
  LAST and left the one it reads FIRST, so a Step-0 reader still got the wrong
  prefix. A correction is only as complete as its last surviving copy.)*

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
   - **RESOLVE THE DRIVE PREFIX FIRST — DO NOT HARDCODE EITHER FORM.** BOTH prefixes
     may be mounted at once (measured 2026-08-06, CRO: `/c` and `/cygdrive/c` resolve to
     the same device + inode — the prior "one or the other, never both" sentence here
     was FALSE on a live box), but they are NOT equally durable: `/c` is a non-`auto`
     user mount that has vanished at reboot (LD-0340 class, 2026-07-29: its death killed
     all 186 `~/bin` forwarders that baked `/c/` in, while A.3 read healthy);
     `/cygdrive/c` is the system-provided `auto,noumount` mount. The Monitor needs an
     **absolute** path (the guard hook blocks the relative form). Measure, then arm:
     ```bash
     test -d /cygdrive/c && echo /cygdrive/c/Users/AndrewBerman/Desktop/ajb_workspace \
                         || echo /c/Users/AndrewBerman/Desktop/ajb_workspace
     ```
   - command: `bash <resolved-prefix>/org/mcp/inbox-watch.sh {serial} stream`
   - **A wrong prefix does NOT fail like a wrong path — it fails as `exit 127` on a
     Monitor you have already been told is the standing mechanism.** The tool returns a
     task id and reports success; the death arrives separately as a
     `<task-notification status=failed>`. **An agent that does not read that
     notification has armed nothing and is deaf for the entire session — while
     `register_agent`, `check_inbox` and `get_agent_status` all still read healthy**,
     because none of them observes the Monitor. Same `/c/`-vs-`/cygdrive/c/` root as
     the corrupted-harness-exit-code class. *(Measured 2026-07-25: this doc's
     previously-hardcoded `/c/` form killed the arm for both `1.0.0_SA_CTO~Z` and
     `0.8.0_AE_CloudComp~E` on the same fleet respawn. Every live watcher on the box
     was already using `/cygdrive/c/` — **the doc was wrong, not the fabric.**)*
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
  (LD-0202 / LD-0346; canonical form + citations in `org/XXX.md` "Inbox path").
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
