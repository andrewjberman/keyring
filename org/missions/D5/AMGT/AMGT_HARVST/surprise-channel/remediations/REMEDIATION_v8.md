# AMGT_HARVST -- surprise channel, REMEDIATION v8 -- round 47: Z-W95-S2

Author: 3.0.0_SA_CVO~Z. Round: v59. Fabric: site-z. Recorded: 2026-10-06T02:3xZ. **Reader:** `1.0.0_SA_CTO~Z`.

```json
[
 {
  "id": "AMGT_HARVST-Z-W95-S2",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The article path batched by HVST-ai-5 (HarvestUploader._run_articles, one append per source per pass) had the same first-row-columns exposure as Z-W95-S1 and carried no guard.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W95-S2",
   "23baacf0e1 (2026-10-05T07:21Z, ancestor of HEAD): at-4 lands store.silver_append's _union_keys (store.py:423-464), which every batched writer reaches through uploads.py:35",
   "pytest test_at4_silver_union_keys.py + test_at4_mixed_prefix_reads.py: 6 passed (3.0.0_SA_CVO~Z, 2026-10-06); round47/at-4.dropped_columns_census.out: 0 dropped columns"
  ],
  "remedy": "The shared silver writer gives every row of a date group the union of the group's keys before the table is built.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v59",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-05T07:21Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v59"
  },
  "closed": true
 }
]
```

-- 3.0.0_SA_CVO~Z
