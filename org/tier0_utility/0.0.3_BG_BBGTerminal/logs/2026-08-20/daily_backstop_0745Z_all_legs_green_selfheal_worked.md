# 0.0.3_BG_BBGTerminal — 07:15 DAILY BACKSTOP, first fire — 2026-08-20 (read ~07:45 ET / 11:45Z)
**archetype:** VALIDATE

First fire of the Andrew-direct standing order (@eede873a2f), cron `8b5d18cb`. Per-leg attribution
as ruled. **NO Step-2 recovery invoked — the scheduled run succeeded on its own.**

## VERDICT: ALL FOUR LEGS GREEN. The device self-healed untouched, and the WDAC acceptance is
## PASSED *and genuinely exercised*. One defect found — in the backstop I armed, not the pipeline.

| Leg | Verdict | Evidence |
|---|---|---|
| a. Scheduled task | **PASS** | `LastRun 2026-08-20 07:00:01 ET`, **`LastResult = 0`**, NextRun 08-21 07:00. `NumberOfMissedRuns` deliberately NOT read as health |
| b. Fallback / self-heal | **PASS — the headline** | `wintrv.exe` StartTime **07:00:25 ET, 24s after the task fired**; `C:\blp\` processes **4 -> 54** (denominator printed both nights); 8194 **Listen** (pid 31428, the bbcomm that survived the night); `bloomberg_health ok:true //blp/refdata` |
| c. WDAC / kernel | **PASS, and EXERCISED** | CodeIntegrity 3033/3077 since 07:00: **0**. **Positive control: 10 in the last 3 days**, latest 08-19 08:49:27 + 08-19 07:00:08 (the original failure) — the instrument reads, so the zero means something |
| d. Publish / served | **PASS, by content** | `data_as_of` **2026-08-19**, `generated_at 2026-08-20T11:09:05Z`; object 19,184 B, ETag `0817a61dcc98afddcb0a7b3aebde1551`, LastModified `2026-08-20T11:09:06Z` (UTC plane — `s3api`, never `s3 ls`, which renders LOCAL unmarked) |

**Trading calendar resolved FIRST (NEVER#1):** `expected_last_trading_day(2026-08-20) = 2026-08-20`;
served `2026-08-19` -> `trading_days_behind = 1` = **the correct healthy state for a T-1 pipeline.**

## >> ANDREW'S RULING WAS RIGHT AND MINE WOULD HAVE BEEN WORSE
I filed the dead Terminal as urgent and asked to sign in. He ruled option (b) — *"the whole point is
that the device needs to be able to figure this out and get it done on its own accord."* **Leg b is
the proof.** Had I signed in last night, the self-heal would have run against a healthy Terminal and
proved nothing: **the one available live exercise would have been consumed by my pre-emption.**
The condition I reported as a problem *was the test*. Banking this as the reasoning error, not just
the outcome: I priced the risk of the acceptance failing and never priced the cost of never learning
whether the fallback works.

## `.ST` CIX content check — RUN, AND WARRANTED (a green rc cannot clear it)
The Terminal signed in **fresh at 07:00:25** and the pull ran immediately after — the exact
login-scoped shape (08-03) where a run SUCCEEDS and still carries wrong custom-index data. Measured
on today's PKL (`data 20260819 v1.pkl`, written 07:05) through the pull's own `cma` interpreter:

| series | rows | inception | latest 2026-08-19 | vs 08-18 |
|---|---|---|---|---|
| `.ST Index` | 689 | 2023-12-29 @ 100.0000 | 113.3085 | 113.1072 (+0.178%) |
| `.ST_BMK Index` | 689 | 2023-12-29 @ 100.0000 | 119.0850 | 118.6242 (+0.388%) |
| `.ST_ETF Index` | 689 | 2023-12-29 @ 100.0000 | 118.6614 | 118.1081 (+0.468%) |

**689 = 688 on 08-18 + exactly the 1 trading day since.** NOT the known-bad 1449-row/~1.9
mis-resolution. **Denominators:** `return_daily` **112,373** rows (= 112,289 + 84 — one day across
84 tickers), 84 distinct tickers, max date 2026-08-19, **2,067** `.ST*` rows (= 2,064 + 3).
**POSITIVE CONTROL** `SPX Index` = **1,414** (= 1,413 + 1); **NEGATIVE CONTROL** bogus ticker = **0**.
Discriminates both directions. Queried on `bbg_ticker`, not `index_name`.
`max|ret|` figures are series-wide and in **PERCENT native units — not re-scaled**; double-scaling
that column is what manufactured a false 68% market anomaly on 08-11.

## >> DEFECT FOUND — IN THE BACKSTOP I ARMED, NOT THE PIPELINE
**The cron fired ~07:45, not 07:15 — a ~30-minute lag on a mechanism Andrew designed around
"15 min after the cron."** Cause: `CronCreate` jobs fire only while the REPL is idle, plus scheduler
jitter. **Today it cost nothing because there was nothing to recover.** On a day that NEEDS Step 2,
recovery would begin **~45 min after the failure rather than ~15** — and the point of the 15-minute
figure is to land the fix before the business day.

**Proposed no alarm and no monitor** (standing moratorium — the cheapest-feeling wrong deliverable
here). **Routed to CTO~Z / Andrew as a SCHEDULING-MECHANISM question:** an in-session cron is a soft
timer backstopping a **hard OS Scheduled Task**. If the 15 minutes is load-bearing, the backstop
likely wants to be an OS Scheduled Task too — but that is a route/schedule design call, not mine to
make or to build. **Surfacing, not chasing.**

*Note the shape: I armed a session-only soft timer to backstop an OS-level hard schedule, and the
mismatch was invisible until the thing actually fired. The arm reported success; only the FIRE
measured the latency.*

## Inherited, unchanged, FYI not action
The superseded-but-still-present conda `win32\pywintypes313.dll` (2024-10-11). It did not load and
did not block today.

## Reporting
`send_message` to 3 seats, **per-recipient denominator 1 DELIVERED / 2 QUEUED / 0 REFUSED** —
MSTR~Z delivered (id 2087); COO~Z (2088) and CTO~Z (2089) **QUEUED, no live session**. Queued is
written, **not read** — the CTO~Z scheduling item above is waiting on a seat, not acted on.

## Compiler Tools
| Tool | Result |
|---|---|
| `lib/trading_calendar.py` (`expected_last_trading_day` / `trading_days_behind`) | the ONE frontier definition — resolved BEFORE any staleness read, per NEVER#1 |

No comp tool fits the rest and I did not force one. The surfaces were a Windows Scheduled Task
record, the CodeIntegrity event log, a live process/port enumeration, PKL contents through a
specific interpreter, and ONE served object read by exact key + body. `comp-freshness` answers "is
the object old", which is not "does the body carry the right `data_as_of`" — the question I asked.

## ~1218-1220Z — my launch runbook slimmed under LD-0427 @f05cf32053 — VERIFIED, not received
Integrator slimmed `refs/RELAUNCH.md`. I read it **from `origin/SITEZ`** rather than filing the FYI:
this file is my successor's launch path, and **a slimming edit is precisely the operation that drops
what it claims to preserve.**

- 127 -> 113 lines. **Positive control** (a known line -> 1) so the retrieval discriminates.
- **§0b INTACT** at the same pre-launch position — re-arm order, `CronCreate("15 7 * * *", ...)`,
  deliverable pointer, ruling record `@eede873a2f`, and the explicit arm-ZERO-crons exception.
- **Step-5 contradiction genuinely fixed:** now *"arm the §0b standing-order cron and NOTHING else"*.
  The old *"arm ZERO crons"* would have pointed a successor **away from a live sovereign order two
  sections up**. That was a real defect and **I did not spot it when I requested the row** — I asked
  for a pointer and never checked whether the surrounding text contradicted it.
- P1–P4: all four rows present.
- **Pointer chain resolves end-to-end** (checked, not assumed): the deliverable resolves on the ref,
  64 lines, carrying both the cron expression and the fire-once discipline; `@eede873a2f` resolves
  and is on `origin/SITEZ`. **Nothing dangling.**

### Stated property of the new shape — recorded so it is known, not discovered
§0b's body is now the placeholder `<the backstop check>`; the firing procedure lives entirely in the
deliverable. **The order is 2 hops instead of 1.** Correct under LD-0427 and I would not reverse it —
but **the failure mode moved**: if the deliverable were swept, renamed or slimmed away, **§0b would
still READ perfectly correct and arm a cron with no procedure behind it.** A successor gets a green
launch and an empty order.

**No gate, check or monitor proposed for it** — one line of awareness for the row's maintainer.
**My half is cheap and mine anyway: spot-check the chain from the ref at each relaunch.**

## LAG RECORD (CTO~Z R1, ruling @008135604e) — n=1
```
armed 07:15 ET / fired <=07:45 / lag ~30 min
```
**Honest bound on "fired":** I did not capture the fire instant. What is measured is that my FIRST tool
call of the fire returned `07:45:23 ET`, so the fire was **at or slightly before 07:45:23** and the lag
is **~30 min, not exactly 30**. Recorded as an observation, **not a monitor** — no alarm, no threshold,
no escalation. **Redesign considered at n>=5**, never off one day.

## ~1229Z — CTO~Z RULED ON MY TIMING SURFACING, AND THE REFRAME IS SHARPER THAN MY FINDING
Ruling `@008135604e`. **(R1)** session cron STANDS as the carrier; keep re-arming per §0b; add the lag
record line above. **(R2)** the load-bearing softness is **not the jitter I found**.

> **THE REFRAME:** my finding was about the **LATENCY of a check that ran.** Theirs is about the
> **EXISTENCE of the check at all** — *the session cron exists only on days an operator relaunched this
> seat before 07:15. On a seat-down day there is no cron, no check, and NO SIGNAL THAT THERE WAS NONE.*
> **The absence of a check produces no artifact, so nothing reports it.** A lag you can measure is
> strictly safer than a check that silently did not exist.

**MY SECOND INSTANCE OF ONE BLIND SPOT TODAY, and I want it recorded as a pattern, not two incidents.**
This morning I never asked whether my own logs were REACHABLE — I measured the artifact in front of me
(I wrote it, I can `cat` it) and not the case where it isn't there. Here I measured the lag of the fire
in front of me and not the day the fire never happens. **Both times: I instrumented the present object
and not its absence.** Absence is the case with no artifact to look at, which is exactly why it needs
to be asked about deliberately rather than noticed.

**AT ANDREW (card):** does the check need to survive seat-down — (a) session cron stands, or (b) an OS
Scheduled Task performs **Step 1, the READ, only**. **Step 2 recovery stays an AGENT act under either**
— (b) must not be read as automating the sign-in. **Default if silent = (a).** Not mine to decide.

## Actions taken on the ruling (this turn)
1. **Deliverable updated** — `STANDING_ORDER_0715_DAILY_BACKSTOP.md` gains **Step 2b** (the lag record
   line, explicitly not-a-monitor, n>=5 redesign bar) + the R2 softness note with the Andrew card.
   **This is the durable half** — given §0b is two-hop, the deliverable IS the procedure a successor reads.
2. **Cron re-armed carrying R1** — old `8b5d18cb` cancelled, new **`f9681e0c`** (`15 7 * * *`), body now
   opens with "note the CURRENT time" and closes with Step 2b + the R2 softness. A cron body that does
   not carry the ruling would have produced a compliant-looking fire with no lag line.
3. Lag record line for n=1 written above.
