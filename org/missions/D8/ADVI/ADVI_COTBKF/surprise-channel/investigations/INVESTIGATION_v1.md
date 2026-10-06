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
