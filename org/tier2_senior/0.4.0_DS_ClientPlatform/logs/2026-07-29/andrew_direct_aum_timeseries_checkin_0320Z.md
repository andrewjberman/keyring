# ANDREW-DIRECT record + aum-timeseries check-in (2026-07-29 ~0320Z)

**archetype:** COORDINATE

## Andrew-direct, VERBATIM (DS terminal, ~0320Z 2026-07-29)

> "Are you sure about that? I am pretty sure we needed you to address the aum-timeseries
> issues, check in with CTO and make sure there is nothing you need to be addressing"

Context: delivered at my terminal immediately after my session-start standby summary.
Recorded per org/XXX.md "Andrew-direct instructions -- RECORD + BROADCAST, same turn."
Broadcast: CTO (check-in message, same turn), COO + MSTR (record broadcast, same turn).
Scope: NOT adjudicated by me -- surfaced verbatim.

## Grounded state at check-in (measured this turn)

- Served `opal-data-portal-v2/json/portfolios/aum-timeseries.json`:
  ETag 9a4559760d3658bd40f1d779fff1e2d4, LastModified 2026-07-27T15:10:07Z, 295,300 bytes.
  That vintage PRE-DATES the Option-1 compose fix (deployed @e56eef609e, 0027Z 07-29) and
  the post-fix trio (00:30-00:33Z run mdpf_daily_20260728_003007). A2's producer
  (`dim_mdpf_aum_timeseries.py`) reads ONLY the global aggregate -- so the served A2 key
  still carries the pre-fix window (the 31 moved historical dates) until A2 re-runs against
  the restored global.
- Trio scope (per AE 004016Z) = global gold artifact + its two downstream copies; A2 was
  NOT part of it.
- Served `json/portfolios/aum-metrics.json` = 9bae4b42 (07-23, the UNMOVED control oracle
  cited in the portal pointer-bump commit) -- expected.
- Flag #3 (smartx-Lambda 13:00Z clobber of the three portfolios/ keys) status UNKNOWN to me
  as of this check-in -- last record (07-23 log) has it HELD pending P1 close; asked CTO.

## Asked of CTO (same turn)

1. Is A2 re-emission against the fixed global mine to execute now, or does it ride the
   15:00Z scheduled fire (production-path law: scheduled run is the production path)?
2. Flag #3 / 13:00Z clobber status -- if not flipped, today's 13:00Z could overwrite the
   portfolios keys ahead of the 15:00Z chain.
3. Anything else on me before the fires beyond the recorded post-fires queue (G7 re-key
   cluster + compose migration + composed_backfill inheritance line + AGG work order).
