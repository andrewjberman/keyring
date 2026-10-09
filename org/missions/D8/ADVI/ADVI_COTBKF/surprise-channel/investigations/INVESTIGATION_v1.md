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

## ADVI_COTBKF-W7-S1 -- two commit gates refused correct code on name shape (a `build_*` function returning a list; a "silver/%s" label); renamed, tests untouched

```json
{
  "id": "ADVI_COTBKF-W7-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~7",
  "surfaced_at": "2026-10-06T20:30Z",
  "one_line": "commit-gate's silver-ids check demanded coerce_silver_ids() on a function named build_rows that returns a list of dicts, and the naming gate refused a human-readable source_file label 'silver/%s' as an out-of-pattern S3 key; both were name-shape false positives, so the function became coverage_rows and the label '<table> table'.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit run 1: commonwealth_coverage.py:130 BLOCKED: build function 'build_rows' returns DataFrame but missing coerce_silver_ids() call -- build_rows returns list[dict], no DataFrame",
      "safe-commit run 2: NAMING REFUSE commonwealth_coverage.py:139 silver/%s -> {source}/{scope}/silver/%s (NEW and OUT-OF-PATTERN as S3Key)",
      "commit 815db65dbc passes both gates after the two renames; 9 tests passed before and after"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-b-4 names no function names or labels; the worker expected the generator to commit as written.",
  "world_is": "The silver-ids check keys on a build_ name prefix, not on a DataFrame return; the naming gate grades any slash-bearing literal shaped like a key.",
  "notes": "Assumption INFERRED, not measured: the generator counts distinct accounts on Account_Number in all three tables and falls back to ReportingPeriod or the reporting_period partition; the real performance and positions silver (CB-b-2) was not read, so the issuer's real run should confirm those column names (distinct_accounts=0 would show a miss)."
}
```

## ADVI_COTBKF-W6-S1 -- the G4 security_market series holds 4 date partitions (2026-09-29 to 2026-10-05), not about 730 days, and none falls inside the needed window

```json
{
  "id": "ADVI_COTBKF-W6-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~6",
  "surfaced_at": "2026-10-06T22:20Z",
  "one_line": "The order names security_market as a Bloomberg-derived series of about 730 days; the prefix holds 4 date partitions, all after 2026-06-23, so it prices 56 universe CUSIPs on 0 needed days.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python boto3 list_objects_v2(Bucket=opal-data-etfs, Prefix=rivalfunds/etfs/gold/security_market/, Delimiter=/) -> 4 CommonPrefixes",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~6/PRICE_COVERAGE_20261006.json: store etfs.rivalfunds.gold.security_market priced_any=56 security_days_covered=0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-b-3: 'the G4 security_market series at s3://opal-data-etfs/rivalfunds/etfs/gold/security_market/ (Bloomberg-derived, about 730 days)'.",
  "world_is": "list_objects_v2 over the prefix returns 4 date partitions (date=2026-09-29, 2026-10-01, 2026-10-02, 2026-10-05; 3,023 rows read, 76 rows on 56 universe CUSIPs). The ~730-day depth sits in sibling G4 prefixes (canonical_shape 505 and flow_reconciliation 504 partitions), which are not price series. Covered security-days inside the needed window: 0.",
  "notes": "Read as a CUSIP-keyed store (security_id); the 56 matches are CUSIP matches, the only CUSIP-keyed store found."
}
```

## ADVI_COTBKF-W6-S2 -- the daily price series the order's starting points did not name live in the bd, inf and cot firm buckets

```json
{
  "id": "ADVI_COTBKF-W6-S2",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~6",
  "surfaced_at": "2026-10-06T22:20Z",
  "one_line": "The stored daily price series that cover the Commonwealth securities are canonical_prices.parquet and historical_prices.parquet in opal-data-bd, opal-data-inf and opal-data-cot, none of them among the order's named starting points; this cell reads only their date, ticker, price and source columns.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "boto3 head/read of schema: silver/prices/canonical_prices.parquet in opal-data-bd, opal-data-inf, opal-data-cot; silver/historical_prices.parquet in opal-data-bd, opal-data-inf",
      ".tools/ds-precommit-check.py lines 69-72: _CROSS_FIRM_FOREIGN_BUCKETS covers data/black_diamond/ and data/cot/ only",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~6/PRICE_COVERAGE_20261006.json: by_source split per store (yahoo_finance, linear_interpolation, transaction_observed)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-b-3: known starting points are security_market, the Bloomberg derived layer and the Yang pickles; the stores are to be found by census. The estate rule keeps bd and cot separate firms and forbids a pipeline tree referencing another firm's bucket (gate .tools/ds-precommit-check.py _CROSS_FIRM_FOREIGN_BUCKETS, homes data/cot/ and data/black_diamond/ only).",
  "world_is": "Census found 3 canonical_prices files (bd 12,570,765 rows, inf 1,455,147, cot 11,291,021) and 2 historical_prices files (bd 5,868,653, inf 4,927,223); with sources yahoo_finance, linear_interpolation, transaction_observed. The script sits under data/assets/scripts/analysis/, outside both gated homes, and reads three columns of each. Whether opal-data-cot is the same firm as the commonwealth/cottonwood tenant was not resolved by this cell. The transaction_observed rows are prices taken from a firm's own transactions.",
  "notes": "Nothing was written to any bucket. Whether a Commonwealth price read from another firm's bucket is acceptable for the daily-return build is for the CTO and CVO; the result file carries per-store numbers so the choice can be applied after the fact."
}
```

## ADVI_COTBKF-W6-S3 -- 103 universe symbols are claimed by more than one CUSIP; a ticker match on them is reported and not credited

```json
{
  "id": "ADVI_COTBKF-W6-S3",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~6",
  "surfaced_at": "2026-10-06T22:20Z",
  "one_line": "The order asks that a ticker match on a reused symbol be reported as such; this cell does not credit it as priced, so coverage is a floor on those securities and the credit left out is printed beside each store.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~6/PRICE_COVERAGE_20261006.json: universe.symbols_claimed_by_more_than_one_cusip=103; per store total.ticker_reused_not_credited and ticker_reused_days_not_credited",
      "data/assets/scripts/analysis/tests/test_commonwealth_price_coverage.py::test_reused_symbol_is_reported_not_credited"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-b-3: 'matches a security to a store by CUSIP, else by ticker (Symbol)' and a test that 'a ticker match on a reused symbol is reported as such' (the order does not say whether such a match counts as priced).",
  "world_is": "103 Symbols are listed by more than one of the 4,634 CUSIPs. In bd canonical_prices 126 securities match a store ticker only through such a symbol (121,421 security-days not credited); inf 61 (25,741); cot 126 (120,287); bd historical 120 (158,988); inf historical 114 (151,979); bbg-testpull 18 (10,602). Crediting them would raise union coverage; the amount is the sum of those columns per store, with overlap.",
  "notes": "The choice (not credited) is the cautious one for an UNPRICED claim; flipping it is one branch in match_security()."
}
```

## ADVI_COTBKF-W6-S4 -- the first read of the nine stores takes 5 to 19 minutes; criterion CB2b3-AC2 meets its 120-second bound only against a primed cache under .scratch/

```json
{
  "id": "ADVI_COTBKF-W6-S4",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~6",
  "surfaced_at": "2026-10-06T22:20Z",
  "one_line": "Reading the three 100 MB-class price files from S3 took 5m24s (parallel) and 18m43s (first serial run); CB2b3-AC2 ran in 8s only because the filtered per-store cache sits at .scratch/price_cache/ in worker ~6's worktree.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "time of the cold parallel run: real 5m23.7s (.scratch/run1.time); first serial cold run: real 18m43.4s",
      "time timeout 120 python data/assets/scripts/analysis/commonwealth_price_coverage.py: real 0m8.1s, rc 0, last line PRICE-COVERAGE universe=4634 stores_checked=22 stores_with_prices=7 ..."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-b-3 BOUNDS: 'Within 120 seconds for CB2b3-AC2: cache what you read under .scratch/ and let the script read the cache when present.'",
  "world_is": "Uncached the script reads about 36 million rows over S3 (bd canonical 12.6M, cot canonical 11.3M, bd historical 5.9M, inf historical 4.9M, inf canonical 1.5M). The cache (.scratch/ is uncommitted) is not in the commit, so AC2 re-run in any other tree, or after this worktree is removed, ends at rc 124 on a cold run. Cached run: 7.8s real, rc 0.",
  "notes": "A grader or the COO re-running AC2 in a clean tree should run the script once without the timeout (about 5.5 minutes) and then under it, or pass --cache-dir to a copy of C:/Users/AndrewBerman/Desktop/wk-advi-cotbkf-6/.scratch/price_cache. The criterion's output is also recorded in the proof instance."
}
```

## ADVI_COTBKF-W6-S5 -- the naming gate refuses the legacy store addresses the cell reads; the census is a record file the script loads

```json
{
  "id": "ADVI_COTBKF-W6-S5",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~6",
  "surfaced_at": "2026-10-06T22:40Z",
  "one_line": "The commit naming gate refused 41 literals when the script typed the legacy bucket and key addresses of the stores it reads, so the store census is kept as a record file the script reads, and the universe address comes from address().",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit naming limb (ENFORCE) on the first commit: NAMING-GATE: REFUSE 41 graded, e.g. commonwealth_price_coverage.py:52 opal-data-bd -> opal-data-49financial (hand-kept carrier), :53 silver/prices/canonical_prices.parquet -> {source}/{scope}/silver/prices/canonical_prices.parquet (OUT-OF-PATTERN)",
      ".tools/naming-gate.py docstring lines 21-29: a firm token is graded unless inside key()/address()/name()/lookup() arguments; files graded are .py .js .mjs .ts .tf .json .yaml .yml outside org/ and docs/; prose strings and */tests/* are not graded",
      "lookup('49financial')['bucket'] is opal-data-49financial, a different bucket from the opal-data-bd that holds silver/prices/canonical_prices.parquet today (the legacy buckets stay active until the D14 full-name migration)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-b-3 reads stored price series at their existing locations; CLAUDE.md rule 30 says every address and name comes from the builders, and a builder refusal is a missing registry row.",
  "world_is": "The existing stores sit at pre-LGIC bucket and key layouts the builders do not produce, and the registry lookup returns a different bucket than the one holding the data. The script therefore reads the census (location, reader spec, verdict for 22 stores) from org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~6/PRICE_COVERAGE_STORES_20261006.json, a record under org/ that the gate does not grade; only the universe address comes from address(). No registry row was added and no override was used.",
  "notes": "Whether the census record or a registry row per legacy store is the right carrier is for the CTO; the migration project (rule 30, R19) removes the legacy locations. A later round that writes to any of these stores must use the builders."
}
```

## ADVI_COTBKF-S4 -- W6-S4's hazard disarmed by its owner: the primed price cache now sits in the shared tree, and AC2 re-runs in 8 s there

```json
{
  "id": "ADVI_COTBKF-S4",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T00:04Z",
  "one_line": "Disarm act for ADVI_COTBKF-W6-S4 (ARMED, disarm_owner 2.0.0_SA_COO~C): the price-coverage read's primed cache (.scratch/price_cache, 7.3 MB) was copied from the worker's worktree into the shared tree before the worktree's removal, and CB2b3-AC2 re-run there under timeout 120 passes in 8.4 s with the identical line.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "cp -r C:/Users/AndrewBerman/Desktop/wk-advi-cotbkf-6/.scratch/price_cache .scratch/ (7.3M) in the shared tree, 2026-10-07 ~00:0xZ, after the merge of the CB-b-3 branch @382f450319",
      "timeout 120 python data/assets/scripts/analysis/commonwealth_price_coverage.py in the shared tree: rc 0, real 8.356 s, last line PRICE-COVERAGE universe=4634 stores_checked=22 stores_with_prices=7 priced_any=1506 security_days_covered=2090953 security_days_needed=9388961 (identical to the worker's AC2 output)",
      "the script's default --cache-dir is <repo>/.scratch/price_cache (commonwealth_price_coverage.py:415), so a re-run in the shared tree reads the copy with no flag"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-b-3 BOUNDS: CB2b3-AC2 runs within 120 seconds; row W6-S4 (ARMED): a re-run in a clean tree ends rc 124 unless run once without the timeout or given --cache-dir.",
  "world_is": "The cache that makes AC2 meet its bound now lives where a grader runs (the shared tree's untracked .scratch/, device-local, never committed). A clean tree on another device still needs one cold run (5-19 minutes) first; that residue is stated, not hidden. W6-S4's own disposition is the CVO's at L9.",
  "notes": "The cache is a local accelerator, not a store: it is never committed and nothing reads it but this script."
}
```

## ADVI_COTBKF-W8-S1 -- the sequential read of the 14 transactions files takes 217 s and misses the 120 s bound; a threaded fetch takes 78 s

```json
{
  "id": "ADVI_COTBKF-W8-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~8",
  "surfaced_at": "2026-10-07T01:02Z",
  "one_line": "The 14-file, 29.4 MB silver transactions read took 217 s serially (about 135 KB/s) and ended CB3c1-AC2 at rc 124 under timeout 120; fetching the 14 files on 14 threads brings it to 78 s, a 42 s margin under the bound.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "first run of python data/assets/scripts/analysis/commonwealth_price_need.py (sequential get_object per file) under timeout 120: rc 124 after 120.5 s",
      ".scratch/prof.py: read_transactions() sequential real 217.5 s for 1,416,497 rows in 14 parquet files; .scratch/prof2.py: one 796,687-byte file 15.5 s to download, 0.35 s to parse with the 3-column projection",
      "after the ThreadPoolExecutor change in read_transactions(): real 1m18.3s, rc 0, last line PRICE-NEED securities=4634 security_days_total=3421735 equity=1453884 etf=331153 fund=752921 fixed_income=688679 other=195098"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-c-1 BOUNDS: 'Within 120 seconds for CB3c1-AC2 (column projection; round 2's full-table reads took under 60 s).'",
  "world_is": "On this device today the S3 download dominates (parse is 0.35 s per file); sequential reads exceeded the bound. The shipped script downloads the files in parallel and passes with 42 s to spare, but the time is network-bound, so a slower link can still exceed 120 s. Nothing is cached and no test or criterion was weakened.",
  "notes": "Column projection here is applied after the whole file is fetched (get_object then pq.read_table on bytes); ranged column reads would cut the 29.4 MB download but are not needed to meet the bound today."
}
```

## ADVI_COTBKF-W9-S1 -- the real archives list every PDF, hold no orphan listing row, and place PDFs flat in the type folder

```json
{
  "id": "ADVI_COTBKF-W9-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~9",
  "surfaced_at": "2026-10-07T01:00Z",
  "one_line": "TO CB-c-2 expects unlisted PDFs and listing rows with no PDF; the real run found none of either (listed=11119 unlisted=0 listing_rows_without_pdf=0), PDFs sit flat at TYPE/<name>.pdf (not in rep folders), and listings name them as .PDF or with a bare trailing dot.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python data/assets/scripts/silver/commonwealth_document_index.py --source $HOME/Downloads/Files.zip --outer HKE.zip HJH.zip 4XF.zip --data-date 2026-06-23 --out .scratch/advi_cotbkf/document_index, rc 0, 45 s: DOCUMENT-INDEX archives=3 listings=51 pdfs=24489 accounted=24489 unique_documents=11119 listed=11119 unlisted=0 listing_rows_without_pdf=0",
      "listing rows read: HKE 11054 (11033 PDFs), HJH 11021 (11000), 4XF 2456 (2456); every row matched a PDF of its own archive by (type, extension-less lower-cased name)",
      "overlap: 8464 documents in 2 archives (HKE+HJH), 2453 in 3, 116 HKE only, 83 HJH only, 3 4XF only (the brief's 10,917 HKE/HJH and 2,453 4XF-in-both)",
      "7 listing layouts read from the files: ADVS DocName/FolderName/Keyword; CLNT DocumentType/Account/ClientName; NCSD DocumentName/Folder/HouseholdName; QSMT StmtDate/HHName/NumberOfPages (0 rows); REPR DocType/DocName/NumberOfPages; STMT Acct/DisplayName/StmtDate; TXRP AccountNumber/ReportName/Year/DisplayName/NumberOfPages"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-c-2 says a listing may not cover every PDF (a first STMT listing held 5 rows against 7,724 STMT PDFs) and asks that unlisted PDFs and absent-file listing rows be kept.",
  "world_is": "The 5-row listing was one of nine STMT listings; across all 51 the listings cover every PDF and every row finds its file. The unlisted and present=False branches are built and unit-tested on fixtures but are exercised by no real row. The vendor ReadMe's no-extension rule is needed: listings say .PDF (NCSD: a trailing dot), the zips say .pdf. TXRP and QSMT carry no per-document date (TXRP has a tax Year, kept in listing_fields), so doc_date for ADVS, CLNT, NCSD, REPR and TXRP is the file-name timestamp (date_source=file_name), and REPR NumberOfPages is a literal W (page_count null, raw kept). Where two archives' listing rows for one document disagree, the first non-empty value in archive order is kept; that conflict count was not measured.",
  "notes": "Whether TXRP should carry the tax year as its doc_date is for the issuer; the builder keeps it in listing_fields."
}
```

## ADVI_COTBKF-W10-S1 -- The current holdings files carry no CUSIP before June and no ticker on the May lines, and the earliest dated lines of a new account carry no units; th

```json
{
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~10",
  "surfaced_at": "2026-10-07T01:45Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "ADVI_COTBKF-W10-S1",
  "one_line": "The current holdings files carry no CUSIP before June and no ticker on the May lines, and the earliest dated lines of a new account carry no units; the join falls back to the asset name's CUSIP and 'first holdings' reads the earliest date with a quantity.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3://opal-data-cot/gold/canonical/holdings/ (130 files, 2026-04-22 to 2026-10-05), columns read per file: cusip is null on 100% of the 2026-04 and 2026-05 lines, 16.7% of 2026-06, about 2.7% after; the first populated date of account z0926757531 is 2026-05-26 and its 18 lines there carry units with ticker and cusip both null (asset_name only)",
      "first-dated lines of accounts opened on 2026-06-08 (z0927183571) list the securities with units null until a later date; 968 of 994 accounts have a quantity-bearing line, 97 of them on a date after their earliest listing",
      "commonwealth_crosswalk.py name_cusip_map + current_first_holdings; the first cut that dropped the name-only lines matched 34 of 1,533, the cut that resolves them through the asset_name's single CUSIP matches 439"
    ]
  },
  "spec_asserts": "CB-c-3 worker face: R2 matches the Commonwealth holdings to 'a current account's FIRST holdings (its earliest holdings date) on the same CUSIPs'.",
  "world_is": "The holdings table has a cusip column only in later files, and the earliest dated lines carry no quantity, so a literal CUSIP join on the literal earliest date returns almost nothing. Applied: a current line takes its cusip, else the CUSIP its asset_name carries on every other line that has one (names with two CUSIPs excluded), else its ticker; first holdings = the earliest date on which the account has units populated and non-zero. Both are printed in the script docstring and the RULE lines.",
  "notes": "Whether the holdings producer should backfill cusip on the April-June files is for its owner; the crosswalk reads what is served."
}
```

## ADVI_COTBKF-W10-S2 -- For an account that left in kind, its literal holdings at its last activity are flat; 'holdings as it left' is read as the holdings immediately before

```json
{
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~10",
  "surfaced_at": "2026-10-07T01:45Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "ADVI_COTBKF-W10-S2",
  "one_line": "For an account that left in kind, its literal holdings at its last activity are flat; 'holdings as it left' is read as the holdings immediately before its last in-kind withdrawal day.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "639 of 1,533 accounts rebuild to no security position with last activity on or after 2026-04-22; their last lines are Transaction_Type lo ('Withdrawal from Asset', Amount 0.00) on non-cash CUSIPs, e.g. B3S782653 on 2026-05-20",
      "validation of the signed rebuild on the real 2026-06-23 positions: 381 of 381 security (account, CUSIP) pairs equal within 0.001 (REBUILD-CHECK line of the run)",
      "an account matched this way: B3S717438 -> z0927158721, 17 of 17 positions equal within 0.001 (evidence column of crosswalk.csv)"
    ]
  },
  "spec_asserts": "CB-c-3 worker face R2: 'its holdings at its last activity rebuilt from its transactions' (for an account without 2026-06-23 positions).",
  "world_is": "Read literally, the net at last activity is zero for exactly the accounts that transferred out in kind, so none could match. Applied: for an account whose full rebuild leaves no security position and which has lo/trfo lines on non-cash CUSIPs, the holdings as it left = the rebuild without the lines dated its last such day (basis REBUILT_BEFORE_IN_KIND_OUT_<date> in every row); every other account uses the plain rebuild.",
  "notes": "The Transaction_Type signs (+ by li trfi dvr lica ci TRFIR licar 12b1 CAF QA CAE; - sl lo trfo loca DVRX) were fitted to the 2026-06-23 positions; CAF, QA, CAE, DVRX have few lines, so the 381 of 381 is partly in-sample."
}
```

## ADVI_COTBKF-W10-S3 -- The first read of the current-side inputs and the transactions takes about 8 minutes; CB3c3-AC2 meets its 120-second bound (5.6 s) only against the co

```json
{
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~10",
  "surfaced_at": "2026-10-07T01:45Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "ADVI_COTBKF-W10-S3",
  "one_line": "The first read of the current-side inputs and the transactions takes about 8 minutes; CB3c3-AC2 meets its 120-second bound (5.6 s) only against the column-projected cache under .scratch/advi_cotbkf/cache.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "cache files mtime 2026-10-06 20:52 (holdings, accounts, positions) and 20:55 (transactions) after a 20:47 start: about 8 minutes cold, 130 holdings files plus 14 transactions parts; a holdings re-read took about 5 minutes",
      "time timeout 120 python data/assets/scripts/silver/commonwealth_crosswalk.py --out .scratch/advi_cotbkf/crosswalk: real 0m5.5s, rc 0, CROSSWALK commonwealth_accounts=1533 every_account_listed=True matched=439 not_matched=1094 ambiguous=36 by_rule=R2-in-kind-transfer:439; a second run's csv is byte-identical"
    ]
  },
  "spec_asserts": "CB-c-3 BOUNDS: 'Within 120 seconds for CB3c3-AC2 (cache reads under .scratch/ and let the script read the cache when present).'",
  "world_is": "The cache (.scratch/, uncommitted, about 19 MB) sits in worker ~10's worktree; AC2 re-run in any other tree or after this worktree is removed ends rc 124 on a cold run. The script writes the cache on a cold run and reads it when present (--cache overrides the location).",
  "notes": "Disarm as the issuer did for W6-S4: copy C:/Users/AndrewBerman/Desktop/wk-advi-cotbkf-10/.scratch/advi_cotbkf/cache to the shared tree's .scratch/advi_cotbkf/ before the worktree's removal, or run once without the timeout (about 8 minutes)."
}
```

## ADVI_COTBKF-W10-S4 -- Of 1,533 Commonwealth accounts 439 are matched by R2, 36 are AMBIGUOUS (18 one-position accounts, and cv-prefixed twins of the same number), 263 hold 

```json
{
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~10",
  "surfaced_at": "2026-10-07T01:45Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "ADVI_COTBKF-W10-S4",
  "one_line": "Of 1,533 Commonwealth accounts 439 are matched by R2, 36 are AMBIGUOUS (18 one-position accounts, and cv-prefixed twins of the same number), 263 hold positions no current account's first holdings reproduce, 758 closed before 2026-04-22, 37 were flat.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "run output of CB3c3-AC2: not_matched reasons AMBIGUOUS 36, CLOSED_BEFORE_CURRENT_HISTORY 758, NO_CURRENT_ACCOUNT_HOLDS_POSITIONS 263, NO_SECURITY_POSITIONS 37; R1 matched 0 (no Commonwealth number equals a current z09... id)",
      "of the 263, 214 have no current account equal on any position by quantity and 49 have a best candidate scoring 0.05 to 0.786 (e.g. B3S606724 -> z0927980101 11 of 14 = 0.786, reason column of crosswalk.csv)",
      "ambiguous examples: 0QF878978 and RGY006839 both reach z0926741471 (19 of 21 = 0.905); cv0QF879181 and cv47440283 and 0QF879181 reach z0926724981"
    ]
  },
  "spec_asserts": "CB-c-3: every Commonwealth account is matched with its rule or listed not matched with the reason; no match is guessed.",
  "world_is": "The 80% bar at a 0.001 tolerance leaves near-matches (a mutual-fund line moved by a dividend between departure and arrival) listed NOT_MATCHED with the best candidate and score in the reason; none is applied. Single-position accounts match only when exactly one current account holds that quantity of that security and no second Commonwealth account claims it (46 matched, 18 ambiguous).",
  "notes": "Whether a looser, still exact rule (fund lines allowed a stated dividend drift) is wanted is the issuer's and the CTO's; this cell applies the rule as written."
}
```

## ADVI_COTBKF-W10-S5 -- The commit naming gate refused the three current-side locations the order names (bucket, accounts key, holdings prefix) as typed literals, so the scri

```json
{
  "id": "ADVI_COTBKF-W10-S5",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~10",
  "surfaced_at": "2026-10-07T01:55Z",
  "one_line": "The commit naming gate refused the three current-side locations the order names (bucket, accounts key, holdings prefix) as typed literals, so the script reads them from a location record in the deliverables folder; a commit gate also refused a build_ function that returns a tuple.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit naming limb (ENFORCE) on the first commit: commonwealth_crosswalk.py:64 opal-data-cot -> opal-data-cottonwood (ALIAS as S3_BUCKET: REFUSE); :65 gold/dimensions/accounts_dimension_latest.parquet and :66 gold/canonical/holdings/ OUT-OF-PATTERN as S3Key: REFUSE; NAMING-GATE: REFUSE 3 graded",
      "safe-commit ds-precommit: commonwealth_crosswalk.py:232 build function 'build_crosswalk' returns DataFrame but missing coerce_silver_ids() (it returns a tuple of rows and info); renamed crosswalk_rows, the same remedy as row W7-S1",
      "lookup('cottonwood')['aliases'] grades opal-data-cot as an ALIAS of opal-data-cottonwood with routed true; the data sits in the alias bucket today"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CLAUDE.md rule 30: every S3 address is address() output; a builder refusal is a missing registry row. TO CB-c-3 names the current-side bucket and keys as literals.",
  "world_is": "The current-side locations are pre-LGIC layouts the builders do not produce. The script reads bucket, accounts key and holdings prefix from org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~10/CURRENT_SIDE_LOCATIONS.json (org/ is not graded), the same carrier as row W6-S5; the Commonwealth silver addresses come from address(). No registry row was added and no override was used.",
  "notes": "Whether a registry row per legacy store or this record is the right carrier is for the CTO; the migration project (rule 30, R19) removes the legacy locations."
}
```

## ADVI_COTBKF-S5 -- W10-S3's hazard disarmed by its owner: the crosswalk's cache now sits in the shared tree, and AC2 re-runs in 6.3 s there

```json
{
  "id": "ADVI_COTBKF-S5",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T02:07Z",
  "one_line": "Disarm act for ADVI_COTBKF-W10-S3 (ARMED, disarm_owner 2.0.0_SA_COO~C): the crosswalk's read cache (.scratch/advi_cotbkf/cache, 19 MB) was copied from the worker's worktree into the shared tree before the worktree's removal, and CB3c3-AC2 re-run there under timeout 120 passes in 6.3 s with the identical line.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "cp -r C:/Users/AndrewBerman/Desktop/wk-advi-cotbkf-10/.scratch/advi_cotbkf/cache .scratch/advi_cotbkf/ (19M) in the shared tree, 2026-10-07 ~02:0xZ, after the merge of the CB-c-3 branch @384efdf29c",
      "timeout 120 python data/assets/scripts/silver/commonwealth_crosswalk.py --out .scratch/advi_cotbkf/crosswalk in the shared tree: real 6.275 s, last line CROSSWALK commonwealth_accounts=1533 every_account_listed=True matched=439 not_matched=1094 ambiguous=36 by_rule=R2-in-kind-transfer:439 (identical to the worker's AC2 output)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-c-3 BOUNDS: CB3c3-AC2 runs within 120 seconds; row W10-S3 (ARMED): the bound holds only against the worker's cache; a cold read takes about 8 minutes.",
  "world_is": "The cache that makes AC2 meet its bound lives where a grader runs (the shared tree's untracked .scratch/, device-local, never committed). A clean tree on another device still needs one cold run first; that residue is stated. W10-S3's own disposition is the CVO's at L9.",
  "notes": "Same disarm shape as row S4 (W6-S4)."
}
```

## ADVI_COTBKF-W11-S1 -- the TO's end-positions rule gives 455 of 459 old accounts an empty book (closed to cash); the build measures holdings just before the final in-kind exit

```json
{
  "id": "ADVI_COTBKF-W11-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~11",
  "surfaced_at": "2026-10-07T02:10Z",
  "one_line": "the TO's end-positions rule gives 455 of 459 old accounts an empty book (closed to cash); the build measures holdings just before the final in-kind exit",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "script run on the cached table: first the literal rule (run1), then the add-back (.scratch/run2.txt, rerun as the AC2 invocation, ACCOUNT-LINKS old_accounts=459 every_old_account_listed=True linked=180 not_linked=279 ambiguous=13 chains=5)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-c-4 link rule: 'A's holdings at its end (rebuilt from A's own transactions up to its last trade) are moved in kind into B'; reason 'closed to cash' for an account that sold out.",
  "world_is": "A rebuild through the last trade is empty after the move, because the move itself is a `lo` (Withdrawal from Asset) or trfo/trco row on each CUSIP at the last trade (account cvB3S605688 ends 2016-02-04 with 100+ lo rows). Literal run: 455 of 459 old accounts 'closed to cash', 4 'no in-kind receiver', 0 linked (.scratch/run1.txt). The build adds back the in-kind exit rows (lo/trfo/trco on a non-cash CUSIP) dated within 10 trading days before the last trade, so the positions are those held just before the exit; an account with no such rows is rebuilt as is and stays 'closed to cash' (90 of 459). Result: linked 180, not_linked 279 (ambiguous 13, below threshold 77, closed to cash 90, no in-kind receiver 99). The add-back is a reading of 'moved in kind', not the TO's words; CB3c4-AC3 grades it."
}
```

## ADVI_COTBKF-W11-S2 -- a chain is followed only through OLD accounts: 46 of the 148 non-old link targets stopped trading before 2026-01-01, and their own replacements are not in this table

```json
{
  "id": "ADVI_COTBKF-W11-S2",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~11",
  "surfaced_at": "2026-10-07T02:10Z",
  "one_line": "a chain is followed only through OLD accounts: 46 of the 148 non-old link targets stopped trading before 2026-01-01, and their own replacements are not in this table",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "pandas read of .scratch/advi_cotbkf/account_links/account_links.parquet against the cached table: last trade per LINKED target not in the old set; 46 below 2026-01-01, 56 below 2026-06-01"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-c-4: 'every OLD account gets exactly one row ... a chain (A -> B -> C) is followed and printed as the client's line.'",
  "world_is": "Rows exist for the 459 old accounts only, so a chain continues only where B is itself an old account (5 chains of three accounts, e.g. cvB3S606716 -> B3S606716 -> 0QF886265). Of the 176 distinct LINKED targets, 148 are not old accounts; 46 of those have a last trade before 2026-01-01 (earliest B3S606708, 2018-01-03), so a client line that ends at such a B may continue to a later account this table does not test. The rule is not applied to non-old accounts, because the TO gives them no row and a row for them would break 'exactly one row per old account'."
}
```

## ADVI_COTBKF-W11-S3 -- AC2 meets its 120-second bound only against a primed cache: the cold run took 89.5 s here, and a pyarrow S3 read of the 14 files failed with a network error on threads

```json
{
  "id": "ADVI_COTBKF-W11-S3",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~11",
  "surfaced_at": "2026-10-07T02:10Z",
  "one_line": "AC2 meets its 120-second bound only against a primed cache: the cold run took 89.5 s here, and a pyarrow S3 read of the 14 files failed with a network error on threads",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "time timeout 300 python ... --out .scratch/cold/out --cache .scratch/cold/cache: real 1m29.529s rc 0; time timeout 120 python ... --out .scratch/advi_cotbkf/account_links: real 1m11.618s rc 0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-c-4 BOUNDS: 'Within 120 seconds for CB3c4-AC2 (column projection; cache under .scratch/ and say so).'",
  "world_is": "The default cache is <out>/../tx_cache, i.e. .scratch/advi_cotbkf/tx_cache (14 parquet files, 30 MB, uncommitted). Cold run (empty cache, boto3 download on 14 threads, then the rule): real 1m29.5s, same ACCOUNT-LINKS line. Cached run: real 1m11.6s on the first AC2 invocation, 2.6 s on re-runs (file-system cache). pyarrow's own S3 reader (threads) failed with 'AWS Error NETWORK_CONNECTION during GetObject', so the script downloads with boto3 (8 retries). A slower link than this device's (a sibling saw over 200 s for the sequential read) ends a cold run at rc 124. Also: the summary line's not_linked counts every NOT_LINKED row, ambiguous being one of its reasons, so linked+not_linked = 459 and ambiguous (13) is a subset of not_linked (279); the TO does not say whether ambiguous is inside or beside not_linked.",
  "notes": "Disarm: copy C:/Users/AndrewBerman/Desktop/wk-advi-cotbkf-11/.scratch/advi_cotbkf/tx_cache to the shared tree's .scratch/advi_cotbkf/ before the worktree is removed (the script reads it with no flag), or run the script once without the timeout."
}
```

## ADVI_COTBKF-S6 -- W11-S3's hazard disarmed by its owner: the account-links cache now sits in the shared tree, and AC2 re-runs in 3.1 s there

```json
{
  "id": "ADVI_COTBKF-S6",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C",
  "surfaced_at": "2026-10-07T02:21Z",
  "one_line": "Disarm act for ADVI_COTBKF-W11-S3 (ARMED, disarm_owner 2.0.0_SA_COO~C): the account-links read cache (.scratch/advi_cotbkf/tx_cache, 29 MB) was copied from the worker's worktree into the shared tree before the worktree's removal, and CB3c4-AC2 re-run there under timeout 120 passes in 3.1 s with the identical line.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "cp -r C:/Users/AndrewBerman/Desktop/wk-advi-cotbkf-11/.scratch/advi_cotbkf/tx_cache .scratch/advi_cotbkf/ (29M) in the shared tree, 2026-10-07 ~02:1xZ, after the merge of the CB-c-4 branch @1a2c42eeca",
      "timeout 120 python data/assets/scripts/silver/commonwealth_account_links.py --out .scratch/advi_cotbkf/account_links in the shared tree: real 3.069 s, last line ACCOUNT-LINKS old_accounts=459 every_old_account_listed=True linked=180 not_linked=279 ambiguous=13 chains=5 (identical to the worker's AC2 output)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-c-4 BOUNDS: CB3c4-AC2 runs within 120 seconds; row W11-S3 (ARMED): the bound holds only against the worker's primed cache (a cold run took 1m29.5s on that device).",
  "world_is": "The cache that keeps AC2 inside its bound lives where a grader runs (the shared tree's untracked .scratch/, device-local, never committed). A clean tree elsewhere needs one cold run first (about 90 s here, inside the bound on this device). W11-S3's own disposition is the CVO's at L9.",
  "notes": "Same disarm shape as rows S4 and S5."
}
```

## ADVI_COTBKF-W13-S1 -- LEFT_COMMONWEALTH is read as "an in-kind exit with no receiver matching any position"; the order left the boundary with "no in-kind receiver" unstated

```json
{
  "id": "ADVI_COTBKF-W13-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~13",
  "surfaced_at": "2026-10-07T03:10Z",
  "one_line": "The new reason LEFT_COMMONWEALTH is applied where the ended account has final in-kind exit rows and no receiver matched any position; an ended account with no exit rows and no receiver keeps round 3's 'no in-kind receiver' (51 of 1,450).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python data/assets/scripts/silver/commonwealth_account_links.py --out .scratch/advi_cotbkf/account_links_r4 (worktree wk-advi-cotbkf-13): NOT_LINKED reasons: LEFT_COMMONWEALTH=587, ambiguous=14, below threshold=91, closed to cash=495, no in-kind receiver=51; the 459 round-3 old accounts keep every status and target (0 changed of 459); 97 of round 3's 'no in-kind receiver' old rows are now LEFT_COMMONWEALTH"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-d-2 THE CELL: NOT_LINKED reasons include LEFT_COMMONWEALTH (the in-kind exit has no receiver inside this delivery) plus round 3's 'no in-kind receiver', 'below threshold', 'ambiguous', 'closed to cash'; it does not say which of the two no-match reasons applies when.",
  "world_is": "Both reasons describe a zero-candidate account. The worker split them on the evidence the table holds: exit rows present (lo/trfo/trco on a non-cash CUSIP within 10 trading days before the last trade) -> LEFT_COMMONWEALTH; none -> 'no in-kind receiver'. The round-3 entry point link_old_accounts keeps the round-3 label for its own tests. Also measured: of 202 client lines (two or more accounts), 12 reach an open account (in positions); the rest stop at an ended account whose own row carries its reason, because only 83 of 1,533 accounts are open.",
  "notes": "If the issuer reads the split differently, the change is one line in _link (the row['reason'] assignment) and the tests named *ended*."
}
```

## ADVI_COTBKF-W14-S1 -- CB4d3-AC2 meets its 120-second bound only against a primed cache: the cache now needs advisor and relationship column, so round 3's cache is stale and a cold read took 2m23s here

```json
{
  "id": "ADVI_COTBKF-W14-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~14",
  "surfaced_at": "2026-10-07T03:40Z",
  "one_line": "CB4d3-AC2 meets its 120-second bound only against a primed cache: the cache now needs advisor and relationship column, so round 3's cache is stale and a cold read took 2m23s here",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "time timeout 590 python data/assets/scripts/silver/commonwealth_crosswalk.py --out .scratch/advi_cotbkf/crosswalk_warm (cache dir copied from round 3, columns missing): real 2m23.6s, S3 pass rewrote the cache; then time timeout 120 python data/assets/scripts/silver/commonwealth_crosswalk.py --out .scratch/advi_cotbkf/crosswalk_r4: real 6.4 s rc 0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-d-3 BOUNDS: 'Within 120 seconds for CB4d3-AC2 (cache under .scratch/, warmed once untimed, and say so).'",
  "world_is": "The cache at <worktree>/.scratch/advi_cotbkf/cache (untracked, about 20 MB) was warmed once untimed in the worker's worktree. load_inputs treats a cache missing Advisor_ID or relationship_id as stale and re-reads S3 (about 2.4 min here, over the bound), so a grader's tree still holding round 3's cache will exceed 120 s on its first run.",
  "notes": "Disarm: copy C:/Users/AndrewBerman/Desktop/wk-advi-cotbkf-14/.scratch/advi_cotbkf/cache over the shared tree's .scratch/advi_cotbkf/cache before the worktree is removed, or run the script once without the timeout. Same disarm shape as rows S4 to S6."
}
```

## ADVI_COTBKF-W14-S2 -- The order names 'the advisor ids' for each near-match entry, but only the Commonwealth side carries an Advisor_ID; the Cottonwood accounts dimension has none, so each entry gives the Commonwealth Advisor_ID(s) plus the candidate's relationship_id

```json
{
  "id": "ADVI_COTBKF-W14-S2",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~14",
  "surfaced_at": "2026-10-07T03:40Z",
  "one_line": "The order names 'the advisor ids' for each near-match entry, but only the Commonwealth side carries an Advisor_ID; the Cottonwood accounts dimension has none, so each entry gives the Commonwealth Advisor_ID(s) plus the candidate's relationship_id",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3 read of the Cottonwood accounts dimension (accounts_key in CURRENT_SIDE_LOCATIONS.json): columns account_id, relationship_id, architect, ... and no advisor column; Commonwealth transactions and positions silver both carry Advisor_ID"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-d-3 change 2: each near-match entry carries 'the advisor ids'.",
  "world_is": "near_matches.csv/.md print commonwealth_advisor_ids (distinct Advisor_ID over the account's transactions and positions rows, blank when none) and, labelled as such and not as an advisor id, the candidate's current_relationship_id. The accounts dimension also has a column named for the portfolio group, which holds a person name on the rows read; this worker left it out because the commit naming gate (LGIC_ENFORCE) refuses that column name as an IAM_GROUP at commonwealth_crosswalk.py (3 refusals), so whether it is the Cottonwood advisor is neither used nor established.",
  "notes": "Judged at L9 under CB4d3-AC3."
}
```

## ADVI_COTBKF-W14-S3 -- Round 3's code already scored every account regardless of date; the cutoff only chose the printed reason, so the in-kind change moves reason and score columns, not any match: matched stays 439 and no status or current account changed

```json
{
  "id": "ADVI_COTBKF-W14-S3",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~14",
  "surfaced_at": "2026-10-07T03:40Z",
  "one_line": "Round 3's code already scored every account regardless of date; the cutoff only chose the printed reason, so the in-kind change moves reason and score columns, not any match: matched stays 439 and no status or current account changed",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "round 3 base run (same cache) vs r4 run, merged on commonwealth_account: status/current_account changes 0 of 1533; reason CLOSED_BEFORE_CURRENT_HISTORY 758 -> 212 (all 212 now REBUILT_FROM_TRANSACTIONS, none in kind); NO_CURRENT_ACCOUNT_HOLDS_POSITIONS 263 -> 788; AWAITING_PERSON 21 (17 round 3 near matches + 4 in-kind exits before 2026-04-22)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-d-3 THE CELL: round 3 'scores an account only if its last activity is on or after 2026-04-22', so 758 rows were not scored.",
  "world_is": "In crosswalk_rows every account is scored (the `scored` list) before the reason branch; the CLOSED_BEFORE_CURRENT_HISTORY branch just left `score` blank and printed no candidate. R2 passing was never date-limited, so no account newly matches. The change makes the reason branch skip the cutoff for an in-kind exit and print the score and best candidate.",
  "notes": "No action needed; recorded because the premise's mechanism differs from the code's."
}
```

## ADVI_COTBKF-S7 -- CB4d4-AC1 (check_restricted_prefix.py) cannot be re-run on dell2: terraform is not installed, so the drain re-grade of the merged C-RESTRICTED policy rests on the laptop worker's run alone

```json
{
  "id": "ADVI_COTBKF-S7",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T07:36Z",
  "one_line": "CB4d4-AC1 (check_restricted_prefix.py) cannot be re-run on dell2: terraform is not installed, so the drain re-grade of the merged C-RESTRICTED policy rests on the laptop worker's run alone",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "command -v terraform on dell2 at 07:30Z: ABSENT",
      "python infra/aws/terraform/shared-infra/tests/check_restricted_prefix.py at HEAD 2040c2db3f on dell2: FileNotFoundError [WinError 2] at line 35 (terraform init)",
      "proof instance deliverables/0.9.0_WK_ADVI_COTBKF~15/...restricted-prefix-policy.proof_of_spec.json: VALID rc=0 at HEAD (the laptop run)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Drain (dispatch Step 5): after each merge, run the hygiene the touched surface needs once, at the drain.",
  "world_is": "The merged .tf change and its check landed (85d8b5f20f); nothing is applied. The check needs a terraform binary and the real backend; dell2 has neither binary nor a recorded apply lane for this round.",
  "notes": "Any terraform plan/apply of CB-d-4 is a separate act (safe-apply) on a box with terraform; the laptop tfplan from -15 is archived only on the laptop (MSTR msg 6)."
}
```

## ADVI_COTBKF-S8 -- Disarm act for ADVI_COTBKF-W14-S1 (ARMED, disarm_owner 2.0.0_SA_COO~C, now off this project; taken by its successor 2.0.0_SA_COO~C2): CB4d3-AC2 runs in 34 s on dell2's shared tree, inside its 120 s bound

```json
{
  "id": "ADVI_COTBKF-S8",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T07:40Z",
  "one_line": "Disarm act for ADVI_COTBKF-W14-S1 (ARMED, disarm_owner 2.0.0_SA_COO~C, now off this project; taken by its successor 2.0.0_SA_COO~C2): CB4d3-AC2 runs in 34 s on dell2's shared tree, inside its 120 s bound",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python data/assets/scripts/silver/commonwealth_crosswalk.py --out .scratch/advi_cotbkf/crosswalk_r4 on dell2 at HEAD 2040c2db3f, 07:3xZ: rc 0, 34 s, last line CROSSWALK commonwealth_accounts=1533 every_account_listed=True matched=439 not_matched=1094 ambiguous=36 by_rule=R2-in-kind-transfer:439 in_kind_unscored=0 near_matches_applied=0 near_matches=21",
      "same pass: CB4d2-AC2 rc 0 in 7 s (ACCOUNT-LINKS ended_accounts=1450 every_ended_account_listed=True); CB4d5-AC2 rc 0 in 6 s (DOCUMENTS-PLAN unique=11119 every_document_once=True)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-d-3 BOUNDS: CB4d3-AC2 within 120 seconds (cache under .scratch/, warmed once untimed). Row W14-S1: the bound holds only against a primed cache, and the primed cache was in the laptop worktree.",
  "world_is": "The laptop worktree and its cache are gone (archived on the laptop only). The grader's tree is now dell2's, and the criterion runs inside its bound there, so the hazard is disarmed.",
  "notes": "Disarm owner reassigned by succession: 2.0.0_SA_COO~C is on NFRA_CTLPLN only (Andrew-direct ~06:1xZ). Same disarm shape as S4, S5 and S6."
}
```

## ADVI_COTBKF-W12-S1 -- This device (dell2) has no pandas_market_calendars, so lib/trading_calendar falls back to a holiday list that covers only 2024-2027: every earlier year counts holidays as trading days, and the census security_days_needed (9,630,847) is not comparable to round 2's (9,388,961)

```json
{
  "id": "ADVI_COTBKF-W12-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~12",
  "surfaced_at": "2026-10-07T07:50Z",
  "one_line": "This device (dell2) has no pandas_market_calendars, so lib/trading_calendar falls back to a holiday list that covers only 2024-2027: every earlier year counts holidays as trading days, and the census security_days_needed (9,630,847) is not comparable to round 2's (9,388,961)",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -c 'import pandas_market_calendars' on dell2: ModuleNotFoundError",
      "lib/trading_calendar.py calendar_source() -> NYSE/hardcoded-fallback-2024-2027 in PRICE_CENSUS_20261007.json; trading_days_between(2015-01-01, 2015-12-31) -> 261 days, 2019 -> 261, 2022 -> 260, 2025 -> 250",
      "round 2 PRICE_COVERAGE_20261006.json universe.needed_days_definition: NYSE/pandas_market_calendars"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-d-1: keep round 2's universe and matching; the report compares priced counts against round 2's.",
  "world_is": "The universe (4,634 CUSIPs) and every priced count (priced_any, priced_fixed_income) do not depend on the calendar and compare directly. security_days_needed, security_days_covered and priced_in_window do: the needed denominator is inflated by the pre-2024 holidays the fallback does not remove (9,630,847 vs 9,388,961, about 2.6 percent), and a covered day on a pre-2024 holiday is dropped from the window. The criterion line passes on its stated prefix; the day totals are labelled with this calendar in the JSON.",
  "notes": "Rerun on a device with pandas_market_calendars installed (the laptop) for day totals comparable to round 2. Armed because a reader comparing 1,318,560 of 9,630,847 with round 2's 2,090,953 of 9,388,961 would read the gap as price coverage when part of it is the calendar."
}
```

## ADVI_COTBKF-W12-S2 -- Two USABLE buckets could not be listed under this identity (cloudops-dell2-agent-user): opal-data-cottonwood, Cottonwood's own scope bucket, and opalinvest-portal; both rows say LIST FAILED: AccessDenied, so what they hold is unknown, not empty

```json
{
  "id": "ADVI_COTBKF-W12-S2",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~12",
  "surfaced_at": "2026-10-07T07:50Z",
  "one_line": "Two USABLE buckets could not be listed under this identity (cloudops-dell2-agent-user): opal-data-cottonwood, Cottonwood's own scope bucket, and opalinvest-portal; both rows say LIST FAILED: AccessDenied, so what they hold is unknown, not empty",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "PRICE_CENSUS_20261007.json buckets[] rows opal-data-cottonwood and opalinvest-portal: holds = LIST FAILED: AccessDenied, list_status list_failed",
      "caller identity arn:aws:iam::313476888478:user/cloudops-dell2-agent-user (sts get-caller-identity)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-d-1: a USABLE bucket with no price store gets one line saying what it holds (listing its top-level prefixes is enough).",
  "world_is": "35 of 35 USABLE buckets are graded; 33 were listed and 2 refused the list. opal-data-cottonwood is the firm's registry scope bucket (opal-data-cot is its legacy alias and holds the two cottonwood stores read), so a per-security daily price store there, if any, is not named by this census. A failed list is a recorded result, never a silent empty.",
  "notes": "Judged at L9 under CB4d1-AC3 (completeness). A listing under the laptop profile would settle it."
}
```

## ADVI_COTBKF-W12-S3 -- The gold canonical holdings store carries two shapes: 47 of its 130 files (the earliest dates) have a ticker column and no cusip column, so the order's CUSIP-keyed read raised on the first run; the census reads each file's available key columns (cusip where present, ticker always)

```json
{
  "id": "ADVI_COTBKF-W12-S3",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~12",
  "surfaced_at": "2026-10-07T07:50Z",
  "one_line": "The gold canonical holdings store carries two shapes: 47 of its 130 files (the earliest dates) have a ticker column and no cusip column, so the order's CUSIP-keyed read raised on the first run; the census reads each file's available key columns (cusip where present, ticker always)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "pyarrow schema read of all 130 objects under the legacy_address('cottonwood-gold-canonical-holdings') prefix: 47 files without cusip (10 columns, 2026-04-22 on), 51 with cusip and cash_equivalent (12 columns, from 2026-06-08), 32 with the supervised columns (14, from 2026-08-20)",
      "first census run: ArrowInvalid: No match for FieldRef.Name(cusip)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-d-1: a custodian mark on a held position is a close for that security on that day (the read named by CUSIP).",
  "world_is": "Holdings priced 1,028 universe securities (1,020 by CUSIP, 8 by ticker; 53 reused symbols reported, not credited). Ticker matches on the 47 early files follow round 2's rule (a reused symbol is not credited).",
  "notes": "No action needed; recorded because the premise's schema is not uniform across the store."
}
```

## ADVI_COTBKF-W12-S4 -- ruff is not installed on this device (dell2), so .tools/commit-gate.sh blocks any .py commit with 'No module named ruff'; the census script and test were blocked the first commit attempt (fail-closed, not bypassed by --force); the worker installed ruff==0.15.11 with pip --user to clear it

```json
{
  "id": "ADVI_COTBKF-W12-S4",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~12",
  "surfaced_at": "2026-10-07T07:50Z",
  "one_line": "ruff is not installed on this device (dell2), so .tools/commit-gate.sh blocks any .py commit with 'No module named ruff'; the census script and test were blocked the first commit attempt (fail-closed, not bypassed by --force); the worker installed ruff==0.15.11 with pip --user to clear it",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bash .tools/commit-gate.sh on the two new files: 'python.exe: No module named ruff' / 'BLOCKED: ruff check failed'",
      "python -m pyflakes on both files: no output; python .tools/ds-precommit-check.py on both files: rc 0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CLAUDE.md rule 14: every .py edit passes .tools/commit-gate.sh (py_compile + ds-precommit + ruff py39).",
  "world_is": "The gate is fail-closed on a missing ruff and --force does not bypass it, so the first commit attempt aborted. This worker installed the pinned linter with python -m pip install --user ruff==0.15.11 (the version the gate's contract names, from the package index; no Opal or vendor API) and re-ran the gate; py_compile, pyflakes and ds-precommit had already been clean.",
  "notes": "Candidate for lint on a device with ruff at the drain."
}
```

## ADVI_COTBKF-S9 -- the account links differ between the laptop and dell2

```json
{
 "id": "ADVI_COTBKF-S9",
 "project": "ADVI_COTBKF",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-10-07T08:45Z",
 "one_line": "The account-links script gives different answers on the laptop and on dell2 over the same silver table: 3 of 1,450 rows differ (laptop 212 LINKED, dell2 211). Two links whose evidence holds on the transactions (0QF879348 -> B3S606523, B3S780328 -> B3S782287) read NOT_LINKED 'closed to cash' on dell2, and cv0QF879185 is AMBIGUOUS on the laptop and LINKED on dell2.",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "deliverables/0.9.0_WK_ADVI_COTBKF~13/account_links_r4.csv (the laptop worker's run, committed): LINKED 212, NOT_LINKED 1,238 (this compile's read, dell2, 2026-10-07 ~08:1xZ-08:4xZ)",
   ".scratch/advi_cotbkf/account_links_r4/account_links.csv (the issuer's dell2 real run, untracked): LINKED 211, NOT_LINKED 1,239; row-by-row against the laptop file, 3 rows differ (this compile's read, dell2, 2026-10-07 ~08:1xZ-08:4xZ)",
   "transactions (.scratch/advi_cotbkf/tx_cache, 1,416,497 rows): 0QF879348's and B3S780328's printed in-kind receipts are present at the printed quantities and dates (part of the 123 of 123 items in the round-4 L9 grade) (this compile's read, dell2, 2026-10-07 ~08:1xZ-08:4xZ)",
   "python -c 'import pandas_market_calendars' on dell2: ModuleNotFoundError (row W12-S1: lib/trading_calendar falls back to a 2024-2027 holiday list); the exits that differ are dated 2023-02-14 and 2023-12-22 (this compile's read, dell2, 2026-10-07 ~08:1xZ-08:4xZ)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "CB-d-2: 'Never guess a link' and the same rule over the same table gives one answer; the issuer's --apply writes the silver account_links table the analyst reads.",
 "world_is": "The result depends on the box that runs it. The dell2 run is the wrong one on the two links checked, and an --apply run on dell2 would write it. The cause is not measured; the calendar fallback is the leading candidate, since both differing exits fall before 2024, where the fallback counts holidays as trading days.",
 "disarm_owner": "2.0.0_SA_COO~C2",
 "notes": "ARMED for the apply. Disarms when the cause is named and the run that is applied reproduces the committed laptop deliverable row for row (or the deliverable is shown wrong on those 3 rows). Do not --apply from dell2 before then. Filed by the round-4 compile, not compiled in it."
}
```

## ADVI_COTBKF-S10 -- Cause of S9 and W12-S1 MEASURED: lib/trading_calendar's fallback holiday list (2024-2027 only). With NYSE holidays 2010-2023 added to the fallback, dell2's account-links run reproduces the laptop deliverable 1,450 of 1,450 rows (0 differ; the unpatched dell2 run differs on 11)

```json
{
  "id": "ADVI_COTBKF-S10",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T08:45Z",
  "one_line": "Cause of S9 and W12-S1 MEASURED: lib/trading_calendar's fallback holiday list (2024-2027 only). With NYSE holidays 2010-2023 added to the fallback, dell2's account-links run reproduces the laptop deliverable 1,450 of 1,450 rows (0 differ; the unpatched dell2 run differs on 11)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python <scratchpad>/s9_calendar_probe.py (extends tc.NYSE_HOLIDAYS_FALLBACK in-process with 127 rule-derived NYSE holidays 2010-2023, then runs data/assets/scripts/silver/commonwealth_account_links.py --out .scratch/advi_cotbkf/s9_probe) on dell2 at 08:4xZ: ACCOUNT-LINKS ended_accounts=1450 linked=212 not_linked=1238 ambiguous=14",
      "csv compare keyed on old_account: probe vs deliverables/0.9.0_WK_ADVI_COTBKF~13/account_links_r4.csv (laptop, pmc present): 0 of 1,450 rows differ; unpatched dell2 r4 run vs the same file: 11 rows differ (0QF879185, 0QF879348, B3S605712, B3S606523, B3S780328, ...)",
      "python -c 'import pandas_market_calendars' on dell2: ModuleNotFoundError; holidays and exchange_calendars also absent",
      "consumers: 91 .py files under lib/, data/, infra/ import trading_calendar (token census)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "S9 disarm condition: the cause is named and the run that is applied reproduces the committed laptop deliverable row for row.",
  "world_is": "The cause is named and the reproduction holds under a pre-2024-complete calendar. S9 stays ARMED: an unpatched --apply on dell2 (or any box or Lambda without pandas_market_calendars) still writes the wrong 11 rows. Two remedies, either disarms S9 and W12-S1: (a) run the apply only where pandas_market_calendars is installed; (b) extend NYSE_HOLIDAYS_FALLBACK in lib/trading_calendar.py back to the earliest year its consumers read. (b) touches 91 consumers, Lambdas included, so it is not this project's write surface: routed to 1.0.0_SA_CTO.",
  "notes": "The probe's holiday list is derived from the published rules plus the 2018-12-05 closure; it omits 2012-10-29/30 (Sandy), which the account-links comparison did not need. A fallback edit should take pmc's own output as its source, not this list."
}
```

## ADVI_COTBKF-S11 -- RULING C list (laptop 1.0.0_SA_CTO 08:5xZ): the pre-2024-dated artifacts this lane made on dell2 through lib/trading_calendar.py -- one committed (the round-4 census's day figures), the rest scratch; none served, landed or graded REALIZED; each re-run after ruling B's fix

```json
{
  "id": "ADVI_COTBKF-S11",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T09:05Z",
  "one_line": "RULING C list (laptop 1.0.0_SA_CTO 08:5xZ): the pre-2024-dated artifacts this lane made on dell2 through lib/trading_calendar.py -- one committed (the round-4 census's day figures), the rest scratch; none served, landed or graded REALIZED; each re-run after ruling B's fix",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "COMMITTED: deliverables/0.9.0_WK_ADVI_COTBKF~12/PRICE_CENSUS_20261007.{json,md} @642222e85f (made on dell2 by ~12): security_days_needed=9630847, security_days_covered=1318560 span pre-2024 dates under calendar NYSE/hardcoded-fallback-2024-2027 (row W12-S1). The priced counts (priced_any=1720, priced_fixed_income=184) do not read the calendar. Quoted in the drain-end packet @29479eeb61",
      "SCRATCH (untracked, dell2 .scratch/advi_cotbkf/): account_links_r4/ (07:3xZ, unpatched calendar; differs from the laptop on 11 of 1,450 rows), r4_realrun/d1.log and d2.log (the census and links real runs), s9_probe/ (patched calendar, diagnostic only)",
      "NOT calendar-dependent (0 imports of trading_calendar), so outside ruling A: crosswalk_r4/, documents_plan/, documents_plan_e3base/",
      "NOT produced: no --apply from dell2 in this lane; nothing landed in S3 by this lane"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Ruling C: each Dell COO lists, as rows, the artifacts its lane produced on a Dell since seating whose dates precede 2024; each is re-run after the fix; none is served, landed to gold or graded REALIZED meanwhile.",
  "world_is": "Two calendar-dependent artifacts exist in this lane on dell2: the committed census day figures and the scratch links run. The links' applied run is E2, uncut until the fix. The census re-run is E2 criterion (3). The CVO's round-4 grade of CB4d1-AC3 was NOT MET and graded nothing REALIZED from them.",
  "notes": "Re-run owner: 2.0.0_SA_COO~C2 in E2. The scratch links output is not deleted (it is the S9 evidence); it is never applied."
}
```

## ADVI_COTBKF-W19-S1 -- the role-request writer cannot state a user as the assuming principal (CB-e-4)

```json
{
  "id": "ADVI_COTBKF-W19-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~19",
  "surfaced_at": "2026-10-07T08:58Z",
  "one_line": "role_request.py cannot express the break-glass role's trust (a console USER); the request carries assuming_service signin.amazonaws.com as the nearest admitted shape",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/standards/ROLE_REQUEST.schema.json assuming_service pattern ^[a-z0-9-]+(\\.[a-z0-9-]+)+$ admits only a dotted service name; org/devices/role_request.py write has no principal field",
      "infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf:248-257 trust = Principal AWS Andrew_Berman_Console user, sts:AssumeRole",
      "request org/devices/role_requests/dell2/dell2-20261007T085711Z-7b15.json written with assuming_service signin.amazonaws.com; the merged .tf, not the request, is the authority for trust"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-e-4: the writer admits the break-glass role request, with the assuming principal a user rather than a service as the named possible refusal.",
  "world_is": "The writer admits the request only with a service-shaped assuming_service; the user principal cannot be stated. The value signin.amazonaws.com is a placeholder, not the trust. The laptop applies the merged file's trust (console user only). Writer and schema are NFRA_CTLPLN's, not edited.",
  "notes": "Gap also carried in C_RESTRICTED_WRITE_IN.md."
}
```

## ADVI_COTBKF-S12 -- The round-5 issuer applies (E5 crosswalk, E3 documents) write to opal-data-cottonwood, whose bucket policy explicitly denies the dell2 identity ListBucket and GetBucketPolicy; whether it also denies PutObject is unmeasured, and measuring it would be a write into a fenced bucket

```json
{
  "id": "ADVI_COTBKF-S12",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T09:15Z",
  "one_line": "The round-5 issuer applies (E5 crosswalk, E3 documents) write to opal-data-cottonwood, whose bucket policy explicitly denies the dell2 identity ListBucket and GetBucketPolicy; whether it also denies PutObject is unmeasured, and measuring it would be a write into a fenced bucket",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3 ls --recursive s3://opal-data-cottonwood/commonwealth/cottonwood/silver/crosswalk/ on dell2, 09:0xZ: AccessDenied, ListObjectsV2, user/cloudops-dell2-agent-user, 'with an explicit deny in a resource-based policy'",
      "aws s3api get-bucket-policy --bucket opal-data-cottonwood on dell2, 09:1xZ: AccessDenied, explicit deny in a resource-based policy",
      "GetObject is admitted: commonwealth_documents.py --plan on dell2 read the bronze archives (sources_verified=11119), 09:1xZ",
      "commonwealth_crosswalk.py apply_to_s3 and commonwealth_documents.py --apply write at opal_naming.address('commonwealth', cottonwood, ...) = opal-data-cottonwood"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Decomposition round 5, issuer's acts 1-2: E5 and the E3 apply run from this seat after the drain; standing rule (1.0.0_SA_CTO~DELL2 msg 214): never widen a fence from dell2.",
  "world_is": "The dell2 identity is fenced on the Cottonwood bucket (NFRA_CTLPLN's Dell bucket fences). No apply is attempted from dell2: a Put that succeeded would write served output from a fenced box, and one that failed would half-land a ledger. ARMED: no --apply of E3 or E5 from dell2.",
  "notes": "Disarms when 1.0.0_SA_CTO~DELL2 rules where the applies run (the laptop by relay, or dell2 after NFRA_CTLPLN round 4 grants the write) and the apply runs there under a never-widen pair."
}
```

## ADVI_COTBKF-S13 -- CORRECTS S12: E5 and E3 do NOT write to opal-data-cottonwood. opal_naming.address('commonwealth', 'cottonwood', 'silver', ...) resolves to opal-data-assets, which the dell2 identity lists without refusal; S12's fence evidence was measured on the wrong bucket

```json
{
  "id": "ADVI_COTBKF-S13",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T09:35Z",
  "one_line": "CORRECTS S12: E5 and E3 do NOT write to opal-data-cottonwood. opal_naming.address('commonwealth', 'cottonwood', 'silver', ...) resolves to opal-data-assets, which the dell2 identity lists without refusal; S12's fence evidence was measured on the wrong bucket",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python: opal_naming.address('commonwealth','cottonwood','silver','crosswalk','date=2026-06-23') = s3://opal-data-assets/commonwealth/cottonwood/silver/crosswalk/date=2026-06-23 (also documents, bronze/imaging, bronze/crm: all opal-data-assets)",
      "listing of s3://opal-data-assets/commonwealth/cottonwood/silver/crosswalk/date=2026-06-23/ on dell2, 09:3xZ: crosswalk.csv 570,490 B and crosswalk.parquet 128,256 B (2026-10-06 22:25, round 3's apply); silver/documents/ empty; silver/account_links/ holds date=2026-06-23/",
      "get-bucket-versioning --bucket opal-data-assets on dell2: Enabled",
      "infra/logic/06_CONFORMANCE_LEDGER.md:149 (X15): only the CRM zip departs to opal-data-cottonwood; address() returns opal-data-assets for every other Commonwealth table (R4: one bronze/silver home)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "S12: the round-5 applies write to opal-data-cottonwood, whose policy denies the dell2 identity List and GetBucketPolicy.",
  "world_is": "The applies write to opal-data-assets. S12's deny is real but on a bucket neither apply touches. PutObject from dell2 on opal-data-assets is unmeasured (no refusal seen on any read). The rulings resting on S12 (1.0.0_SA_CTO~DELL2 msg 239; laptop 09:3xZ item 6) rest on a wrong premise and go back to their authors with this row.",
  "notes": "S12 is not disarmed by this row: its hazard (an apply from dell2) stands until 1.0.0_SA_CTO~DELL2 re-rules on the corrected premise. The never-widen draft is corrected to opal-data-assets in the same commit."
}
```

## ADVI_COTBKF-S14 -- CB-e-3's hold-back guards s3://opal-data-assets/commonwealth/cottonwood/bronze/crm/, but the C-RESTRICTED prefix (register X15) is in opal-data-cottonwood; the guard compares the full URI, so it watches a prefix in the wrong bucket

```json
{
  "id": "ADVI_COTBKF-S14",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T09:35Z",
  "one_line": "CB-e-3's hold-back guards s3://opal-data-assets/commonwealth/cottonwood/bronze/crm/, but the C-RESTRICTED prefix (register X15) is in opal-data-cottonwood; the guard compares the full URI, so it watches a prefix in the wrong bucket",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "worker ~18 report: restricted_prefix() = opal_naming.address(SOURCE, SCOPE, 'bronze', 'crm', 'date=<d>') less the partition; a key is held when its full URI starts with it",
      "address('commonwealth','cottonwood','bronze','crm','date=2026-06-23') = s3://opal-data-assets/... (measured 09:3xZ)",
      "X15 (06_CONFORMANCE_LEDGER.md:149): THE RESTRICTED PREFIX is commonwealth/cottonwood/bronze/crm/ in opal-data-cottonwood; address() has no route to the firm bucket for bronze"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-e-3: the prefix is the key prefix lib/opal_naming builds for (commonwealth, cottonwood, bronze, crm), resolved the way the script resolves its own addresses.",
  "world_is": "The order's own instruction aimed the guard at address(), which X15 says does not reach the restricted bucket. Inert today: documents write only to opal-data-assets silver, so no planned key can land in either prefix (held_restricted=0 both ways). The fix is key()-based matching (bucket-agnostic) or X15's bucket; a one-function repair for the next cut on this script.",
  "notes": "An issuer's cut defect (2.0.0_SA_COO~C2), not the worker's: the worker built what the face said."
}
```

## ADVI_COTBKF-S15 -- W12-S2 answered by the laptop's listing: opal-data-cottonwood holds only irpt/cottonwood/ and mdpf/cottonwood/ at two levels; opalinvest-portal holds assets/, fonts/, logos/ with no sub-prefix. Neither names a per-security daily price store

```json
{
  "id": "ADVI_COTBKF-S15",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T09:35Z",
  "one_line": "W12-S2 answered by the laptop's listing: opal-data-cottonwood holds only irpt/cottonwood/ and mdpf/cottonwood/ at two levels; opalinvest-portal holds assets/, fonts/, logos/ with no sub-prefix. Neither names a per-security daily price store",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "laptop 1.0.0_SA_CTO ran deliverables/2.0.0_SA_COO~C2/list_unlisted_usable_buckets.py (@27b47e8ef1) at 2026-10-07T09:25Z; result org/missions/D8/ADVI/ADVI_COTBKF/deliverables/1.0.0_SA_CTO/UNLISTED_USABLE_BUCKETS_20261007.json (not yet on origin; Taildrop copy C:/Users/Test/Downloads/UNLISTED_USABLE_BUCKETS_20261007.json, 682 B, read by this seat 09:3xZ)",
      "opal-data-cottonwood: top=['irpt/','mdpf/'], second: irpt/ -> ['irpt/cottonwood/'], mdpf/ -> ['mdpf/cottonwood/']",
      "opalinvest-portal: top=['assets/','fonts/','logos/'], second: 0 sub-prefixes each"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB4d1-AC3 (NOT MET at L9 @2114a2a7a2): the census is complete -- no unnamed store holding a per-security daily price in a USABLE bucket; two USABLE buckets were never listed.",
  "world_is": "Both buckets are now listed two levels deep. Prefix names alone do not name a price store; irpt/cottonwood/ and mdpf/cottonwood/ are reporting and model-portfolio trees, read at prefix depth only. Bears on the CVO's re-grade of CB4d1-AC3; the grade is the CVO's.",
  "notes": "Row filed by the dell2 seat per laptop ruling (row ids minted only on the project's box)."
}
```

## ADVI_COTBKF-S16 -- DISARMS S9: the account links APPLIED from dell2 on the 2010-2027 calendar reproduce the committed laptop deliverable row for row (1,450 of 1,450, every column; 212 LINKED)

```json
{
  "id": "ADVI_COTBKF-S16",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T10:25Z",
  "one_line": "DISARMS S9: the account links APPLIED from dell2 on the 2010-2027 calendar reproduce the committed laptop deliverable row for row (1,450 of 1,450, every column; 212 LINKED)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "calendar_source() on dell2 = NYSE/hardcoded-fallback-2010-2027 (lib/trading_calendar.py @83ab7192ee via dell2 merge 0a73ed06a0)",
      "ledger advi-cotbkf-e2-account-links-apply-20261007 CLOSED 1/1: applied 10:19:07Z, VersionIds ogf8Q2zk... -> OQ9YHJ3h..., JqEXeGJY... -> JY3f29AV...",
      "independent read-back of s3://opal-data-assets/commonwealth/cottonwood/silver/account_links/date=2026-06-23/account_links.csv vs deliverables/0.9.0_WK_ADVI_COTBKF~13/account_links_r4.csv: 1,450 rows each, differ on (status,new_account) 0, differ on any column 0; 0QF879348->B3S606523 LINKED, B3S780328->B3S782287 LINKED, cv0QF879185 NOT_LINKED"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "S9 (ARMED): disarms when the run that is applied reproduces the committed laptop deliverable row for row.",
  "world_is": "It does. S9's hazard (a dell2 apply writing the wrong 3 rows) cannot recur on this box: the calendar covers the table's dates, and CB-e-1's guard refuses any calendar that does not.",
  "notes": "Never-widen pair: COO @163c0dd8a1, CTO @792b16742d. Branch A."
}
```

## ADVI_COTBKF-S17 -- DISARMS W12-S1: the census re-run on the 2010-2027 calendar needs 9,388,961 security-days, equal to round 2, so the day totals compare again: covered 1,297,651 (round 2: 2,090,953)

```json
{
  "id": "ADVI_COTBKF-S17",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T10:25Z",
  "one_line": "DISARMS W12-S1: the census re-run on the 2010-2027 calendar needs 9,388,961 security-days, equal to round 2, so the day totals compare again: covered 1,297,651 (round 2: 2,090,953)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/2.0.0_SA_COO~C2/census_e2/PRICE_CENSUS_20261007.json @163c0dd8a1: PRICE-CENSUS buckets=40 every_bucket_graded=True barred_read=0 usable=35 barred=5 universe=4634 priced_any=1720 priced_fixed_income=184 security_days_covered=1297651 security_days_needed=9388961",
      "round 2 (PRICE_COVERAGE_20261006): security_days_covered=2090953 of 9388961"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "W12-S1 (ARMED): disarms when the census's security_days_* are re-run under a calendar that covers 2013 onward and are reported against round 2.",
  "world_is": "Re-run and reported. The needed denominator now equals round 2's exactly. The covered drop (2,090,953 -> 1,297,651) is real and is ruling 1's: the bd and inf price files are BARRED, not a calendar effect. Ruling C's re-run of this lane's pre-2024 artifacts (row S11) is complete: the census here, the links in S16; the round-4 census deliverable under ~12 stays as the record of the fallback run.",
  "notes": "The E3 documents apply also closed this hour (ledger advi-cotbkf-r6-documents-apply-20261007, 11,119 written, read back); it is calendar-free."
}
```

## ADVI_COTBKF-S18 -- DISARMS S12: the applies ran from dell2 against the bucket they actually write (opal-data-assets), each under a never-widen pair and a closed ledger; no write touched opal-data-cottonwood

```json
{
  "id": "ADVI_COTBKF-S18",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T10:30Z",
  "one_line": "DISARMS S12: the applies ran from dell2 against the bucket they actually write (opal-data-assets), each under a never-widen pair and a closed ledger; no write touched opal-data-cottonwood",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "S13 @b9411881a0: the applies resolve to opal-data-assets; 1.0.0_SA_CTO~DELL2 re-ruling msg 264 struck the CT-d-2 wait",
      "ledgers CLOSED 1/1: advi-cotbkf-r5-crosswalk-apply-20261007 @98652475d8; advi-cotbkf-r6-documents-apply-20261007 and advi-cotbkf-e2-account-links-apply-20261007 @3c39c9f4ae",
      "every Put from dell2 on opal-data-assets admitted (crosswalk 2, documents 11,120, account_links 2); no call made under opal-data-cottonwood"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "S12 (BLOCKING, ARMED): no --apply of E3 or E5 from dell2 until a ruling names where they run.",
  "world_is": "Ruled (msg 264) and run; branch A on all three applies.",
  "notes": "Closes this seat's last ARMED row on ADVI_COTBKF."
}
```

## ADVI_COTBKF-W22-S1 -- the order's "today's positions on 2026-06-23" is the Cottonwood account's first holdings dated 2026-06-30; the current side holds nothing dated 2026-06-23 for it

```json
{
  "id": "ADVI_COTBKF-W22-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~22",
  "surfaced_at": "2026-10-07T11:00Z",
  "one_line": "CB-g-2 compares old positions to the current account's first holdings (2026-06-30), the crosswalk's own basis, not to 2026-06-23 positions",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "crosswalk.parquet evidence for 04003450617: current account z0927272491's first holdings (2026-06-30)",
      "silver positions (2026-06-23) holds no current-side account id (z0927272491: 0 rows); FWD8_READ.md cites the holdings date it used"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order cell step 2: the new account's positions are 'today's positions on 2026-06-23'.",
  "world_is": "Current-side holdings for z0927272491 begin 2026-06-30; the read uses them (the matching rule's basis) and states the date."
}
```

## ADVI_COTBKF-W23-S1 -- The applied silver transactions table reads 1,416,497 rows, not the 1,415,137 that W2-S1 says the silver table keeps after dropping 1,360 duplicates

```json
{
  "id": "ADVI_COTBKF-W23-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~23",
  "surfaced_at": "2026-10-07T11:10Z",
  "one_line": "The applied silver transactions table reads 1,416,497 rows, not the 1,415,137 that W2-S1 says the silver table keeps after dropping 1,360 duplicates",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "count_rows over the transactions prefix on 2026-10-07: 1,416,497",
      "coverage.parquet transactions rows=1416497"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "W2-S1: the silver table keeps 1,415,137 rows after dropping 1,360 exact duplicates.",
  "world_is": "The applied transactions prefix counts 1,416,497 rows (dataset count_rows, 14 files) and the applied coverage table reports transactions rows=1,416,497; the 1,360-row drop is not visible in what was applied. The coverage statement reports the applied count.",
  "notes": "Surfaced building TO CB-g-3 (the FWD-6 coverage statement)."
}
```

## ADVI_COTBKF-W23-S2 -- The silver positions table is one snapshot (2026-06-23): 469 positions for 83 of the 1,533 accounts that traded

```json
{
  "id": "ADVI_COTBKF-W23-S2",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~23",
  "surfaced_at": "2026-10-07T11:10Z",
  "one_line": "The silver positions table is one snapshot (2026-06-23): 469 positions for 83 of the 1,533 accounts that traded",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "coverage.parquet positions earliest=latest=2026-06-23 rows=469 distinct_accounts=83"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-6: a reader learns what the backfill holds; positions is read as a history alongside transactions.",
  "world_is": "The positions table holds one AsOfDate (2026-06-23), 469 rows, 83 accounts; the delivery's positions file is a single snapshot, so earlier holdings are rebuilt from transactions (crosswalk, account_links). Stated on the coverage page.",
  "notes": "Surfaced building TO CB-g-3 (the FWD-6 coverage statement)."
}
```

## ADVI_COTBKF-W23-S3 -- 1,544 of the 11,119 indexed documents carry no account: all NCSD (1,239), ADVS (165), REPR (13) and 127 of 932 CLNT

```json
{
  "id": "ADVI_COTBKF-W23-S3",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~23",
  "surfaced_at": "2026-10-07T11:10Z",
  "one_line": "1,544 of the 11,119 indexed documents carry no account: all NCSD (1,239), ADVS (165), REPR (13) and 127 of 932 CLNT",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Counter of doc_type where account is null on document_index.parquet: NCSD 1239, ADVS 165, CLNT 127, REPR 13"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-6: the document index ties each document to an account.",
  "world_is": "document_index account is null for NCSD, ADVS, REPR and 127 CLNT; STMT and TXRP carry one. Stated on the coverage page as a gap; the cause is read from the types, not from the vendor's listing text.",
  "notes": "Surfaced building TO CB-g-3 (the FWD-6 coverage statement)."
}
```

## ADVI_COTBKF-W23-S4 -- The silver coverage table grades only transactions, performance and positions (5 record kinds); nothing in it covers the crosswalk, account_links, documents or bronze

```json
{
  "id": "ADVI_COTBKF-W23-S4",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~23",
  "surfaced_at": "2026-10-07T11:10Z",
  "one_line": "The silver coverage table grades only transactions, performance and positions (5 record kinds); nothing in it covers the crosswalk, account_links, documents or bronze",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "coverage.parquet record_kind values: transactions, performance_month, performance_year, performance_inception, positions"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-6: coverage is the one account of what the backfill holds.",
  "world_is": "coverage.parquet has 5 rows (transactions, performance_month/year/inception, positions). The one-page statement is the only account of the other tables.",
  "notes": "Surfaced building TO CB-g-3 (the FWD-6 coverage statement)."
}
```

## ADVI_COTBKF-W23-S5 -- 14 of the 1,533 accounts in transactions have no performance record (1,519 accounts in performance, none outside transactions)

```json
{
  "id": "ADVI_COTBKF-W23-S5",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~23",
  "surfaced_at": "2026-10-07T11:10Z",
  "one_line": "14 of the 1,533 accounts in transactions have no performance record (1,519 accounts in performance, none outside transactions)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "distinct Account_Number over the silver transactions and performance prefixes on 2026-10-07"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-6: the delivery's performance file covers every transacting account.",
  "world_is": "Set difference of Account_Number: transactions 1,533, performance 1,519, performance-minus-transactions 0, transactions-minus-performance 14 (4876983, B3S728493, RGY006662, VUL1019560 and ten cv-prefixed accounts).",
  "notes": "Surfaced building TO CB-g-3 (the FWD-6 coverage statement)."
}
```

## ADVI_COTBKF-W24-S1 -- The order names "statements" and "tax forms" but no doc_type for either; the page maps STMT to statements and TXRP to tax forms, and TXRP's dates are file-name dates (2025-02-09 to 2026-06-06), not tax years

```json
{
  "id": "ADVI_COTBKF-W24-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~24",
  "surfaced_at": "2026-10-07T12:30Z",
  "one_line": "Statements and tax forms were mapped to STMT and TXRP by reading TO CB-c-2; TXRP carries file-name dates spanning 16 months, not 2 tax years",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver documents.parquet and document_index.parquet on 2026-10-07: STMT 7,736 dated 2025-06-30 to 2026-05-31 (date_source listing:StmtDate); TXRP 1,034 dated 2025-02-09 to 2026-06-06 (date_source file_name)",
      "org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-c-2.document-index.md line 34: STMT (monthly statements), TXRP (tax documents)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-h-1: statements run 12 months and tax forms 2 tax years; spans come from the documents table's doc_type and doc_date.",
  "world_is": "The documents table has no kind column; the order does not say which doc_type is a tax form. The page uses STMT and TXRP. TXRP's doc_date is read from the file name (all 1,034), so its span is a file-date span of 16 months, which may not be the 2 tax years the order states; the tax year sits in the listing fields (row W9-S1). The page prints the span as measured and says the dates come from the file name.",
  "notes": "Surfaced building TO CB-h-1 (the FWD-6 per-kind page)."
}
```

## ADVI_COTBKF-S19 -- MEASURED ABSENCE: opal-data-cottonwood/irpt/cottonwood/ listed to its leaves (725 objects, 205 prefixes, 468,525,549 B) holds 0 per-security daily price stores; FWD-3's price gap is therefore sized from Opal's usable stores alone: 2,914 of 4,634 securities unpriced, 8,091,310 of 9,388,961 security-days uncovered

```json
{
  "id": "ADVI_COTBKF-S19",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T11:15Z",
  "one_line": "MEASURED ABSENCE: opal-data-cottonwood/irpt/cottonwood/ listed to its leaves (725 objects, 205 prefixes, 468,525,549 B) holds 0 per-security daily price stores; FWD-3's price gap is therefore sized from Opal's usable stores alone: 2,914 of 4,634 securities unpriced, 8,091,310 of 9,388,961 security-days uncovered",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "laptop 1.0.0_SA_CTO ran data/assets/scripts/analysis/commonwealth_price_store_scan.py (@d97b008a7c) ~11:12Z; result JSON 222 B (Taildrop C:/Users/Test/Downloads/price_store_scan, sha256 229d8993...; origin copy to follow at deliverables/1.0.0_SA_CTO/price_store_scan): status=LISTED objects=725 prefixes=205 bytes=468525549 candidates=[] security_days_possible=0 need=9388961",
      "dell2 run of the same script: status=DENIED (rc 3) -- the denied branch never read as empty",
      "census on the 2010-2027 calendar (deliverables/2.0.0_SA_COO~C2/census_e2/, row S17): universe=4634 priced_any=1720 security_days_covered=1297651 security_days_needed=9388961",
      "PRD v0.4 ADDENDUM 2 (prd/ADVI_COTBKF_PRD.md:214-222): C-DAILY's source is Yahoo Finance for equity/ETF/fund and Bloomberg at site Z for fixed income and other, on Andrew's word ('i like the yahoo finance vs bloomberg rec'); prices land in MDPF_SECHIST's securities history"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB4d1-AC3: the census is complete -- no unnamed store holding a per-security daily price in a USABLE bucket.",
  "world_is": "The last unlisted USABLE prefix is listed and holds no price store, so the census is complete on a measured absence. The gap: 4,634 - 1,720 = 2,914 securities and 9,388,961 - 1,297,651 = 8,091,310 security-days. CANDIDATE ACT, NOT A CUT: the PRD's C-DAILY sources fill it; any Yahoo or Bloomberg pull is a vendor call that needs Andrew's per-use word (CLAUDE.md Agent Autonomy), and the pull lands in MDPF_SECHIST's store, which is another project's (dell1).",
  "notes": "Two need figures exist and are not the same quantity: 9,388,961 (the census, every security-day in the window) and 3,421,735 (PRICE_NEED @c907766ef4, held security-days by asset type, the figure ADDENDUM 2 cites). The gap above is on the census's basis; a pull would be sized on the held basis."
}
```

## ADVI_COTBKF-S20 -- MEASURED ABSENCE ACROSS BOTH PREFIXES: mdpf/cottonwood/ listed to its leaves (7 objects, 7 prefixes, 57,860 B) holds 0 price stores; with irpt/cottonwood/ (S19, 0 of 725) the Cottonwood bucket holds no per-security daily price store

```json
{
  "id": "ADVI_COTBKF-S20",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T12:05Z",
  "one_line": "MEASURED ABSENCE ACROSS BOTH PREFIXES: mdpf/cottonwood/ listed to its leaves (7 objects, 7 prefixes, 57,860 B) holds 0 price stores; with irpt/cottonwood/ (S19, 0 of 725) the Cottonwood bucket holds no per-security daily price store",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "laptop 1.0.0_SA_CTO ran commonwealth_price_store_scan.py --prefix mdpf/cottonwood/ (@d97b008a7c) ~12:02Z; result JSON 214 B (Taildrop C:/Users/Test/Downloads/price_store_scan_mdpf, sha256 cc698e0a...): status=LISTED objects=7 prefixes=7 bytes=57860 candidates=[] security_days_possible=0 need=9388961",
      "dell2 probe of the same prefix at 11:49Z: status=DENIED (rc 3)",
      "S19: irpt/cottonwood/ status=LISTED objects=725 candidates=[]; S15: the bucket's top level holds only irpt/ and mdpf/"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB4d1-AC3: the census is complete -- no unnamed store holding a per-security daily price in a USABLE bucket.",
  "world_is": "Both Cottonwood prefixes are listed to their leaves and hold no price store. CB4d1-AC3 can grade on a measured absence across the whole firm bucket. FWD-3's gap stays as S19 sized it (2,914 securities; 8,091,310 security-days), pending any internal non-firm store not yet in the census.",
  "notes": "The registry's marketdata system lists historical-prices-daily / historical-prices-yfinance resources not among the census's six legacy stores; whether their output sits in a USABLE (non-firm) bucket is unmeasured. Other firms' stores (49F, INF) stay BARRED: CTO ruling 1 and the CLAUDE.md NEVER on another firm's data."
}
```

## ADVI_COTBKF-D2-W26-S1 -- The registry's marketdata LAMBDA historical-prices-yfinance does not exist live; the one live function is historical-prices-scheduler, which launches an EC2 that runs fetch_historical_prices_yfinance.py

```json
{
  "id": "ADVI_COTBKF-D2-W26-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~26",
  "surfaced_at": "2026-10-07T12:25Z",
  "one_line": "The registry's marketdata LAMBDA historical-prices-yfinance does not exist live; the one live function is historical-prices-scheduler, which launches an EC2 that runs fetch_historical_prices_yfinance.py",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "dell2 default identity, us-east-1, 2026-10-07: lambda get-function-configuration historical-prices-yfinance -> ResourceNotFoundException; lambda list-functions filtered on 'istorical' or 'yfinance' in us-east-1, us-east-2, us-west-2, eu-west-1 -> 1 function, historical-prices-scheduler (no environment variables)",
      "infra/logic/registry/resources.json: the yfinance row's evidence is a census row '/aws/lambda/historical-prices-yfinance' (a log group name), not a function",
      "infra/aws/lambda/historical-prices-scheduler/lambda_function.py:33,58-60: the user-data downloads fetch_historical_prices_yfinance.py from the launcher's bucket and runs it on an ephemeral EC2 tagged historical-prices-fetcher; EventBridge rule historical-prices-daily cron(0 14 * * ? *) ENABLED"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-j-1: a Lambda historical-prices-yfinance exists, and its configuration names where it writes.",
  "world_is": "No such function is live. The script located the writer through the scheduler's repo source (infra/aws/lambda/historical-prices-scheduler) and the script it hands over to (data/black_diamond/scripts/silver/fetch_historical_prices_yfinance.py: S3_BUCKET = os.environ.get('BD_S3_BUCKET', <default>) at line 43, HISTORICAL_PRICES_KEY at line 47, uploaded at lines 431, 549, 783). The MARKETDATA-PRICES line names writer=historical-prices-scheduler; the real writer is the EC2 the scheduler launches. BLIND: the EC2 instance's own environment (it could set BD_S3_BUCKET; the scheduler's user-data does not).",
  "notes": "Surfaced building TO CB-j-1."
}
```

## ADVI_COTBKF-D2-W26-S2 -- MEASURED: marketdata's historical-prices output (silver/historical_prices.parquet) is in opal-data-bd, a bucket alias of the 49financial FIRM scope -- BARRED; it adds 0 securities and 0 security-days to the FWD-3 need, with 0 calls under it

```json
{
  "id": "ADVI_COTBKF-D2-W26-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~26",
  "surfaced_at": "2026-10-07T12:26Z",
  "one_line": "MEASURED: marketdata's historical-prices output (silver/historical_prices.parquet) is in opal-data-bd, a bucket alias of the 49financial FIRM scope -- BARRED; it adds 0 securities and 0 security-days to the FWD-3 need, with 0 calls under it",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python data/assets/scripts/analysis/commonwealth_marketdata_prices.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~26 -> MARKETDATA-PRICES writer=historical-prices-scheduler bucket=opal-data-bd prefix=silver/historical_prices.parquet grade=BARRED barred_read=0 securities=0 security_days=0 gain_securities=0 gain_security_days=0 need=9388961 (rc 0; S3 calls by bucket: none)",
      "infra/logic/registry/scopes.json: scope 49financial (class FIRM) lists alias opal-data-bd with planes [bucket]; grade_buckets (commonwealth_price_census.py:128) grades it BARRED, firm 49financial, plane alias",
      "data/black_diamond/scripts/silver/fetch_historical_prices_yfinance.py:43,47 (bucket default and key)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-j-1 / FWD-3: marketdata's output may sit in a USABLE non-firm bucket and add to the six stores.",
  "world_is": "It sits in a BARRED firm bucket (CTO ruling 1 and the CLAUDE.md NEVER on another firm's data), so it was not listed, headed or read and the gain is 0 by the grade, not by a measured empty store. FWD-3's gap is unchanged from S19: 2,914 of 4,634 securities and 8,091,310 of 9,388,961 security-days unpriced from Opal's usable stores. The registry names the same price tables as 49F's (round 4's PRICE_TABLES_NAMED) -- whether Commonwealth may use a 49financial-held price table (prices are not client positions) is a ruling, not a measurement.",
  "notes": "Surfaced running TO CB-j-1 AC2. The number of securities in that table is not known: it was never read."
}
```

## ADVI_COTBKF-D2-W27-S1 -- MEASURED: 2,914 securities and 8,091,310 security-days are two different sets; the cell's rows number 4,545 and sums_ok is False

```json
{
  "id": "ADVI_COTBKF-D2-W27-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~27",
  "surfaced_at": "2026-10-07T12:50Z",
  "one_line": "MEASURED: 2,914 securities and 8,091,310 security-days do not describe the same set -- 2,914 is the never-priced securities (6,259,410 days); 8,091,310 also holds the gap days of 1,631 priced-but-not-fully-covered securities (1,831,900 days); the rows the cell describes number 4,545",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python data/assets/scripts/analysis/commonwealth_price_need_file.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27 -> PRICE-NEED-FILE securities=4545 security_days=8091310 yahoo_securities=3226 yahoo_days=5773776 bloomberg_securities=1319 bloomberg_days=2317534 sums_ok=False fetched=0 (rc 1); census line it reconciles to: universe=4634 priced_any=1720 security_days_covered=1297651 security_days_needed=9388961 (cache-served, 0 barred calls)",
      "deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.json row_split: never_priced_securities=2914 never_priced_days=6259410; gap_only_securities=1631 gap_only_days=1831900; 2914+1631=4545 and 6259410+1831900=8091310",
      "data/assets/scripts/analysis/commonwealth_price_census.py:235-276 coverage(): priced_any counts a security once ANY store prices it on any day; security_days_covered counts only the days inside its needed window, so a partly priced security is in priced_any and still owes uncovered days"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-k-1 cell text and CB11k1-AC2: for every security with any uncovered day one row is written, the totals are securities=2914 security_days=8091310, and sums_ok is True when the totals equal universe - priced_any and security_days_needed - security_days_covered. AC1's stub (2 fully priced, 1 equity partly covered, 1 bond uncovered) writes 2 rows with sums_ok=True.",
  "world_is": "Days reconcile to the census exactly (8,091,310 = 9,388,961 - 1,297,651). Securities do not: a row for every security with any uncovered day is 4,545, not universe - priced_any = 2,914, because 1,631 of the 1,720 priced securities are priced on only some of their needed days. sums_ok=False is therefore the correct reading of the order's own definition, and AC2's expected prefix securities=2914 cannot be printed without writing rows only for the never-priced securities (then security_days=6259410, not 8091310) or without changing the sums_ok definition. The same contradiction hits AC1's stub: with C partly covered the stub writes 2 rows but universe - priced_any is 1, so sums_ok=False; the tests assert that (test_partly_priced_security_...) and also assert sums_ok=True on a stub whose rows are all never-priced. The refusal clause applied: nothing weakened, the file is written as the cell describes (4,545 rows, source YAHOO 3,226 / BLOOMBERG_SITE_Z 1,319), AC2 is FAIL. Which set MDPF_SECHIST should pull (the 4,545 including gaps, or the 2,914 never-priced alone) is the COO/CTO's ruling; the file carries both splits. Round 10's S19 and D2-W26-S2 state '2,914 securities and 8,091,310 security-days unpriced' as one set; it is two.",
  "notes": "Surfaced building TO CB-k-1. BLIND: whether a vendor prices the gap days of a partly priced security (MDPF_SECHIST's to measure)."
}
```

## ADVI_COTBKF-D2-S21 -- CORRECTS S19's wording: 2,914 securities and 8,091,310 security-days are two different sets. 2,914 are never priced (6,259,410 days); the 8,091,310 uncovered days span 4,545 securities (2,914 + 1,631 partly priced with 1,831,900 gap days)

```json
{
  "id": "ADVI_COTBKF-D2-S21",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T12:55Z",
  "one_line": "CORRECTS S19's wording: 2,914 securities and 8,091,310 security-days are two different sets. 2,914 are never priced (6,259,410 days); the 8,091,310 uncovered days span 4,545 securities (2,914 + 1,631 partly priced with 1,831,900 gap days)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "worker ~27 (branch wk-ADVI_COTBKF-27 @8d3c0fe34f), commonwealth_price_need_file.py on the census basis: PRICE-NEED-FILE securities=4545 security_days=8091310 yahoo_securities=3226 yahoo_days=5773776 bloomberg_securities=1319 bloomberg_days=2317534 fetched=0; row_split 2,914 never-priced / 6,259,410 days + 1,631 gapped / 1,831,900 days",
      "row D2-W27-S1 (BLOCKING, INERT): AC2 as first cut could not be met"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "S19 world_is: 'The gap: 4,634 - 1,720 = 2,914 securities and 9,388,961 - 1,297,651 = 8,091,310 security-days', read as one set; TO CB-k-1 as cut expected securities=2914 security_days=8091310.",
  "world_is": "The day total is right; the security count beside it described a different, smaller set. An issuer's error, carried into S19, the round-10 packet, the round-10 analysis's E1 and CB-k-1. Ruled by the issuer (amendment 1 to CB-k-1): MDPF_SECHIST pulls every uncovered day, so the FILE has 4,545 rows and carries both splits.",
  "notes": "Resolves D2-W27-S1 once CB-k-1's AC2 passes under the amendment."
}
```

## ADVI_COTBKF-D2-S22 -- FWD-1 THREAD RE-TRACED on dell2 after rounds 4-11's applies: both 2026-10-06 traces reproduce (0 rows missing, 0 changed); D49141617 carries 5 more rows, each a C-SILVER-restored repeat; every trace still resolves to its delivered line with sha256_ok=True line_match=True

```json
{
  "id": "ADVI_COTBKF-D2-S22",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T14:17Z",
  "one_line": "FWD-1 THREAD RE-TRACED on dell2 after rounds 4-11's applies: both 2026-10-06 traces reproduce (0 rows missing, 0 changed); D49141617 carries 5 more rows, each a C-SILVER-restored repeat; every trace still resolves to its delivered line with sha256_ok=True line_match=True",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python data/assets/scripts/analysis/commonwealth_account_history.py --account D49141617 --trace 1 (rc 0, 12 s): HISTORY rows=3537 first=2016-01-25 last=2026-06-22; TRACE row=1 line=159882 sha256_ok=True line_match=True",
      "same, --account cv46440182 --trace 25 (rc 0, 6 s): HISTORY rows=56 first=2013-04-29 last=2013-09-10; TRACE row=25 line=410952 sha256_ok=True line_match=True",
      "vs deliverables/2.0.0_SA_COO~C/FWD1_REAL_RUN_D49141617_20261006.txt (rows=3532, pre-C-SILVER silver): 3,532 of 3,532 old rows present and unchanged; 5 extra rows, source_lines 161765, 161767, 161773, 161780, 161784 (2022-12-15 SBR sales), each an exact repeat of an earlier row; cv46440182: 56 of 56 equal",
      "the same two accounts through the applied tables: account_links cvD49141617 -> D49141617 LINKED, cv46440182 NOT_LINKED; crosswalk 2 + 1 rows NOT_MATCHED; documents D49141617 29 (CLNT 14, STMT 12, TXRP 3), cv46440182 0",
      "outputs kept at deliverables/2.0.0_SA_COO~C2/fwd1_retrace_20261007/"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Spine v3.16 drain: re-run the live thread trace once per round and keep its artifact; FWD-1 REALIZED (round 4 analysis).",
  "world_is": "The thread holds on today's applied data. The only movement since 2026-10-06 is the C-SILVER rebuild restoring exact repeats, which FWD-1's account history now shows as the delivery recorded them. Rounds 4-11 skipped this re-trace; this row discharges it.",
  "notes": "FWD-1 stays REALIZED."
}
```

## ADVI_COTBKF-D2-S23 -- CLOSES W6-S5: round 4's CB-d-1 replaced the round-2 census, which read store addresses from a record file because the naming gate refused typed ones, with commonwealth_price_census.py, which reads every legacy store through lib/opal_naming.legacy_address() and deleted the --stores record read

```json
{
  "id": "ADVI_COTBKF-D2-S23",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T14:22Z",
  "one_line": "CLOSES W6-S5: round 4's CB-d-1 replaced the round-2 census, which read store addresses from a record file because the naming gate refused typed ones, with commonwealth_price_census.py, which reads every legacy store through lib/opal_naming.legacy_address() and deleted the --stores record read",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "W6-S5: the round-2 census kept its store addresses in a record file the script read, after the naming gate refused 41 typed literals",
      "TO CB-d-1 (round 4): the new script reads stores only via legacy_address(<key>) over the six registry rows (@4991b8b11b); the --stores read of PRICE_COVERAGE_STORES_20261006.json is REMOVED; commonwealth_price_coverage.py deleted (drain @642222e85f)",
      "the census has run on dell2 three times since (07:53Z, 10:1xZ census_e2, round 11's need FILE) with barred_read=0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "W6-S5 (OPEN since round 2): the store census is kept as a record file the script reads.",
  "world_is": "No script reads that record file any more; the addresses come from the registry builder. Nothing in W6-S5 remains to act on.",
  "notes": "Carried unchanged in the round-6 analysis; closed by its owner (this seat)."
}
```

## ADVI_COTBKF-D2-W28-S1 -- The order's snapshot_pairs is not defined for a security the rebuild holds and the snapshot lacks; the script counts the union (394 pairs, 13 differences) and also records the crosswalk's REBUILD-CHECK basis (381 of 381 equal)

```json
{
  "id": "ADVI_COTBKF-D2-W28-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~28",
  "surfaced_at": "2026-10-07T13:10Z",
  "one_line": "The order's snapshot_pairs is not defined for a security the rebuild holds and the snapshot lacks; the script counts the union (394 pairs, 13 differences) and also records the crosswalk's REBUILD-CHECK basis (381 of 381 equal)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python data/assets/scripts/silver/commonwealth_daily_holdings.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~28 -> DAILY-HOLDINGS accounts=1533 account_days=1691729 holding_rows=23226716 snapshot_accounts=83 snapshot_pairs=394 snapshot_equal=381 snapshot_diffs=13 (rc 0)",
      "deliverables/0.9.0_WK_ADVI_COTBKF~28/daily_holdings.md: REBUILD-CHECK basis pairs=381 equal=381; 13 differences over 3 accounts, all fractional quantities (0.09 to 1.014) the rebuild holds and the snapshot does not list",
      "data/assets/scripts/silver/commonwealth_crosswalk.py:209-219 rebuild_check iterates only the snapshot's own pairs, so it cannot see a rebuilt-open security absent from the snapshot"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-l-1 cell text step 2: compare each snapshot account's rebuilt quantity with the snapshot, non-cash only, write EVERY difference; the final line carries snapshot_pairs, snapshot_equal, snapshot_diffs. The crosswalk's rebuild_check, which the cell says already does this comparison, counts only pairs the snapshot lists.",
  "world_is": "Taking the snapshot's own pairs, the rebuild matches 381 of 381. Taking every non-cash (account, cusip) either side holds for the 83 snapshot accounts, there are 394 pairs and 13 differ: the 13 are securities the transactions leave open in small fractional quantities that the snapshot does not list. The script uses the second reading so that every difference is a row, and the md carries the first reading beside it. Two further rules were chosen where the order is silent: a transaction on a non-trading day takes effect on the next trading day (220 of 3,537 distinct trade dates are non-trading), and an account's span runs to that day when its last transaction is on a non-trading day; a running quantity within 1e-6 of zero is not stored. The last daily state of all 1,533 accounts equals the full rebuild.",
  "notes": "Whether the 13 fractional residues are unrecorded corporate actions (the order's BLIND) or a snapshot that omits fractional lots is not measured here."
}
```

## ADVI_COTBKF-D2-S24 -- cash in lieu is never subtracted from rebuilt holdings

```json
{
 "id": "ADVI_COTBKF-D2-S24",
 "project": "ADVI_COTBKF",
 "fabric": "dell2",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-10-07T15:05Z",
 "one_line": "The shared signed-quantity map (commonwealth_crosswalk.SIGN, imported by commonwealth_daily_holdings) has no entry for transaction type 'leu' (Cash in Lieu), so every fractional share paid out as cash stays in the rebuilt holdings: all 13 of round 12's snapshot differences are exactly that pair's leu quantities, and 515 leu rows across 69 accounts over-state every later day.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "commonwealth_crosswalk.SIGN (imported): 17 types, no 'leu' and no 'ileu' (this compile's read, dell2 CLOUD, 2026-10-07 ~15:0xZ)",
   "deliverables/0.9.0_WK_ADVI_COTBKF~28/snapshot_differences.csv: 13 rows; for each, the sum of that (account, cusip)'s leu quantities in the silver transactions equals the residual, 13 of 13 (this compile's read, dell2 CLOUD, 2026-10-07 ~15:0xZ)",
   "silver transactions: leu 515 rows, all with a quantity, 69 accounts; ileu 267 rows, 1 with a quantity, 97 accounts (this compile's read, dell2 CLOUD, 2026-10-07 ~15:0xZ)",
   "example B3S706372 / 78462F103 (SPY): li 40.324, sl 40, leu 0.324 (2021-01-15/20); li 21.581, sl 21, leu 0.581; li 53.095, sl 53, leu 0.095; the rebuild holds 1.000 after 2023-02-23 (this compile's read, dell2 CLOUD, 2026-10-07 ~15:0xZ)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "C-DAILY step 1: the daily holdings of every account follow its transactions; CB12l1-AC3: one account's daily holdings read right against its transactions across its span.",
 "world_is": "They do not after a cash-in-lieu payout: the fraction sold for cash is never removed. Nothing is served or landed (local files only); the crosswalk's applied table uses the same rule for its pre-exit rebuild, where a stray fraction can only lower a match score.",
 "disarm_owner": "2.0.0_SA_COO~C2",
 "notes": "INERT (no served output). Remedy: SIGN gains leu -1.0 (read ileu's one quantity row to decide it), daily holdings rebuilt with 0 snapshot differences, the account re-read, and the crosswalk re-scored on the fixed rule. Filed by the round-12 compile, which grades CB12l1-AC3 NOT MET on it."
}
```

## ADVI_COTBKF-D2-W29-S1 -- One vendor Transaction_Type is 'csltfee ' with a trailing space, so the ONE signing table has to key it exactly as delivered

```json
{
 "id": "ADVI_COTBKF-D2-W29-S1",
 "project": "ADVI_COTBKF",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_ADVI_COTBKF~29",
 "surfaced_at": "2026-10-07T15:28Z",
 "one_line": "One vendor Transaction_Type is 'csltfee ' with a trailing space, so the ONE signing table has to key it exactly as delivered",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "python data/assets/scripts/analysis/commonwealth_tx_types.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~29 -> types=61; the type reads 'csltfee ' (7 characters plus a space), 164 rows, no quantity on a non-cash CUSIP",
   "a first draft of NO_SHARE_MOVEMENT keyed 'csltfee' and the census listed 'csltfee ' as the one type neither signed nor named (set difference of the 61 delivered types against the table)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO CB-m-1 step 2: every Transaction_Type is decided in the one table, signed or named in NO_SHARE_MOVEMENT.",
 "world_is": "The silver transactions carry the type with a trailing space (164 rows). commonwealth_signs.NO_SHARE_MOVEMENT keys it as 'csltfee ' on purpose. The type moves no shares, so no output depends on it, but a consumer that strips type names would miss the key."
}
```

## ADVI_COTBKF-D2-W29-S2 -- One existing assertion in test_commonwealth_daily_holdings.py ended the DAILY-HOLDINGS line at snapshot_diffs=1; the order puts two fields after it, so that one assertion line was extended

```json
{
 "id": "ADVI_COTBKF-D2-W29-S2",
 "project": "ADVI_COTBKF",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_ADVI_COTBKF~29",
 "surfaced_at": "2026-10-07T15:29Z",
 "one_line": "One existing assertion in test_commonwealth_daily_holdings.py ended the DAILY-HOLDINGS line at snapshot_diffs=1; the order puts two fields after it, so that one assertion line was extended",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "data/assets/scripts/silver/tests/test_commonwealth_daily_holdings.py test_snapshot_with_one_mismatched_pair_writes_that_row: assert line.splitlines()[-1].endswith(\"snapshot_pairs=2 snapshot_equal=1 snapshot_diffs=1\") at 65ce59b838",
   "python -m pytest data/assets/scripts/silver/tests -q -k commonwealth -> 122 passed with that one assertion now ending with 'snapshot_diffs=1 fractional_residuals=0 fractional_accounts=0'"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO CB-m-1 tests: every existing test of the three scripts keeps passing; the last line gains fractional_residuals and fractional_accounts after the existing fields.",
 "world_is": "Both cannot hold for that one assertion: an endswith on the old last field fails once fields follow it. The test file is in the order's paths; every other existing assertion of the file is unchanged. No test was weakened: the new assertion checks the whole tail of the line."
}
```

## ADVI_COTBKF-D2-W29-S3 -- The account_links rule change moves 52 rows' reason (51 'no in-kind receiver' rows mostly become 'closed to cash') that the order's compared fields (status, new_account) do not count; the diff reports them beside the counts

```json
{
 "id": "ADVI_COTBKF-D2-W29-S3",
 "project": "ADVI_COTBKF",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_ADVI_COTBKF~29",
 "surfaced_at": "2026-10-07T15:39Z",
 "one_line": "The account_links rule change moves 52 rows' reason (51 'no in-kind receiver' rows mostly become 'closed to cash') that the order's compared fields (status, new_account) do not count; the diff reports them beside the counts",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "python data/assets/scripts/analysis/commonwealth_rule_change_diff.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~29 -> account_links_changed=2 while CLASS lines read 'closed to cash: 495 -> 544' and 'no in-kind receiver: 51 -> 2' and INFO 'account_links reason differs on 52 rows'",
   "control: both scripts re-run with the OLD tables (crosswalk SIGN and HOLDING_SIGN as at 65ce59b838) give crosswalk_changed=0 account_links_changed=0 against the applied tables (439 matched, 212 linked), so every difference is the rule change and none is input drift (scratch run, .scratch/rcd_control.py, uncommitted)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO CB-m-2 step 3: account links are compared by old_account on status and new_account; the last line counts those changes.",
 "world_is": "Those two fields moved on 2 rows (one gained link, one lost). The reason text, end_positions and score moved on 52, 87 and 52 rows with status unchanged, because the one table adds `ci` (Contribution to Income) to the link rebuild: the old links table with `ci` added gives account_links_changed=2 (the same 2 rows), with `12b1` added 0 (scratch ablation). The diff keeps the order's counts and adds an INFO line per extra field (reason_code, positions_compared, positions_matched, holdings_basis for the crosswalk; reason, end_positions, matched, score for the links) so a reason shift is not read as no change."
}
```

## ADVI_COTBKF-D2-S25 -- The round-14 re-apply on the one signing table moves the crosswalk's near-match list from 21 to 22 entries; the list put to Andrew for Cottonwood (deliverables/0.9.0_WK_ADVI_COTBKF~14/near_matches.md) is now one entry short

```json
{
  "id": "ADVI_COTBKF-D2-S25",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T16:02Z",
  "one_line": "The round-14 re-apply on the one signing table moves the crosswalk's near-match list from 21 to 22 entries; the list put to Andrew for Cottonwood (deliverables/0.9.0_WK_ADVI_COTBKF~14/near_matches.md) is now one entry short",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "crosswalk --apply 15:57Z (ledger advi-cotbkf-r14-reapply-crosswalk-links-20261007): CROSSWALK matched=471 not_matched=1062 ambiguous=38 near_matches_applied=0 near_matches=22",
      "round 4 (CB-d-3) near_matches=21; the near-match list in the round-6/7 analyses and the FWD-8 read carries 21 'awaiting a person'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-8 (REALIZED round 7): the 21 near-matches are left for a person, never linked.",
  "world_is": "Near-matches are still never linked (near_matches_applied=0). The fixed signs changed one account's scores into the 0.65-0.8 band, so the person's list needs the 22nd entry; the near-match file is regenerated by any crosswalk run (.scratch/advi_cotbkf/r14_crosswalk_apply/near_matches.*).",
  "notes": "For the CTO: the list sent toward Andrew/Cottonwood should be refreshed to 22 before it reaches the firm."
}
```

## ADVI_COTBKF-D2-W30-S1 -- All 5 fractional residuals equal the 2026-06-23 snapshot quantity of their pair; RGY007151's single li is classed SOURCE_GAP by structure

```json
{
  "id": "ADVI_COTBKF-D2-W30-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~30",
  "surfaced_at": "2026-10-07T16:40Z",
  "one_line": "All 5 fractional residuals equal the 2026-06-23 snapshot quantity of their pair, so none is a rebuild error; the order's three classes name a delivery defect, and RGY007151's single li is classed SOURCE_GAP by structure (no row takes it out) though nothing is shown missing",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python data/assets/scripts/analysis/commonwealth_residuals_explain.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~30 -> RESIDUALS explained=5 of 5 sign_gap=0 vendor_rounding=4 source_gap=1; each pair line ends 'snapshot holds <q> (equal to the rebuild)': 0.029, 0.02, 0.00086, 0.00086, 0.003",
      "B3S605716 and B3S622848: CAF rows sum to 20479.60514 (5 decimals) and the closing lo is 32000.164 (3 decimals) against 32000.16486 held before it; B37631286 and B3S706372: the 2026-05-29 dvr (3.485 / 2.458) re-books a cancelled dvr (DVRX 3.456 / 2.438) by 0.029 / 0.020 more, and the 2026-06-02 sl (861.008 / 607.405) is the position before the re-booking"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-n-1: each of the 5 residuals is a SIGN_GAP, VENDOR_ROUNDING (quantities delivered do not net to zero) or SOURCE_GAP (a row the pair needs is not in the delivery).",
  "world_is": "The snapshot, a second custodian record, holds the same fractions, so the rebuild reproduces the custodian's figure on all 5 and no sign change is indicated (sign_gap=0; the snapshot is 381 of 381 equal, not re-run because commonwealth_signs.py is unchanged). Four pairs are VENDOR_ROUNDING (two sales sized to the position before a dvr re-booking; two final lo rows delivered to 3 decimals against 5-decimal CAF rows). RGY007151 (TOIXX, one li of 0.003 on 2025-10-08, held in the snapshot) has no out row and nothing implies a missing one; SOURCE_GAP is the only class whose definition fits an inbound-only pair, and the report says so.",
  "notes": "A grader who reads RGY007151 as a real 0.003 holding rather than a gap can re-class it; the script's rule is structural (every signed row inbound)."
}
```

## ADVI_COTBKF-D2-S26 -- The served document index carries no page count: page_count is 0 or empty for all 11,119 documents

```json
{
  "id": "ADVI_COTBKF-D2-S26",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T18:50Z",
  "one_line": "silver document_index.page_count sums to 0 over 11,119 documents in every doc_type (ADVS, CLNT, NCSD, REPR, STMT, TXRP), so the served index cannot say how long any document is",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "read of s3://opal-data-assets/commonwealth/cottonwood/silver/document_index/date=2026-06-23/document_index.parquet (boto3 get_object, pandas): 11,119 rows; groupby(doc_type).page_count.sum() = 0.0 in all 6 types; the column is int64 in the schema"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-5: a person searches by account, type and date and opens the one document they need; the index carries page_count as a field.",
  "world_is": "The documents open (11,119 VERIFIED in silver documents) and search works, so FWD-5 stands as realized; the page_count field is present but never filled. A one-cell enrichment (count pages from the served PDFs) would fill it.",
  "notes": "Found by the issuer while answering Andrew's status question, not by a task order. Offered to 1.0.0_SA_CTO~DELL2 for the next enrichment list."
}
```

## ADVI_COTBKF-D2-W33-S1 -- The order says a flow's amount is its Amount; the module uses direction x |Amount| because the Amount sign convention on the silver transactions is not documented anywhere the worker may read

```json
{
  "id": "ADVI_COTBKF-D2-W33-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~33",
  "surfaced_at": "2026-10-07T19:54Z",
  "one_line": "The order says a flow's amount is its Amount; the module uses direction x |Amount| because the Amount sign convention on the silver transactions is not documented anywhere the worker may read",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/silver/commonwealth_flows.py: flow_amount(); data/assets/scripts/silver/tests/test_commonwealth_daily_returns.py: test_signed_amount_gives_the_same_flow_as_unsigned passes (lo -20.0 and lo 20.0 both give flow -20)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-p-2 step 1: the flow amount of a row is its Amount.",
  "world_is": "No file in the silver scripts or the order records whether Amount is stored signed (a withdrawal negative) or unsigned (like Quantity). A bare Amount read as signed would turn an unsigned lo into an inflow. commonwealth_flows.flow_amount returns direction x |Amount| (direction from the flow table; for share-moving types it equals commonwealth_signs.SIGN), which equals the signed Amount when the vendor signs it and is right when the vendor does not; it is wrong only for a row booked with the opposite sign to its type (a negative-Amount li). The first real run should count flow rows by type and sign of Amount before the grade is trusted."
}
```

## ADVI_COTBKF-D2-W33-S2 -- commonwealth_daily_holdings.load_tx_pos() cannot supply the flows: cw.TX_COLS has no Amount, so the returns script has its own four-column loader

```json
{
  "id": "ADVI_COTBKF-D2-W33-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~33",
  "surfaced_at": "2026-10-07T19:54Z",
  "one_line": "commonwealth_daily_holdings.load_tx_pos() cannot supply the flows: cw.TX_COLS has no Amount, so the returns script has its own four-column loader",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/silver/commonwealth_crosswalk.py:444 TX_COLS; data/assets/scripts/silver/commonwealth_daily_returns.py: load_tx()"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-p-2 step 2: read silver transactions with commonwealth_daily_holdings.load_tx_pos().",
  "world_is": "load_tx_pos() projects commonwealth_crosswalk.TX_COLS (Account_Number, Cusip, Symbol, Quantity, Trade_Date, Transaction_Type, Advisor_ID) and the cache written from it has no Amount column. commonwealth_daily_returns.load_tx() reads Account_Number, Trade_Date, Transaction_Type and Amount from the cache only when the cache carries Amount, else from the silver transactions table on S3 (read-only, same prefix and reader as load_tx_pos). Not exercised on real data this round (stub only); the first real run reads S3 once for four columns."
}
```

## ADVI_COTBKF-D2-W32-S1 -- the census reader keeps no price column; the valuation re-reads the stores with a price-keeping cleaner

```json
{
  "id": "ADVI_COTBKF-D2-W32-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~32",
  "surfaced_at": "2026-10-07T20:04Z",
  "one_line": "the census read_store keeps no price (its cleaner drops the column) and the cached store frames are priceless, so the valuation re-reads the six stores from S3 with the cleaner swapped in memory",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/analysis/commonwealth_price_census.py _clean returns only kind,key,day,source; .scratch/price_census_cache/*.parquet columns = ['kind','key','day','source'] (6 files read with pandas)",
      "first run of data/assets/scripts/silver/commonwealth_daily_valuation.py read the six stores read-only from S3 (cold 1m45s, over the 120 s bound once; cached reruns 74 s); inside one store 2204 gold-holdings and 3753 silver-canonical-prices security-days carry disagreeing rows (silver (max-min)/min median 4.6, i.e. the highest row is typically 5.6 times the lowest) and are left unpriced; gold had a further ~31,000 float32-noise disagreements (relative < 1e-6) that PRICE_TOL now treats as one price"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB-p-1: prices come from the six census stores via STORES, read_store (or load_store_cached), symbol_claims, match_security -- the cache at .scratch/price_census_cache is usable.",
  "world_is": "read_store/load_store_cached return day keys without prices, so no valuation can come from them or their cache. The script imports the census module, swaps pc._clean for a price-keeping variant for the duration of the read, and caches the priced frames under <data-dir>/price_cache. Nothing in the census file is edited. Same-key-day disagreement inside a store (silver 3753, gold 2204) is a data question for whoever owns the price load: the script blanks those days rather than choose.",
  "notes": "The 3753 silver conflicts differ by a median factor of 5.6 (highest row over lowest), which looks like two different securities or units under one key and day, not rounding."
}
```

## ADVI_COTBKF-D2-S27 -- Security transfers in and out mostly carry no Amount, so once prices land their days will read FLOW_UNVALUED instead of a return

```json
{
  "id": "ADVI_COTBKF-D2-S27",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T20:52Z",
  "one_line": "Of the external-flow rows, lo 18,157 / trco 147 (all) / trfo 611 / li 1,424 / trfi 60 carry Amount 0; CB-p-2 blanks such a day (FLOW_UNVALUED), so today only 101 days are blanked for it because the rest are already UNPRICED",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "issuer census on the drained code (b07434a3f5): external flow rows by sign of Amount -- li 59,720 positive / 1,424 zero; lo 31,532 / 18,157; trfo 1,298 / 611; trfi 2,613 / 60; trco 0 / 147; ftax 4,156 NEGATIVE / 56 positive; stax 112 negative",
      "real run: DAILY-RETURNS account_days=1691729 computed=127300 blank=1564429; blank_reason UNPRICED 1,560,217, ZERO_BASE 2,578, FIRST_DAY 1,533, FLOW_UNVALUED 101"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-p-2: a flow's amount is its Amount; a flow row with Amount zero or null blanks that day (FLOW_UNVALUED).",
  "world_is": "Amount is unsigned for the in/out types (direction comes from the type, as the worker built) but signed negative for ftax/stax; a security transfer usually carries no Amount at all, so its value is quantity x that day's close, which step 2 already has. Answers W33-S1: direction x |Amount| is right for every type measured.",
  "notes": "Enrichment candidate: value a zero-Amount security flow at quantity x the same-day close from the valuation step; still blank when that close is missing."
}
```

## ADVI_COTBKF-D2-S28 -- On the 4,231 months graded today, months with a flow mostly DIFF (866 of 1,138, median |diff| 7.4 pct pts); months with no flow MATCH 1,675 of 3,093

```json
{
  "id": "ADVI_COTBKF-D2-S28",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-07T20:52Z",
  "one_line": "The monthly grade on the stores Opal already holds: 1,947 MATCH, 2,284 DIFF, 78,362 UNGRADABLE (a blank day); the DIFFs concentrate in months with an external flow, so the end-of-day flow convention or a flow class is off",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "MONTHLY-GRADE months=82593 match=1947 diff=2284 ungradable=78362 tolerance_pct=0.05 (shared tree after the drain, b07434a3f5)",
      "graded months by has-flow: no flow MATCH 1,675 DIFF 1,418 (median |diff| 0.353); with flow MATCH 272 DIFF 866 (median |diff| 7.445); 280 accounts graded, 57 with 12 or more MATCH months"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "C-DAILY step 4: the days chained per month give Commonwealth's monthly return, MATCH within the stated tolerance or DIFF with its reason.",
  "world_is": "Chaining works where nothing enters or leaves (half of no-flow months MATCH inside 0.05 points); a month with a flow is usually far off, which points at the flow (timing: end of day vs start of day; class: ftax/stax as external; sign) rather than the prices.",
  "notes": "Enrichment candidate: grade the flow months under start-of-day vs end-of-day flow and with tax withholding internal, and keep the convention that MATCHes more; a DIFF still carries its reason."
}
```

## ADVI_COTBKF-D2-W36-S1 -- The order reads the empty page_count as 10,072 listings with no NumberOfPages and 1,034 with "0"; 13 more (all 13 REPR documents) carry a value that is not a number

```json
{
  "id": "ADVI_COTBKF-D2-W36-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~36",
  "surfaced_at": "2026-10-07T22:17Z",
  "one_line": "The order's 10,072 + 1,034 leaves 13 documents of the 11,119 unaccounted: every REPR listing carries NumberOfPages as a non-number (5 'W', 5 'Barnett', 3 empty), a shifted column in the REPR listing",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/analysis/commonwealth_page_counts.py run on the served index: ADVS 165 / CLNT 932 / NCSD 1239 / STMT 7736 absent key, TXRP 1034 '0', REPR 13 other; sums 10,072 + 1,034 + 13 = 11,119",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~36/page_counts.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-q-3: 10,072 listings carry no NumberOfPages and 1,034 carry it as '0'.",
  "world_is": "Those two counts hold, and 13 more listings (REPR) carry the field with a non-numeric value, which the index's _int() turns into null. The script folds them into listing_none on the PAGE-COUNTS line (10,085) and shows them apart in page_counts.md. No listing in any doc type carries a positive value, so the cause (absent: no positive NumberOfPages in any listing) is unchanged; all 13 REPR PDFs are counted from their bytes."
}
```

## ADVI_COTBKF-D2-W35-S1 -- on the real run the zero-Amount valuation newly grades 6 months, all DIFF, all lo/li; no trf* row sits in a newly graded month

```json
{
  "id": "ADVI_COTBKF-D2-W35-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~35",
  "surfaced_at": "2026-10-07T22:24Z",
  "one_line": "Zero-Amount flow rows 20,403, valued 5,017, blank for no price 15,386; only 6 account-months move from UNGRADABLE to graded (all DIFF, 2,284 -> 2,290; MATCH unchanged at 1,947), each carries an lo or li row, none a trf* row, so the order's 'transfer' example month is an lo",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "DAILY-RETURNS account_days=1691729 computed=127396 blank=1564333 flow_types=61 of 61 zero_amount=20403 valued=5017 blank_no_price=15386 (computed 127,300 -> 127,396)",
      "monthly grade over the same performance rows before/after: UNGRADABLE 78,362 -> 78,356, DIFF 2,284 -> 2,290, MATCH 1,947 -> 1,947; valued rows by type li 458, lo 4,474, trco 27, trfi 15, trfo 43, si/so 0; no valued row has Quantity 0 or a cash CUSIP"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-q-1 item 4: one account-month containing a valued zero-Amount transfer, fully priced, blank before and computed and graded after.",
  "world_is": "Most months holding a zero-Amount row stay blank for another reason (an unpriced holding, or 15,386 rows with no same-day price). The only months that become fully priced are 6, all lo/li (securities in or out of the account); the worked month is B3S703388 2025-09 (lo of 21 shares of 594918104 at 508.037384 = -10668.785065, UNGRADABLE -> DIFF computed 0.7664 vs reported 0.84). Also: the transactions cache (cache/transactions.parquet) has no Amount, so the returns script reads Account_Number, Trade_Date, Transaction_Type, Amount, Cusip, Quantity from S3 (read-only) as before."
}
```

## ADVI_COTBKF-D2-W35-S2 -- the start-of-day negative-base rule blanks days after a negative prior-day value that the end rule computes; the no-flow control holds only on the months graded under both

```json
{
  "id": "ADVI_COTBKF-D2-W35-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~35",
  "surfaced_at": "2026-10-07T23:36Z",
  "one_line": "The order's start-of-day rule (zero or negative base stays ZERO_BASE) blanks 26,903 days that the end rule computes, all after a NEGATIVE prior-day value, so 416 no-flow months graded under end are blank under start and the control 'every no-flow month grades identically' holds only on the months graded under both",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "start run: ZERO_BASE 29,668 account-days against 2,578 under end; 27,112 days computed under end and ZERO_BASE under start, of which 25,499 have flow 0 and 26,903 have prev < 0 (209 have prev > 0 with a large outflow); account_day_value.parquet carries 27,672 negative values over 637 accounts",
      "graded months: end 4,237, start 3,614, both 3,613, end only 624 (208 flow, 416 no-flow, 291 MATCH under end), start only 1; commonwealth_flow_timing.py prints these as excluded_graded_one_side_only"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-q-2 item 1 and AC2: start of day is value_t / (value_(t-1) + flow_t) - 1 with a zero or negative base ZERO_BASE, and the no-flow control grades identically under both timings (control_same=True).",
  "world_is": "The end rule blanks only value_(t-1) == 0, so an account whose prior-day value is negative (an overdrawn cash line, a short position) gets a computed return under end (flat -498.20 reads 0.0) and a blank under start. The two conventions are the same formula on a no-flow day, so the gap is the base rule, not the timing. The script compares the months graded under BOTH (control_same=True over 2,676 months) and states the 624 excluded months in flow_timing.md; whether a negative base should be blank under end too (which would move the round 16 grade, 4,237 months, by about 624) is a ruling for the CTO, not made here. The default FLOW_TIMING stays end."
}
```

## ADVI_COTBKF-D2-W39-S1 -- largest DIFF flow class lo/over 10%: value falls by twice the withdrawal (lo of CFNCASH paired with sl of the FDIC sweep)

```json
{
  "id": "ADVI_COTBKF-D2-W39-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~39",
  "surfaced_at": "2026-10-08T03:32Z",
  "one_line": "In the largest DIFF flow class (lo/over 10%, 252 months) the account value falls by TWICE the withdrawal on the flow day in 74 of 106 single-lo months (once in 2), because the lo row (CFNCASH) is paired with an sl row of the FDIC sweep for the same amount",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "FLOW-DIFF-CLASSES diff_flow_months=857 classes=8 largest=lo/over 10% largest_months=252 examples=3 (deliverables/0.9.0_WK_ADVI_COTBKF~39/flow_diff_classes.md)",
      "single-lo months of the class with a computed flow day: 106; value drop == 2 x |flow| (within 1% + 0.05): 74; == 1 x |flow|: 2",
      "0QF879352 2023-07-14: lo 455.68 CFNCASH qty 455.68 and sl 455.68 FDIC66606 qty 455.68; value 1395.47 -> 484.11, drop 911.36 = 2 x 455.68; day return -0.326542 vs reported month -0.18"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-r-3 item 1: the DIFF flow months are explained by flow type and size; the holdings chain values the withdrawal once (the lo takes value out, the paired sl is internal).",
  "world_is": "A withdrawal of cash is booked as lo of CFNCASH plus an sl of the FDIC sweep for the same quantity. The holdings fall by both legs (the sl removes the sweep and the lo removes cash that the sl never credited), so the value falls by twice the flow while the return subtracts the flow once. This is the holdings side (commonwealth_signs / daily_holdings), not the flow rule; no fix made here."
}
```

## ADVI_COTBKF-D2-W39-S2 -- order's 937 / 242 flow-month population differs from the grade's 1,173 / 316

```json
{
  "id": "ADVI_COTBKF-D2-W39-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~39",
  "surfaced_at": "2026-10-08T03:49Z",
  "one_line": "The order's flow-month population (937 fully priced flow months, 242 MATCH) is not reproducible from the committed chain: months graded MATCH or DIFF that carry an external-flow row are 1,173 (316 MATCH, 857 DIFF); with a nonzero daily flow 1,145 (297 MATCH, 848 DIFF)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "MONTHLY-GRADE months=82593 match=1973 diff=2264 ungradable=78356 tolerance_pct=0.05 reproduced exactly from the three chain scripts at defaults",
      "flow_diff_classes.md: Months graded MATCH with a flow: 316; DIFF flow months 857; daily_returns flow != 0 months graded: MATCH 297, DIFF 848, UNGRADABLE 22,869; 28 classed months carry a flow row but no nonzero daily flow (net zero or off the value span)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-r-3 cell text: on the fully priced months, months with an external flow MATCH 242 of 937 (median |diff| of the DIFFs 6.3 points).",
  "world_is": "No definition of 'fully priced flow month' over the committed grade gives 937 / 242; this script's denominator is every graded (MATCH or DIFF) month with at least one external-flow row, stated in flow_diff_classes.md. The class ranking does not depend on the gap."
}
```

## ADVI_COTBKF-D2-S29 -- the sweep re-grade moves 163 months MATCH -> DIFF

```json
{
  "id": "ADVI_COTBKF-D2-S29",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-08T17:38Z",
  "one_line": "The sweep-is-cash re-grade (CB-s-1) moves 163 months MATCH -> DIFF beside 543 DIFF -> MATCH; the worker did not investigate the 163",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/0.9.0_WK_ADVI_COTBKF~40/sweep_regrade.md lines 692-702: DIFF -> MATCH 543, MATCH -> DIFF 163, DIFF -> UNGRADABLE 31, MATCH -> UNGRADABLE 10, UNGRADABLE -> graded 4",
      "same file, control: 642 of 642 graded months of accounts with no listed-sweep row on or before the month unchanged; the literal in-month reading has 919 months, 158 moved, all in accounts that traded a sweep earlier",
      "SWEEP-REGRADE sweeps=2 rejected=517 double_drop_months=74 fixed=42 months_before=1685/1931/78977 months_after=2057/1522/79014 control_same=True (drained @bf424e274b)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CTO round-18 ruling (msg 1237 @04b347e9ea): sweep balances are cash and sweep buys/sells INTERNAL, so a sweep-funded withdrawal moves the value once; the re-grade should repair DIFF months, not break MATCH months.",
  "world_is": "Net MATCH rises 1,685 -> 2,057, but 163 months that matched Commonwealth before now DIFF. Unexplained: a candidate is that sweep balances counted as cash at 1.0 now enter the value in months where the earlier chain left them unpriced or cancelling, so a month that matched by offsetting errors no longer does. Classing the 163 is an enrichment candidate for the round-19 analysis."
}
```

## ADVI_COTBKF-D2-S30 -- L9 CB19s1-AC3 MET; Fidelity Government Cash Reserves trades like a core sweep (232 accounts), off the list by the ruling's bank-only scope

```json
{
  "id": "ADVI_COTBKF-D2-S30",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-08T17:47:16Z",
  "one_line": "L9 CB19s1-AC3 MET (the sweep list is a declared list of two bank deposit sweeps; no rejected candidate is a bank sweep by its source). Beyond the criterion: 316067107 Fidelity Government Cash Reserves trades like a custodian core sweep across 232 accounts and is off the list only because the round-18 ruling covers bank sweeps.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_19_L9_GRADE_20261008.md",
      ".scratch/advi_cotbkf/cache/transactions.parquet (1,416,497 rows, dell2): 316067107 8,768 rows, 232 accounts, 2023-03-17..2026-06-22, dv 3,410 / dvr 3,292, 91% of rows on an account-day with another CUSIP traded (FDIC66606 75%, FDIC66853 78%)",
      "1.0.0_SA_CTO~DELL2 round-18 analysis @04b347e9ea section 1: 'A bank sweep is the account's cash parked in an interest-bearing vehicle ... sweep vehicles are cash'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Round-18 ruling: sweep vehicles are cash, their buys and sells INTERNAL, by a declared list.",
  "world_is": "The list holds the two bank deposit sweeps. A money-market core position that behaves as a sweep for 232 accounts is valued as a priced holding and its buys and sells count as trades; whether it is a sweep vehicle under the ruling is the CTO's call (wider than the packet's 6-month enrichment item 2)."
}
```

## ADVI_COTBKF-D2-W41-S1 -- CB-t-2: no custodian designation of 316067107 as a core position is citable; the (b) entry stays OFF, sweeps-v2 = sweeps-v1 in membership

```json
{
  "id": "ADVI_COTBKF-D2-W41-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~41",
  "surfaced_at": "2026-10-08T18:17:38Z",
  "one_line": "CB-t-2: the ruling lands 316067107 on the list under rule (b) only with the custodian's designation; none exists in the repo or in the silver fields the chain reads, so the entry is off and the 163 movers are unchanged under v2.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-t-2.sweeps-v2-core.md (item 1: 'if none can be cited, leave it off, and say so in the report and a row')",
      "S3 opal-data-assets commonwealth/cottonwood/silver/transactions (read-only, column projection): 316067107 Position_Type CASH 8,761 / DIVIDENDS_BOND_INTEREST_ACCUMULATION 7 of 8,768 rows, but Position_Type is CASH on 1,408,059 of the table's 1,416,497 rows for every security (cash/margin side, not a core flag); Asset_Type 'Cash Equivalent' is shared by all money-market funds; FundCode CTC1260; Transaction_Note carries trade wording only. Silver positions: Position_Type CASH, Account_Status 0.",
      "repo search by CUSIP and by 'core position' (org/, docs/, data/): the CTO round-19 analysis and the CVO round-19 grade call it core on behavior; org/tier1_exec/1.0.0_SA_CTO/logs/2026-04-20/aua_active_filter_investigation_and_brief.md names it 'Fidelity Phillips Street Trust Govt Cash Resv' as an asset bought, not as a designated core; data/inf/config/ticker_lookup.json maps FDRXX to the name only.",
      "deliverables/0.9.0_WK_ADVI_COTBKF~41/v2/sweep_regrade.md: SWEEP-REGRADE months_before=2057/1522/79014 months_after=2057/1522/79014 control_same=True; the 163 movers: core 16 / other_mmf 0 / neither 147 all still DIFF"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The CTO ruling: 316067107 goes on sweeps-v2 under (b) with the custodian's own documentation or account data naming it the core position; if no designation can be cited the entry does not land.",
  "world_is": "No such documentation or field is readable. The behavior census (232 accounts, 8,768 rows, 91.1% same-day paired, dividends in 40 months) is the CVO's measure and informs; it is not a designation. A statement or custodian document held outside the repo, or a vendor field not in the silver tables, would let the entry land by one dict entry (rule b, designation_source set) and a re-run."
}
```

## ADVI_COTBKF-D2-W41-S2 -- CB-t-2: sweeps-v2 version bump breaks one CB-t-1 test outside the CB-t-2 write grant

```json
{
  "id": "ADVI_COTBKF-D2-W41-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~41",
  "surfaced_at": "2026-10-08T18:17:38Z",
  "one_line": "test_the_arm_options_default_to_round_19 in test_commonwealth_mover_classes.py (my CB-t-1 test) pins ARM_LISTS['v1'] to the current SWEEP_LIST_VERSION; v2 is now current, so it fails; the file is not in CB-t-2's paths.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -m pytest -q data/assets/scripts/silver/tests (this worktree, after the CB-t-2 edits): 1 failed, 513 passed, 11 skipped; the one failure is data/assets/scripts/silver/tests/test_commonwealth_mover_classes.py::test_the_arm_options_default_to_round_19",
      "ARM_LISTS['v1'] is now (rule 'list', sweeps-v1-20261008) as the CB-t-2 order requires (v1 stays reachable); the test asserted it equal to (rule 'list', sw.SWEEP_LIST_VERSION)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB-t-1 test: the runner's v1 option reproduces round 19, pinned as equal to the current SWEEP_LIST_VERSION.",
  "world_is": "The pin was over-coupled to the module's current-list name. The honest assertion is ARM_LISTS['v1'] == (RULE_LIST, sw.SWEEP_LIST_V1_VERSION). Not edited here: the file is outside the CB-t-2 grant. The CB-t-1 proof (AC1: 9 passed at 101fb91b59) was true at that commit. The issuer can widen the grant by one line or fold the one-line fix into a later order."
}
```

## ADVI_COTBKF-D2-W41-S3 -- CB-t-2: remediation of ADVI_COTBKF-D2-W41-S2 (arm test re-pinned to SWEEP_LIST_V1_VERSION)

```json
{
  "id": "ADVI_COTBKF-D2-W41-S3",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~41",
  "surfaced_at": "2026-10-08T18:45:00Z",
  "one_line": "Corrects ADVI_COTBKF-D2-W41-S2: after the issuer ruling (amendment c6e1cae6d3) the test now asserts against sw.SWEEP_LIST_V1_VERSION; S2 is REMEDIATED by this commit.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_mover_classes.py: 9 passed",
      "python -m pytest -q data/assets/scripts/silver/tests: 514 passed, 11 skipped"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "ADVI_COTBKF-D2-W41-S2 was UNDER_INVESTIGATION: the CB-t-1 arm test pinned ARM_LISTS['v1'] to the current list version and failed once v2 landed.",
  "world_is": "Fixed at line 113 of test_commonwealth_mover_classes.py (SWEEP_LIST_VERSION -> SWEEP_LIST_V1_VERSION) in the same commit as this row. The row gate bars in-place mutation of S2, so its disposition is closed by this new row citing the old id; S2 itself is unedited."
}
```

## ADVI_COTBKF-D2-W42-S1 -- CB-u-1: sweep-balance movers carry an unfunded cash debit (a sweep buy funded by a non-sweep sale)

```json
{
  "id": "ADVI_COTBKF-D2-W42-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~42",
  "surfaced_at": "2026-10-08T18:48:41Z",
  "one_line": "CB-u-1: the sweep-balance movers carry a cash DEBIT for a sweep buy whose funding sale (a non-sweep security) never credits cash, so the after-arm base shrinks; the fix lies in the chain's cash legs, not in the sweep list.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~42/mover_causes.md trace sweep_balance D49141714 2019-02: value before 4061.90 / after 51.04 on every no-trade day, D = -4010.86; reported 0.04 pct, before 0.0416, after 3.3111",
      "silver transactions of D49141714 (local cache): FDIC66606 buys minus sells on or before 2019-02-28 = 4010.86, equal to -D; the funding of the 2019-01-24 sweep buy of 3840.59 is a SALE of 30306A436 (a non-sweep security, 562 shares), and commonwealth_sweeps.sweep_cash_rows adds cash legs for listed-sweep trades only",
      "mover_causes.parquet (this deliverable): 106 of 147 `neither` movers have s < 0 (the before arm sat above the after arm), 41 s > 0; 72 sweep_balance, 75 other:sweep_trade_day, offsetting 0 (only 2 of 147 months carry a nonzero flow-component error e_f)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "E1 (round-20 analysis): a mover may have matched before only because two errors offset, in which case DIFF is the truer state and the fix lies elsewhere in the chain.",
  "world_is": "Under the stated rule no month is `offsetting` (the before-state's value-change and flow-taken-out components are not off in opposite directions). The movers are carried by the sweep balance and by sweep-trade days. In the largest-|s| sweep_balance month the after arm debits cash for a sweep purchase (type LIX on CFNCASH) but the sale of the non-sweep security that paid for it credits nothing, so cash goes negative and cancels the sweep position: the after-arm value is the before-arm value minus the sweep balance. This is a reading of ONE traced account; how many of the 147 share it is not measured here (no fix and no wider census in this order)."
}
```

## ADVI_COTBKF-D2-S31 -- the mover-causes invocation depends on the data-dir's last arms

```json
{
  "id": "ADVI_COTBKF-D2-S31",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-08T19:00Z",
  "one_line": "CB21u1-AC2's invocation reads day values from the runner's default --data-dir, so its result depends on which arms ran there last: on the trunk it gave sweep_balance=0 other=147 (all other:unexplained) until the none->v1 arms were rebuilt, then 72/0/75, equal to the worker",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "trunk run 1 after the drain @0aefdc2e8e: MOVER-CAUSES movers=147 sweep_balance=0 offsetting=0 other=147 sum_ok=True core_separate=16; trace reading: 'the arms day values do not reproduce the persisted month grade' (the default data-dir held round 20's v1->v2 arms)",
      "after commonwealth_sweep_regrade.py --before-list none --after-list v1 on the trunk: SWEEP-REGRADE ... months_before=1685/1931/78977 months_after=2057/1522/79014 control_same=True, then MOVER-CAUSES movers=147 sweep_balance=72 offsetting=0 other=75 sum_ok=True core_separate=16"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-u-1 AC2: the invocation as written classes the 147 movers.",
  "world_is": "The script's reproduce-guard refuses stale arms honestly (unexplained, never forced), but the invocation is not self-contained: it needs the none->v1 arms in the default data-dir. A repair: the script rebuilds or checks the arms' list versions itself, or the invocation names its own --data-dir."
}
```

## ADVI_COTBKF-D2-S32 -- L9 CB21u1-AC3 MET; both traced classes show W42-S1's missing cash credit

```json
{
  "id": "ADVI_COTBKF-D2-S32",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-08T19:02:48Z",
  "one_line": "L9 CB21u1-AC3 MET: the rule is printed before the counts with fixed constants and an ordered first-fit, ties are never forced, and each class's traced month shows its mechanism in the printed day values (re-derived by this seat). Beyond the criterion: BOTH traces show the same mechanism as W42-S1. The after arm's value steps down by the sweep buy (-4,010.86 carried from before the month; -199.98 then -188.14 on RGY005018's two sweep-trade days) and never steps back, so the 72/75 split is WHERE the missing cash credit lands, not two causes.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~42/mover_causes.md lines 5-114 (rule, counts, both traces)",
      "this seat's re-derivation: D49141714 2019-02-28 after 52.73/51.04-1 = 0.033111, before 4063.59/4061.9-1 = 0.000416; RGY005018 2024-12-10 after 21808.25/21852.77-1 = -0.002037, before 22008.23/21852.77-1 = 0.007114",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_21_L9_GRADE_20261008.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB21u1-AC3: each class's traced month shows its named mechanism in the printed day values, and the rule, not the result, decided the class.",
  "world_is": "Met. The two classes partition where the sweep-buy debit without a funding credit moves the month: on no-trade days (a balance carried in) or on the trade days themselves. The W42-S1 repair is the test: if it lands, both classes should collapse together."
}
```


## ADVI_COTBKF-D2-W43-S1 -- the sale credit returns 25 of 72 sweep_balance movers and 0 of 75 sweep_trade_day movers; dividends and fees carry the same missing cash leg

```json
{
  "id": "ADVI_COTBKF-D2-W43-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~43",
  "surfaced_at": "2026-10-08T19:31:00Z",
  "one_line": "CB-v-1: the sale-funding credit returns 25 of the 72 sweep_balance movers and 0 of the 75 sweep_trade_day movers to MATCH; the same missing cash leg also sits on dividend rows (credit) and fee rows (debit) that fund or are paid by a sweep trade, and 23 months moved MATCH -> DIFF.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~43/sweep_regrade.md 'The 163 round-19 movers under three verdicts': back to MATCH 25 of 163; neither cause sweep_balance 25 of 72, other:sweep_trade_day 0 of 75; core 0 of 16; BEFORE arm (v1, cash leg r19) reproduces the unrepaired DIFF verdict on 163 of 163",
      "worker scratch read of the silver transactions (Amount column, S3 read-only) joined to month_grades_after.parquet and mover_causes.parquet: of the 122 `neither` movers still DIFF, 94 carry a non-sweep row on a day the account traded a listed sweep: man only 53, dv only 28, dv+man 7, fch 1, 12b1 with man or dv 3, li with man 2; the other 28 carry an earlier month's unfunded balance and have no such row in the month. No non-sweep sale (sl) falls on a sweep-trade day inside any of the 147 `neither` mover months themselves, so the 25 that returned are carried-balance months: an EARLIER month's sale-funded sweep buy is what the credit repaired",
      "RGY005018 2024-12 stays DIFF (computed -8.8079, reported -8.02): its two sweep-trade days are a dv of 199.98 on 30231G102 that funds by FDIC66606 199.98 on 2024-12-10, and man -11.84 on CFNCASH paid by sl FDIC66606 11.84 on 2024-12-11; the step -199.98 then -188.14 = -199.98 + 11.84 is an income credit and a fee debit missing, not a sale",
      "D49141714 2019-02 returns to MATCH (computed 0.0128, reported 0.04): its 2019-01-24 sweep buy 3840.59 = sale of 30306A436 3836.32 + dv 4.27, the credit covers the sale part",
      "sweep_regrade.md 'Months that moved MATCH -> DIFF between the arms': 23 months, 19 of them in 0QF879130 (2025-05..10) and 0QF879352 (2023-05..2024-11); cause not measured here (0QF879130's 2025-04-07 trade is a 100000 bond sale paying a 102495.34 sweep buy, then a 100000 sweep sale buying 316067107); named in the md, not forced"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB-v-1 / row D2-S32: 'The non-sweep sale that funded it credits no cash'; the W42-S1 repair is the test, and if it lands both classes should collapse together.",
  "world_is": "The sale-funding credit (min of the account-day's non-sweep sale proceeds and its listed-sweep buys, credited to CFNCASH) lands as one general rule and collapses 25 of the 72 sweep_balance months; the sweep_trade_day class does not collapse, because what funds or is paid by its sweep trades is a dividend (cash in) or a fee on CFNCASH (cash out: man, fch are unsigned in the signs table so the sweep sale that pays them credits cash with no matching debit), not a sale. The round-19 cash-leg design is incomplete on all cash receipts and payments of the non-sweep rows, not only sales. This order's grant and item 1 name the sale only, so dividends and fees were not touched. Control: control_same=True, 642 of 642 months."
}
```

## ADVI_COTBKF-D2-S33 -- the version check cannot see the day parquet's arms

```json
{
  "id": "ADVI_COTBKF-D2-S33",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-08T19:40Z",
  "one_line": "CB-v-2's list-version check reads the version from the persisted month grades only; the day parquet under --data-dir records no list version, so D2-S31's actual case (right grades, stale day values) still passes the check and is caught only by mover_causes' reproduce guard",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "worker ~44 report on CB-v-2 (drained @c0f717a5c9): 'The day parquet does not record a list version, so the check reads it from the grades only.'",
      "D2-S31: on the trunk the grades at deliverables/~41 were the round-19 arms (none -> v1) while the default data-dir held round 20's v1 -> v2 day values"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Round-21 analysis E2: the mover scripts refuse to run when the arms' sweep-list version differs from the one they expect.",
  "world_is": "--data-dir is now required (the caller names the folder), and a grade-version mismatch is refused; a day-parquet mismatch is not detectable until the runner stamps the list version (and cash-leg rule) into the day parquet."
}
```

## ADVI_COTBKF-D2-S34 -- L9 CB22v1-AC3 MET; the one-cause prediction falsified; a double-credit lead for the 23 regressions

```json
{
  "id": "ADVI_COTBKF-D2-S34",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-08T19:42:34Z",
  "one_line": "L9 CB22v1-AC3 MET: funding_credit_rows is one general rule (per account and trade date with a listed-sweep buy, credit min(non-sweep sale proceeds, sweep buy); no account named in code), the 72 and 75 are counted from the persisted mover grades (25 of 72, 0 of 75), and all 138 movers still DIFF are named (138 distinct account-months). The CVO's round-21 prediction (D2-S32: both classes collapse together) is FALSIFIED: only carried-balance months returned.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/silver/commonwealth_sweeps.py funding_credit_rows (this seat's read at HEAD); comp-find of the traced/regressed account ids over data/assets/scripts/silver: 1 hit, a crosswalk test, none in the rule",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~43/sweep_regrade.md lines 711-1207: 163 movers read from mover_classes.parquet; 'Movers left not MATCH ... each named: 138', 138 distinct rows (this seat's count)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_22_L9_GRADE_20261008.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB22v1-AC3: one general cash-leg rule, the 72 and 75 counted back from the persisted grades, every month still DIFF named, not forced.",
  "world_is": "Met. Unmeasured lead for the 23 MATCH -> DIFF regressions (19 in 0QF879130 and 0QF879352): the rule credits cash whenever a non-sweep sale and a sweep buy share a day, so if the vendor already posts a cash leg for some of those sales, the synthetic credit counts it twice. A per-month check for an existing CFNCASH row on the credited days decides it."
}
```

## ADVI_COTBKF-D2-W45-S1 -- CB23w1-AC2 not met: the double-credit lead is falsified (0 of 23), the conditional rule drops 0 of 2703 credits

```json
{
  "id": "ADVI_COTBKF-D2-W45-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~45",
  "surfaced_at": "2026-10-08T20:12Z",
  "one_line": "CB23w1-AC2 cannot be met by the conditional rule as ordered: the double-credit lead (D2-S34) is falsified -- 0 of the 23 regressions are double credits and the conditional rule drops 0 of 2703 funding credits, so regressions=23 stays",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "real run of the AC2 invocation (r19 -> conditional, list v1 both arms): months_after=2103/1520/78970 control_same=True regressions=23 movers_back=25; report org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~45/sweep_regrade.md section 'Round 22's 23 regressions' (classes: other:cfncash_row_not_the_sale_cash=13, other:no_cfncash_row_on_credit_day=10, double_credit=0; 0 of 23 MATCH under conditional)",
      "funding_credit_rows over the whole transactions table (1,416,497 rows): 2703 credit days unconditional, 2703 conditional -- 0 dropped. Only 310 of the 2703 credit days carry any CFNCASH row at all; of 451 (credit day, CFNCASH row) pairs, 3 have |Amount| equal to the sale proceeds and all 3 are type lo (a withdrawal, debit sign), none a credit-signed row",
      "0QF879352 (13 of the 23): on the credit days 2021-07-16, 2021-07-20, 2022-07-18 the CFNCASH row is the withdrawal lo (12788.22 / 10000.00 / 7034.39) paired with a sweep sl of the same amount; the stock sale (13000 / 10000 / 24,560.55 over six securities) funds the sweep buy. Skipping every credit day that carries ANY CFNCASH row (a wider condition than the order's, tried in a scratch probe on the six accounts of the 23, not shipped) removes those 13 months and leaves 10 regressions, so no CFNCASH-row condition reaches regressions=0",
      "the other 10 (0QF879130 2025-05..2025-10, B3S691415 2023-10, B3S748567 2025-07, B3S808881/B3S808882 2025-01): no CFNCASH row on any credit day. In a scratch probe of those accounts under r19, on 9 of the 10 months the account value on the day before a credit day is blank (holdings 3-4, priced 2-3: the sold bond/bill/fund has no price) and the sale day is the first complete day; the credit then adds the sale's proceeds to a value that never held the sold security (0QF879130 2025-04-07: r19 24,239.68, repaired 239,239.68, the difference 215,000 = the three earlier credits). B3S748567 2025-07 is the exception: its sold fund (316067107) was priced and the value fell by the credit under r19. Lead only, not a claim: a credit conditioned on the sold security having been valued the day before"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order CB-w-1 / CTO round-22 ruling E1 (row D2-S34): the 23 MATCH -> DIFF regressions come from a funding credit applied where the vendor already posts a CFNCASH leg; a rule that credits only where no CFNCASH row exists removes them (regressions=0).",
  "world_is": "No CFNCASH row of the credit days carries a sale's cash in the 23 months; the conditional rule is implemented (commonwealth_sweeps.py funding_credit_rows(conditional=True), cash_leg conditional, default) and is a no-op on the data. All 23 are `other`. The order's refusal clause applies: the test is not weakened and the rule is not widened beyond the order."
}
```

## ADVI_COTBKF-D2-W45-S2 -- CB23w1-AC2 not met under AMENDMENT 1: regressions=1, the 25 recovered movers lost to condition (a)

```json
{
  "id": "ADVI_COTBKF-D2-W45-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~45",
  "surfaced_at": "2026-10-08T20:42Z",
  "one_line": "CB23w1-AC2 not met under AMENDMENT 1: (a)+(b)+(c) leaves regressions=1 (B3S748567 2025-07) but loses all 25 round-22 recovered movers; no variant measured has regressions=0 and the 25 kept",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "real run of the AC2 invocation with the shipped `conditional` = (a) sold security valued the day before + (b) no credit-signed CFNCASH row equal to the proceeds + (c) no CFNCASH row of any type equal to a same-day sweep sale: months_after=2058/1525/79010 control_same=True regressions=1 movers_back=0; report org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~45/sweep_regrade.md; one 0QF879352 month traced before the change in trace_0QF879352.md @86a13267df",
      "classes of the 23 (sum 23): double_credit 0; vendor_cfncash_leg_of_sweep_sale 13 (0QF879352 2023-05,06,08,09,11,12, 2024-02,03,05,06,08,09,11: on all three credit days 2021-07-16, 2021-07-20, 2022-07-18 a CFNCASH lo equals the same-day sweep sale 12788.22 / 10000.00 / 7034.39; the credits total 32678.95 and sit in the level from the first complete day 2022-07-18: r19 17640.53, repaired 50319.48); sold_security_not_valued_day_before 9 (0QF879130 2025-05..10, B3S691415 2023-10, B3S808881 and B3S808882 2025-01); other:credit_kept_by_every_condition 1 (B3S748567 2025-07). Now: 22 of 23 MATCH",
      "variants measured with the same invocation (scratch driver patching funding_credit_rows, caches shared, control_same=True in each): (a)+(b) as ordered: regressions=14 movers_back=0; (b)+(c) without (a): regressions=10 movers_back=25 months_after=2116/1507/78970; (a)+(b)+(c): regressions=1 movers_back=0. Credit days kept of 2703: (b)+(c) 2671, (a)+(b)+(c) 793",
      "the 25 recovered movers are lost by (a), not by (c): their five accounts (0QF879238 2017-07..2018-06, B3S605725 2018-01, B3S804888 2024-02/08 2025-02/08, D49141608 2019-02..09, D49141714 2019-02) have 0 of their credit days with a sold security valued the day before, the same state as the 9 that (a) clears, so the condition cannot tell a credit that restores the level (the 25) from one that inflates it (the 9). The credit is right for the 25 and wrong for the 9 and the 13 by the evidence of the reported returns; the variable that separates them is not in (a), (b) or (c)",
      "the remaining month B3S748567 2025-07 (computed 0.0535, reported 0.12): sold security the money-market fund 316067107 (rule (b) candidate, off in list v1, priced), credit days 2025-03-28 4871.60, 2025-04-29 4711.88, 2025-05-28 1514.07, 2025-06-27 778.15 (sum 11875.70), each paired with a sweep buy of the same amount and no CFNCASH row that day; r19 value 2025-07-31 9816.72 vs credited 21692.42, the difference 11875.70; the month's interest base matches r19 (0.12 pct of 9.8k)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order CB-w-1 AMENDMENT 1 (issuer ruling on row D2-W45-S1): a credit conditioned on (a) the sold security valued the day before and (b) no equal credit-signed CFNCASH row, with a general condition for the 13 shipped only if it keeps round 22's 25 MATCH and the control unchanged, gives regressions=0.",
  "world_is": "(a)+(b) leaves 14 regressions and loses the 25; (c) clears the 13 and keeps the 25 (measured without (a)); (a) clears 9 of the other 10 but loses the 25; one month (B3S748567 2025-07) is untouched by every condition. regressions=0 with the 25 kept is not reached by any combination of (a), (b), (c). The shipped default is (a)+(b)+(c) as the order directs; the issuer may rule (a) out, which gives regressions=10 with the 25 kept. The test is not weakened."
}
```

## ADVI_COTBKF-D2-W45-S3 -- CB23w1-AC2 not met under AMENDMENT 2: regressions=1 (B3S748567 2025-07); the blank relabels 2110 already-UNPRICED days and moves no verdict

```json
{
  "id": "ADVI_COTBKF-D2-W45-S3",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~45",
  "surfaced_at": "2026-10-08T21:00Z",
  "one_line": "CB23w1-AC2 not met under AMENDMENT 2: (a')+(b)+(c) leaves regressions=1 (B3S748567 2025-07, core candidate 316067107, row D2-S30); the blank changes no verdict (2110 of 2111 blank days were already UNPRICED) and round 22's 25 are 0 MATCH / 25 DIFF / 0 UNGRADABLE",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "real run of the AC2 invocation with the shipped AMENDMENT 2 rule (b)+(c) credit, (a') unvalued funding sale blanked: months_after=2058/1525/79010 control_same=True regressions=1 movers_back=0 (rc 0, 5m47s under timeout 1500); report org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~45/sweep_regrade.md sections 'CB-w-1 AMENDMENT 2' and 'Round 22's 23 regressions'. Classes of the 23 (sum 23): vendor_cfncash_leg_of_sweep_sale 13, unvalued_funding_sale 9, other:credit_kept_by_every_condition 1; 22 of 23 now MATCH",
      "variant table, all measured with the same invocation: round 22 repaired 23/25 (regressions/movers_back, months_after 2103/1520/78970); (b)+(c) 10/25 (2116/1507/78970); (a)+(b) 14/0 (2045/1538/79010); (a)+(b)+(c) 1/0 (2058/1525/79010); (a')+(b)+(c) 1/0 (2058/1525/79010). Credit days posted of 2703: (b)+(c) 2671; (a')+(b)+(c) 560 with 2111 blank days",
      "the blank moves no verdict: of 2111 credit days with an unvalued funding sale, 2110 are on the value grid and all 2110 were already blank (reason UNPRICED) under the same values with no blank list (daily_returns run with and without blank_days on the persisted after values: 2110 reasons changed UNPRICED -> UNVALUED_FUNDING_SALE, 0 computed days changed); the 1797 months holding one were already UNGRADABLE; no month of the 23 or of round 22's 25 holds a blank day (their credit days are in earlier months)",
      "round 22's 25 by new verdict: MATCH 0, DIFF 25, UNGRADABLE 0 (0QF879238 2017-07..12, 2018-01..06; B3S605725 2018-01; B3S804888 2024-02/08, 2025-02/08; D49141608 2019-02..09; D49141714 2019-02). Not crediting leaves their accounts' level at r19 (DIFF); a one-day blank on the credit day cannot reach the later months that carry the level",
      "the remaining MATCH -> DIFF month: B3S748567 2025-07 (computed 0.0535, reported 0.12). Sold security 316067107 is held (bought 45000 on 2024-05-02) and priced 1.00, so (a') does not blank it; credits 2025-03-28 4871.60, 2025-04-29 4711.88, 2025-05-28 1514.07, 2025-06-27 778.15 (sum 11875.70) each pay a same-day sweep buy, no CFNCASH row on those days, so (b) and (c) drop nothing; value 2025-07-31 r19 9816.72 vs credited 21692.42. The reported return has the r19 base: consistent with the vendor not carrying the fund in its performance base (inference), i.e. the parked core candidate of row D2-S30"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order CB-w-1 AMENDMENT 2 (issuer ruling on row D2-W45-S2): a funding sale of a security not valued the day before blanks the credit day (UNVALUED_FUNDING_SALE, month UNGRADABLE), (b) and (c) stay, and AC2 stays regressions=0; round 22's 25 are reported by new verdict.",
  "world_is": "The rule is built as stated and does not reach regressions=0: B3S748567 2025-07 passes every condition because its sold fund is held and priced (a row-type or valuation condition cannot tell a core cash fund from any held fund; it needs the D2-S30 designation). The blank is a relabel, not a verdict mover: every blank day was already UNPRICED, so round 22's 25 land DIFF, not UNGRADABLE. The test is not weakened; the order stays open."
}
```

## ADVI_COTBKF-D2-W45-S4 -- CB23w2-AC2 not met: divfee as ordered leaves regressions=95 (181 DIFF->MATCH, 58 of the 75 sweep_trade_day movers back); fch never helps, the dividend leg is 46 gained / 28 lost

```json
{
  "id": "ADVI_COTBKF-D2-W45-S4",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~45",
  "surfaced_at": "2026-10-08T21:42Z",
  "one_line": "CB23w2-AC2 not met: the divfee rule as ordered (dv credit, man/fch debit, on a conditional baseline) leaves regressions=95 against 181 DIFF->MATCH; 58 of the 75 sweep_trade_day movers are back to MATCH; fch never helps (0 of 24 DIFF months, 25 MATCH->DIFF), the dividend leg is 46 gained / 28 lost",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "real run of the AC2 invocation as written (before conditional, after divfee, list v1 both arms, --out .../0.9.0_WK_ADVI_COTBKF~45/divfee): months_before=2058/1525/79010 months_after=2121/1438/79034 control_same=True regressions=95 movers_back=78 (rc 0, 8m11s under timeout 1500); report org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~45/divfee/sweep_regrade.md section 'CB-w-2' and its table 'Months that moved MATCH -> DIFF between the arms'. Transitions (82593 months): DIFF->MATCH 181, MATCH->DIFF 95, MATCH->UNGRADABLE 23, DIFF->UNGRADABLE 14, UNGRADABLE->DIFF 13",
      "the 95 by what the month carries: fch_fee_leg_in_month (30): 0QF878979 2017-11; 0QF878981 2020-11; 0QF879231 2017-11,2018-11,2019-11; 0QF879353 2020-11,2022-11,2023-11,2024-11,2025-11; 0QF895828 2018-11,2019-11; 0QF895984 2018-11; 0QF927346 2022-05; B3S661358 2018-11,2019-11; B3S749464 2023-11,2024-11; B3S782299 2022-11,2023-11; D49146094 2019-11,2020-11,2021-11,2022-11,2023-11,2024-11; H2Y365503 2023-11; H2Y365888 2023-11; RGY004120 2025-11; RGY005715 2025-11 | dividend_leg_in_month (28): 0QF878956 2023-08,2024-08,2025-02,2026-03; 0QF879143 2021-08; 0QF879353 2022-05,2022-08,2023-02,2023-05,2023-08,2024-02,2024-08,2025-02,2025-05,2026-02; 0QF899639 2024-11; B3S786844 2022-12; B3S798436 2024-08,2024-09,2024-12,2025-02,2025-11,2025-12; B3S804888 2025-12; B3S808045 2026-01; RGY003587 2025-06,2025-09; RGY007351 2026-03 | level_from_earlier_legs (28): 0QF878981 2022-04; 0QF879181 2020-10,2021-01,2021-04; 0QF879353 2021-12,2022-09,2022-10,2022-12,2023-01; 0QF880505 2021-02,2022-01,2022-07,2022-10; 0QF911558 2022-08,2023-02; B3S670862 2021-08,2021-09,2023-02; B3S670865 2021-08,2021-09,2022-09,2023-02; B3S703388 2024-05,2024-11; RGY004120 2025-03,2025-05,2025-06,2025-09 | man_fee_leg_in_month (7): 0QF878956 2025-04; 0QF880505 2024-04; B3S670862 2021-10; B3S703388 2023-07; B3S808881 2025-01; B3S808882 2025-01; RGY004222 2024-10 | man_fee_and_dividend_legs_in_month (2): 0QF878956 2025-01; RGY007351 2025-12",
      "variants measured with the same invocation shape (scratch driver, FEE_TYPES / DIVIDEND_TYPES patched; regressions / movers_back / sweep_trade_day back of 75): ordered man+fch & dv 95/78/58; man & dv 78/80/60; man only 32/42/35; man+fch no dividend 91/40/33; dividend only 70/32/20; control_same=True in all. No variant reaches 0",
      "fch: of the months carrying an fch fee leg and no dividend leg, 24 stay DIFF, 0 become MATCH, 25 MATCH become DIFF, 6 stay MATCH; man: 174 stay DIFF, 112 become MATCH, 11 become UNGRADABLE, 7 MATCH become DIFF, 22 stay MATCH. Example 0QF879231 2017-11: fch -35.00 paid by a 35.00 sweep sale, reported 0.00, computed 0.0026 before and -4.586 after",
      "dividend: of the months carrying a dividend leg and no fee leg, 349 stay DIFF, 46 become MATCH, 28 MATCH become DIFF, 6 stay MATCH. Example 0QF879143 2021-08: dv 90.00 (stock 293792107) with a 90.00 sweep buy the same day, reported -2.59, computed -2.556 before and -1.595 after. Sweep purchase B equals dividend D on 29127 of 39788 dividend days with a sweep buy, so the pairing is real where it holds",
      "23 months leave MATCH for UNGRADABLE (not counted by regressions): 22 are 0QF879352 2023-05..2025-12 (every day NON_POSITIVE_BASE under the fee debit) and B3S765083 2022-08 (17 of 23 days)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order CB-w-2: a dividend that funds a sweep buy credits cash and a fee paid by a sweep sale debits cash, one general rule over the row types, layered on conditional; AC2 expects regressions=0 against that baseline.",
  "world_is": "The rule is built as ordered (commonwealth_sweeps.divfee_rows, default divfee, 36 tests in the cash-leg file, mutants fire) and regresses 95 months that matched under conditional while recovering 181 and 58 of the 75 sweep_trade_day movers. The reported return of a month with an fch leg, and of 28 months with a dividend leg, equals the computed return WITHOUT the leg: the vendor appears to leave IRA maintenance fees (fch) out of the return and to take some dividends at another date than the pay date (inference; the transactions carry no ex-date). A row-type set of man only cuts regressions to 32 but still not to 0. The test is not weakened; the order stays open for the issuer and the CTO to rule on the fee-type set and the dividend timing."
}
```

## ADVI_COTBKF-D2-S35 -- L9 CB23w1-AC3 NOT MET as written: round 22's 25 recovered movers are DIFF again (0 of 25 MATCH)

```json
{
  "id": "ADVI_COTBKF-D2-S35",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-08T22:03:43Z",
  "one_line": "L9 CB23w1-AC3 NOT MET as written: three of its four clauses hold (the 23 classed with evidence rows, 13 + 9 + 1 = 23; one general rule, no account special-cased in code; non-sweep control 642 of 642 unchanged), but 'round 22's 25 recovered movers are still MATCH' fails: 0 of 25 are MATCH under conditional. AMENDMENT 3 (CTO msg 1618) moved AC2 only; AC3's text was never amended.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~45/sweep_regrade.md lines 1210-1282 (49 table rows: the 23 classed, the 25 now DIFF) and 1311ff (AMENDMENT 3 section: 'MATCH 0, DIFF 25')",
      "org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-w-1.conditional-credit.md:49 and :69 (AC3 text, unamended)",
      "comp-find of the three named accounts over data/assets/scripts/silver: 1 hit, a comment in commonwealth_sweeps.py:35, none in a condition (this compile)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB23w1-AC3: the 23 are classed with evidence rows and sum to 23; the rule is one general condition; round 22's 25 recovered movers are still MATCH and the non-sweep control is unchanged.",
  "world_is": "Not met on the third clause. The issuer's own diagnosis (packet): what is wrong is the cash LEVEL carried into later months, which a per-day credit or blank cannot reach; the CTO put carried-level propagation in round 24 (msg 1618). That round's re-grade is where the 25 should return; this grade does not soften the clause to fit."
}
```

## ADVI_COTBKF-D2-W46-S1 -- CB24x1-AC2 not met: control_same=False, 52 of 667 no-sweep control months unchanged; the method is account-wide and moves every account

```json
{
  "id": "ADVI_COTBKF-D2-W46-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~46",
  "surfaced_at": "2026-10-08T23:25Z",
  "one_line": "CB24x1-AC2 cannot be met as written: the real run ends control_same=False (52 of 667 no-sweep months unchanged, 58 of 65 accounts differ) because the method's cash ledger and fee/charge rules apply to every account, sweep or not",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46/sweep_regrade.md, section 'The control: months with no listed position' and the last line: control_same=False; 667 control months, 52 same verdict and same computed return (1e-09); by verdict move MATCH->MATCH 465, MATCH->UNGRADABLE 101, UNGRADABLE->MATCH 25, DIFF->MATCH 18, MATCH->DIFF 6; 517 of 667 keep their verdict",
      "465 MATCH->MATCH months: 464 have a reported 0.0 (accounts holding almost nothing) and the computed return moved a median 0.00165 and at most 0.0465 pct points; the method posts every cash movement of every account (fees, trades, dividends); the round-23 chain posted fees and dividends not at all and a trade's cash only as a funding credit on a sweep-purchase day",
      "101 MATCH->UNGRADABLE months (13 accounts, all NON_POSITIVE_BASE): under the method the account holds nothing, value 0.0; the round-23 chain carried a constant phantom cash level in them (00085401932 2023-09: value 78,848.46 every day, return 0.0, a MATCH against a reported 0.0). The 40-account positions snapshot check (sweep_regrade.md 'The ledger against the 2026-06-23 positions snapshot') equals the ledger to the cent on 40 of 40, which the round-23 level did not",
      "the before arm reproduces round 23's baseline exactly (months_before=2058/1525/79010, as ~45's run), so the movement is the method's, not the baseline's"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB24x1-AC2: 'the method re-graded against round 23's baseline; the no-sweep months unchanged' -- expect control_same=True, where control_same compares each month of an account with no listed-sweep transaction before and after (same verdict and same computed return to 1e-9 pct points).",
  "world_is": "Not met. The CTO's method (E1) values the whole account, cash included, so the same rule runs on accounts with no sweep: their fees are debited, their trades and dividends reach cash, their charges become flows, and their value and return change. The control as defined cannot hold for a general rule; it held in rounds 22-23 because those rules fired only on sweep days. The test is not weakened and no rule is fitted to it; the reading by verdict (517 of 667 same) is printed beside the literal one."
}
```

## ADVI_COTBKF-D2-W46-S2 -- CB-x-1 item 4 not doable from the stores the chain reads: no dividend ex-date exists in them, so the pay-vs-ex grade of the cross-month dividend months is NOT GRADED

```json
{
  "id": "ADVI_COTBKF-D2-W46-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~46",
  "surfaced_at": "2026-10-08T23:25Z",
  "one_line": "The order grades every cross-month dividend month both ways (pay date, ex-date) from the Yahoo dividend series; no store the chain reads holds an ex-date, so the ex arm and the very set of cross-month months cannot be built and are reported NOT GRADED, never inferred",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "opal-data-cot silver/prices/canonical_prices.parquet (the first price store, address from lib/opal_naming.legacy_address('cottonwood-silver-canonical-prices')): schema date, asset_name, ticker, price, source; 11,291,021 rows; no dividend or ex-date column. The other five stores read through pc.STORES are cached as (kind, key, day, price, source) only (.scratch price_cache, this worktree)",
      "silver transactions: every dv / dvr / dvlt / dvst row carries ONE date (Trade_Date = Cost_Date = Settle_Date on over 99.9% of rows, per the CRO research section 2), the pay date; 410,839 dv rows, none with an ex-date",
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261008_COTTONWOOD_YAHOO_PRICE_BACKFILL_STRUCTURE.md section 3 stores the dividend events apart, but the backfill is dell1's queue and nothing it writes is in a store the chain reads; the order bars any download or vendor call",
      "comp-find over the repo for ex_date: the matches are the rivalfunds ETF event tables (data/etfs/scripts/rivalfunds), another product's data and not read by this chain",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46/sweep_regrade.md, section 'Cross-month dividends graded BOTH ways: NOT GRADED'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB-x-1: 'Implement both as a runner option (--dividend-date pay|ex, default pay, as delivered) and grade every month containing a cross-month dividend BOTH ways, printing the swing per month and in total, BEFORE either is adopted'; the CRO: ex-dates come from the Yahoo dividend series the price backfill already pulls.",
  "world_is": "The option is built and tested (--dividend-date pay|ex, --ex-dates <cusip, pay_date, ex_date>; commonwealth_sweeps.method_cash_rows moves a dividend's cash posting to its ex-date; stub tests for both dates) and the runner grades the cross-month months both ways, with the swing, the moment an --ex-dates source is named. None exists, so the run prints NOT GRADED with the reason, the default stays pay, and neither date is adopted. Of the 98 MATCH->DIFF months, 45 hold a dv / dvlt / dvst row (a lead, not a cause: the dating cannot be tested without ex-dates)."
}
```

## ADVI_COTBKF-D2-W46-S3 -- CRO table is silent on nine fee/charge/tax row types and ManCheck/ci needed a reading; defaults kept and reported: 35 of the 98 MATCH->DIFF months hold an unlisted charge or tax (ftax 30)

```json
{
  "id": "ADVI_COTBKF-D2-W46-S3",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~46",
  "surfaced_at": "2026-10-08T23:25Z",
  "one_line": "The CRO's table names no treatment for ASF, bcf, cbf, fco, stp, term, ftax, stax, frntax; they keep the default (internal, a drag now that the ledger debits cash) and are reported, 35 of the 98 regression months hold one",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46/sweep_regrade.md, section 'The method, row type by row type' (rows by line class and the treatment of each of the 61 types) and '### What the 98 MATCH -> DIFF months hold': 35 months hold an unlisted charge/tax type (ftax 30, cbf 3, fco 1, stax 1, stp 1), 45 hold a dividend row, 24 neither; 25 accounts",
      "specimen 0QF879431 2016-03 (20 of the 98 months are this account): sl 648.19 on the sweep = lo 518.56 + ftax 129.63 on CFNCASH, reported 0.00; the lo is a flow, the ftax is not named, so it stays a drag and the month computes -0.1616",
      "the CRO table row 'other charges' lists fch, genmain, fee, misc, csltfee, pcf; its section 1 says 'every other charge is a withdrawal'; the order lists the same six and says unlisted types are reported, never silently treated",
      "ManCheck (124 rows) is read as ManAltT (a drag on the owing account, no cash debit: fee paid outside the account): no snapshot account carries one, so it is untested, as the CRO says. ci is read as a flow code because the CRO's flows row names it: no graded month holds a ci row (0 of 119 ci months), so it moved no grade"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB-x-1: the CRO's table decides each row type's treatment; 'do not change a treatment because of its effect on the grade'; types the table does not list are reported, never silently treated.",
  "world_is": "Nine fee/charge/tax types (ASF, bcf, cbf, fco, stp, term, ftax, stax, frntax; 5,596 CFNCASH rows, ftax 4,198) have no row in the table. Under the old chain their cash was never debited, so 'internal' meant 'ignored'; under the method the ledger debits it (the snapshot needs that), so the same label now means a drag. The default was kept and no variant was graded or adopted; whether a withholding that rides a withdrawal is a flow is the CTO's call, with the 35 months named here as the evidence."
}
```

## ADVI_COTBKF-D2-S36 -- L9 CB24x1-AC4 NOT MET as written: dividend months not graded both ways (no ex-date source)

```json
{
  "id": "ADVI_COTBKF-D2-S36",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T00:05:26Z",
  "one_line": "L9 CB24x1-AC4 NOT MET as written, on one clause that cannot be measured yet: no cross-month dividend month is graded both ways, because no store the chain reads holds an ex-date. Clause 1 (the method follows the CRO's table row by row) and clause 2 (round 22's 25: 25 of 25 MATCH) are MET; neither date is adopted by assumption.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261008_COMMONWEALTH_TWR_METHOD.md (the leg table)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46/sweep_regrade.md lines 1239-1306 (method, type by type), 1204 (25 of 25), 685ff (98 named)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_24_L9_GRADE_20261008.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB24x1-AC4: the rule follows the CRO's table row by row; round 22's 25 are each MATCH or named with a traced cause; every cross-month dividend month is graded both ways with the swing printed and neither date adopted by assumption.",
  "world_is": "Clause 3's 'graded both ways' is not done and could not be: every dividend row carries the pay date only (row D2-W46-S2); the pay|ex option is built and tested with no ex-date input. A MET would claim a swing nobody measured. Closes when an ex-date source lands (the dell1 data-queue project; Yahoo carries ex-dates) and the 22 dividend-dated regressions are graded both ways, or when the CTO amends the clause by name."
}
```

## ADVI_COTBKF-D2-W47-S1 -- the carried-level regressions are the baseline's departure, not the method's: no method fix, method_r25b = method_r25

```json
{
  "id": "ADVI_COTBKF-D2-W47-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~47",
  "surfaced_at": "2026-10-09T01:19Z",
  "one_line": "CB-y-2's premise does not hold: in all 13 accounts of the 39 carried-level regression months the METHOD's cash level is what the account's own rows support; it is the conditional baseline's level that departs, so there is no method fix and method_r25b equals method_r25",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/levels/sweep_regrade.md, section 'Round 24's 39 carried-level regressions traced': per account the checks on the method's level (ledger closure over the account's life, running level, unmatched sales, positions still held, the 2026-06-23 snapshot) and on the baseline's; per month its first differing level, the step by row type and the result. Printed by the AC2 run: CARRIED-LEVELS months=39 supported=39 accounts=13",
      "the method's ledger closes to 0.00 on 13 of 13 accounts (each closed: no security still held, absent from the 2026-06-23 positions snapshot, last row 2026-02-10 to 2026-06-18), no sale of an unheld security (0 of 13), and the running level is never below -0.5 in any of the 39 months; the baseline (conditional) cash level closes at -238786.38 to +134287.28 on the same 13",
      "four runs of days with the method's running level below -0.5 exist (0QF879353 2018-11-19 to 2018-11-21, lowest -9.78; B3S703388 2024-04-05 to 2024-04-24, lowest -138.63, and 2025-04-07 to 2025-04-10; RGY004222 2025-01-23 to 2025-01-24, lowest -909.67): a debit posted before its credit, recovered, and none in a regression month",
      "the baseline's departure by kind (decided from the first step's row types): postings it never makes (security-line purchases and sales, dividends, fees, taxes) 23 months, a ManAltF payment made for another account 14 (D49141625 2017-10-09: sl 105.20 pays ManAltF -30.84 and -74.36 for two other accounts), a sweep sale that funds a non-sweep purchase 2 (RGY004222 2024-04-08: sl 140000 on the sweep funds by 140000 of 316067107; B3S808045 2023-03-29: sl 995277.78 funds by 995000 + man 277.78)",
      "the baseline's agreement with Commonwealth is isolated in 11 of the 13 accounts (graded months MATCH under conditional: 0QF878956 6 of 54, 0QF878981 4 of 69, 0QF879143 1 of 70, 0QF879181 5 of 69, 0QF880505 11 of 47, 0QF899639 1 of 21, B3S703388 14 of 69, B3S798436 6 of 22, B3S804888 2 of 34, B3S808045 1 of 31, RGY004222 1 of 12); the other two are 0QF879353 (50 of 68) and D49141625 (35 of 67)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB-y-2: the earliest month in which the method's carried cash level departs from what the account's own rows support can be traced for each of the 39 carried-level regressions; where one general rule fixes a traced cause it ships as method_r25b.",
  "world_is": "No month of these 13 accounts is a wrong month of the METHOD's level: each account's own rows close to zero under the method's ledger and break under the baseline's. What the 39 months have in common is that the baseline's level differs from the method's from a first month (printed per month) and that the baseline's reproduces Commonwealth's reported return in that month; whether Commonwealth's own level equals the ledger is not testable from the rows (only its reported returns exist), and the baseline's agreement is isolated in most of these accounts. So there is nothing general to fix in the method's level: method_r25b is method_r25 and regressions=0 trivially. Whether these months are noise, a small-base artifact (D49141625: a 0.058 pct point difference on a base of 37.95) or a Commonwealth convention is the CTO's call at the round-N analysis."
}
```

## ADVI_COTBKF-D2-W47-S2 -- dividend months graded at pay and at ex: 22 of 22 graded, the ex-date helps 2 months and hurts 6, neither adopted

```json
{
  "id": "ADVI_COTBKF-D2-W47-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~47",
  "surfaced_at": "2026-10-09T01:19Z",
  "one_line": "Ex-dating the dividends: the 22 months are graded both ways (22 of 22), 20 do not move, the 2 XOM months turn MATCH, but the same XOM dividend turns 6 other MATCH months (3 accounts, 2025-06 and 2025-09) DIFF; neither date adopted",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/dividends/sweep_regrade.md, section 'The 22 dividend months graded at the pay date and at the ex-date': MATCH under pay 0, under ex 2; DIFF 22 and 20; graded in both arms 22 of 22; total swing -0.2381 pct points; verdict changes 2 (RGY003587 2025-06 swing -0.1233 and 2025-09 swing -0.1149, both DIFF to MATCH); the other 20 swing 0.0 (ex-date and pay date in the same month, no flow between them)",
      "the same run's 'Months that moved MATCH -> DIFF between the arms': 6 (0QF878981, 0QF879181, RGY005018, each 2025-06 and 2025-09), cause cash_leg_difference on the XOM pay day (2025-06-10, 2025-09-10: the arms' values differ by -3960.54, -108.9, -199.98 on that day); printed by the run: DIVIDEND-MONTHS months=22 graded=22 swing=-0.2381 abs_swing=0.2381 verdict_changes=2, and SWEEP-REGRADE ... regressions=6 dividend_both=22/22",
      "ex-date input: org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/EXDATES_ADVI_COTBKF_20261009.csv (39 rows, 16 CUSIPs, all measured; read from origin/box/dell1, untracked, never staged); only XOM 30231G102 has the ex-date in a different month from the pay date (pay 2025-06-10 / ex 2025-05-15, pay 2025-09-10 / ex 2025-08-15); across the whole delivery 548 dividend rows have an ex-date and 50 of those (XOM, in the accounts holding it) are cross-month"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB-y-2 AC4 (amendment 1): the 22 dividend_row months are graded at the pay date and at the ex-date on method_r25b with each swing printed; neither date is adopted as the default.",
  "world_is": "The 22 months grade both ways, but the ex-date moves only 2 of them (the 2 XOM months of RGY003587, DIFF to MATCH); the other 20 hold a dividend whose ex-date and pay date share a calendar month, so the chained monthly return cannot change. The ex arm on the whole grade is not better: it turns 6 MATCH months DIFF (the same XOM dividend in three other accounts) against the 2 it turns MATCH, so on this evidence the pay date is not worse than the ex-date for the one cross-month security measured. The source holds 39 (CUSIP, pay date) keys on 16 CUSIPs and only XOM has a cross-month key, so the dividends of every other security in the delivery carry no ex-date and are graded at the pay date only. Neither date is adopted; the default stays pay."
}
```

## ADVI_COTBKF-D2-S37 -- L9 CB25y1-AC3 MET and CB25y2-AC3 MET

```json
{
  "id": "ADVI_COTBKF-D2-S37",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T01:43:44Z",
  "one_line": "L9 CB25y1-AC3 MET and CB25y2-AC3 MET. y1: every unlisted-type treatment cites a stated source (DESCRIPTION, PAIRING or the CRO's table) committed @679c3c22b5 (20:41 ET) before the run's output @499405a2fe (20:52 ET); 35 of 35 months MATCH; ASF is the one sourceless type, named as such, and touches 0 of the 35. y2: 39 of 39 carried-level months each traced to their first differing month, step and posting; no fix applied (method_r25b = method_r25), so nothing was fitted to the grade.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/unlisted/sweep_regrade.md lines 1176-1235 (source table; the 35, 0 ASF)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~47/levels/sweep_regrade.md lines 1231-1313 (39 traced rows, 0 blank trace cells)",
      "git log of the table commit vs the run output (this seat's read)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_25_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB25y1-AC3: every treatment cites a source decided before the run; each of the 35 is MATCH or carries a traced cause; no treatment chosen by its effect. CB25y2-AC3: each of the 39 traced to a first wrong month with its posting and cause, or named untraced; any fix one general rule.",
  "world_is": "Both met as written."
}
```

## ADVI_COTBKF-D2-W49-S1 -- FWD-3 local daily-returns file grades 1,685 MATCH, not the 3,098 reported; nothing served

```json
{
  "id": "ADVI_COTBKF-D2-W49-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~49",
  "surfaced_at": "2026-10-09T02:08:35Z",
  "one_line": "CB-z-3 FWD-3: the only daily-returns file on this box (.scratch/advi_cotbkf/fwd3/daily_returns.parquet, 2026-10-08 01:27) grades MATCH 1,685 of 82,593 months, not the 3,098 the round-25 real run reports; no daily-returns table is in Opal's store",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python data/assets/scripts/silver/commonwealth_monthly_grade.py --returns .scratch/advi_cotbkf/fwd3/daily_returns.parquet: MONTHLY-GRADE months=82593 match=1685 diff=1931 ungradable=78977",
      "aws s3 ls s3://opal-data-assets/commonwealth/cottonwood/silver/: 8 tables, none daily returns",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~49/ENDPOINT_READ_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order expects FWD-3's instrument to read the method_r25 grade (MATCH 3,098 of 82,593 per round 25).",
  "world_is": "The returns file the instrument can read is older than or built differently from the method_r25 run; this worker did not rebuild it (a rebuild writes the local data dir and needs the price caches), so the FWD-3 row reports 1,685 as measured and the 3,098 as unreproduced. The grade is NOT either way: the daily series is not served and 78,977 months are ungradable."
}
```

## ADVI_COTBKF-D2-W48-S1 -- the new default breaks one test outside the order's paths

```json
{
  "id": "ADVI_COTBKF-D2-W48-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~48",
  "surfaced_at": "2026-10-09T02:18Z",
  "one_line": "Setting method_r26 the default cash leg (CB-z-2 step 1) turns test_commonwealth_carried_levels.py::test_method_r25b_is_selectable_and_is_method_r25 red: its line 57 asserts the old default, and that file is not in CB-z-2's paths",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/silver/tests/test_commonwealth_carried_levels.py line 57 at fa87b0ca99: `assert sw.CASH_LEG_DEFAULT == sw.CASH_LEG_METHOD  # method stays the default, r25 and r25b are chosen`; the CB-z-2 order sets CASH_LEG_DEFAULT to method_r26 (commonwealth_sweeps.py), so the assertion cannot hold",
      "python -m pytest -q data/assets/scripts/silver/tests -p no:cacheprovider after the default change: 1 failed, 640 passed, 11 skipped; the one failure is that test (AssertionError: assert 'method_r26' == 'method'); the three tests that asserted the old default in CB-z-2's paths (test_commonwealth_method.py, test_commonwealth_unlisted_types.py, test_commonwealth_cash_leg.py) were updated to the new default; test_commonwealth_carried_levels.py is not in the order's <paths> block, so it is left as it is",
      "org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-z-2.nonmatch-census.md <paths> (11 entries, none is test_commonwealth_carried_levels.py)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB-z-2 step 1: method_r26 is the default cash-leg rule and every earlier rule stays selectable and unchanged; the end-of-order silver suite (python -m pytest -q data/assets/scripts/silver/tests) is the hygiene check.",
  "world_is": "The default changes and every earlier rule stays selectable, but one test outside the order's write grant pins the old default (`== sw.CASH_LEG_METHOD`), so the silver suite is red by that one test until a seat whose paths include test_commonwealth_carried_levels.py changes its line 57 to `sw.CASH_LEG_DEFAULT == sw.CASH_LEG_METHOD_R26` (the same edit made in the three sibling tests). No code path is wrong; the assertion states a superseded default."
}
```

## ADVI_COTBKF-D2-W48-S2 -- CB26z2-AC2 not met: 512 of 886 DIFF months unexplained by the census rule

```json
{
  "id": "ADVI_COTBKF-D2-W48-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~48",
  "surfaced_at": "2026-10-09T02:30Z",
  "one_line": "CB26z2-AC2 not met: the non-MATCH census classes 79,495 of 79,495 months but 512 DIFF months (of 886) are unexplained by the rule fixed before the counts: 478 where no posting category reaches |D|, 34 that hold no driver row; the 78,609 UNGRADABLE months are all classed",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~48/census/nonmatch_census.md and nonmatch_census.parquet (the AC2 invocation, rc 0): NONMATCH-CENSUS total=82593 match=3098 diff=886 ungradable=78609 classes=10 unexplained=512; MATCH 3098 of 82593 (3.75%); the class counts sum to 79495 = 886 + 78609 (sum_ok=True)",
      "classes: ungradable:UNPRICED 74846 (94.2% of the non-MATCH months, the largest class), FIRST_DAY 1533, NON_POSITIVE_BASE 1173, NO_REPORTED_RETURN 878, NO_DAILY_RETURNS 116, REPORTED_SPAN 63; diff:driver:SWEEP_CASH_LEG 190, INCOME 154, CLIENT_FLOW 30; unexplained 512 (478 'no driver category reaches |D| (7 categories checked)', 34 'the month holds no row of any of the 7 driver categories'). The 512 are named one per line in the md (section 'Unexplained months'): 45 accounts, 2020-08 to 2026-04",
      "the re-derivation check passed: the day values reproduce the persisted computed return on 886 of 886 DIFF months (1e-06 pct points) and the first blank reason on every UNGRADABLE month that holds a blank day, so no unexplained month is a recompute mismatch",
      "of the 478: the largest driver exposure is a median 0.13 (90th percentile 0.86, maximum 1.00) of |D|, by category INCOME 392, SWEEP_CASH_LEG 84, CLIENT_FLOW 2; the 512 have a median |D| of 0.47 pct points (260 of them within 0.5)",
      "the rule is fixed in data/assets/scripts/silver/commonwealth_nonmatch_census.py at cd084bc838, committed before the default re-grade run and before any count; no class was added, widened or dropped after the counts"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB-z-2 (CTO E1): every non-MATCH month is classed with counts and no class is unexplained; the criterion is `unexplained=0`.",
  "world_is": "The rule traces a DIFF month to a posting category only when that category's postings are big enough to move the month by the difference (exposure at least |D|). For 374 of 886 DIFF months one does (cash legs 190, income 154, client flows 30). For the other 512 the difference is larger than anything a different treatment of the month's postings could move (478) or the month holds no driver posting at all (34): these months' differences sit outside the categories the method decides, which points at the valuation (price, holdings, carried cash level) rather than a posting treatment, but this census has no instrument for that and names no cause it did not trace. The order is left open and the test is not weakened; widening the rule after seeing these counts would be rule-fitting, so a rule that traces valuation-side drivers (carried level, stale or missing price, holdings step) is a round-27 cell for the CTO's analysis. The UNGRADABLE side is fully classed: UNPRICED alone is 74,846 months, a cause that spans the whole table (the order states that only about 8% of account-days are priced from Opal's stores; not re-measured here) and is named, not split."
}
```

```json
{
  "id": "ADVI_COTBKF-D2-W48-S3",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~48",
  "surfaced_at": "2026-10-09T02:37Z",
  "one_line": "Row ADVI_COTBKF-D2-W48-S1's red test (test_method_r25b_is_selectable_and_is_method_r25) is fixed by this commit under the issuer ruling at 4a4088de98: line 57 now asserts the default is CASH_LEG_METHOD_R26",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/silver/tests/test_commonwealth_carried_levels.py line 57: `assert sw.CASH_LEG_DEFAULT == sw.CASH_LEG_METHOD_R26`; the file was added to CB-z-2 <paths> by 4a4088de98",
      "python -m pytest -q data/assets/scripts/silver/tests: 659 passed, 11 skipped, 0 failed (S1 recorded 1 failed, 640 passed, 11 skipped)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "S1: the default change to method_r26 leaves one test red that is outside CB-z-2's paths, ARMED until the issuer disarms it.",
  "world_is": "The issuer widened CB-z-2's grant by that one path and this worker changed that one assertion to the new default; the suite is green. S1 is not edited; its disarm is this row's subject."
}
```

## ADVI_COTBKF-D2-S38 -- L9 CB26z1-AC3, CB26z2-AC3, CB26z3-AC2 MET

```json
{
  "id": "ADVI_COTBKF-D2-S38",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T03:03:20Z",
  "one_line": "L9 CB26z1-AC3 MET, CB26z2-AC3 MET, CB26z3-AC2 MET. ASF's rule committed @422ae4888c (22:00 ET) before its run @d7c2fbf66b (22:12); the census rules committed @cd084bc838 (22:19) before the counts @48cdd857cd (22:33), over the whole 82,593 graded months (sum_ok), with the 512 unexplained named, not forced; each FWD row's instrument was run in the task with measured output (this seat re-ran FWD-6: identical line).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~48/asf/asf_source.md (rule section before the census)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~48/census/nonmatch_census.md lines 1-60",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~49/ENDPOINT_READ_20261009.md",
      "git log of the rule commits vs the run commits (this seat's read)",
      "commonwealth_coverage_statement.py re-run by this seat: 'COVERAGE-STATEMENT tables=11 kinds=7 every_kind_has_own_span=True every_not_covered_has_reason_and_row=True rows_cited=15 rows_missing=0' rc=0",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_26_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB26z1-AC3, CB26z2-AC3, CB26z3-AC2 (the three judgment criteria of round 26).",
  "world_is": "All three met as written."
}
```

## ADVI_COTBKF-D2-W51-S1 -- CB-aa-2 weight fallback and list population

```json
{
  "id": "ADVI_COTBKF-D2-W51-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~51",
  "surfaced_at": "2026-10-09T03:31Z",
  "one_line": "CB-aa-2 weight rule has no stated value for a security with no purchase row (1,540 of 4,372 listed): this worker used the largest inbound amount (1,428), else weight 1.0 (112), with weight_basis printed per row; and the list holds 4,372 securities where the CRO's section 6 tier counts sum to 3,226",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/PRICE_NEED/COTTONWOOD_PRICE_NEED_RANKED.md (weight_basis: BUY 2832, INBOUND 1428, NONE 112; P1 2155, P2 195, P3 2022)",
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261008_COTTONWOOD_YAHOO_PRICE_BACKFILL_STRUCTURE.md section 6 (P1 1,714, P2 64, P3 1,448)",
      "data/assets/scripts/silver/commonwealth_price_need.py module docstring (the weight rule); RECONCILE account_days=1691729 mismatched=0 against the run's holdings - priced_holdings"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order scores held days x holding accounts weighted by the largest single purchase amount, and tiers the securities by the CRO's rule; it does not say what weight a security without a purchase row takes, and it does not state the population the CRO's tier counts were taken over.",
  "world_is": "1,540 listed securities have no `by` row (they enter by in-kind transfer or contribution); weight 0 would zero their score and tie them, so the script takes the largest inbound line amount (commonwealth_signs share-in types), else 1.0, and prints weight_basis BUY/INBOUND/NONE on every row. The list counts every non-cash security held on an unpriced account-day in the default run (4,372, the unpriced holding days equal holding_days - priced = 15,986,926), a wider population than the CRO's 3,226; the CRO's population definition was not available to this worker, so the difference is recorded, not reconciled. The weight rule is the CTO's or CRO's to change; the script reads one function (purchase_weights)."
}
```

## ADVI_COTBKF-D2-W50-S1 -- CB-aa-1: the price store's closes are split-ADJUSTED back through history while the rebuilt quantity is as traded: 59 of the 512 untraced DIFF months (6 securities, 8 accounts) are months before a split

```json
{
  "id": "ADVI_COTBKF-D2-W50-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~50",
  "surfaced_at": "2026-10-09T04:01Z",
  "one_line": "The closes the chain reads are split-adjusted over their whole history while the quantity rebuilt from the rows is as traded, so a month before a split values the position at 1/k and a split day shows a ghost return (B3S605610 2025-11-17 +274.9% against a reported -2.67)",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~50/diff_trace.md section 'One traced month per cause': B3S605610 2025-11, NFLX 64110L106: 68 shares and a stored close of 111.22 on 2025-11-14 (10 times that, 1,112, as traded, if the 10-for-1 ratio holds), a QA row of +612 shares on 2025-11-17 (10-for-1), the stored close continuous across the day (115.42 -> 111.22 -> 110.29); the account value goes 24,498 -> 91,844; with the closes before the split scaled x10 the month is -2.5150 against reported -2.67 (D was +279.4650)",
      "diff_trace.parquet: 59 months with sub_kind split over 6 securities (02079K107, 02079K305, 023135106, 64110L106, 808524102, 88160R101) and 8 accounts; the split ratios come from the QA rows of every account (same ratio in every account that shows the day), 14 confirmed events",
      "python data/assets/scripts/silver/commonwealth_diff_trace.py (the AC2 invocation): DIFF-TRACE months=512 traced=73 untraced=439 classes=3"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "data/assets/scripts/silver/commonwealth_daily_valuation.py docstring (CB-p-1): each holding is valued at that day's close, quantity x price, and the CTO's cell reads holdings x as-traded close.",
  "world_is": "For a security with a split, the stored close before the split day is the split-adjusted one (as traded divided by the cumulative ratio) and the rebuilt quantity before the day is the pre-split quantity, so the position is valued at 1/k of its worth until the QA row steps the quantity. Every month before the split since the quantity last changed is mis-weighted, not just the split month; a repair that scales the pre-split closes by the split ratio (written from the QA rows, not from the reported return) carries at least 90% of D in 59 of the 512 months. Nothing in the chain is changed here. The remedy (an as-traded close or a split-aware quantity for every graded month) is a round-28 cell for the issuer and the CTO."
}
```

## ADVI_COTBKF-D2-W50-S2 -- CB-aa-1: an in-kind contribution (li) can carry the cost as its Amount, so the flow is valued at cost and the return takes the difference (B3S793726 2025-11: Amount 5,302 against shares worth 14,453)

```json
{
  "id": "ADVI_COTBKF-D2-W50-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~50",
  "surfaced_at": "2026-10-09T04:01Z",
  "one_line": "An li row that delivers shares can carry the cost basis as its Amount, so the flow the chain subtracts is below the value the shares add to the account and the day returns the difference (B3S793726 2025-11-20 +8.30%)",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "transactions cache (silver with Amount): B3S793726 2025-11-20 li GOOGL 02079K305 Quantity 50 Amount 5302.475; the day's close x 50 = 14,452.87; the day's value steps 99,206 -> 112,741 with flow 5,302.48 recorded, return +8.2991%",
      "diff_trace.md: with the flow set to the shares' value the month is 2.9946 against reported 2.22 (D was +10.3632, remainder +0.7746); the second li month, 2026-02 (two rows, Amounts 5,282.60 and 14,436.70 against 16,729.65 and 25,301.95) stays untraced: the repair leaves +1.04 of D +20.05"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "commonwealth_flows.py EXTERNAL: li is a contribution whose flow is direction x |Amount|; the CB-q-1 rule values a ZERO Amount from quantity x price, which assumes a non-zero Amount is the value.",
  "world_is": "A non-zero Amount on an in-kind li is taken as the value of what entered. In two B3S793726 months it is well below the shares' value (a cost basis is the reading; the rows do not say). The trace names this as flow_value in one month and measures it in a second; it does not change the flow rule (the order's bounds forbid it) and it does not know how many other in-kind rows across the 82,593 months carry a cost."
}
```

## ADVI_COTBKF-D2-W50-S3 -- CB-aa-1: on a reinvested-distribution day (dvr) the stored close steps UP by about the distribution per share while the shares also step up: 13 months, 8 accounts

```json
{
  "id": "ADVI_COTBKF-D2-W50-S3",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~50",
  "surfaced_at": "2026-10-09T04:01Z",
  "one_line": "On a dvr day the position's value steps twice, once by the reinvested shares and once by a close that rises by about the distribution per share instead of falling by it (RGY004120 2025-12-05 FCNTX +5.04% close, +42.5 shares)",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C2",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "transactions cache: RGY004120 2025-12-05 dvlt 1019.65 and dvr Quantity 42.539 of 316071109; the stored close 22.7407 (2025-12-04) -> 23.8867 (2025-12-05), 1.1460 a share against a distribution of about 1.09 a share; the day returns +9.74% (price +5.00, shares +4.74) and the month is 11.2855 against reported 1.65",
      "diff_trace.parquet: 13 months with sub_kind distribution (4 are the RGY accounts of 316071109 in 2025-12); with the day's whole position step taken out of the value from that day on the month is within 0.11 of reported",
      "INFERRED: the store is not shown to be total-return adjusted; the sign and size of the close step are measured, the cause of it is not"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The close on a distribution day is an as-traded close, which falls by the distribution per share on the ex-date, so reinvested shares at that close leave the position's value unchanged.",
  "world_is": "The stored close does not fall on these days; it rises by about the distribution per share. Together with the reinvested shares the account value steps up by the distribution twice. The trace repairs this per day (the position's step taken out) and names it price:<cusip>; it does not say whether the store is dividend-adjusted, whether Commonwealth books the distribution as income, or how many other months carry the same step."
}
```

## ADVI_COTBKF-D2-S39 -- disarm of W50-S1..S3 at CB-aa-4's pair

```json
{
  "id": "ADVI_COTBKF-D2-S39",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-09T04:08Z",
  "one_line": "Disarm of D2-W50-S1, S2, S3 (disarm_owner 2.0.0_SA_COO~C2): the only path by which their wrong day values could reach a reader is CB-aa-4's SERVED mint of the FWD-3 tables; the COO half of its never-widen pair is now conditioned on those days being repaired or blanked with reason, so nothing wrong can be served",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R27_FWD3_SERVE_COO_HALF.md: COO half DRAFT, condition added (not given while split / in-kind li / dvr days carry known-wrong values)",
      "CB-aa-4 (0.7.0_AE_CloudOps~CB2) BOUNDS: no write before both halves of the pair exist",
      "the three target prefixes hold 0 objects (measured 03:2xZ, control 14): nothing is served today"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "An ARMED hazard disarms same-turn via its disarm_owner (CLAUDE.md section 2).",
  "world_is": "W50-S1..S3 describe valuation defects on specific days (59 split months, 13 distribution months, 1 in-kind flow). They stay OPEN as defects for the round-28 analysis; their hazard (publication of wrong day values) is blocked at the pair."
}
```

## ADVI_COTBKF-D2-W52-S1 -- a default sweep re-grade run persists account-level day values only (no per-holding rows, no daily returns), s

```json
{
  "id": "ADVI_COTBKF-D2-W52-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~52",
  "surfaced_at": "2026-10-09T04:06:00Z",
  "one_line": "CB-aa-3: a default sweep re-grade run persists account-level day values only (no per-holding rows, no daily returns), so the serve builder re-derives holdings and daily returns and refuses unless they reproduce the run",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/silver/commonwealth_fwd3_serve.py@4d4d00aa6f (rederive, check_values, check_grades)",
      ".scratch/advi_cotbkf/fwd3_serve/fwd3_manifest.json (checks.day_values_rows=1691729, day_values_worst_abs_diff=0.0, month_grades_rows=82593)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~52/dry_run_ac2.log"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order has --build write the three tables 'from a default run's day values and month grades', and states the run 'writes day parquet to --data-dir and month grades beside its report'.",
  "world_is": "The run's <data-dir>/after/account_day_value.parquet holds account, date, value, holdings, priced_holdings, complete (no cusip, quantity, close, price source) and no daily_returns.parquet is written at all (the chain computes the returns in memory). commonwealth_fwd3_serve.py --build therefore re-derives the holdings (daily_holdings_table over with_sweep_cash), the per-holding valuation (value_days on the run's security_day_price.parquet) and the daily returns (daily_returns, the run's cash leg) from the transactions cache, which must carry Amount (the shared cache lacks it; a local one was built from the silver transactions, read-only), and REFUSES unless the re-derived account-day values equal the run's file and the re-derived month grades equal month_grades_after.parquet. Measured at 4d4d00aa6f: 1,691,729 account-days, worst abs diff 0.0, 82,593 month grades equal; the three tables hold 1,691,729 / 21,102,041 / 82,593 rows."
}
```

## ADVI_COTBKF-D2-W52-S2 -- the three tables are mostly blanks with a reason -- 6.4% of account-days carry a return, 24.2% of holding-days

```json
{
  "id": "ADVI_COTBKF-D2-W52-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~52",
  "surfaced_at": "2026-10-09T04:06:00Z",
  "one_line": "CB-aa-3: the three tables are mostly blanks with a reason -- 6.4% of account-days carry a return, 24.2% of holding-days a close; account_day_value is 21,102,041 rows (58 MB, one object)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python data/assets/scripts/silver/commonwealth_fwd3_serve.py --dry-run --data-dir .scratch/advi_cotbkf/r27 --out .scratch/advi_cotbkf/fwd3_serve: rows 1691729 / 21102041 / 82593",
      "pyarrow read of the three local tables: return notna 107453; close notna 5115115; verdicts {'UNGRADABLE': 78609, 'MATCH': 3098, 'DIFF': 886}",
      ".scratch/advi_cotbkf/r27/after_out/daily_valuation.md (holding_days 21102041, priced 5115115)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-3 reads 'an analyst reads its return for any single day from 2013 to June 2026'; the order builds the tables for serving as one object each.",
  "world_is": "daily_returns: 1,691,729 account-days, 107,453 with a return (6.4%); blanks 1,584,276 = UNPRICED 1,560,217, NON_POSITIVE_BASE 22,521, FIRST_DAY 1,533, FLOW_UNVALUED 5 (null with the reason, nothing filled). account_day_value: 21,102,041 holding-days, 5,115,115 with a close (24.2%), the rest null close and null value. month_grades: MATCH 3,098, DIFF 886, UNGRADABLE 78,609 of 82,593 (the round-25/26 run's own numbers, reproduced). account_day_value.parquet is 57,970,640 bytes written as a single part-00000.parquet; the hash is taken in 1,000,000-row chunks so the table is never one pandas frame. This is the delivery's price coverage, not a defect of the builder; it bounds what the served tables can answer and the size CB-aa-4 writes."
}
```

## ADVI_COTBKF-D2-W52-S3 -- only 35 of the 3,098 MATCH months belong to the 83 open accounts, and Commonwealth's Year row is not always a 

```json
{
  "id": "ADVI_COTBKF-D2-W52-S3",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~52",
  "surfaced_at": "2026-10-09T04:06:00Z",
  "one_line": "CB-aa-3: only 35 of the 3,098 MATCH months belong to the 83 open accounts, and Commonwealth's Year row is not always a calendar year; the one-account read and the Year join state their rules",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/silver/commonwealth_fwd3_serve.py@4d4d00aa6f (choose_account, _year_pick, reported_index)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~52/dry_run_ac2.log (ANALYST-READ account=RGY004256)",
      "python read of silver performance Month/Year/InceptionToDate at the performance_prefix builder address: 80709 / 6425 / 1520 rows"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order asks for the one-account read of 'a MATCHED, living client' and for the yearly figure 'beside' the computed month.",
  "world_is": "Of 3,098 MATCH months only 35 are on the 83 accounts open in the delivery's positions (4 of them on a non-flat security with a reported move of 0.5 pct or more); the read account is the open account with the most such months, RGY004256 (4 MATCH, 2 DIFF, 21 UNGRADABLE of 27 months, 547 days of which 160 carry a return), chosen by a stated rule (choose_account) and overridable with --account. Commonwealth's Year rows are calendar years, parts of a year, or an account's single cross-year span (560 of 6,425 cross a year end); the builder carries the Year row whose span overlaps the month with its start and end shown: 80,508 months have a Year figure, 1,901 months have none (no Year row covers the month, reported_note says so), InceptionToDate is present for 81,989 months, absent for 289 months and in conflict (two disagreeing rows) for 17."
}
```

## ADVI_COTBKF-D2-S40 -- L9 CB27aa1-AC3 NOT MET; CB27aa2-AC3, CB27aa3-AC3 MET

```json
{
  "id": "ADVI_COTBKF-D2-S40",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T04:44:16Z",
  "one_line": "L9 CB27aa1-AC3 NOT MET as written; CB27aa2-AC3 MET; CB27aa3-AC3 MET. CB27aa1-AC3 fails on 'nothing forced': REACH_CAP_PCT was moved 0.5 -> 1.0 after exploratory runs on the same 512 months (traced 70 -> 73, the worker's own disclosure), and the three months it admits include the ONLY flow_value month, so one of the three classes exists by a constant tuned on the outcome. The other two clauses hold (rule commit 4624627872 precedes the run; each class shown on a traced month's day values; 439 left untraced with what each cause leaves).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~50/ADVI_COTBKF.TO-CB-aa-1.trace-512.proof_of_spec.json controls.determinism ('the exploratory run before the reach cap moved from 0.5 to 1.0 gave traced=70')",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~50/diff_trace.md:15-21 (the rule states the cap 1.0, not that it moved), :87-166 (one traced month per class)",
      "data/assets/scripts/silver/commonwealth_price_need.py tier_of :115-121 against the CRO rule RESEARCH_20261008_COTTONWOOD_YAHOO_PRICE_BACKFILL_STRUCTURE.md:126-131",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~52/dry_run_ac2.log :1-6 (schemas) and the one-account read",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_27_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB27aa1-AC3, CB27aa2-AC3, CB27aa3-AC3 (the three judgment criteria of round 27).",
  "world_is": "CB27aa1-AC3: two of three clauses met, 'nothing forced' not met for the three months between the 0.5 and 1.0 caps. Remedy: re-run at the pre-registered 0.5, or keep 1.0 and label those three months 'traced at a cap set after the results'; either way flow_value is not an earned class until a month reaches under a cap fixed before it was seen. CB27aa2-AC3 and CB27aa3-AC3 met, with notes in the grade file."
}
```

## ADVI_COTBKF-D2-W53-S1 -- CB-ab-1: a test outside the order's paths asserts the superseded default and fails now that method_r28 is the default

```json
{
  "id": "ADVI_COTBKF-D2-W53-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~53",
  "surfaced_at": "2026-10-09T06:10Z",
  "one_line": "tests/test_commonwealth_unlisted_types.py:134 asserts CASH_LEG_DEFAULT == CASH_LEG_METHOD_R26 and fails with method_r28 the default; the file is outside the order's <paths>, so it was not edited",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~C2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -m pytest -q data/assets/scripts/silver/tests @8137a94e91: 1 failed, 717 passed, 11 skipped; the failure is test_commonwealth_unlisted_types.py::test_method_is_unchanged_and_stays_selectable, assert 'method_r28' == 'method_r26' at :134",
      "the three same-kind asserts that ARE in <paths> (test_commonwealth_carried_levels.py:57, test_commonwealth_cash_leg.py:305, test_commonwealth_method.py:227) were moved to method_r28 in commit 8fe7ffd558"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order makes method_r28 the DEFAULT and lists the test files it may edit; it asks for python -m pytest -q data/assets/scripts/silver/tests at the end.",
  "world_is": "A fourth test (test_commonwealth_unlisted_types.py, :134, also :135-136 read) pins the round-26 default and is not in <paths>. The suite therefore ends with exactly that one failure; no behaviour is wrong. The one-line change is `CASH_LEG_METHOD_R26` -> `CASH_LEG_METHOD_R28` on :134, for a seat whose paths include the file. Armed because a drain that runs the silver suite fails on it."
}
```

## ADVI_COTBKF-D2-W53-S2 -- CB-ab-1: the split repair's premise (stored closes are split-adjusted) fails for store-sourced splits of 464287614 / 464287481-class series; found by run 1 (regressions=61), corrected after it, disclosed

```json
{
  "id": "ADVI_COTBKF-D2-W53-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~53",
  "surfaced_at": "2026-10-09T06:10Z",
  "one_line": "Run 1 of the AC2 invocation gave regressions=61 (3 accounts) because dell1's store names a 4-for-1 of 464287614 on 2026-04-29 while the chain's stored closes for it are as traded; the first version scaled every earlier day x4. A continuity test on the store-sourced split was added AFTER run 1 (commit 8137a94e91) and run 2 was made",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~53/run1_pre_continuity/ac2_stdout.log: months_after=3078/893/78622 regressions=61, R28-REPAIRS splits_applied=36 disagreements=1",
      "run 1 regressions by account: 0QF880382 30, B3S804888 22, B3S804864 5, B3S728506 2, B3S728504 2; the first three hold 464287614 / 464287481 (store-sourced); 0QF880382's value on 2021-02-25 went 302,074.91 -> 596,039.55 under method_r28 against method_r26 (the same day, same cache)",
      "the order says a disagreement between the account rows and the store is printed and a split that cannot be confirmed is left as it is, named; the rows-sourced path required a continuous close across the day (commonwealth_diff_trace.confirm_splits), the store-sourced path did not -- an omission in this worker's rule, found through the grade, not through a second look at the stored closes first",
      "commit 8137a94e91 message: states the correction follows run 1 and is the only change after it; commits 8fe7ffd558, 34a595ecc0, 2ef83474dd preceded run 1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order item 1: for each confirmed split value every day before the split with the stored close x the cumulative ratio of later splits; where dell1's store holds the CUSIP its split history is the source; a split that cannot be confirmed leaves its days as they are, named. The order's premise: the stores' closes are split-adjusted over their whole history.",
  "world_is": "For some CUSIPs the chain's stored close is NOT split-adjusted across the store's split day (the close drops by the ratio, or has no row that day). Scaling such a series doubles or quadruples an account's value. Run 1 is kept unedited in the deliverables folder; run 2 (continuity applied to both sources) is the reported AC2 run. The CVO should read this as a rule changed after a run: whether it is an implementation correction of 'confirmed' or a fit is the L9 call (CB28ab1-AC3). Run 2's 61 -> 4 regressions are the effect, recorded; no further change was made."
}
```

## ADVI_COTBKF-D2-W53-S3 -- CB-ab-1: CB28ab1-AC2 NOT MET -- the AC2 invocation ends regressions=4 (B3S728504 and B3S728506, 2023-05 and 2023-06), not 0

```json
{
  "id": "ADVI_COTBKF-D2-W53-S3",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~53",
  "surfaced_at": "2026-10-09T06:10Z",
  "one_line": "AC2 (python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg method_r26 --after-cash-leg method_r28 ...) ends 'regressions=4' against the expected 'regressions=0'; the refusal clause applies, nothing further was tuned",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "last line of the AC2 run (rc 0) @8137a94e91: SWEEP-REGRADE sweeps=2 rejected=517 double_drop_months=0 fixed=0 months_before=3098/886/78609 months_after=3133/838/78622 control_same=True regressions=4 movers_back=139 year_chain_same=True r22_named=25/25 dividend_both=NA",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~53/sweep_regrade.md: the four months, MATCH under method_r26 and DIFF under method_r28 (computed before -> after, reported): B3S728504 2023-05 0.1418 -> 0.1813 (0.10), 2023-06 4.8344 -> 5.2399 (4.81); B3S728506 2023-05 0.1493 -> 0.1894 (0.11), 2023-06 4.8943 -> 5.2853 (4.86)",
      "the two accounts hold 808524102 (splits 2022-03-11 x2 and 2024-10-11 x3, rows-sourced, close continuous) and 808524839 (2024-10-11 x3): the repair raises B3S728504's value on 2023-04-28 from 11,121.73 to 27,199.01; the month's MATCH under method_r26 was within 0.0418 of the 0.05 band",
      "INFERRED, not measured: the larger weight now exposes a dividend-dating difference (pay date against ex-date; the cross-month dividend months are NOT GRADED, no ex-date source) that the smaller weight hid; no other repair of the three touches these accounts (the dvr rule only blanks, producing UNGRADABLE, and MATCH -> UNGRADABLE is 0)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB28ab1-AC2: the AC2 invocation ends regressions=0 ('the repairs regress no month that matched under method_r26').",
  "world_is": "regressions=4 after one disclosed correction (see D2-W53-S2); run 1 gave 61. Other effects of run 2: MATCH 3098 -> 3133, DIFF 886 -> 838, UNGRADABLE 78609 -> 78622 (13 DIFF -> UNGRADABLE by the dvr rule); movers_back 139; the 73 round-27 traced months: MATCH 27, DIFF 42, UNGRADABLE 4. No rule was changed to remove the four; choosing one by its effect on the grade is forbidden by the order. The SERVED mint (CB-ab-2) stays held at the COO half's condition."
}
```

## ADVI_COTBKF-D2-W53-S4 -- CB-ab-1: 28 of 61 detected splits cannot be confirmed (their earlier days stay on the stored basis, named), and the dvr close-step cause remains INFERRED

```json
{
  "id": "ADVI_COTBKF-D2-W53-S4",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~53",
  "surfaced_at": "2026-10-09T06:10Z",
  "one_line": "method_r28 detects 61 split events over the accounts' rows and the store (round 27's trace named 14 for the traced months); 33 are applied, 28 are UNCONFIRMED (close not continuous across the day, or no row that day) and left as they are, named; 1086 account-days on 35 distribution close-step security-days are blank (DVR_CLOSE_STEP), the cause of that step is not measured",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "AC2 run 2 stdout: R28-REPAIRS splits_applied=33 splits_not_applied=28 disagreements=0 dvr_close_step_security_days=35 dvr_account_days_blank=1086; every unconfirmed split is printed as an R28-SPLIT line and in org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~53/sweep_regrade.md",
      "the store-versus-rows disagreement is one CUSIP: 00162Q866, store 0.2 on 2020-05-18, the account rows show no such split, the stored close is not continuous across it: not applied",
      "the 28 include FCNTX 316071109 (10.0 on 2018-08-10), AAPL 037833100 (7.0 on 2014-06-09), and the 2026-04-21 events of 921910816 / 92204A702 / 922908629 / 922908736",
      "dvr: 309,330 dvr rows on non-cash CUSIPs; 2,173 security-days evaluated; the signature (close step 0.5..1.5 x the per-share distribution, the distribution at least 2 percent of the close) fired on 35; 13 DIFF months became UNGRADABLE, 0 MATCH months did"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order items 1 and 2: a split that cannot be confirmed leaves its days as they are, named; where the close step of a dvr day cannot be separated the day is blank with reason DVR_CLOSE_STEP.",
  "world_is": "The unconfirmed splits' earlier days are still valued at the stored close x the as-traded quantity, which is wrong if the stored series is adjusted for them and unchanged if it is as traded; the plan cannot tell. The dvr signature was fixed from the rows and closes before the run; whether the store is dividend-shifted is not shown. The COO half's condition on CB-ab-2 (D2-S39: no known-wrong day served) should read the plan table, not assume the 14."
}
```

## ADVI_COTBKF-D2-W53-S5 -- CB-ab-1: S1's red test is fixed under the issuer ruling (@e8bdbd5c38): test_commonwealth_unlisted_types.py:134 now asserts method_r28

```json
{
  "id": "ADVI_COTBKF-D2-W53-S5",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~53",
  "surfaced_at": "2026-10-09T06:18Z",
  "one_line": "the equality at test_commonwealth_unlisted_types.py:134 moved from CASH_LEG_METHOD_R26 to CASH_LEG_METHOD_R28, so D2-W53-S1's failing test passes; silver suite 718 passed, 11 skipped, 0 failed",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -m pytest -q data/assets/scripts/silver/tests on wk-ADVI_COTBKF-53: 718 passed, 11 skipped, 0 failed",
      "the order's <paths> gained data/assets/scripts/silver/tests/test_commonwealth_unlisted_types.py, identical to the trunk amendment e8bdbd5c38"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Row D2-W53-S1: a fourth test pins the round-26 default and is outside the order's paths, so the silver suite ends with one failure.",
  "world_is": "The ruling widened the grant by that one path; the equality and its trailing comment were changed and nothing else in the file. S1 is unedited; its armed hazard no longer has a red test behind it."
}
```

## ADVI_COTBKF-D2-W53-S6 -- CB-ab-1 AMENDMENT 1: the serve builder's re-derivation did not reproduce a method_r28 run until it applied the run's repair sidecar; fixed in the builder, no repair rule changed

```json
{
  "id": "ADVI_COTBKF-D2-W53-S6",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~53",
  "surfaced_at": "2026-10-09T06:45Z",
  "one_line": "commonwealth_fwd3_serve.py --build refused on the method_r28 run (re-derived day values differ from the run's, blank mismatches 13) because rederive() ignored the run's repair_days.parquet; it now applies the DVR_CLOSE_STEP days, and a holding-day carrying a reason is never valued",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "first --build on .scratch/advi_cotbkf/r28 at fc9435beb0 plus the ABSENT edit: 'refused: the re-derived day values differ from the run's (blank mismatches 13, worst abs diff 0.000e+00)'",
      "commonwealth_daily_valuation.py run() blanks av with blank_account_days(av, dvr_close_step_days(...)) and writes the sidecar; commonwealth_sweep_regrade.py chain() passes repair=dv.read_repair(data_dir) to daily_returns; the builder did neither",
      "second --build after the fix: day_values_rows_checked=1691729, month_grades_rows_checked=82593, absent_months=4, rc 0 (the build REFUSES unless both reproduce the run)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 1: the serve build takes its ABSENT list from the persisted grades of the AC2 run and its default cash leg is method_r28; CB-aa-3's builder was written against method_r26 and was assumed to re-derive any default run.",
  "world_is": "The builder's rederive() now reads the run's sidecar for method_r28 (blanks the account-days, passes repair to the daily returns) and marks those account-days' holding rows with blank_reason DVR_CLOSE_STEP and a null value; the account_day_value table gained a nullable blank_reason column (also carrying REGRESSED_UNDER_R28). No method_r28 rule, test of a rule or grade was changed. The built tables carry run_commit fc9435beb098, the HEAD the build ran on, which precedes the commit that holds this builder change."
}
```

## ADVI_COTBKF-D2-S41 -- L9 round 28: CB28ab1-AC3 NOT MET as written, the continuity rule a FIX; CB28ab3-AC3 MET

```json
{
  "id": "ADVI_COTBKF-D2-S41",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T07:21:34Z",
  "one_line": "L9 round 28: CB28ab1-AC3 NOT MET as written ('decided ... before the run' fails for one rule), but the post-run continuity rule is a FIX, not a fit -- it extends the row path's existing 0.7..1.4 stored-close continuity test to store-sourced splits, reads only stored closes (never the reported return), carries its own test, and run 1 is kept unedited; the other repairs (splits, DVR_CLOSE_STEP, INKIND_UNDERSTATED) were committed before run 1 and blank with reasons. CB28ab3-AC3 MET: cap 0.5 (the value pre-registered before round 27's exploratory runs, per D2-S40), the 3 months traced only at 1.0 named with their 0.5 remainders, and nothing else in the rules changed (diff 4624627872..HEAD: the cap, the last line's cap= field, report layout only).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git show 8137a94e91 (the continuity rule, disclosed; test_a_store_split_on_a_series_that_is_as_traded_across_the_day_is_not_applied)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~53/run1_pre_continuity/",
      "git diff 4624627872 HEAD -- data/assets/scripts/silver/commonwealth_diff_trace.py (this seat's read)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~54/diff_trace.md:665-674",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_28_DRAIN_END_20261009.md @57d5583a6f",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_28_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB28ab1-AC3 and CB28ab3-AC3 (round 28's judgment criteria); CB28ab1-AC3 carries the CTO's fit-vs-fix grade (msg 2671).",
  "world_is": "CB28ab1-AC3: fix, not fit -- the condition for CB-ab-2's mint (CTO msg 2671) reads FIX. The literal clause fails for one disclosed rule. CB28ab3-AC3 met."
}
```

## ADVI_COTBKF-D2-W56-S1 -- CB-ac-3: 3 of 28 unconfirmed splits are confirmable on the store's own close; 25 CUSIPs are not in the store (32 rows, newest as_of 2026-06-23); the 3 were unconfirmed because the chain's close, not the store's, failed continuity

```json
{
  "id": "ADVI_COTBKF-D2-W56-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~56",
  "surfaced_at": "2026-10-09T07:40Z",
  "one_line": "SPLIT-RECOUNT unconfirmed=28 now_confirmable=3 store_rows=32 store_as_of=2026-06-23: 00162Q866 (2020-05-18 x0.2), 464287614 (2026-04-29 x4), 464288646 (2018-08-08 x2) are in the store, its splits.parquet names the split, and the store's close_served is continuous across the day; the other 25 splits' CUSIPs are not in the store",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~56/split_recount.md, from python data/assets/scripts/silver/commonwealth_split_recount.py (rc 0)",
      "the same 3 were already store-sourced in the round-28 plan and failed continuity there on the chain's own nine-store close series (commonwealth_daily_valuation.split_plan), which the price fill does not change"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-ac-3: print for each of the 28 whether the continuity condition would now hold, i.e. whether the split is now confirmable.",
  "world_is": "The recount tests continuity on the store's close_served, the only series the fill adds. The apply-time condition in split_plan tests the chain's series (the nine stores), so now_confirmable=3 is an upper bound: those 3 become applicable only if the chain reads the store's close for them. Nothing was applied."
}
```

## ADVI_COTBKF-D2-W55-S1 -- CB-ac-2: no source holds the ex-dates of 808524102 / 808524839; the 4 months are untraced by the rule

```json
{
  "id": "ADVI_COTBKF-D2-W55-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~55",
  "surfaced_at": "2026-10-09T08:00:00Z",
  "one_line": "CB-ac-2: neither ex-date source holds the two dividend CUSIPs of the 4 regressed months (808524102, 808524839), so the ex-dated return cannot be computed; all 4 months class untraced by the pre-committed rule",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~55/div_dating_trace.md (DIV-TRACE months=4 dividend_dating=0 other=0 untraced=4)",
      "git show 9de2bd74ef (the class rule, committed before the run)",
      "EXDATES_ADVI_COTBKF_20261009.csv: 39 rows, no 8085 CUSIP; dell1 price_history store: 32 cusip= partitions listed, none 8085*"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order's cell: ex-dates are available from dell1's price store and the 39-row EXDATES csv, so the month's return at the ex date can be computed.",
  "world_is": "Neither source holds 808524102 or 808524839, the only two dividend CUSIPs of both accounts in the window. Also read: r28/r26 account day value ratio is 2.44-2.47 in all four months (a split-scaled position since 2022-10-12), and the largest pay-ex gap in the csv is 26 days, which widens the candidate bound to about 0.41 pp against regressions of 0.04-0.41 pp. Ex-dates for the two Schwab CUSIPs would settle the dating question."
}
```

## ADVI_COTBKF-D2-S42 -- CB-ac-1: step 3's regressions=0 precondition is stale; the pair and the order's own later paragraph require regressions=4 NAMED and BLANKED

```json
{
  "id": "ADVI_COTBKF-D2-S42",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~CB2",
  "surfaced_at": "2026-10-09T08:20:00Z",
  "one_line": "TO CB-ac-1 step 3 still gates the mint on CB-ab-1 draining with regressions=0, a precondition the round-28 rulings and both halves of its own never-widen pair had already replaced with regressions=4 NAMED and BLANKED; read literally the step is an unsatisfiable wait",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "the order's step 3: 'From the drained trunk, after CB-ab-1 drains VALID with regressions=0'",
      "the order's own later paragraph, which disagrees with it: 'The build to apply carries method_r28 with exactly 4 account-months ABSENT (B3S728504, B3S728506; 2023-05, 2023-06): your --dry-run must print the same 4 and absent_months=4, or stop'",
      "CTO half AMENDMENT 1 @478334e021: 'condition 1 relaxed to regressions = 4 NAMED and BLANKED'; COO half section 3 gives on that same basis",
      "CB-ab-1's own AC2 was amended @5c9e31b2be to EXPECT regressions=4 (a fifth voids the amendment), and it delivered @15e50bfbc1 on that expectation",
      "this seat's re-grade at its own HEAD, rc 0: SWEEP-REGRADE ... control_same=True regressions=4 year_chain_same=True"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CB-ac-1 step 3: the mint proceeds after CB-ab-1 drains VALID with regressions=0.",
  "world_is": "regressions=0 is unreachable for method_r28 by RULING, not by defect. The order carries both readings at HEAD; the act was graded against the pair and the order's later paragraph, which agree with each other and with the measured world (regressions=4, absent_months=4, the four being exactly B3S728504 and B3S728506 at 2023-05 and 2023-06, each served BLANKED with reason REGRESSED_UNDER_R28 and never valued). Nothing was weakened and nothing was waited on. The stale clause cost this seat nothing because it read the pair first, but a seat reading step 3 alone would hold a SERVED act forever on a condition no build at the chain's own default cash leg can meet."
}
```

## ADVI_COTBKF-D2-S43 -- CB-ac-1: the order's WCB2 row-id form is unparseable by proof-of-spec-check.py's SURPRISE_ID_RE

```json
{
  "id": "ADVI_COTBKF-D2-S43",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~CB2",
  "surfaced_at": "2026-10-09T08:22:00Z",
  "one_line": "TO CB-ac-1's refusal clause names the row id form ADVI_COTBKF-D2-WCB2-S<k>, which proof-of-spec-check.py's SURPRISE_ID_RE cannot parse, so a row filed exactly as the order instructs makes the instance INVALID and blocks the complete flip",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "the order's refusal clause: 'a NEW surprise row (id ADVI_COTBKF-D2-WCB2-S<k>, \"fabric\": \"dell2\")'",
      ".tools/proof-of-spec-check.py:1206 SURPRISE_ID_RE = ^\\s*([A-Z0-9_]+-(?:(?!W[0-9]*-|C-)[A-Z][0-9]*-)?(?:W[0-9]+-|C-)?S[0-9]+)\b -- the W arm is W[0-9]+, so W followed by letters does not match",
      "measured both forms against that regex: ADVI_COTBKF-D2-WCB2-S1 REJECTED, ADVI_COTBKF-D2-S42 PARSES",
      "channel census, denominator printed: 125 row ids in ADVI_COTBKF's channel, of which 21 are the non-worker D2-S<n> form, max n = 41"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "A row this seat files under the order's named id form is a valid citation in the proof-of-spec instance.",
  "world_is": "It is not. SURPRISE_ID_RE admits a lane segment only as a single letter plus digits ([A-Z][0-9]*) or as W<digits> / C, so WCB2 falls outside both arms and the checker reports 'surprises[0] carries NO row id'. The gate is the mechanical authority named in the order's own <proof_of_spec> block, so these two rows were filed in the project's existing non-worker namespace (D2-S42, D2-S43) rather than under the order's prose form, and this row records the departure instead of silently renaming. The order's intent -- a NEW row from this seat, fabric dell2 -- is met. A future ~<lane> seat told to mint W<non-numeric> ids hits the same wall; the fix is the issuer's to make, either in the clause or in the regex."
}
```

## ADVI_COTBKF-D2-S44 -- L9 CB29ac2-AC2 MET

```json
{
  "id": "ADVI_COTBKF-D2-S44",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T08:35:55Z",
  "one_line": "L9 CB29ac2-AC2 MET: each of the 4 months is classed by the pre-committed rule from the printed rows -- ex-date sources searched (39-row EXDATES csv, 32-CUSIP store listing), candidates within the 26-day lag, bound_pp from the candidates' amounts against the r28 value, compared with regression_pp = r28 - r26 computed; the reported return is printed for context and enters no decision. All 4 untraced, each naming what was checked.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~55/div_dating_trace.md (four month sections)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_29_DRAIN_END_20261009.md @48715ba8d8",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_29_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB29ac2-AC2: the class of each month is decided by the script's rule from the printed rows, not from the reported return.",
  "world_is": "Met as written."
}
```

## ADVI_COTBKF-D2-S45 -- the re-count tests a different series; a constant r28/r26 value ratio on two accounts

```json
{
  "id": "ADVI_COTBKF-D2-S45",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T08:35:55Z",
  "one_line": "Two findings from this seat's L9 read. (1) The split re-count's 'continuous' (W56-S1) is measured on the store's close_served, which is split-ADJUSTED by construction and so always continuous across a split; round 28's rule tests the CHAIN's stored close, the series the repair scales. The two tests measure different series, so the re-count does not contradict round 28 on 464287614 or 00162Q866. (2) On B3S728504 and B3S728506, method_r28's day values are 2.43-2.47x method_r26's on EVERY valued day, not only in the 4 regressed months. A constant ratio barely moves a month's return, so month grades can still MATCH while the served account_day_value carries a level that differs from r26 by that factor; which level is right is unmeasured.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~56/split_recount.md:4 ('Continuity is tested on the store's close_served (split-adjusted)')",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~55/div_dating_trace.md (r28/r26 ratio min/max per month: 2.4365-2.4641)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_29_DRAIN_END_20261009.md @48715ba8d8"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-3's served account_day_value carries each account's true daily value; the round-29 packet reads the re-count as contradicting round 28's continuity test.",
  "world_is": "(1) No contradiction: different series. (2) Open: the level of two accounts' served day values differs between methods by a constant ~2.45; the packet's lead (a split applied to closes already as traded) fits it. To be traced before the served values are relied on for these accounts."
}
```

## ADVI_COTBKF-D2-W57-S1 -- the delivery holds no outside price for the two scaled CUSIPs; both accounts class untraced

```json
{
  "id": "ADVI_COTBKF-D2-W57-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~57",
  "surfaced_at": "2026-10-09T09:10:00Z",
  "one_line": "CB-ad-1: the factor on B3S728504 and B3S728506 is wholly the two equity CUSIPs 808524102 (close28/close26 = 3.0000) and 808524839 (2.0000), each equal to the product of the APPLIED plan splits dated 2024-10-11 (rows source) on all 5 scaled sample days per account; implied cash is identical under r26 and r28 (not the cash leg). The pre-written rule needs an outside price to choose a level, and the delivery has none: the two CUSIPs enter only as li/trfi/QA/dv/lo rows (Amount 0 on the position rows), no by/sl, so 0 of 10 carrier-days per account have a trade price within 5 days. Both accounts class untraced:0 carrier-days with an outside price. Not a class: the plan applied the split because the chain close was continuous across 2024-10-11, and S45 (1) records the store close as split-adjusted by construction, which would put r26 short by the factor (r28 right) -- an inference from the series' construction, not an outside value. The first run raised a pandas TypeError in outside_price (date vs Timestamp); fixed in the same file, rule untouched.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~57/scale_trace.md (per-CUSIP rows, both Class lines)",
      "data/assets/scripts/silver/commonwealth_scale_trace.py @3d3ddbceb5 (rule committed before the run)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB-ad-1: where the delivery holds an outside level (reported market value or position value) it is printed beside both and says which level is right.",
  "world_is": "The delivery holds no market or position value (silver positions: quantity only) and no trade price for 808524102 or 808524839 (no by/sl rows in 2020-08-21..2026-05-27); the level question needs a source outside the delivery (a vendor close as traded on a pre-split day)."
}
```

## ADVI_COTBKF-D2-S46 -- L9 CB30ad1-AC2 MET

```json
{
  "id": "ADVI_COTBKF-D2-S46",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T09:04:24Z",
  "one_line": "L9 CB30ad1-AC2 MET: each account's class (untraced) follows from the printed per-CUSIP rows by the rule committed @3d3ddbceb5 before the first run (the only later change, @816400901c, is a one-line date-type conversion, no rule); the rows show the factor carried by 808524102 (close ratio 3.0000, x3 2024-10-11) and 808524839 (2.0000, x2 2024-10-11), cash identical, and no outside trade price within 5 days. No 'which level is right' claim is made as measured: the r28-is-right reading is labelled an INFERENCE (W57-S1), and the settling outside value (an as-traded close) is proposed for round 31.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~57/scale_trace.md",
      "git diff 3d3ddbceb5 816400901c -- data/assets/scripts/silver/commonwealth_scale_trace.py (one line)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_30_DRAIN_END_20261009.md @6a163e8b24",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_30_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB30ad1-AC2: each account's class follows from the printed per-CUSIP rows by the script's pre-written rule, and the 'which level is right' statement rests on an outside value where one exists.",
  "world_is": "Met. An outside value exists outside the delivery (an as-traded close from MDPF_DEMQUE or Yahoo) and was not read in this read-only cell; D2-S45 stays OPEN until it is."
}
```

## ADVI_COTBKF-D2-W58-S1 -- Yahoo as-traded closes on 2022-10-12 match neither r28 nor r26 for 808524102 (SCHB) and 808524839 (SCHZ); branch OTHER

```json
{
  "id": "ADVI_COTBKF-D2-W58-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~58",
  "surfaced_at": "2026-10-09T09:20:00Z",
  "one_line": "CB-ae-1: Yahoo (yfinance 1.2.0, auto_adjust=False) Close on 2022-10-12 x Yahoo's own later splits (both x3/x2 on 2024-10-11, same ratios as the rows) gives as_traded SCHB 13.98 x3 = 41.94 vs r28 39.9906 (+4.9%) and r26 13.3302; SCHZ 22.465 x2 = 44.93 vs r28 39.4362 (+13.9%) and r26 19.7181. Neither CUSIP is within 2% of r28 or r26, so the pre-written rule prints branch OTHER. Direction: the store close is below the outside level on both (r28 -4.7% / -12.2% of as_traded), and the shortfall differs per CUSIP, so it is not a split-factor error alone. Evidence stored at the price_evidence key (2 rows, read back).",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~58/split_level_probe.md",
      "data/assets/scripts/silver/commonwealth_split_level_probe.py (rule in header, written before the first run, unchanged)",
      "s3://opal-data-assets/commonwealth/cottonwood/silver/price_evidence/date=2022-10-12/part-00000.parquet"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB-ae-1: one outside as-traded close per CUSIP settles whether r28 or r26 is the right level (both within 2% of one).",
  "world_is": "Neither level matches the outside as-traded close; r28 is closer than r26 on both CUSIPs but off by 4.9% and 13.9%. The store's 2022-10-12 closes for these CUSIPs carry a further difference (source, date alignment or price basis) that a split-level test cannot settle. Symbols: SCHB from the delivery transactions Symbol column (66 rows, one distinct value), SCHZ likewise and per PRICE_NEED csv."
}
```

## ADVI_COTBKF-D2-W59-S1 -- chain base close for SCHB/SCHZ is a Yahoo-labelled stored series at a constant ratio to Adj Close; class other_source by the written rule

```json
{
  "id": "ADVI_COTBKF-D2-W59-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~59",
  "surfaced_at": "2026-10-09T10:00:00Z",
  "one_line": "CB-af-1: the chain's SCHB and SCHZ close is the cottonwood silver canonical_prices row (field price, ticker key, source label yahoo_finance, same-day row); it sits at a CONSTANT ratio to today's Yahoo Adj Close (SCHB 1.0054, SCHZ 1.0216 on every sampled day) but 0.9214..1.0000 / 0.8777..1.0000 to Close. By the pre-written rule the class is other_source:yahoo_finance for both (adj_close_base needs 0.5%: SCHB misses by 0.04 pt, SCHZ by 1.7 pt).",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~59/base_close_trace.md",
      "data/assets/scripts/silver/commonwealth_base_close_trace.py (rule in header, written before the first run, unchanged)",
      "s3://opal-data-cot/silver/prices/canonical_prices.parquet"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB-af-1: the chain's base close for SCHB and SCHZ traces to a named source and class (adj_close_base / stale_carry / other_source / untraced).",
  "world_is": "The chain reads a Yahoo-sourced stored price series that is a dividend-adjusted level from an earlier fetch vintage, not today's Close. The constant ratio to Adj Close says one adjustment vintage; a 0.5% test cannot call it adj_close_base because the vintages differ (SCHB 0.54%, SCHZ 2.16%). Also: 10 of 25 SCHB and 7 of 15 SCHZ candidate sample days (first calendar-quarter day, e.g. 2022-01-01) are non-trading stored days (linear_interpolation rows) with no Yahoo bar; the rule skipped them (listed in the md), so the sample is 15 and 8 days, not one per quarter."
}
```

## ADVI_COTBKF-D2-S47 -- L9 CB32af1-AC2 MET (two notes)

```json
{
  "id": "ADVI_COTBKF-D2-S47",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T09:53:30Z",
  "one_line": "L9 CB32af1-AC2 MET, with two notes. The class (other_source, both CUSIPs) follows from the printed per-day rows by the script's rule (TOL 0.5%, SHARE 80%): chain/AdjClose is a constant 1.0054 (SCHB) and 1.0216 (SCHZ), above TOL, so not adj_close_base. The named source is the one the chain reads: commonwealth_daily_valuation imports commonwealth_price_census, whose STORES[0] is cottonwood-silver-canonical-prices read on column price (this seat's read). Notes: (1) the rule and its output landed in one commit (0af60ccd42), so 'written before the first run' is the worker's statement, not git-ordered; (2) SCHB's 1.0054 sits 0.04 points over the 0.5% TOL, so its class turns on the tolerance -- but either class gives the same reading (a dividend-adjusted vintage), so no outcome rides on it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~59/base_close_trace.md",
      "data/assets/scripts/analysis/commonwealth_price_census.py STORES[0]; data/assets/scripts/silver/commonwealth_daily_valuation.py:48 imports it",
      "git show --stat 0af60ccd42 (rule and output in one commit)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_32_DRAIN_END_20261009.md",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_32_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB32af1-AC2: the class follows from the printed per-day rows by the pre-written rule, and the named source is the one the chain actually reads.",
  "world_is": "Met; the two notes stand."
}
```

## ADVI_COTBKF-D2-S48 -- the cottonwood price store carries a `bd_txn_price` source label

```json
{
  "id": "ADVI_COTBKF-D2-S48",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~C2",
  "surfaced_at": "2026-10-09T09:59:02Z",
  "one_line": "Sizing the round-33 census, the cottonwood price store s3://opal-data-cot/silver/prices/canonical_prices.parquet (11,291,021 rows, 4,003 tickers) carries 6 source labels; one is bd_txn_price (1,623 rows, 3 tickers). Whether 'bd' names the Black Diamond reporting platform's transaction price for cottonwood accounts, or the separate bd firm's data, is unread; the cross-firm law (cot is a separate firm from bd) makes the second reading a hazard to rule out.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "issuer read ~10:0xZ: source value_counts = linear_interpolation 7,831,140; yahoo_finance 3,396,067; transaction_observed 50,143; scoped_override 12,042; bd_txn_price 1,623; transaction_observed_capped 6",
      "tickers by source: bd_txn_price 3"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CLAUDE.md NEVER: a pipeline tree never references another firm's data (cot is a separate firm from bd).",
  "world_is": "A cot store row source reads bd_txn_price on 1,623 rows; its provenance is unread. Folded into round 33's census cell (name the 3 tickers and the writer of the label).",
  "disarm_owner": "2.0.0_SA_COO~C2"
}
```

## ADVI_COTBKF-D2-W60-S1 -- The only repo code that writes the bd_txn_price label is in the bd firm's tree (data/black_diamond/scripts/sil

```json
{
  "id": "ADVI_COTBKF-D2-W60-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~60",
  "surfaced_at": "2026-10-09T10:41Z",
  "one_line": "The only repo code that writes the bd_txn_price label is in the bd firm's tree (data/black_diamond/scripts/silver/inject_scoped_overrides.py:136 default, force_source set at scoped_price_exceptions.json:10,18,26); no writer in data/cot, yet the cottonwood price store carries its 1,623 rows on 3 CUSIP_ tickers.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git grep -n -F bd_txn_price -- '*.py' '*.json' at worktree HEAD e5b8ad94ba: 8 hits; writer = data/black_diamond/scripts/silver/inject_scoped_overrides.py:136 (src = exc.get('force_source', 'bd_txn_price')); the label values come from data/black_diamond/scripts/silver/scoped_price_exceptions.json lines 10, 18, 26; data/cot/scripts/gold/B_01.holdings_lots.py:2263 mentions it in a comment only",
      "store rows (org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~60/price_basis_census.md section 5): CUSIP_05613L3H2 431 rows 2024-10-15..2026-06-09 at 1.0188; CUSIP_651639AX4 572 rows 2024-04-01..2026-06-09 at 0.9037; CUSIP_95000U2D4 620 rows 2024-01-24..2026-06-09 at 0.9804; each a constant price",
      "data/tier2_senior 0.4.0_DS_ClientPlatform logs 2026-04-15 (wp11_and_3bond_formalization.md:74) name the same three CUSIPs (BNP, WFC, NEWMONT) and prices as the bd firm's inception-price overrides"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CB-ag-1 item 5: print the 3 bd_txn_price tickers, their dates, and which code writes the label, from repo search; row D2-S48 asks whether the label is cottonwood's own or the bd firm's data.",
  "world_is": "The repo's only writer is the bd firm's inject_scoped_overrides.py; the 3 CUSIP_ tickers and prices equal the bd firm's scoped overrides. The route by which those rows reached the cottonwood store (a copy of the bd build, or a cot-side writer outside the repo) is unread; reading the bd bucket to find out is barred. Not a class input: the 3 tickers carry no yahoo_finance rows in the census."
}
```

## ADVI_COTBKF-D2-W60-S2 -- The Yahoo pass was one pass of 72 network calls in the real run, plus 1 earlier call from a 12-ticker debug ru

```json
{
  "id": "ADVI_COTBKF-D2-W60-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~60",
  "surfaced_at": "2026-10-09T10:41Z",
  "one_line": "The Yahoo pass was one pass of 72 network calls in the real run, plus 1 earlier call from a 12-ticker debug run whose pulls were cached and reused: 73 Yahoo calls in total, 0 rate-limited.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "real run log: 'yahoo call 1..72' at <=50 tickers each (3,568 fetched, 12 reused from cache), pause 6 s between calls, no rate-limit text; last call 72 of 18 tickers",
      "debug run .scratch/dbg1 (--max-tickers 12 --skip-served) made 1 call; its 12 per-ticker pulls sit in .scratch/advi_cotbkf/yahoo_census/ and the full pass reused them"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CB-ag-1: make one pass, at most 50 tickers per call, at least 5 s apart, print the call count; develop with --max-tickers before the full pass.",
  "world_is": "The final line prints yahoo_calls=72 (the full pass counted from an already-cached 12). The debug call made 73 total. The class rule was unchanged between the debug runs and the full run (script blob identical to the rule commit e5b8ad94ba)."
}
```

## ADVI_COTBKF-D2-S49 -- L9 CB33ag1-AC2 MET

```json
{
  "id": "ADVI_COTBKF-D2-S49",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T10:50:45Z",
  "one_line": "L9 CB33ag1-AC2 MET: the rule commit e5b8ad94ba (06:10 ET) precedes the output commit 3a063e09a6 (06:42), and git shows no .py change between them; each of the 3,580 tickers' class follows from its printed comparison by that rule (TOL 0.5%, SHARE 80%, MIN_OVERLAP 20, MIXED_FLOOR 0.20): e.g. dividend_adjusted = store/AdjClose constant on >= 80% of days and store/Close drifting beyond TOL, printed per row with share_close, share_adj, share_ra_c, rc_spread, the medians and the implied vintage.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git log e5b8ad94ba / 3a063e09a6; git diff --stat e5b8ad94ba 3a063e09a6 on the scripts (empty)",
      "git show e5b8ad94ba:data/assets/scripts/silver/commonwealth_price_basis_census.py (CLASS RULE, docstring lines 22-42)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~60/price_basis_census.csv (3,580 rows, each with class, reason and its ratios)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_33_DRAIN_END_20261009.md @2fc7789480",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_33_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB33ag1-AC2: the rule commit precedes the output commit in git, and each class follows from the printed comparison by that rule.",
  "world_is": "Met as written."
}
```

## ADVI_COTBKF-D2-S50 -- the served FWD-3 tables rest materially on dividend-adjusted prices, unmarked

```json
{
  "id": "ADVI_COTBKF-D2-S50",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T10:50:45Z",
  "one_line": "The SERVED FWD-3 tables rest materially on dividend-adjusted prices: in account_day_value, 638,948 of 1,669,040 account-days (38.3%), 688 of 1,528 accounts and 31,249 of 81,718 account-months (73 of 159 months) hold at least one position priced from a dividend_adjusted or mixed ticker, while the chain also books dividends as cash. Until CTO ADDENDUM 8 item 2's marking and rebuild land, a reader of those served rows sees values on the wrong basis with no mark.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_33_DRAIN_END_20261009.md @2fc7789480 (served-table counts, the issuer's run equal to the worker's)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~60/price_basis_census.csv (3,580 rows, each with class, reason and its ratios)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-3's served tables carry each account's true daily value and return; a figure on a known-wrong basis is marked or blanked (CTO ADDENDUM 8 @bff4e48547 item 2).",
  "world_is": "Served on the wrong basis for 38% of account-days, unmarked today; the marking and rebuild (CB-ag-2, CB-ag-3) are drafted @a9a774a7b9, not yet cut."
}
```

## ADVI_COTBKF-D2-W61-S1 -- the writer of the cot store's bd-txn-price rows is BD-tree code with BD inputs (class cross_firm)

```json
{
  "id": "ADVI_COTBKF-D2-W61-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~61",
  "surfaced_at": "2026-10-09T11:05:09Z",
  "one_line": "CB-ah-1 class=cross_firm: the only writer of the bd-txn-price label, data/black_diamond/scripts/silver/inject_scoped_overrides.py:136, takes its prices from a 49 Financial repo file (scoped_price_exceptions.json, :62) and module (bd_price_update.py _SCOPED_PRICE_OVERRIDES, :80), and its code default reads and writes s3://opal-data-bd/silver/prices/canonical_prices.parquet (:54,:179,:253); no cot-tree code calls it (data/cot/scripts/gold/build_canonical_prices_v2.py:24 says cot does NOT run it), so how 1,623 rows of those three BD-sourced CUSIP prices came to be in the opal-data-cot store is NOT shown by the repo.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~61/bd_txn_writer_trace.md (static repo trace, no S3 call; last line class=cross_firm)",
      "data/black_diamond/scripts/silver/inject_scoped_overrides.py:54,62,80,136,179,253",
      "data/cot/scripts/gold/build_canonical_prices_v2.py:24 (cot does not run the inject); env BD_S3_BUCKET=opal-data-cot is set by infra/aws/terraform/cot-pipeline/ssm.tf:233,331 and data/cot/scripts/gold/gold_dispatch.sh:62, but no cot-side code invokes the writer",
      "scoped_price_exceptions.json carries no account id, only 3 CUSIPs and asset names"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Cottonwood and BD / 49 Financial are separate firms, never mirrored; a cot price-store row labelled with the BD override label has a cot-owned origin.",
  "world_is": "The writer is BD-tree code with BD-derived inputs; a run with the env bucket pointed at the cot bucket (a runtime act the repo does not show) is the only way the writer reaches the cot store; the repo cannot say which run did."
}
```

## ADVI_COTBKF-D2-W63-S1 -- CB-ai-1 detector corrections and builder-in-force reading (class shared_builder_run)

```json
{
  "id": "ADVI_COTBKF-D2-W63-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~63",
  "surfaced_at": "2026-10-09T11:50:00Z",
  "one_line": "CB-ai-1: the run-1 detector of the committed class rule over-matched (docstring lines read as live cot paths; same-run daily files read as a prior carrier) and no cot-path builder commit exists before the store write, so the rule's 'revision in force' was read from the seed commit 6b0be4337e plus the shared builder path; class=shared_builder_run after the detector was corrected (rule text unchanged).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "rule commit 5c79b91853 (script docstring, no output)",
      "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~63/bd_txn_provenance.md sections 2-4",
      "run 1 (first output) printed class=live_cot_path:data/cot/scripts/gold/B_01.holdings_lots.py:2263, a module docstring line, and build_canonical_prices_v2.py:24, also a docstring; run 2 uses ast to skip docstrings/comments and treats only an earlier-than-60s hit as a prior carrier",
      "git log: data/cot/scripts/gold/build_canonical_prices_v2.py first commit 6b0be4337e 2026-06-10, after the store write 2026-06-09T20:42:16Z; that seed revision auto-chains inject_scoped_overrides (lines 22,481,669) and was removed 319a716cb4 2026-06-12"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The class rule reads the cot builder revision in force at the store LastModified from git log; a cot builder revision exists at that time.",
  "world_is": "The cot-path builder entered git (as a faithful S3 seed) the day after the store write; the writer-in-force is the seed's content, which still auto-chained the 49F inject; the grader should confirm the seed-as-in-force reading and the 60 s same-run reading."
}
```

## ADVI_COTBKF-D2-W62-S1 -- AC2's invocation names no --grades, so the build reads <data-dir>_out/month_grades_{after,before}.parquet; AC1

```json
{
  "id": "ADVI_COTBKF-D2-W62-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~62",
  "surfaced_at": "2026-10-09T11:35Z",
  "one_line": "AC2's invocation names no --grades, so the build reads <data-dir>_out/month_grades_{after,before}.parquet; AC1 writes them to its --out (the deliverables folder), so they were copied to .scratch/advi_cotbkf/r34_out/ for AC2 to run as written.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "commonwealth_fwd3_serve.py build(): grades_path default = Path(str(data) + '_out') / GRADES_AFTER (a65776f167)",
      "cp of org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~62/month_grades_{before,after}.parquet to .scratch/advi_cotbkf/r34_out/; the worktree also had no tx cache or price cache, so .scratch/advi_cotbkf/cache and fwd3/price_cache were copied from the base checkout's .scratch (local files, no S3 write)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CB34ah2-AC2 runs --build --data-dir .scratch/advi_cotbkf/r34 --out ... as written after AC1.",
  "world_is": "It runs as written only after the two grade files sit at <data-dir>_out; the copy is a byte copy of AC1's own output (CB-ah-3's applier needs the same step)."
}
```

## ADVI_COTBKF-D2-W62-S2 -- The committed as-traded rule drops 3,962 linear_interpolation days that lie after (3,959) or before (3) a tick

```json
{
  "id": "ADVI_COTBKF-D2-W62-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_COTBKF~62",
  "surfaced_at": "2026-10-09T11:36Z",
  "one_line": "The committed as-traded rule drops 3,962 linear_interpolation days that lie after (3,959) or before (3) a ticker's last/first yahoo_finance point: the store interpolated them toward a non-Yahoo neighbour (transaction_observed), and the rule brackets by replaced Yahoo points only; 36 priced holding-days are lost (5,115,115 -> 5,115,079).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "PRICE-BASIS arm=AFTER line of the AC1 run: points_replaced=1049193 points_dropped_no_close=0 days_rederived=477980 days_dropped_unbracketed=3962; BEFORE priced=5115115, AFTER priced=5115079",
      "store read (price_cache canonical prices, the 911 substituted tickers): LI days outside [first, last] yahoo_finance day = 3962 on 911 tickers' rows, 5 tickers with 65-68 each (SDIV, TDTT, WAL, SPYI, UHS); e.g. HLN transaction_observed 19194 then LI 19195-19197 then yahoo_finance 19198",
      "rule at 2536c4fc09 (committed before the run): 'a day with a replaced point on only one side is dropped'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CB-ah-2 item 1: re-derive the ticker's linear_interpolation days linearly between the replaced points; nothing else changes.",
  "world_is": "Days with a replaced point on one side only cannot be derived from replaced points; they are blank, never filled. The rule was not changed after the run; widening the neighbours to include the store's transaction_observed points would restore up to 36 holding-days and is the COO's/CTO's call."
}
```
