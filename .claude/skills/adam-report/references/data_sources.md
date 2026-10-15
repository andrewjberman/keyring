# Data sources -- where every memo figure comes from

Order of preference for each item: **(1) the opalgateway harvest tools** (fast, Opal's own vetted store), then
**(2) primary filings on the web (SEC EDGAR or the home regulator)**, then **(3) the company's own IR material**,
then **(4) reputable secondary sources**. Record the source of every figure in the section's Sources note.

## 1. Opal data harvest via the opalgateway MCP

Tool names below are the opalgateway connector's; in a client they may carry a prefix
(`mcp__opalgateway__harvest_get_fundamentals`). Run independent calls in parallel.

| call | gives | feeds |
|---|---|---|
| `harvest_resolve_security(query="<ticker or name>")` | `status` exact / candidates / none / not_held, `security_key` (e.g. `UNH_US_Equity`), CIK, ISIN, other listings | everything; `none`, `not_held` or an unmatched `candidates` list means the harvest does not cover the name -> web path |
| `harvest_security_coverage(security_key)` | which datasets hold the name and how many trading days behind T-1 each is | decide per section: harvest or web |
| `harvest_get_fundamentals(security_key, kind="model", mnemonics=[...])` | annual fiscal-year lines, about FY2016-FY2025, Bloomberg-standardised, `MILLIONS` in reporting currency | 10-year table, balance-sheet FY column, valuation history |
| `harvest_get_fundamentals(security_key, kind="consensus")` | Bloomberg BEST consensus FY1-FY3 (`1FY`, `2FY`, `3FY`) | estimate columns, comps FY1/FY2 |
| `harvest_get_fundamentals(security_key, kind="segments")` | 5 annual periods of segment and product revenue / operating income (periods are unlabelled; period 1 = latest FY: check it sums to revenue) | company description table, sales-by-region table |
| `harvest_get_fundamentals(security_key, kind="valuation_history")` | year-end P/E, EV/EBITDA, P/B and FCF-yield bands | valuation commentary |
| `harvest_get_fundamentals(security_key, kind="price")` | daily closes, last ~30 days only | share price and recent move (not enough for a 52-week range) |
| `harvest_get_research(security_key)` | research dossier (thesis, risks, positives / negatives), continuation (`fund_of_record`, `last_stated_position`, `thesis_pillars`), `ai_fill_blocks` (`mgmt_bio`, `mgmt_team_view`, with citations), prior Opal research reports, `management_roster` (Bloomberg executive officers) | thesis, risks, management, prior Opal view |
| `harvest_get_filing_analysis(security_key)` | the latest analysed filing: guidance, segments, risks, commentary, big bets, big challenges, with citations (often only the annual 10-K / 20-F) | risks, guidance, description |
| `harvest_get_peers_and_scores(security_key)` | peer list, scores, Opal posture | starting point for comps (check the peers are the right industry; the list is size/sector-based) |
| `harvest_search_articles(security_key, limit=25)`, `harvest_get_chatter(...)`, `news_for_security(ticker=...)` | recent articles with sentiment | recent events, stock moves, broker actions |

Always pass `mnemonics` to `kind="model"`: the unfiltered response is ~70 KB. The core list:

```
SALES_REV_TURN  IS_OPER_INC  OPER_MARGIN  EBITDA  EBITDA_ADJUSTED  EBITDA_MARGIN  NET_INCOME  IS_DIL_EPS_CONT_OPS
IS_EPS  IS_COMP_EPS_ADJUSTED  IS_SH_FOR_DILUTED_EPS  ARD_SHARES_OUTSTANDING  CF_CASH_FROM_OPER  CAPEX_ABSOLUTE_VALUE
CF_FREE_CASH_FLOW  EQY_DPS  SHORT_AND_LONG_TERM_DEBT  BS_CASH_NEAR_CASH_ITEM  CASH_AND_MARKETABLE_SECURITIES
ARD_TOT_ASSETS  BS_TOTAL_LIABILITIES  TOTAL_EQUITY  ARD_GOODWLL  ARD_OTHER_INTANGIBLE_ASSET  PX_LAST
HISTORICAL_MARKET_CAP  PE_RATIO  EV_TO_T12M_EBITDA  DIVIDEND_YIELD  GROSS_MARGIN
```

Consensus row fields: `BEST_SALES BEST_EBIT BEST_EBITDA BEST_NET_INCOME BEST_EPS BEST_EPS_NUMEST BEST_DPS
BEST_ESTIMATE_FCF BEST_CAPEX BEST_BPS BEST_PE_RATIO BEST_DIV_YLD BEST_PERIOD_END_DATE`.

What the harvest does **not** hold (go to the web for these even when the name is covered): quarterly or interim
figures (H1, latest 10-Q balance sheet, LTM), the debt maturity ladder, credit ratings and outlooks, company-defined
adjusted metrics (e.g. "Core Adjusted EBITDA", "Adjusted FCF") and KPI lines, guidance from the latest quarter,
52-week range and YTD return, withholding-tax rates. The harvest covers about 240 names; a name outside it (TMUS
was, on 2026-10-15) takes the whole web path.

## 2. Web fallback -- when it applies and where to look

Fall back to web search, **for that item only**, when any of these holds:
- the opalgateway connector is not available or a call errors / times out;
- `harvest_resolve_security` does not return `exact` for the company;
- the dataset is absent (`absent_reason` set, empty `figures` / `rows`) or more than 5 trading days behind T-1;
- the item is on the "does not hold" list above.

Say so in the section's Sources note: *"Opal data harvest did not hold <item> as of <date>; sourced from <source>."*

Source ranking (use the highest that answers; never cite an unsourced blog or content farm):

1. **SEC EDGAR** (US filers): 10-K, 10-Q, 8-K Ex. 99.1 earnings releases, DEF 14A proxy (board, pay, control).
   - Ticker -> CIK: `https://www.sec.gov/files/company_tickers.json`
   - Filing list: `https://data.sec.gov/submissions/CIK##########.json` (CIK zero-padded to 10 digits)
   - Every XBRL fact: `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`. Useful concepts:
     `Revenues`, `RevenueFromContractWithCustomerExcludingAssessedTax`, `OperatingIncomeLoss`, `NetIncomeLoss`,
     `EarningsPerShareDiluted`, `WeightedAverageNumberOfDilutedSharesOutstanding`,
     `NetCashProvidedByUsedInOperatingActivities`, `PaymentsToAcquirePropertyPlantAndEquipment`,
     `CommonStockDividendsPerShareCashPaid`, `LongTermDebt`, `CashAndCashEquivalentsAtCarryingValue`,
     `dei:EntityCommonStockSharesOutstanding` (cover-page share count).
   - EDGAR full-text search: `https://www.sec.gov/edgar/search/`
   - A script fetching `data.sec.gov` must send a descriptive `User-Agent` (firm name and a contact address) or
     SEC refuses it; a browser or web-fetch tool needs nothing extra.
2. **Home regulators** for non-US issuers: 20-F / 6-K on EDGAR where filed, otherwise the annual report and the
   exchange / regulator filing system (Companies House and RNS, SEDAR+, EDINET, HKEXnews, AMF, CNMV, BaFin register).
3. **Company investor relations**: earnings releases, investor factbooks, capital-markets-day targets, the debt
   schedule / fixed-income page (maturities, ratings), dividend announcements.
4. **Ratings agencies** (S&P, Moody's, Fitch) for ratings and outlooks; confirm against the company's IR page.
5. **Consensus and market data**, when the harvest has none: MarketScreener, StockAnalysis, Yahoo Finance, Nasdaq,
   exchange websites. State which, the page date and whether EPS is GAAP or adjusted.
6. **Reputable press** for events, management changes and broker actions: Reuters, Bloomberg, WSJ, FT, CNBC, the
   trade press of the industry.
7. **Tax**: IRS treaty tables / the treaty text for dividend withholding rates for a US holder.

## 3. Opal-derived figures (teal italics)

Anything Opal computes rather than reads is teal: growth rates, margins, CAGRs, payout ratios, multiples, yields,
per-share back-outs, LTM sums, bucket sums, medians, "change" columns, implied shares (consensus net income / EPS).
Compute them from the figures in the table so the table ties out. Checks before building:
- segment or line rows add to the reported total (state any residual as "Other");
- EPS approximately equals net income / diluted shares (state the tie-out tolerance);
- the snapshot market cap = price x shares, EV = market cap + net debt;
- CAGR spans are stated in the header (e.g. "9y CAGR 2016-25").
