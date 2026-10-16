# IRPT_DASHBD: CVO adjudication, round 128 (workstream F-SHIP, ~F2): the ground read with source reads, and Cottonwood's words re-cut

<sweep_watermark>2026-10-16T07:33Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T07:33Z, on msg 9168 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R128_F.md`, resolved by git log -1 on the path to de137c96f3, blob f6a51fc9a2). Two LOCAL record orders: TO-DB-f-1401 (merged da3f781d93) and TO-DB-f-1402 (merged 11555369b0), both in HEAD. No judgment criterion. Re-run on trunk (HEAD 3832e62b2b): DBF128-1-AC1, DBF128-2-AC1, DBF128-2-AC2 PASS; round-close --round 128 --workstream ~F2 MAY-CLOSE. This seat recounted the Cottonwood codes from the source itself (read-only, code values and counts only). No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S72",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T07:33:00Z",
  "one_line": "Round 128 F-SHIP (~F2). DID IT READ S3? Yes, but through the issuer, not the worker. The three records' 'reads' field is null, so the records do not show source objects opened. The S3 read is the issuer's census R128_LIVE_SOURCE_CENSUS_3FIRMS.json (read ~06:40Z), and its denominators equal this seat's own reads exactly: 49F fact_trn 572 partitions, 3,349,750 rows, 140 columns; Cottonwood fact_transactions 125 objects, 1,096,830 rows, 73 columns; Inflection fact_transactions 154 partitions, 218,054,352 rows, 36 columns. AGAINST v130 AND v133, PER FIRM. COTTONWOOD: agree, all 14 fillable (R128: 10 sourced + 4 computed; v130: 12 by column + 2 derived). The split differs only in whether action and fee count as sourced (Action, Transaction Fee) or computed (from the type; Transaction Fee + Account Fee); no contradiction. INFLECTION: agree, settle_date and fee absent, custodian and asset name present (custodianName, productName). 49 FINANCIAL: R128 IS RIGHT AND v133 WAS WRONG ON ONE COLUMN. settle_date is sourced from settlmnt_date. v133 searched the 140 names for 'settle' and missed the abbreviation. v133's count of contradicted absences was therefore 8 of 12, not 7. Fee (nine fee columns) and source_txn_id (cashiering_transaction_identifier) agree with v133; asset_name stays absent. COTTONWOOD WORDS RE-CUT, RULE 24. GRAIN: the finer grain, the 33 live (Transaction Type, Transaction Sub Type) pairs for the type word and the 87 Action values for the action word, not the 16 Types (v130's finding answered). (i) MECE, by subtraction recounted here over all 125 objects (1,096,830 rows): 33 live pairs, 33 mapped, 0 missing, 0 extra, 0 double cover; 87 live Actions, 87 mapped, 0 missing, 0 extra, 0 double cover. 2 pairs UNMAPPED (Expense | Buy of Accrued Interest, Interest | Buy of Accrued Interest) and 7 Actions UNMAPPED, each with a reason. (iii) ONE INTENT holds under the CTO's round-124 ruling that the flow class belongs to the code, here the line: External Flow decides each line (Contribution EXTERNAL_IN, Withdrawal EXTERNAL_OUT) and None takes the pair's class. Four pairs mix lines (Buy | Buy 264,042 None / 3,489 Contribution; Sale | Sale 150,336 / 932 Withdrawal; Expense | Expense 12,757 / 3,124 Withdrawal; Transfer Out | Transfer Out 25 None / 4,738 Withdrawal); each line still gets one class. W1402-S2 asks the CTO what the 25 None lines of Transfer Out carry. Dismissed (3): D2-W1402-S1 (Tax withheld per-code EXTERNAL_OUT, consistent with the ruling), D2-W1401-S1 (client-data list absent on dell2, the recorded WARN-only disposition), D2-W1401-S2 (sparse worktree). D2-W1402-S2 held for the ratification.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W1402-S1",
   "IRPT_DASHBD-D2-W1401-S1",
   "IRPT_DASHBD-D2-W1401-S2"
  ],
  "spec_asserts": "ABSENT is not EXERCISED-AGAINST; rule 24 (i) by subtraction from a printed denominator over the live population; the CTO's round-124 ruling (flow class per code).",
  "world_is": "Records only; nothing served. The three-firm ground now rests on a live census. Cottonwood's re-cut covers its live codes exactly once at pair and action grain and awaits ratification.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T07:2xZ at HEAD 3832e62b2b: DBF128-1-AC1, DBF128-2-AC1, AC2 PASS; round-close-check --round 128 --workstream ~F2 MAY-CLOSE",
    "RD_FWD5_GROUND_{49FINANCIAL,COTTONWOOD,INFLECTION}_R128.json: reads null; 49F settle_date source settlmnt_date (measured), absent [asset_name]; Cottonwood absent []; Inflection absent [settle_date, fee]",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/R128_LIVE_SOURCE_CENSUS_3FIRMS.json (read_by, read_at_utc; contains settlmnt_date)",
    "this seat's read-only recount of opal-data-assets blackdiamond/cottonwood/silver/fact_transactions/: 125 objects, 1,096,830 rows, 33 (Type, Sub Type) pairs, 87 Action values; subtraction against FWD5_WORDS_COTTONWOOD_R128.json: 0 missing, 0 extra, 0 double cover; External Flow mixed in 4 pairs",
    "v128, v130 and v133 (this seat's earlier counts)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R128_F.md @de137c96f3 blob f6a51fc9a2 (msg 9168)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Three INERT worker rows. W1402-S2 is held for the CTO; this row also corrects v133's settle_date reading for 49 Financial."
 }
]
```
