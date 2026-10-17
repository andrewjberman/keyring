# IRPT_ANLREQ round 56, workstream ~G (ENGINE) -- decomposition: the pricing as_of is the trading-calendar frontier (row S163)

Issuer `2.0.0_SA_COO~G2`, 2026-10-17.

**Input:** row `IRPT_ANLREQ-D2-S163`: the pricing `as_of` is a local weekday rule (`reports/resident_installed.py:379-385`, `_t_minus_1`: the UTC date minus one day, minus further days while Saturday or Sunday), not `lib/trading_calendar.py`'s frontier (`prev_trading_day(expected_last_trading_day(day))`); the two differ on weekends and holidays (Saturday: Friday against Thursday). The count (`deliverables/2.0.0_SA_COO~G2/ASOF_COUNT_20261017.md` @1b5b53cf80): 0 delivered reports carry a price as_of, 0 queued. CTO msg 10257 RULED: as_of is that module's frontier function, called, never a local weekday rule; on Saturday and Sunday it prints what the module returns (if Friday is believed right, the fix is in the module, for every reader, as a row); no served move today; it rides the next release that touches `resident_installed.py`, with a test pinning Saturday, Sunday, a holiday and the day after. The cell is built now so that release finds it merged; nothing is deployed by it.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **One worker cell.** `AR-g-161`: `_t_minus_1(epoch)` returns `tc.prev_trading_day(tc.expected_last_trading_day(<UTC date of epoch>)).isoformat()` (`import trading_calendar as tc` inside the function: `lib` is on the service's path since AR-g-159 / r34k, and the repository tests put `lib` on the path). Same name, same argument, same ISO string, so `_pricing_extras` is untouched.
- **The test that pinned the old rule moves.** `test_opal_pricing_binding.py::test_t_minus_1_skips_weekends` asserted 2027-01-15 for Sunday 2027-01-17 and for Monday 2027-01-18, which is Martin Luther King Day (a holiday, so the comment calling it "a Monday" missed it). It is replaced by the pinned cases: Saturday 01-16, Sunday 01-17 and the holiday Monday 01-18 give Thursday 01-14; the day after the holiday, Tuesday 01-19, gives Friday 01-15; an ordinary Wednesday 01-20 gives Tuesday 01-19. The other test in that file (`as_of == "2027-01-14"` for a Friday clock) is unchanged and still true.
- **The calendar's fallback covers 2010 to 2027** (`pandas_market_calendars` is absent on the host): a date outside it raises `CalendarCoverageError`; the pricing stage would raise at run time. Named in every packet; `lib/tests/gen_nyse_closures.py --write` before 2028.
- **Not in this cut:** a release. The next resident release that touches `resident_installed.py` carries it (CTO msg 10257).

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-161` | `_t_minus_1` on the calendar frontier; the weekday-rule test replaced by five pinned cases | `reports/resident_installed.py`, `reports/tests/test_opal_pricing_binding.py` | WORLD (the floor of an infra path; code and tests only, nothing deployed) |

## Edges and chains

- ONE chain, no dependency.

## Four-postulate record

(i) Domain: the pricing as_of. (ii) One grain: a date. (iii) One intent: one frontier, the calendar's. (iv) What this cut does NOT move: the tiers, the readers, `_pricing_extras`, every other member.

fanout: 1 of 1 chains, cap 8, reason: one worker cell.
