# IRPT_ANLREQ round 54, workstream ~G (ENGINE) -- decomposition: the door's yfinance checker reads the last finite close at the T-1 frontier (for r34j)

Issuer `2.0.0_SA_COO~G2`, 2026-10-17.

**Input:** IB2 rolled r34i back at 00:53Z: V1 green, V2S FAIL on SPY `NOT_KEPT LAST_CLOSE_NOT_FINITE` (22 rows) at 00:50Z on a Saturday. The code was byte-equal to r34h bar the bindings; the failing code is the door's checker, `intake/yfinance_check.py:226-237`, which reads the NEWEST Yahoo row and calls a null close NOT_KEPT, and has no cut at T-1. The price reader (`price_adapter_yfinance.py:39-44, 122-124, 117-120`) is sound: it drops non-finite closes and ends the window at `as_of`. r34h runs on the host. CTO msgs 10112 and 10122: r34j fixes the checker (drop non-finite closes; the last row at or before `lib/trading_calendar.py`'s frontier), with tests for a null newest row, a Saturday and a holiday; the V2 check follows it; the pricing `as_of` alignment is a separate pair.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **One cell, the checker only.** `AR-g-157`: `YfinanceChecker` takes `now=` (default the wall clock); `_check_one` takes the last FINITE close dated at or before `prev_trading_day(expected_last_trading_day(now))`; an only-non-finite history still reads NOT_KEPT `LAST_CLOSE_NOT_FINITE`, a last finite close of zero or less NOT_POSITIVE, rows only after the frontier NOT_KEPT `NO_ROWS`; a calendar error is a CHECK_FAILED, never NOT_KEPT. The V2 script needs no change: it runs the shipped checker.
- **The release is AR-g-156 (R53):** r34j carries AR-g-155 (merged), AR-g-157 and the bindings with the `ycharts` tier back.
- **Known limit (named):** the calendar's fallback covers 2010 to 2027 (`pandas_market_calendars` absent on the host); a date outside it raises, which the checker reads as CHECK_FAILED. It must be regenerated before 2028 (`lib/tests/gen_nyse_closures.py --write`).
- **Not in this cut:** moving the pricing `as_of` (`resident_installed.py:379-385`, a weekday rule: Saturday gives Friday, the calendar gives Thursday) onto the calendar frontier. It changes report as-of dates, a served move: its own pair with a count of the reports whose as_of changes (CTO msg 10122, row `IRPT_ANLREQ-D2-S163`).

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-157` | the checker's frontier rule and `now=`, with tests for a null newest row, a Saturday, a holiday, the run's own day, a null row on the frontier day, and rows only after the frontier | `intake/yfinance_check.py`, `intake/tests/test_yfinance_check.py` | WORLD (the floor of an infra path; code and tests only, nothing deployed) |

## Edges and chains

- ONE chain, no dependency; `AR-g-156` (R53) follows it.

## Four-postulate record

(i) Domain: one checker, one rule. (ii) One grain: a symbol's history. (iii) One intent: a symbol Yahoo holds is KEPT on its last finite close at the frontier. (iv) What this cut does NOT move: the cap, the pacing, `default_history`, the resolver, the pricing as_of, the price reader.

fanout: 1 of 1 chains, cap 8, reason: one worker cell.
