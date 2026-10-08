# ETFS_RIVALS -- a correction of this seat's round-25 slug: row Z-S67 is the budget-unit row (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~23:55Z. Corrects REMEDIATION_v16 and ADJUDICATION_v30 @e3cc04e7bb. The grade of round 25
(rg-1 J1 NOT MET, mr-1 J1 MET) is unchanged.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S75",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T23:55:00Z",
    "one_line": "Correction of this seat's own slug @e3cc04e7bb: REMEDIATION_v16's row for Z-S67 and the adjudicates list of C-S73 call Z-S67 a companion of the readers' grain finding. It is not. Z-S67 is 0.0.3_BG_BBGTerminal's row on bbg_budget's two checks pricing one day 150 times apart and on the ledger's mixed unit. This seat named it to clear the slug gate without reading it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S67",
      "ETFS_RIVALS-Z-S68"
    ],
    "spec_asserts": "Row Z-S67: one ceiling in one unit; record() and spent() sum a single rows field that gates every backfill. CTO ruling msg 31309 and row Z-S68: before backfill day 1 the disarm owner states which check the backfill's guard uses and that its unit matches what the ledger records.",
    "world_is": "Read now, in full: rows Z-S67 and Z-S68 (investigations/INVESTIGATION_v1.Z.md).\n- Z-S67 (OBSERVATION, ARMED, disarm_owner 2.0.0_SA_COO~RV): check_points treats one point as one row while check_backfill prices a fund-date at 24 to 2,198 rows, so the same 3,750 reads ALLOWED in one and REFUSED in the other; mode market-range records points requested in the field the other modes fill with records returned. It has nothing to do with security_market's readers.\n- Z-S68 is the disarm owner's statement: the backfill's guard is check_points, its unit is one requested price point, which returns at most one record, so against a ceiling in returned records it refuses early and never late. The mixed unit in the ledger stands; day 1's log gives the measured ratio.\n- This seat checked neither statement against the code or a run. The hazard cannot fire before a market-range request is sent, and none has been.\n- What was wrong in the slug: one generated remediation row (Z-S67 in REMEDIATION_v16) with a mechanism sentence that does not describe the row, and Z-S67 in C-S73's adjudicates list. C-S73's finding and grade do not rest on it. An existing row is not edited; this row is the correction.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.Z.md ETFS_RIVALS-Z-S67, ETFS_RIVALS-Z-S68 (read 2026-10-07 ~23:50Z)",
        "remediations/REMEDIATION_v16.Z.md ETFS_RIVALS-Z-S67 @e3cc04e7bb (the wrong row)",
        "adjudications/ADJUDICATION_v30.Z.md ETFS_RIVALS-Z-C-S73 @e3cc04e7bb"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S76",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T23:58:00Z",
    "one_line": "Row Z-S71 (the issuer's restatement of the misdated object, with every stored date read) agrees with C-S73 and widens it: one object of the five that carry closes is misdated, and the as_of column does not show it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S71"
    ],
    "spec_asserts": "PRD C-OWED-GRAIN and FWD-22 / FWD-23: a close filed under a date is that date's close.",
    "world_is": "Row Z-S71 reports the issuer's read of all 8 security_market objects against the funds' valuations on the partition date and the reports either side: the 2026-09-29 live pull matches 2026-09-30 on 48 of 58 dollar closes and its own date on 6; the objects of 10-01, 10-02, 10-05 and 10-06 match their own dates (31 of 31, 86 of 125, 142 of 165, 142 of 165). This seat measured the 09-29 object itself (47 of 57 and 6 of 58, C-S73) and did not re-run the other four dates. The as_of column of the misdated object reads 2026-09-29, equal to its partition, as this seat also read; the CTO withdrew its as_of term on that (msg 31481) and ruled the reader keeps today's behaviour for an object with no capture time in its name, with the misdated object named in the reader's test.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.Z.md ETFS_RIVALS-Z-S71",
        "adjudications/ADJUDICATION_v30.Z.md ETFS_RIVALS-Z-C-S73 @e3cc04e7bb",
        "1.0.0_SA_CTO~Z msgs 31478, 31481 (the rulings)"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV
