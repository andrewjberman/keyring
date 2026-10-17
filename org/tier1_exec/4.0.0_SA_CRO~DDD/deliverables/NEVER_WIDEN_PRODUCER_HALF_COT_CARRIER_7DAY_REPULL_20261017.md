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
