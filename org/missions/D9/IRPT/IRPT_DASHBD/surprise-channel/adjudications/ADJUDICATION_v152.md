# IRPT_DASHBD: CVO adjudication, the Cottonwood 20-row J sample on contract 0.5.1 (round 138); S103 and S107 DISARMED

<sweep_watermark>2026-10-17T06:47Z</sweep_watermark>

**Basis.** L9 grade, dispositions and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-17T06:47Z, on msg 10364. The packet is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R138_COTTONWOOD_J.md` @ce4643c238. This is the sample v151 (row C-S89) asked for. Trunk HEAD is c830f3eb58. Read-only S3 GETs; no client value below.

**The figure files.**
- The untracked, git-ignored file `org/mcp/drive_ticks/J1_SAMPLE_COTTONWOOD_R138.json` hashes df731f30de8d.
- The committed hashed form hashes f82eff29c105.
- Both equal the packet.

**Criterion id.** No task order carries a criterion id for this sample: it was cut on the CTO's word (msg 10351), not by an order. It is graded here under the name **COT-J-R138**, the sample owed by C-S89. `round-close-check.py` cannot count it.

**L9 -- COT-J-R138: PASS** (Cottonwood, 20 of 20), by natural key: account, Trade Date, `type | sub type | action`, symbol, units, amount.
- **Census, full domain (this seat's):** 126 `fact_transactions` partitions, 1,105,342 rows; 37,792 rows in 18,658 non-unique keys. These equal the packet's.
- **Uniqueness:** each of the 20 sampled keys is unique in its own partition. No row locator was used.
- **Source blocks:** every sample source block equals the live row.
- **Re-derivation:** all 19 columns re-derive from the live row and contract 0.5.1 (schema hash ac652e2f71b18427), 20 of 20, 0 field mismatches.
- **`business_date_claim`:** 19 rows read measured and 1 reads inferred, the rolled line. That line's `business_date` is the first NYSE trading day after its Trade Date.
- **Padded Actions:** 4 rows carry a blank-padded Action, the forced one included. All 4 keep `source_action_raw` byte-equal to the source and map to a non-null action, coverage MEASURED.

**The consequence.** All three firms now carry an L9 PASS on contract 0.5.1, which is unchanged since:
- 49 Financial: DBF136-1-J2 (v146);
- Inflection: DBF136-1-J1 (v146);
- Cottonwood: COT-J-R138 (this file).

S103's disarm line (S107; CTO msg 8841) holds, so **S103 and S107 are DISARMED.**

**Limits, as the packet states.** The sample grades the PRODUCER on real source rows. It does not grade the Lambda stage that calls it (DB-f-2605 and DB-f-2606, not deployed), and nothing is written at the Cottonwood `account_transaction` prefix yet.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S91",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-17T06:47:00Z",
  "one_line": "L9 COT-J-R138 (the Cottonwood 20-row J sample owed by C-S89; no order carries a criterion id) PASS, 20 of 20 on contract 0.5.1: unique natural keys, every source block equal, all 19 columns re-derive; business_date_claim 19 measured and 1 inferred (the rolled line); 4 padded Actions keep source_action_raw and map. Full census 126 partitions, 1,105,342 rows, 37,792 in 18,658 non-unique keys (equal to the packet's).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-C-S89"],
  "spec_asserts": "C-S89: S103 disarms on one Cottonwood 20-row J sample graded PASS on contract 0.5.1, natural key, unique-key rows, business_date_claim included.",
  "world_is": "Sample df731f30de8d (untracked) / hashed f82eff29c105 (committed), seed 138, n 20, contract 0.5.1. CVO grader over s3 blackdiamond/cottonwood/silver/fact_transactions/ (126 partitions): 20 of 20 unique matches, 20 of 20 every field equal; claims 19 measured, 1 inferred; padded Actions 4 of 4 raw kept and MEASURED.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "sha256 org/mcp/drive_ticks/J1_SAMPLE_COTTONWOOD_R138.json df731f30de8d; deliverables/2.0.0_SA_COO~F2/J1_SAMPLE_COTTONWOOD_R138_HASHED.json f82eff29c105",
    "CVO grader (read-only S3 GETs) in census mode against org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json 0.5.1; counts and field names only"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "PASS: the owed Cottonwood sample passes on the current contract."
 },
 {
  "id": "IRPT_DASHBD-D2-C-S92",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-17T06:47:00Z",
  "one_line": "DISARMS IRPT_DASHBD-D2-S103: the transaction contract (0.5.1) and the three per-firm producers have landed with an L9 PASS each on 0.5.1 -- 49F DBF136-1-J2, Inflection DBF136-1-J1 (v146), Cottonwood COT-J-R138 (v152).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-S103", "IRPT_DASHBD-D2-C-S89"],
  "spec_asserts": "S103's disarm line (S107, CTO msg 8841): the transaction contract and the per-firm producers land with their L9.",
  "world_is": "Contract 0.5.1 (schema_hash ac652e2f71b18427) on trunk; three producers on trunk; L9 PASS for each firm on 0.5.1.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "ADJUDICATION_v146.md (DBF136-1-J1, DBF136-1-J2 PASS on 0.5.1)",
    "row IRPT_DASHBD-D2-C-S91 in this file (COT-J-R138 PASS on 0.5.1)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "DISARMED: the disarm condition holds for all three firms. Not covered: the Lambda stages that call the producers and the first writes, which are later pairs."
 },
 {
  "id": "IRPT_DASHBD-D2-C-S93",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-17T06:47:00Z",
  "one_line": "DISARMS IRPT_DASHBD-D2-S107 (S103's disarm line) with S103: its condition, the contract and per-firm producers committed and graded at L9, holds for all three firms on 0.5.1.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_DASHBD-D2-S107", "IRPT_DASHBD-D2-C-S90"],
  "spec_asserts": "S107 DISARMS WHEN: IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json and the per-firm producer are committed and the CVO has graded the cell that landed them (L9).",
  "world_is": "As C-S92.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "row IRPT_DASHBD-D2-C-S92 in this file"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "DISARMED with S103."
 }
]
```
