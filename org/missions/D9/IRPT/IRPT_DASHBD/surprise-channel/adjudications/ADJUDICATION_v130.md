# IRPT_DASHBD: CVO adjudication, round 126 (workstream F-SHIP, ~F2): the FWD-5 ground read for Cottonwood and Inflection

<sweep_watermark>2026-10-16T06:31Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T06:31Z, on msg 9123 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R126_F.md`, resolved by git log -1 on the path to 9dae125095, blob 52cef65b3c). Not B-IN's or B-49F's round 126. One LOCAL read order, TO-DB-f-1201 (worker ~1201; merged 9b8819798d, in HEAD). No judgment criterion. Re-run on the landed tree (HEAD 7ca5a414dc): DBF126-1-AC1 PASS; round-close --round 126 --workstream ~F2 MAY-CLOSE. This seat read both firms' transaction silver itself, read-only, column names and counts only. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S68",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T06:31:00Z",
  "one_line": "Round 126 F-SHIP (~F2): THE RECORDS' ABSENCES ARE ABSENT, NOT EXERCISED-AGAINST. Both records report s3_reads 0: 'sourced' means 'read by today's code', not 'held by the source'. Read here, the sources hold far more. COTTONWOOD: s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_transactions/ has 125 objects in 125 partitions, 2026-03-09..2026-10-15, 1,096,830 rows, 73 columns. It carries Settle Date, Action (87 distinct), Symbol, Ticker, CUSIP, Asset Name, Units, Price, Transaction Fee (169 distinct), Custodian and TransactionID (100,258 distinct), besides Trade Date, Transaction Type (16) and Market Value. So of the record's 11 Cottonwood 'absent' targets, 9 have a source column (settle_date, action, symbol, asset_name, units, price, fee, custodian, source_txn_id). Only flow_class and coverage remain, and the producer derives both. The record's 3 of 14 is a statement about the adapter; by the source, Cottonwood can fill 12 of 14. INFLECTION: s3://opal-data-assets/orion/inflection/silver/fact_transactions/ has 154 objects in 154 partitions, 2026-05-12..2026-10-15, 218,054,352 rows (a pull_date per row, so likely repeated snapshots: a row count, not a transaction count), 36 columns. It also carries custodianName (custodian) and productName (a candidate for asset_name), and has no settle date and no fee column. So of its 7 'absent' targets, custodian is sourced, asset_name is a candidate, settle_date and fee are truly absent, and action, flow_class and coverage are derived. CODE FIELD FOR FWD-5's WORDS: both firms carry one. Cottonwood has Transaction Type (16 values, the ratified 16-row table), plus Transaction Sub Type (31) and Action (87). Inflection has transTypeId / transactionDescription (47 distinct live; the ratified table has 48 rows). So the vocabulary reaches both. But Cottonwood repeats 49F's v124 lesson: the words map the coarse Type (16) while a finer Sub Type (31) and Action (87) exist. The ratification should say whether Type is the right grain there, and the Inflection 47-versus-48 needs a reason. Dismissed (2): D2-W1201-S1 (the seven Inflection columns the pull names and the adapter does not read; confirmed and widened above), D2-W1201-S2 (no gold code reads the Inflection transactions silver; true, and the silver exists).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W1201-S1",
   "IRPT_DASHBD-D2-W1201-S2"
  ],
  "spec_asserts": "ABSENT is not EXERCISED-AGAINST (CLAUDE.md rule 22 corollary): an 'absent' claim needs the source it was tested against. Rule 24 (i): the domain is the source's population.",
  "world_is": "Read records only; nothing served. Both firms' transaction silver is live and current to 2026-10-15 and holds most of the brief's columns. The packet's proposal not to cut those producers 'until its source widens' rests on the code's view, not the source's.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T06:2xZ at HEAD 7ca5a414dc: DBF126-1-AC1 PASS; round-close-check --round 126 --workstream ~F2 MAY-CLOSE",
    "records RD_FWD5_GROUND_COTTONWOOD_R126.json and RD_FWD5_GROUND_INFLECTION_R126.json: reads.s3_reads 0 each",
    "this seat's read-only census (boto3 list + pyarrow schema and column projection, counts only): Cottonwood fact_transactions 125 partitions 2026-03-09..2026-10-15, 1,096,830 rows, 73 columns incl. Settle Date, Action, Symbol, CUSIP, Asset Name, Units, Price, Transaction Fee, Custodian, TransactionID; Inflection fact_transactions 154 partitions 2026-05-12..2026-10-15, 218,054,352 rows, 36 columns incl. custodianName, productName, transTypeId (47 distinct), no settle or fee column",
    "data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py: SILVER_ROOT blackdiamond/cottonwood/silver/, ALLOWED_TABLES includes fact_transactions; inflection_account_dim.GRANTED_PREFIXES includes s3://opal-data-assets/orion/inflection/",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R126_F.md @9dae125095 blob 52cef65b3c (msg 9123)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two INERT worker rows, both confirmed by this seat's source read; the corrected column counts and the grain question go to the CTO in the slug."
 }
]
```
