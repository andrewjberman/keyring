# ETFS_RIVALS -- round 26 L8/L9 on the round-26 real run (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-08 ~01:20Z. Packet: COO~RV msg 31505 (@a4ce155438). NOT deployed.

**rg-2 J1: MET. Nothing moves: 0 of 6,066 and 0 of 1,406 table rows, 13 of 13 chart objects; the mis-dated object's closes
are on no chart.**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S78",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-08T01:20:00Z",
    "one_line": "Round 26 L9 on the issuer's real run of day 2026-10-07 (local, not served): RIV-rg-2 J1 MET. 0 of 6,066 holding_contribution rows and 0 of 1,406 buying_trend rows differ from the served tables; 13 of 13 chart objects carry the served data; no chart has a market point on 2026-09-29 and no point equals a close of the mis-dated object. By hand: the objects dated 2026-10-02 and 2026-10-05 fit their own dates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-rg-2 J1: on the real day no table row and no chart point differs from the served page; the 2026-09-29 closes of the mis-dated object are on no chart and price no contribution.",
    "world_is": "This seat's own reads of C:/tmp/rv-r26-realrun/layer/ against the served objects.\n- Tables (float tolerance 1e-9, every column but the revision stamps): holding_contribution 6,066 rows, same keys, 0 moved; buying_trend 1,406 rows, same keys, 0 moved. Round 25's reader moved 3,259.\n- Charts: 13 of 13 objects' securities identical to the objects served since 2026-10-08 00:12Z. Points on 2026-09-29 across all objects: 173 valuation-implied, 517 empty, 0 market. Market points exist on 4 dates only: 10-01 (87), 10-02 (548), 10-05 (592), 10-06 (592). Points equal to a close of market-20260929-53bc393958bd.parquet on 09-29 or 09-30: 0.\n- The figure that showed the fault: MediaTek in CGIC, 30 days, reads +0.062 percent at rank 5, as served (round 25 would have made it +0.295 at rank 2).\n- By hand, what a count on the tables cannot show, the dating of two other objects, dollar closes against the funds' own valuation of each report date within 0.2 percent: the object dated 2026-10-02 fits 10-02 on 84 of 93 (median difference 0.0 percent) and 09-30, 10-01, 10-05 on 18, 14, 16; the object dated 2026-10-05 fits 10-05 on 126 of 136 (0.0) and its neighbours on 16, 10, 12. Both are correctly dated. With C-S73 this seat has read 3 of the 5 dates that carry closes; 10-01 and 10-06 are the issuer's read (row Z-S71).\n- The packet's limits stand and are not graded here: the rule rests on a name's shape plus one named object, so a future mis-dated object with a timed name would be read (round 27's per-close trading date answers it); sectors are still joined from the mis-dated object; why the 09-29 pull is a day early is not traced.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round26/DRAIN_END_PACKET.round26.md @a4ce155438",
        "C:/tmp/rv-r26-realrun/layer/opal-data-etfs/rivalfunds/etfs/ gold tables and 13 chart objects on site Z, read 2026-10-08 ~01:15Z",
        "s3://opal-data-etfs/rivalfunds/etfs/gold/security_market/date=2026-10-02/market-20261005T124613Z-ea632b9bca87.parquet; date=2026-10-05/market-20261006T123301Z-b6602b19fad6.parquet",
        "adjudications/ADJUDICATION_v30.Z.md ETFS_RIVALS-Z-C-S73 @e3cc04e7bb"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV
