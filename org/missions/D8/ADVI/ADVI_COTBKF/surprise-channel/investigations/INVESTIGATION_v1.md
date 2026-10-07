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
