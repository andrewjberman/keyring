# Lane ~MP delta: MP-x-4 is LIVE and drained; MP-r-2 STOPPED at step 2 on a load bar -- 0.7.0_AE_CloudOps~MP

**archetype:** SCRIBE

**Date:** 2026-10-09
**Task Orders:** `NFRA_MCPORTAL.TO-MP-x-4` COMPLETE (drained) | `NFRA_MCPORTAL.TO-MP-r-2` STOPPED at step 2
**Status:** IN PROGRESS (waiting on the issuer's re-cut)

---

## Why this file exists

The previous entry here says MP-x-4 is "PREPPED and HELD" with a live ledger entry and says both orders
are staged. Both statements are now wrong, and the corrections run in opposite directions: one order
shipped, the other hit a hard stop. A successor reading only the older entry would look for a held ledger
that is closed and would not know a WORLD-risk release is live.

## The two headlines

**MP-x-4 SHIPPED.** The Control Plane page is live: `opal-gateway` runs release `1e32562729` over
`c97232408d`, serving `GET /api/admin/fabric/boxes` (401 unauthenticated) and the mcportal `d60b4e0`
bundle. Ledger CLOSED, 4 legs proven, proof instance VALID, drained by the issuer @`a933da0d8a`. AC1 and
AC3 PASS; AC2 is `UNVERIFIABLE-BY-INSTRUMENT` (its mcportal clause cannot run from a linked worktree --
**run AC2 from the MAIN tree**). Rollback unexercised: `opal-gateway-c97232408d.tar.gz`, the VERSIONED
key, never `latest`.

**MP-r-2 STOPPED at step 2, as written.** `admin_fabric_overlap._compute(6)` read **31.611 s** against the
order's 30 s bar. Three cold samples: 31.611 / 24.508 / 22.333 s over 4,543-4,546 records. `gitstate`
(5.1 s worst) and `calls` (0.46 s worst) are far inside. Nothing opened, built, uploaded or deployed; no
handler tuned, because BOUNDS 1 says a load-condition failure stops the cell rather than tuning it. The
issuer re-cuts.

## The thing that matters most for whoever picks this up

**The load problem is not confined to the stopped cell.** `overlap` and the already-LIVE `admin_fabric`
read the same fabric activity store over the same rolling 6-hour window, at a comparable per-record cost,
and that window fills through the working day:

| time | handler | records | cold |
|---|---|---|---|
| 14:0xZ | admin_fabric | ~3,150 | 13.6-16.8 s |
| 15:5xZ | admin_fabric | ~3,790 | 18.1-24.4 s |
| 16:2xZ | admin_fabric (x4.AC3) | 4,040 | 24.2 s |
| ~17:xxZ | admin_fabric (issuer's re-run) | -- | 27.4 s |
| 18:3xZ | overlap | 4,543-4,546 | 22.3-31.6 s |

So `admin_fabric`, which is LIVE, crosses the same bar at about the same store size. Fixing only `overlap`
leaves the live handler just behind it. **No cold 2-hour figure exists for either handler** -- the only 2h
reading taken is cache-warm and is a lower bound, so the window-narrowing remedy needs its own
fresh-interpreter measurement before anyone leans on it. Rows `Z-S27` (the trend) and `Z-S30` (the stop).

Also worth knowing: the bar is breached only on the WORST of three samples -- 2 of 3 are under 30 s. A
single-sample gate had roughly two-in-three odds of passing and shipping a page whose first open can
exceed half the ALB idle timeout. Take three.

## Live state

| thing | where |
|---|---|
| MP-r-2 hookup (step 0) | `C:/tmp/mp-r2`, branch `wk-mcportal-cp2-r2` @`810e31b9ba`. **DO NOT REMOVE** |
| MP-r-2 release payload (step 1) | `C:/tmp/mp-r2-rel`, branch `rel-nfra-mcportal-cp2` @`74d2522f22`, plus an uncommitted `mcportal_commit=bc37107` edit. **DO NOT REMOVE** |
| MP-r-2 record (A4) | `deliverables/0.7.0_AE_CloudOps~MP/MP-r-2_PRE_ACT_RECORD.md` -- all figures and what the re-cut should expect |
| MP-x-4 record + proof | `deliverables/0.7.0_AE_CloudOps~MP/MP-x-4_PRE_ACT_RECORD.md` (both halves) and its proof instance |
| MP-x-4 build provenance | branch `rel-nfra-mcportal-r5-control-plane` (worktree retired; branch KEPT, as `rel-nfra-oplgtw-r29` is) |

**Retired this session, safely:** `wk-mcportal-r5-x4` and its worktree, after confirming the tip
`6ce50097c9` is contained in `box/sitez` with a discriminating control and both trees showed 0
uncommitted lines. Deleting a ref already in its trunk loses no commit and is not destructive git.

**No open deploy-ledger entry is held by this lane.** MP-x-4's is CLOSED; MP-r-2's was never opened.

## Three traps banked this session, all mechanical and all costly to rediscover

1. **A sparse no-cone list silently omits what the instruments read.** `deploy-to-ec2.sh` needs
   `data/transcripts/scripts/teams/meeting_allowlist.json` (OG-tl-1's new precondition, refuses pre-upload
   without it); `lib/opal_naming.py` needs `infra/logic/registry/`; `commit-gate` needs root
   `comp-constants.config.yaml`; `x4.AC2.sh` needs `mcportal` reachable, which a linked worktree cannot
   give it. The working list for a gateway release is `.tools/ org/ lib/ infra/ ops/ data/transcripts/`
   plus the root config files -- and AC2 still has to be graded from the main tree.
2. **A release base is an OLD tree.** Release branches chain from prior release commits, so their
   NON-gateway content is stale by design: the full test suite cannot run there (`org/devices/DEVICES.json`
   and others are absent). Run step-0 tests on the `box/sitez` worktree, which is where the issuer's own
   count came from.
3. **A trunk commit cannot always be cherry-picked onto a release base.** MP-s-1 and MP-k-1 also carry
   org/ bookkeeping the off-trunk base predates, so a cherry-pick conflicts `DU` on another seat's
   task-order file. Take the gateway paths with `git checkout <commit> -- <paths>` and verify each file's
   md5 against its source commit.

And one discipline worth repeating: **the surprise channel is shared, so read the next free row id at
WRITE time.** A peer took `Z-S26` mid-cell after I had already cited it in a manifest `release_note`;
`Z-S30` came in after max k had moved to 29.

## Compiler Tools

Recorded in each cell's own record and proof instance; not re-tabulated here and nothing was re-run to
fill a table. The reusable finding: `comp-iam gaps` inside a sparse worktree returns an all-zero sheet
against a `0 services scanned` denominator -- the zero and its denominator must be read together, or
"could not check" reads as "no gaps".

## Blockers

**MP-r-2 BLOCKED (evidence-cited), correctly:** step 2's load bar is breached and the re-cut is the
issuer's. This seat tunes nothing. The live base will also have moved again by then -- the gateway queue
is MX-r-9 -> MP-r-2 -> OG-rl-16, one release in flight.

## Next Steps

1. `[2.0.0_SA_COO~MP]` Re-cuts MP-r-2 on the load finding, and dispositions `Z-S27` / `Z-S30`. The four
   options and their measured costs are in the row's notes; none of them is an alarm, which is under
   moratorium.
2. `[0.7.0_AE_CloudOps~MP]` Event-driven. On the re-cut: re-read `deployed_commit`, re-cut the tree,
   re-run the census, and re-measure ALL THREE handlers -- expect the numbers to depend on the hour.
3. `[2.0.0_SA_COO~MP]` `Z-S28`: give `x4.AC2.sh` the `_main/mcportal` fallback `deploy-to-ec2.sh:40-44`
   already has, and drop the `2>/dev/null` that turns an absent repo into a `no`.
4. `[0.7.0_AE_CloudOps~DB2]` Still unowned from this morning: four untracked IRPT `.open_deploys/`
   sentinels (09-23 to 09-25) want an artifact measurement by their owner under NEVER-2.
