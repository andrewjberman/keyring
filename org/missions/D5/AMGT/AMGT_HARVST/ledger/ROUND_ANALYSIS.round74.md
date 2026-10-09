# AMGT_HARVST -- ROUNDS 73 AND 74, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~02:0xZ)

**Inputs:** `deliverables/2.0.0_SA_COO_H/round74/DRAIN_END_ROUNDS_73_74.md` @e25bf67559 (site Z's last issuer, `2.0.0_SA_COO~H`), read whole.
Rounds 73 and 74 are closed, 5 of 5 orders terminal. The packet went to `1.0.0_SA_CTO~Z` (msg 32112) before the move, and no analysis
followed. This seat writes it as the project's CTO since the dell1 re-placement (@a4bcfa869f; Andrew-direct 2026-10-08 ~22:5xZ).
Issuer from now on: `2.0.0_SA_COO~W1`.

## Placements (the packet's four items)

1. **FWD-18 activation vs the `bq-2` merge hold. RULED: the hold reads "not merged while a leg runs FROM THE TREE BEING MERGED INTO".**
   The runner runs from a PINNED checkout at site Z, so a merge cannot reach a running leg, and the hold as first written would never
   lift. Two conditions bind: (a) the runner's pin moves only by an explicit re-pin, never by box-sync; (b) the runner is a site-Z
   producer (census @6a308cd424), so `bq-2`'s merge into a producer path is a site-Z deploy under a never-widen pair carrying
   `1.0.0_SA_CTO~Z`'s half before the merge (msg 1267). W1 amends section 86 accordingly and states which gate limb graded it.
2. **The Seeking Alpha overlap. RULED: activate the runner on bbg, wsj and barrons now; add `sa` only when the r47 backfill ends.**
   The backfill is Andrew's (2026-10-06, depth to 2026-01-01) and runs in site Z's `~H` session (msg 1304). Ending it is not this
   fabric's call. Asking Seeking Alpha twice at once is the hazard. The `sa` cycle joins on site Z's report that run 3 has ended.
3. **Merge order. RULED as R26 states:** rebuild #11 first (AIG and both OMAB lines, ten titles each, to the CVO, under its list-move
   pair), then gold `br-1`, then acceptance `bq-2`, each under its own pair. Rebuild #11 is round 75's first cell.
4. **Next enrichment. RULED:** FWD-18 hop 3, the page that says when a publisher did not run, is cut once cycle records exist from the
   activated runner (item 2). Not before: a page with no records to read cannot be graded.

## Also placed

- The `bo-1`/`bp-1` merge pair is complete and waits only on site Z reading C-a. It is a site-Z read and is not re-cut here.
- Seeking Alpha staleness on DSGN_AMGTV1's walk (Lenovo 992 HK, last read 2026-09-22; DSGN round-55 analysis R2) arrives as a row from
  `2.0.0_SA_COO~D1`. Placed with item 2: the backfill and the runner's `sa` cycle are where it heals.

## ENRICHMENT LIST, round 75 (ONE issuance by `2.0.0_SA_COO~W1`)

1. Rebuild #11 under R28 (AIG, OMAB lines; list-move pair).
2. Runner activation on bbg, wsj and barrons (item 2), on site Z's pinned checkout, by order to site Z's producer seat.
3. The section-86 amendment for `bq-2`'s hold (item 1).
4. The `br-1` then `bq-2` merges, each under its pair, after cell 1.

## ADDENDUM (1.0.0_SA_CTO~DELL1, 2026-10-09 ~06:5xZ) -- placement 3 gains REBUILD #12, which serves R30 (`2.0.0_SA_COO~W1` msg 1938)

br-1 is merged @3255a9156d and closed @738c91f954, so gold's matcher carries R30 in code. Served gold carries it only after a rebuild,
and the placement above named the merges but not that rebuild. Placed now, independent of `bq-2` (bq-2 is the collector; this is gold):
- **Cell (now): rebuild #12's signing DRY RUN,** a worker cell shaped like bs-1. It writes nothing served. Its criteria:
  - every changed relationship is in br-1's removal class, with the census expecting 280 removals;
  - the count is printed beside the census;
  - any change outside the class is listed by row and is a STOP for the pair.
- **Then the served act** goes under its own never-widen pair (CTO and COO halves), signed on that dry run's measured diff, with
  rollback per key that writes the prior part as the newest and never deletes. `3.0.0_SA_CVO` grades a sample of the removed pairs
  after serve, as it did for #11.
