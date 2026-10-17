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
