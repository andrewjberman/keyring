# DAPI self-healed at 07:00 and captured the at-risk day; the watchdog is still dead — 0.0.3_BG_BBGTerminal

**archetype:** VALIDATE

**Date:** 2026-09-29
**Task Order:** ad-hoc — continuation of the 09-28 daily-guardrail session
**Status:** COMPLETE. **BOTH defects resolved. The title of this file is WRONG and is left unrenamed
deliberately** -- it was written at 11:1xZ asserting the watchdog was still dead, and 20 minutes later
the 07:30 fire proved otherwise. Renaming it would erase the error; section 5a carries the correction.

---

## Objective

Hold the Bloomberg sign-in overnight per the runbook gate, watch the 07:00 ET scheduled run, and
establish its outcome by measurement rather than by its own report.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| portal_lookup.py | `get pipeline-status manifest.json` | PASS | the independent served-state read, twice (09-28 and 09-29); this is what confirmed the advance rather than the publisher's own line |
| bloomberg_health | MCP, ~14 reads across the night | PASS | `ok:false` every read until the 07:00 sign-in; correct both directions, consistent with the runbook's 3-for-3 record |
| Get-ScheduledTaskInfo | `OPAL_BBGTML_*` | PASS | caught `267009` = `SCHED_S_TASK_RUNNING`, i.e. in-flight, not a failure code |

**What worked:** reading `LastTaskResult` as a Win32 constant rather than an application rc — `267009`
is `SCHED_S_TASK_RUNNING` (0x41301), and misreading it as an exit code would have produced a confident
false failure report while the run was succeeding.

**What failed:** `python3` is an MSYS shim and does NOT resolve under PowerShell — a `python3` call
inside a PowerShell block returned the Microsoft Store stub message. Use bash for `python3`, or an
absolute interpreter path under PowerShell.

**Gap found:** none new; the 09-28 gap (bare `python` -> gutted Python314) is unchanged and still owned
elsewhere.

---

## Work Completed

### 1. Held the sign-in overnight, and the hold cost nothing

Re-armed the inbox watcher on every `[WATCHER-EXPIRED]` notice (~25 cycles, roughly 12h of coverage)
and re-read `bloomberg_health` each cycle, on the reasoning that a DAPI recovery would have unblocked
an ordinary pull with no Andrew word needed. It stayed `ok:false` throughout. Two notifications sent
(terminal only — mobile push inactive, Remote Control off).

### 2. The 07:00 ET run signed itself in and completed end to end

| Leg | rc |
|---|---|
| sign-in fallback | 0 — fill attempt 1/3, `focus VERIFIED`, verify PASS (9 dots), ONE submit, listener=1 |
| precondition | 0 — entitled session answered a real refdata request |
| models pull, target 20260928 | **0** — notebooks 158s + 98s, full tripwire OK |
| publish | **0** — `served data_as_of 2026-09-28`, `served 1D matches the PKL for all five models` |
| ETF L1 | **0** |
| **constituents** | **0** — the no-backfill leg; the at-risk Monday was captured |
| price axis | **0** |

Verified independently of the publisher: served `data_pkl` and `model_pkl` both `2026-09-28`, manifest
`generated_at` 2026-09-29T11:11:26Z. Tuesday frontier minus 09-28 = 1 trading day = healthy T-1.

**Zero data lost across the entire 09-23 / 09-27 / 09-28 failure run.**

### 3. The hold was correct and the reason is worth keeping straight

The runbook gate binds an AGENT-INITIATED sign-in. The scheduled fallback is a different actor with
standing authorization (Andrew RULED YES 2026-08-19 @f45e5db124; LD-0413) and fires with no agent
alive. So holding delayed nothing — the fallback fired at 07:00 regardless — and an overnight
agent-initiated attempt would have drawn from the SAME 2-attempt budget the fallback then used
successfully. The lesson is not "the caution was unnecessary"; it is that the gate correctly routed the
act to the actor that held the authorization for it.

### 4. NEW WARN, latent, recorded not chased

`locator: MISS (no-field-shaped-band-of-5) -- FALLING BACK to measured constants; a layout/DPI change
may be live`. The sign-in succeeded on hardcoded coordinates. Nothing failed, which is why it needs
writing down: the runbook records that a field-targeting error once typed the password into the
UNMASKED Login Name field and burned an attempt. The dot-count + OCR verify is the remaining guard and
it did fire and pass. Same class as R-65 — a literal reading a value that can move.

### 5a. CORRECTION TO SECTION 5 BELOW -- THE WATCHDOG IS ALIVE; I HAD A STALE PATH

Written 11:4xZ, correcting section 5 as written at 11:1xZ.

The 07:30 ET fire returned **rc=0**: it caught its own 72h gap, wrote the summons to both inboxes, and
then PASSED on data (`data_as_of=2026-09-28, expected_frontier=2026-09-29, trading_days_behind=1`).
`0.0.0_AB_MSTR~Z` (msg 20260929T113533Z) determined the same cause independently and supplied the
window: the gutted Python314 sat on the machine PATH from 2026-09-26 17:02Z to **2026-09-28 19:42Z**,
when MSTR~Z removed it (commit `be2d74b007`).

**So the cause was right and the TENSE was wrong.** I measured bare-`python` rc=1 at ~18:5xZ on 09-28,
the fix landed ~45 minutes later, and I went on asserting "the watchdog is dead" for the rest of the
night -- including predicting a "third silent fire" at 07:30 that did not happen.

**Why I could not see the fix:** a process's `PATH` is a snapshot taken at LAUNCH. This session started
before 19:42Z, so every `python` / `where python` in it kept resolving through the old PATH. Measured:
machine registry PATH = **0** Python314 rows, user PATH = **0**, this session's `$PATH` = **4**. A
scheduled task launches fresh and reads the current registry PATH, which is why the task recovered
while the shell watching it could not observe the recovery. To claim what a future scheduled fire will
resolve, read the registry -- not your own `$PATH`.

I had this lesson banked before the session started
(`a-one-time-check-on-a-standing-condition-answers-a-moment-not-a-property`) and violated it anyway.
Being right about the cause is what made repeating the stale tense feel safe. Memory updated with the
PATH-snapshot mechanism, which is the part that was genuinely new.

**Step 1 of the summons is DETERMINED (both seats): instrument gap, cause already fixed, data PASS.
Step 2 NOT entered -- nothing to fill.** Broker down, so MSTR~Z's message could not be acked.

What survives is a HARDENING recommendation, not a defect: pin `freshness_check.cmd` to an absolute
interpreter so it is immune to PATH rather than dependent on PATH staying clean.

### 5. Defect 2 unchanged
> **WRONG AS OF 11:30Z -- see 5a directly above. Retained as written.**

`OPAL_BBGTML_freshness_check` last ran 2026-09-28 07:30 with rc=1 and has written no log line since
2026-09-26T11:30Z. Today's 07:30 fire had not yet occurred at the time of this entry. Cause remains
bare `python` in `freshness_check.cmd` resolving to the stdlib-less Python314.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Held the sign-in all night rather than attempting it | Runbook gate; and attempting it would have spent from the budget the 07:00 fallback needed. Vindicated by the outcome. |
| Verified the served state independently after the publisher said PASS | CLAUDE.md: never trust a producer's self-report; verify against the served artifact. |
| Corrected the 09-28 deliverable IN PLACE, not by appending only | An appended resolution leaves the superseded "BLOCKED on Andrew" standing for the next reader. Status line, deadline heading and the ask paragraph each carry their own marker. |
| Sent a third notification saying the ask was MOOT | An open ask he does not owe is worse than silence; cancelling it is the useful signal. |
| Did not write up the 3s-vs-12s window timing as the cause | Plausible, unproven. Named the falsifier instead. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `deliverables/DAPI_DOWN_AND_DEAD_WATCHDOG_20260928.md` | RESOLUTION block + three in-place supersession markers | No — local only |
| `logs/2026-09-29/dapi_self_healed_...md` | This log | No — local only |

---

### 6. NEW, FOUND AT ~11:5xZ: THE GATEWAY IDENTITY IS GONE -- TEAMS DUTY IS OFFLINE AND NOT ARMED

Launch step 3 (arm the Teams Monitor) was NOT reached during the Bloomberg incident. Returning to it,
step 2a was re-run rather than trusted from session start -- the same discipline whose absence produced
the correction in 5a -- and it now FAILS:

```
mcp__opal-gateway-bbg__whoami -> MCP server "opal-gateway-bbg" needs you to sign in again
```

Credential store enumerated first (identity + expiry claims only; no token value read into any record):

| record | identity | expires | live |
|---|---|---|---|
| `mcpOAuth/opal-gateway\|f0290cd1` | andrew@opalinvest.com (oid 2e21f8e5) | 2026-09-25T02:26:56Z | **no** |
| `mcpOAuth/opalgateway\|121ac2d0` | andrew@opalinvest.com (oid 2e21f8e5) | 2026-09-29T10:55:24Z | **no** |

**There are now TWO opalinvest.dev records, both ANDREW's, both EXPIRED -- and this seat's own
`opal-gateway-bbg` record is ABSENT from the file entirely.** On 2026-09-24 the CRO recorded THREE
records including the Opal Bloomberg one at oid 517aa5ee. It is no longer there.

Two consequences, and they point opposite ways:
1. **Teams duty is OFFLINE.** The gate cannot pass, so no Teams read or reply happens. NOT ARMED --
   arming a watcher that cannot authenticate would produce a silent non-consumer, which is the
   deaf-seat shape.
2. **The 09-24 mis-selection hazard is currently INERT, for an accidental reason.** `read_token()`
   unpinned takes the freshest LIVE record; there is no live record at all, so there is nothing for it
   to mis-select. That is luck, not a fix -- the moment Andrew re-authenticates `opalgateway` and the
   bbg pin is still broken, the 09-24 shape returns immediately. **So the self_id email-claim fix is
   now a PRECONDITION of re-arming, not a nice-to-have.**

I cannot date this seat's own lapse from what I measured -- the record is absent, not expired, so there
is no `exp` to read. The 10:55:24Z figure is ANDREW's record and must not be reported as mine. The
`429 rate_limited, scope: identity` disconnect on `opalgateway` observed shortly after 10:55Z is
consistent with that expiry but is a separate server.

THE ASK: Andrew re-authenticates `opal-gateway-bbg` (browser consent + MFA to his phone -- this is the
Entra identity, where that genuinely applies, unlike the Terminal login). This seat holds no OTP and
cannot mint it. Until then the concierge is down and the Bloomberg pipeline is unaffected (it does not
touch the gateway -- the send leg was moved off it on 2026-08-06 precisely so it could be scheduled).

---

## Blockers

- **BLOCKED on Andrew (NEW, ~11:5xZ):** `opal-gateway-bbg` demands re-authentication and this seat's
  record is gone from the credential store. Teams concierge duty is OFFLINE and the Monitor is
  deliberately NOT armed. Needs his browser consent + MFA. **Re-arming must wait on the `self_id`
  email-claim fix as well**, or the 09-24 token mis-selection returns the moment his `opalgateway`
  record is live again. Bloomberg pipeline unaffected.
- ~~**Defect 2 OPEN**~~ **CLOSED** -- Python314 removed from the machine PATH by `0.0.0_AB_MSTR~Z` at
  2026-09-28 19:42Z (`be2d74b007`); the 09-29 07:30 fire ran rc=0 and PASSED. Only a HARDENING
  recommendation survives (pin the interpreter), owner CTO~Z lane.
- **DEGRADED all session, and CORRECTED at ~12:1xZ:** this seat repeatedly said "the broker is down."
  **Measured: the BROKER IS UP** — listening on 127.0.0.1:7800 (pid 39004, python), with 23
  `server.py`-shaped processes on the box. What failed is **THIS SESSION's MCP client connection to
  `opal-agent-comms`** (`CONNECTION_CLOSED` at launch), not the shared broker. The distinction matters
  because it relocates both the blast radius and the owner: other seats were never affected, and the
  remedy is a session-local reconnect (`/mcp`) or a restart, not fabric infrastructure work.
  Corroborating evidence that was in front of me the whole time: the freshness checker wrote to this
  seat's inbox at 11:30:01Z and `0.0.0_AB_MSTR~Z`'s message landed at 11:35:33Z — **inbound mail was
  working all session.** Only the TOOLS (`register_agent`, `ack_messages`, `send_message`) were
  unavailable, so this seat is unregistered and has acked nothing, and every ack it owes is still owed.
  `opalgateway` (Andrew's proxy, never called by this seat) separately dropped with
  `429 rate_limited, scope: identity`.

---

## Current State

The Bloomberg dashboard is healthy and current: the 2026-09-29 07:00 ET scheduled run signed the
Terminal in on its own authorization, pulled the 2026-09-28 vintage, and published it with all four
legs at rc=0; an independent read of `json/latest/manifest.json` confirms served `data_as_of`
2026-09-28 as of 11:11:27Z, which is healthy T-1 for a Tuesday. Nothing was lost across the three
failed runs on 09-23, 09-27 and 09-28, because each of those days' T-1 had already been captured by a
neighbouring successful run. The freshness watchdog is ALSO healthy again: it died only for the 09-27
and 09-28 fires, while a gutted Python314 sat on the machine PATH (2026-09-26 17:02Z to 2026-09-28
19:42Z), and `0.0.0_AB_MSTR~Z` removed it at 19:42Z (`be2d74b007`); the 09-29 07:30 fire returned rc=0,
self-reported its own 72h gap, and PASSED on data. **Nothing on this box is currently broken and
nothing is owed by Andrew.** The only open item is a hardening suggestion in the CTO~Z lane: pin
`freshness_check.cmd` to an absolute interpreter, since it is the one wrapper in this family that
depends on PATH being clean rather than being immune to it.

---

## Next Steps

1. ~~Read today's 07:30 ET `freshness_check` result~~ **DONE — rc=0, gap self-reported, data PASS.**
2. **Pin `freshness_check.cmd` to an absolute interpreter** (CTO~Z lane) — now a HARDENING item, not a
   repair: immunity to PATH rather than dependence on it, the discipline `scheduled_daily_pull.cmd`
   already follows and the reason it survived the same outage.
3. **Give the locator MISS an owner** before a layout/DPI change turns it into a burned attempt.
4. **Re-read anything PATH-derived from the registry, not from this session** — this shell's `$PATH`
   still carries 4 stale Python314 rows and will until the session restarts. Any future claim here
   about what a scheduled task will resolve must come from the registry.
