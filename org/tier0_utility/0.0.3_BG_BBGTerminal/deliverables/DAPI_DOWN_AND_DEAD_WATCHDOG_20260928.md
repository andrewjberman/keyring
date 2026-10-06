# DAPI DOWN + THE WATCHDOG THAT WOULD REPORT IT IS ALSO DEAD -- 2026-09-28

**Author:** 0.0.3_BG_BBGTerminal, session start 2026-09-28 ~18:5xZ.
**Class:** two INDEPENDENT defects on this box, measured, one gated on Andrew.
**Status:** **DEFECT 1 RESOLVED 2026-09-29 07:0xZ BY THE SCHEDULED FALLBACK ITSELF -- see the
RESOLUTION block immediately below; everything about Defect 1 further down is the state as it stood
on 09-28 and is retained as the record of that day, not as current state.**
**DEFECT 2 ALSO RESOLVED -- and it was resolved at 19:42Z on 2026-09-28, roughly 45 MINUTES AFTER
this seat measured it, by `0.0.0_AB_MSTR~Z` removing Python314 from the machine PATH
(commit `be2d74b007`). This seat then went on asserting "the watchdog is dead" for the rest of the
night off a measurement that had already expired. See the CORRECTION block below.**

---

## RESOLUTION -- DEFECT 1 CLOSED 2026-09-29, NO DATA LOST, NO ANDREW ACT NEEDED

The 07:00 ET run on 2026-09-29 signed itself in and completed end to end. The deadline named below
was MET, by the mechanism that exists for it, with no agent and no human in the path.

| Leg | rc | Evidence |
|---|---|---|
| sign-in fallback | 0 | fill attempt **1/3**, `focus VERIFIED`, verify PASS (9 dots), ONE submit, `8194 listener count after submit: 1` |
| precondition | 0 | `PASS -- DAPI UP, an entitled session answered a real refdata request` |
| models pull (target 20260928) | **0** | both notebooks OK (158s, 98s); full tripwire OK at as-of 2026-09-28 |
| publish | **0** | `served data_as_of 2026-09-28`, `served 1D matches the PKL for all five models`, `PUBLISHED 2026-09-28 -- verified by content` |
| ETF L1 | **0** | -- |
| **constituents** | **0** | **the leg with NO BACKFILL. The at-risk day was captured.** |
| price axis | **0** | generation committed |

INDEPENDENTLY VERIFIED, not taken from the publisher's own log: `portal_lookup.py get pipeline-status
manifest.json` reads `data_pkl.data_as_of` and `model_pkl.data_as_of` both **2026-09-28**, manifest
`generated_at` 2026-09-29T11:11:26Z. Tuesday 09-29 frontier minus 09-28 = 1 trading day behind =
healthy T-1.

**THE HOLD WAS STILL CORRECT, AND THE DISTINCTION IS THE POINT.** The runbook gate binds an
AGENT-INITIATED sign-in. The scheduled fallback is a DIFFERENT ACTOR with its own standing
authorization (Andrew RULED YES 2026-08-19, record @f45e5db124; LD-0413), and it is designed to fire
with no agent alive. Holding did not delay the fix by one second -- the fallback was always going to
fire at 07:00 regardless of what this seat did, and an agent-initiated attempt overnight would have
SPENT FROM THE SAME 2-ATTEMPT BUDGET the fallback then needed. Reading this as "the hold was
unnecessary caution" inverts it.

**WHY IT WORKED TODAY AND NOT ON 09-28 -- HYPOTHESIS, NOT ESTABLISHED.** On 09-28 the script accepted
a login window after 3s (`hwnd=44175040`) and `fg=0` on all three attempts; on 09-29 it waited 12s,
found `hwnd=590712`, and focus verified first try. The plausible reading is that the 09-28 handle was
a not-yet-input-ready or orphaned window. NOT PROVEN -- the falsifier would be a run that finds a
window at 3s and succeeds, or a deliberate early-accept that reproduces `fg=0`. Do not write this up
as the cause.

### NEW WARN FROM THE SUCCESSFUL RUN -- LATENT, WORTH AN OWNER

```
[fallback]   locator: MISS (no-field-shaped-band-of-5) -- FALLING BACK to measured constants;
             a layout/DPI change may be live
```

The dynamic field locator FAILED and the sign-in succeeded only on hardcoded coordinates
(`Login Name (659,348) / Password (659,426) / Login (590,482)`). It worked, so nothing failed loudly
-- which is exactly why it is worth recording. The runbook already warns that `{TAB}` between fields
typed a password into the UNMASKED Login Name field once and burned an attempt; coordinate constants
are the thing standing between that outcome and a moved dialog. A layout or DPI change would not
announce itself, and the verify step (dot-count + OCR) is the only thing that would catch it -- it
did fire and did pass here. Same class as R-65: a literal reading a value that can move.

---

## STATE OF THE SERVED DATA: HEALTHY. ZERO DATA LOSS TO DATE.

Resolved against the trading calendar BEFORE calling anything stale (CLAUDE.md NEVER#1).

| Fact | Value | How measured |
|---|---|---|
| Served `data_as_of` | **2026-09-25** (Friday) | publisher verified BY CONTENT, 09-26 log line 92 |
| Today | Monday 2026-09-28 | `date` |
| Expected frontier (Monday IS a trading day) | 2026-09-28 | checker's own basis |
| Trading days behind | **1** | Friday -> Monday |
| Verdict | **HEALTHY T-1** (`<=1` passes) | the checker's own rule |

**Friday IS Monday's answer.** The 09-26 (Saturday) run pulled and published as-of 2026-09-25 and
landed ALL FOUR legs clean: models rc=0, publish rc=0 (served-content verified), ETF rc=0,
constituents rc=0, price rc=0 (two generations COMPLETE). Today's T-1 is that same 2026-09-25, so
today's failed run would have been a duplicate publish, not a lost vintage.

**So the three failed runs (09-23, 09-27, 09-28) have cost NOTHING yet.** Stating that plainly
because the raw exit codes read like three days of loss and they are not.

### THE DEADLINE IS 07:00 ET TUESDAY 2026-09-29, AND IT IS A HARD ONE
> **MET 2026-09-29 -- see the RESOLUTION block at the top. The constituents day was captured, rc=0.
> The reasoning below stands as written; only its outcome is settled.**

Tuesday's T-1 is **Monday 2026-09-28 -- uncaptured**. If DAPI is still down at 07:00 ET Tuesday:
- the models leg misses a real vintage (recoverable later by re-pull);
- **the CONSTITUENTS leg is CURRENT-DAY-ONLY at the source with no backfill** -- that day is gone
  permanently. `scheduled_daily_pull.cmd` says so in its own `:cons_leg` comment, and rc=50
  deliberately does NOT reach that leg.

That asymmetry is why this is worth Andrew's attention today rather than tomorrow.

---

## DEFECT 1 -- DAPI DOWN. REMEDIES 1-4 ELIMINATED. SIGN-IN IS THE CANDIDATE REMEDY.

`OPAL_BBGTML_daily_pull` 07:00 ET today: **rc=50** = DAPI-liveness precondition FAILED, pull NOT
attempted. The auto sign-in fallback tried `fill` 3 times and aborted each time at
**ZERO Bloomberg attempts spent**:

```
ABORT: focus did not take (fg=0 != 44175040). Refusing to type a password
into an unverified window. NO attempt spent.
```

`fg=0` = no foreground window. The login window EXISTED (hwnd found each time); the guard correctly
refused to type a password into a window it could not confirm. **That is the guard working, not a
fault in it.**

### The four runbook remedies, run this session, in order

| # | Remedy | Result | Verdict |
|---|---|---|---|
| 1 | Re-probe 8194, 4 probes ~2s apart | listeners = **0, 0, 0, 0** | sustained absence = a FINDING, not an unlucky read |
| 2 | Restart `bbcomm` (stop pid 10964, relaunch) | new pid **13604**, still 0 sockets, still no listener | **ELIMINATED** |
| 3 | Network to Bloomberg + UNRELATED CONTROL | `69.187.48.83:8194` = **True**; control `8.8.8.8:53` = **True** | **ELIMINATED** -- path provably open |
| 4 | `bbcomm`'s own outbound sockets | **0 sockets** (2026-08-12 was loopback-only; this is worse) | up but not connecting |

`bloomberg_health` re-read after the restart: still `ok:false`. Per the runbook, an `ok:false` is
REAL evidence the transport is down -- act on it.

### Preconditions for the GUI sign-in, measured NOW

| # | Check | Reading |
|---|---|---|
| P1 | interactive console session | **PASS** -- `console  Opal Bloomberg  1  Active` |
| P1a | session locked? | **NOT LOCKED** -- `LogonUI` process count = 0 |
| P3 | `wintrv` already running | **absent** (0 processes) -- and per P0 that is NOT by itself evidence a sign-in is needed |
| -- | pull's own interpreter | present: `C:/Anaconda/envs/cma/python.exe` |
| -- | attempts spent today | **0** -- the 2-attempt budget is intact |

**The `fg=0` blocker that defeated the 07:00 automated fill is NOT present right now.** The desktop
is interactive and unlocked. That is a window, and it is the reason to act today.

### WHY THIS SEAT STOPPED HERE

The runbook is explicit and this seat wrote it:

> Only after 1-4 are eliminated is the sign-in the candidate remedy, and this seat **cannot complete
> one alone**. **Surface it with the eliminations attached and hold.** Do not attempt a login to
> "just try"; that is the lockout risk the P0 gate exists to prevent, **and it does not stop being a
> risk because the fault is real this time.**

Bloomberg locks the account on repeated failures. The escalation ledger shows one attempt spent on
09-23 and another on 09-27, both submitted with DAPI still down afterwards. So the budget has been
drawn on twice in six days and this seat will not draw on it unprompted.

> **ASK WITHDRAWN 2026-09-29 -- MOOT. The scheduled fallback signed in on its own authorization at
> 07:00 ET and the pull completed end to end. Nothing is owed by Andrew on this item. The paragraph
> below is retained because its DISTINCTION (Terminal login vs gateway OAuth) is still live law.**

**THE ASK IS ANDREW'S WORD TO RUN THE SIGN-IN -- not "stand by with your phone."** The Terminal
login is a person's Bloomberg login from Secrets Manager (`bloomberg/terminal/login`). The
"MFA goes to Andrew's phone" line belongs to the `opal-gateway-bbg` MS Entra identity, a DIFFERENT
login system; importing it into the Terminal runbook was a corrected error on 2026-08-12 and is not
repeated here. The one measured Terminal login (2026-08-11) required NO second factor, though
Bloomberg MAY demand B-Unit, in which case the procedure stops and needs the human who holds it.

Recommended: run `-Phase fill` FIRST. It costs **zero** attempts, is repeatable by construction, and
produces `C:/opal-elev/bbg_login_shot.png` for verification before any `submit` spends from the
budget.

---

## CORRECTION 2026-09-29 -- DEFECT 2's CAUSE WAS RIGHT; ITS STANDING WAS STALE WITHIN THE HOUR

**The diagnosis below is CORROBORATED at a second seat and needs no change.** `0.0.0_AB_MSTR~Z`
(msg 20260929T113533Z) independently determined the same cause and supplied the window this seat could
not see: **the machine PATH resolved `python` to the gutted Python 3.14 from 2026-09-26 17:02Z until
2026-09-28 19:42Z**, which is exactly the two fires (09-27, 09-28) that wrote no line.

**WHAT WAS WRONG IS THE TENSE.** This seat measured bare-`python` rc=1 at ~18:5xZ on 09-28 and
reported the watchdog as CURRENTLY DEAD and as certain to fire silently again. It was fixed at
**19:42Z, commit `be2d74b007`** -- about 45 minutes later -- and this seat then repeated the dead-
watchdog claim for the rest of the night, including once in a report that also named the 07:30 fire as
a coming "third silent fire". Today's 07:30 run returned **rc=0**, caught its own 72h gap, summoned
both seats, and then PASSED on data (`data_as_of=2026-09-28, expected_frontier=2026-09-29,
trading_days_behind=1`). **The instrument works.**

### THE MECHANISM THAT HID THE FIX, AND IT IS THE REUSABLE PART

A process's `PATH` is a SNAPSHOT taken at launch. This session started before 19:42Z, so every
`python` this seat ran all night resolved through the OLD PATH and kept returning rc=1 -- a TRUE
reading about THIS PROCESS and a FALSE one about the machine. Measured 2026-09-29:

| PATH source | rows containing `Python314` |
|---|---|
| `HKLM\...\Session Manager\Environment` (machine, authoritative) | **0** |
| `HKCU\Environment` (user) | **0** |
| **this session's inherited `$PATH`** | **4** |

A scheduled task launches fresh and therefore reads the CURRENT registry PATH, which is why the task
recovered while this seat's own shell could not observe it. **So a PATH claim measured inside a
long-lived process is only ever a claim about that process.** To assert what a future scheduled fire
will resolve, read the registry (or launch a fresh shell) -- never your own `$PATH`, and never
`where`/`command -v` inside the aged session.

**AND THIS SEAT HAD BANKED THIS EXACT LESSON.** `a-one-time-check-on-a-standing-condition-answers-a-
moment-not-a-property` was in memory before the session started, and the violation was still made --
which is the [[a-lesson-written-down-is-not-a-lesson-applied]] shape. The re-check cost one registry
read.

### WHAT SURVIVES AS A RECOMMENDATION (not a defect)

Pinning `freshness_check.cmd` to an absolute interpreter is still worth doing, but it is HARDENING, not
a repair: it makes the checker immune to PATH rather than dependent on PATH staying clean, which is the
discipline `scheduled_daily_pull.cmd` already follows and the reason that file survived the same
outage. Owner remains the CTO~Z lane; this seat cannot write `integrations/`.

---

## DEFECT 2 -- THE FRESHNESS WATCHDOG HAS BEEN DEAD SINCE 09-27, SILENTLY
> **SUPERSEDED as CURRENT STATE 2026-09-29 -- see the CORRECTION immediately above. The cause below is
> correct and corroborated; the "is dead" tense held only for 09-27 and 09-28.**

`OPAL_BBGTML_freshness_check` (07:30 ET daily) is the instrument that exists to summon this seat
when served data goes stale. It **ran** on 09-27 and 09-28 and **wrote nothing**.

| Evidence | Value |
|---|---|
| Task `LastRunTime` / `LastTaskResult` | 2026-09-28 07:30:01, **rc=1** |
| Checker's own exit contract | **0** fresh / **2** stale-summoned / **3** check-error-summoned |
| Is rc=1 in that contract? | **NO** -- it is outside the script's exit space entirely |
| Last line in `C:/opal-elev/freshness_check.log` | **2026-09-26T11:30:02Z** -- two fires missing |
| `freshness_check.cmd` interpreter | bare **`python`** (no absolute path) |
| `where python` under cmd.exe (the task's context) | `C:/Program Files/Python314/python.exe` **FIRST** |
| `Python314/Lib/` contents | **1 entry** (`site-packages`) -- no `encodings`, no stdlib |
| bare `python` rc, measured | **1** in bash AND **1** under cmd.exe |
| Error it dies with | `Fatal Python error: Failed to import encodings module` |

**rc=1 matches bare-python's own rc exactly and is outside the script's contract, so the interpreter
dies before the checker runs.** That is a match on the observed value, not a plausible story.

**These two defects are INDEPENDENT, and that matters for the fix.** `scheduled_daily_pull.cmd`
resolves every interpreter by ABSOLUTE path (`%PY%`, `%PY_AWS%`, `%PRICE_PY%`), which is exactly why
it got as far as a genuine DAPI verdict instead of dying like the checker. Do not fold one into the
other.

### The compounding, which is the real hazard

The pull is down AND the watchdog that would report it is down. Today that is harmless because the
data is genuinely healthy. **Tomorrow, when it stops being healthy, nothing will summon anyone.** A
watchdog whose failure mode is silence is indistinguishable from a watchdog with nothing to report.

### Ownership

The gutted-Python314-on-PATH defect is **already owned**: commit `e4403635d9` is a handoff prompt for
an ELEVATED `1.0.0_SA_CTO~Z` session to remove the Python314 rows from the machine PATH on Andrew's
standing approval. This seat is surfacing that the defect has a SECOND victim nobody had named --
the freshness checker -- not re-filing the PATH item.

Two candidate fixes, neither this seat's to land (`integrations/` is outside its write surface):
1. the owned PATH removal (fixes this and every other bare-`python` caller); and/or
2. pin `freshness_check.cmd` to an absolute interpreter, the same discipline its sibling
   `scheduled_daily_pull.cmd` already uses. Independently worth doing: it makes the checker immune
   to any future PATH regression rather than dependent on PATH staying clean.

---

## WHAT THIS SEAT DID AND DID NOT DO

**Did:** read the mail, ran the startup protocol, passed the identity gate (`opal-gateway-bbg` =
Opal Bloomberg, NOT Andrew), measured the pull history across all 30 retained logs, resolved the
trading calendar, ran runbook remedies 1-4, measured both sign-in preconditions, and closed the
freshness-checker causal chain.

**Did NOT:** attempt a Bloomberg sign-in (runbook gate, lockout risk, Andrew's word); edit
`freshness_check.cmd` or the machine PATH (outside write surface, already owned); build any alert or
monitor (standing moratorium).

**Broker note:** `opal-agent-comms` failed to connect this session (`CONNECTION_CLOSED`), so
`register_agent`, `get_agent_status`, `get_delivery_state` and `ack_messages` were all unavailable.
Mail was read off the filesystem via the armed watcher, which means **no ack clock moved** -- senders
of the 09-24 thread will still see their messages unacked. The 09-24 breach thread needed no act:
per the 09-28 routing pointer it is already dispositioned and ends RELEASED.
