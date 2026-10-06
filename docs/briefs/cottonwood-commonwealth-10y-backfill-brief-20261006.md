# L1 BRIEF -- the Cottonwood 10-year backfill from Commonwealth, landed in `opal-data-assets` under the naming canon

- **Author:** `4.0.0_SA_CRO` (L1), 2026-10-06 ~17:0xZ (1:0x PM Eastern). **Mode:** NEW. **Priority:** Andrew's word.
- **Order:** Andrew-direct 2026-10-06 at the `4.0.0_SA_CRO` terminal, verbatim in
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_16xxZ_COTTONWOOD_COMMONWEALTH_10Y_BACKFILL_SPEC.md`:

  > I need you to analyze the structure of the download from Cottonwood, because you need to spec out a mechanism for
  > how to bring this data into opal-data-assets. There should just be an LGIC_NAMING approved process on how this
  > fits in there and how it is split out. The premise is that this is a 10Y backfill of all the Cottonwood Capital
  > Advisors client data. This came in from their old management partner, commonwealth. That's likely how it should be
  > named in the string for the upload.

  and: "Disregard MSTR instruction on using a cottonwood specific bucket. We will use the opal-data-asset format which
  is customary according to LGIC_NAMING." The relay of the same project at `0.0.0_AB_MSTR` (msg 105635) called it "a
  priority project".
- **Consumer:** `1.0.0_SA_CTO`, `/endpoint --forward` at L2.
- **Input read:** `Files.zip` in Andrew's Downloads folder, 3,218,239,946 bytes, finished downloading 2026-10-06
  12:52 Eastern (the Box download of "Cottonwood Historical Data"). Read for STRUCTURE ONLY: names, column headers,
  row counts, date ranges, distinct counts. No client name, account number, identifier or value is written here.

---

## PART I -- THE OUTCOME TERRITORY

### The candidate thread

**One Cottonwood account's 13-year transaction history, read from Opal's own store.** The Commonwealth delivery is in
`opal-data-assets` exactly as received; the transaction file is in silver as typed rows; an analyst picks one
Cottonwood account and reads every transaction from 2013 to June 2026, and can trace each row to the file it came
from. Everything else in this brief enriches that one journey.

### O1 -- Anyone can find the whole Commonwealth delivery in Opal's store, exactly as it arrived

All five files Commonwealth shipped are kept byte-for-byte, at addresses the naming canon produces, with each file's
size and checksum recorded. Nobody has to go back to Box or to Andrew's Downloads folder for any of it.

### O2 -- An analyst reads Cottonwood's transaction history back to 2013

1.42 million transactions across 1,533 accounts, trade dates 2013-04-03 to 2026-06-22, typed and queryable, every
vendor column and row kept.

### O3 -- An analyst reads each Cottonwood account's monthly and annual net-of-fee returns back to 2013

88,654 performance rows (monthly, yearly and since-inception time-weighted returns, net of fees, with a benchmark
column), 2013-04 to 2026-06. This is the history the Black Diamond conversion was late to deliver (base brief
precedent: Cottonwood historical performance, 2026-10-01).

### O4 -- An analyst reads Cottonwood's client relationship records as Commonwealth held them

Households, contacts, relationships between people, advisor users, insurance policies, and 109,883 logged
activities (2016-04 to 2026-06), typed and queryable.

### O5 -- An analyst finds any client document (statement, tax form, client file) by account, type and date

About 24,500 PDF document entries across three advisor plan archives, each with its index row. A person searches the
index and opens the one document they need, without unzipping a 1.5 GB archive by hand.

### O6 -- A person can see what this backfill covers and what it does not

The coverage is uneven (Part IV, F5): transactions and returns span 13 years; statements only 12 months; positions
only one day. The person reading Cottonwood's history can tell which kind of record goes back how far.

### O7 -- Cottonwood's most sensitive personal data is held only where Andrew decided it may be

The contacts file carries tax IDs, dates of birth, driver's license and passport numbers (Part IV, F6). Wherever those
fields land, they land by Andrew's decision, and a reader can say who can see them.

### O8 -- An analyst can line up a Commonwealth account with the same client's account at its current custodian

Cottonwood moved from Commonwealth to its current platform. A person can tell which old account is which current
account, or can see that the match is not yet known.

---

## PART II -- WHERE THE BOUNDARY SITS

**This project owns:** the landing of this one delivery (bronze), its typed silver tables, the document index, the
registry row for Commonwealth as a source, the coverage statement, and the account crosswalk's first version.

**It relies on, and does not own:**
- **The naming canon and its builders** (`infra/logic/02_DOCTRINE.md`, `lib/opal_naming.py`, `infra/logic/registry/`;
  D14 / LGIC). A new source is a registry row added through its owner, not a hand-typed path.
- **The existing Cottonwood pipelines** (Black Diamond under `opal-data-assets/blackdiamond/cottonwood/`; the
  Cottonwood gold and platinum in `opal-data-cottonwood`). This backfill does not change them.
- **Gold and anything served to a page** (R5, R6): out of scope for this brief. Which product reads the history
  (Investor Reporting performance, Advisor Intelligence, the Cottonwood portal) is a later decision.
- **The classification table** (MDPF_SECCLASS): securities in these transactions are classified there, later.

**It does not own:** any further pull from Commonwealth or Box, and no client-facing release.

---

## PART III -- THE QUALITATIVE BAR

1. Asked "what did Commonwealth send us?", a person answers from Opal's store, file by file, without Box.
2. An analyst reconstructs a Cottonwood account's history from 2013 without asking anyone for a spreadsheet.
3. No one finds a Cottonwood tax ID or passport number somewhere Andrew did not put it.
4. Nobody mistakes "13 years of transactions" for "13 years of statements".
5. A later delivery from Commonwealth, if one comes, lands next to this one without renaming anything.

---

## PART IV -- THE SUBSTRATE: what the delivery holds, measured

### F1. The package: five vendor zips inside one Box zip

| Inner file (as shipped) | Bytes (uncompressed) | What it is |
|---|---|---|
| `CRM_CottonwoodCapitalAdvisors.zip` | 26,485,027 | 7 pipe-delimited text files: the CRM export |
| `Cottonwood Capital Advisors_Portfolio_Accounting_Performance_ClientDelivery.zip` | 23,833,956 | 3 pipe-delimited text files, prefixed `CFN_SCTASK...` (CFN = Commonwealth Financial Network), stamped 2026-06-23 |
| `HKE.zip` | 1,554,270,895 | imaging archive for one advisor plan ID: 11,051 files |
| `HJH.zip` | 1,503,993,172 | imaging archive for a second plan ID: 11,018 files |
| `4XF.zip` | 113,362,389 | imaging archive for a third plan ID: 2,474 files |

### F2. The portfolio-accounting files (the 10-year history)

| File | Rows | Columns | Dates | Distinct |
|---|---|---|---|---|
| Historical Transactions | 1,416,497 | 20 | trade date 2013-04-03 to 2026-06-22 | 1,533 accounts; 61 transaction types (dividend, reinvest, buy, sell, interest, journal and others) |
| Historical Performance (TWR, cumulative, net of fees) | 88,654 | 13 | 2013-04 to 2026-06 | 1,519 accounts; Month 80,709, Year 6,425, Inception-to-date 1,520 rows |
| Historical Positions | 469 | 11 | ONE as-of date, 2026-06-23 | 83 accounts |

Rows per trade year rise from about 36,000 (2013, a partial year) to about 160,000 (2023 to 2025). Each file carries
an `Advisor_ID` (a Commonwealth rep code; four appear) and an account number. Columns are named (transactions):
Advisor_ID, Account_Number, Transaction_Type, Transaction_Description, Cusip, FundCode, Symbol, Quantity, Amount, AI,
Trade_Date, Cost_Date, Settle_Date, Asset_Type, CA_Event_Id, LongShort_Indicator, Position_Type, Security_Description,
Transaction_Note, AsOfDate.

### F3. The CRM export

| File | Rows | Columns | Dates |
|---|---|---|---|
| Households (CRM) | 270 | 95 | client start 2013-03 to 2023-05 |
| Households (C360) | 270 | 4 | -- |
| Contacts | 676 | 156 | -- (personal dates, see F6) |
| Connections | 46 | 12 | -- |
| Users | 7 | 5 | -- |
| Activities | 109,883 | 20 | updated 2016-04 to 2026-06 |
| Manual insurance | 105 | 152 | policy dates 2004 to 2053 |

### F4. The imaging archives

- Each archive is one advisor plan ID, with a vendor `ReadMe.txt` describing its folders: ADVS advisor documents, CLNT
  client documents, NCSD non-Commonwealth scanned documents, QSMT quarterly statements (empty), REPR advisor reports,
  STMT monthly statements, TXRP tax documents.
- Inside each type folder, one sub-folder per rep code with a `Listing.csv`: the index from each PDF file name to its
  account, statement date, year, document name and page count. 51 listings; 7 distinct index layouts (one per type).
- **Heavy duplication across archives:** 10,917 of the PDF paths in `HKE.zip` are also in `HJH.zip`, and 2,453 of
  `4XF.zip`'s are in both. The rep codes overlap too (one shared rep code appears in all three). The three archives are
  three advisor views of largely the same documents.
- PDF counts: statements about 7,700 per large archive; tax 1,034; client documents about 930; scanned 1,239.

### F5. Coverage: what "10 years" is true of

| Record kind | Span measured |
|---|---|
| Transactions | 13 years (2013-04 to 2026-06-22) |
| Performance | 13 years (2013-04 to 2026-06) |
| CRM activities | 10 years (2016-04 to 2026-06) |
| Positions | one day (2026-06-23) |
| Monthly statement PDFs | 12 months (statement dates 2025-06-30 to 2026-05-31) |
| Tax document PDFs | 2 tax years (2024, 2025) |

The delivery stops at 2026-06-23. What happened to these accounts after that is in Opal's current Cottonwood feeds,
not here.

### F6. The most sensitive fields in the estate are in this delivery

The contacts file has columns for TaxID, DateOfBirth, DriversLicenseNumber, PassportID and full addresses and phone
numbers; the insurance file names owners, insureds and beneficiaries. The canon's silver rule keeps every vendor
column (R10). Those two facts meet here and need Andrew's word (Part V).

### F7. Where it lands under the canon (measured against the builders)

- **Bucket:** client custodial bronze and silver have ONE home, `opal-data-assets` (doctrine R4). The builder agrees:
  `address('blackdiamond','cottonwood','bronze','holdings','date=2026-10-02')` returns
  `s3://opal-data-assets/blackdiamond/cottonwood/bronze/holdings/date=2026-10-02`.
- **Key grammar:** `{source}/{scope}/{tier}/{table}/{partition}` (N1), source first.
- **Source:** `commonwealth` is NOT a registered source today. The builder refuses it:
  `address('commonwealth','cottonwood',...)` raises `source 'commonwealth' is not a systems.json key`. A refusal is a
  missing registry row to add (CLAUDE.md rule 30): one VENDOR row, display name "Commonwealth Financial Network".
- **Scope:** `cottonwood` (a registered FIRM). The advisor plan IDs and rep codes are entity identifiers and may not sit
  in the scope segment (R2); they belong in the partition.
- **Bronze format:** raw and untouched, zips stay zips (R9).
- **Silver format:** typed, deduplicated parquet, every vendor column and row, hive partitions (R10).
- **The shape this implies (for the CTO to settle with builder output, not typed here as final):**

  ```
  opal-data-assets/commonwealth/cottonwood/
    bronze/crm/date=<delivery date>/CRM_CottonwoodCapitalAdvisors.zip
    bronze/portfolio_accounting/date=<delivery date>/<the ClientDelivery zip, name as shipped>
    bronze/imaging/date=<delivery date>/plan_id=HKE/HKE.zip      (likewise HJH, 4XF)
    silver/transactions/...   silver/performance/...   silver/positions/...
    silver/crm_households/... silver/crm_contacts/...  (one table per CRM file)
    silver/document_index/... (the 51 listings, de-duplicated across the three archives)
  ```

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- **A registry row for Commonwealth** through the naming registry's owner, before any address is produced.
- **Andrew's word on the sensitive fields (O7):** whether tax IDs, license and passport numbers and dates of birth
  enter silver as-is (R10's every-column rule), or are held in bronze only, or masked. This is his call, not a
  build default.
- **Which delivery date partitions bronze:** the vendor's stamp (2026-06-23) or the day Opal received it
  (2026-10-06).
- **Where individual PDFs live** once indexed, since bronze keeps zips whole (R9) and silver is parquet (R10): a
  declared place for the extracted documents, or retrieval from the zip on demand.
- **The cross-firm guard** (`.tools/ds-precommit-check.py`): the new tree is Cottonwood's only.
- **No shadow path:** this is a one-time backfill landing beside, never duplicating, the current Cottonwood feeds.
- **Access:** Andrew's Downloads copy is not a store; once landed, the local copy's fate is his.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-06 ~16:5xZ to ~17:0xZ on the laptop. Nothing is uploaded. The file sits only in Andrew's Downloads.
`opal-data-assets` today holds `blackdiamond/`, `schwab/`, `orion/`, `eclipse/`, `pathfinder/`, `smartx/`,
`trueshares/` and older prefixes; no `commonwealth/` prefix exists.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- No PDF was opened; document contents are unread.
- The meaning of `Account_Status` (0 or 1) and of the 61 transaction codes was not looked up.
- Whether the 1,533 accounts are all Cottonwood clients, or include accounts that left before the move, is unmeasured.
- How Commonwealth account numbers map to the current custodian's (O8) is unmeasured.
- The "10-year" premise holds for transactions, returns and activities; it does not hold for statements and positions
  (F5). That is a finding, not a defect of the delivery.
- No cost was estimated for storage (about 3.2 GB raw) or for the silver build.

---

## REFS

```
  BRIEF PATH        docs/briefs/cottonwood-commonwealth-10y-backfill-brief-20261006.md
  PROJECT           NONE-YET (CTO registers at L3)
  EXISTING PRD      NONE
  ANDREW'S WORDS    org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_16xxZ_COTTONWOOD_COMMONWEALTH_10Y_BACKFILL_SPEC.md
                    org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261006_16xxZ_COTTONWOOD_LGIC_NAMING_VOLUME_IN_OPAL_DATA_COTTONWOOD_PRIORITY_CRO_SPEC.md (bucket superseded)
  INPUT             Files.zip, Andrew's Downloads, 3,218,239,946 bytes (not in the repo; client data)
  CANON             infra/logic/02_DOCTRINE.md R1-R4, R9, R10, N1-N2; lib/opal_naming.py address(); infra/logic/registry/systems.json
  SIBLING PROJECTS  the Black Diamond Cottonwood pipeline; the Cottonwood firm bucket's gold and platinum; MDPF_SECCLASS
  OPEN FOR ANDREW   the sensitive-field decision (O7, Part V)
  MEASURED AT       2026-10-06 ~16:5xZ to ~17:0xZ
```
