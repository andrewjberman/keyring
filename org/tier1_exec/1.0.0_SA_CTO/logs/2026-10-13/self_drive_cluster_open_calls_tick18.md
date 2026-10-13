# SELF-DRIVE cluster open calls -- tick 18 (2026-10-13 02:00Z, cron 9c76a283) -- state: ARMED

Arming record `ANDREW_DIRECT_20261012_125xZ_SELF_DRIVE_CLUSTER_OPEN_CALLS.md` @4698a8f59d. Ticks covered: 18. Last committed log:
tick 17 @e0c5ab1a58 (01:0xZ). Hourly-floor log carrying the Inflection resolution.

## Measurements

- open rows: 16 (sitez 7, dell1 2, dell2 7, laptop 0), closed 92; fork 1 (sitez 1b36, the grant), act 15. No new row since
  tick 16. inbox: 0 unread. No unacked crossbox call to a laptop seat.
- CLIENT-FACING Inflection performance deny -- RESOLVED. Timeline (UTC): failing from 00:04; cause measured on the bucket policy
  00:4x; ruled 00:5x (@af61c60689); B1's COO half + exemptions row merged @61cc536c29 and ORDER XB-2b72 (FB-f-21) delivered to
  `0.7.0_AE_CloudOps~FBL` 01:06; APPLIED 01:17-01:18 (commit 8fd299478c; AC1-3 PASS on simulate); the policy now admits
  `irpt-performance-adapter-role` under three scoped Denies (any other action; GetObject outside the prefix; ListBucket outside
  `irpt/inflection/gold/holdings_performance_daily/*`), read-only on one prefix as ruled; READ-BACK by dell2 `2.0.0_SA_COO~P2`
  01:31-01:33: handler 200, computed 191-point series (PERFORMANCE_PARTIAL is the adapter's own partial state), explicit-deny
  0 since 01:18 (6 before), AccessDenied 0 since 01:18 (18 before); forwarded to ~FBL (the broker refuses MSTR's Tier-2 write);
  the FB-f-21 ledger entry is CLOSED (absent from `.open_deploys/` at 02:00). Andrew pushed twice (failure, restored). Row S22:
  the order's `-target` key was wrong (`opal-data-inflection` vs `inflection`), which made its AC1 vacuous; ~FBL planned with the
  real key; a FIRMBKTS hygiene item for its issuer.

## Calls since the last log

- RULED by the driver: 0 new rows. The Inflection read-back reader was named (dell2 ~P2) and done.
- Site Z (108716): OG-ap-13 / sitez-ffaf DONE @c7d4d1f4f1 (dell agents' gateway/teams/bearer read removed, policy v5 of 5: the
  next applier on the laptop root prunes a version first; COO~C copied). OPEN at Andrew, routed by CTO~Z: whether "Dell boxes
  should not be curtailed" reaches ffaf; if yes, the revert is a restore of v4.
- DESIGN FORKS at CRO research: 0. GOVERNANCE FORKS: 0 open.
- ACTS ONLY ANDREW CAN DO: 20 (tick-15 log), unchanged.

## Completion test

UNMEASURABLE (free-text scope); the loop ends on Andrew's stand-down word.

state: ARMED

## Compiler Tools

`python .tools/open-calls.py list --all --cloud`; `check_inbox`; `.tools/aws s3api get-bucket-policy` (one bucket, polled once a
minute in the background until the role appeared); `ls -a org/critical_paths/.open_deploys/`; `safe-commit.sh`.
