# Brief 2 — Cottonwood Capital Advisors (COT): `CW_Transactions_Rich` Field-Population Analysis

**Author:** 0.4.0_DS_ClientPlatform
**Date:** 2026-06-08
**Project (proposed):** ADVI_CCAETL
**Source artifact:** `C:\Users\AndrewBerman\Downloads\CW_Transactions_Rich (1).xlsx`
**Companion:** Brief 1 (HAR auth/API) — this export is the output of the DataMining `queryTypeId=2` (Transactions) template documented there.

---

## 0. Dataset shape

| Property | Value |
|---|---|
| Data rows | **18,929 transactions** |
| Columns | **63** (across 6 DataMining join levels: Transactions, Relationship, Portfolio, Account, Holding/Asset) |
| Window | **12/06/2025 → 06/05/2026** (`dateRangeType: Last6Months`) |
| Sheets | `Sheet1` (data) + `Timestamps` (export metadata: template name, window, refresh time) |
| Export refresh time (Eastern) | 5/1/2026 6:37:55 PM (data-as-of); file created 6/8/2026 12:38 PM |

The `Timestamps` sheet is a useful provenance footer — bronze should capture `Refresh (Eastern)` as the data-as-of watermark (it can lag the file-creation time).

---

## 1. Population classification (all 63 fields)

Legend: **RICH** ≥90% populated · **PARTIAL** 10–90% · **SPARSE** <10% · **EMPTY** 0%. `distinct` capped at 60 (`+` = ≥60).

| # | Column | mappedColumn | pop % | distinct | class | Notes |
|---|---|---|---|---|---|---|
| 0 | TransactionID | transactionID | 100% | 60+ | RICH | Primary key |
| 1 | Return Date | returnDate | 100% | 28 | RICH | The transaction's effective/return date |
| 2 | Action | action | 100% | 41 | RICH | Fine-grained txn taxonomy (41 values) |
| 3 | Transaction Type | transactionType | 100% | 12 | RICH | Coarse txn taxonomy (12 values) |
| 4 | Transaction Sub Type | transactionSubType | 100% | 17 | RICH | |
| 5 | External Flow | externalFLow | 100% | 3 | RICH | **NNA driver:** Contribution / None / Withdrawal |
| 6 | Backdated Date | backdatedDate | 100% | 13 | RICH | Mostly "Not Available" sentinel |
| 7 | User Notes | userNotes | 0% | 0 | **EMPTY** | Not used by COT |
| 8 | Internal Notes | bdNotes | 2% | 7 | SPARSE | Onboarding annotations only |
| 9 | Entry Date | entryDate | 2% | 13 | SPARSE | Populated for 336 rows only |
| 10 | Settle Date | settleDate | 100% | 31 | RICH | |
| 11 | Description | description | 100% | 60+ | RICH | Free-text |
| 12 | Price | price | 100% | 60+ | RICH | money |
| 13 | Trade Date | transactionTradeDate | 100% | 30 | RICH | |
| 14 | Has Contra Account | hasContraAccount | 100% | 2 | RICH | true/false |
| 15 | Contra Account Number | contraAccountNumber | 0.1% | 20 | SPARSE | 22 rows (transfers w/ contra) |
| 16 | Contra Account Name | contraAccountName | 0.1% | 20 | SPARSE | 22 rows |
| 17 | Relationship ID | relationshipExternalId | 100% | 60+ | RICH | **Client/household key** |
| 18 | Relationship Name | relationshipName | 100% | 60+ | RICH | |
| 19 | Relationship Display Name | relationshipDisplayName | 100% | 60+ | RICH | |
| 20 | Relationship Inception Date | relationshipInceptionDate | 0% | 0 | **EMPTY** | Not emitted at txn level |
| 21 | Relationship Termination Date | relationshipTerminationDate | 0% | 0 | **EMPTY** | |
| 22 | Portfolio Strategy ID | portfolioRebalStrategyID | 0% | 0 | **EMPTY** | COT does not use BD rebalancer strategies |
| 23 | Portfolio Strategy Name | portfolioRebalStrategyName | 100% | 1 | RICH* | Single value "No Strategy" — *semantically empty* |
| 24 | PortfolioID | portfolioExternalID | 100% | 60+ | RICH | |
| 25 | Portfolio Name | portfolioName | 100% | 60+ | RICH | |
| 26 | Account Number | accountNumber | 100% | 60+ | RICH | **Account key** |
| 27 | AccountID | accountExternalID | 100% | 60+ | RICH | BD internal account id |
| 28 | Original Account Number | longNumber | 100% | 60+ | RICH | |
| 29 | Account Display Number | accountDisplayNumber | 100% | 20 | RICH* | Mostly "No Display Number" sentinel |
| 30 | Account Name | accountName | 100% | 60+ | RICH | |
| 31 | Account Display Name | accountDisplayName | 99% | 60+ | RICH | |
| 32 | DST Rep Name | repName | 1% | 1 | SPARSE | 226 rows, all "No RepName Assigned" — semantically EMPTY |
| 33 | Custodian | custodian | 100% | 11 | RICH | **98.8% Fidelity IWS** + held-away |
| 34 | Account Owner Type | accountOwnerType | 100% | 4 | RICH | Sole/Joint/Trust/None |
| 35 | Account Owner | accountOwner | 100% | 6 | RICH | |
| 36 | Account Category | accountCategory | 100% | 10 | RICH | Retirement/Investment/Trust/Education… |
| 37 | Account Subcategory | accountSubCategory | 100% | 17 | RICH | |
| 38 | Tax Status (account) | accountTaxStatus | 100% | 3 | RICH | Taxable/Tax-Exempt/Other |
| 39 | Tax Lot Methodology | taxLotMethodology | 100% | 1 | RICH* | All "FIFO" |
| 40 | Client Name | clientName | 98.8% real | 60+ | RICH | See §3 — real for 18,703 rows |
| 41 | Client Street Address | clientStreetAddress | 98.8% real | 60+ | RICH | |
| 42 | Client City | clientCity | 98.8% real | 60+ | RICH | |
| 43 | Client State | clientState | 98.8% real | 16 | RICH | **Geo driver** — 87% TX |
| 44 | Client Zip Code | clientZipCode | 98.8% real | 60+ | RICH | |
| 45 | AssetID | assetID | 100% | 60+ | RICH | |
| 46 | Asset Display Name | assetDisplayName | 0% | 0 | **EMPTY** | Redundant w/ Asset Name |
| 47 | Asset Name | assetName | 100% | 60+ | RICH | |
| 48 | Original Asset Name | originalAssetName | 100% | 60+ | RICH | |
| 49 | Last Dividend | lastDividend | 77% | 60+ | PARTIAL | Securities only (not cash) |
| 50 | Symbol | identifier | 100% | 60+ | RICH | |
| 51 | Ticker | ticker | 96% | 60+ | RICH | |
| 52 | CUSIP | cusip | 94% | 60+ | RICH | |
| 53 | Bond Duration | bondDuration | 100% | 27 | RICH | 0 for non-bonds |
| 54 | Coupon Rate | couponRate | 3% | 48 | SPARSE | Bonds only (637 rows) |
| 55 | Expense Ratio | expenseRatio | 67% | 60+ | PARTIAL | Funds/ETFs only |
| 56 | Issue Date | issueDate | 3% | 60+ | SPARSE | Bonds only (650 rows) |
| 57 | Share Class Type | shareClassType | 100% | 10 | RICH* | Mostly "Not Available" |
| 58 | Call Date | callDate | 2% | 60+ | SPARSE | Callable bonds only (318 rows) |
| 59 | Called Date | calledDate | 0% | 0 | **EMPTY** | |
| 60 | Tax Status (asset) | assetTaxStatus | 100% | 4 | RICH | |
| 61 | SEC Asset Type | secAssetType | 100% | 9 | RICH | Asset classification |
| 62 | Cash Equivalent | cashEquivalent | 100% | 2 | RICH | true/false |

**Summary counts:** RICH ≈ 47 · PARTIAL 2 · SPARSE 8 · EMPTY 6. (`RICH*` = 100% populated but single-valued or sentinel-dominated → *structurally* rich, *semantically* low-information.)

---

## 2. Analytics-driving value distributions

**External Flow** (the NNA inflow/outflow classifier): Contribution **10,521** · None **8,231** · Withdrawal **177**.

**Transaction Type** (12): Transfer In **8,996 (47.5%)** · Dividend Reinvestment 2,988 · Dividend 2,461 · Buy 1,735 · Cash Deposit 1,525 · Journal 586 · Interest 329 · Cash Withdrawal 142 · Sale 115 · Expense 29 · Transfer Out 22 · Return of Capital 1.

**Custodian** (11): **Fidelity IWS 18,703 (98.8%)**; remainder held-away/aggregated (Voya, Capital One, BofA, Vanguard, credit unions, credit cards, Schwab, Transamerica, Invesco, Chase).

**Account Category** (10): Retirement 10,406 · Investment 6,047 · Trust 1,622 · Education 598 · Business Interests 113 · Credit Card 59 · Cash 47 · Other 33 · Loans 3 · Mortgage 1.

**SEC Asset Type** (9): RIC (mutual funds/ETFs) 12,735 · Cash & Equivalents 4,568 · ETF Equity 1,032 · Muni Bonds 446 · N/A 70 · IG Corp Bonds 45 · Govt/Agency 27 · Derivatives 4 · Non-IG Corp 2.

**Client State** (16): **TX 16,497 (87%)** · CA 858 · FL 350 · No State 226 · AZ 143 · WI 142 · NC 131 · NY 128 · MO 126 · KY 123 · OK 60 · SC 54 · VA 45 · CO 32 · PA 12 · +1.

**Account Owner Type:** Sole 14,336 · Joint 2,680 · Trust 1,652 · None 261.

---

## 3. The sentinel correction — geo/PII is REAL (important)

A first pass reads several fields as "100% populated" while their *samples* show placeholders (`No Name`, `No City`, `No State`, `No Zip`, `No RepName Assigned`). **These sentinels are NOT widespread.** Measuring real-vs-sentinel across the 5 client-PII fields:

- **18,703 rows (98.8%) carry 5/5 real PII fields** (name, street, city, state, zip).
- **226 rows (1.2%) carry 0/5** — and these are exactly the 226 "No RepName Assigned" / held-away accounts.

**Conclusion:** client identity + geography are genuinely populated. **Geo analytics (bd-pipeline gold script 07 — NNA/AUA by geography/state/city) is fully feasible for COT.** Cottonwood is a Texas-concentrated book (87% TX). The only fields that are structurally-rich-but-semantically-empty are the BD-feature fields COT doesn't use: Portfolio Strategy ("No Strategy"), Account Display Number, Share Class Type, DST Rep Name, Tax Lot Methodology (uniform FIFO).

---

## 4. The onboarding-window caveat (must carry into gold NNA semantics)

This 6-month window is **dominated by onboarding migration**: Transfer In is 47.5% of all transactions, and External Flow=Contribution outnumbers Withdrawal **59:1**. This is the **same pattern documented for Inflection NNA** (`project_inflection_nna_is_institutional_not_cash_only` — ~72% of inflow $ was Merge-In book migrations, not deposits).

**Implication for the gold layer:** COT's NNA must be classified as **institutional Net-New-Assets** (transaction-classified, in-kind transfers included), **not** strict cash-in/out. A naïve cash-only NNA would massively undercount the onboarding flows. The `External Flow` + `Transaction Type` + `Action` fields together give us the classification surface to do this correctly — and we should port the Inflection NNA classification semantics, not re-derive a cash-only definition. (Flag for portal tooltip wording, same "deposits minus withdrawals" label-drift risk Inflection hit.)

---

## 5. Coverage gap — transactions ≠ positions/AUA (linkage to Brief 3)

This export is **transactions only** (`queryTypeId=2`). The bd-pipeline gold layer needs more than transactions:

| bd-pipeline gold need | Served by this export? | Source |
|---|---|---|
| NNA / flows (scripts 07, 08, 10) | **Yes** — External Flow + Transaction Type + amounts | This Transactions export |
| Geo/advisor cohorts (07, 08, 09) | **Yes** — Client State/City + relationship/account dims | This Transactions export |
| Positions cube / holdings (02, 03) | **No** | DataMining `queryTypeId=1` (Holdings) — available per Brief 1 §3.1 |
| AUA snapshots / balances | **No** (transactions carry price, not market-value balances) | Holdings + a `facts`/`measures` query (Market Value measure) |
| Client performance (05) | **No** | A performance query type, or derived downstream |
| Tax liability / cost basis (06) | **Partial** — has tax status, FIFO, asset attrs; not lot-level gain/loss | Holdings/tax-lot query |

**Action:** the COT bronze must pull **at least two DataMining domains** — Transactions (`queryTypeId=2`, this) **and** Holdings/positions (`queryTypeId=1`) — plus a market-value/measure query for AUA. All are reachable from the single DataMining contract (Brief 1). Brief 3 details how this maps onto the bd-pipeline medallion.

---

## 6. Bottom line

`CW_Transactions_Rich` is a high-quality, richly-populated transaction extract: ~47 of 63 fields are genuinely rich, client geography/identity is real (98.8%), and the transaction taxonomy (External Flow × Transaction Type × Action) is exactly what the gold NNA/flows analytics consume. Two cautions carry forward: (1) classify NNA as **institutional** (onboarding-heavy window, Inflection precedent), and (2) transactions alone don't cover positions/AUA/performance — bronze must add the Holdings + measure query types. The empty/sparse fields are BD features COT doesn't use, not data-quality gaps. Proceed to Brief 3 (bd-pipeline deep dive + medallion port plan).
