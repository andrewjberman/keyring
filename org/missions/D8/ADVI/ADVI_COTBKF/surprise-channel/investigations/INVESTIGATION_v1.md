# ADVI_COTBKF -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~C` at the L5 cut (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`).
Lane `ANY`.
**Id grammar:** a worker's row is `ADVI_COTBKF-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that coordinate); a seat's row
is `ADVI_COTBKF-S<k>`; the CVO's adjudication rows live in `../adjudications/` as `ADVI_COTBKF-C-S<k>`. **Append-only during the
round.** Never edit an existing row.

## ADVI_COTBKF-S1 -- the PRD's thread names a transactions zip and a performance zip; the delivery has one zip carrying both

```json
{
  "id": "ADVI_COTBKF-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-06T18:12Z",
  "one_line": "The PRD's round-1 thread lands 'the transactions zip and the performance zip'; the delivery carries ONE portfolio-accounting zip holding the transactions, performance and positions files, so round 1 lands that one zip.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python zipfile over %USERPROFILE%/Downloads/Files.zip (3,218,239,946 bytes): five members -- CRM_CottonwoodCapitalAdvisors.zip, Cottonwood Capital Advisors_Portfolio_Accounting_Performance_ClientDelivery.zip, HKE.zip, HJH.zip, 4XF.zip",
      "the portfolio-accounting zip (23,833,956 bytes, sha256 a3a2772efa3447fd3adaa4b6eb5dacdf400667743c4f4040e2d0cad3296d658b) holds three members under CFN_SCTASK0548380_Portfolio_Accounting_Performance/: Historical_Positions (48,610 bytes), Historical_Transactions (308,186,603), Historical_Performance_TWR_Cumulative_NetofFees (8,513,299)",
      "brief F1 (docs/briefs/cottonwood-commonwealth-10y-backfill-brief-20261006.md:110) already lists one zip, 3 pipe-delimited files"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.3 section 2 hop 2: 'The transactions zip and the performance zip are uploaded from Andrew's Downloads to bronze, with the manifest'.",
  "world_is": "There is one zip for both (and positions); the decomposition lands that one zip in round 1. No outcome changes: FWD-1 needs only the transactions member.",
  "notes": "A wording difference in the thread, not in the ENDPOINT; the CTO may fold it into the next addendum. The decomposition cites this row."
}
```

## ADVI_COTBKF-W1-S1 -- the commit naming gate refuses the order's literal scope 'cottonwood'; the tool reads it through lookup()

```json
{
  "id": "ADVI_COTBKF-W1-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~1",
  "surfaced_at": "2026-10-06T19:00Z",
  "one_line": "Order item 3 types address('commonwealth','cottonwood',...); the LGIC naming gate (ENFORCE) refused the literal 'cottonwood' in commonwealth_landing.py, so the scope is read as lookup('cottonwood')['long'] -- same value, same keys.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit naming-gate output: NAMING REFUSE data/assets/scripts/bronze/commonwealth_landing.py:22 cottonwood -> lookup('cottonwood'); :23 commonwealth/cottonwood -> commonwealth/cot",
      "address('commonwealth','cottonwood','bronze','portfolio_accounting','date=2026-06-23') = s3://opal-data-assets/commonwealth/cottonwood/bronze/portfolio_accounting/date=2026-06-23 (builder output at base 0b5d303674); lookup('cottonwood')['bucket'] = opal-data-cottonwood, a different home than the builder returned for source 'commonwealth'",
      "dry run on the real zip at 09d7ad4ea2: LANDING-PLAN bytes=23833956 sha256=a3a2772efa3447fd3adaa4b6eb5dacdf400667743c4f4040e2d0cad3296d658b keys=2 builder=OK apply=False"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-a-1 item 3: the scope argument is the literal 'cottonwood'; the bucket the issuer will apply to is whatever the builder returns.",
  "world_is": "The gate wants the scope read through the registry; the keys are unchanged. Separately the builder's bucket for source 'commonwealth' is opal-data-assets while the tenant registry row names opal-data-cottonwood; the issuer should read the printed s3 address before --apply.",
  "notes": "The manifest's bronze_key holds the full s3:// address the builder returned (the order did not fix the form)."
}
```

## ADVI_COTBKF-W2-S1 -- the 3 extra physical lines are line breaks inside quoted fields; 1,360 exact-duplicate records are dropped, so silver rows_out is 1,415,137 not 1,416,497

```json
{
  "id": "ADVI_COTBKF-W2-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~2",
  "surfaced_at": "2026-10-06T19:20Z",
  "one_line": "Order CB-a-2 called the 3-line gap (1,416,501 physical lines vs the brief's 1,416,497 rows) unexplained: measured, it is 3 quoted fields holding a CRLF; and 1,360 of the 1,416,497 records are exact 20-column duplicates, so the silver table holds 1,415,137 rows.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python csv over the member (Historical_Transactions_20260623_102751.txt, 308,186,603 bytes, inner zip sha256 a3a2772efa3447fd3adaa4b6eb5dacdf400667743c4f4040e2d0cad3296d658b): physical=1416501 header=1 record_first_lines=1416497 continuation_lines=3 blank=0 unexplained=0; the continuation lines are 156037, 156039, 156041 (Transaction_Note quoted with an embedded CRLF); every record parses at exactly 20 fields",
      "the same pass: dropped_dup=1360 (records identical in all 20 vendor columns; first occurrence kept), rows_out=1415137; accounts=1533, min_trade=2013-04-03, max_trade=2026-06-22 (the brief's span and account count hold)",
      "run line: SILVER-TRANSACTIONS lines=1416501 rows_out=1415137 dropped_dup=1360 blank=0 unexplained=0 accounts=1533 columns=24 min_trade=2013-04-03 max_trade=2026-06-22 lineage_sample=50/50 (data/assets/scripts/silver/commonwealth_transactions.py on branch wk-ADVI_COTBKF-2, base 9180968a4c)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-a-2 THE CELL: 'The 3-line difference is unexplained'; the brief's 1,416,497 rows are the row count a downstream cell may compare against.",
  "world_is": "The 3 lines are continuation lines of 3 records (no blank line, no trailer). The record count is 1,416,497 as the brief says, but the silver table keeps 1,415,137 after the order's own rule 'de-duplicate only rows identical in all 20 vendor columns'; a downstream count check against 1,416,497 must add dropped_dup=1,360 (or the lineage source_line shows which lines were dropped: a dropped duplicate's line is absent from silver).",
  "notes": "No criterion changes: CB2-AC2 asserts unexplained=0, accounts, columns, span and sample, not rows_out. The dropped lines are recoverable from the member by line number only through the first occurrence; the duplicate lines' numbers are not stored."
}
```

## ADVI_COTBKF-S2 -- no single account spans 2013 to 2026: every 2013 account ends by 2017-12-29, the longest history is 10.4 years from 2016-01

```json
{
  "id": "ADVI_COTBKF-S2",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-06T19:40Z",
  "one_line": "FWD-1 reads one account's history '2013 to June 2026'; in the delivered transactions no account spans both years -- the 311 accounts trading in 2013 all stop by 2017-12-29, and the longest single-account history is 10.4 years (2016-01-25 to 2026-06-22), so a 2013-2026 client history needs the old-to-new account link across a 2016-2017 break.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "boto3+pyarrow over s3://opal-data-assets/commonwealth/cottonwood/silver/transactions/date=2026-06-23/ (14 partitions, 1,415,137 rows): 1,533 accounts; first trade in 2013: 311; last trade in 2026: 769; both: 0",
      "the 311 accounts whose first trade is in 2013: latest last trade 2017-12-29; 0 of them trade after 2020-12-31",
      "distinct accounts per trade year: 2013 311, 2014 348, 2015 381, 2016 768, 2017 465, 2018 489 ... 2025 810, 2026 769 (2016 roughly doubles: an overlap year)",
      "longest spans: D49141617 2016-01-25 to 2026-06-22 (3,532 rows), 0QF879095, 0QF879142, E1202062, B3S605728 (all from 2016-01-2x); span quantiles p50 2.82y, p90 10.32y, max 10.41y",
      "the account-number form differs across the break: 2013 rows carry 11-digit numbers (01001355831, 00074413503); the 2016+ long histories carry alphanumeric ones (D49141617, 0QF879095)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.3 FWD-1: 'An analyst picks one Cottonwood account and reads its whole transaction history, 2013 to June 2026, from Opal's own store'.",
  "world_is": "Read per account number, the store holds at most 10.4 years for one account; the 2013-2017 history sits under different account numbers. FWD-1 was exercised on D49141617 (2016-01-25 to 2026-06-22, three rows traced); the full 2013 span for one client needs an old-number to new-number link, which the delivery may carry (the CRM files, round 3) or which FWD-8's crosswalk must build.",
  "notes": "Cause INFERRED, not shown: a custodian or platform conversion around 2016-2017 renumbered accounts. Not read: whether the CRM export or the positions file links old and new numbers. Bronze keeps every byte, so nothing is lost; this is a read-path question for the CTO's round-1 analysis (FWD-1's wording, or FWD-8 moving up the backlog)."
}
```

## ADVI_COTBKF-S3 -- the transactions file holds 1,416,497 records on 1,416,500 lines; v0.4's "1,416,500 rows" and "2 unexplained" count lines, not records

```json
{
  "id": "ADVI_COTBKF-S3",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-06T19:55Z",
  "one_line": "PRD v0.4 addendum item 1 rebuilds silver 'with all 1,416,500 rows' and names '2 unexplained'; the file holds 1,416,497 records (3 records each span two physical lines), so the full rebuild is 1,416,497 rows and no row is unexplained -- the 2 come from counting lines instead of records.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python over the member read from %USERPROFILE%/Downloads/Files.zip: split on LF, 1,416,500 physical data lines, 1,415,139 distinct, 1,361 line-level repeats",
      "csv.reader(delimiter='|') over the same bytes: 1,416,497 records, every one exactly 20 fields, 1,415,137 distinct, 1,360 record-level repeats",
      "the 6 physical lines that are not a whole 20-field record: 156036+156037, 156038+156039, 156040+156041 -- three Dividend Received rows of account B3S688184 (2023-12-28) whose quoted Transaction_Note carries a CRLF; the tails 156037 and 156039 are the identical text 'Adjusted to LO Date\"|2026-06-23', which is the line-level 1,361 vs record-level 1,360",
      "silver as written (CB-a-2 @04ca7e3556): rows_out 1,415,137 = 1,416,497 records - 1,360 record-level repeats; unexplained=0 (worker row ADVI_COTBKF-W2-S1)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.4 addendum item 1: 'Silver transactions is rebuilt with all 1,416,500 rows and the source line on each; the 2 unexplained rows are named.'",
  "world_is": "Every delivered record is 1,416,497 rows; the 1,360 record-level repeats are what v0.4 restores. A three-record continuation is one row each, carrying its FIRST physical line as source_line. The recut's criterion is rows_out=1416497 dropped_dup=0.",
  "notes": "Confirms v0.4's ruling (keep every row); corrects only its count. Owner of the PRD text: 1.0.0_SA_CTO, before 3.0.0_SA_CVO re-signs the ratified-text half."
}
```
