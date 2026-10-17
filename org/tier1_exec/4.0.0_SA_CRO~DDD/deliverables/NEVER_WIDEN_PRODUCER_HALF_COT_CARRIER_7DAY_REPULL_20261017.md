# Never-widen PRODUCER half, 4.0.0_SA_CRO~DDD -- Cottonwood 7-day re-pull for dell2 (holdings + allocations, land only if fuller)

**Author:** 4.0.0_SA_CRO~DDD, 2026-10-17 ~14:0xZ. **For:** 1.0.0_SA_CTO~DELL1 (CTO half).
**Ask:** dell2 CTO via 0.0.0_AB_MSTR~DELL1 msgs 7385 and 7434. **Rule:** CTO~DELL1 msgs 7390 and 7439 -- YES on all 7 days,
after 2.0.0_SA_COO~C1's fire read (done 12:34Z, msg 7508) and the 13:30Z fire (published 13:51Z). Holdings and allocations
only; no account_attributes.

## Days (as-of) and the run date that pulls each (1-bday snapshot lag)

| as-of | RunDate | dell2's finding |
|---|---|---|
| 2026-07-22 | 2026-07-23 | carrier rows absent |
| 2026-07-27 | 2026-07-28 | fact_allocations 3 accounts of ~880 |
| 2026-07-29 | 2026-07-30 | carrier rows absent |
| 2026-08-03 | 2026-08-04 | partial allocations |
| 2026-08-19 | 2026-08-20 | carrier rows absent |
| 2026-09-24 | 2026-09-25 | carrier rows absent |
| 2026-09-25 | 2026-09-26 | carrier rows absent |

Source of the list: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/RD_COT_CARRIER_ABSENT_DAYS_20261017.json`
@5e3c0c1d92, plus 07-27 per msg 7434.

## The act, per day

1. **Record** the current VersionIds of the day's bronze holdings, allocations and sidecars (opal-data-cot `forwardfill_v2/`),
   and its silver holdings and allocations in both buckets.
2. **Holdings:** SSM `opal-cot-bronze-run` Table=holdings, RunDate as above. The deployed no-regress guard (@de2e85035d) lands
   it ONLY if its nzf beats the landed sidecar. Otherwise it prints REJECT and nothing moves.
3. **Allocations:** the guard does not cover them. I first fetch the delivery WITHOUT landing it (a local DataMining read with
   the same template and as-of; no S3 write), print new vs landed account counts, and land only if new > landed (CTO 7439:
   equal or fewer does not land). The land is the same SSM run with Table=allocations. If a dry fetch is not possible from
   this box, allocations days are reported REFUSED-UNMEASURED and not landed.
4. **Rebuild:** for each landed day only, run scoped silver (`cot_silver_merge --table holdings|allocations --date <as-of>`;
   no account_attributes, no finalize), the MDPF mirror, and `convert_bd(force=True)` for that day's re-landed keys.
5. **Gold:** after all 7 days, ONE ADVI gold chain (B_00 --force-recent-days 14 covers only 10/03..10/16, so these July,
   August and September days change ADVI history only through C_03's full snapshot re-read). The MDPF dated keys for those
   days are A8-immutable, so MDPF history does NOT change from this act. That is stated, not worked around. dell2 gets the
   per-day landed or refused counts for D2's second pair.

## Branches

- (a) A day is fuller: it lands, and its silver is rebuilt.
- (b) A day is not fuller (guard REJECT, or allocation count <= landed): nothing lands for it.
- (c) BD returns a partial or empty export: the ingest's own partial floors reject it, and nothing lands.

## Served move and rollback

- **What can move:** ADVI history (account_performance and platinum timeseries) for the landed days, at the next ADVI gold
  build. MDPF served history does not move (A8).
- **Rollback per key:** copy-object of the recorded prior VersionId for each re-landed bronze, sidecar and silver key, then
  one ADVI gold chain.
- **Collisions:** COO~C1 gets each run time for its snapshot. No account_attributes partition and no A_00 code are touched.

## Producer half: SIGNED by 4.0.0_SA_CRO~DDD. Awaiting the CTO half.

## AMENDMENT 1 (2026-10-17 ~14:1xZ) -- CTO msg 7560: MDPF served history DOES move at the next fire

The earlier line "MDPF served history does not move (A8)" is **withdrawn: wrong.** A8 freezes the old dated keys, but every
fire writes a NEW dated `aggregate-aua-timeseries` that recomputes the whole series.

**(c) The rules this rests on (read in code):**
- **Total leg, recomputed every fire.** `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py` `holdings_total_by_date`
  re-reads `blackdiamond/cottonwood/silver/fact_holdings/date=<d>` for EVERY axis date on every run (`for d in dates:`),
  with no cache and no point-in-time pin. A re-converted silver partition therefore moves `partner_custody_total`, and with
  it `non_model_aua` (= total - model), for that date in the next fire's new dated key.
- **Model leg, point-in-time.** `cottonwood_gold_by_date` (same file, :438-537) keys each value_date to its EARLIEST
  `blackdiamond/cottonwood/gold/dim_model_portfolio` partition (Andrew ruling 2026-08-10, "point-in-time, history does not
  restate", @e82326bdb2). This act rebuilds no dim partition, so `model_aua` and the SMA legs do NOT move on the 7 dates.
- **Global.** `dim_mdpf_aggregate_aua_timeseries.build_global_artifact` takes Cottonwood's model and SMA-additive legs and
  NOT its custody or non_model (Client is 49F only, `GLOBAL_CLIENT_CONSTITUENTS = ("49financial",)`, :2294). So Global does
  not move on the 7 dates.

**(a) The move and its fire.** The next scheduled MDPF fire after the landing (the 13:30Z `mdpf-scheduled-floor` on the next
run day) writes a new dated Cottonwood `aggregate-aua-timeseries`. On each LANDED day, `partner_custody_total` and
`non_model_aua` rise by the landed carrier value (supervised only, under the FWD-10 switch). The ADVI history moves at the
next ADVI gold build.

**(b) Before values (served now, `portal/gold/mdpf/cottonwood/aggregate-aua-timeseries/2026-10-16.json`;
global `.../global/aggregate-aua-timeseries/2026-10-15.json`):**

| as-of | cot custody_total | cot model_aua | cot non_model | global model_aua | global opal_aggregate |
|---|---:|---:|---:|---:|---:|
| 07-22 | 432,828,463.21 | 127,143,134.99 | 305,685,328.22 | 1,683,808,436.76 | 1,958,990,786.07 |
| 07-27 | 437,876,540.63 | 126,369,737.47 | 311,506,803.16 | 1,674,953,802.51 | 1,952,765,208.42 |
| 07-29 | 435,249,975.13 | None | None | 1,671,074,249.56 | 1,946,492,076.49 |
| 08-03 | 443,619,506.02 | 132,521,716.52 | 311,097,789.50 | 1,704,272,885.96 | 1,983,305,573.89 |
| 08-19 | 449,733,561.36 | 146,008,861.28 | 303,724,700.08 | 1,750,174,707.61 | 2,037,496,150.98 |
| 09-24 | 520,542,325.69 | 198,026,295.50 | 322,516,030.19 | 1,798,653,702.99 | 2,091,947,684.52 |
| 09-25 | 521,308,070.48 | 201,286,426.57 | 320,021,643.91 | 1,809,980,302.09 | 2,105,280,662.98 |

**After values:** printed per landed day BEFORE the next fire, by a local no-write `build_composed` of the slice over the
re-converted silver. Expected: cot custody_total and non_model rise by the day's landed supervised carrier value; cot
model_aua and every Global column are equal to the before values. Any Global difference stops the act and the landed days
roll back per key.

**(d) Buckets written:**
- `opal-data-cot`: `forwardfill_v2/{holdings,allocations}` bronze and sidecars, and `silver/{holdings,allocations}`.
- `opal-data-assets`: the `blackdiamond/cottonwood/bronze/...` mirror and `silver/fact_{holdings,allocations}` via the
  converter.
- **NO 49F bucket (`opal-data-bd`) is written.** The ingest runs with BD_S3_BUCKET=opal-data-cot. The guard's
  opal-data-bd copy was rolled back by CTO 7262, so 49F runs its prior code.
