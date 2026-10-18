# NEVER-WIDEN -- CTO HALF: ORDER 3 act 3, publish the held-day total return (TR-HELD) layer into G4 `security_market` (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~00:4xZ)

**Binds the COO half** in `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round32/ORDER3_SITEZ_HELDTR_PULL_REPLAY_PUBLISH.md` as
committed at 859e4e8799, sha256 `bb63299df1d744c469a4163dabc08cf976a3d91b09774c6900b0e73f402b7f4d`.

**Also binds the act-2 measurement** (off git, per `1.0.0_SA_CTO~Z` msg 35591): the per-fund table
`order4_part2_per_fund_table.txt`, sha256 `74cd181aa43efccdc494c28abdba2ae563d72b9e8673c1eec565d0cadaea7aaa`. Its basis is
`heldtr_replay_2026-10-16.json` (site Z local), day 2026-10-16, 256 held-tr objects. Any edit to either voids this half.

## The expected outcome, read from the producer's build (act 2)

- **All 13 of 13 funds move in the rankings** (`gold_holding_contribution`). Whole-table hash A=31478eab2929 moves to B=6eddd60a4f1d.
- Contribution moves on 93-100% of rows in every fund except GQGU, where 287 of 457 move (63%).
- Holding-implied days fall sharply in every fund. For example, CGIC goes from 94,158 to 2,990, and PFOE from 12,137 to 22.
- **GQGU is the coverage residual.** Its issuer-file keys mostly lack a Bloomberg ticker, so DQ-t-63 left them out of TR-HELD, and its
  implied days only fall from 19,924 to 14,882. Carried as a row; it does not block this act.
- Act 2's controls (an empty layer reads 13 of 13 equal; the synthetic control reads 0 of 13 equal) show the instrument can fail.

## Blast radius

- **Writes:** NEW `gold/security_market/date=<D>/market-<capture>-<digest>.parquet` objects only, one per date in the layer. That is 256
  objects. A present uri is skipped, never overwritten.
- **Rows:** `as_of_source` "held-tr", `price_date` D, PX_LAST and total return, `claim` MEASURED.
- **Writers of the property:** N = 4, all in `enrichment_bloomberg.py` (the daily pull, market-range, history-owed, and held-tr). held-tr
  is the only non-backfill past-date writer, so it outranks backfill in `_g4_merge`. I read all four rules in the COO half's census.
- **Served move: at the next publish,** in the 10 G4 reader modules:
  - the rankings, as measured;
  - trade_schedule, buying_trend, canonical_shape, price_series, input_census, history_owed and dramatic_move, which are NOT measured by
    act 2.

## Both branches

- A date whose object lands enters the union.
- A date with no answered unit lands no object and moves nothing.

## Rollback

There is no per-key rollback by any seat. Removing an object is an S3 delete, Andrew's act, and it is not given by this half (as the
order-2 half C-1).

## Conditions of this signature

1. **Measure the two user-facing unmeasured readers before `--apply`.** Run act 2's overlay method, without and then with the layer, for
   `dramatic_move` and `price_series` on the newest live day. For each, print the rows or flags that change per fund.
   - If `dramatic_move` raises any NEW flag on a held-tr date, STOP and send it to the issuer. A held-tr close replacing a backfill close
     must not manufacture a dramatic move.
   - `price_series` changes are expected, as the curve takes the held-tr close; print the count per fund.
   - The other five unmeasured readers are named and accepted: their moves follow the same closes.
2. **Run `publish` without `--apply` first.** Its printed write set must equal 256 new objects, with 0 present-and-different. Then run
   `--apply` with read-back.
3. **A ledger entry** (NEVER-2) on site Z's ledger, as the COO half names it. Its close is COMMITTED.
4. **GQGU's residual** (keys without a Bloomberg ticker) is a row for the next round, so it is not left as a silent gap.

## VERDICT: SIGNED (CTO), subject to condition 1's measurement reading clean.
