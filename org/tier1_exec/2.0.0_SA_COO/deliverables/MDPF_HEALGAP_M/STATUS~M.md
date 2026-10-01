# MDPF_HEALGAP cell 1 -- the Cottonwood gold catch-up step -- STATUS (2.0.0_SA_COO~M)

Overwritten each tick. Register: `org/projects/MDPF_HEALGAP.json` (no tree home, by ruling). Authority:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` batch 72 items 1-7 and batch 75
items 5-7. Trace: `org/tier1_exec/4.0.0_SA_CRO~X/deliverables/COTTONWOOD_ABSENT_POINT_TRACE_BRIEF_20261001.md`.

## Lease

FAST, armed 11:39Z until 19:39Z, seat `2.0.0_SA_COO~M`, surface: the module, its test and
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_M`. (The first arm, on the consolidator, was refused at 09:06Z
while MDPF_TAXSMA held all of `data/mdpf`; that lease is now on its claimed files, batch 75 item 6.) The consolidator's
one call line stays `4.0.0_SA_CRO`'s.

## Write claims

None open. The module and its test are landed; the next writes here are ledger legs.

## Pins

- Module `data/mdpf/scripts/gold/mdpf_gold_catchup.py` and test `data/mdpf/tests/test_mdpf_gold_catchup.py` (16 passed):
  on CLOUD (commits 524ee9beb1, 1124461a6c, 5082ed0513). Wired nowhere. Nothing is deployed, nothing is written.
- Half: `NEVER_WIDEN_HALF_REQUEST_HEALGAP_COTTONWOOD_CATCHUP_20261001.md`, BOTH halves signed (CTO @9fb81ec9f6), with
  addendum 1 (the sanity read; the figures in served terms).
- Ledger: `healgap-cottonwood-catchup-m-20261001`, open; leg P closed.
- Hand-off: `HOOKUP_HANDOFF_FOR_4.0.0_SA_CRO.md`, state READY TO WIRE.
- Row: `MDPF_HEALGAP-S1` (`org/surprise_channel/MDPF_HEALGAP/INVESTIGATION_v1.md` @e96bc4c4d8): the EC2 daily runner
  still launches at 13:30Z; the Lambda wrote the partitions read.

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

1. **Both halves are SIGNED** (CTO half @9fb81ec9f6). The CTO half's sanity read is done (the half's addendum 1): the
   fold equals the served file on 5 of 5 neighbour dates, and the five restored values in served terms are
   136,124,300.89; 139,107,569.53; 139,653,361.92; 175,667,910.62; 176,412,889.04, each between its neighbours or within
   0.82 percent of the nearer one.
2. **Ledger `healgap-cottonwood-catchup-m-20261001`: OPEN**, leg P closed (the five prior VersionIds; the sanity read).
3. **WAITING ON `4.0.0_SA_CRO`'s deploy:** its packet
   (`org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/4.0.0_SA_CRO/DEPLOY_PACKET_GOLD_HEALGAP_HOOKUP_20261001.md`
   @68e3b0d465) is at `1.0.0_SA_CTO` for signature; the act has not run and runs after MDPF_TAXSMA's own leg V2
   (the 13:50Z publisher run) and that signature (msg 103727). **The first daily run that carries the call line is
   2026-10-02 13:30Z** (the packet's leg V2). The packet's own "not measured" list, read 12:2xZ: a dry run of the
   deployed function read non-green at 11:58Z (the Global scope's coherence gate; likely a mid-window read, not
   established; its leg V1 re-runs it after 13:30Z), and the catch-up has never run on the Lambda runtime.
   Hand-off: `HOOKUP_HANDOFF_FOR_4.0.0_SA_CRO.md`.
4. Leg D1, the first 13:30Z run after that deploy: the manifest's `catchup` block reads five built, 0 failed; each of the
   five objects carries its value date; the older dates' earliest partitions are byte-unchanged.
5. Leg S: one trace per date to the served Cottonwood and Global points; 49 Financial and Inflection byte-unchanged.
6. Leg D2, the next day's run: `catchup` reads 0 planned.

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
