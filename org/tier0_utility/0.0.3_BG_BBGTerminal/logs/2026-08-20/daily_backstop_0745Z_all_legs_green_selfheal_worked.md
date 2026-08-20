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
