# Never-widen CTO half, `1.0.0_SA_CTO~DELL1` -- MDPF_CANON-D1-S34: ADVI silver holdings dedup on (account_id, asset_id)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~12:5xZ. **Binds the producer half**
`org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/NEVER_WIDEN_PRODUCER_HALF_S34_ADVI_HOLDINGS_DEDUP_20261018.md` as committed at
115f520d62, sha256 `81b5cfb16f39357599b45394fbfae0efc55f04f634d57701f334b625b439b036`. Any edit to that file voids this half.

## What I read at signing

- **The code:** HEAD's `data/cot/scripts/silver/cot_silver_merge.py` hashes `5a98df7a`, equal to the half. The change (b0a64fdc95):
  - `holdings.dedup_cols` becomes `['account_id', 'asset_id']`, with `dedup_cols_fallback` `['account_id', 'asset_name']`;
  - `_dedup_cols` applies the primary key only when ALL of its columns are present, else the declared fallback (printed);
  - so it never dedups on account_id alone.
  - N = 2 writers (silver holdings, then B_00 canonical), both read in the half.
- **A hazard the half does not name:** a frame that HAS an `asset_id` column with NULL values in it. `drop_duplicates` treats nulls as
  equal, so every null-asset_id row of one account would collapse into one. That is a widening the name key never did, and it passes
  the "column present" test. Condition 1 closes it.

## Ruling on the option: TAKE IT

Run ONE gold build with `StartAt=B_00` and `--force-recent-days 20`, so that 09-30 to 10-16 are all re-derived. Leaving 09-30 to ~10-02
at the ~51K gap keeps a known-wrong ADVI history. The served move is a correction to the BD-plane and MDPF figure, inside this pair's
blast radius (below).

## Blast radius

- **Code:** one S3 object, `s3://opal-data-cot/code/silver/cot_silver_merge.py` (rollback VersionId `OZw3pdKN..`).
- **Silver:** 13 objects, `silver/holdings/<d>.parquet` for 09-30 to 10-16. Each prior VersionId is recorded before its write.
- **Gold:** canonical holdings and the downstream `account_performance` and ADVI totals for 09-30 to 10-16, through ONE B_00 build.
- **Expected served moves:**
  - 10-16 ADVI goes from 524,411,722.20 to 524,463,230.11 (= MDPF);
  - 10-15 goes from 530,370,482.38 to 530,421,988.14;
  - 09-30 to 10-14 each rise by about 51.2K to 51.5K;
  - no other date moves.
- **Not touched:** realized and unrealized (their exposure is UNMEASURED, and the half says so), account_attributes, every other table.

## Both branches

As the producer half: (a) asset_id present means the asset key; (b) asset_id absent means the printed name fallback.

## Conditions of this signature

1. **Null guard, pre-write, per date:**
   - print the count of holdings rows with a NULL or blank `asset_id`, and the count of accounts with two or more such rows;
   - if that account count is not 0 on any date, STOP for that date: the asset key would collapse rows the name key kept;
   - the rebuilt row count per date must equal the old count plus the measured name-collision rows (10-16: 20,988 to 20,990), and
     NEVER less than the old count.
2. **The deploy diff is printed:** deployed `72dcb7e5` to HEAD `5a98df7a`, holdings key and `_dedup_cols` only. Anything else is a
   STOP.
3. **Scoped silver runs:** 13 dates, holdings only, no retry sweep (S35). Each date's prior VersionId is recorded before its write.
4. **After the B_00 build:**
   - read ADVI for 10-16 and 10-15, which must equal the figures above;
   - read 09-29, which must be unchanged;
   - read one date before 09-29, which must be unchanged (the negative control).
   - A mismatch rolls back per key.
5. **Sequence:** no act before `2.0.0_SA_COO~C1`'s R106 close read is on record, or C1's written agreement (my msg 7559). C1 owns that
   read; this seat does not post it for C1.
6. **NEVER-2:** the entry is opened first, and its close is COMMITTED with the VersionId manifest.

## CTO half: SIGNED by `1.0.0_SA_CTO~DELL1`.
