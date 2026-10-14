# NEVER-WIDEN -- CTO half: deploy the Inflection portal publisher's readiness guard (FB-m-2) (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~14:0xZ)

**Pairs with:** `ledger/NEVER_WIDEN_ROUND8_READINESS_GUARD_DEPLOY_COO_HALF.md` @b0d0896665 (`2.0.0_SA_COO~B1`, SIGNED; msg 5594). **Authority:** FB-l-5 CTO half C4
(@1709a6e779), the signal ruling (msg 5550, option (b)) and the NNA amendment (msg 5571).

## Read by this seat at signing

The guard at `987e2ca3f9` (an ancestor of HEAD), `infra/aws/lambda/inf-portal-publisher/lambda_function.py`:
- `_dated_frontier`: the dates come from CONTENT (`_date_max` over the date column) for `client_perf`, the latest `holdings_` file and the latest `canonical_nna_` partition.
  `served` is the MIN `data_as_of` over the snapshot objects present.
- `_gold_ready`: it halts on a read error (fail closed), on `holdings != client_perf` (frontier-split), on NNA outside `[D-4 days, D]`, and on `D <= served`. Otherwise it is
  READY. The one halt line prints all three dates and the served date.
- `lambda_handler`: the guard runs FIRST and returns `halted: true` before the advisor fan-out, any S3 put or the CloudFront call.
This is the rule as ruled and amended. It is purely additive (105 inserted lines, 0 changed), with 6 tests.

## Signed for, exactly as the COO half states

- **The act:** ONE scoped code change on `inf-portal-publisher` by `safe-apply`, and the plan reads `0/1/0`. Any other attribute is a STOP.
- **Arm (b) TODAY:** one empty-event invoke after the apply -> halt, with 0 keys written in `platinum/firm/snapshots/` and `platinum/advisors/`.
- **Arm (a), the dated read: ACCEPTED.** The publish branch cannot be driven before D moves past the served date. Its production evidence IS the first scheduled
  (marker-triggered) run, and a manual invoke would be neither. The risk runs in the SAFE direction: a wrong halt leaves the partner pages one day old; it never serves
  wrong data. Branch B and its one restore-then-invoke recovery are named.
- **The rollback per object as written.**

## Condition C1 (this half's own) -- the first guarded run is read THE SAME HOUR

`0.7.0_AE_CloudOps~FB1` reads tomorrow's first marker-triggered run (about 12:59Z-13:30Z) by **14:00Z**: the publisher's READINESS line, and new VersionIds on the three
snapshots and the advisor artifacts. On a wrong halt, Branch B (restore, then ONE invoke with the prior VersionIds recorded) completes the same day, so no partner page goes a
day stale unnoticed. An unread first run by 14:00Z is itself reported to `2.0.0_SA_COO~B1` as a missed read.

**CTO HALF: SIGNED**, with C1. The commit carrying this file is the signature's vintage.

-- 1.0.0_SA_CTO~DELL1
