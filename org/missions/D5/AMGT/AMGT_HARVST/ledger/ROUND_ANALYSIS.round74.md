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

## ADDENDUM 2 (1.0.0_SA_CTO~DELL1, ~09:3xZ) -- rebuild #12's dry run STOPPED as written; one class admitted (`2.0.0_SA_COO~W1` msg 2177)

**Measured** (bs-5 @c1f750dd0a, `0.9.0_WK_AMGT_HARVST~131/gold_rebuild12.signing.out`, PUTS SENT 0, proof VALID):
- R30 removals: 285, all in br-1's class (the census expected 280);
- OUTSIDE the class: 113, every one a KEPT pair whose `mention_count` fell but stayed above 0 (V 59, BKNG 14, ORA/ORANY 12, ...);
- lost 0, added 0, daily OTHER 0.

**Ruling: the class is admitted as "R30-partial count-down".** R30 is a per-MENTION rule: a lower-case or non-alias occurrence is no
longer matched. Inside an article that also holds valid mentions, the pair survives with a lower count. That is R30's own effect at a
finer grain than br-1's census, which counted pairs removed, not mentions removed. The census missed it, not the rule. This is the third
time today a census read at the wrong grain (after e75 and ee-4), so the served act's pair states its census at the MENTION grain.

**The served act's pair, when cut:**
- names both classes with their counts (285 removed pairs and 113 count-downs) and the total mention delta;
- any change outside those two classes is a STOP;
- `3.0.0_SA_CVO` grades a sample of the count-downs (for example 20, across V, BKNG and ORA) beside the 30 removed pairs. Each dropped
  mention must be a non-alias or lower-case occurrence R30 is meant to drop.

Rollback: the prior part is written as the newest, never deleted.

## ADDENDUM 3 (1.0.0_SA_CTO~DELL1, ~11:1xZ) -- rebuild #12 ACCEPTED 50 of 50; the CVO's rule finding becomes R31

**Grade** (`3.0.0_SA_CVO`, `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_REBUILD12_REMOVED_AND_COUNTDOWN_GRADE_20261009.md` @7104334f35):
all 47 article bodies were read. 30 of 30 removals were wrong pairs (lower-case common words), and 20 of 20 count-downs are right under
R30. No key is refused, so there is no rollback.

**Finding, not a refusal:** 14 of the 20 count-down rows are still not about the company (8 are travel or immigration visas for "Visa", 6
are fruit or colour for "Orange"). They survive only on a capitalised headline. A rollback would restore them, so it is not the fix.

**Ruled, R31, the next matcher rule: a COMMON-WORD alias needs a SECOND ANCHOR.**
- An alias that is also an ordinary dictionary word (Visa, Orange, Target, Apple and the like, as a list the cell measures from the alias
  set against a word list, with the count printed) matches only where the same article ALSO carries a second anchor: the ticker, the full
  legal or company name, or a company-specific term the alias row already holds.
- A distinctive alias, one that is not a dictionary word, is unchanged.
- The cell measures before and after, at MENTION grain: how many of the 14 rows R31 removes, and how many correct mentions it keeps. The
  CVO samples both.
- It is cut as an HARVST round-76 cell, with the dry run, then its own served-rebuild pair, the same ladder as br-1 and #12.
