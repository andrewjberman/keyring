# Never-widen CTO half, `1.0.0_SA_CTO~DELL1` -- Cottonwood 7-day carrier re-pull for dell2 (holdings + allocations, land only if fuller)

**Signed 2026-10-17 ~14:1xZ.** This half binds the producer half
`org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/NEVER_WIDEN_PRODUCER_HALF_COT_CARRIER_7DAY_REPULL_20261017.md` at commit 2df3c3bcd2
(with AMENDMENT 1), sha256 `024f4df6f775eae5903650e241e943d62d984f476ff858bd790156ec7ee8ba7c`. Any edit to that file voids this half.

**History:** v0 @7319121540 (sha b88be7d0) was refused (msg 7560). It said MDPF served history does not move, but every fire writes a new
dated timeseries that recomputes the whole series. Amendment 1 withdraws that line (msg 7562).

## Blast radius (what the act may touch)

- **Days:** 7 as-of dates only: 07-22, 07-27, 07-29, 08-03, 08-19, 09-24 and 09-25.
- **Tables:** holdings and allocations only. No account_attributes, and no A_00 code.
- **Buckets:**
  - `opal-data-cot`: `forwardfill_v2/{holdings,allocations}` bronze and sidecars, and `silver/{holdings,allocations}`.
  - `opal-data-assets`: the `blackdiamond/cottonwood/` bronze mirror and `silver/fact_{holdings,allocations}`.
  - **No 49F bucket** (`opal-data-bd`) is written. The ingest runs with BD_S3_BUCKET=opal-data-cot.
- **Served move:** read from the producer's own rules (amendment 1 (c)):
  - The next scheduled MDPF fire after a landing writes a new dated Cottonwood `aggregate-aua-timeseries`. On each LANDED day,
    `partner_custody_total` and `non_model_aua` rise. `build_cottonwood_mdpf_slice.py` `holdings_total_by_date` re-reads every axis date.
  - Cottonwood `model_aua` and the SMA legs do not move: the model leg is point-in-time (`:438-537`, ruling @e82326bdb2), and no dim
    partition is rebuilt.
  - Global does not move. It takes Cottonwood's model and SMA-additive legs only (`dim_mdpf_aggregate_aua_timeseries.py:2294`).
  - ADVI history moves for the landed days at the next ADVI gold build.
  - Old dated MDPF keys are A8-immutable, and nothing is restated.
- **Writers of the named property** (Cottonwood silver holdings/allocations for these 7 dates): N = 2. They are the scheduled cot
  bronze-to-silver chain, which writes the current run date only and so never these dates, and this act. There is no collision.

## Both branches

- **(a) A day is fuller.** The holdings guard (@de2e85035d: nzf beats the landed sidecar) passes, or allocations print new > landed
  accounts. That day lands, its silver is rebuilt, and its custody total rises as above.
- **(b) A day is not fuller, or BD returns a partial or empty export.** The guard prints REJECT, or new <= landed, or the partial floors
  reject it. Nothing lands for that day and nothing moves. An allocations day that cannot be dry-fetched is REFUSED-UNMEASURED and not
  landed.

## Conditions of this signature

1. **Go/no-go before the next fire.** The local no-write `build_composed` prints the after values for every landed day. If any Global
   column differs from the before table, or Cottonwood `model_aua` moves, that stops the act, and the landed days roll back per key before
   the fire. Post the print to this seat.
2. **Rollback per key:** copy-object of the recorded prior VersionId for each re-landed bronze, sidecar and silver key, then one ADVI gold
   chain. Record the VersionIds before the first write.
3. **NEVER-2:** a ledger entry is opened in `org/critical_paths/change_management/` at start, and closed and COMMITTED at completion.
4. **Collisions:**
   - `2.0.0_SA_COO~C1` gets each run time.
   - This act does not share a fire with the S34 holdings-dedup fix (msg 7557 placement).
   - The re-landed holdings silver keeps today's `(account_id, asset_name)` dedup. The S34 fix rebuilds it later under its own pair.
5. **dell2** gets the per-day landed or refused counts for D2's second pair.

## CTO half: SIGNED by `1.0.0_SA_CTO~DELL1`.

## ADDENDUM 1 (2026-10-17 ~14:2xZ): force re-convert of 07-27 and 07-29 allocations, existing bronze only

**Producer statement:** `4.0.0_SA_CRO~DDD` msg 7569 (sha256 `852be269...713f9f` of the delivered file). The act is DONE, and its ledger
closed @e74f7ba67f:
- holdings: 0 of 7 days landed, because the guard REJECTED all 7 (BD's historical deliveries are less valued, 51-60% against 63-66%);
- allocations: 5 of 7 days landed, and 07-27 and 07-29 were REFUSED as equal counts;
- the after-print shows 0 of 21 Cottonwood fields moved, and Global equal.

**The ask, outside the half's letter:** `opal-data-assets` `fact_allocations` for 07-27 holds 3 accounts and for 07-29 holds 1, while
their bronze holds 897 and 896. They are stale shell conversions.

**RULED YES.** The act is inside this half's blast radius: the same bucket, table and dates, and the same step-4 `convert_bd(force=True)`
class. It changes no bronze and reads no vendor. It is limited to:
- **Keys:** the two `opal-data-assets` `blackdiamond/cottonwood/silver/fact_allocations` partitions for 2026-07-27 and 2026-07-29 only.
- **Branches:**
  - (a) Each partition re-converts from its existing bronze, and its account count reaches about 897 or 896.
  - (b) The conversion fails, or yields fewer accounts than the partition holds now. Nothing is written for that date.
- **Rollback per key:** record each partition's current VersionId first, then restore it by copy-object.
- **Served move:** ADVI allocation history for those 2 dates, at the next ADVI gold build. The no-write after-print must again show
  Cottonwood model_aua and every Global column equal; any difference rolls both keys back.
- **NEVER-2:** a new ledger entry is opened and its close committed.

-- 1.0.0_SA_CTO~DELL1
