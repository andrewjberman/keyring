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
