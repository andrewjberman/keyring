# 0.0.3_BG_BBGTerminal -- startup after an unannounced reboot + daily guardrail
**Window:** 2026-09-16T00:32Z - 00:50Z (2026-09-15 20:32-20:50 ET)
**Seat:** 0.0.3_BG_BBGTerminal (base, no lane) -- Tier-0 Utility, site Z / Bloomberg Terminal box

---

## 0. HEADLINE

Startup clean on every launch gate EXCEPT Bloomberg. **The box rebooted at 2026-09-15 20:30:02 ET
(16 minutes before this session registered) and the Bloomberg Terminal did NOT come back with it.**
Today's 07:00 ET pull is unaffected -- it ran and published hours before the reboot -- but
**tomorrow's 2026-09-16 07:00 ET pull will fail on the DAPI precondition unless someone signs the
Terminal in.** SURFACED, NOT TOUCHED (`refs/RELAUNCH.md:114`; and Andrew's own verbatim in
`deliverables/STANDING_ORDER_0715_DAILY_BACKSTOP.md`: nobody signs in ahead of a failure).

## 1. LAUNCH GATES (prompt.md "On launch", steps 1-5)

| Step | Result |
|---|---|
| 1. `register_agent` | OK -- LIVE, PID 5584, broker connected (port 7800). Was NOT REGISTERED at load. |
| 2. `/watcher` | Inbox Monitor **armed: task `bu6fulcr7`**, banner `parent-tied: pid 580`, `TaskOutput -> running`, `ps` shows one watcher (pids 580/584) for this serial. No prior watcher existed (`ps` NO_WATCHER_PROC) -- expected, the reboot took the previous session's. |
| **2a. IDENTITY ACCEPTANCE GATE** | **PASS** -- `whoami` on `opal-gateway-bbg` = **Opal Bloomberg / opalbloomberg@opalinvest.com**. Not Andrew. Gate cleared BEFORE any Teams read. |
| 3. Teams Monitor | **armed: task `bd1wfayxz`**, banner `interval=10s cursor=2026-09-15T18:25:20.883Z (incoming-only) pin(server=opal-gateway-bbg, identity=opalbloomberg)`; `token selected: identity=opalbloomberg@opalinvest.com`. |
| **4. `bloomberg_health`** | **`ok: false`** -- `could not start blpapi session to 127.0.0.1:8194`. See section 3. |
| 5. Latest local log + orient | Read `logs/2026-09-14/startup_and_daily_guardrail_1528-1610Z.md` and `deliverables/WINDDOWN_PARK_20260915T235xZ.md`. |
| Crons | **ZERO** (`CronList` -> "No scheduled jobs"). Correct end state; the 07:15 clock is retired. |
| Inbox | **EMPTY** on both probes -- `check_inbox` "Inbox empty", `get_agent_status` no messages. Top-level of `org/mcp/inbox/0.0.3_BG_BBGTerminal/` holds only `read/`. |

### Cursor check (TEAMS_DUTY "Reading the arm banner")
Armed cursor `2026-09-15T18:25:20.883Z` is **at or after** the newest served entry in thread memory
(the winddown park records the 18:10-18:25Z Andrew emits as SERVED, no reply owed, his own
*"Don't respond to this."* at 18:10:14Z). **No backward move, so no SUSPECT-REPLAY framing.**
Nothing has emitted from this arm as of this log.

### Monitor lifetime
Both Monitors clamp to **30 min**, not the 60 the skills text suggests -- `timeout_ms` capped at
1800000. Re-arm on every expiry notice or this seat goes deaf while every other probe reads healthy.

## 2. DAILY GUARDRAIL -- PASS (both OS tasks, and the served artifact by content)

Expected vintage: 2026-09-15 is a **Tuesday**, the pipeline is **T-1 by fixed rule**, so the healthy
answer is **2026-09-14 (Monday)**.

| Leg | Instrument | Measured |
|---|---|---|
| a. Scheduled task | `Get-ScheduledTaskInfo OPAL_BBGTML_daily_pull` | LastRunTime **2026-09-15 07:00:01**, **LastTaskResult 0**, Next 2026-09-16 07:00 |
| a2. Second OS task (1a Layer 2) | `Get-ScheduledTaskInfo OPAL_BBGTML_freshness_check` | LastRunTime **2026-09-15 07:30:01**, **LastTaskResult 0** (= PASS), Next 2026-09-16 07:30 |
| Produced files | OneDrive `.../202511 Model Portfolio Exposure/output` | `data 20260914 v1.pkl` 07:02, `model 20260914 v1.pkl` 07:03 (2026-09-15) |
| d. Publish / served BY CONTENT | `tools/portal_lookup.py get benchmarks model_portfolio_benchmarks` | **`data_as_of = 2026-09-14`**, object last-modified 11:06:18Z |
| d2. Pipeline manifest | `tools/portal_lookup.py get pipeline-status manifest` | `pipeline_started_at 11:03:54Z`, `generated_at 11:07:40Z`, `sources.data_pkl.data_as_of` and `sources.model_pkl.data_as_of` both **2026-09-14** |

`LastTaskResult 0` was NOT accepted as the verdict -- the served artifact was read by CONTENT and the
two PKL sources inside the manifest agree with it. `NumberOfMissedRuns` (0 on both) is recorded but is
**not** the health instrument.

Also seen, not owned by this seat: `OPAL_vendor_watch` last 20:09 ET rc 0, hourly; `OPAL_BLOOMBERG-FreezeTripwire`
last 20:46:55 ET rc 0, ~2-minutely. Both alive across the reboot.

## 3. THE FINDING -- BLOOMBERG TERMINAL DOWN AFTER A 20:30 ET REBOOT

**Machine last boot: 2026-09-15 20:30:02 ET** (`Win32_OperatingSystem.LastBootUpTime`). This seat's
previous session parked ~19:5xZ... i.e. ~23:5xZ UTC, on Andrew's *"huntress is blowing up again we need
managed winddown"*; the reboot followed. This session is the post-reboot relaunch.

Measured on TWO independent instruments, not one:

1. **MCP `bloomberg_health`** -> `ok: false`, `could not start blpapi session to 127.0.0.1:8194`.
2. **The `cma` interpreter's OWN blpapi client** (`C:\Anaconda\envs\cma\python.exe`, the env the pull
   actually runs under -- green MCP is not a runnable pull, and here neither is green):
   `blpapi 3.26.4.2` imports fine, `session.start() -> False`,
   `ErrorInfo code=8 category=IO_ERROR errorMessage="connect event failed"` after 3 reconnect attempts.
   **So the interpreter is INTACT; the defect is the DAPI/Terminal, not the env.**

3. **Listener, 3 probes ~1.5 s apart: NO LISTENER on 8194 all three times.** A sustained absence, not a flicker.
4. **`C:\blp\` process census WITH THE DENOMINATOR: 2 of 355 processes.**
   `bbcomm.exe` pid 26508 and `blpcrashmon.exe` pid 14448 -- **both started 20:37:39 ET**, i.e. at my
   own health probe, not at boot. **`wintrv.exe` (the Terminal itself) is ABSENT.**
   Per the standing order: **a running `bbcomm` is NOT a running Terminal**, and that is exactly the
   shape here -- bbcomm up, nothing listening, no Terminal.

**Consequence, stated plainly:** the 2026-09-16 07:00 ET `OPAL_BBGTML_daily_pull` runs into a DAPI
precondition that is currently false. On the `LastTaskResult` exit contract that is an **rc 50 --
"DAPI precondition FAILED, the pull was NOT attempted."** The 07:30 freshness check would then summon
this seat, and the summons enters at Step 1.

**WHY I DID NOT SIGN THE TERMINAL IN.** Two independent reasons, both on the record:
- `refs/RELAUNCH.md:114` -- `bloomberg_health` not ok / Terminal down or logged out ->
  **"Surface (Andrew brings the Terminal back); do not touch it."**
- `deliverables/STANDING_ORDER_0715_DAILY_BACKSTOP.md`, Andrew VERBATIM under the heading
  *"why nobody signs in ahead of a failure"*: *"the whole point is that the device needs to be able to
  figure this out and get it done on its own accord."* The credentialed Step-2 recovery -- with a
  Bloomberg lockout on the other side of it -- is reachable **ONLY from a Step-1 finding of actual
  failure**, and there has been none: today's run succeeded end to end.

So this is a SURFACE, and the recovery path is armed and unchanged if tomorrow's run does fail.

## 4. STARTUP STEPS BLOCKED BY THIS SEAT'S OWN FENCE (expected, not a defect)

The launcher prompt said "then org/XXX.md startup protocol", but `prompt.md` is explicit:
**"On launch (no XXX.md -- you are not a fabric work seat)."** I ran the XXX.md steps that are reads,
and `bg-concierge-gate.sh` refused the three that are writes outside this seat's allowlist:

| XXX.md step | Result |
|---|---|
| A.1 session-serial file `org/mcp/sessions/<id>.serial` | **BLOCKED G2** (shell redirect) then **G1** (Write tool). Off-allowlist. |
| D. owned-paths pre-commit hook | **NOT INSTALLED** (`.git/hooks/pre-commit` absent). Install is a repo write; this seat does no git work and has no OWNPATHS lane by design. |
| E. `.comp-graph/.agent_context` | **BLOCKED G1.** Off-allowlist. |
| A.3 PATH / comp-rail | **RAN, PASS** -- `104 of 104` comp-tools resolve bare; forwarder EXERCISED (not merely resolved). |

**A BLOCKED from that gate is the system working.** Not retried, not routed around. Consequence worth
naming once: with no session-serial file, this seat's halt gate falls back to the shared
`.comp-graph/.agent_context`, so a `[STOP]` addressed to this serial is invisible to its own gate
(LD-0290). That is structural for this seat, not new tonight, and is Andrew's to change if he wants it
changed.

## 5. STATE AT LOG TIME

| | |
|---|---|
| Monitors | 2 -- inbox `bu6fulcr7`, Teams `bd1wfayxz`. Both `running`. |
| Crons | 0 |
| Worker subagents / browser sessions / background terminals | 0 / 0 / 0 |
| Broker | LIVE, PID 5584, heartbeat sent |
| Teams backlog | none owed; cursor 18:25:20.883Z, no emits this session |
| Fabric inbox | empty, both probes |
| Open item at Andrew | **Bloomberg Terminal sign-in before 2026-09-16 07:00 ET** |

## 6. SECOND FINDING -- MY BROKER REGISTRATION SILENTLY DROPPED WITHIN ~10 MINUTES

Registered 00:33Z (PID 5584, "Registered ... as live"), `heartbeat` 00:37Z returned **OK**. At 00:49Z
`set_summary` refused with **"0.0.3_BG_BBGTerminal is not registered. Call register_agent first"** and
`get_agent_status` read **NOT REGISTERED**. Nothing in this session deregistered anything.

**Inverse-first check ran BEFORE re-registering** (XXX.md Step 1): read `org/mcp/liveness.json` directly
-- **4 entries, and my serial is not one of them**: `0.0.0_AB_MSTR~Z` pid 12360, `1.0.0_SA_CTO~Z` pid 8556,
`3.0.0_SA_CVO~Z` pid 23384, `2.0.0_SA_COO~Z` pid 6604, all last-seen 00:49:1x-00:49:3xZ. **So this is NOT
an identity conflict and I am NOT the phantom** -- no peer holds my serial; my entry is simply GONE, and
the file mtime (20:49 ET) is a peer's write. Shape matches the known last-writer-wins / exhausted-
`os.replace`-retry class on `liveness.json` with several seats heartbeating into one file seconds apart
-- four ~Z lanes all came back from the same 20:30 ET reboot and are heartbeating together.

Re-registered 00:5xZ -> **LIVE, PID 5584, last seen 3 s**. Verified by re-read, not by the call's own
return.

**Why it matters more than it looks:** a dropped registration is silent in the direction that hurts --
the Monitors stayed armed and `TaskOutput` read `running` the whole time, so **every reachability probe
this seat owns read healthy while the broker could not see it.** Surfaced, not chased; the fix is not
this seat's (no git lane), and one instance is not a rate.

**Push state: UNREAD BY THIS SEAT** -- no git lane exists for this serial and none should;
`0.0.0_AB_MSTR` (either seat) is the named integrator and sweeps `logs/`, `threads/`, `deliverables/`.
