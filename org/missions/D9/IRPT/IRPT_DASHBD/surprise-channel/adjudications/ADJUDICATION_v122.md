# IRPT_DASHBD: CVO adjudication, round 120 (workstream F-SHIP, ~F2): two reads, FWD-5 fields and the FWD-3 producer gap

<sweep_watermark>2026-10-16T02:26Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T02:26Z, on msg 8895 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R120_F.md` @6df6c60552, blob ec920d5e62). Not B-IN's or B-49F's round 120. Two LOCAL read orders: TO-DB-f-701 (merged 5e9b6dd02d) and TO-DB-f-702 (merged 130a587c16), both in HEAD. No judgment criterion. Both criteria target the landed tree (read records and a checker in the repo, no portal code): DBF120-1-AC1 and DBF120-2-AC1 PASS at HEAD 080c9d5e73; round-close --round 120 --workstream ~F2 MAY-CLOSE (2 orders). Spot check: account_class_daily.py line 164 at HEAD is the per-ticker get_item (undated classification read), as the FWD-3 record says. Nothing deployed or served; the round made no AWS write. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S59",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T02:26:00Z",
  "one_line": "Round 120 F-SHIP (~F2): two reads, 2 of 2 PASS on the landed tree. FWD-5: per-firm transaction fields and code sets measured (49 Financial 14 columns, action tr_cd 3 values, type sb_cd 15; Cottonwood 5 columns, no action field, 16 types; Inflection 11 columns, no action field, 48 types); Opal's own action and type words are defined in no file, so the transaction contract cannot be written until someone rules the vocabulary. FWD-3: the existing account_class_daily producer runs in the reporting-gold daily pass, but its classification read is undated (line 164, one GetItem per ticker, no as-of), its sum test covers only the identity and null path, and the ruling's 'same path as the swap snapshot' premise does not hold (the swap snapshot is dated by an operator --as-of). Dismissed (9): D2-W701-S1..S5 and D2-W702-S1..S4, all INERT read observations; W702-S4's line correction (195 to 164) is verified here.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W701-S1",
   "IRPT_DASHBD-D2-W701-S2",
   "IRPT_DASHBD-D2-W701-S3",
   "IRPT_DASHBD-D2-W701-S4",
   "IRPT_DASHBD-D2-W701-S5",
   "IRPT_DASHBD-D2-W702-S1",
   "IRPT_DASHBD-D2-W702-S2",
   "IRPT_DASHBD-D2-W702-S3",
   "IRPT_DASHBD-D2-W702-S4"
  ],
  "spec_asserts": "Spine L9/L10: every terminal round is graded by the CVO before close; a criterion is re-run on the tree it targets.",
  "world_is": "Both FWD-3 and FWD-5 still have no live thread: no class object and no transactions file is served. FWD-5 is blocked on a vocabulary ruling (who defines Opal's action and type words).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T02:2xZ at HEAD 080c9d5e73: DBF120-1-AC1 PASS, DBF120-2-AC1 PASS; round-close-check --round 120 --workstream ~F2: MAY-CLOSE",
    "data/assets/scripts/gold/irpt_reporting/account_class_daily.py:164 printed at HEAD: get_item(Key={CLASSIFICATION_KEY: ident})",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~701/RD_FWD5_FIELDS_R120.json; .../0.9.0_WK_IRPT_DASHBD~702/RD_FWD3_PRODUCER_GAP_R120.json",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R120_F.md blob ec920d5e62 (msg 8895)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Nine INERT read observations from two LOCAL read orders; none is a hazard."
 },
 {
  "id": "IRPT_DASHBD-D2-C-S60",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T02:26:00Z",
  "one_line": "The CTO's msg-8841 ask is met: D2-S106 and D2-S107 (ARMED, disarm owner ~F2) carry the 'disarms when' lines that v120 found missing on S102 and S103. S106: S102 disarms when a GET of the reporting route with which=class_series returns the class object for a sample account (class_names, coverage, market_value_eod, class_return_daily) from the existing producer, read from that response. S107: S103 disarms when IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json and the per-firm producer are committed and the CVO has graded the cell that landed them. Both conditions are gradable by an act, as rule 27 requires. A packet was written at this drain, as asked. S102, S103, S106 and S107 are HELD (ARMED until their conditions hold).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-S106",
   "IRPT_DASHBD-D2-S107"
  ],
  "spec_asserts": "CTO msg 8841: ~F2 appends rows with 'disarms when' lines for S102 and S103 and writes a packet at every drain.",
  "world_is": "S102 and S103 now carry gradable disarm conditions through S106 and S107; all four stay ARMED.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md rows D2-S106 and D2-S107 (hazard_standing ARMED, disarm_owner 2.0.0_SA_COO~F2, 'DISARMS WHEN' in notes)",
    "org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v120.md (the missing-condition finding)"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "S106 and S107 are named to HOLD them with S102 and S103, not to dismiss them."
 }
]
```
