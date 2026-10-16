# IRPT_DASHBD: CVO adjudication, round 123 (workstream F-SHIP, ~F2): the FWD-5 49 Financial producer ground read

<sweep_watermark>2026-10-16T04:43Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T04:43Z, on msg 9054 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R123_F.md` @cd716684d7, blob 0ea190e7c4). Not B-49F's or B-IN's round 123. One LOCAL read order, TO-DB-f-901 (worker ~901; merged 33ef71b10d, in HEAD). No judgment criterion. Re-run on the landed tree (HEAD 23001ba328): DBF123-1-AC1 PASS; round-close --round 123 --workstream ~F2 MAY-CLOSE. No live read in the round (the address probe is the builder's output, rc 0, not an AWS call). No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S65",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T04:43:00Z",
  "one_line": "Round 123 F-SHIP (~F2): a read of what the 49F transaction producer can stand on. DENOMINATORS AND CLAIMS: the record prints its denominator (14 brief targets, absent_count 7), and every target carries a claim (5 measured, 2 inferred, 7 absent). One claim-form gap: custodian (a firm constant) and flow_class and coverage (derived) are labelled 'absent', because the record's claim set has no 'derived' value (row W901-S2). A consumer reading 'absent' would wrongly drop three columns the producer can fill. The two inferred targets (action from tr_cd, txn_type from sb_cd) are superseded by the CTO's msg 9036 at tran_srcde grain, as the packet says. FOR ROUND 124: this read does NOT give it the 157-code denominator. The record names tran_srcde only to rule it out as a transaction id, citing 157 distinct values from the CRO table via the round-120 record; it lists no codes and maps none. Round 124 must print its own denominator, and the population is the codes 49F's silver actually carries, not only the 2026-08-11 CRO table (187 rows, 157 codes): a code first seen after that date would be uncovered and invisible to a subtraction over the table (rule 24 (i), falsify the domain first). Dismissed (4): D2-W901-S1 (the round-120 column list omitted trade_date, order_number, quantity, net_amount), D2-W901-S2 (the claim-form gap above, the issuer's checker to improve), D2-W901-S3 (the brief's seven flow classes against the code's five finals, open for the contract), D2-W901-S4 (the builder accepts a gold table with no registry row, so a missing row cannot surface as a refusal). All INERT.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W901-S1",
   "IRPT_DASHBD-D2-W901-S2",
   "IRPT_DASHBD-D2-W901-S3",
   "IRPT_DASHBD-D2-W901-S4"
  ],
  "spec_asserts": "A value must carry its claim in a field a consumer can reject on; rule 24 (i): subtraction from a printed denominator whose domain is the claim's population.",
  "world_is": "A read record; nothing served. The new gold prefix it scopes is a never-widen act (write list and the single PutObject statement), not yet cut.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T04:4xZ at HEAD 23001ba328: DBF123-1-AC1 PASS; round-close-check --round 123 --workstream ~F2 MAY-CLOSE",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~901/RD_FWD5_PRODUCER_GROUND_R123.json: 14 targets, claims measured 5 / inferred 2 / absent 7; tran_srcde named once (as not a transaction id, '157 distinct values measured in RD_F...')",
    "org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json: 187 rows, 157 distinct tran_srcde (read for v124)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R123_F.md blob 0ea190e7c4 (msg 9054)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Four INERT read observations, each an input to the contract cell; the claim-form gap and round 124's denominator go to the CTO in the slug."
 }
]
```
