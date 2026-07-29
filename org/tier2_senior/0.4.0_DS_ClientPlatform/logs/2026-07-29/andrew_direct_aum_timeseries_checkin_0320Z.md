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

## CTO ruling (033205Z) -- all three answered, check-in CLOSED

1. **A2 RIDES the 15:00Z fire, no ad-hoc** (D2 evidence fire untouched; A2 chained in the
   legacy 15:10Z emit re-reads the fixed global and heals; key is fallback-only post-headline
   fix; legacy emission the teardown wave may retire). **STANDING CHECK ON ME: verify the
   served key's vintage after the 15:10Z emit, report EITHER WAY.** Baseline: ETag
   9a4559760d3658bd40f1d779fff1e2d4 @07-27T15:10:07Z; a heal must move the ETag AND restore
   the 31-date window.
2. **My 07-23 record was STALE: no 13:00Z smartx rule exists on the applied plane** (CTO
   measured: 3 smartx rules -- 16:00Z silver sweep / 11:30Z account-distribution ENABLED /
   14:00Z export-trigger DISABLED). The 11:30Z rule is routed to the teardown wave's writer
   census (COO gate 2). Nothing mine tonight. This paragraph is the correction of the 07-23
   log's "13:00Z clobber" premise -- do not carry 13:00Z forward.
3. **Queue complete as recorded**: G7 re-key cluster (Andrew-sighted, first) -> compose
   migration/splice removal + composed_backfill inheritance line -> 0318Z AGG work order.

Andrew's "aum-timeseries issues" full disposition (CTO): Global trend 1.91b = client-side
composition (DE lane, next promote, member #1); cottonwood trend frozen 07-22 = my G7 re-key
(post-fires); stale legacy A2 key = heals at 15:10Z. Every surface: mechanism + owner + window.

## My clock (live owner: this session)

- **~15:20Z 2026-07-29:** head-object json/portfolios/aum-timeseries.json; heal -> confirm
  to CTO; no-heal -> FINDING, immediately. Background timer armed in-session as backstop.
