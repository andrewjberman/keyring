# SELF-DRIVE cluster open calls -- tick 17 (2026-10-13 01:00Z, cron 9c76a283) -- state: ARMED

Arming record `ANDREW_DIRECT_20261012_125xZ_SELF_DRIVE_CLUSTER_OPEN_CALLS.md` @4698a8f59d. Ticks covered: 17. Last committed log:
tick 16 @9ee7ec7ad7 (00:0xZ). Substantive-delta log (one client-facing ruling between ticks).

## Measurements

- open rows: 16 (sitez 7, dell1 2, dell2 7, laptop 0), closed 92; fork 1 (sitez 1b36, the grant), act 15. dell2 closed 0eab
  on the tick-16 ruling. inbox: 0 unread. No unacked crossbox call to a laptop seat.
- CLIENT-FACING, open since 00:04Z: Inflection's performance page -- `DenyForeignFirmPrincipals` on `opal-data-inflection`
  refuses `irpt-performance-adapter-role` (measured by this seat at 00:4xZ and again at 01:00Z: the exception list admits
  `irpt-holdings-role`, Andrew's users, Opal_Terminal, `role/*-inf-*` and the two dell agent users, never the performance
  adapter's role, which has existed since 2026-09-10). The deny is latent from the 10-08 fence (last put 05:17Z by B1); dell2's
  IB-pr-487 deploy (22:35Z) only resumed the traffic. dell1 withdrew its attribution (ADDENDUM 11).

## Calls since the last log

- RULED by the driver (between ticks, relays 108708/108709): `CTO_RULING_INFLECTION_PERFORMANCE_DENY_OWNER_APPLIER_AND_PAIR_20261013.md`
  @af61c60689 -- owner ADVI_FIRMBKTS; fix = ONE exemptions.json row (that role, read-only, prefix
  `irpt/inflection/gold/holdings_performance_daily/`) + ONE bucket-policy safe-apply under a pair (CTO half `1.0.0_SA_CTO~DELL1`
  @354a12bc04, signed 00:49Z, "laptop applies"; COO half `2.0.0_SA_COO~B1`); applier `0.7.0_AE_CloudOps~FBL` on the laptop by
  B1's staged seat order (the FB-f-19 shape); read-back = one Inflection performance 200 and the deny events stopping; no
  rollback of IB-pr-487; no Andrew act. Andrew pushed one line (client-facing). At 01:00Z the policy is unchanged, no order has
  reached ~FBL (live, idle) and box/dell1 carries no COO half or exemption row since 00:49Z: the fix waits on B1; MSTR asked for
  the relay state and the clock (01:02Z); ruling section 3 names dell1's own CloudOps lane as the fallback applier.
- DESIGN FORKS at CRO research: 0. GOVERNANCE FORKS: 0 open.
- ACTS ONLY ANDREW CAN DO: 20 (tick-15 log), unchanged.

## Completion test

UNMEASURABLE (free-text scope); the loop ends on Andrew's stand-down word.

state: ARMED

## Compiler Tools

`python .tools/open-calls.py list --all --cloud`; `.tools/aws s3api get-bucket-policy` (one bucket); `.tools/aws lambda
get-function-configuration` / `iam get-role` (one resource each); `comp-iam roles`; `python .tools/crossbox-call.py list --open`;
`git log origin/box/dell1 --since`; `safe-commit.sh`.
