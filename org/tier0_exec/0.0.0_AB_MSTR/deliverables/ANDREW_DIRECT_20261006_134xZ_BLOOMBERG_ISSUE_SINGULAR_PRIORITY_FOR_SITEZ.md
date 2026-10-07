# ANDREW-DIRECT 2026-10-06 ~13:4xZ -- the Bloomberg issue is the singular priority for site Z

Given at the `0.0.0_AB_MSTR~Z` terminal (site Z).

## Context

At ~13:20Z Yang Liu asked Andrew in Teams to "take a look at the index benchmark return". His screenshot is the portal's
Benchmark Comparison panel (Index, Gross, as of 2026-10-05 5:00p ET, source Bloomberg). Every model's index BENCHMARK
row reads N/A at 1D, WTD, MTD and QTD. Yang says the ETF view is not affected. Andrew assigned the trace to
`4.0.0_SA_CRO~Z` and the briefing to `1.0.0_SA_CTO~Z`. The leading lead, unverified, is OPAL_BBGTML-Z-S5 @952f3c8a00:
7 of 13 custom CIX series (.INT_BMK .LT_BMK .ST_BMK .UST_BMK .LT_ETF .ST_ETF .UST_ETF) stop at 2026-09-29.

## Verbatim

Andrew: "Bloomberg issue is singular priority for the box. until that is fixed no other projects matter."

## Scope as read (surfaced, not adjudicated)

- "The box" is site Z: every seat on this device's fabric.
- "The Bloomberg issue" is read as the index-benchmark return problem above (the frozen CIX series and whatever froze
  them). Whether it also covers the sign-in fallback defects (OPAL_BBGTML-Z-S2/S3/S4) is asked of Andrew, not assumed.
- "No other projects matter" is relayed verbatim to each seat. It is not converted into a stop order on any running act:
  each seat's owner applies it to its own work.
- The fix likely touches `integrations/bloomberg/`, which is under Andrew's no-modify order. This word does not by itself
  lift that order; the route is asked of Andrew.
