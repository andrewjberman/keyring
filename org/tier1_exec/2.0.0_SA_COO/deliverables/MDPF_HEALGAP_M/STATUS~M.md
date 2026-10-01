# MDPF_HEALGAP cell 1 -- the Cottonwood gold catch-up step -- STATUS (2.0.0_SA_COO~M)

Overwritten each tick. Register: `org/projects/MDPF_HEALGAP.json` (no tree home, by ruling). Authority:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` batch 72 items 1-7 and batch 75
items 5-7. Trace: `org/tier1_exec/4.0.0_SA_CRO~X/deliverables/COTTONWOOD_ABSENT_POINT_TRACE_BRIEF_20261001.md`.

## Lease

NOT ARMED. `drive-mode.py arm MDPF_HEALGAP --surface data/mdpf/scripts/gold/mdpf_gold_consolidator.py` was REFUSED at
09:06Z: the live FAST lease MDPF_TAXSMA (seat `4.0.0_SA_CRO`) holds all of `data/mdpf`. Ruled (batch 75 items 5-6): the
catch-up is a NEW module built in this seat's worktree; `4.0.0_SA_CRO` re-arms MDPF_TAXSMA on its claimed files; the
consolidator's one call line is added by that seat at its next merge.

## Pins

- Module `data/mdpf/scripts/gold/mdpf_gold_catchup.py` and test `data/mdpf/tests/test_mdpf_gold_catchup.py` (16 passed):
  on CLOUD (commits 524ee9beb1, 1124461a6c, 5082ed0513). Wired nowhere. Nothing is deployed, nothing is written.
- Half: `NEVER_WIDEN_HALF_REQUEST_HEALGAP_COTTONWOOD_CATCHUP_20261001.md`, COO half signed; the CTO half is owed.
- Hand-off: `HOOKUP_HANDOFF_FOR_4.0.0_SA_CRO.md` (the call line and the Lambda package row; both held until the half
  carries two signatures).

## Live thread

Not wired. The step's one real run so far is read-only: against live silver with `upload` off it plans exactly five
builds and each dry run returns rc 0 and RECONCILE PASS (QA run 11:16Z-11:23Z).

## What the live plan read (53 gold partitions, 78 holdings dates on the axis, 44 valued by no partition)

| outcome | dates |
|---|---|
| built (dry run) | 08-18, 08-20, 08-21, 09-23, 09-24 -- Opal totals 142,434,495.60; 145,708,847.84; 146,275,792.27; 197,132,575.38; 198,026,295.50 |
| skipped, no assignment partition for the next trading day | 34 (June 15, July 12, 08-31, September 6) |
| skipped, no partition to rewrite (the step never mints one) | 07-28, 07-29, 07-30 |
| skipped, would restate an older date | 08-04, 08-12 |

## Next, in order

1. The CTO's half on the five-object act.
2. `4.0.0_SA_CRO` adds the call line and the package row and deploys `mdpf-gold-lambda` (its lease, its ledger).
3. Ledger `healgap-cottonwood-catchup-m-20261001`, opened before that deploy with the five prior VersionIds.
4. The first daily run after the deploy: the `catchup` block reads five built; one trace per date to the served point;
   the second daily run reads 0 planned.

## Parked

| Question | Owner | Un-parks when |
|---|---|---|
| The seven days with no assignment partition stay absent (ruling item 4) | Andrew (a Rebalancer re-pull is a vendor call) | his per-use word |
| 07-28, 07-29, 07-30: buildable, but each would mint a gold partition in the backfill's range | `1.0.0_SA_CTO` | it rules them in or out |
| 08-04 and 08-12: valued by no partition; how they read on the served series is unmeasured | `2.0.0_SA_COO~M` | the first trace of acceptance reads the series |
| MDPF_TAXSMA's lease surface is the whole directory | `4.0.0_SA_CRO` | it re-arms on its claimed files (batch 75 item 6) |
| Whether the EC2 nightly (`mdpf-daily-dispatch.sh:554`) still fires; the instance reads stopped | `0.7.0_AE_CloudOps` (dark) | an AE seat is live |

## Limits

The five figures are the builder's dry-run totals, not served values. The Holdings and S3 reads of this session ran on
a connection that timed out once inside a build (10:33Z); the step now records such an error instead of raising.
