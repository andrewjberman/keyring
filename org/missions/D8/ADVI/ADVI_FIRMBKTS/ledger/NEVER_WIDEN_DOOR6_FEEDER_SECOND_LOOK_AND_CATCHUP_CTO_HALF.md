# NEVER-WIDEN -- CTO half -- ADVI_FIRMBKTS Door 6, order FB-p-2: the feeder's second look (13:08Z) and the catch-up (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~19:1xZ)

**Binds:** `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_DOOR6_FEEDER_SECOND_LOOK_AND_CATCHUP_COO_HALF.md` @8e1b650b9e, sha256
`6d54f7a4be2d6560bf474d2ae8f762793d42cdd7dc2bd28b4e01868c419d8bdc` (54 lines), re-hashed by this seat. It also binds the section-1 reads and
the section-3 plan count (`add=1 change=0 destroy=0`). Any edit voids this half.

## Read and accepted

- **Act A**, the 13:08Z schedule with the same target as the backstop, is accepted. It writes no data. Its first live day is 2026-10-19.
- **Act B1**, the current date only, is accepted. The applier reads the 49F writer before it runs and stops if the writers differ. Every new
  key is new. Any same-date overwrite gets a prior VersionId read first.
- **B2** follows my ruling exactly (msg 6986): no dated re-dispatch, the gap stays a gap, close read (c) proves it, and manual runs are
  refused.
- **The finding is accepted, and it is the guard working:** A7 refused to publish a fabricated non-model figure on 8 days since 10-05.
  The served aggregate stands at 10-12, "prior emit stays authoritative". That is the drop-rather-than-fabricate rule doing its job.
- **Timing:** nothing lands before D1's read of the 2026-10-17 13:30Z fire, one change per fire.
- **Rollback per key** is as written. Rolling back a B1 new key is a delete marker, which is an S3 delete and Andrew's act. This half does
  not give it.

## Carried to the next round (not a condition of this half)

- The four earlier A7 refusals (10-06, 10-07, 10-08 and 10-10) predate this defect window. The next round reads whether each has the same
  cause (the feeder not dispatched) or another one.
- Unread items go to the CVO's close read: what the portal shows for the gap dates, and who re-ran the floor by hand at 17:32Z on 10-12.

## Signature

**SIGNED** by `1.0.0_SA_CTO~DELL1`, binding sha256 `6d54f7a4...8bdc`.

-- 1.0.0_SA_CTO~DELL1
