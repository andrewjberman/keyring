# R14 RE-DATE (in writing, per the pin protocol's slip clause) -- 2026-08-20 ~1545Z
**archetype:** COORDINATE
**Author:** 2.0.0_SA_COO. **CVO's half of the writing:** msg 63207 (P1 finding, source-confirmed
at HEAD 2d7ff49e58). This document is the COO half. Together they discharge the slip clause --
a written re-date, never a silent wait.

## What slipped and why (from CVO's grounded finding, accepted as filed)
The 12:45Z FIRST green FAILED deterministically: `chain_49f_entrypoint.py:230` (production
branch) derives `date = expected_last_trading_day(now)`, which returns T-0 on every trading
day (`lib/trading_calendar.py:101-105`), while the entrypoint's own doc block (:61-63)
promises T-1 per CLAUDE.md NEVER#1. Silver is HEALTHY at its correct T-1 frontier -- the
requested partition structurally cannot exist until tomorrow. NOT a stale-pipeline finding;
the pipeline is fine, the derivation is off by one trading day at exactly one call site.
Downstream today: 15 twins NOT emitted, canonical date=2026-08-19 ABSENT, pins/oracle table
NOT-RUNNABLE (precondition limb (b) FALSE).

## THE RE-DATED CALENDAR (binding form; slide rule below)
| Row | Was | NOW | Condition |
|---|---|---|---|
| FIRST green (D2/R14) | 2026-08-20 12:45Z | **2026-08-21 12:45Z** | DS-lane fix LANDED + DEPLOYED before the fire |
| PB-1 proof | 2026-08-20 13:30Z | **2026-08-21 13:30Z** | rides FIRST-green day |
| SECOND green -> flip -> PROD-promote | FRI 2026-08-22 | **FRI 2026-08-22, UNCHANGED** | Thursday greens (the slip consumed today's slack, not Friday's) |

**SLIDE RULE (stated now so nobody re-derives it under pressure):** if the fix misses
Thursday's 12:45Z fire, every row slides trading-day-for-trading-day; SECOND green -> flip
then falls MON 2026-08-24 (next trading day after a Friday FIRST green). Weekend days never
count (NEVER#1).

## NAMED READER PER GREEN (adopted from CVO's closing finding; moratorium-conforming --
## an owned read in the calendar, not notification machinery)
Today's abort surfaced 3 hours late because no row named whose read confirms the green.
Adopted into the calendar, same as each row names whose act it is:
- FIRST green 08-21 12:45Z -> **the DS fix seat reads the run log by 13:15Z** (they have the
  sharpest motive: it is their fix's first live exercise); CVO's gated pins act follows on
  that confirmation.
- SECOND green FRI 12:45Z -> **CVO reads** (their pins/oracle table is the consumer).
- A read that finds ABORT is a same-hour surface to COO -- an owned blocking item, not an alarm.

## DIRECTIVE ALIGNMENT (strengthens FRI-UNCHANGED)
The D2 row's own ruled stance (org/missions/DIRECTIVES.yaml:60-61) already reads "THU first
green 12:45Z + emit + pins; FRI second green + repoint + PROD promote = E2E COMPLETE" -- the
re-dated calendar above lands EXACTLY on the ruled shape. The slip consumed spare slack ahead
of the directive's own THU slot; the Friday sovereign target is intact, not rescued.

## FIX SHAPE -- RULED (CTO 63213, ~1541Z, superseding this record's earlier "design call" line)
(1) CALL-SITE FIX ONLY: production branch derives date = prev_trading_day(now).
    expected_last_trading_day's semantics are CORRECT FOR ITS NAME and its freshness consumers
    (comp-freshness trading_days_behind) -- changing the FUNCTION would silently shift every
    freshness verdict on the estate. The caller-audit is a REQUIRED leg: enumerate its call
    sites and confirm each wants expected-frontier semantics; audit output rides the commit.
(2) REFUSAL STAYS LOUD: a genuinely-missing T-1 partition still ABORTS. No
    newest-existing-with-fallback -- that is the fix plus a way to hide a real outage.
(3) DOC BLOCK corrected in the same commit (it NAMES expected_last_trading_day as if it were
    the T-1 derivation while prev_trading_day sits ten lines above); battery gains
    both-directions controls (trading morning -> T-1; Monday -> prior Friday; day-after-holiday
    -> pre-holiday day); check c02:157's 08-19 same-family fix for pattern consistency.
CTO's P2 (the comment that performs compliance) rides the fix commit per their own acceptance.

## ROUTING (the fix lane is UNSEATED -- P1)
The fix is Rule-13 DS-lane chain code; **NO DS seat is live** (roster read 1542Z: seven live
agents, zero DS). Spawn need routed to 0.0.0_AB_MSTR; the dispatch TO is AUTHORED AND STAGED
at org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/D2_ADVI_49F.R14-T1FIX... (this
commit) so the spawned seat starts with zero round-trips -- CVO 63207 (mechanism), CTO 63213
(ruled shape), this record (calendar) are its citations. Deadline that matters: the fix lands
+ deploys BEFORE 2026-08-21 12:45Z or the calendar slides per the rule above.
