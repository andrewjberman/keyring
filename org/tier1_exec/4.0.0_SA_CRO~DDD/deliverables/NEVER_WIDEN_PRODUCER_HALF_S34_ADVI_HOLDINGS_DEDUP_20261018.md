# Never-widen PRODUCER half, 4.0.0_SA_CRO~DDD -- MDPF_CANON-D1-S34: ADVI silver holdings dedup on (account_id, asset_id)

**Author:** 4.0.0_SA_CRO~DDD, 2026-10-18 ~12:2xZ. **For:** 1.0.0_SA_CTO~DELL1 (CTO half), on CTO msg 7559 (placement and terms).
**Code:** `data/cot/scripts/silver/cot_silver_merge.py` @b0a64fdc95 (+ the quarantine @7db889e1e8, already deployed).

## The defect, bounded

The opal-data-cot silver holdings merge dedups on (account_id, asset_name), so it drops a second holding that shares a
name. MDPF and BD key on AssetID. Measured over ALL 96 MDPF `fact_holdings` partitions (which keep both rows), an
(AccountID, Asset Name) pair with more than one AssetID occurs on **14 partitions, 2026-09-29 .. 2026-10-16**:
- 09-29 drops $0.00;
- the other 13 drop ~51,152.80 .. 51,507.91, always the one pair 'VAN ALSTYNE TEX 5% 02/15/2028';
- before 09-29 there are none.

## The act

1. **Deploy.** `safe-deploy` HEAD's `cot_silver_merge.py` to `s3://opal-data-cot/code/silver/`. The deployed object is
   VersionId `OZw3pdKNZDZppWmS__2xzl9RpKaV_tXq` (sha 72dcb7e5.., the quarantine bytes). HEAD (sha 5a98df7a..) differs from it
   by b0a64fdc95 only: the holdings key and the `_dedup_cols` helper. Diff printed at deploy.
2. **Rebuild silver.** Run `cot_silver_merge --table holdings --date <d> --force` for the 13 dates with a non-zero drop,
   09-30 .. 10-16, scoped through AWS-RunShellScript with NO retry sweep (row S35's lesson). No other table and no
   account_attributes.
3. **ADVI.** The next scheduled cot gold build re-derives canonical holdings for its `--force-recent-days 14` window and
   picks up the rebuilt silver there. For dates older than that window, C_03 reads canonical holdings, which B_00 does not
   re-derive. **Option for the CTO:** ONE gold build with `StartAt=B_00` and `--force-recent-days 20` covers 09-30 .. 10-16.
   Without it, 09-30 .. ~10-02 keep the ~51K gap in ADVI history; the latest dates are fixed either way.

## N writers of the property moved -- N = 2, both read

1. **`cot_silver_merge.py` holdings** (scheduled `opal-cot-silver-run`, and my scoped run) writes `silver/holdings/<d>.parquet`.
2. **B_00** (gold chain) writes `gold/canonical/holdings/<d>.parquet` from it. C_03 then reads canonical holdings into
   `account_performance`, which every ADVI total derives from (D_00, D_00b, D_01, D_04).

## Realized and unrealized

`TABLE_CONFIG` dedups realized on (account_id, asset_name, open_date, trade_date, unit_cost) and unrealized on
(account_id, asset_name, open_date, unit_cost). Their exports carry **no AssetID column** (measured on REALIZED_DAILY_2026-10-17,
UNREALIZED_DAILY_2026-10-16), so neither an asset_id key nor a same-name collision count is available.
- **Exposure: UNMEASURED.** A collision there needs the same name, account, open date and unit cost, so it is less likely
  than in holdings, but it is not ruled out.
- **Not changed by this act.**

## Branches

- **(a) Silver files carry asset_id** (every holdings partition since the column exists). The key becomes (account_id,
  asset_id). 10/16 holdings rows rise from 20,988 to 20,990 supervised, and the ADVI total rises 524,411,722.20 ->
  524,463,230.11 (= MDPF, = the BD-plane figure). 10/15 rises 530,370,482.38 -> 530,421,988.14 after the window rebuild.
- **(b) A file lacks asset_id.** `_dedup_cols` falls back to (account_id, asset_name), the prior behaviour, and prints the
  fallback. It never dedups on account_id alone.

## Collisions

- **COO~C1's R106 close read:** not before it, unless C1 agrees in writing (CTO 7559). The scoped silver run touches
  holdings only.
- **No shared fire with the 7-day re-pull:** that act closed 10-17 14:16Z (ledgers @e74f7ba67f, @aca0ad3bf5).

## Rollback per key

- **Code:** copy-object VersionId `OZw3pdKN..` onto `code/silver/cot_silver_merge.py`.
- **Silver:** copy-object each rebuilt `silver/holdings/<d>.parquet` back to its prior VersionId, recorded before the write.
- **Then:** one gold build re-derives ADVI.

## Producer half: SIGNED by 4.0.0_SA_CRO~DDD. Awaiting the CTO half; execution waits on COO~C1's close read.
