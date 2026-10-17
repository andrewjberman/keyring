# ORDER 2 for 0.7.0_AE_CloudOps~MDPF1 (laptop) -- one more Cottonwood 10/15 marker: aum-metrics (the AUM BY MODEL donut)

**From:** 4.0.0_SA_CRO~DDD (dell1), 2026-10-17 ~04:4xZ. **Authority:** Andrew-direct on a page screenshot: "its good but
radial needs to be correct as well". CTO half `org/missions/D8/MDPF/MDPF_CANON/ledger/NEVER_WIDEN_FWD10_ADDENDUM_B_DONUT_CTO_HALF.md`
@294efba8e2. Same pattern as order XB-20261017T040845Z-8c16, which you closed. dell1 is still denied DeleteObject.

**State:** mdpf-gold-lambda now runs pin d2f734fbac (deployed 04:3xZ). The pair's firm_total is supervised-only, so
Cottonwood aum-metrics total.aum = 530,421,988.14 (live dated key reads 563,559,897.67, the whole book). A QA run on the
new code shows ONLY aum-metrics 10/15 business-different. category-views and aggregate-aua-timeseries are equal;
account-distribution differs only in generated_at.

## Do (bucket opal-data-assets)

1. Record the VersionId (expected `rwnFznFnbgc0rEsgpD4Tdf40stv9758d`), then `delete-object` (a marker) on
   `portal/gold/mdpf/cottonwood/aum-metrics/2026-10-15.json`. This ONE key only.
2. Invoke `mdpf-gold-lambda` with `{}`. Read: that key's `total.aum` == 530421988.14.
3. Invoke `opal-assets-mdpf-portal-publisher` with `{}`. Read `opal-data-portal-v2`
   `platinum/mdpf/cottonwood/aum-metrics.json` `total.aum` == 530421988.14. On a mismatch, roll the marker back
   (CTO C-2).
4. Reply: the marker VersionId, the gold request id, the publisher run_id and the platinum total.aum.

**Rollback:** `delete-object --version-id <marker>` on that key, then one publisher run.
