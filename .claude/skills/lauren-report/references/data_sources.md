# Data sources for an earnings update

Preference per item: **(1) the Opal data harvest through the opalgateway MCP**, **(2) the company's own quarterly
filings and release (SEC EDGAR or the home regulator)**, **(3) company IR material**, **(4) reputable secondary
sources**, and **AlphaSense** for the series only it holds. Name the source of anything non-obvious in the text.

## 1. Opal data harvest (opalgateway)

| call | use |
|---|---|
| `harvest_resolve_security(query)` | `security_key` (e.g. `ASML_NA_Equity`, `UNH_US_Equity`); not `exact` -> skip to the web |
| `harvest_get_research(security_key)` | `research_reports` lists Opal's prior reports for the name (e.g. her 2Q26 update, `report_class` B, `fund`, `period`); continuation `fund_of_record` / `last_stated_position`; dossier positives / negatives; `ai_fill_blocks` |
| `harvest_list("amgt/harvest/bronze/research-report/security_key=<key>/")` | the prior report files themselves (PDF / xlsx) by folder |
| `harvest_get_fundamentals(key, kind="consensus")` | FY1-FY3 consensus (`BEST_SALES BEST_EBIT BEST_EBITDA BEST_EPS BEST_DPS BEST_ESTIMATE_FCF BEST_CAPEX BEST_NET_INCOME BEST_EPS_NUMEST`) for the 2026E-2028E columns |
| `harvest_get_fundamentals(key, kind="model", mnemonics=[...])` | last-FY column (`SALES_REV_TURN IS_OPER_INC EBITDA IS_DIL_EPS_CONT_OPS IS_SH_FOR_DILUTED_EPS CAPEX_ABSOLUTE_VALUE CF_FREE_CASH_FLOW EQY_DPS RETURN_ON_ASSET RETURN_COM_EQY`), balance-sheet panel; always pass `mnemonics` |
| `harvest_get_fundamentals(key, kind="price")` | share price on the date of pricing (last ~30 days only) |
| `harvest_get_peers_and_scores(key)`, `harvest_search_articles(key)` | context, stock reaction, broker actions in the press |

**The harvest holds no quarterly series** (no quarterly revenue, margins, EPS, segments or KPIs) and no 4E year
beyond FY3. Quarterly figures always come from the company's filings / release (section 2) or the chartbook.

## 2. The company's own quarterly numbers (primary)

- **US filers:** the 8-K Ex. 99.1 earnings release and the 10-Q. Quarterly XBRL:
  `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` (each fact has `fp` Q1/Q2/Q3/FY and `frame`
  `CY2026Q2`; Q4 = FY minus the three quarters; a script must send a descriptive `User-Agent`). Ticker -> CIK:
  `https://www.sec.gov/files/company_tickers.json`; filing list: `https://data.sec.gov/submissions/CIK##########.json`.
- **Foreign filers:** the 6-K and the company's quarterly results package (press release, financial statements,
  presentation, historical-data workbook) on its IR site; the home regulator's filing system for anything else.
- **KPIs** (ASML system sales by technology / end use / region, units, ASP; UNH medical care ratio, membership,
  premium revenue by business, segment margins): the release tables and the IR presentation.
- **Guidance**: the release and the call (transcript or the company's prepared remarks).
- **Broker actions**: reputable press (Reuters, Bloomberg, WSJ, FT, Barron's, MarketWatch, Investing.com) naming
  the firm, rating and target; mark a figure you could not confirm.

## 3. AlphaSense

Lauren's chart data and two standing AlphaSense agents feed her current workflow. Until the AlphaSense MCP is
connected for her, a series only AlphaSense holds stays a `pending` figure naming the series and the period
needed, or is read from her chart workbook / the chartbook when she supplies it. Never estimate it.

## 4. Fallback rule

If the opalgateway is unavailable, a harvest call errors, the security does not resolve, or a dataset is absent
or stale (more than 5 trading days behind T-1), use web search for that item, primary sources first (EDGAR, the
regulator, company IR), then reputable secondary sources. Never cite unsourced blogs, forums or content farms.
