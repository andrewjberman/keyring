# AMGT_RESAPP -- round 96 L8/L9 adjudication, packet FINAL (dell1)

<sweep_watermark>2026-10-11T19:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T19:50:00Z. L8 packet: 2.0.0_SA_COO~R1 msg 4082,
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round96/DRAIN_END_PACKET.md @04e9d955ff (blob 931611f542, verified).
One order, AMGT-bc-1, a READ (nothing served, no Bloomberg call). Its one JUDGMENT, AC2, is MET on this seat's own S3 reads (C-S90). 3 rows swept
since v116 (watermark 2026-10-11T18:55Z; 3 of 1071 investigation rows after it): all dismissed. No BLOCKING or ARMED row is open from this round.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S90",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T19:50:00Z",
    "one_line": "JUDGMENT AMGT_RESAPP.TO-AMGT-bc-1.read-whether-the-stored-bloomberg-data-for-the-listing-carries-a-sector AC2: MET. The outcome SECTOR-SERVED follows from the evidence, the control and the named surfaces: on this seat's own S3 reads the newest model blocks of SAN FP and CSL AU each carry GICS_SECTOR_NAME 'Health Care' from bloomberg-dapi under the exchange-qualified listing key, bronze refdata agrees, and the control BA US reads 'Industrials'. Three of the surfaces the reading left unread were read here and add no conflicting sector; the rest cannot change an existence answer. No Bloomberg call was made.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "This seat's own S3 reads (GET and list only; no Bloomberg call). Newest model block per key: SAN_FP_Equity 20261011T130935Z (newest of 17), top-level security 'SAN FP Equity', figures[3] {scope header, mnemonic GICS_SECTOR_NAME, value 'Health Care', source bloomberg-dapi}; CSL_AU_Equity 20260930T093804Z (newest of 6), security 'CSL AU Equity', the same record 'Health Care'; control BA_US_Equity 20261011T130241Z (newest of 31), 'Industrials'. The only other GICS_SECTOR_NAME occurrence in each block is the nested basis definition, not a value. Bronze refdata agrees: SAN FP 20261011T130928Z (of 11) key 'SAN FP Equity' GICS_SECTOR_NAME 'Health Care'; CSL AU 20260919T152121Z (of 3) 'Health Care'; BA US 'Industrials'. Why the evidence carries the outcome: each value is keyed to the exchange-qualified listing ('SAN FP Equity', 'CSL AU Equity'), not to the bare ticker that collides in etf-classifications; the control differs (Industrials), so the field is per security and not a constant; for CSL the value also differs from the collided table row (Carlisle: 'US Large Cap', sector null), while for SAN the table row happens to read 'Health Care' too, so for SAN the listing key, not the value, is what discriminates. Unread surfaces: this seat read three the reading left unread -- bronze bestdata (SAN of 11, CSL of 2), bronze identity (1 and 1) and bronze segments (SAN 1, CSL 0) -- and none carries a sector-class field, so none conflicts. Still unread by both: exec_officers, histdata, silver/listing_hit and the opal-data-assets equity reference tables. They cannot change the outcome: the question is whether the stored data CARRIES a sector, and a found per-listing value answers it; an unread surface could only add a second, possibly conflicting value, which by inference is unlikely (the field dictionaries hold one sector-class mnemonic). Carried, not a defect of the reading: CSL AU's value is as of 2026-09-30, and the label SECTOR-SERVED means stored, not served on the page (nothing is served until bc-2).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_AMGT_RESAPP~392/BC1_LISTING_SECTOR_READING_20261011.md (read whole)",
        "3.0.0_SA_CVO S3 GET s3://opal-data-harvest/derived/model_block/{SAN_FP_Equity/20261011T130935Z,CSL_AU_Equity/20260930T093804Z,BA_US_Equity/20261011T130241Z}/model_block.json 2026-10-11T19:4xZ",
        "3.0.0_SA_CVO S3 GET newest bloomberg/harvest/bronze/refdata, bestdata, identity, segments for SAN_FP_Equity and CSL_AU_Equity: sector only in refdata",
        "BLOOMBERG CALLS: none"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "JUDGMENT AMGT_RESAPP.TO-AMGT-bc-1.read-whether-the-stored-bloomberg-data-for-the-listing-carries-a-sector AC2: MET. The outcome SECTOR-SERVED follows from the evidence, the control and the named surfaces: on this seat's own S3 reads the newest model blocks of SAN FP and CSL AU each carry GICS_SECTOR_NAME 'Health Care' from bloomberg-dapi under the exchange-qualified listing key, bronze refdata agrees, and the control BA US reads 'Industrials'. Three of the surfaces the reading left unread were read here and add no conflicting sector; the rest cannot change an existence answer. No Bloomberg call was made."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S91",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T19:50:00Z",
    "one_line": "D1-W392-S1, D1-W392-S2 and D1-W392-S3 (INERT) dismissed: the order's wrong function name (the read is crosswalk.resolve()) changed no read; the key-only sweep was discarded and the mnemonic-record sweep is the one reported (this seat's own sweep read both planes and found the same values); CSL AU's older vintage (model block 2026-09-30, refdata 2026-09-19) is confirmed here and carried to bc-2 as its served sector_as_of, a CTO call.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W392-S1",
      "AMGT_RESAPP-D1-W392-S2",
      "AMGT_RESAPP-D1-W392-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W392-S1, D1-W392-S2 and D1-W392-S3 (INERT) dismissed: the order's wrong function name (the read is crosswalk.resolve()) changed no read; the key-only sweep was discarded and the mnemonic-record sweep is the one reported (this seat's own sweep read both planes and found the same values); CSL AU's older vintage (model block 2026-09-30, refdata 2026-09-19) is confirmed here and carried to bc-2 as its served sector_as_of, a CTO call.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-W392-S1, S2, S3",
        "adjudication row AMGT_RESAPP-D1-C-S90"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W392-S1, D1-W392-S2 and D1-W392-S3 (INERT) dismissed: the order's wrong function name (the read is crosswalk.resolve()) changed no read; the key-only sweep was discarded and the mnemonic-record sweep is the one reported (this seat's own sweep read both planes and found the same values); CSL AU's older vintage (model block 2026-09-30, refdata 2026-09-19) is confirmed here and carried to bc-2 as its served sector_as_of, a CTO call."
  }
]
```
