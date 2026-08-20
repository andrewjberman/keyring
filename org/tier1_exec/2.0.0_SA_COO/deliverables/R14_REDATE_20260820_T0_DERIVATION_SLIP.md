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

## ⛔ CORRECTED ~1552Z (CTO 63236/63238, verified INDEPENDENTLY at three seats incl. mine:
## python weekday 08-20=THURSDAY, 08-21=FRI, 08-22=SATURDAY, 08-24=MON; CVO's partition-triple
## and git-header proofs concur). THE ORIGINAL TABLE BELOW CARRIED WEEKDAY LABELS OFF BY ONE,
## AND ITS CENTRAL CLAIM INVERTED: "FRI 08-22 promote UNCHANGED" named a SATURDAY, so the
## sovereign Friday target was NOT preserved as written -- the ruled THU-first slot is the one
## that fired and failed TODAY (Thursday). Original table preserved struck for provenance;
## the CORRECTED CALENDAR + FORK below binds.

~~| FIRST green | 08-20 -> 08-21 ("THU") | PB-1 rides | SECOND green -> flip "FRI 08-22 UNCHANGED" |~~

## THE CORRECTED CALENDAR (binding)
| Row | Instant | Day | Condition |
|---|---|---|---|
| FIRST green (D2/R14) | 2026-08-21 12:45Z | **FRIDAY** | DS-lane fix LANDED + DEPLOYED before the fire (instant unchanged from the first cut -- only the day-name moved) |
| PB-1 proof | 2026-08-21 13:30Z | FRIDAY | rides FIRST-green day |
| END-GAME | **FORKED -- see below** | | |

**THE FORK -- RESOLVED ~1553Z: ANDREW RULED (a), VERBATIM "Better do do it now (a)"
(at the MSTR terminal; record ANDREW_DIRECT_20260820_D2_PROMOTE_SINGLE_GREEN_FRIDAY_A.md +
the DIRECTIVES.yaml D2 stance refresh, MSTR-pushed).**
- **OPERATIVE (a): SINGLE-GREEN FRIDAY** -- FIRST green FRI 08-21 12:45Z -> flip -> PROD
  promote SAME DAY on ONE green. Named readers stand: DS reads FRI's log by 13:15Z (abort =
  same-hour surface); CVO's pin act + flip verification compress into the same day (CVO
  pre-staging the pin-file mechanics so compression costs nothing). Miss Friday's fire ->
  the MON 08-24 slide stands.
- **SCOPE, surfaced not adjudicated (MSTR's relay carries it): a THIS-RUN compression of
  the two-green discipline on his word -- NO PRECEDENT for the next promote.**
- (c) two-green default: SUPERSEDED by his word on arrival, as this record pre-committed.
  (b) Saturday-promote: rejected, unchanged.

**SLIDE RULE (corrected):** miss FRIDAY's 12:45Z fire and every row slides
trading-day-for-trading-day from there; weekends never count (NEVER#1).

## NAMED READER PER GREEN (adopted from CVO's closing finding; moratorium-conforming --
## an owned read in the calendar, not notification machinery)
Today's abort surfaced 3 hours late because no row named whose read confirms the green.
Adopted into the calendar, same as each row names whose act it is:
- FIRST green 08-21 12:45Z -> **the DS fix seat reads the run log by 13:15Z** (they have the
  sharpest motive: it is their fix's first live exercise); CVO's gated pins act follows on
  that confirmation.
- SECOND green FRI 12:45Z -> **CVO reads** (their pins/oracle table is the consumer).
- A read that finds ABORT is a same-hour surface to COO -- an owned blocking item, not an alarm.

## DIRECTIVE ALIGNMENT -- ⛔ CORRECTED ~1552Z: THE ORIGINAL READ OF THIS SECTION WAS THE
## ERROR'S MECHANISM. The D2 stance's "THU first green" names TODAY (08-20 IS Thursday) --
## the ruled THU slot is the one that fired and failed at 12:45Z. The original text below
## claimed alignment by shifting every label one day late; preserved struck for provenance.
~~The re-dated calendar lands EXACTLY on the ruled shape... the Friday sovereign target is
intact, not rescued.~~
TRUE STATE: the slip broke the ruled THU-first/FRI-second shape on its first row. The
directive's FRI-promote target survives ONLY via fork option (a), which is Andrew's word.

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
