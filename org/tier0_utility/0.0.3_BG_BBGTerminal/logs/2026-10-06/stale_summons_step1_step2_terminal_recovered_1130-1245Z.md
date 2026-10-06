# STALE summons: Step 1 found a real failure, Step 2 recovered it -- the cause was click-coordinate drift, not credentials

**archetype:** DIAGNOSE

**Window:** 2026-10-06 11:30Z - 12:45Z | **Seat:** 0.0.3_BG_BBGTerminal | **Trigger:** inbox
`20261006T113002Z_freshness_checker_stale.md` (Kind: STALE), entered at Step 1 per
`deliverables/STANDING_ORDER_0715_DAILY_BACKSTOP.md`.

## Current State

**RESOLVED end to end.** The portal serves `data_as_of=2026-10-05` (generated_at
2026-10-06T12:32:48Z), verified BY CONTENT with my own read of `json/latest/manifest.json`,
not from the producer's rc. That is `trading_days_behind=1` against frontier 2026-10-06 --
the healthy T-1 steady state. The STALE condition is cleared.

The Bloomberg Terminal is signed in and DAPI is serving (`bloomberg_health` ok=true,
service `//blp/refdata`, 1 listener on 8194).

## Step 1 -- READ AND DETERMINE (per leg, never collapsed)

**Trading calendar resolved FIRST from `lib/trading_calendar.py`, not from the summons**
(source: NYSE/hardcoded-fallback-2024-2027). 2026-10-06 is a Tuesday and a trading day;
`prev_trading_day` = 2026-10-05. Control run so a `1` would have been distinguishable from a
constant: served 10-05 -> 1, 10-02 -> 2, 10-01 -> 3, 09-30 -> 4. The summons' figure
independently CONFIRMED: served 2026-10-02 was 2 behind, and healthy is 1.

| Leg | Verdict | Evidence |
|---|---|---|
| **a. Scheduled task** | FAILED | `OPAL_BBGTML_daily_pull` LastRunTime 2026-10-06 07:00:01, **LastTaskResult 267014**. `NumberOfMissedRuns` 0, correctly ignored as a non-health instrument. |
| **b. Fallback (first)** | FAILED, and it is the honest finding | `wintrv.exe` IS running (pid 38444, launched 07:00:28 by the fallback). **26 blp-rooted processes enumerated, denominator printed** against 627 total processes. **0 listeners on 8194**, against a positive control of 41 listening ports. A running Terminal that is not signed in. |
| **c. WDAC/kernel** | **UNEXERCISED** -- DAPI was never restored, so the leg never ran. Not reported as a pass. |
| **d. Publish / served** | STALE confirmed by content | `json/latest/manifest.json`: data_pkl + model_pkl `data_as_of` 2026-10-02, generated_at 2026-10-03T11:07:01Z. |

**267014 is not in the exit contract.** It is `0x00041306` = SCHED_S_TASK_TERMINATED, a Task
Scheduler status, not one of the `.cmd`'s own codes (0/1/9/20/30/40/50). The 07:00 log ends in
`^C` at ~07:29 while a downstream leg was still retrying 8194, so the task was terminated
before the `.cmd` could return its own `exit /b 50`. A reader consulting only the
LastTaskResult table in the standing order gets no verdict for this value.

The 07:00 log itself carried the real verdict: `PRECONDITION: FAILED -- DAPI DOWN and not
self-healed. PULL NOT ATTEMPTED.` and `DAPI FALLBACK EXIT: 2`, reached from
`bbg_fallback.ps1:93` -- fill did not verify after 3 attempts, aborting **at ZERO Bloomberg
attempts**.

Step 1 therefore found an ACTUAL FAILURE, which is the only thing that opens Step 2.

## Step 2a -- FIRE-ONCE LEDGER PRECHECK (before any fill, no exceptions)

Discriminated on the TIMESTAMP and the 6-hour count, never on the `outcome` label.
`$USERPROFILE\.bbg_signin_attempts.json`: **30 entries total (denominator printed), 0 within
6 hours, most recent 2026-10-04T11:02:23Z = 48.77 h old.** VERDICT: CLEAR, one fill permitted.

## Step 2 -- RECOVERY, and the root cause

### R1 -- CLICK-COORDINATE DRIFT (the whole outage)

`bbg_signin.ps1` holds three ABSOLUTE SCREEN constants: `COORD_USER=(659,348)`,
`COORD_PASS=(659,426)`, `COORD_LOGIN=(590,482)`, clicked via `SetCursorPos`. The live
`BLOOMBERG: Login` dialog sits at L=275 T=64, 962x769. Measured from the captured bitmap:

| control | true window rect | true screen centre | constant | offset |
|---|---|---|---|---|
| username field | x 61-301, y 202-230 | (455, 279) | (659,348) | +204, +69 |
| password field | x 63-303, y 283-307 | (455, 360) | (659,426) | +204, +66 |
| **Login button** | x 60-162, y 339-361 | **(386, 414)** | (590,482) | +204, +68 |

All three constants land on RGB(0,0,0) -- bare dialog background. Probe control: the password
field interior sampled RGB(255,160,40), so the probe does detect controls where they are.

Consequence: **the unattended fallback can never log in.** It clicks dead space, records a
fire-once ledger attempt, waits 18s, finds no listener, and reports "still no listener" --
having never reached Bloomberg at all. The ledger burns down while Bloomberg counts nothing.

I recomputed the Login centre from THIS window's `GetWindowRect` (never a stale constant) and
clicked once at (386,414): **8194 listener count 1, login dialog gone, `bloomberg_health`
ok=true.** The credentials were never the problem.

### R2 -- VERIFY-GATE FALSE NEGATIVE

`bbg_verify.ps1` gates on `okDots AND okUser`, with `uLo=len-1, uHi=len` -> band 11..12 for a
12-char username. Its comment derives that from a reference fixture where ONE glyph pair
touches. The live 12-char `<username>` contains TWO doubled-letter pairs, so it renders **10
runs and fails every single time** -- 3/3 today, deterministic. The same gate's own OCR read
the username at **100% similarity** and the password dots at exactly 9. The code comment calls a 10 "a
legit fill that ever renders 10 fails SAFE ... fail-safe-rare"; for this credential it is not
rare, it is total. The gate's intent (never pass-wrong) is right; the band's derivation is
wrong for the credential actually in use.

### R3 -- CAPS LOCK WAS ON during the automated fills

The 07:04 fallback screenshot shows Bloomberg's own **"Caps Lock is on"** warning in the
dialog; machine state read `CapsLock: True`. The typer is
`[System.Windows.Forms.SendKeys]::SendWait`, which is Caps-Lock-sensitive for alphabetic
characters, so the 9-char password may have been typed case-inverted. It is unverifiable
through a masked field, and the dot-count check cannot see it (case does not change the
count). I cleared Caps Lock before my fill; the warning was ABSENT from my screenshot, which
is Bloomberg's own confirmation the state changed. **Nothing in the fill path checks or
clears Caps Lock.** Whether it contributed to earlier submitted-but-still-down days
(09-23, 09-27) is NOT established here.

### The recovery run

Re-ran `scheduled_daily_pull.cmd` itself rather than the individual runner+publisher, so the
recovery COMPLETES the failed scheduled run instead of opening a second path. cmd rc=0, 544s,
log `bbg_tplus1_20261006_082454.log`:

- `PRECONDITION: PASS -- DAPI UP, an entitled session answered a real refdata request` (first PASS today)
- target `20261005`, the exact missing date
- `RESULT: PASS -- both PKLs safe to send`; as-of-scoped tripwire PASS
- `portal currently serves 2026-10-02 -- 2026-10-05 is newer, safe to advance` (no backward publish)
- PULL 0 | PUBLISH 0 | ETF 0 | CONSTITUENTS 0 | PRICE 0 | RIVALFUNDS BBG **90 landed** (was 93 nothing-written at 07:00) | RIVALFUNDS ENRICHMENT 94 landed

### `.ST` CIX content check (required after a fresh sign-in -- CIX resolution is login-scoped)

Run against the PKL that was actually published, so it tests what will be served rather than a
fresh query, and spends no Bloomberg budget against the still-running legs.

- `.ST Index` **721 -> 722 rows, advance exactly 1** = trading days elapsed 10-02 -> 10-05
- inception **2023-12-29 @ 100.0** exactly as specified; last 2026-10-05 @ 111.1831
- POSITIVE CONTROL `SPX Index` 1445 -> 1446, +1
- NEGATIVE CONTROL `ZZZZ Index` 0 rows, absent -- so a zero above would have meant something
- all five primary model series (.ST .UST .INT .LT .ULT) advanced by exactly 1

**R4 -- CIX PARTIAL STALENESS, PRE-EXISTING, surfaced not chased.** Of 13 custom CIX series,
**7 last carry 2026-09-29** (.INT_BMK, .LT_BMK, .LT_ETF, .ST_BMK, .ST_ETF, .UST_BMK,
.UST_ETF) while the other 6 and the SPX control reached 2026-10-05. They were already at 718
rows in the 10-02 pull, so this PREDATES the outage and was not caused by the recovery. The
tripwire passes regardless. Routed to 0.0.0_AB_MSTR~Z, not investigated further.

## Corrections made in-session

My first `.ST` check printed `*** MISMATCH ***` on all five regression keys. **That verdict was
my own instrument's bug, not a data finding**: `trading_calendar.trading_days_between` returns a
LIST of dates, not a count, so the comparison was against a list; and `model['regression']` holds
5 fitted results, not a time series, so a row count was the wrong measure. Re-run against
`data['return_daily']` with a real count, it passes. Recorded because a wrong-object MISMATCH
that reads like a data defect is exactly the shape that gets escalated.

Separately, my first attempt to re-run the `.cmd` sent its output AND its rc to `/dev/null`;
it reported exit 0 having never run (cmd.exe argv mangling from Git Bash on this
path-with-a-space device). The emptiness carried the verdict and I had discarded it. Re-run
through PowerShell with output captured.

## Blockers

- **None on the Bloomberg pipeline.** Serving current.
- **Teams concierge remains OFFLINE** -- `opal-gateway-bbg` still requires Andrew's browser
  consent + MFA (carried from the 2026-09-29 log). I did NOT run the step-2a identity
  acceptance gate or arm the Teams Monitor this session, and did not initiate re-auth:
  that needs Andrew. Bloomberg duty is unaffected.
- **R1 and R2 are unfixed.** I cannot write `integrations/bloomberg/auth/` -- it is outside my
  fence and I hold no git lane. Until R1 is fixed, **every unattended sign-in will keep failing
  the same way**, and the daily pull depends on a human or this seat recovering it by hand.
  Owner needed.

## Next Steps

1. **R1 fix (owner needed, not mine):** derive the three click points from `GetWindowRect` plus
   the located field box at call time. `bbg_verify.ps1` ALREADY locates the username field
   window-relatively and reported `delta vs constants dx=0 dy=0` -- its constants are in window
   space and are correct. The drift is confined to `bbg_signin.ps1`'s screen-space constants,
   and the locator that is already in the tree can supply them.
2. **R2 fix:** derive the glyph-run band from the credential's own doubled-letter count, or
   drop `okUser` to an advisory beside the OCR similarity, which scored 100% while the band
   refused.
3. **R3:** clear Caps Lock in the fill path before typing, and record its state in the log.
4. **Layer-2 ran-at-all duty:** `Microsoft-Windows-TaskScheduler/Operational` returned **no
   events** over 5 days -- the channel appears disabled, so "did the task fire" is
   **INSTRUMENT-ABSENT on this box**, not answered. On disk, 10-02/10-03/10-04/10-06 all have
   07:00-stamped logs and **2026-10-05 has none** (its only log is 08:32:46). The `.cmd` writes
   its log unconditionally, so that reads as the Monday 07:00 fire not happening -- stated as a
   finding, with its instrument gap named.

## Addendum -- broker registration expired TWICE mid-session (observation, no decision attached)

`heartbeat()` returned **"is not registered. Call register_agent first"** twice: at ~12:45Z
(~56 min after my previous heartbeat) and again at ~13:02Z (~17 min after re-registering).
Same PID 25392 both times -- **my process never restarted; the broker row went away.**

Measured, not assumed: `org/mcp/agent-spawn-audit.log` carries **0 deregistration events dated
2026-10-06**, so no peer deregistered me and this is not a `deregister_all_stale` sweep. Note
also that `send_message` calls at 12:51Z and 12:55Z did NOT keep the row alive -- only
`heartbeat`/`register_agent` appear to touch it.

> **CORRECTED, same session, after reading the source.** I first wrote this up as unexplained.
> It is documented behaviour: `org/mcp/server.py:93` `DEAD_THRESHOLD = 600`, and `_clean_stale`
> (`:204-211`) **DELETES** any entry quiet for more than 10 minutes; `heartbeat` then takes the
> `:1234` branch and returns "is not registered" rather than resurrecting the row. So the cause
> is an ordinary 10-minute prune, not an anomaly, and all three drops followed a >10 min
> quiet gap once turn wall-clock is counted. **The part worth keeping is not the mechanism but
> its consequence:** `org/XXX.md` states the 2-minute STALE degrade and does NOT state that the
> entry is DELETED at 10 minutes. A reader who knows only the documented half expects a seat to
> read `stale` and finds it ABSENT instead -- and `heartbeat`, the call named to keep a seat
> alive, is exactly the call that cannot revive it.

**Why it matters, and why it is not just noise:** while unregistered, mail still REACHES me --
`send_message` writes the filesystem inbox and my Monitor reads that carrier. What breaks is the
other direction: a peer reading `get_live_agents` sees me ABSENT and may conclude this seat is
down and route around it, or park an item on a condition that cannot fire. That is the
"an UNREGISTERED session is not a dead one" class, observed from the inside this time.

**Mitigation inside my own lane:** heartbeat at every turn boundary rather than relying on
session longevity. **Not** a cron -- this seat arms zero (org/XXX.md Step 1b-F), and building a
liveness monitor would be the standing moratorium's exact anti-pattern. Recorded here rather
than sent to an inbox per CLAUDE.md Rule 31: it is an observation with no decision attached.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-find` | locate SendKeys typing path in `integrations/bloomberg/auth/` | 6 hits / 6 files, denominator printed -- found `bbg_signin.ps1:148-155` |
| `comp-find` | locate the glyph-run verify band | 13 hits / 6 files -- found `bbg_verify.ps1`, NOT `bbg_signin.ps1` |
| `comp-find` | locate the `.ST` CIX check | 82 hits / 181 files, 4 pages -- found my own `deliverables/bloomberg_entitlement_probe.py` |
| `comp-read --enumerate` | search `bbg_signin.ps1` for the verify gate | 0 of 188 lines -- a true ABSENT, which correctly redirected me to `bbg_verify.ps1` |
| `portal_lookup.py get` | leg d, served manifest by content, twice (before and after) | 2026-10-02 -> 2026-10-05, each with its own generated_at |
| `lib/trading_calendar.py` | resolve the frontier independently of the summons | confirmed, with a 4-point control series |

**What failed / gaps:** `check-inbox` is not on PATH as a bare command on this box (the
`org/XXX.md` Step B form `check-inbox {serial}` returns `command not found`); I used
`get_agent_status` + `get_delivery_state` + a direct `read/` listing instead. The comp-rail
correctly refused two `comp-find | grep` pipes where the receiver would have erased the
denominator; I re-ran with native flags both times.
