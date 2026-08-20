# 0.0.3_BG_BBGTerminal — Session Log — 2026-08-18 (launch + daily guardrail, ~1855–1910Z)
**archetype:** VALIDATE

New session. Prior session's record: `logs/2026-08-12/post_reboot_upload_validation_1310-1325Z.md`
— **a six-day gap**, and that log closed with `BLOOMBERG DAPI DOWN`. Both conditions resolved
before I asserted anything about them.

## Summary
Launched, armed both monitors, and discharged the daily guardrail: **today's scheduled upload ran
on time and IS SERVED, with correct login-scoped CIX data.** The DAPI outage that closed the last
session is over. Backfilled a 7-day Teams window rather than letting a bare arm erase it. One
5-day-old inbound is unhandled and surfaced to Andrew rather than answered on my own read. Nothing
built.

## Launch protocol (prompt.md — no XXX.md; not a fabric work seat)
1. `register_agent` — was **NOT REGISTERED** (clean state). PID 2284.
2. `/watcher` — no `inbox-watch.sh` for my serial. The one on the box was `0.0.0_AB_MSTR~Z`'s at a
   different PID with a live eval-wrapper parent; **left untouched** (self-scoping + the dual-COO
   false-positive precedent). Armed `bbdkv7gjr`, confirmed `running` via `TaskOutput`. Inbox empty
   on both probes; `CronList` → zero crons.
2a. **IDENTITY ACCEPTANCE GATE — PASS.** `whoami` on `opal-gateway-bbg` → Opal Bloomberg
    (`opalbloomberg@opalinvest.com`). Ran before any Teams read.
3. Teams Monitor `b7qa0vazi` armed identity-pinned; banner confirmed
    `pin(server=opal-gateway-bbg, identity=opalbloomberg)` + `token selected:
    identity=opalbloomberg@opalinvest.com`.
4. `bloomberg_health` → `ok:true`, `//blp/refdata`. **Necessary, not sufficient** (my own 08-12
    correction) — the discriminating check is the CIX probe below, and it passed.
    `cma` interpreter confirmed RUNNABLE, not merely present: `C:\Anaconda\envs\cma\python.exe`
    → Python 3.13.2, pandas 2.2.3, **blpapi 3.26.4.2**.
5. Read the prior log and oriented.

**XXX.md Step 1b A.1 is STRUCTURALLY BLOCKED for this seat and that is correct.** The session-serial
file write (`org/mcp/sessions/<sid>.serial`) is denied by `bg-concierge-gate` G2 — repo content is
outside my writable set. **Identity therefore resolves via `$OPAL_AGENT_SERIAL`** (the gate's own
second source), verified `= 0.0.3_BG_BBGTerminal`. `liveness.json` cross-check clean: my serial at
**my** PID 2284, no peer holding it. Steps D (owned-paths hook) and E (`.comp-graph` context) are
likewise not applicable — this seat does no git work by design.

## DAILY GUARDRAIL — **TODAY'S UPLOAD RAN, ON SCHEDULE, AND IS SERVED**

**Scheduled task.** `OPAL_BBGTML_daily_pull`: LastRun **2026-08-18 07:00:01 ET**, Result **0**,
NextRun 2026-08-19 07:00, **NumberOfMissedRuns 0**. `OPAL_vendor_watch` hourly, last 14:09 ET, rc 0.

**Publish leg — verified by me, not by the log.** rc=0 is a producer self-report. Independent live
read of `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json`:
`data_as_of` **2026-08-17**, `generated_at` **2026-08-18T11:05:49Z**, LastModified 11:05:51Z,
19,203 B.

**Trading calendar resolved BEFORE any currency judgement (NEVER#1).**
`expected_last_trading_day(2026-08-18) = 2026-08-18`; served 2026-08-17 = **1 trading day behind**,
the correct healthy state for a T-1 pipeline. Tuesday; no weekend or holiday in play.

**Pull leg real.** PKLs `data/model 20260817 v1.pkl` written **07:02/07:03 today**.

### `.ST` CIX content check — run because today MATCHED the hazard shape, and it PASSED

Yang reported (Teams, 16:08Z today) *"Somehow the Bloomberg was logged out over the weekend."*
CIX resolution is **login-scoped** — the exact 08-03 hazard — so a pull that executed after a
logout/re-login is precisely the case that can succeed and still carry wrong custom-index data.

Measured on today's PKL through the pull's own `cma` interpreter:

| ticker | rows | inception | latest (2026-08-17) |
|---|---|---|---|
| `.ST Index` | 687 | 2023-12-29 @ 100.0 | **113.0911** |
| `.ST_BMK Index` | 687 | 2023-12-29 @ 100.0 | 118.6699 |
| `.ST_ETF Index` | 687 | 2023-12-29 @ 100.0 | 118.1965 |

**687 = 683 on 08-11 + exactly the 4 trading days since** (08-12, 13, 14, 17). `.ST` 112.9556 →
113.0911 is plausible drift. **Not** the known 1449-row/~1.9 mis-resolution.
**Denominator printed:** 112,205 `return_daily` rows, 84 distinct tickers, 2,061 matched `.ST*`.
**Positive control** `SPX Index` = 1,412 rows; **negative control** (bogus ticker) = 0. The
instrument discriminates in both directions — so the zero would have meant something.

*Queried on `bbg_ticker`, not `index_name` — the wrong-column empty set that nearly redirected the
08-12 investigation is banked and was not repeated.*

### The six-day gap, read from PKL mtimes — the 07:00 slot was NOT held every day

| PKL written (local) | data date | on the 07:00 slot? |
|---|---|---|
| Aug 12 07:02 | 20260811 | yes |
| **Aug 13 17:48** | 20260812 | **no — ~10.8h late** |
| **Aug 14 11:48** | 20260813 | **no — ~4.8h late** |
| **Aug 17 13:46** | 20260814 | **no — ~6.8h late** (Fri data on Mon = correct T-1) |
| Aug 18 07:02 | 20260817 | yes |

Consistent with the DAPI outage I escalated on 08-12 and the weekend logout Yang reports, with
someone re-running manually each day. **I am NOT asserting that mechanism** — I did not observe
those runs and the mtimes cannot distinguish a late automatic retry from a hand re-run. What is
measured: the data was produced every trading day and no date is missing. Today the slot is held
again. Recorded because a successor reading only `NumberOfMissedRuns 0` would conclude five clean
mornings, and that is not what the artifacts show.

## Teams — the 7-day window was MEASURED, not assumed

`teams-watch.cursor` still read **2026-08-11T09:34:48.861Z**. Before arming, I polled
`poll_addressed_teams_messages` explicitly from that cursor: **3 items across 7 days.** A bare arm
would have reset the cursor to `now_iso()` and made the entire window invisible — the arm looks
identical whether nothing arrived or everything did.

1. **Yang Liu thread (today, 16:08–17:54Z) — ALREADY HANDLED, by Andrew in person.** The
   "Opal Bloomberg" messages in it are **Andrew typing from this device** (*"Hey it's Andrew was
   just logging onto this device and saw this thread"*), and on 08-17 the same account was
   **Alyssa** (*"hi its Alyssa"*). Thread closes on Yang's *"Sounds good!"* / *"thank you"*.
   **Nothing outstanding for me.** Content worth carrying: Bloomberg logged out over the weekend;
   Andrew has fixed restart/update logouts and was fixing **mid-session** logouts; the VUG break is
   identified and fixed; he intends to have this seat instantiate at computer startup.
   ⚠ **Operationally important for this seat: the account is shared with humans.** A message on it
   is not necessarily addressed to the agent, and my own outgoing history is not all mine.
2. **Alyssa Keith, 2026-08-13T21:41Z — `"ajb 0.0.0_AB_MSTR~Z ?"` — UNHANDLED, 5 days.** Reads like
   a novice user asking whether that is the right launch command. **Not answered on my own read**
   and not silently dropped: the intended recipient is genuinely ambiguous (see the shared-account
   point above — she may have been asking Andrew, not the agent), it is 5 days cold, and Andrew is
   at this terminal now. Surfaced to him with a draft reply ready. TEAMS_DUTY ladder #3 (ambiguous
   → one clarifying question) is the fallback if he wants me to take it.

**Cursor mechanic, corrected in the same turn I got it wrong.** I wrote the backfilled cursor to
`/tmp/teams-watch.cursor` and the Windows-Temp copy. **Neither is the file the monitor reads.**
`teams-watch.py` runs under **native Windows Python 3.11**, where `TMPDIR` is unset and `/tmp`
resolves to **`C:\tmp`** — the banner then armed at `2026-08-12T13:22:11Z`, not my value, which is
how I caught it. Two stale decoy copies exist at the Git-Bash and Windows-Temp paths and will
mislead the next reader. Live file: **`C:\tmp\teams-watch.cursor`**, now correctly at
`2026-08-18T17:54:21.641Z` — advanced **by the monitor itself**, not by my write. *My action was a
no-op that converged on the right answer; recording it as a success would have banked a false
mechanism.* Same `/c` vs `/cygdrive/c` vs native-Windows path-form family as
`[[native-python-cannot-read-cygdrive-paths]]`.

## State
ON DUTY. Fabric inbox Monitor `bbdkv7gjr`, Teams Monitor `b7qa0vazi` (identity-pinned), broker
LIVE, **zero crons**. Bloomberg DAPI **UP** (`ok:true`, entitlement confirmed by CIX resolution,
not by process presence). Portal serving current T-1 (`data_as_of 2026-08-17`). Next scheduled run
2026-08-19 07:00 ET.
**Known residual (unchanged, not papered by me):** while idle this seat makes no gateway calls by
definition, so Teams polling halts at each ~hourly token expiry and resumes only on my next
gateway call. Messages **queue rather than drop** (`cursor` cannot advance while `tok` is falsy).
Latency defect, not loss.
**Open item:** Alyssa's 08-13 message, awaiting Andrew's call.

## Compiler Tools
None fit the surfaces touched. `comp-which "how do I grep the repo"` was run once as the mandatory
XXX.md A.3 EXERCISE check (91 of 97 comp-tools resolve bare; the forwarder RAN, routing to
`comp-find` with its own denominator banner — resolution is not execution). The session's actual
reads were a Windows Scheduled Task execution record, local PKL contents through the `cma`
interpreter, two Teams threads via the gateway, and **one** served-artifact read by exact key —
a content read of a known key, not an inspection or a prefix sweep. `comp-freshness` answers
"is the object old", which is a different question from "does the JSON body carry the right
`data_as_of`", and no comp tool models Scheduled Tasks, PKL contents, or Teams.
