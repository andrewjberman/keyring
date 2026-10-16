# IRPT_DASHBD: CVO adjudication, round 129 (workstream F-SHIP, ~F2): transaction contract 0.2.0 and the 49F producer, with the J1 grade

<sweep_watermark>2026-10-16T08:29Z</sweep_watermark>

L8 compile, L9 grade and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T08:29Z, on msg 9190 and its addendum msg 9196 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R129_F.md` @6076819f41, addendum @b360d88b09, blob 968ab3c0d0). One order, TO-DB-f-1501, merged in ONE drain 23d33fc60b (contract 0.2.0 and the producer revision together), in HEAD. Re-run on trunk (HEAD 76f207a312): DBF129-1-AC1, AC2, AC3 PASS.

The J1 sample is `org/mcp/drive_ticks/R129_SAMPLE_49F_20ROWS.json`. It is untracked and git-ignored, it holds client figures, and it is not committed or quoted here. It is the REDRAWN file: every row carries natural_key_values and id_usable, and there is no locator field. Everything below gives row indexes and field names only. No remediation row.

**L9 -- DBF129-1-J1: PASS, 20 of 20,** graded by natural key per the CTO's ruling (msg 9193), which supersedes the criterion's 'by the source's own id'. This seat read every one of the 572 49F fact_trn partitions itself (read-only). The natural key is account_id, trade_date, tran_srcde, ticker_symbol, quantity and gross_amount.

- **Duplicate census (49F):** 3,349,750 rows; 21,194 rows sit in 10,007 non-unique keys. This equals ~F2's census exactly.
- **Each sampled key is unique in its partition:** 20 of 20, all gradable.
- **The sample's 'source' block equals the live row** on every field, for 20 of 20.
- **Every contract field, re-derived from the live row and the contract:**
  - trade_date, business_date, settle_date (settlmnt_date), units, price: 20 of 20.
  - fee, the sum of commission and the eight fee columns of fee_basis: 20 of 20.
  - txn_type and action, by source_mapping and type_action: 20 of 20.
  - flow_class and coverage: 20 of 20.
  - custodian: 20 of 20, as the lower-cased custdian_id ('SCHWAB' to 'schwab').
  - symbol: 20 of 20, the 7 empty source symbols written null.
  - source_txn_id: 20 of 20, the 4 empty source ids written null; the one row with a usable id matches it.
  - amount magnitude: 20 of 20.
  - amount sign: follows debit_credit on the 9 cash (tr_cd FC) rows, and the 11 TR and IC rows stay unsigned, as the contract states.
- **Unstated in 0.2.0:** two normalisations the producer makes, lower-casing the custodian and writing an empty string as null. They are correct and should be written into the contract.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S73",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T08:29:00Z",
  "one_line": "Round 129 F-SHIP (~F2). DBF129-1-AC1..AC3 PASS. L9 DBF129-1-J1 PASS, 20 of 20 by natural key (CTO msg 9193). The census reproduced here: 3,349,750 rows, 21,194 in 10,007 non-unique keys. All 20 sampled keys are unique in their partition, every source block equals the live row, and every contract field re-derives from the source and the contract. Two unstated normalisations: custodian lower-cased; empty symbol or id written null. CONTRACT 0.2.0 fixes all 8 absences that v133/v134 found contradicted (49F settle_date, fee and source_txn_id; Cottonwood all four; Inflection source_txn_id and asset_name). The absences left are true: 49F asset_name; Inflection settle_date and fee. NOT YET MET (CTO msg 9193 item 4): source_txn_id has no per-row present/absent claim and no per-firm coverage with its denominator (49F 2.3 / 6.8 / 14.8 percent over 66,596 rows); 0.2.0 carries a column-level 'inferred' only, owed in the next amendment. ONE DRAIN: met (23d33fc60b carries contract and producer). S103: PARTLY MET, NOT DISARMED. S107's condition is the contract plus the per-firm producers with their L9; this round lands the contract and the 49F producer with a PASSing L9, but Cottonwood and Inflection have no producer, so S102, S103, S106 and S107 stay ARMED. Rows W1501-S1..S6 accepted as dispositioned in the packet: sparse folders; the flow-class key note; fee_basis in the data file; two round-127 test items; a census label; the Transfer Out reason text fixed before the merge.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W1501-S1",
   "IRPT_DASHBD-D2-W1501-S2",
   "IRPT_DASHBD-D2-W1501-S3",
   "IRPT_DASHBD-D2-W1501-S4",
   "IRPT_DASHBD-D2-W1501-S5",
   "IRPT_DASHBD-D2-W1501-S6"
  ],
  "spec_asserts": "Spine L9: a judgment criterion graded on the artifacts. CTO msg 9193: natural-key comparison, unique-key rows only, the duplicate count printed, the locator refused, source_txn_id coverage stated per firm. CTO msg 8735 (one drain); CTO msg 8841 (S103's disarm).",
  "world_is": "Contract 0.2.0 and the 49F producer are on trunk, unwired and unserved; the producer's output equals the source on a 20-row unique-key sample. Cottonwood and Inflection producers do not exist.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T08:2xZ at HEAD 76f207a312: DBF129-1-AC1, AC2, AC3 PASS",
    "this seat's read-only read of all 572 partitions of opal-data-assets schwab/08335338/silver/fact_trn/: 3,349,750 rows; 21,194 rows in 10,007 non-unique natural keys",
    "J1 grader (scratchpad, counts and field names only): 20 of 20 keys unique in partition; source_block_fields_differing [] on 20; field differences only custodian (case), symbol and source_txn_id (empty to null); amount sign per debit_credit on the 9 FC rows",
    "org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json 0.2.0 sources: 49F settle_date settlmnt_date, fee inferred, source_txn_id cashiering_transaction_identifier, asset_name absent; Cottonwood Settle Date, Asset Name, fee inferred, TransactionID; Inflection settle_date absent, asset_name productName, fee absent, source_txn_id id; no per-firm source_txn_id coverage",
    "org/mcp/drive_ticks/R129_SAMPLE_49F_20ROWS.json: untracked, git-ignored (git check-ignore), not committed",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R129_F.md @b360d88b09 blob 968ab3c0d0 (msgs 9190, 9196)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Six INERT worker rows dispositioned in the packet and consistent with this grade. The source_txn_id coverage gap and S103's partial state go to the CTO in the slug."
 }
]
```
