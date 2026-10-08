# RESEARCH -- are the ADVI_COTBKF "Commonwealth" files Fidelity fact tables? (vs the Schwab fact tables)

**archetype:** EXPLORE
**Author:** 4.0.0_SA_CRO~DELL2, 2026-10-08
**Ask:** 1.0.0_SA_CTO~DELL2 msg 1392; Andrew-direct ~18:3xZ items 5 and 10, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_183xZ_DELL2_OVERVIEW_FOLLOWUPS_CRO_FIDELITY_COMPARE_IRPT_FRONTEND_MAPPING.md` @34c9adbbec.

## Answer

**No. These are not Fidelity fact tables, and the files themselves show it.** They are a one-time history export from
Commonwealth Financial Network's own portfolio-accounting system. The "Fidelity shape" is in the identifiers inside the
rows (account-number formats, Fidelity money-market sweep funds), not in the file design. Most of the accounts were
probably custodied at Fidelity, through Commonwealth's clearing relationship with Fidelity's National Financial
Services. But the files also carry assets no Fidelity custodian file would hold. Fidelity's own feeds would be separate
custodian record files, comparable to Schwab's CRS files; none of those was delivered.

## What was read (measured, 2026-10-08)

Source: `s3://opal-data-assets/commonwealth/cottonwood/bronze/portfolio_accounting/date=2026-06-23/Cottonwood Capital Advisors_Portfolio_Accounting_Performance_ClientDelivery.zip`.
It holds three pipe-delimited files under folder `CFN_SCTASK0548380_Portfolio_Accounting_Performance/`. CFN =
Commonwealth Financial Network; SCTASK = a ServiceNow request number, so this was a requested extract.

| file | bytes | rows | columns |
|---|---|---|---|
| Historical_Positions | 48,610 | 469 (83 accounts, one date 2026-06-23) | Advisor_ID, AccountNumber, Cusip, FundCode, Symbol, Security_Description, Quantity, LongShort_Indicator, Position_Type, AsOfDate, Account_Status |
| Historical_Transactions | 308,186,603 | 1,416,494 parsed (1,533 accounts, trade dates 2013-04-03 to 2026-06-22) | Advisor_ID, Account_Number, Transaction_Type, Transaction_Description, Cusip, FundCode, Symbol, Quantity, Amount, AI, Trade_Date, Cost_Date, Settle_Date, Asset_Type, CA_Event_Id, LongShort_Indicator, Position_Type, Security_Description, Transaction_Note, AsOfDate |
| Historical_Performance_TWR_Cumulative_NetofFees | 8,513,299 | not counted | Advisor_ID, Account_Number, ReportingPeriod, PerfType, NetGross, Annualize, StartDate, EndDate, PerfNum, BenchMark1Value, BenchMark1Description, Account_Status, AsOfDate |

Schwab comparison: `s3://opal-data-assets/schwab/08242234/` (bronze `trn/20261007/08242234.CRS20261007.TRN.zip`;
silver `fact_acc`, `fact_rps`, `fact_trn`, `fact_sec`, one partition each read for schema).

## Compare and contrast

| axis | Schwab fact tables | Commonwealth files | what it shows |
|---|---|---|---|
| producer | the custodian (Schwab CRS daily files, `custdian_id='SCHWAB'`) | the former broker-dealer's accounting system (CFN request extract) | not a custodian feed |
| cadence | daily file per record type; silver partitioned by `business_date` | ONE extract, `AsOfDate` 2026-06-23 on every row | a history dump, not a feed |
| record types | ~20 file types: ACC accounts, RPS positions, TRN transactions, SEC security master, ULN/ULT/UPN/UPT lots, RLD/RLU/RLW/RLY realized, TCF, ... | 3: positions (one date), transactions, computed performance | no account master, security master, lots or realized gains |
| width | `fact_trn` 140+ columns: fees split out, withholding, wire/check, order ids, broker | 20 columns | summarized |
| transaction codes | Schwab `tr_cd`/`sb_cd` + source descriptions ("ORD DIV - CASH", "AUTO BANK SWEEP") | portfolio-accounting codes: `by sl dv dvr int li lo dvlt dvst man ci lica licar trfi trfo ftax` (61 distinct) | `li`/`lo`/`dvr`/`man` are the vocabulary of an accounting book (Advent-style), not a custodian's activity codes |
| performance | none (custodians do not compute TWR) | monthly TWR net of fees with a benchmark | the accounting/reporting system's own output |
| account keys | Schwab 8-10 digit numbers under a master account | mixed, see below | one book over several custodians |
| fields kept out | full PII in `fact_acc` (SSN, DOB, address) | none in these three files (they sit in the separate CRM zip) | -- |

**Account-number shapes in the transactions file** (top 8 of 1,533 accounts; 93 in the tail):
`A9A999999` 504, `9AA999999` 217, `AAA999999` 203 (together 924: the 3-character-prefix, 6-digit form that Fidelity/NFS
brokerage accounts use -- inferred, by format); `cv`-prefixed forms 355 (a Commonwealth-internal prefix, meaning
unknown -- inferred); 11-digit numbers 120 (fund-company "direct" accounts, which carry a `FundCode` -- inferred); `A99999999` 41.

**Assets in the file that a Fidelity custodian file would not hold:** annuities (12,481 transaction rows), direct-held
mutual-fund accounts (11-digit numbers with fund-company codes), and limited partnerships held away (for example a
"Partners Fund II LP" position). A custodian reports only what it holds. A history covering all of these is the
broker-dealer's consolidated book.

**The Fidelity evidence** (consistent with Fidelity clearing; it does not make the files Fidelity's): the 9-character
account format; Fidelity government money funds trading as the core sweep across 232 accounts (`316067107` Fidelity
Government Cash Reserves; the round-20 decomposition and the round-19 drain-end record measured this); a "Bank Deposit
Sweep Program" position.

## What can and cannot be inferred from what is provided

- CAN: the files are Commonwealth's accounting-system extract; most brokerage accounts follow Fidelity/NFS numbering
  conventions; the cash sweep runs through Fidelity funds.
- CANNOT, from these bytes alone: the custodian of each account. No column names a custodian, so the split by account
  shape is a format inference, not a field. Commonwealth clearing through Fidelity's NFS is outside knowledge (held),
  not something the files state.
- To make it measured: ask Commonwealth (or Cottonwood) for the custodian per account, or match the 924 Fidelity-shaped
  numbers against Cottonwood's current Fidelity or Schwab account lists if the accounts moved.

## Consequence for ADVI_COTBKF (recorded, not adjudicated)

These files should not be mapped onto Schwab's `fact_*` tables as if they were a custodian's record types. Their silver
grain is closer to Black Diamond's or an accounting book's (accounts, transactions, performance) than to a custodian's.
The pipeline already treats them as a source of their own (`commonwealth/cottonwood/`, registry row `commonwealth`), so
this answer changes no home.

Working files: session scratchpad only; no client data is committed here (account shapes and counts only).
