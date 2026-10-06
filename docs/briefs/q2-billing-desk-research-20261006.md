# Q-2 Billing: Buy or Build -- Desk Research

Research lane of `4.0.0_SA_CRO`, run on Andrew's word of 2026-10-06 ~19:2xZ ("4.) Yes": public web sources, read-only;
record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_192xZ_DELLS_SECHIST_LIFT_PUSH_RHYTHM_RESEARCH_EGRESS_Q3_OPS_WORKFLOW.md`).
The companion L1 brief is `docs/briefs/q2-billing-buy-or-build-brief-20261006.md`.

Prepared 2026-10-06 from public sources only (vendor sites, help centers, press releases, SEC/NASAA texts, industry press). No accounts, forms, or vendor APIs were used. Bracketed numbers point to section 8. "UNCONFIRMED" marks anything public sources did not settle.

## 1. The answer in five lines

1. "Buy all" is almost certainly Morningstar **ByAllAccounts**, an account-aggregation (data-gathering) service. It does not bill. Morningstar agreed in April 2026 to sell it to Pello Companies [1][2].
2. The Morningstar product that did bill, **Morningstar Office**, was retired on 2026-02-28, and Morningstar steered its users to Black Diamond [3][4][5].
3. Billing is a well-defined calculation: values on the billing date (or average daily balance) times a tiered or flat schedule, adjusted for household grouping, flows, minimums and exclusions. The output is a custodian fee file uploaded to Schwab Advisor Center, plus client invoices or statements [6][7][8][9][10].
4. Several vendors sell billing without their portfolio-accounting system. The clearest are **Envestnet BillFin** (accepts uploaded values on a template), **SmartKx**, and **Altruist** (free on Altruist custody, USD 1 per account per month for third-party accounts above 100) [11][12][13][14].
5. Recommendation: **buy the calculation engine and front it** for the 2027-01-01 cutover, with Opal feeding it values and households. A narrow Opal-built engine is feasible later, but fee errors are the SEC's most-cited fee deficiency and must be designed in, not patched [9].

## 2. How advisory-fee billing works

**Fee schedule types.** Flat dollar fees, tiered percentage-of-AUM (assets under management) fees, security-type tiers, and performance fees are standard methodologies [8]. Tiers are "blended" (each slice of assets at its own rate) or "discrete/cliff" (the whole balance at one rate) [10][11]. An annual minimum is enforced per period: a USD 1,200 annual minimum billed quarterly becomes at least USD 300 a quarter [8].

**Frequency and timing.** Most firms bill quarterly or monthly, in advance (the first fee covers the coming period) or in arrears (it covers the period just ended) [6][10][11]. Switching from arrears to advance forces a double bill to close out the old basis [15].

**Valuation basis.** Either period-end value or average daily balance; the advisory agreement fixes which [11][15]. The SEC staff found advisers using period-end value where the contract said average daily balance [9].

**Proration.** New accounts that start mid-period and money flowing in or out during the period are prorated. Morningstar Office calls proration optional but "always recommended", because without it you overcharge in arrears or undercharge in advance [8]. Form ADV (the adviser registration form) Part 2A Item 5D requires the adviser to disclose how prepaid fees are refunded on termination [9].

**Household aggregation.** Accounts are grouped (a "billing group" or household) so the combined value reaches lower breakpoints [7][8]. The fee is then allocated back to each account, or to one designated paying account [8][17].

**Exclusions.** Assets, securities, accounts or asset classes (cash, alternatives, variable annuities) can be excluded by contract [8][9][11].

**Inputs required per billing run:**
- account values on the billing date, or daily values for an average daily balance;
- dated external cash flows (deposits and withdrawals) for proration;
- account open and close dates;
- the household or billing-group mapping and the fee-paying account designation;
- the fee schedule, minimum, discounts and exclusions per account or group, taken from the signed advisory agreement;
- custodian and master-account identifiers.

**Outputs:**
- a per-account fee;
- a custodian fee file;
- client invoices or statements showing the billable value, tiers, adjustments and proration [7];
- revenue and payout (advisor compensation) reports [11][17];
- an audit history of fee-schedule changes [18].

## 3. Who does it today

| Vendor | What it does | Standalone (without the vendor's portfolio accounting)? | Integration | Source |
|---|---|---|---|---|
| SS&C Black Diamond | Billing and revenue management inside the Black Diamond platform; sends management fees to Schwab "with a few clicks" | No: a module of the platform | Schwab Advisor Center integration; REST API with OAuth. A billing endpoint is UNCONFIRMED | [19][20][21] |
| Advent Revenue Center (SS&C) | Fee structures, invoices, debit letters, revenue forecasts | Historically separate from Black Diamond. Current availability is UNCONFIRMED (one directory lists it as discontinued) | Files | [22][23] |
| Orion | Billing engine for advance or arrears billing, personalized schedules, exclusions, paying accounts, mock bills, payouts; creates custodian-specific fee files with a "Send" shortcut to Schwab | Sold as part of Orion Connect. Standalone use is UNCONFIRMED | Custodian fee files. A secondary source says Orion's API reads and writes billing data | [16][17][18][24] |
| Envestnet BillFin | Purpose-built RIA (registered investment adviser) billing: flat, tiered and banded AUM fees; advance or arrears; period-end or average daily balance; exclusions by household, account, asset class or security; branded invoices; payouts | **Yes.** Values can be synced or uploaded "using a simple template" | Schwab, Fidelity, Pershing, RBC; custodian fee-file templates. A public API is UNCONFIRMED | [11][12] |
| Envestnet Tamarac | Billing definitions, billing groups (households), proration, average-balance valuation, client billing statements | No: part of Tamarac Reporting | Custodian fee-file output is UNCONFIRMED in public help | [7] |
| Envestnet Revenue Manager | Enterprise billing templates, approval workflows, revenue sub-ledger | Enterprise product, not RIA-scale | UNCONFIRMED | [25] |
| Addepar | Tiered or flat schedules, exclusions, billable portfolios; downloads in Schwab and Pershing formats | No: part of Addepar | Custodian-format files; APIs for reports and imports | [26] |
| Advyzon | Multiple schedules, AUM plus flat fees, advance or arrears, average or period-end, blended or discrete tiers; preformatted custodian fee files; direct upload to Schwab | No: an all-in-one platform | Custodian files; Apex fee submission by API | [27][28] |
| SmartKx | Billing and contract system in which "the client contract is the fee calculator"; bulk fee files per master account | **Yes**: a billing and contracts product | Schwab data feed; Redtail and Wealthbox CRMs. A public API is UNCONFIRMED | [13][29] |
| Altruist | Built-in AUM billing and automatic deduction for Altruist-custodied accounts | Billing is free with Altruist custody; third-party (Schwab, Fidelity) accounts cost USD 1 per account per month above 100 | Custodian-native | [14] |
| AdvicePay | Payments for fee-for-service (planning) fees, not AUM billing | Yes | Integrations | [30] |

## 4. Morningstar specifically

- **ByAllAccounts is aggregation only.** Morningstar describes it as a "financial data aggregation and enrichment solution" [31]. The sale announcement describes "data aggregation technology", used for portfolio management, reporting, compliance and tax-aware investing [1]. No public source describes it calculating or collecting fees.
- **Ownership is changing.** On 2026-04-09 Pello Companies agreed to buy ByAllAccounts, with closing expected in the first half of 2026. ByAllAccounts will run standalone, and Morningstar stays a customer [1][2]. Whether the sale has closed is UNCONFIRMED.
- **Morningstar Office did bill, and it is gone.** It calculated flat, tiered and performance fees, minimums, proration, group billing and custodian fee files in CSV (comma-separated values) format [8][32]. Morningstar retired it on 2026-02-28 [3]. More than 400 firms moved to Black Diamond under an SS&C-Morningstar alliance [3][4][5].
- **Morningstar Wealth's turnkey platform also exited.** Morningstar sold its turnkey asset management platform (TAMP) assets to AssetMark in 2024 [33].
- **Most likely reading of "buy all":** the advisors' data reaches Black Diamond or Orion partly through ByAllAccounts for held-away accounts, and billing runs in Black Diamond or Orion, not in Morningstar. A firm that was a former Morningstar Office user would now be on Black Diamond. UNCONFIRMED for 49 Financial and Cottonwood; see section 7.

## 5. Custodian fee-deduction path and regulatory constraints

**Schwab mechanics.** The adviser uploads a management-fee file to Schwab Advisor Center as a .csv, .txt or .mfa file "following Schwab's required format". A Management Fee Worksheet validates each account before upload and shows why a fee would be rejected [34]. The minimum data per fee is the Schwab account to debit, the dollar amount, and the adviser's fee account number [35].

Schwab is expanding account numbers (to 10 digits). Firms with proprietary fee-file software may need to update it and should read the technical specifications on Schwab Advisor Center's Technical Support tab [34]. The field-level layout is behind Schwab's login: UNCONFIRMED here.

Both Schwab pages returned HTTP 403 (access refused) to direct fetch, so their content was read through search-engine excerpts. Orion's workflow confirms the same path: generate the fee file, verify its total against Schwab's balance due, then import it in Advisor Center's Management Fees section [16]. The client authorizes deduction through Schwab's Fee Payment Authorization in the limited power of attorney (LPOA), and the fee appears on Schwab's client statement [36].

**SEC custody rule (Rule 206(4)-2).**
- Authority to withdraw client funds, including fee deduction, is "custody" [37][38].
- An adviser with custody needs a qualified custodian and "a reasonable basis, after due inquiry" that the custodian sends quarterly statements [37].
- The annual surprise examination does not apply where custody exists "solely as a consequence of your authority to make withdrawals ... to pay your advisory fee" [37].
- The SEC withdrew its 2023 replacement "Safeguarding" proposal on 2025-06-12, so the current rule stands [39].

**State-registered advisers (NASAA model rule).** The NASAA (North American Securities Administrators Association) model rule requires written client authorization. Each time a fee is deducted, it requires an invoice to the custodian and an itemized invoice to the client showing "the formula used to calculate the fee, the amount of assets under management the fee is based on, and the time period", plus notice on Form ADV [40]. Whether 49 Financial and Cottonwood are SEC-registered or state-registered is UNCONFIRMED.

**Exam focus.** The SEC staff's most frequent fee deficiencies are:
- wrong valuations;
- wrong valuation basis;
- billing excluded assets;
- billing in advance when the contract says arrears;
- no proration for new or terminated clients;
- wrong rates and double billing;
- missed household aggregation and breakpoints [9].

The staff noted that advisers with "periodic internal testing of billing practices" found and refunded errors themselves [9].

## 6. Buy vs build

**What an Opal-built engine would need.** Opal already has custodial values, flows and households. It would add:
1. a fee-agreement registry per account or group: schedule, tier type, minimum, exclusions, paying account, advance or arrears, valuation basis, start and termination dates, with effective dating and an audit trail [18];
2. a calculation engine covering blended and cliff tiers, proration for flows and partial periods, minimums, discounts and allocation [8][9];
3. a Schwab fee-file writer that tracks Schwab's format changes [34];
4. client invoices or statements meeting the NASAA itemization if any firm is state-registered [40];
5. maker-checker approval, a stored immutable bill history, and refund handling for terminations [9].

Items 1, 2 and 5 carry the regulatory risk. Item 3 is the brittle integration.

**What "buy and front" means.** Opal pushes values, flows and household maps to a standalone engine (BillFin's upload template [12], SmartKx, or the Orion billing the firms may already pay for [16]). The vendor calculates, produces the Schwab file and invoices, and keeps the audit history. Opal shows the results in its portal. Altruist is cheap but tied to Altruist custody to be free [14].

**Recommendation.** For 2027-01-01, buy:
- Keep the fee calculation and the Schwab file in a purpose-built, already-examined product.
- Make Opal the system of record for the inputs (values, flows, households).
- Make Opal the display surface for the outputs.
- Shortlist: **BillFin** (explicitly standalone with an upload template) and **SmartKx** (standalone, contract-driven).
- If either firm stays on Orion, keep Orion billing for those accounts and do not migrate them.
- Before the first live run, recompute the last billed quarter once in the new engine and reconcile it to the actual Schwab debits. This is a one-time conversion check, not a standing comparator.

Revisit "build" only after two or more clean quarters and a documented fee-agreement inventory.

**Main risks:**
- **Fee errors.** These are the top SEC deficiency and may require client refunds [9].
- **Audit trail.** The adviser must show which contract term produced each fee [9][18].
- **Custodian file drift.** Schwab is changing account-number formats now [34].
- **Cutover timing (inference, not a sourced fact).** A 2027-01-01 cutover means the 2026-Q4 arrears bill or the 2027-Q1 advance bill is the first live run, in early January 2027. Which system runs it must be decided.
- **Vendor lock-in and pricing.** Prices are not public for BillFin or SmartKx (UNCONFIRMED).

## 7. Open questions only the advisors or counterparties can answer

1. Which system calculates each firm's fees today: Black Diamond, Orion, Morningstar Office (retired), or a spreadsheet? Where does ByAllAccounts appear in their stack?
2. Is each firm SEC-registered or state-registered? This decides whether the NASAA itemized invoice applies.
3. Fee terms per agreement: advance or arrears, period-end or average daily balance, blended or cliff tiers, minimums, exclusions, household rules, paying accounts, payout splits.
4. Which custodians beyond Schwab (Fidelity, Pershing, Altruist) need fee files?
5. Do clients receive invoices today, or only the Schwab statement line?
6. Pricing and API access from BillFin, SmartKx and Orion (a commercial conversation Andrew must authorize).
7. Who signs off each bill run (the adviser's chief compliance officer)?
8. Internal observation, not a public source: this session's tool list includes an Opal gateway tool named `blackdiamond_list_fees`. Opal may already read Black Diamond fee data. UNCONFIRMED; it was not called.

## 8. Sources

1. Morningstar newsroom, "Pello Companies to Acquire ByAllAccounts from Morningstar" (2026-04-09): https://newsroom.morningstar.com/news/news-details/2026/Pello-Companies-to-Acquire-ByAllAccounts-from-Morningstar/default.aspx
2. RIABiz, Morningstar moves on from ByAllAccounts (2026-04-11): https://riabiz.com/a/2026/4/11/morningstar-moves-on-from-byallaccounts-sending-it-to-a-startup-incubator-12-years-after-former-ceo-joe-mansueto-invited-doubts-by-paying-a-premium-for-it-after-market-already-appeared-commoditized
3. SS&C release, "400+ Firms Transition to SS&C Black Diamond ... from Morningstar Office" (2025-08-21): https://s29.q4cdn.com/602562954/files/doc_news/400-Firms-Transition-to-SSC-Black-Diamond-Wealth-Solutions-from-Morningstar-Office-2025.pdf
4. WealthManagement.com, end of Morningstar Office (2025-02-14): https://www.wealthmanagement.com/financial-technology/wealthstack-roundup-the-end-for-morningstar-office
5. RIABiz, Morningstar shuttering Office in 2026: https://riabiz.com/a/2025/2/19/morningstar-is-shuttering-office-in-2026-and-steering-its-orphaned-rias-to-black-diamond-to-get-revenue-cut-in-deal-but-advyzon-and-orion-arent-planning-to-get-cut-out
6. Orion, billing in arrears: https://orion.com/blog/how-billing-arrears-can-help-advisors-get-paid-faster
7. Tamarac help, Introduction to Billing: https://help.tamaracinc.com/help/content/tamarac_reporting/billing/introduction_to_billing.htm
8. Morningstar, "Billing in Morningstar Office" guide (PDF): https://gladmainnew.morningstar.com/articles/tutorial/30/Billing.pdf
9. SEC OCIE (Office of Compliance Inspections and Examinations) Risk Alert, most frequent advisory fee and expense issues (2018-04-12): https://www.sec.gov/files/ocie-risk-alert-advisory-fee-expense-compliance.pdf
10. Orion billing product page: https://orion.com/advisor-tech/portfolio-accounting/billing
11. Envestnet, BillFin for RIAs: https://www.envestnet.com/billing-solutions/for-rias
12. Envestnet, Billing Solutions overview: https://www.envestnet.com/billing-solutions
13. SmartKx, RIA fee billing software: https://www.smartkx.io/best-ria-fee-billing-software/
14. Altruist, eliminating PAS fees (2023-09-21): https://altruist.com/company-insights/eliminating-pas-fees
15. Kitces, advisory fee billing during a merger: https://www.kitces.com/blog/advisory-fee-billing-in-advance-arrears-quarterly-daily-balance-merger-acquisition/
16. Orion, speeding up quarter-end fee submissions: https://orion.com/blog/how-speed-quarter-end-advisor-management-fee-submissions
17. Orion Billing fact sheet: https://orion.com/orion-billing-fact-sheet
18. Orion billing release notes: https://orionadvisortech.com/release-notes-billing/
19. PR Newswire, Black Diamond and Schwab Advisor Center integrations (2020-08-10): https://www.prnewswire.com/news-releases/ssc-announces-expanded-black-diamond-integrations-with-schwab-advisor-center-301109183.html
20. SS&C Black Diamond solution page: https://www.advent.com/solutions/black-diamond-wealth-platform/
21. RFP.wiki, Black Diamond buyer notes (secondary): https://www.rfp.wiki/investment/wealth-management-software/ss-c-black-diamond
22. Advent Revenue Center brief: https://www.advent.com/resources/all-resources/brief-advent-revenue-center/
23. Cuspera listing, Advent Revenue Center (discontinued; secondary): https://www.cuspera.com/products/advent-revenue-center-x-14899
24. Feathery, Orion integration (secondary, for the API claim): https://www.feathery.io/integrations/orion
25. Envestnet Revenue Manager: https://www.envestnet.com/billing-solutions/revenue-manager
26. Addepar, Inside Addepar Q4 2024: https://addepar.com/blog/inside-addepar-q4-2024
27. InvestmentNews, best RIA billing software (2025-08-20): https://www.investmentnews.com/goria/technology/best-ria-billing-software-solutions-for-accuracy-and-efficiency/261798
28. SmartAsset, billing software options (Advyzon detail; secondary): https://smartasset.com/advisor-resources/financial-advisor-billing-software
29. SmartKx integrations: https://www.smartkx.io/integrations/
30. AdvicePay entry in [27].
31. Morningstar ByAllAccounts for enterprises: https://www.morningstar.com/business/products/byallaccounts/for-enterprises
32. Morningstar Office help, Creating Custodian Fee Files: https://awgmain.morningstar.com/webhelp/Practice/Billings/Custodian_Fee_File.htm
33. Nasdaq/AssetMark, completed acquisition of Morningstar Wealth TAMP assets: https://www.nasdaq.com/articles/assetmark-completes-acquisition-morningstar-wealths-turnkey-asset-management-platform
34. Schwab Advisor Services, What's New: Other Enhancements (HTTP 403 to direct fetch; read through search excerpt): https://advisorservices.schwab.com/whats-new/account-management/other-enhancements
35. Schwab, how to collect investment advisory fees (HTTP 403 to direct fetch; read through search excerpt): https://saccontent.schwabcdn.com/ask/funding-disbursements/management-fees/how-to-collect-fees
36. Schwab LPOA for Investment Advisor, with Fee Payment Authorization (form copy; read through search excerpt, not fetched): https://www.q3tactical.com/Forms/LPOA_for_IA.pdf
37. 17 CFR 275.206(4)-2 (Cornell Legal Information Institute): https://www.law.cornell.edu/cfr/text/17/275.206(4)-2
38. Kitces, RIA custody rule liability triggers: https://www.kitces.com/blog/ria-custody-rule-2064-2-investment-advisers-act-1940-sec-regulation-trigger-compliance-liabillity/
39. Dechert, SEC withdraws rule proposals (June 2025): https://www.dechert.com/knowledge/onpoint/2025/6/sec-withdraws-significant-number-of-rule-proposals.html
40. NASAA Model Rule 102(e)(1)-1, custody requirements: https://www.nasaa.org/wp-content/uploads/2011/07/11-IACustodyRules.pdf
