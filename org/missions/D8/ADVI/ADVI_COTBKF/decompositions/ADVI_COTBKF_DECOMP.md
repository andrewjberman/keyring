# ADVI_COTBKF decomposition -- ROUND 1, the THREAD (issuer 2.0.0_SA_COO~C; drafted 2026-10-06 ~18:1xZ)

**Status: DRAFT -> ISSUED in one issuance** (the issuance commit carries the `fanout:` line).

**Cut on:**
- PRD `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` v0.3 @5567e751f1, ADMITTED (`python .tools/prd-signoff.py status
  ADVI_COTBKF`: ratified-text SIGNED by `3.0.0_SA_CVO` @7d6b709c2f, brief half accepted, the CRO wrote the brief).
- Receiving check: `python .tools/receiving-check.py <PRD>` -> ACCEPT (`prd-manifest`: manifest, ENDPOINT, header, outcome cards).
- Seating: `1.0.0_SA_CTO` msg 105663 to `0.0.0_AB_MSTR` ("point ~C at ADVI_COTBKF L5"), relayed to this lane as msg 105664.

**Round 1 is the PRD's section 2 THREAD (FWD-1)**, decomposed over its four hops:
1. the `commonwealth` registry row (LANDED @8e39143feb) and the builder output for every key this round writes;
2. the portfolio-accounting zip from the delivery to bronze, byte for byte, with its manifest (C-RAW, C-DATE);
3. the transactions file to the silver transactions table (C-SILVER), every row carrying its file of origin;
4. an analyst names one account, reads its history oldest to newest from Opal's store, and traces one row back to the delivered file.

**Rule 24.** Domain: the four hops of the thread, nothing else (the CRM zip, the imaging archives, performance and positions silver,
C-DAILY, coverage and the crosswalk are the ENRICHMENT BACKLOG, later rounds). Hop 1 is measured below and needs no cell. Hops 2,
3 and 4 are one cell each: one intent each (land / type / read), one write set each, no remainder. The S3 WRITES are not worker
cells: they are the issuer's acts after the drain, under one change-management ledger entry (PRD section 4).

## Measured constraints (read at the base, 2026-10-06 ~18:0xZ)

1. **The input.** `%USERPROFILE%\Downloads\Files.zip` (the Box download, 3,218,239,946 bytes), Andrew's only copy (PRD section 4).
   It holds five zips (brief F1). The portfolio-accounting one is
   `Cottonwood Capital Advisors_Portfolio_Accounting_Performance_ClientDelivery.zip`: 23,833,956 bytes, SHA-256
   `a3a2772efa3447fd3adaa4b6eb5dacdf400667743c4f4040e2d0cad3296d658b`. It holds THREE text files under
   `CFN_SCTASK0548380_Portfolio_Accounting_Performance/`: `..._Historical_Transactions_20260623_102751.txt` (308,186,603 bytes),
   `..._Historical_Performance_TWR_Cumulative_NetofFees_20260623_102759.txt` (8,513,299), `..._Historical_Positions_20260623_102747.txt`
   (48,610).
2. **The PRD's thread says "the transactions zip and the performance zip"; the delivery has ONE zip carrying both** (plus positions).
   Round 1 lands that one zip. Row `ADVI_COTBKF-S1`.
3. **The transactions file.** Pipe-delimited, one header line, 20 columns as the brief lists (F2). 1,416,501 physical lines: header +
   1,416,500, against the brief's 1,416,497 rows. The 3-line difference is unexplained and is the worker's to account for (blank
   lines, a trailer, or embedded line breaks), never to drop silently. `Account_Number` carries leading zeros (`acct#c9405219`): a string.
4. **Builder output (rule 30, C-SOURCE)**, `lib/opal_naming.address('commonwealth','cottonwood',<tier>,<table>,'date=2026-06-23')`:
   - bronze zip: `s3://opal-data-assets/commonwealth/cottonwood/bronze/portfolio_accounting/date=2026-06-23`
   - bronze manifest: `s3://opal-data-assets/commonwealth/cottonwood/bronze/manifest/date=2026-06-23`
   - silver transactions: `s3://opal-data-assets/commonwealth/cottonwood/silver/transactions/date=2026-06-23`
   Code never types these: it calls `address()`.
5. **Code home.** `data/assets/scripts/` is the home of custodial sources landing in `opal-data-assets` (the Schwab precedent,
   `data/assets/scripts/silver/schwab_conversion.py`). Rule 13: these are DS-lane scripts; a one-time backfill runs them by hand, so
   there is no scheduled producer and no `safe-deploy` upload (C-ONE-TIME: no pipeline beside the current Cottonwood feeds).

## THE LINEAGE CONTRACT (fixed here so the three cells run in parallel)

Every silver transactions row carries four columns after the 20 vendor columns:
`source_zip` (the zip's name as shipped), `source_zip_sha256` (lowercase hex), `source_file` (the member path inside the zip, as
shipped), `source_line` (int, the 1-based PHYSICAL line number of the row in that member file; the header is line 1).
The manifest is one JSON object: `{"delivery": "commonwealth/cottonwood", "data_date": "2026-06-23", "received_date": "2026-10-06",
"files": [{"name_as_shipped", "bytes", "sha256", "bronze_key", "members": [{"path", "bytes"}]}], "builder": {"zip_prefix",
"manifest_prefix"}}`, written as `manifest.json` under the manifest prefix.

## The cells

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `CB-a-1` | hop 2: the bronze landing tool -- extracts one inner zip from the Box download untouched, computes bytes and SHA-256, builds the manifest, plans the keys from `address()`, dry run by default; `--apply` puts with a SHA-256 checksum, refuses to overwrite a different object, and reads back size and checksum | FWD-1 (FWD-2's first file) | NOT-EVALUATED | laptop | WORLD | A, `0.9.0_WK_ADVI_COTBKF~1` |
| `CB-a-2` | hop 3: the silver transactions converter -- reads the zip, types the 20 vendor columns, keeps every row and column, de-duplicates exact repeats (counted), adds the lineage columns, writes parquet under the `address()` prefix (local by default; `--apply` to S3) | FWD-1 | NOT-EVALUATED | laptop | WORLD | B, `0.9.0_WK_ADVI_COTBKF~2` |
| `CB-a-3` | hop 4: the analyst read -- names one account, prints its transactions oldest to newest from the silver table, and traces a chosen row: its lineage, the member line re-read from the bronze zip and compared byte for byte, the zip's SHA-256 against the manifest | FWD-1 | NOT-EVALUATED | laptop | LOCAL | C, `0.9.0_WK_ADVI_COTBKF~3` |

## Write sets (disjoint)

- **CB-a-1:** `data/assets/scripts/bronze/commonwealth_landing.py`, `data/assets/scripts/bronze/tests/test_commonwealth_landing.py`.
- **CB-a-2:** `data/assets/scripts/silver/commonwealth_transactions.py`, `data/assets/scripts/silver/tests/test_commonwealth_transactions.py`.
- **CB-a-3:** `data/assets/scripts/analysis/commonwealth_account_history.py`, `data/assets/scripts/analysis/tests/test_commonwealth_account_history.py`.
- Each: its own deliverables folder and the investigation file.

**Ordering and fan-out:** `fanout: 3 of 3 chains, cap 8` -- A, B and C are independent once the lineage contract above is fixed; each
builds and tests against its own fixture and the real file read locally. No chain waits on another.

## The issuer's acts after the drain (L7 close; the COO's one real run of FWD-1)

1. Open the ledger entry `org/critical_paths/change_management/` (a write into a NEW prefix: the act's write set is the literal key list
   below, which the issuer controls, so the never-widen pair does not apply -- CLAUDE.md section 5 non-application).
2. `CB-a-1 --apply`: the zip and `manifest.json`; read back.
3. `CB-a-2 --apply`: the silver transactions; read back (row count, columns, one partition listed).
4. `CB-a-3` against S3: one real account, oldest to newest, one row traced to the delivered file. That run is FWD-1's EXERCISED read.
5. Close the ledger entry with the measured keys and counts.
