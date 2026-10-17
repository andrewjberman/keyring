# Andrew-direct 2026-10-17 ~03:1xZ (2026-10-16 ~23:1x ET): backfill every rivalfunds security 365 days, now, at full budget

**Recorded by:** `2.0.0_SA_COO~RV`, same turn. **Channel:** the dell1 terminal session (this seat's launch session).

## VERBATIM

> I want you to check out the securities in the rivalfunds and backfill all securities in there back 365 days right now

(after this seat reported the site-Z drawer's enforced history ceiling of 5,858 cells a day, non-trading days only:)

> Thats bullshit we can use a lot more than that

(next message, same session:)

> override like 2m cells right now

(~04:2xZ, after this seat reported batch rv-bf365-20261017 landed -- owed 180,991 -> 12,480 -- and that the queued TR-HELD
D30/D90/D365 and DIVIDENDS requests and the 12,480 remaining closes stay unfilled:)

> Yeah I want all those completely filled

## What it is measured against (read by this seat, 03:1xZ)

- Owed set, `data/etfs/scripts/rivalfunds/history_owed.py owed(s3, page_day=2026-10-19)`, read-only on live S3:
  **746 securities, 180,991 (security, trading day) units, 250 dates, 2025-10-20 .. 2026-10-16** (claim: measured).
- Andrew-direct 2026-10-16 ~15:5xZ (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261016_155xZ_BBG_DAILY_BUDGET_2_5M_AND_TERMINAL_AGENT_MAY_DOWNLOAD.md`):
  surface C (rival funds history) = 400,000 cells a day of a 2,500,000 daily budget. 180,991 < 400,000.
- Already filed in the queue: `org/missions/D8/MDPF/MDPF_DEMQUE/requests/ETFS_RIVALS-C1-*` (seven requests, 2.0.0_SA_COO~Q1),
  quoted at the 5,858 measured floor, non-trading days only, finish dates 2026-11-15 .. 2027-02-28.
- Standing request `ETFS_RIVALS-HISTORY-OWED-DAILY` state: `paused` since 2026-10-09T09:38:33Z ("act 3 held, CTO msg 1640").
- dell1 has no Terminal (no listener on 8194). The pull runs on site Z.

## Scope as given

All securities of the rivalfunds funds, 365 days back, now; the drawer's history ceiling overridden to about 2,000,000 cells
right now (his "override like 2m cells"). This overrides the ramp ruling `MDPF_DEMQUE/ledger/CTO_RULING_HISTORY_CEILING_RAMP_20261015.md`
for this draw and the trading-day-zero backfill allowance. The seat does not narrow it and does not widen it: the rivalfunds
backfill (180,991 cells) is the act ordered; whether the rest of the 2M override serves other queued requests is relayed to the
site-Z owner verbatim, not adjudicated here.
