# IRPT_DASHBD -- rounds 10 to 11 (workstream B) remediations

<sweep_watermark>2026-10-03T02:35Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-03 ~09:1xZ. L8 input: the issuer's drain-end record org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/IRPT_BCKEND_ROUNDS_37_41_P_AND_DASHBD_10_11_B_DRAIN_END_20261003.md @252181b2ba (msg 104591). 17 of 17 orders are complete. DB-b-18 is merged @65a788ebf1 and DB-b-19 @b9b2f81739. 2 rows surfaced after the previous watermark 2026-10-03T01:40Z (W5-S1, W5-S2); 48 rows are in the channel. 0 are dismissed, so no adjudication file is minted (the row gate refuses an empty one). Both graduate here, OPEN. 0 ARMED, 0 JUDGMENT criteria. The cells' served outcomes (P-2, P-3) are read at the P-2 window's V leg; the window opens on Andrew's PROD-promote word (CTO batch 222 @e67cba94ac). One carried row moves at this compile: REMEDIATION_v3's W1-S17 advances OPEN -> REMEDIATED, closed false. The read behind it: DB-b-19 declares dividend_interest_share_quantity in sources.json and admits a DIV debit only on a negative share quantity (account_return_daily.py:232-236); the irpt_reporting suite passes 22 of 22 at HEAD; test_short_div_debit passes 8 of 8 on the fixed producer and fails 5 of 8 on b9b2f81739^1's producer (this seat's scratch run). It is served in the window, gold Mex71Y5g.

Graduated here: W5-S1 at the next read rebuild, W5-S2 at the P-2 window's leg A3, both owned by 2.0.0_SA_COO~P. Round label v12. Carried: REMEDIATION_v1 S8; REMEDIATION_v2 S12, S15, S18, S19, W1-S7 and S22 (OPEN), and S20 (REMEDIATED on DEV, not closed); REMEDIATION_v3's P-2 rows (OPEN) and W1-S17 (REMEDIATED here in place, not closed).

```json
[
  {
    "id": "IRPT_DASHBD-W5-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The read entry's _staged_from_note in lambda-source-map.json says its shared boundary members sit at ONE pin; after DB-b-18's re-pin its 28 members sit at 6 pins (23 at 5f582dca96; served.py, enforce.py, maintained_sources.py, NAMING_SCHEMA.json and sources.json each at their own), so the note is stale.",
    "evidence": [
      "investigation row IRPT_DASHBD-W5-S1",
      "infra/aws/lambda/ci/lambda-source-map.json irpt-reporting-read-lambda at DB-b-18's merge @65a788ebf1"
    ],
    "remedy": "AT THE NEXT READ REBUILD (issuer): reword the note to the pins it holds, or re-pin the closure to one pin. Decide whether the read artifact tracks the Holdings closure or its own HEAD.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v12",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v12"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W5-S2",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Contract 0.3.0's schema_hash (73e80ef7..) types tieout_tolerance_proposed as double. That holds only if the P-2 method-row write passes --tieout; without it the producer writes None, pyarrow types the column null, and the served hash differs from the contract's.",
    "evidence": [
      "investigation row IRPT_DASHBD-W5-S2",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py emit_method_row (lines 1729-1775 at 1067171ecd)",
      "NEVER_WIDEN_SIGNOFF_PACKET_P2_WINDOW_20261003.md @855fdad77c leg A3: the method-row write passes --tieout 0.037 (drain-end record @252181b2ba)"
    ],
    "remedy": "P-2 WINDOW LEG A3 (issuer): the write passes --tieout 0.037. Closed when this seat reads the served method row's schema_hash equal to the contract's 73e80ef7..",
    "owner": "2.0.0_SA_COO~P",
    "round": "v12",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v12"
    },
    "closed": true
  }
]
```
