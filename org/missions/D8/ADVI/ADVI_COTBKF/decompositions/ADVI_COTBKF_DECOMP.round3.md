# ADVI_COTBKF decomposition -- ROUND 3 (issuer 2.0.0_SA_COO~C under /canonical-drive; drafted 2026-10-07 ~00:3xZ)

**Status: DRAFT -> ISSUED in one issuance** (the issuance commit carries the `fanout:` line).

**Cut on:** the CTO's round-2 analysis (msg 105855, 2026-10-07 00:16Z): "C-DAILY never reads bd or inf. Opal-wide history is
MDPF_SECHIST's job ... it waits on dell1. Next cut, one measurement cell: per security, trading days held (first to last appearance),
split equity/ETF/fund vs fixed income, total rows. That number decides the vendor ask to Andrew ... Meanwhile run the rest of the backlog:
CRM after its policy, documents, crosswalk, FWD-9." PRD v0.4 @51a7c07278 (ADMITTED). Round-2 close @1055c50f3e.

**Rule 24.** Domain: the measurement cell plus the backlog items cuttable now. Item 4 (documents) splits into the archives' landing (an
ISSUER act with the round-1 landing tool, no cell) and the document INDEX (a cell); unpacking unique documents waits on the index (round
4). Item 5 is the crosswalk (FWD-8). FWD-9 is its own cell. Excluded, with the reason: the CRM (item 3) -- C-RESTRICTED's bucket policy
(manifest S09, an AE's Terraform act) is not live, and no byte of the CRM zip moves before it. Four cells, one intent each, disjoint writes.

## Measured constraints (read at the base, 2026-10-07 ~00:2xZ)

1. **Silver** (S3, `opal-data-assets/commonwealth/cottonwood/silver/`, read back @1055c50f3e): transactions 1,416,497 rows / 25 columns /
   1,533 accounts (`Account_Number`, `Cusip`, `Symbol`, `Asset_Type`, `Trade_Date`, `Transaction_Type`, `Transaction_Description`,
   `Quantity`, `Amount`); performance 88,654; positions 469 (`AccountNumber`); coverage 5 kinds. 4,634 distinct CUSIPs.
2. **The 2016 break (row S2):** the 311 accounts trading in 2013 all end by 2017-12-29; the longest single-account history starts
   2016-01. `li` "Contribution to Asset" rows: 2015 1,736 -> 2016 14,216 -> 2017 2,939; `trfi`/`trfo` "Position Transfer In/Out" first
   appear in 2016 (534 / 318). Old account numbers are 11 digits (`acct#c9405219`); the long 2016+ ones alphanumeric (`acct#0e4ff3a3`).
3. **The imaging archives** (in `%USERPROFILE%\Downloads\Files.zip`, not yet in bronze): `HKE.zip` 11,075 members (11,033 PDF, 17
   `Listing.csv`), `HJH.zip` 11,042 (11,000 PDF, 17 listings), `4XF.zip` 2,498 (2,456 PDF, 17 listings): 51 listings. Top folders ADVS,
   CLNT, NCSD, QSMT, REPR, STMT, TXRP. Listing layouts differ by type: REPR `ReportID, ReportSectionID, ReportVersionID, FileName, DocType,
   DocName, NumberOfPages`; STMT `ReportID, ReportSectionID, ReportVersionID, FileName, Acct, DisplayName, StmtDate` (values carry a
   leading space; `ReportVersionID` a leading apostrophe). The first STMT listing read holds 5 rows against 7,724 STMT PDFs in that archive:
   the listings may not index every PDF -- the cell accounts for every PDF either way. Statement accounts read like `acct#7b5bf6ff` (NFS).
4. **Current Cottonwood accounts** (`s3://opal-data-cot/gold/dimensions/accounts_dimension_latest.parquet`, Cottonwood's own bucket, same
   firm): 994 rows; `account_id` like `acct#c6ac42e6`, `relationship_id`, `account_open_date` and `first_transaction_date` mostly 2026-05/06,
   `account_registration_type`, `account_type`; names mostly null. The holdings history is `s3://opal-data-cot/gold/canonical/holdings/<date>.parquet`.
5. **Cross-firm law:** this project reads only `opal-data-assets/commonwealth/cottonwood/` and `opal-data-cot`; never `opal-data-bd` or
   `opal-data-inf` (CTO ruling on W6-S2).

## The cells

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `CB-c-1` | the price-need measurement: per security, trading days from first to last appearance in the transactions; split equity / ETF / fund / fixed income / other; the total security-days | FWD-3 (sizes the vendor ask) | NOT-EVALUATED | laptop | LOCAL | A, `0.9.0_WK_ADVI_COTBKF~8` |
| `CB-c-2` | the document index: the 51 listings of the three archives as one index, every PDF accounted for, a document in several archives listed once | FWD-5 | NOT-EVALUATED | laptop | WORLD | B, `0.9.0_WK_ADVI_COTBKF~9` |
| `CB-c-3` | the crosswalk (FWD-8): each Commonwealth account to its current Cottonwood account by stated rules, or listed unmatched with the reason | FWD-8 | NOT-EVALUATED | laptop | WORLD | C, `0.9.0_WK_ADVI_COTBKF~10` |
| `CB-c-4` | FWD-9: each pre-2018 Commonwealth account linked to the account that replaced it inside Commonwealth, by matched in-kind moves, or listed unlinked with the reason | FWD-9 | NOT-EVALUATED | laptop | WORLD | D, `0.9.0_WK_ADVI_COTBKF~11` |

## Write sets (disjoint)

- **CB-c-1:** `data/assets/scripts/analysis/commonwealth_price_need.py`, `data/assets/scripts/analysis/tests/test_commonwealth_price_need.py`; results in its deliverables folder.
- **CB-c-2:** `data/assets/scripts/silver/commonwealth_document_index.py`, `data/assets/scripts/silver/tests/test_commonwealth_document_index.py`.
- **CB-c-3:** `data/assets/scripts/silver/commonwealth_crosswalk.py`, `data/assets/scripts/silver/tests/test_commonwealth_crosswalk.py`.
- **CB-c-4:** `data/assets/scripts/silver/commonwealth_account_links.py`, `data/assets/scripts/silver/tests/test_commonwealth_account_links.py`.
- Each: its deliverables folder and the investigation file.

**Ordering and fan-out:** `fanout: 4 of 4 chains, cap 8` -- no cell consumes another's output this round.

## The issuer's acts (one change-management ledger entry)

1. Land the three imaging zips to bronze with the round-1 tool (`commonwealth_landing.py --member HKE.zip|HJH.zip|4XF.zip --table imaging`;
   the manifest gains each file), read back size and SHA-256 -- FWD-2 then holds 4 of 5 delivered files; the CRM zip waits on C-RESTRICTED.
2. After the drain: CB-c-2, CB-c-3, CB-c-4 `--apply` (silver `document_index`, `crosswalk`, `account_links`), each read back.
3. CB-c-1's number goes to `1.0.0_SA_CTO` for the vendor ask to Andrew.
