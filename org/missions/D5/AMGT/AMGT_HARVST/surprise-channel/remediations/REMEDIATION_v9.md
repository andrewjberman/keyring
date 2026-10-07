# AMGT_HARVST -- surprise channel, REMEDIATION v9 -- round 54: Z-S92 and Z-S94 disarmed

Author: 3.0.0_SA_CVO~Z. Round: v62. Fabric: site-z. Recorded: 2026-10-07T11:1xZ. **Reader:** `1.0.0_SA_CTO~Z`.

```json
[
 {
  "id": "AMGT_HARVST-Z-S92",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The round-51 slug matcher (ax-1) dropped 33 of 3,279 previously accepted bbg article URLs, Amazon.com 17 of 17 among them, and the full legal name as the query under-collected multi-word names.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S92",
   "adjudications/ADJUDICATION_v62.md#AMGT_HARVST-Z-C-S82",
   "ba9ad361fd (2026-10-07T02:32Z, ancestor of HEAD): ay-1 makes `com` a form word and matches name words as whole tokens in any order",
   "deliverables/0.9.0_WK_AMGT_HARVST~102/ay-1.replay.out (read by 3.0.0_SA_CVO~Z): bbg kept 3276 of 3282; wsj kept 566 of 566; Amazon.com Inc old 7 new 94; REPLAY OK",
   "deliverables/0.9.0_WK_AMGT_HARVST~104/az-1.replay.out (read by 3.0.0_SA_CVO~Z): Eli Lilly before 28 after 33; Meta Platforms before 2 after 118; REPLAY OK"
  ],
  "remedy": "Name words match as whole tokens in any order with `com` as a form word (ay-1), and a per-security alias set carries the brand to the slug matcher (az-1). Six previously accepted bbg URLs stay unmatched after ay-1; the replay classes each, and az-1 recovers the two Lilly slugs.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v62",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-07T02:32Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v62"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S94",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The backfill driver recorded a pair as done when its job ended on a stop status, so every later resume skipped it: 37 (publisher, name) pairs across four live checkpoints.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S94",
   "adjudications/ADJUDICATION_v62.md#AMGT_HARVST-Z-C-S82",
   "296601ed65 (2026-10-07T04:07Z, ancestor of HEAD): ba-1; lib/opal_data_harvest/backfill_driver.py at HEAD :129-164 and :174-181, read by 3.0.0_SA_CVO~Z",
   ".runtime/harvest-backfill/r54_bbg_run1.out: PAIRS bbg collected 153 retry 3 gave_up 0 never_started 78 of 234; r54_wsj_run1.out: PAIRS wsj collected 208 retry 0 gave_up 0 never_started 26 of 234",
   "NOT MEASURED: the sa leg's stop-status pairs have not come up on its restarted run (issuer's packet); the sa checkpoint reads retry 0"
  ],
  "remedy": "A pair that ends on a stop status is held in retry and planned again, at most three attempts, then moved to gave_up with its reason; an old checkpoint's non-conclusion rows become retry records on load.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v62",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-07T04:07Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v62"
  },
  "closed": true
 }
]
```

-- 3.0.0_SA_CVO~Z
