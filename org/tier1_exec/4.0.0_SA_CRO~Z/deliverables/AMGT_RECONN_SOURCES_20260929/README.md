# AMGT_RECONN: holdings sources and backfill assessment

**Author:** 4.0.0_SA_CRO~Z (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO~Z/
**Recon ID:** RCN-0020
**Measured:** 2026-09-29, approximately 15:13-15:22 ET.
**Status:** Research assessment and implementation proposal; no production collector installed.

**Subsequent Bloomberg clarification:** [Guide review and live tests](BBG_GUIDES_FOLLOWUP.md) found a non-BQL top-ten holdings field working for five of six ETFs. Complete portfolios remain unproven through Bloomberg. The follow-up also exercises historical bulk overrides and the distinct custom-portfolio request operation.

## Decision

Use issuer holdings for the lightweight version. Current full-portfolio data was retrieved for all six confirmed ETFs. BASG and GQGU have publicly accessible dated files, with samples reaching their launch periods. The other four have current holdings plus periodic portfolio disclosures; a daily historical archive was not established for those four in this assessment. Start preserving daily snapshots and backfill actual available dates, capped at two years. Weekly or quarterly observations are acceptable under Andrew's revised direction; retain their actual dates.

Bloomberg's current local DAPI connection works, but its BQL service refuses holdings enumeration. The failure is not confined to beta or other characteristics. An upgrade is unnecessary to start this source-first version. Whether another Bloomberg product or an entitled Terminal/Excel surface can supply these funds' historical full portfolios remains unverified.

## Per-fund findings

| Fund | Actual current source exercised | Historical evidence | Lightweight route |
|---|---|---|---|
| WCMG — First Trust WCM Global Equity | [First Trust holdings table](https://www.ftportfolios.com/Retail/Etf/EtfHoldings.aspx?Ticker=WCMG), dated September 28: 49 rows including two cash currencies; weights total 100.02% after source rounding. | Fund began April 21, 2026. June 30 full portfolio is present in [Item 7 of its SEC report](https://www.sec.gov/Archives/edgar/data/1329377/000144554626006643/etf1-ncsrs.htm), not merely the top-ten shareholder summary. No daily historical selector established. | Parse the complete HTML table each day. Backfill the available filing snapshots; seek an issuer archive only if higher historical frequency is valuable. |
| GQGU — GQG US Equity | [Issuer-linked FilePoint](https://gqg.filepoint.live/), pipe-delimited daily files. September 28: 39 rows including cash; net-asset weights total 100.02%. | Eleven of eleven sampled dates returned matching internal dates: July 11/14, September 30 and December 31, 2025; March 31, June 30, August 31 and September 23/24/25/28, 2026. First sample predates July 14 ETF operations by one trading day and must retain that distinction. | Shared SEI/FilePoint parser with BASG; enumerate available dates from the launch period through the latest trading day. |
| TSEL — Touchstone Sands Capital US Select Growth | [Full holdings CSV](https://www.touchstoneinvestments.com/api/sitecore/TsiETFApi/GetFullHoldingsCsv?etfNumber=TUE0080): 29 rows, weights total 100%. Includes identifiers, shares, price, value and weight. | Launch around year-end 2024/January 2025; issuer materials and BBG differ by a few days. Full [March 31, 2025 portfolio](https://www.sec.gov/Archives/edgar/data/1919700/000114554925036610/tetftpartf033125.htm), [December 31, 2025 report](https://www.sec.gov/Archives/edgar/data/1919700/000110465926022224/tm266679d1_ncsr.htm), and [June 30, 2026 portfolio](https://www.sec.gov/Archives/edgar/data/1919700/000110465926103767/tm2623940d1_ncsrs.htm) located. No daily historical endpoint established. | Save the current CSV daily and pair it with the holdings date on the [fund page](https://www.touchstoneinvestments.com/etfs/sands-capital-us-select-growth-etf). Filing snapshots support periodic backfill. |
| BASG — Brown Advisory Sustainable Growth | [Issuer-linked FilePoint](https://brownadvisory.filepoint.live/Sustainable-Growth-ETF/bottom-container), same SEI-style format as GQGU. September 28: 35 rows including cash; net-asset weights total 100%. | Twelve of twelve sampled dated files retrieved, from June 13, 2025 inception through September 28, 2026. Samples include June 16/30, September 30, December 31, 2025; March 31, June 30, August 31, September 23/24/25/28, 2026. | Shared SEI/FilePoint parser; date-based backfill is demonstrated. Full intervening-day coverage still needs a census. |
| ETFT — Fundsmith Equity | [Fund page](https://www.fundsmithetf.us/) embeds a complete 29-row portfolio including cash, dated September 28; weights total 100%. The apparent CSV download returned only ten rows and is unsuitable as a full-portfolio input. | Fund inception December 1, 2025; BBG reports December 2. [December 31, 2025 full schedule](https://www.fundsmithetf.us/media/1rvdx5ey/fundsmith-equity-etf-1st-fiscal-quarter-holdings.pdf) verified; issuer also links March and June 2026 portfolio reports. No daily historical archive established. | Extract the full embedded holdings array daily; use full periodic schedules for backfill. |
| PCLG — Polen Focus Growth | [Issuer-linked FilePoint page](https://polen.filepoint.live/PCLG) consumes [PolenHoldings_.csv](https://polen.filepoint.live/assets/data/PolenHoldings_.csv). Filter Basket Name = Polen Focus Growth ETF: 29 rows, weights approximately 100%. File execution timestamp September 28, 18:39:53; includes quantity, identifiers, value, ETF shares outstanding and net assets. | ETF began September 30, 2025. [January 31, 2026 full portfolio](https://www.polencapital.com/sites/default/files/Polen%20ETF%20Funds%201.31.26%20N-PORT.pdf) verified; [April 30, 2026 report](https://www.sec.gov/Archives/edgar/data/1388485/000119312526299551/d112667dncsr.htm) contains the portfolio. No daily historical file archive established. | Capture the current CSV daily; use periodic disclosures for backfill. Verify holdings-effective date separately from file execution time. |

Denominators: six issuer current portfolios retrieved; seven BQL queries (six funds plus IBM control); ordinary reference requests for six funds plus SPY; SPX index positive control; 23 dated issuer-file samples across BASG/GQGU. This is a source feasibility sample, not an exhaustive historical coverage census or an installed production pipeline.

All six ETF vehicles have less than two years of operating history. GQGU's issuer explicitly carries predecessor performance from 2019, while ETF operations commenced July 14, 2025. A performance predecessor does not establish accessible historical holdings and is not silently stitched into ETF history. [Issuer explanation](https://gqg.filepoint.live/).

## Bloomberg: what the live test actually establishes

- `//blp/refdata` connected successfully. NAME, ISIN and inception fields returned for all six. Reported holdings counts differed from the issuer snapshots; GQGU even returned zero. These scalar values are not a portfolio dataset.
- `//blp/bqlsvc` returned **User not authorized to use BQL** for each `get(id().weights)for(holdings('<ticker> US Equity'))` request and the unrelated `get(px_last)for(['IBM US Equity'])` control. This demonstrates a service authorization refusal before fund coverage or query suitability can be assessed.
- `INDX_MEMBERS` and `INDX_MWEIGHT_HIST` returned field-not-applicable-to-security for all six ETFs and SPY. `INDX_MEMBERS` returned 503 constituents for **SPX Index** as a positive control. Index constituents are not the actively managed ETF portfolios we need.
- BQL is a query interface, not synonymous with characteristics. The currently blocked route is relevant to holdings. These tests do not prove that every Bloomberg product lacks a route, nor establish the cost or availability of an entitlement change. The old repo runbook's universal claims are broader than this bounded result.

If Bloomberg consolidation is pursued later, ask support to demonstrate constituent identifier, quantity, weight and actual holdings date for these six tickers on recent and historical dates using this account's permitted API. A generic claim that Bloomberg has ETF data or historical prices is insufficient.

## Concrete issuer retrieval mechanisms

```text
BASG: https://brownadvisory.filepoint.live/assets/data/SEI_Brown_Tradedate_Holdings_MMDDYYYY.txt
GQGU: https://gqg.filepoint.live/assets/data/SEI_GQG_Tradedate_Holdings_MMDDYYYY.txt
TSEL: https://www.touchstoneinvestments.com/api/sitecore/TsiETFApi/GetFullHoldingsCsv?etfNumber=TUE0080
PCLG: https://polen.filepoint.live/assets/data/PolenHoldings_.csv
WCMG: https://www.ftportfolios.com/Retail/Etf/EtfHoldings.aspx?Ticker=WCMG
ETFT: https://www.fundsmithetf.us/ (top-ten-holdings-table element, :holdings attribute contains full array)
```

The BASG/GQGU filename patterns were read from the sites' own JavaScript, then exercised on real dates; they were not inferred from fund names. For example, [BASG June 13, 2025](https://brownadvisory.filepoint.live/assets/data/SEI_Brown_Tradedate_Holdings_06132025.txt) and [GQGU July 11, 2025](https://gqg.filepoint.live/assets/data/SEI_GQG_Tradedate_Holdings_07112025.txt) both returned fund rows with matching internal dates.

Source details that affect correctness:

- SEI files carry both `percent_of_market_value` and `percent_of_net_assets`. Use and label the latter for portfolio weights, matching both issuer renderers. The former summed above 100% when cash was included; that was a denominator mismatch, not missing holdings.
- Preserve actual identifiers from raw columns. Brown's generated CSV labels one column CUSIP while its JavaScript populates it with ISIN; the raw file has both correctly named fields.
- PCLG calls fields Basket Name/Quantity, but this is the exact file its issuer uses for portfolio holdings and it also carries total net assets and ETF shares. Retain those semantics; do not substitute an arbitrary creation/redemption basket file.
- TSEL's CSV lacks an internal date column. Capture the page's holdings date alongside the CSV; do not substitute retrieval date or the separate historical NAV date.
- Avoid imposing Bloomberg's reported holdings count as a hard validator. Check source completeness, cash handling and weight basis instead.

## Proposed small first version

One scheduled Site-Z job, one manifest of six funds and about five parser families: SEI/FilePoint shared by BASG/GQGU; Polen CSV; Touchstone CSV; First Trust HTML; Fundsmith embedded JSON. Existing Opal issuer-to-holdings patterns are a reference for reuse, not evidence that these six adapters already exist.

Keep the downloaded bytes and source URL/hash in bronze. Produce one typed holdings table in silver: fund identifier, portfolio date, observation time, security identifier/name, quantity, value, weight and weight basis, cash/security type, source and observed frequency. Add fund net assets and shares outstanding when supplied. Deliver CSV/Parquet tables for Andrew to explore; beta, an AI service and a dashboard are not first-version dependencies.

Backfill order: (1) census BASG/GQGU dated files and retain successful actual dates; (2) inventory and extract full portfolio disclosures for the other four, beginning with the concrete reports above; (3) if the resulting historical frequency is insufficient, seek issuer archives or a vendor sample. No known continuous daily backfill for all six is claimed.

Public N-PORT and financial statements are suitable periodic holdings evidence, not a method to reconstruct unobserved daily trades. More frequent N-PORT publication requirements were delayed to 2027/2028; do not assume monthly public history from the 2024 announcement. [SEC extension](https://www.sec.gov/newsroom/press-releases/2025-64).

A commercial fallback exists: [Intrinio's holdings API](https://data.intrinio.com/documentation/web_api/get_etf_holdings_v2) documents historical `as_of_date` requests, which require historical entitlements and may return the nearest preceding snapshot. Coverage, frequency and price for these six were not tested. It is a candidate to qualify only if issuer/filing history proves inadequate.

Preserve sparse history as sparse history. A weight change is not by itself a buy/sell: prices, FX, flows and corporate actions can move it. Quantity and fund shares outstanding, when available, leave a path to separating manager changes later without expanding this initial holdings-collection scope.

## Evidence and reproduction

Raw captures and read-only probe scripts are local under `.runtime/amgt-reconn-sources-20260929/`, excluded from this commit. Principal evidence: `bbg_reference.json`, `bbg_spx_control.json`, `bql_*.txt`, `issuer_pages.json`, `dated_probe_results.json`, `historical_samples.json`, `row_validation.json`, plus fetched HTML/JS/CSV and dated files. `sample_validation.json` retains an exploratory market-value-weight sum; the net-asset-weight correction above supersedes that denominator. No raw licensed Bloomberg responses were committed.

Reproduction: the `probe_bbg.py`, `probe_issuers.py`, `probe_downloads.py`, `probe_dated.py`, and `probe_history.py` scripts in that local directory issue read-only requests and save captures there. The mechanism URLs and parsing requirements above are the durable source map. No purchase, external correspondence, scheduled task or cloud write occurred.
