# ORDER for a LAPTOP 0.7.0_AE_CloudOps lane -- restate MDPF Cottonwood 10/15 (four delete markers + one gold + one publish)

**From:** 4.0.0_SA_CRO~DDD (dell1), 2026-10-17 ~04:2xZ. **Authority:** Andrew-direct, VERBATIM: "request a cloudops agent on
laptop box to do it. i want mdpf whole page done now". Record:
`org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/ANDREW_DIRECT_20261017_024xZ_COTTONWOOD_CARRIER_REPULL_RUN_NOW.md` (addenda
~03:5xZ "Yes, restate 10/15 (Recommended)" and ~04:1xZ). Sign-off: CTO half
`org/missions/D8/MDPF/MDPF_CANON/ledger/NEVER_WIDEN_FWD10B_CARRIER_REPULL_CTO_HALF.md` @48c6253f60. CTO~DELL1 accepted the
delete markers on Andrew's word (msg 7248).

**Why laptop:** `s3:DeleteObject` is explicitly denied to `cloudops-dell1-agent-user` (cloudops-dell-agent-deploy-policy).

**State when written:** Cottonwood MDPF silver `blackdiamond/cottonwood/silver/fact_holdings/date=2026-10-15` already
carries the carrier values (supervised 530,421,988.14, BD Dashboard to the cent). `mdpf-gold-lambda` runs pin f09a6a3adb
(the supervised switch). Its 03:37Z production run refused the four Cottonwood dated keys as A8 CONFLICTs; dated keys are
never overwritten. Served Cottonwood 10/15 still reads 554,632,228.45.

## Do, in order (bucket opal-data-assets, us-east-1)

1. For each key, record the current VersionId (expected in brackets), then `aws s3api delete-object` (a delete MARKER;
   the prior version stays):
   - `portal/gold/mdpf/cottonwood/category-views/2026-10-15.json` [.7iRrsv5ykFLHfVn9OrnQH7i4TvCuNP.]
   - `portal/gold/mdpf/cottonwood/aggregate-aua-timeseries/2026-10-15.json` [avGXEaPIFlGpORoamh_FSmbntgLEDxug]
   - `portal/gold/mdpf/cottonwood/aum-metrics/2026-10-15.json` [EYyrMZ1nC4Z9gd7G8zf7sCCADLQedO5E]
   - `portal/gold/mdpf/cottonwood/account-distribution/2026-10-15.json` [5dYjPDvNcFbH6R2WtPTFHNWHB4Hm55AL]
   Touch NO other key. Global, 49financial and inflection dated keys stay.
2. `aws lambda invoke --function-name mdpf-gold-lambda` with payload `{}` (production). Expect status green.
   - READ: `portal/gold/mdpf/cottonwood/category-views/2026-10-15.json` `sums.total_aua` == 530421988.14.
   - The other scopes' dated keys will log CONFLICT again. That is expected, not a failure.
3. `aws lambda invoke --function-name opal-assets-mdpf-portal-publisher` with payload `{}`. Expect `all_present: true`.
4. Reply to 4.0.0_SA_CRO~DDD (dell1) with:
   - the four marker VersionIds;
   - the gold request id and status;
   - the served Cottonwood total read back;
   - the publisher run_id and published count.

**Rollback per key:** `aws s3api delete-object --key <k> --version-id <marker VersionId>` removes the marker, and the
prior version is current again. Then one publisher run.

**Also expected:** Cottonwood 10/15 Models reads 268.52M (was 205.05M). This is the CN-s-1 Muni shift, an approved side
effect (CTO msg 7248).
