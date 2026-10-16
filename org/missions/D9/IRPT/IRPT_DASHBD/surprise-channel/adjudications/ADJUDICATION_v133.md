# IRPT_DASHBD: CVO adjudication, round 127 (workstream F-SHIP, ~F2): transaction contract 0.1.0 and the 49F producer, a known-wrong draft

<sweep_watermark>2026-10-16T07:09Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T07:09Z, on msg 9151 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R127_F.md`, resolved by git log -1 on the path to 92695738aa, blob 62afa30910). Not B-IN's or B-49F's round 127. Two LOCAL orders: TO-DB-f-1301 (contract 0.1.0 and the mapping file, drain 94d8b2ff60 at 06:31:12Z) and TO-DB-f-1302 (the producer and 23 tests, drain af8468b4b8 at 06:58:12Z), both in HEAD. No judgment criterion. Re-run on trunk (HEAD fbbaf7758e): DBF127-1-AC1, AC2, DBF127-2-AC1, AC2 PASS; round-close --round 127 --workstream ~F2 MAY-CLOSE. Nothing served, nothing wired, no Terraform. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S71",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T07:09:00Z",
  "one_line": "Round 127 F-SHIP (~F2): MAY-CLOSE ONLY AS A KNOWN-WRONG DRAFT, pending round 128's amendment (0.2.0). It must not read as a ratified contract. (1) ABSENT CLAIMS KNOWN FALSE. The contract marks settle_date, asset_name, fee and source_txn_id 'absent' for every firm. Measured by this seat: COTTONWOOD (v130) carries all four (Settle Date, Asset Name, Transaction Fee, TransactionID). INFLECTION (v130) carries source_txn_id (id) and an asset_name candidate (productName); settle_date and fee are truly absent. 49 FINANCIAL (one fact_trn partition, 2026-10-14, 140 columns, read here) carries fee (8 fee columns plus commission and exec_brok_comm) and source_txn_id candidates (schwab_cashiering_unique_id, cashiering_transaction_identifier); no settle or security-name column is in the 140. So of the 12 firm-column absences, 7 are false (COT 4, INF 1 sourced + 1 candidate, 49F 2), and the producer writes None where 49F has a fee and an id. (2) ONE-DRAIN RULE NOT MET (CTO msg 8735): the contract landed at 06:31Z and its writer, the producer, at 06:58Z, in two drains 27 minutes apart. Trunk had no red test because no writer existed yet. (3) S103 CANNOT DISARM ON THIS ROUND: S107 (CTO msg 8841) disarms S103 only when the transaction contract and the per-firm producer land WITH THEIR L9. This round has no judgment criterion, so no L9 exists, and S102, S103, S106 and S107 stay ARMED. (4) RULE 24: the ratified words carry their four-postulate record and census in the round-124 proposal (v128). The contract's own rule24_record is a citation block (ratified_words, cvo_grades, cto_ratification, analysis_path, round_123_ruling), not a record. The enums new in this contract (coverage's 3 values; new_code_reason CODE_NOT_IN_MAPPING; unmapped_display Unclassified) have no postulates or census (W1301-S1, thin). Dismissed (7): D2-W1301-S1 (the thin citation, as above, for 0.2.0), D2-W1301-S2 (naming-gate warnings on firm literals, a question for the CTO), D2-W1302-S1..S5 (sparse cone; the order omitted tr_cd, which the producer requires; firm derived from the registry; trade legs unsigned; four per-code flow-class pairs).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W1301-S1",
   "IRPT_DASHBD-D2-W1301-S2",
   "IRPT_DASHBD-D2-W1302-S1",
   "IRPT_DASHBD-D2-W1302-S2",
   "IRPT_DASHBD-D2-W1302-S3",
   "IRPT_DASHBD-D2-W1302-S4",
   "IRPT_DASHBD-D2-W1302-S5"
  ],
  "spec_asserts": "A value must carry its claim and the claim must be true; ABSENT is not EXERCISED-AGAINST. CTO msg 8735 (one drain); CTO msg 8841 (S103 disarms with the L9). Rule 24.",
  "world_is": "Contract 0.1.0 (served false) and an unwired producer, both on trunk. Seven of their twelve firm-column absences are contradicted by the live sources; round 128 re-measures and 0.2.0 amends.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T07:0xZ at HEAD fbbaf7758e: DBF127-1-AC1, AC2, DBF127-2-AC1, AC2 PASS; round-close-check --round 127 --workstream ~F2 MAY-CLOSE",
    "org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json 0.1.0: claim absent on settle_date, asset_name, fee, source_txn_id; rule24_record keys ratified_words, cvo_grades, cto_ratification, analysis_path, round_123_ruling",
    "read-only schema of opal-data-assets schwab/08335338/silver/fact_trn/date=2026-10-14: 140 columns; fee columns exchange_processing_fee, broker_service_fee, prime_broker_fee, trade_away_fee, redemption_fee, other_fee, step_in_fee, research_fee; commission, exec_brok_comm; id columns schwab_cashiering_unique_id, cashiering_transaction_identifier; no column containing 'settle' or 'security'",
    "ADJUDICATION_v130.md (Cottonwood and Inflection transaction silver column census)",
    "git show -s --format=%cI: 94d8b2ff60 06:31:12Z, af8468b4b8 06:58:12Z",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R127_F.md @92695738aa blob 62afa30910 (msg 9151)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Seven INERT worker rows, each carried into the 0.2.0 amendment. The false absent claims are the round's standing defect, and the slug names it; S102, S103, S106 and S107 remain ARMED."
 }
]
```
