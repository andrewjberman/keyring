# ADVI_COTETL — Full BD DataMining Field Catalog per Endpoint (Cottonwood)

**Author:** 0.4.0_DS_ClientPlatform · **Date:** 2026-06-08 · **Project:** ADVI_COTETL
**Source:** DimensionsFacts catalogs + template bodies across the 3 captured HARs. This is the COMPLETE menu of selectable dimensions + measures BD exposes for Cottonwood per query type — not just what any one template selected.

## 0. Structure
All 5 endpoints draw from ONE shared dimension core (Team/Relationship/Portfolio Group/Portfolio/Account/Classification/Holding). Each endpoint adds a specialty level (Transactions for qt2; Tax Lot for qt3/qt4) and its own measures. qt5 (Allocation) reorganizes the same core into parent/child dimension levels over an allocation hierarchy. Counts:

| Endpoint | qt | dims | levels | measures |
|---|---|---|---|---|
| Snapshot (Holdings) | 1 | 205 | 7 | 4 |
| Transaction | 2 | 222 | 8 | 5 |
| Realized Gain/Loss | 3 | 209 | 8 | 7 |
| Unrealized Gain/Loss | 4 | 208 | 8 | 11 |
| Allocation | 5 | via alloc hierarchy | 7 | 3 |

---
## 1. Shared dimension core (available on qt1/2/3/4; qt5 via parent/child)

### Team (10 dims)
`Team`, `Team Display Name`, `Team Description`, `Address 1`, `Address 2`, `City`, `State`, `Zip Code`, `Phone`, `Primary Email`

### Relationship (10 dims)
`Relationship ID`, `Relationship Name`, `Relationship Display Name`, `Relationship SEC Client Type`, `Relationship Inception Date`, `Relationship Termination Date`, `Relationship Benchmark`, `Relationship Target`, `Relationship Target ID`, `Relationship Target Description`

### Portfolio Group (3 dims)
`Portfolio Group`, `Previous System Key`, `Exclude From BI`

### Portfolio (48 dims)
`PortfolioID`, `Portfolio Name`, `Previous System Key`, `Portfolio Display Name`, `Portfolio Notes`, `Exclude From Batch`, `BD3 Report Template Name`, `BD3 Report Template Description`, `Show Client`, `Portfolio Logo`, `Portfolio Reporting Target`, `Reporting Target Description`, `Portfolio Benchmark`, `Portfolio Strategy ID`, `Portfolio Strategy Name`, `Portfolio Fee Schedule`, `Fee Schedule Description`, `Basis Points`, `Fee Schedule Level`, `Fee Schedule Rate Type`, `Fee Schedule Type`, `Lower Range`, `Upper Range`, `Flat Fee`, `History Start Date`, `Portfolio - Billing Configuration Name`, `Portfolio - Billing Configuration Description`, `Portfolio - Rep Fee Split`, `Portfolio - Billing Discount Percentage`, `Portfolio - Billing Notes`, `Portfolio - Billing Team Name`, `Portfolio - Billing Include Non-Billable`, `Portfolio - Billing Breakpoint Portfolio`, `Primary Portfolio Group`, `Address Source Account Number`, `Address Source Account Name`, `Primary Client Relationship Portfolio`, `Primary Client Relationship for Portfolio Group`, `Admin Only`, `Demo Portfolio`, `Address Source Client Name`, `Address Source Street Address`, `Address Source City`, `Address Source State`, `Address Source Zip Code`, `Portfolio Rebal Assignment ID`, `Portfolio Program ID`, `Portfolio Program Name`

### Account (81 dims)
`Account Number`, `AccountID`, `Original Account Number`, `Account Display Number`, `Account Name`, `Account Display Name`, `Original Account Name`, `DST Rep Name`, `Data Provider`, `Custodian`, `Position Only`, `Rep Code`, `SEC Client Type`, `Style`, `External Style ID`, `Manager`, `Account Owner Type`, `Account Owner`, `Goal`, `Account Category`, `Account Subcategory`, `Tax Status`, `Tax Lot Methodology`, `Tax Lot Methodology`, `Account Reporting Target`, `Reporting Target Description`, `Account Benchmark`, `Account Supervised`, `Account Billable`, `Account Discretionary`, `Account Fee Schedule`, `Fee Schedule Description`, `Fee Schedule Type`, `Fee Schedule Rate Type`, `Upper Range`, `Lower Range`, `Fee Schedule Level`, `Basis Points`, `Flat Fee`, `Billing Start Date`, `Billing End Date`, `Billing Account`, `Billing Account Custodian`, `Pay by invoice`, `Account - Billing Configuration Name`, `Account - Billing Configuration Description`, `Account - Rep Fee Split`, `Account - Billing Discount Percentage`, `Account - Billing Notes`, `Account - Billing Team Name`, `Account - Billing Include Non-Billable`, `Account - Billing Breakpoint Portfolio`, `Account Strategy ID`, `Account Strategy Name`, `Start Date`, `Performance Start Date`, `As of Date`, `Account Is Open`, `Closed Date`, `History Start Date`, `Client Name`, `Client Street Address`, `Client City`, `Client State`, `Client Zip Code`, `Advisor of Record Name & B2B ID`, `Authorized Person`, `CSP Date`, `Managed Program Type`, `NFS Account Number`, `Team Name - Salentica`, `Wrap/Non-Wrap`, `Account Type`, `Account Registration Type`, `Account Create Date`, `Account Rebal Assignment ID`, `Account Program ID`, `Account Program Name`, `Manager Strategy`, `Investment Strategy Name`, `Managed Account Manager Name`

### Classification (2 dims)
`Class`, `Segment`

### Holding (51 dims)
`AssetID`, `Asset Name`, `Class`, `Custom`, `Fixed`, `Industry Group`, `Sector`, `Security Type`, `Asset Display Name`, `Original Asset Name`, `Last Dividend`, `Symbol`, `Ticker`, `CUSIP`, `Alternative Identifier`, `Holding Supervised`, `Holding Billable`, `Holding Discretionary`, `Investment Discretion`, `Voting Authority`, `Automated`, `Billing Cash`, `Custodial Cost Basis Sync`, `Bond Duration`, `Coupon Rate`, `Custodian Security Code`, `First Payment Date`, `Last Payment Date`, `Ex Date`, `Expense Ratio`, `Share Class Type`, `Issue Date`, `Location`, `Maturity Date`, `Municipal State`, `Has Prerefunded Date`, `Call Date`, `Called Date`, `Issue Type`, `Tax Status`, `Payment Frequency`, `Cash Equivalent`, `Is 13F Eligible`, `Long Holding`, `Accrual Day Count Methodology`, `SEC Asset Type`, `Asset Benchmark`, `Fund Family Name`, `Fund Manager`, `Investment Period Close Date`, `Target Return`

---
## 2. Per-endpoint specialty level + measures

### Transaction (qt2) — specialty level **Transactions** (17 dims)
`TransactionID`, `Return Date`, `Action`, `Transaction Type`, `Transaction Sub Type`, `External Flow`, `Has Contra Account`, `Contra Account Number`, `Contra Account Name`, `Description`, `Price`, `Trade Date`, `Settle Date`, `Entry Date`, `Internal Notes`, `User Notes`, `Backdated Date`

**Measures:** Units, Market Value, Transaction Fee, Income, Account Fee

### Realized Gain/Loss (qt3) — specialty level **Tax Lot** (4 dims)
`Open Date`, `Trade Date`, `Unit Cost`, `Is Wash Sale`

**Measures:** Units, Cost Basis, Proceeds, Short-Term Gain/Loss, Long-Term Gain/Loss, Total Gain Loss, Disallowed Loss

### Unrealized Gain/Loss (qt4) — specialty level **Tax Lot** (3 dims)
`Open Date`, `Unit Cost`, `Inherited Date`

**Measures:** Units, Cost Basis, Amortization, Market Value, Short-Term Gain/Loss, Long-Term Gain/Loss, Total Gain Loss, Unaccrued Market Value, Unaccrued Short-Term Gain/Loss, Unaccrued Long-Term Gain/Loss, Accrual

### Snapshot/Holdings (qt1) — core only, no specialty level
**Measures:** Market Value, Accrual, Units, Unaccrued Market Value

### Allocation (qt5) — same core via parent/child dimension levels over an allocation hierarchy
Allocation hierarchy levels: `Portfolio Group` -> `Client Relationship` -> `Portfolio` -> `Account` -> `Class` -> `Segment` -> `Holding`. Dimensions are selected as parentDimensionLevels (Team/Relationship) + childDimensionLevels (Portfolio/Account/...) drawn from the same core. Cash inclusion is configurable.
**Measures:** Market Value, Allocation % (per hierarchy level), Units
