# Rivalfunds: 365 days of history per security and per fund -- what manages it today, and what is missing

**From:** 4.0.0_SA_CRO~Z. **For:** 1.0.0_SA_CTO~Z, to place in ETFS_RIVALS with 2.0.0_SA_COO~RV.
**On:** Andrew-direct ~20:4xZ, record
`ANDREW_DIRECT_20261007_204xZ_RIVALFUNDS_365D_BACKFILL_PER_SECURITY_AND_FUND_IN_THE_INGESTION_SEQUENCE.md` (beside this file).
**Measured:** 2026-10-07 ~20:5xZ, read-only, on live S3 (`s3://opal-data-etfs/rivalfunds/etfs/gold/`) and the code at
site-Z HEAD. No Bloomberg call, no write.

## The answer to "what are we doing to manage that process at this time?"

**Nothing in the ingestion sequence manages it. One ad hoc act is planned, and after it the gap re-opens by itself.**

1. **Holdings history per fund is largely there.** 506 daily partitions back to 2024-09-30.
2. **Price history per security is not there yet.** The market table holds 5 trading days of closes (2026-09-29 to
   2026-10-06). The year of closes Andrew authorised this morning has not landed: it is step 4 of the project's order
   of acts, a one-time run by `2.0.0_SA_COO~RV` over two or more days.
3. **No step gives a newly appearing security its prior 365 days.** The daily pull asks Bloomberg only for the
   securities held on that day. The backfill tool is described in its own code as "AD HOC ... never scheduled".
4. **The backfill tool cannot do that job even if it were scheduled.** It skips any DATE that already holds a price
   object, whatever securities are in it. Once the one-time backfill and the daily pulls have covered a date, a later
   run for a new security plans zero days and asks for nothing.

## 1. What the store holds today

Window: 2025-10-06 to 2026-10-06, 252 NYSE trading days (`lib/trading_calendar`).

| Table | Date partitions | First | Last |
|---|---|---|---|
| `canonical_shape` (holdings, G1) | 506 | 2024-09-30 | 2026-10-06 |
| `trade_schedule` (the transactions record, G5) | 505 | 2024-10-01 | 2026-10-06 |
| `security_market` (closes, G4) | **5** | 2026-09-29 | 2026-10-06 |
| `security_universe` | 3 | 2026-10-02 | 2026-10-06 |
| `corporate_actions` (G3) | 5 | 2026-09-30 | 2026-10-06 |

**Holdings report dates per fund in the window (of 252):**

| Fund | Report dates | First in window |
|---|---|---|
| WCMG | 95 | 2026-04-23 |
| PFOE | 190 | 2026-01-02 |
| IDVZ | 191 | 2026-01-02 |
| ETFT | 210 | 2025-12-02 |
| PCLG | 230 | 2025-10-16 |
| BIDD, CGIC, TSEL | 244, 245, 245 | 2025-10-06 to 2025-10-09 |
| GQGU, SCHY, INEQ | 250, 250, 251 | 2025-10-06 |
| BASG, TXUE | 252, 252 | 2025-10-06 |

Nine of 13 funds have 244 or more of 252. For the four short ones I did not check launch dates, so a short count may
be a young fund and not a hole.

**Closes per security in the window.** 761 securities appear in at least one fund's reports in the window. Days with a
positive close, as a share of 252:

| No close at all | Under 25% of days | 25% or more |
|---|---|---|
| 206 | 555 | 0 |

All 2,966 stored price rows are marked `pull` (the daily leg). None is marked `backfill`.

**The case Andrew describes, measured.** A security that enters a fund after that fund's first stored report is an
observed entry. There are **355** such (fund, security) entries in the window. For the days of the window BEFORE the
entry:

| No close on any pre-entry day | Some | Half or more |
|---|---|---|
| 354 | 1 | 0 |

What the page draws for those days today is a price implied from holdings (`price_series.py`: market value over
quantity, from whichever tracked fund reported the security that day). That exists only on days some tracked fund held
it, and only for a listing stored as USD. So a new buy has a curve only from the day it was bought.

## 2. Why the gap re-opens after the planned backfill (code read)

| Mechanism | Where | Effect |
|---|---|---|
| The daily leg's security list is G1 at `date=<D>` | `enrichment_bloomberg.py:15`, `:501-529` | A security gets a close only on days it is held. The day after a fund sells out, its closes stop, and its 365d curve loses a day at the far end every day |
| The range backfill is hand-run | `enrichment_bloomberg.py:63-64` ("AD HOC ... never scheduled, run by the issuer") | Nothing fires it when the transactions record shows a new security |
| The range backfill's "already held" test is per DATE | `enrichment_bloomberg.py:723-730` (`_held_dates`), `:804-805`, `:811` | `todo` drops every date that has any `market-*.parquet`. After the one-time run, every date has one. A new security then plans `securities x 0 days` |
| It never overwrites a date object | docstring `:70` | Correct for integrity, and it is what makes the per-date test final |
| A new tracked fund's holdings history is the collector's `backfill` mode, also hand-run | `collector_bloomberg.py` docstring | Onboarding a fund is two hand-run acts (holdings, then closes) |

The STATUS file's plan already widens the one-time list to "formerly-held keys" (CTO ruling msg 30817), which covers
exited names once. It does not cover a name that enters, or keeps exiting names topped up, after that run.

## 3. What "built into the ingestion sequence" needs (recommendation; the design is the CTO's)

Four parts. The first three are small; the fourth is the one structural change.

1. **A "history owed" step in the daily sequence, with no vendor call.** After the transactions record and the
   security universe are built: for every security any tracked fund held in the last 365 days, list the trading days
   in [as-of minus 365d, as-of] with no stored close. The inputs exist: `security_universe` carries `first_seen`,
   `last_seen` and `funds` per security. Its output is a plan with a printed denominator, the same shape the range
   backfill already prints.
2. **A scheduled leg that spends the plan,** on the terminal machine after the 11:00Z vehicle, inside `bbg_budget`,
   capped per day, with what is left carried to the next day. A new security is then whole within a day or two of
   its first trade, with no one remembering to run anything.
3. **The daily list widens from "held today" to "held within 365 days".** Exited names keep their curve current.
4. **The stored grain changes from per date to per (security, date).** Today one object per date is final. The owed
   test has to ask "does this security have a close on this day", and a later top-up has to be able to land for a date
   that already holds an object, without overwriting it. One way that keeps never-overwrite: a top-up lands as its own
   object in the date's partition. That only works if every reader of the table takes all objects of a date; the
   table already has 8 objects over 5 dates, and I did not check each reader.

**New fund.** With parts 1 to 4, adding a fund needs no second act for closes: its securities enter the universe and
become owed. Its HOLDINGS history is still the collector's hand-run backfill, and that is the costly part.

## 4. Size against the Bloomberg budget

`bbg_budget.json`: ceiling 150,000 rows a day, production reserve 30,000, so 120,000 a day for anything non-production.

| Load | Points | Against 120,000 a day |
|---|---|---|
| One-time: 761 securities x 252 days | 191,772 | two days |
| A new security | 252 each | 355 entries in the last year is about 1.4 a trading day, about 355 points a day |
| Keeping exited names current | 1 a day each | about 200 names, about 200 points a day |

Steady state is under 1% of the daily allowance. The one-time load is the only heavy part, and it is already planned.
The points-versus-rows unit question on the budget is open (rows Z-S67, Z-S68); these figures are points requested.

A holdings backfill is a different order of size: the budget file estimates 2,198 rows per fund-date for a broad fund
(ACWI) and 150 by default, and the 2026-10-05 incident it records was about 175,000 rows of holdings backfill
exhausting the Terminal's day.

## 5. Calls that are not this seat's

1. **Which reading of "per tracked fund".** (a) Each fund's holdings history reaches 365 days: largely met, four
   funds short. (b) 365 days per (fund, security) from that fund's first trade: closes are per security, so this is
   met by the security-level store once it is complete. (c) The fund's own share-price series: not examined here.
2. **Whether Andrew's ~20:4xZ message is his word for a STANDING scheduled Bloomberg pull.** His ~05:1xZ word covered
   an ad hoc backfill for the rivalfunds funds. Widening the daily list (part 3) changes a scheduled production
   request, and part 2 adds a scheduled one.
3. **Round placement.** Parts 1 to 3 are additions; part 4 changes a stored contract and its readers, and it should be
   decided before the one-time backfill writes a year of per-date objects that a later top-up cannot add to.
   That ordering point is the one time-sensitive item here.
4. **The four short funds:** young funds or holes. One read of launch dates settles it.

## What bounds this

- The census read the newest `canonical_shape` object of each of 252 date partitions and every `security_market`
  object. Securities are counted by `security_bloomberg`; a row with no Bloomberg id is not counted, so 761 and 355
  are floors.
- "Observed entry" means first seen after the fund's first stored report in the window. A security that left and
  came back counts once, at its first appearance.
- The project's STATUS file sizes the backfill's currency lookup at 282 keys. I did not reconcile that with 761; the
  planned list may be narrower than "every security in the window".
- I read the code paths named above, not every reader of `security_market`.
- The scheduled-leg mechanics (the vehicle's `.cmd`, the leg gates) were not opened.
