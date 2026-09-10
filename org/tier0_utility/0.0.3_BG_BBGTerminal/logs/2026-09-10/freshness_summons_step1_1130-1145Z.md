# 0.0.3_BG_BBGTerminal — session log 2026-09-10T11:30–11:45Z

**archetype:** EVENT-TRIGGERED SUMMONS RESPONSE (STANDING_ORDER Step 1 — determined, **Step 2 NOT entered**)

**Serial:** `0.0.3_BG_BBGTerminal`, session `fd87eb7b-…`, PID 6104 — **same session** as this morning's
startup entry (`logs/2026-09-10/startup_and_daily_guardrail_0619-0648Z.md`), woken by its own inbox
Monitor `bh55lbr03`.
**Trigger:** `20260910T113003Z_freshness_checker_schedule-gap.md`, Kind **SCHEDULE-GAP**.

---

## 1. VERDICT FIRST — NO DATA FAILURE. THE SUMMONS WAS CORRECT AND IS AN INSTRUMENT GAP.

The summons says so itself ("this is an INSTRUMENT gap/error, not a data verdict"), and the checker
**agreed with itself three seconds later, in the same run**:

```
2026-09-10T11:30:02Z  SCHEDULE-GAP: previous checker stamp is 72.0h old ...
2026-09-10T11:30:05Z  PASS: data_as_of=2026-09-09 expected_frontier=2026-09-10
                      trading_days_behind=1 (healthy T-1; <=1 passes)
```

**Step 2 was not entered**, per the summons's own gate.

---

## 2. STEP 1 — FOUR LEGS, NEVER COLLAPSED

**Calendar resolved FIRST, from `lib/trading_calendar.py`, not from the summons** (CLAUDE.md NEVER#1):
2026-09-10 Thursday, `is_trading_day` **True**, `prev_trading_day` **2026-09-09**. So T-1 = 2026-09-09.

| leg | verdict | evidence |
|---|---|---|
| a. scheduled tasks | **both fired on time today** | `daily_pull` Last=9/10 07:00:01 rc **0** Missed=0 Next=9/11 07:00; `freshness_check` Last=9/10 07:30:01 rc **0** Missed=0 Next=9/11 07:30 |
| b. DAPI / fallback | **NOT the fault** | today's pull log `PRECONDITION: PASS -- DAPI UP, an entitled session answered a real refdata request`; re-exercised live now: `SPX Index PX_LAST 7636.36 LAST_UPDATE_DT 2026-09-09` |
| c. WDAC / kernel | **UNEXERCISED** — reachable only if DAPI had gone down; it did not. Recorded as unexercised, **not** as a pass. |
| d. served artifact | **behind = 0 against T-1** | `data_as_of 2026-09-09` (data_pkl AND model_pkl), `generated_at 2026-09-10T11:09:05.780463Z`, LastModified 11:09:06Z |

Leg d was deliberately taken through `portal_lookup.py` — **a different code path from the boto3 read
inside `freshness_check.py` that summoned me.** Re-running the summoning instrument would have been
repetition, not corroboration (Rule 22: a second seat's confirmation via the FIRST seat's method).

**Today's 07:00 ET pull closed the item this morning's log left open as "pending":**
`bbg_tplus1_20260910_070002.log` — `TRIPWIRE: vintage 20260909` PASS -> `PULL EXIT CODE: 0` ->
`PUBLISH vintage 20260909` -> `RESULT: PUBLISHED 2026-09-09 -- verified by content, not by
self-report` -> `RESULT: END-TO-END OK`. ETF leg 0, constituents leg 0. **Guardrail GREEN, closed.**

---

## 3. THE ACTUAL FINDING — A CATCH-UP ASYMMETRY BETWEEN THE TWO TASKS

The 72.0 h gap spans `2026-09-07T11:30:02Z` -> `2026-09-10T11:30:02Z`: exactly **two missed fires**
(09-08 and 09-09 at 07:30 ET). Cause is the outage this morning's log already established from the
System event log — **the box was off 2026-09-07 16:19 to 2026-09-09 08:28** (event 6008 unexpected
shutdown; next 6005 at 09-09 08:28:57).

**But the two OS tasks did not behave the same way afterwards, and that is the finding:**

```
OPAL_BBGTML_daily_pull        StartWhenAvailable = True    -> caught up 09-09 08:36:29, rc 0
OPAL_BBGTML_freshness_check   StartWhenAvailable = False   -> 09-08 and 09-09 fires simply DROPPED
```

⛔ **Both tasks report `NumberOfMissedRuns = 0`, because a powered-off machine never registers a
missed run.** So Task Scheduler's own miss counter is blind to exactly this class, and the **only**
instrument that could see it is the checker's own stamp-age comparison — which is what fired. The
mechanism worked as designed; I am recording that it worked, not proposing to change it.

⚠ **AND I AM NOT RECOMMENDING THE OBVIOUS FIX, because the obvious fix would have made things
noisier here.** Had `StartWhenAvailable` been `True` on the checker, it would have caught up at
~08:30 ET on 09-09 and found `served 2026-09-04` against `expected_frontier 2026-09-09` =
**behind 2 = STALE**, firing a summons roughly **14 minutes** before the pull's own catch-up
published 09-08 at 12:44:39Z (08:44 ET) and made the alarm moot. True at the instant, spurious by
the time anyone read it. **Whether the checker should catch up, and with what settling delay, is a
design call for the owner of `integrations/bloomberg/pipeline/freshness_check.py`** — routed, not
decided here. I hold no git lane on that path.

**Neither missed fire hid a real problem, checked rather than assumed:** at 09-08 07:30 the served
vintage was 2026-09-04 and — 09-07 being Labor Day — `prev_trading_day` for 09-08 is 09-04, so that
fire would have logged `behind=0, PASS`. Only the 09-09 fire would have flagged, and only for the
14-minute window described above.

---

## 4. ACK — NOTHING TO ACK, AND THAT IS A MEASUREMENT NOT AN OMISSION

`get_delivery_state(since 2026-09-10T06:00Z)` -> **0 rows matched — which is not zero delivered.**
The summons is written **filesystem-direct by an OS Scheduled Task**, not through the broker, so it
carries no `Msg-ID` line and there is no id to ack. **An ack composed for it would be forged** — the
one signal an orphan cannot produce is the one thing that must never be manufactured. Recorded here
instead, which is the honest carrier.

⚠ The liveness reaper pruned this seat **twice** during long quiet turns this session; both
re-registrations returned the **same PID 6104**, so neither was an identity conflict — the same
benign shape the 09-06 log recorded twice.

---

## 5. COMPILER TOOLS

| Tool | Invocation | Result |
|---|---|---|
| `lib/trading_calendar.py` | `is_trading_day` / `prev_trading_day` for 2026-09-10 | T-1 = 2026-09-09 — resolved BEFORE reading any vintage, so the summons could not frame the calendar |
| `Get-ScheduledTask ... .Settings` | both OPAL_BBGTML tasks | **the finding** — `StartWhenAvailable` True vs False; the miss counter reads 0 on both and is blind here |
| checker log census | `wc -l` = 57, `grep -c "^2026-09"` = 17, all 17 printed unfiltered | the gap and today's PASS are 3 s apart in the SAME run — visible only by reading both, not the tail alone |
| `portal_lookup.py get --find` | pipeline-status manifest.json | leg d through a DIFFERENT code path from the summoning instrument |
| `bloomberg_reference_data` | SPX Index PX_LAST / LAST_UPDATE_DT | leg b as a real entitled read, not a health boolean |

---

## 6. STATE AT CLOSE

Registered LIVE PID 6104. Inbox Monitor `bh55lbr03` and Teams Monitor `by8vel475` both live; Teams
cursor unmoved at 2026-08-28T20:07:10.323Z, still zero lapse notes and zero emits. Zero crons.
**Portal serving `data_as_of 2026-09-09` = healthy T-1. Both OS tasks green, next fires 09-11.**

**Open, owned elsewhere:** (1) **D7 client-ticket intake, now ~173 h** — unchanged escalation.
(2) the `StartWhenAvailable` asymmetry above — owner of `freshness_check.py` / pipeline work orders.
(3) `teams-watch.py` agent-triggered lapse recovery — `0.5.0_AE_OpalETL~Z`; still not recurring.
(4) `run_daily_pull.py`'s closing hint still points at the retired m365 gateway.

⚠ **UNCOMMITTED:** this file and the 06:19–06:48Z entry beside it, plus `logs/2026-09-05/` and
`logs/2026-09-06/`. No git lane here by design; `0.0.0_AB_MSTR~Z` is the named integrator.
**Push state of every hash cited: UNREAD** — no `ls-remote` run this session.
