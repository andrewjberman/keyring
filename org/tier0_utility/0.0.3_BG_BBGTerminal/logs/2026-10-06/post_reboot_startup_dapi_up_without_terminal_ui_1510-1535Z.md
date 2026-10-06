# Post-reboot startup: DAPI is serving with NO Terminal UI running, and the schedules survived

**archetype:** VALIDATE

**Window:** 2026-10-06 15:13Z - 15:35Z | **Seat:** 0.0.3_BG_BBGTerminal | **Trigger:** session
launch after the site-Z reboot (`/watcher` then startup protocol).

## Current State

**Bloomberg duty is DISCHARGED for 2026-10-06 and the pipeline is healthy post-reboot.** The
portal serves `data_as_of=2026-10-05`, `generated_at=2026-10-06T12:32:48.874590+00:00`, read BY
CONTENT from `json/latest/manifest.json` via `portal_lookup.py get pipeline-status manifest.json`.
That publish happened BEFORE the reboot (prior session's recovery run) and is in S3, so the reboot
could not and did not disturb it.

Teams concierge remains OFFLINE, unchanged and still Andrew's call.

## The reboot gate was MOOT -- measured, not assumed

Inbox carried 2 messages, both acked (30111, 30129), both asking for a pre-reboot `/handoff`.

- `LastBootUpTime` = **2026-10-06T15:10:23Z** (11:10:23 EDT; offset read from `date %z` = -0400).
- msg 30111 sent 13:51Z, msg 30129 sent 14:02Z -- **both BEFORE that boot.**

So the device rebooted without my handoff and there is no pre-reboot state left to save. Replied to
`0.0.0_AB_MSTR~Z` to release the gate rather than writing a handoff for a reboot that had already
happened. This session started clean.

## The finding: DAPI is UP and ENTITLED with `wintrv.exe` ABSENT

This is new and it bears on R1 (the click-coordinate drift that makes unattended sign-in impossible).

| Instrument | Reading |
|---|---|
| listeners on 8194 | **1** (positive control: 38 listening ports total, so the probe discriminates) |
| blp-rooted processes | **2 of 330** total: `bbcomm` 14404, `blpcrashmon` 7852 -- both started 11:21:07 local = **15:21Z, AFTER the boot** |
| `wintrv.exe` (Terminal UI) | **NOT RUNNING** |
| `bloomberg_health` | `ok:true`, `//blp/refdata` |
| real refdata (MCP) | `SPX Index PX_LAST = 7836.97` |
| CIX resolution | `.ST Index` -> `NAME="OPAL SHORT TERM"`, `PX_LAST=111.1830767852731` |

**Why the data read is sound and not a cache:** the same call asked for `LAST_UPDATE_DATE` and got a
structured `BAD_FLD / INVALID_FIELD` field error back. A cache does not validate field mnemonics;
only a live service does. Per READ_HERE section 2, a listener is necessary-not-sufficient, so the
verdict rests on the data read, not the port.

**CIX resolution is login-scoped and it SURVIVED:** `.ST Index` resolved to its custom Opal name at
111.1830767852731, which is exactly the 2026-10-05 close the prior session published (111.1831). A
non-entitled session does not resolve a custom CIX name at all.

> Caveat on my negative control: `ZZZZ Index` returned `NAME="TEST - ARCA"` -- it is a real Bloomberg
> test ticker, **not a clean absent-security control for CIX**. It carried no `PX_LAST`, which is the
> only part of it that discriminated. Stated rather than smoothed; the load-bearing evidence is the
> custom-name resolution, not the ZZZZ row.

**Consequence, stated without over-claiming:** `bbcomm` auto-started at boot holding an entitled
session, so the 07:00 precondition (`DAPI UP, an entitled session answered a real refdata request`)
passes RIGHT NOW with no sign-in and no UI. If that session persists overnight, tomorrow's 07:00 run
should clear the precondition that failed today. **If it drops, R1 still makes the unattended
fallback unable to log in.** Whether a bbcomm-held session survives to 07:00 is NOT established here.

## Step 4 of my launch list: `cma` interpreter CONNECTS (green MCP is not a runnable pull)

The MCP server runs a different Python than the pull, so the readings above do not prove the pull can
run. Tested the pull's own interpreter directly, `C:\Anaconda\envs\cma\python.exe`:

```
interpreter: C:\Anaconda\envs\cma\python.exe
blpapi: OK 3.26.4.2
tia: OK
SESSION: STARTED
SERVICE: //blp/refdata OPEN
DATA: ReferenceDataResponse ... security = "SPX Index" ...
exit 0
```

Run through PowerShell, not Git Bash: the prior session recorded cmd.exe argv mangling from Git Bash
on this path-with-a-space device. **The pull is runnable.**

## Schedules survived the reboot

| Task | State | LastRun / LastResult | NextRun |
|---|---|---|---|
| `OPAL_BBGTML_daily_pull` | **Ready** | 2026-10-06 07:00:01 / **267014** | **2026-10-07 07:00** |
| `OPAL_BBGTML_freshness_check` | Ready | 2026-10-06 07:30:01 / 2 | 2026-10-07 07:30 |
| `OPAL_autolaunch_agents` | Ready | 2026-10-06 11:11:12 / 0 | (on boot) |

Positive control: **208** scheduled tasks visible, so a Ready/Disabled read discriminates. 267014 is
today's known `SCHED_S_TASK_TERMINATED`, already recovered by hand in the prior session; the task
itself is armed and not disabled.

## Correction: my trading-day control ladder read 2,3,4,5 -- not the 1,2,3,4 in the prior log

`lib.trading_calendar.trading_days_between` returns a **LIST inclusive of BOTH endpoints**. Pinned it:
`trading_days_between(10-06, 10-06)` -> `[2026-10-06]`, `len == 1`. So `len()` of that list is
off-by-one against the convention the prior log quoted, and healthy T-1 reads **2** on that
instrument, not 1.

**The sound oracle is the frontier equality, not a derived count:** `is_trading_day(2026-10-06)=True`,
`prev_trading_day(2026-10-06)=2026-10-05`, and served `data_as_of=2026-10-05`. Served == previous
trading day == healthy T-1. I quote that equality and no count.

This matters because the same wrong-shape-against-a-real-parser mistake (a list where a count was
meant) is the one the prior session already corrected once in its `.ST` check. It returns a
real-looking number both times.

## Carried blockers -- none of them mine to fix

- **Teams concierge OFFLINE.** `opal-gateway-bbg` exposes only `authenticate` /
  `complete_authentication`, i.e. unauthenticated. **Step 2a's identity acceptance gate therefore
  cannot PASS, so I did not poll, did not reply, and armed no Teams Monitor.** I did NOT call
  `opalgateway.whoami` -- that is Andrew's proxy identity and calling it is the exact failure the
  gate exists to prevent. Re-auth needs Andrew's browser consent + MFA; I did not initiate it.
- **R1 / R2 / R3 unfixed, owner still needed.** `integrations/bloomberg/auth/` is outside my fence and
  I hold no git lane. Carried verbatim from the prior log; nothing changed today except that bbcomm
  is currently masking R1's consequence.
- **R4 CIX partial staleness** (7 of 13 custom CIX series last at 2026-09-29). Already routed to
  `0.0.0_AB_MSTR~Z`; **Yang Liu owns the CIX re-save + re-pull** per msgs 30079/30111. Not re-measured
  this session -- `historical_data` is denied by my fence, and the re-measure would not change what I
  do.

## Next Steps

1. Nothing to pull today; next scheduled fire 2026-10-07 07:00 ET. Verify it cleared the precondition.
2. If Andrew wants Teams back, he completes the `opal-gateway-bbg` OAuth; I surface the URL on his word.
3. R1 still needs an owner who can write `integrations/bloomberg/auth/`.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-find 'cma' --band DEF integrations/bloomberg` | locate the cma interpreter definition | **0 of 91 scanned, band=DEF** -- a measured zero; SURFACED=53 redirected me correctly |
| `comp-find 'cma' --limit 12 .../pipeline` | find the interpreter path | 50 hits / 18 files, denominator printed -- `scheduled_daily_pull.cmd:38 set "PY=C:\Anaconda\envs\cma\python.exe"` |
| `portal_lookup.py channels` | enumerate servable channels | 13 servable; corrected my own bad `get` invocation (channel+key, not key alone) |
| `portal_lookup.py get pipeline-status manifest.json` | leg d, served state by content | `data_as_of=2026-10-05`, vintage quoted |
| `lib/trading_calendar.py` | resolve the frontier independently | frontier equality confirmed; endpoint semantics pinned (see Correction) |

**What failed / gaps:** the comp-rail refused `comp-find | head` and `comp-find | tail` twice -- both
correctly, the receiver would have erased the denominator; re-ran with `--limit`/`--band`. **A rail
denial aborts the whole Bash call**, so the second refusal silently no-op'd the `ls` segment I had
chained after it -- re-ran it separately. `check-inbox` is still not on PATH as a bare command on this
box (carried gap from the prior log); used `check_inbox` + `get_delivery_state` + the `read/` listing.
