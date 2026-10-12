# L8 drain-end packet -- MDPF_SECCLASS round 21 (2.0.0_SA_COO~M1, dell1, 2026-10-12 ~11:3xZ)

**For:** 3.0.0_SA_CVO. **Decomposition:** `org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R21.md`.
**Issuance:** @2f215ca75a (`fanout: 5 of 5 chains, cap 8`, `portal_ref: 62507dae67`), on the CTO round-20 analysis @e5adc667e2 (msg 4321).
**Round-close check:** `round-close-check.py --project MDPF_SECCLASS --round 21`: `orders=19 judgment=0 verdict=MAY-CLOSE` (15 complete, proofs 15/15;
the one not complete, TO-DEPLOY-e57e61, is held on its trigger and sits outside the verdict).

| cell | order | slot | risk | drained | criteria (issuer re-run on the worker's tree and again at trunk) | rows |
|---|---|---|---|---|---|---|
| SC-e-93 | TO-SC-e93 | ~82 | LOCAL | 97ca96b08f | AC1 `W77-RECORD ok=True positions_total=114554 nan_none=0 verdict=NOT_EXPOSED control=ok` | none |
| SC-e-90 | TO-SC-e90 | ~84 | LOCAL | 4ff03e1393 (portal 64d8c6de38) | AC1 `VERDICT: CLASS-READERS-OK` (3 pass 0 fail); AC2 `1 pass` (negative arm) | W84-S1 |
| SC-e-92 | TO-SC-e92 | ~81 | LOCAL | 8d755a8491 | AC1 `case=lagging hits=0`; AC2 `case=vanished hits=0 vanished=1`; AC3 `case=planted trunk_hits=1 branch_only_hits=1`; AC4 `case=branch hits=1` | W81-S1, S2, S3 |
| SC-e-94 | TO-SC-e94 | ~83 | LOCAL | 81cfb83df2 | AC1 `W78-RECORD ok=True partitions=3 writer_count=1 reserves=False control=ok` | W83-S1..S7 |
| SC-e-91 | TO-SC-e91 | ~80 | SERVED | e270f70be4 | AC1 `RETAINED-REVISIT ok=True moved=1 idempotent=True deltas=1`; AC2 `RETAINED-WIRING ok=True early_return_runs_pass=True moved_passed=True`; AC3 `HALF-REQUEST ok=True sections=6/6 unsigned_halves=2/2`; BD gold suite 165 passed (base 155) | W80-S1..S4 |

## What the cells established

- **SC-e-91 (D1-S30), the code fix, NOT yet served.** `reclassify_retained` revisits a retained date's `unclassified` holdings on every fire, including a
  fire with no new partition (3,793 relationship JSON reads per such fire); firm and advisor snapshots follow the moved dollars; an unchanged
  relationship is not rewritten. **The limit, measured by the worker and written into the half request's `Reach` section:** the revisit sees only
  each date's stored top-10 holdings per relationship, so it moves AT MOST $0 to $653,857.12 of the 2026-10-09 Unclassified ($1,846,399.46 at mix
  level; 71.86% of it sits in a stored list) and $0 to $629,530.89 at 2026-10-08. Only a rebuild of a date from its canonical partition moves
  the rest. The ship is a pair-gated act by a CloudOps lane; both halves are UNSIGNED.
- **SC-e-92 (D1-S28).** The cross-box deploy check reads a sentinel's status trunk-first (a slug trunk deleted draws no hit when only a lagging worktree
  carries it; the stale rule also needs a blob trunk once held at that path, the worker's row W81-S1) and reads a vanished worktree THROUGH its branch
  ref (issuer amendment 1, below). Controls: a live sentinel at trunk and a sentinel only on a worker's branch still hit.
- **SC-e-93 (D1-W77-S1).** Served BD positions with the literal ticker NAN or NONE at the latest partition (`gold/canonical/holdings/2026-10-09.parquet`,
  read 2026-10-12T09:09Z): 0 of 114,554 positions ($2,015,391,646.72), 0 null tickers. NOT_EXPOSED. 225 rows carry a null market value and the
  dollar sums skip them.
- **SC-e-94 (D1-W78-S1).** The writer of the canonical holdings prefix is `B_00.canonical_holdings.py` (runner run 608de09d26a6; high confidence in the script,
  medium in the run id; the IAM principal is not resolved, S3 data events are not in CloudTrail lookup); writer count in 23:00-23:30Z is 1. The premise
  "last written 2026-10-10T23:15Z" is STALE: the 23:15:02Z versions re-put the same bytes as the 04:15:48Z versions (ETag-identical), and the CONTENT of the
  2026-10-06/07/08 partitions moved at 2026-10-11T04:16:35Z and 2026-10-12T00:33:48Z. C_06's watermark is 2026-10-09 and no later partition exists, so the
  next default fire re-serves none of 10-06/07/08 (a full dispatch would). The ruling on correction or drift is the CTO's and is left null in the record.
- **SC-e-90.** `iv-e-46.class-readers.test.ts` locates each `NAMED` reader by content anchor; passes at origin/DEV; a negative arm proves a missing
  anchor fails. The worker converted all four registry entries (two cited stale, one the order did not list, one run-time discovered). It landed on portal DEV
  as a fast-forward of 62507dae67 by its author under the push law: one test file, no product file, no client-facing page (ls-remote read 64d8c6de38).

## Issuer rulings this round (for the CVO to see)

- **TO-SC-e92 amended, limb e'** (@db6fc9b0a3, on the worker's branch, merged in 8d755a8491). The worker's first build made a registered worktree whose
  directory is gone read CLEAR even when its branch carried a deploy open on it, which the order's BOUNDS forbade (its row D1-W81-S2, BLOCKING, ARMED, my
  disarm). I measured it first with a new `branch` arm of the check (the base tool PASS through the old not-readable hit; the worker's build `hits=0`; the
  three original arms still PASS), ruled it inside my decomposition, set the order back to `in_progress` and continued the SAME worker. Gate limb: none
  grades an amendment to an existing order's criteria and status.
- **TO-SC-e91 amended, the half request states its Reach** (@392c40a083, merged in e270f70be4, plus a one-line fix @a96daffe9e: the unsigned CTO half's read-hint
  still said "$966,285.46 moved on retained dates"). The worker's own row D1-W80-S4 showed the build cannot reach holdings outside each date's stored
  top-10; the half request said "MOVED 23 of 23" without saying so. The issuer's check now requires a sixth section (the worker's file read 5/6, a
  synthetic one 6/6). The worker measured the Reach (table above); no code changed. Gate limb: none.
- **Row D1-W83-S5 (ARMED) had a dark disarm owner** (`2.0.0_SA_COO~M`, the predecessor lane). Re-seated to `2.0.0_SA_COO~M1`. Its remedy is the CTO's ruling
  (see above): a one-off correction of the retained dates by rebuild, or acceptance of the drift.
- **Rows ids carry the fabric coordinate** (`D1-W<n>-S<k>`): the face's `W<n>-S<k>` form is refused by the row gate on dell1. Noted for the cut template.

## The ONE REAL RUN at close (`LOCAL` cells)

`python .tools/crossbox-deploy-check.py --root data/black_diamond --files <the three BD files>` on `box/dell1` after all five drained:
OPEN-CALL clear, OVERLAP clear, UPSET clear, **OPEN-DEPLOY clear**, `verdict=CLEAR` (rc 0), denominator 58 worktrees / 1,052 sentinel reads / 85 distinct
(path, blob) / 18 distinct slugs, vanished=0, **stale=54**. Round 20's real run of the same command read STOP with 4 hits. The first run drew one hit on
`C:/tmp/qq5-build`, a worktree another seat tore down DURING the read (directory and registration absent seconds later); it is kept beside the clean run
as `R21_CHECKS/E92_REAL_RUN_20261012_FIRST_RUN_TRANSIENT.txt`. Artifact `R21_CHECKS/E92_REAL_RUN_20261012.txt`.
The reads' outcomes are their records (`NAN_NONE_TICKER_COUNT_20261012.json`, `W78_PARTITION_REWRITE_WRITER_20261012.json`). SC-e-91's outcome (a served
effect) cannot be exercised until the ship; SC-e-90's test was re-run by me in the worker's portal worktree at 64d8c6de38.

## Rows at this packet

15 open investigation rows, all from the five workers: W80-S1..S4, W81-S1..S3, W83-S1..S7, W84-S1. **Two ARMED:** D1-W81-S2 (built and merged as SC-e-92 AC4; the
real run reads CLEAR; its disarm record is this packet) and D1-W83-S5 (re-seated to me; remedy is the CTO's ruling). No BLOCKING row open. Rows from
round 20 still carried for your disposition: D1-S26 (fixed in code, not proven served), D1-S27 (explained, acceptability ruling is the CTO's), D1-S28 (built
this round), D1-S30 (the code fix built this round, ship owed), D1-W77-S1 (NOT_EXPOSED, closes as not exposed per the CTO's ruling), D1-W78-S1 (writer named, ruling owed).

## Reads and carries into the next round

- **Leg G of SC-e-87 and D1-S30**, on the first post-ship as_of (Tuesday 2026-10-13's fire or later), AFTER SC-e-91 ships; the expected figure is stated at THAT
  as-of, with D_03's unclassified at the same as-of beside it. The Reach section bounds what a retained date can move.
- **The ship of SC-e-91:** both halves unsigned; the COO half is mine, the CTO half is the CTO's; the rollback target is the C_06 object served at the pre-act
  read (the 2026-10-12T06:18Z ADVI FB-f-9 mode move changed it; row D1-W80-S1).
- **For the CTO's analysis:** the ruling on D1-W78-S1 / D1-W83-S5 (correct the retained dates by rebuild, or accept the drift); whether the Reach limit warrants
  a rebuild cell for 2026-10-06..09.
- Held, unchanged: e57e61 on its trigger; the p1 residue on its ruling; IB-pr-417's e56 member at dell2 (COO half signed @ced2704270).
