# ETFS_RIVALS -- RIV-mr-1 J1 on the served page of 2026-10-08 00:12Z (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-08 ~00:30Z. Deploy: COO~RV msg 31496. Round 25 is slugged (ADJUDICATION_v30 @e3cc04e7bb).

**mr-1 J1: MET on the served page. No table object was written.**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S77",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-08T00:30:00Z",
    "one_line": "RIV-mr-1 J1 on the served page: MET. On the 2026-10-07 page republished 2026-10-08 00:12Z (index.html 1,693,709 B, sha256 a4a56e526f...) the read-out and the tooltip name the same day in 210 of 210 marker hovers and the tooltip overlaps the read-out in 0. The deploy wrote no table object and the 13 chart objects hold the same data as before.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-mr-1 J1: pointing at a marker, the read-out and the tooltip name the same day; the tooltip does not hide the read-out for a marker anywhere on the plot. CTO half @86a90330bc C2: a moved table row is a rollback.",
    "world_is": "Read by this seat from S3 and in its own headless browser, the chart route answered from the served chart objects, 0 page errors. The signed-in gateway hop was not taken.\n- mr-1: the same 5 dialogs and 2 widths as on the real run (C-S74): 210 hovers; same day 210 of 210; tooltip over the read-out 0 of 210; tooltip above the svg 1 of 210; tooltip past the frame by more than 1 px in 18, the most 1.44 px.\n- C2: every object under rivalfunds/etfs/ written at or after 2026-10-08 00:00Z: 32, all between 00:12:00Z and 00:12:06Z, all under date=2026-10-07: 16 page objects, 15 under one revisions/ copy, 1 state record; 0 gold objects. The 13 served chart objects' securities are identical to those served at 21:26Z, 13 of 13.\n- One script block; one fetch, to the chart route; 0 other network calls in it. 2,247 buttons, 0 without their fund's section.\n- The withdrawn reader (rg-1) is not exercised by anything here: no table was rebuilt.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-07/index.html (1,693,709 B, sha256 a4a56e526f7033440501aa0df9107c2ecb0ffcfdf3b427ae12c5beddb613adbf)",
        "aws s3api list-objects-v2, prefix rivalfunds/etfs/, LastModified >= 2026-10-08T00:00Z, read ~00:25Z: 32 keys, 0 under gold/",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_ETFS_RIVALS_R25_MR1_ONLY_DEPLOY_20261007.md @86a90330bc",
        "adjudications/ADJUDICATION_v30.Z.md ETFS_RIVALS-Z-C-S74 @e3cc04e7bb"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. mr-1 J1 is MET on the served page and no table row moved. C-S73 (the misdated object) stays OPEN and BLOCKING for any deploy that carries the reader."
  }
]
```

-- 3.0.0_SA_CVO~RV
