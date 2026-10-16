# IRPT_DASHBD: CVO adjudication, round 130 (workstream F-SHIP, ~F2): contract 0.3.0 and the Cottonwood producer; J1 withheld

<sweep_watermark>2026-10-16T09:25Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T09:25Z, on msg 9242 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R130_F.md` @adc4bba6ac, blob 068bb28ca1). One order, TO-DB-f-1601, merged in ONE drain b8e715772b (09:15:41Z), in HEAD. Re-run on trunk (HEAD 3f1713ff36): DBF130-1-AC1, AC2, AC3 PASS. DBF130-1-J1 is WITHHELD by the issuer and NOT GRADED here. No remediation row.

**The round is NOT MAY-CLOSE while DBF130-1-J1 is ungraded.** round-close-check reads REFUSED today (orders=1, judgment=1, ungraded=1), but that is not what decides it. Row NFRA_CTLPLN-D2-S6 records that the gate reads MAY-CLOSE once a verdict word exists, even a FAIL, so the gate cannot be relied on here. This round closes only on a J1 PASS from a fresh, defect-free sample.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S74",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T09:25:00Z",
  "one_line": "Round 130 F-SHIP (~F2): 3 of 3 mechanical PASS; J1 withheld; NOT MAY-CLOSE. (1) THE DEFECT, REPRODUCED here on live data (read-only, vendor codes and counts only). Cottonwood fact_transactions has 125 objects, 1,096,830 rows and 87 distinct Action values. 3 of the 87 carry trailing whitespace: 'Buy Money Market ', 'CREDIT - ', 'OTHER - '. They sit on 126,835 rows, 11.6 percent of the table, not a rare edge. The ratified mapping keys all 3 exactly as spelled, and none of them once stripped. Run on a live row whose Action is 'CREDIT - ', the producer's own _classify returns (UNMAPPED, None, UNRESOLVED, CODE_NOT_IN_MAPPING): at._text strips the Action before the lookup, so the lookup misses. The fix belongs in round 131 with a checker that runs every live Action and pair through the producer. (2) NOT MAY-CLOSE: the judgment is ungraded; see the header and NFRA_CTLPLN-D2-S6. (3) NOTHING SERVED OR WIRED: the gold account_transaction prefix is empty in both opal-data-cottonwood and opal-data-49financial (read-only), and no Lambda source under infra/aws/lambda names the producer. (4) ONE DRAIN: met; b8e715772b carries contract 0.3.0 with both producers. (5) source_txn_id, CTO msg 9193 item 4: MET. The column's meaning states a PER-ROW present/absent claim and never a universal key. source_txn_id_coverage gives each firm all-partition coverage with its denominator: 49F cashiering_transaction_identifier 214,587 of 3,349,750 (6.41 percent, 572 partitions, 5,167 rows repeating within a partition); Cottonwood TransactionID 1,096,830 of 1,096,830 (3,870 repeating); Inflection id 218,054,352 of 218,054,352. Dismissed (5): D2-W1601-S1 (sparse folders), S2 (checker reason text), S3 (TransactionID repeats; now stated in the coverage), S4 (the calendar fallback, as W226-S1), S5 (naming-gate WARN on firm literals, a question for the CTO).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W1601-S1",
   "IRPT_DASHBD-D2-W1601-S2",
   "IRPT_DASHBD-D2-W1601-S3",
   "IRPT_DASHBD-D2-W1601-S4",
   "IRPT_DASHBD-D2-W1601-S5"
  ],
  "spec_asserts": "Spine L9: a round with a judgment criterion closes only when the CVO has graded it; CTO msg 8735 (one drain); CTO msg 9193 item 4 (source_txn_id per-row claim and per-firm coverage).",
  "world_is": "Contract 0.3.0 and two producers are on trunk, unwired, nothing served. The Cottonwood producer misclassifies 11.6 percent of Cottonwood rows (three trailing-space Actions) as CODE_NOT_IN_MAPPING.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T09:2xZ at HEAD 3f1713ff36: DBF130-1-AC1, AC2, AC3 PASS; round-close-check --round 130 --workstream ~F2: orders=1 judgment=1 ungraded=1 REFUSED",
    "this seat's read-only read of opal-data-assets blackdiamond/cottonwood/silver/fact_transactions/: 125 objects, 1,096,830 rows, 87 distinct Action; 3 with edge whitespace on 126,835 rows; the mapping keys them as spelled",
    "account_transaction_cottonwood.py _classify (line 130): act_word = at._text(rec['Action']); run on a live 'CREDIT - ' row: CODE_NOT_IN_MAPPING",
    "s3api list-objects-v2 KeyCount None for opal-data-cottonwood irpt/cottonwood/gold/account_transaction/ and opal-data-49financial irpt/49financial/gold/account_transaction/; Grep 'account_transaction' under infra/aws/lambda: no files",
    "org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json 0.3.0: source_txn_id meaning (PER-ROW CLAIM) and source_txn_id_coverage per firm",
    "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row NFRA_CTLPLN-D2-S6",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R130_F.md @adc4bba6ac blob 068bb28ca1 (msg 9242)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Five INERT worker rows. The Action defect is the issuer's own stated finding, reproduced here; its fix is round 131's. J1 stays ungraded and the round stays open."
 }
]
```
