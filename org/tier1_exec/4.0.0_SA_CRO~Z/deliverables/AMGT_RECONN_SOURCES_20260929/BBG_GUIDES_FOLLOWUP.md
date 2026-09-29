# Bloomberg API guides: holdings follow-up

Author: 4.0.0_SA_CRO~Z. Measured September 29, 2026, approximately 15:30-15:36 ET. Extends RCN-0020.

## Result

No complete ETF portfolio route demonstrated. However, ordinary Bloomberg reference data DOES enumerate the top ten holdings for five of the six ETFs. Any earlier statement that Bloomberg cannot enumerate any holdings without BQL is too broad. The supported conclusion is that we have not obtained FULL holdings for these six through the tested non-BQL API routes.

## What the supplied documents establish

- Local `BLPAPI-Core-User-Guide.pdf`: 38 pages, version 1.5, dated May 19, 2016. Page 31 describes field discovery and documentation through `//blp/apiflds`, and field-specific overrides. Page 34 describes service schemas.
- Local `BLPAPI-Core-Developer-Guide.pdf`: 106 pages, version 1.6, dated August 30, 2016. Pages 29, 34 and 37 distinguish scalar reference, bulk reference and historical time series. Pages 46-48 document field information/search. Pages 91-92 explicitly map Excel BDS to `ReferenceDataRequest` on `//blp/refdata`; BDS is not a separate API access route.
- These are generic API mechanics guides, not an ETF coverage catalog. Their age makes live field documentation and request results material. Bloomberg's [API Library](https://professional.bloomberg.com/support/api-library/) still lists the Core guides.

## Live exercises prompted by the guides

### Field discovery and partial holdings

Six searches (`fund holdings`, `portfolio holdings`, `ETF holdings`, `constituents`, `fund portfolio`, `holdings`) returned 2,419 distinct field records. This is a search result union, NOT an exhaustive dictionary census. Additional targeted searches covered portfolio IDs, portfolio members and holdings dates.

`TOP_MUTUAL_FUND_HOLDINGS` is documented as limited to ten holdings. It returned ten rows for WCMG, TSEL, BASG, ETFT and PCLG, plus the SPY control. GQGU returned field-not-applicable. Rows include security name/ticker, position, value, change, percentage of fund assets and filing date. WCMG/TSEL/BASG/ETFT rows were dated September 28; PCLG rows were dated September 29. The field documentation lists no overrides. No pagination or historical extension was established. This is useful partial data but fails the full-portfolio requirement.

Other candidate semantics do not solve the task: `CURRENT_PORTFOLIO_LIST`/`HISTORICAL_PORTFOLIO_LIST` are documented for private equity funds. The current-list field rejected all six ETFs and SPY. Holdings-based allocation fields describe aggregate exposures; holder lists describe ownership of a security, not necessarily the securities held by the ETF. `HLDG_WITH_DIR_EXPSR_DIG_ASSTS` is only a subset exposed to digital assets.

### Historical bulk data

Live documentation for `INDX_MWEIGHT_HIST` explicitly permits `END_DT` or `END_DATE_OVERRIDE`. This is a concrete demonstration that some historical bulk snapshots use a reference request with an override rather than a `HistoricalDataRequest`.

Tested `ReferenceDataRequest` + `INDX_MWEIGHT_HIST` + `END_DATE_OVERRIDE` for June 30 and September 28, 2026. Both dates returned 503 constituents for SPX Index; all twelve ETF/date combinations returned field-not-applicable. Thus the date-override mechanism works, but this field's index scope does not yield these ETF portfolios. Failure of BDH alone would not establish absence of all bulk history.

### A distinct portfolio operation

The live `//blp/refdata` schema exposes `PortfolioDataRequest`. A separate official Bloomberg [Developer's Guide v2.54](https://data.bloomberglp.com/professional/sites/4/blpapi-developers-guide-2.54.pdf), sections 7.2.5 and A.2.10 (printed pages 86 and 178), specifies a user's PRTU portfolio ID, portfolio fields and historical `REFERENCE_DATE` override. The live field descriptions for `PORTFOLIO_MEMBERS`, `PORTFOLIO_MPOSITION` and `PORTFOLIO_MWEIGHT` also explicitly say user custom portfolio.

Tested `PortfolioDataRequest` / `PORTFOLIO_DATA` with all six ordinary ETF tickers: six `BAD_SEC / INVALID_SECURITY` responses. This establishes that direct ETF-ticker substitution does not work. It does NOT establish whether an entitled, Bloomberg-maintained portfolio identifier for these ETFs exists. No suitable custom-portfolio identifier was available as a positive control, and no historical custom-portfolio request was claimed successful. Importing issuer holdings into a custom portfolio would require already possessing the source data and would not solve sourcing.

## Consequence and remaining question

The supplied docs provide real investigative leads, but do not establish a full-portfolio entitlement workaround. BQL's prior service-level authorization refusal remains unresolved. A precise Bloomberg support question is: can this login access complete holdings for these six ETFs, with actual portfolio dates and historical snapshots, through BQL or a supported portfolio-ID/API route; and if BQL is refused, is enablement/configuration or additional licensing required? Nothing in this assessment establishes that a purchase is necessary. No support message was sent.

Issuer full holdings remain the demonstrated working source. The new top-ten result does not replace it. Generic enterprise Data License offerings do not establish account access, coverage or price for these six funds.

## Evidence

Local raw evidence, not committed: `.runtime/amgt-reconn-bbg-guides-20260929/`. Extracted page text and JSON for both PDFs; `probe_fields.py`, `all_fields.json`, `probe_candidates.py`, `candidate_docs.json`, `current_candidates.json`, `historical_bulk_20260630.json`, `historical_bulk_20260928.json`, `portfolio_schema.txt`, `portfolio_etf_test.json`, and targeted search responses. Raw portfolio rows remain local. All operations were read-only; no production changes, orders, purchases, messages or account-permission changes.
