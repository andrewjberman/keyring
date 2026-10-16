# IRPT_DASHBD: CVO adjudication, round 132 (workstream F-SHIP, ~F2): one business date for three firms, the fund-only price, contract 0.4.1, with J1 and J2

<sweep_watermark>2026-10-16T14:58Z</sweep_watermark>

L8 compile, L9 grades and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T14:58Z, on msg 9383 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R132_F.md` @4eccf6649d, blob 91b98de6ce). One order, TO-DB-f-1801, merged in one drain 37e4f1bee7, in HEAD. Re-run on trunk (HEAD 73244659e7): DBF132-1-AC1, AC2, AC3 PASS.

SAMPLES AND CLIENT DATA:
- The figure-bearing samples (org/mcp/drive_ticks/R132_SAMPLE_49F_20ROWS.json, R132_SAMPLE_INFLECTION_20ROWS.json) are untracked and git-ignored.
- The committed hashed forms (J1_SAMPLE_INFLECTION_R132_HASHED.json, J2_SAMPLE_49F_R132_HASHED.json) and R132_F49_BUSINESS_DATE_CENSUS.json hold no money-like numeric field. Their one long digit run is a census row count, not a client figure.
- Nothing below carries a client value.

All AWS reads are read-only, counts only. No remediation row.

**L9 -- DBF132-1-J1: PASS** (Inflection, 20 of 20), by natural key over Complete rows (CTO msg 9193).
- **Census, scoped:** this seat's census was SCOPED to the 20 sampled rows' own partitions (20 of 155): 24,959,171 Complete rows, 134,332 rows in 61,844 non-unique keys. The FULL 155-partition census was NOT RUN to completion by this seat (stopped after about 75 minutes). ~F2's full count (1,043,390 of 192,697,735 in 480,463 keys) is the issuer's, unreproduced here.
- **Uniqueness and source blocks:** each sampled key is unique in its own partition, 20 of 20, and every source block equals the live row.
- **Every contract field re-derives,** 20 of 20, including the fund-only price (navPrice only where a fund family, units and a positive navPrice are present).
- **The rolled line (row 13):** business_date is the next NYSE trading day by an independent day-by-day walk of lib/trading_calendar.py, and trade_date keeps the transDate as received.

**L9 -- DBF132-1-J2: PASS** (49 Financial, 20 of 20), by natural key.
- **Census, full:** recounted over ALL 573 partitions: 3,354,885 rows, 21,236 rows in 10,027 non-unique keys (equal to ~F2's).
- **Uniqueness and source blocks:** 20 of 20 keys are unique in partition, and every source block equals the live row.
- **Every contract field re-derives,** 20 of 20.
- **The rolled line (row 4):** business_date rolls to the next trading day; trade_date is kept as received, and source_action_raw is the code as received.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S79",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T14:58:00Z",
  "one_line": "Round 132 F-SHIP (~F2): AC1..AC3 PASS. L9 DBF132-1-J1 PASS, 20 of 20 (Inflection; census scoped to the sampled rows' 20 of 155 partitions, 134,332 rows in 61,844 non-unique keys of 24,959,171; full census not run here). L9 DBF132-1-J2 PASS, 20 of 20 (49F; full census over 573 partitions, 21,236 rows in 10,027 non-unique keys of 3,354,885). Each sample includes one rolled line that rolls to the next trading day, with the original date kept in trade_date. THE 49F MOVE, recounted over all 573 partitions: 296 of 3,354,885 rows have a business_date other than the first trading day on or after their trade date, all in partition 2025-01-09 (the NYSE closed that day, and the source stamps it as the business date). No served number moves: the account_transaction gold prefix is empty in all three firm buckets and the contract reads served false, so no never-widen act is owed yet. CLAIM GAP: contract 0.4.1 marks business_date 'measured' with no method, but on a rolled line it is computed (the roll); it should read inferred with business_date_rule as its method, while trade_date stays measured. RULINGS: all four of v140's held decisions now carry CTO rulings. (a) Complete-only STANDS, with the Reversed-offset census: msg 9342 ruling 1. (b) fund-only price: msg 9342 ruling 2. (c) one business date for all three firms: msg 9342 ruling 3. (d) S6, both legs INTERNAL, RULED FINAL and DISARMED: msg 9382 (round-131 analysis ADDENDUM 2). Dispositions: W1801-S1 to S7 accepted. S4 (BLOCKING) was the issuer's checker defect, amended at 247989c493, and AC3 passes here; S5, a null noUnits counted ZERO_UNITS, is consistent with the price rule.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W1801-S1",
   "IRPT_DASHBD-D2-W1801-S2",
   "IRPT_DASHBD-D2-W1801-S3",
   "IRPT_DASHBD-D2-W1801-S4",
   "IRPT_DASHBD-D2-W1801-S5",
   "IRPT_DASHBD-D2-W1801-S6",
   "IRPT_DASHBD-D2-W1801-S7"
  ],
  "spec_asserts": "Spine L9; CTO msg 9193 (natural key, unique within the row's own partition, census printed, no locator); CTO msg 9342 rulings 1 to 3 and msg 9382 (S6); a value must carry its claim.",
  "world_is": "Contract 0.4.1 and three producers on one business-date rule, on trunk, unwired and unserved; both samples equal the source on unique-key rows.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T14:xxZ at HEAD 73244659e7: DBF132-1-AC1, AC2, AC3 PASS",
    "J2 grader (read-only): 49F census 573 partitions, 3,354,885 rows, 21,236 in 10,027 non-unique keys; 20 of 20 unique and matching every field; row 4 rolled",
    "J1 grader (read-only, census scoped): 20 of 155 partitions, 24,959,171 Complete rows, 134,332 in 61,844 non-unique keys; 20 of 20 unique and matching every field; row 13 rolled",
    "49F business-date recount (read-only): 573 objects, 3,354,885 rows, 296 move, 0 null trade dates, all in date=2025-01-09",
    "s3api list-objects-v2 KeyCount None for irpt/<firm>/gold/account_transaction/ in opal-data-49financial, opal-data-cottonwood, opal-data-inflection",
    "org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json 0.4.1: business_date claim measured, no method; business_date_rule first_trading_day_on_or_after",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_131_20261016.md rulings 1 to 4 and ADDENDUM 2 (msgs 9342, 9382)",
    "git ls-files / check-ignore: the hashed samples tracked, the figure samples ignored"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Seven INERT worker rows, the BLOCKING one cured by the issuer's checker amendment. The business_date claim gap goes to the CTO in the slug."
 }
]
```
