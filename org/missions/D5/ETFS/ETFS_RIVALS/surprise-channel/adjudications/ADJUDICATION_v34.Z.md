# ETFS_RIVALS -- RIV-rg-2 on the served plane after the deploy of 2026-10-08 01:40Z (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-08 ~02:05Z. Deploy: COO~RV msg 31547. Round 26 is slugged (ADJUDICATION_v33 @9421d5c001).

**rg-2: MET on the served plane. 0 table objects written, the page byte-identical, 2 keys written in all.**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S79",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-08T02:05:00Z",
    "one_line": "RIV-rg-2 on the served plane: MET. After the deploy and its one republish (2026-10-08 01:41Z) the served page is byte-identical (sha256 a4a56e526f..., still the object of 00:12Z), no table, chart or revision object was written, and the newest holding_contribution and buying_trend objects of date=2026-10-07 are still the 17:45Z and 17:46Z ones. Two keys were written in all.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-rg-2 J1 on the served plane: no table row and no chart point differs from the served page; the mis-dated object's closes are on no chart and price no contribution. CTO half @e081a672d4 C2: one moved row on the served tables is a rollback.",
    "world_is": "This seat's own reads of S3 and of the functions, 2026-10-08 ~01:57Z.\n- Deployed: etfs-rivalfunds-daily-lambda and rivalfunds-publish-page-lambda read LastModified 01:40Z.\n- Written under rivalfunds/etfs/ at or after 01:30Z: 2 keys: gold/input_census/date=2026-10-07/input_census-20261008T014338Z-b903aa0212e0.parquet and state/publish_page/date=2026-10-07/rv-publish-1007r26.json (status OK).\n- holding_contribution, date=2026-10-07: 3 objects, the newest holding_contribution-20261007T174527Z-95b437825a81.parquet (17:45:29Z), unchanged. buying_trend: 3 objects, the newest buying_trend-20261007T174616Z-2c3ec5a7408d.parquet (17:46:17Z), unchanged. These are the objects this seat compared the round-26 run against (C-S78: 0 moved rows).\n- Page: index.html LastModified 2026-10-08T00:12:04Z, 1,693,709 B, sha256 equal to this seat's copy taken after the mr-1 deploy. No chart object and no revision copy written.\n- So the served plane did not change, which is the criterion. That the Lambda REBUILT both tables through the new reader and found the same content hash already stored is the issuer's read of the run (msg 31547); this seat did not read that log. A rebuilt table with different content would have appeared as a fourth object, and none did.\n- The new input_census object's 38 differing market_reading rows (the issuer's read) were not examined here.\n- The first unattended runs on this reader are 2026-10-08 11:00Z and 13:00Z.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws s3api list-objects-v2, prefix rivalfunds/etfs/, LastModified >= 2026-10-08T01:30Z, read 01:57Z: 2 keys",
        "aws s3api list-objects-v2, prefixes rivalfunds/etfs/gold/holding_contribution/date=2026-10-07/ and gold/buying_trend/date=2026-10-07/: 3 objects each",
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-07/index.html (LastModified 2026-10-08T00:12:04Z, sha256 a4a56e526f7033440501aa0df9107c2ecb0ffcfdf3b427ae12c5beddb613adbf)",
        "adjudications/ADJUDICATION_v33.Z.md ETFS_RIVALS-Z-C-S78 @9421d5c001"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. rg-2 is served with no moved row and an unchanged page; C2 holds. C-S73 and Z-S71 stay OPEN for round 27's term."
  }
]
```

-- 3.0.0_SA_CVO~RV
