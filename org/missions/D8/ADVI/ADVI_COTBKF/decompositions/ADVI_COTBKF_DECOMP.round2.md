# ADVI_COTBKF decomposition -- ROUND 2, the recut (issuer 2.0.0_SA_COO~C; drafted 2026-10-06 ~20:1xZ)

**Status: DRAFT -> ISSUED in one issuance** (the issuance commit carries the `fanout:` line).

**Cut on:**
- The CTO's round-1 analysis, PRD v0.4 @51a7c07278 (ADMITTED: ratified-text half SIGNED by `3.0.0_SA_CVO`, current by ENDPOINT hash;
  brief half accepted). Its rulings: C-SILVER keeps EVERY delivered record with its source record number; FWD-1 reads as far back as
  Commonwealth recorded it; FWD-9 added (a client across a Commonwealth account change). "Recut in one issuance: rebuild silver
  transactions to 1,416,497 ... then the backlog" (msgs 105714, 105718).
- Round-1 close @b168025b06; rows S1, W1-S1, W2-S1, S2, S3 (`surprise-channel/investigations/INVESTIGATION_v1.md`).

**Rule 24.** Domain: the remediation (silver transactions loses 1,360 delivered records) plus the ENRICHMENT BACKLOG's head that is cuttable
now -- item 1 (performance and positions to silver; the daily-return build's price-coverage read first) and item 2 (the coverage table).
Excluded, with the reason: the daily-return BUILD itself (C-DAILY steps 1-4) waits on the price-coverage read this round produces; item 3
(the CRM) waits on C-RESTRICTED's bucket policy being live (manifest S09, an AE's Terraform act) -- no byte of the CRM zip before it;
items 4 (imaging and documents) and 5 (crosswalk) and FWD-9 follow in round 3. Four cells, one intent each, disjoint write sets.

## Measured constraints (read at the base, 2026-10-06 ~20:0xZ)

1. **Transactions** (row S3, recounted by the CTO): 1,416,497 records on 1,416,500 physical lines (three records of account
   acct#1059baa6 each span two lines through a CRLF inside a quoted `Transaction_Note`); 1,360 record-level repeats. Silver today
   (`s3://opal-data-assets/commonwealth/cottonwood/silver/transactions/date=2026-06-23/`, written @b168025b06) holds 1,415,137 rows.
2. **Performance** `CFN_SCTASK0548380_Historical_Performance_TWR_Cumulative_NetofFees_20260623_102759.txt`: 88,654 records, every one
   13 fields, all distinct. Header `Advisor_ID|Account_Number|ReportingPeriod|PerfType|NetGross|Annualize|StartDate|EndDate|PerfNum|
   BenchMark1Value|BenchMark1Description|Account_Status|AsOfDate`. `ReportingPeriod`: Month 80,709, Year 6,425, InceptionToDate 1,520.
   `StartDate`/`EndDate` ISO; **`AsOfDate` is `MM/DD/YYYY` (`06/23/2026`)**; `NetGross`/`Annualize` are `True`/`False`.
3. **Positions** `CFN_SCTASK0548380_Historical_Positions_20260623_102747.txt`: 469 records, 11 fields, all distinct. Header
   `Advisor_ID|AccountNumber|Cusip|FundCode|Symbol|Security_Description|Quantity|LongShort_Indicator|Position_Type|AsOfDate|
   Account_Status` (note `AccountNumber`, no underscore); `AsOfDate` ISO.
4. **The security universe** (silver transactions, read from S3): 4,634 distinct CUSIPs, none blank -- Equity 1,830, Mutual Fund 978,
   Fixed Income 778, Cash Equivalent 488, ETF 349, Mutual Fund (Closed End) 99, Unit Investment Trust 58, Annuity 29, Alternative
   Investment 22, Cash 3.
5. **Builder output** (rule 30): `address('commonwealth','cottonwood','silver',<table>,'date=2026-06-23')` for `transactions`,
   `performance`, `positions`, `coverage`. Code reads the scope via `opal_naming.lookup` (row W1-S1: the naming gate refuses a typed scope).

## THE CONTRACTS FIXED HERE (so the four cells run in parallel)

- **Lineage on every silver row of every table:** `source_zip`, `source_zip_sha256`, `source_file`, `source_line` (1-based physical
  line of the record's FIRST line; header = line 1), and NEW `source_record` (int, the 1-based record ordinal in the file, header
  excluded). `(source_file, source_record)` is unique per table. Two identical records are two rows.
- **Row count equals the file's record count**, printed beside it (C-SILVER v0.4).
- **Partitions:** transactions `trade_year=<YYYY>/` (unchanged); performance `reporting_period=<Month|Year|InceptionToDate>/`; positions
  unpartitioned (one as-of date).
- **The coverage table** (FWD-6, C-COVERAGE) reads those three tables and writes one row per record kind:
  `record_kind, source_file, earliest, latest, rows, date_column, note` -- generated from the data, never from the brief.

## The cells

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `CB-b-1` | remediation: the transactions converter keeps EVERY record (no de-duplication), adds `source_record`, refuses to write if rows != records | FWD-1, FWD-3 | NOT-EVALUATED | laptop | WORLD | A, `0.9.0_WK_ADVI_COTBKF~4` |
| `CB-b-2` | backlog 1a: performance and positions to silver (Commonwealth's own figures, as reported), every record, typed, lineage | FWD-3 | NOT-EVALUATED | laptop | WORLD | B, `0.9.0_WK_ADVI_COTBKF~5` |
| `CB-b-3` | backlog 1b: the price-coverage read (C-DAILY step 0) -- for the 4,634 CUSIPs, which existing Opal stores hold a daily close, over which days; security-days covered vs needed; no vendor call | FWD-3 | NOT-EVALUATED | laptop | LOCAL | C, `0.9.0_WK_ADVI_COTBKF~6` |
| `CB-b-4` | backlog 2: the coverage table generator (FWD-6) over the three silver tables | FWD-6 | NOT-EVALUATED | laptop | WORLD | D, `0.9.0_WK_ADVI_COTBKF~7` |

## Write sets (disjoint)

- **CB-b-1:** `data/assets/scripts/silver/commonwealth_transactions.py`, `data/assets/scripts/silver/tests/test_commonwealth_transactions.py`.
- **CB-b-2:** `data/assets/scripts/silver/commonwealth_portfolio_files.py`, `data/assets/scripts/silver/tests/test_commonwealth_portfolio_files.py`.
- **CB-b-3:** `data/assets/scripts/analysis/commonwealth_price_coverage.py`, `data/assets/scripts/analysis/tests/test_commonwealth_price_coverage.py`,
  and its result file in its own deliverables folder.
- **CB-b-4:** `data/assets/scripts/silver/commonwealth_coverage.py`, `data/assets/scripts/silver/tests/test_commonwealth_coverage.py`.
- Each: its deliverables folder and the investigation file.

**Ordering and fan-out:** `fanout: 4 of 4 chains, cap 8` -- the contracts above fix every column and key a cell consumes, so no chain
waits on another; CB-b-4 builds and proves on fixtures and runs for real after the issuer's applies.

## The issuer's acts after the drain (one change-management ledger entry)

1. CB-b-1 `--apply`: the transactions table REPLACED under its prefix (the old 14 part files overwritten by the same keys; a stale
   part file removed); read back 1,416,497 rows. Never-widen non-application: a literal key list this seat controls, no reader yet.
2. CB-b-2 `--apply`: performance (88,654) and positions (469); read back.
3. CB-b-4 on the three tables in S3, then `--apply`; read back.
4. The FWD-1 trace re-run on the rebuilt table (one repeat record traced to its own line), and the coverage table read by a seat that
   was not told it (FWD-6's DONE WHEN) is the CVO's L9 read.
