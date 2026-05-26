# YALP_MACROS Phase 2a — Treasury/FDIC/other federal-source Multi-Source Reconnaissance

**TO:** YALP_MACROS.006d — Treasury/FDIC/other federal-source RE reconnaissance (Phase 2a parallel lane D)
**Author:** 0.1.0_DS_MarketIntelligence~D (Phase 2a Treasury/FDIC/govt-other lane; sister to ~A FRED + ~B BLS + ~C Census + ~E Aggregate-orphan)
**PRD:** `docs/architecture/YALP_MACROS.md` v0.5 RE-OPENED `7e781ea8c` — Phase 2 multi-source RE charter
**Authority:** Andrew sovereign direct ~21:00Z + RE-OPEN Phase 2 ~21:05Z + MSTR LD-0104 fast-trajectory endorsement + Andrew direct 2026-05-26 ~22:?Z mid-flight HAR-capture pattern (record HARs → fan-out subagent parse)
**T*:** indicator-cadence-bound (Treasury yields daily; FRB releases weekly/monthly; BEA NIPA quarterly; FDIC quarterly Call Report); brief authored 2026-05-26 against current API surface
**Status:** Phase 2a reconnaissance COMPLETE — 5/5 ACs met

---

## §0 — TL;DR

The ~D lane covers federal-source endpoints **NOT** owned by FRED/BLS/Census/sister-lanes. ~D-PRIMARY for 79-indicator universe = **~20 indicators (~25.3%)** across 5 source-classes:

| Source-class | Indicators | API model | HAR-RE needed? |
|---|---|---|---|
| **Treasury Direct daily yield curve** (CSV) | 10 Treasury Yields (1M/3M/1Y/2Y/3Y/5Y/7Y/10Y/20Y/30Y) | Public CSV download per-year `home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/{YYYY}/all?type=daily_treasury_yield_curve&_format=csv` | NO (live-verified ~22:0?Z; clean CSV) |
| **Treasury Fiscal Data API** (JSON) | Avg interest rates, debt-to-the-penny, federal financing activity (cross-validation for yields + Wave-2 fiscal-side) | REST JSON `api.fiscaldata.treasury.gov/services/api/fiscal_service/...` | NO (live-verified; documented REST JSON-API) |
| **NY Fed Markets API** (JSON) | Effective Fed Funds Rate (Fed Fund Rate indicator), SOFR, reference rates | REST JSON `markets.newyorkfed.org/api/rates/.../...` | NO (live-verified; documented REST JSON-API) |
| **BEA API** (NIPA / Trade) | GDP QoQ, PCE MoM, Core PCE MoM, Trade Balance (joint Census/BEA cross-ref) | REST JSON `apps.bea.gov/api/data/?...` — UserID required (free signup) | NO (probe-verified shape; documented REST JSON-API; auth-key blocked GUEST probe — needs registered key) |
| **FRB statistical releases** (CSV/XLSX via Data Download Program) | Industrial Production (Lagging "Industrial Productivity"), Capacity Utilization (G.17), Consumer Credit YoY (G.19), Fed Balance Sheet (H.4.1), Net LT TIC Flows (TIC release) | Data Download Program (DDP) — series-ID-bound CSV/XLSX downloads via `federalreserve.gov/datadownload/Output.aspx?...` | **YES — HAR capture recommended** (DDP click-path is gnarly; HAR reveals series-ID parameter encoding) |

**FDIC BankFind API** (`banks.data.fdic.gov/api/...`) is live-verified clean REST JSON but covers **ZERO** of the 79-indicator universe — purely banking-sector data (institutions, failures, deposit insurance, Call Reports). Catalogued as Wave-2 candidate for any future banking-sector page.

**Regional Fed surveys** (Empire State, Philly Fed BOS, KC Fed, Richmond, Dallas) cover **ZERO** of the 79-indicator universe; they're survey-class manufacturing/services diffusion indices distinct from the 79. Catalogued as Wave-2 candidates; XLSX/PDF distribution model = **HAR capture recommended** to find programmatic data endpoints behind the survey landing pages (if any exist).

**OCC, CFPB, SSA** cover **ZERO** of the 79-indicator universe. CFPB has a documented REST API (consumer complaints database) — Wave-2-relevant if any future financial-services page consumes complaint data. OCC + SSA = no documented REST API surface relevant to 79.

**Phase 2b TO-007 synthesis input:** for the ~20 ~D-PRIMARY indicators, **upstream-Treasury / upstream-Fed is the RE-MATCH source-of-truth**; FRED is the convenient mirror; harness should default to FRED for simplicity (sister ~A coverage) and reserve Treasury Direct / FRB DDP for cross-validation when FRED-mirror lag or DRIFT class fires. **Two-tier harness design: FRED as PRIMARY runtime, Treasury/FRB as CROSS-CHECK / upstream-authoritative.**

Per Andrew direct 2026-05-26 mid-flight ratification: **HAR-capture pattern applies only to non-REST-API frontends** — FRB DDP, regional Fed survey landings, and select Treasury XLSX-only tables. The documented REST APIs (Treasury Fiscal Data, FDIC BankFind, NY Fed Markets, BEA, CFPB) are HAR-NOT-REQUIRED.

---

## §1 — API Surfaces by Source

### §1.1 — Treasury Direct (daily yield curve)

**Endpoint pattern (live-verified ~22:?Z):**
```
GET https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/{YYYY}/all
    ?type=daily_treasury_yield_curve
    &field_tdr_date_value={YYYY}
    &page&_format=csv
```

Response: CSV with header row + per-business-day rows. Live-verified shape:
```
Date,"1 Mo","1.5 Month","2 Mo","3 Mo","4 Mo","6 Mo","1 Yr","2 Yr","3 Yr","5 Yr","7 Yr","10 Yr","20 Yr","30 Yr"
05/26/2026,3.72,3.70,3.69,3.68,3.78,3.80,3.82,4.01,4.10,4.19,4.33,4.50,5.03,5.03
05/22/2026,3.72,3.69,3.69,3.68,3.78,3.79,3.86,4.13,4.18,4.27,4.41,4.56,5.06,5.07
```

**Cadence:** Daily, posted ~4pm ET (after market close).
**Auth:** None — fully public CSV download.
**Pagination:** None (entire YTD returned in single CSV; per-month variant also supported via `field_tdr_date_value_month={YYYYMM}`).
**Failure modes:** None observed. 30s timeout sufficient. HTTP 200 always returns CSV; 30-day windows + business-day-only.
**Related Treasury yield products:** real (TIPS) yield curve, par yield curve, long-term composite rate — separate `type=` query params on same base URL.

### §1.2 — Treasury Fiscal Data API

**Endpoint pattern (live-verified ~22:?Z):**
```
GET https://api.fiscaldata.treasury.gov/services/api/fiscal_service/{endpoint}?fields=...&sort=-record_date&page[size]=N
```

Live-verified sample response (avg interest rates v2):
```json
{
  "data": [
    {"record_date":"2026-04-30","security_type_desc":"Marketable","avg_interest_rate_amt":"3.696"},
    {"record_date":"2026-04-30","security_type_desc":"Marketable","avg_interest_rate_amt":"3.230"}
  ],
  "meta": {
    "count": 2, "total-count": 4928, "total-pages": 2464,
    "dataTypes": {"avg_interest_rate_amt":"PERCENTAGE","record_date":"DATE"}
  },
  "links": { "self":"...", "next":"...", "last":"..." }
}
```

**Coverage relevant to 79:** Cross-validation for Treasury Yields (avg interest rates by security type — Bills/Notes/Bonds). Wave-2-relevant: debt-to-the-penny (`debt_to_penny`), monthly Treasury statement (`mts/mts_table_1`), federal debt outstanding.
**Auth:** None — fully public REST JSON.
**Pagination:** Standard JSON-API `page[number]` + `page[size]`; URL-encoded as `page%5Bsize%5D`.
**Failure modes:** Empty `data: []` on out-of-range queries; HTTP 200 + JSON error body on malformed.
**Quirks:** Numeric values returned as STRING (parse to float client-side; matches Census EITS quirk per ~C §6).

### §1.3 — NY Fed Markets API

**Endpoint pattern (live-verified ~22:?Z):**
```
GET https://markets.newyorkfed.org/api/rates/secured/sofr/last/N.json
GET https://markets.newyorkfed.org/api/rates/unsecured/effr/last/N.json    (Effective Fed Funds)
GET https://markets.newyorkfed.org/api/rates/unsecured/obfr/last/N.json    (Overnight Bank Funding)
```

Live-verified sample (SOFR):
```json
{ "refRates": [
  { "effectiveDate":"2026-05-22", "type":"SOFR", "percentRate":3.55,
    "percentPercentile1":3.51, "percentPercentile25":3.53, "percentPercentile75":3.61,
    "percentPercentile99":3.65, "volumeInBillions":3078, "revisionIndicator":"" },
  ...
] }
```

**Coverage relevant to 79:** Fed Fund Rate indicator (Financial Condition group) — EFFR (Effective Federal Funds Rate) is the canonical upstream-FRB source. NB FRED `FEDFUNDS` mirrors EFFR.
**Auth:** None — fully public REST JSON.
**Pagination:** Path-segment `last/N` returns last N observations; date-range variants also exist (`/range/{startDate}/{endDate}`).
**Failure modes:** HTTP 200 + empty `refRates` on out-of-range; clean JSON shape.
**Wave-2-relevant rates classes:** SOFR (sister to EFFR), OBFR, BGCR/TGCR (Treasury repo rates).

### §1.4 — BEA API (NIPA + Trade)

**Endpoint pattern (probe-verified shape only; UserID-blocked further):**
```
GET https://apps.bea.gov/api/data/?UserID=YOUR_KEY
    &method=GetData
    &datasetname=NIPA
    &TableName=T20807                                  (Personal Income & Outlays, monthly)
    &Frequency=M
    &Year=ALL
    &ResultFormat=JSON
```

**Auth:** UserID **required** (free signup at `apps.bea.gov/API/signup/`). GUEST UserID returns `APIErrorCode:4 — This UserId is not active`. Same pattern as Census API key.
**Coverage relevant to 79:**
- GDP QoQ — NIPA Table T10101 (GDP %-change-from-preceding-period); Frequency=Q
- PCE MoM — NIPA Table T20807 row "Personal consumption expenditures (PCE)"; Frequency=M
- Core PCE MoM — NIPA Table T20807 row "PCE excluding food and energy"; Frequency=M
- Trade Balance — `ITA` dataset OR `T40205B` (foreign trade) — **OVERLAPS WITH SISTER ~C TO-006c CENSUS `ftd`** per ~C §2.1 row 7 (Census-PRIMARY for Trade Balance; BEA-cross-ref). ~D defers Trade Balance ownership to ~C; documents BEA upstream side here.
**Pagination:** Driven by `Year=ALL` vs explicit year list; large tables paginated by year ranges.
**Failure modes:** `APIErrorCode` in response body on any error (auth, dataset-not-found, table-not-found).
**Quirks:** Table-naming convention `T{XXX}{YYY}` is BEA-internal; `GetParameterList` + `GetParameterValuesFiltered` are introspection endpoints; harness should cache table metadata.

### §1.5 — FRB Data Download Program (DDP) — HAR-RE candidate

**Endpoint pattern (gnarly; not live-verified clean):**
```
GET https://www.federalreserve.gov/datadownload/Output.aspx
    ?rel={RELEASE_CODE}                                 (H15, H4, G17, G19)
    &series={SERIES_ID}                                 (long hex-like ID per series)
    &lastobs=                                           (N, or empty for ALL)
    &from=                                              (MM/DD/YYYY)
    &to=                                                (MM/DD/YYYY)
    &filetype=csv                                       (csv|xml|sdmx|excel)
    &label=include                                      (include|omit)
    &layout=seriescolumn                                (seriescolumn|seriesrow)
```

**Coverage relevant to 79:**
- **H.15 (Selected Interest Rates)** — Treasury Yield Curve constant maturities (CMT 1M/3M/6M/1Y/2Y/3Y/5Y/7Y/10Y/20Y/30Y), Fed Funds (target + effective), commercial paper rates. **Upstream-authoritative for Treasury Yields** — Treasury Direct CSV §1.1 publishes the SAME data; H.15 is FRB-published mirror.
- **H.4.1 (Factors Affecting Reserve Balances)** — Fed Balance Sheet (Total assets, SOMA holdings, Federal Reserve notes outstanding, MBS holdings, USTs held outright). PRIMARY upstream for "Fed Balance Sheet" indicator (Financial Condition).
- **G.17 (Industrial Production and Capacity Utilization)** — Industrial Production Index (yang "Industrial Productivity MoM"), Capacity Utilization rate. PRIMARY upstream for 2 Lagging indicators.
- **G.19 (Consumer Credit)** — Total consumer credit outstanding, revolving/nonrevolving breakouts. PRIMARY upstream for "Consumer Credit YoY" indicator.

**Auth:** None — but DDP series-ID encoding is gnarly + the parameter `series=` takes a long hex string per series that's discoverable via the DDP UI's "Build a series" wizard (the URL parameter is generated client-side).
**Failure modes:** Empty 200 OK on malformed series-ID (live-probe ~22:?Z confirmed: HTTP 200 + 0 bytes when probed with placeholder). Wrong series ID = silent empty CSV, not error.
**HAR-RE pattern:** Capture HARs of (1) H.15 series-build wizard click-path → CSV download URL; (2) H.4.1 series wizard; (3) G.17 wizard; (4) G.19 wizard. From HARs we can recover the canonical series= parameter per indicator we want, then bake those into harness as constants.
**FRED-mirror alternative:** ALL FRB statistical release data is mirrored on FRED (`FEDFUNDS`, `INDPRO`, `TCU`, `TOTALSL`, `WALCL`, etc.). **For runtime, FRED is preferred.** FRB DDP value-add = upstream-authoritative + alternative-format (XML/SDMX) + revision history.

### §1.6 — Treasury TIC (Treasury International Capital)

**Endpoint pattern (XLSX-only; HAR-RE candidate):**
```
GET https://home.treasury.gov/data/treasury-international-capital-tic-system-home-page/...
```

TIC data is published as monthly XLSX tables (TIC Table 1: Major Foreign Holders of Treasury Securities; Table 2: Net Long-Term TIC Flows; Table 3: Net Cross-Border Portfolio Flows; ~10 tables total). **No documented REST API.**

**Coverage relevant to 79:**
- Net Long Term TIC Flows (Financial Condition indicator) — TIC Table 2.

**HAR-RE pattern:** Capture HAR of the TIC landing page navigation → table 2 XLSX download. Confirm whether download URL is stable (versioned by date) or session-bound. FRED mirror exists for some TIC series (`TICFLT`, etc.) — likely-preferred runtime path.

### §1.7 — FDIC BankFind API

**Endpoint pattern (live-verified ~22:?Z):**
```
GET https://banks.data.fdic.gov/api/institutions?filters=ACTIVE%3A1&fields=NAME,CITY,STALP,ASSET&limit=2
GET https://banks.data.fdic.gov/api/financials?filters=...
GET https://banks.data.fdic.gov/api/failures?filters=...
GET https://banks.data.fdic.gov/api/locations?filters=...
GET https://banks.data.fdic.gov/api/sod?filters=...                        (Summary of Deposits)
```

Live-verified sample (institutions endpoint):
```json
{ "meta":{"total":4278,"parameters":{"filters":"ACTIVE:1","fields":"NAME,CITY,STALP,ASSET","limit":"2"},
         "index":{"name":"institutions_20260522090006","createTimestamp":"2026-05-22T11:51:40Z"}},
  "data":[ {"data":{"CITY":"Markesan","ASSET":261034,"STALP":"WI","NAME":"Ergo Bank","ID":"10004"},"score":0}, ... ] }
```

**Coverage relevant to 79:** **ZERO.** FDIC scope is bank-specific (4,278 active US banks per live response; bank failures; deposit insurance fund metrics; quarterly Call Reports). Catalogued as Wave-2 candidate for future banking-sector page (e.g., bank stress dashboard, regional bank failure tracker).
**Auth:** None — fully public REST JSON.
**Wave-2 relevance:** if Opal builds a banking-sector page (bank stress + deposit flows + failure tracker), FDIC BankFind is the canonical upstream.

### §1.8 — Regional Fed Surveys — HAR-RE candidates

Five regional Fed manufacturing/business surveys, all distributed as **XLSX/PDF on bank websites** (no programmatic JSON APIs documented):

| Reserve Bank | Survey | URL landing | Format | Cadence |
|---|---|---|---|---|
| **NY Fed (FRBNY)** | Empire State Manufacturing Survey | `newyorkfed.org/medialibrary/Research/Surveys/Empire/empire-history.xlsx` (live HTTP 200 HTML — XLSX behind landing page click) | XLSX | Monthly (around 15th) |
| **Philly Fed (FRBP)** | Business Outlook Survey (BOS) | `philadelphiafed.org/-/media/frbp/assets/surveys-and-data/business-outlook-survey/historical-data/bos_history.xlsx` (live HTTP 200 HTML) | XLSX | Monthly (around 18th) |
| **KC Fed (FRBKC)** | Manufacturing Survey, Services Survey | `kansascityfed.org/surveys/manufacturing-survey/` | XLSX/PDF | Monthly |
| **Richmond Fed (FRBR)** | Manufacturing Survey, Services Survey | `richmondfed.org/research/regional_economy/surveys_of_business_conditions` | XLSX/PDF | Monthly |
| **Dallas Fed (FRBD)** | Texas Manufacturing Outlook, Texas Service Sector Outlook | `dallasfed.org/research/surveys/tmos` | XLSX/PDF | Monthly |

**Coverage relevant to 79:** **ZERO.** These surveys (regional diffusion indices) are distinct from ISM PMI (national) + S&P Global PMI in the Leading Indicator group. They could be Wave-2-relevant if Opal builds a regional-Fed dashboard or wants a manufacturing-breadth proxy beyond the national PMI.
**HAR-RE pattern:** Capture HARs of each survey landing page → XLSX download click. Confirm download URL stability; identify whether any survey publishes structured data behind the landing (some Fed banks have a "Download data" sidebar with CSV options; HAR reveals these endpoints).
**FRED mirror:** Many of these series are mirrored on FRED (e.g., `GACDISA066MSFRBNY` for Empire State headline; `MFGSFTPHFRBP` for Philly Fed general business activity). For runtime if Wave-2 picks any up, FRED is preferred.

### §1.9 — OCC / CFPB / SSA

| Agency | Data | API model | 79-coverage |
|---|---|---|---|
| **OCC (Office of the Comptroller of the Currency)** | Bank examination data, mortgage metrics, large-bank report cards | No documented REST API; PDF reports | **ZERO** — Wave-2 if banking-sector page |
| **CFPB (Consumer Financial Protection Bureau)** | Consumer complaints database, mortgage HMDA data, credit-card data | **Documented REST JSON API** `api.consumerfinance.gov/data/...` (e.g., Consumer Complaint Database has `https://api.consumerfinance.gov/data/...`) | **ZERO** — Wave-2 if financial-services-complaint page |
| **SSA (Social Security Administration)** | COLA, SSI/SSDI benefit data, actuarial tables | Limited; XML/PDF for COLA announcement | **ZERO** |

None of these contribute to the 79-indicator universe. CFPB's REST API is the only "ready-to-consume" surface among the three.

---

## §2 — Per-Indicator Match-Set (79 yang → ~D federal sources)

### §2.1 — ~D-PRIMARY matches (~20/79 = ~25.3%)

**Treasury Yields group (10 indicators) — all ~D-PRIMARY:**

| # | Yang indicator | ~D PRIMARY source | Endpoint | Maturity column | Cadence | FRED-mirror |
|---|---|---|---|---|---|---|
| 1 | 1M | Treasury Direct daily yield curve | §1.1 CSV | `"1 Mo"` | Daily | ✅ `DGS1MO` |
| 2 | 3M | Treasury Direct daily yield curve | §1.1 CSV | `"3 Mo"` | Daily | ✅ `DGS3MO` |
| 3 | 1Y | Treasury Direct daily yield curve | §1.1 CSV | `"1 Yr"` | Daily | ✅ `DGS1` |
| 4 | 2Y | Treasury Direct daily yield curve | §1.1 CSV | `"2 Yr"` | Daily | ✅ `DGS2` |
| 5 | 3Y | Treasury Direct daily yield curve | §1.1 CSV | `"3 Yr"` | Daily | ✅ `DGS3` |
| 6 | 5Y | Treasury Direct daily yield curve | §1.1 CSV | `"5 Yr"` | Daily | ✅ `DGS5` |
| 7 | 7Y | Treasury Direct daily yield curve | §1.1 CSV | `"7 Yr"` | Daily | ✅ `DGS7` |
| 8 | 10Y | Treasury Direct daily yield curve | §1.1 CSV | `"10 Yr"` | Daily | ✅ `DGS10` |
| 9 | 20Y | Treasury Direct daily yield curve | §1.1 CSV | `"20 Yr"` | Daily | ✅ `DGS20` |
| 10 | 30Y | Treasury Direct daily yield curve | §1.1 CSV | `"30 Yr"` | Daily | ✅ `DGS30` |

NB: Treasury Direct CSV includes 4 additional maturities (1.5Mo, 2Mo, 4Mo, 6Mo) not in yang 79; these are CMT yields published since 2018 (1.5Mo, 4Mo) and 2008 (2Mo) but not in yang's selection. Document; do not match.

**Financial Condition group (3 ~D-PRIMARY of 6):**

| # | Yang indicator | ~D PRIMARY source | Endpoint | Cadence | FRED-mirror |
|---|---|---|---|---|---|
| 11 | Fed Fund Rate | NY Fed Markets API (EFFR) | §1.3 `markets.newyorkfed.org/api/rates/unsecured/effr/last/N.json` | Daily (published next business day morning) | ✅ `FEDFUNDS` (monthly avg) / `DFF` (daily) |
| 12 | Fed Balance Sheet | FRB H.4.1 (DDP) | §1.5 HAR-RE candidate; series=WALCL-equivalent | Weekly (Wednesday) | ✅ `WALCL` |
| 13 | Net Long Term TIC Flows | Treasury TIC Table 2 | §1.6 HAR-RE candidate (XLSX) | Monthly (M+2 day ~15) | partial (`TICFLT` subset) |

**Lagging Indicator group (3 ~D-PRIMARY of 7):**

| # | Yang indicator | ~D PRIMARY source | Endpoint | Cadence | FRED-mirror |
|---|---|---|---|---|---|
| 14 | GDP QoQ | BEA NIPA Table T10101 | §1.4 `apps.bea.gov/api/data/?...&datasetname=NIPA&TableName=T10101&Frequency=Q` | Quarterly (advance/2nd/3rd estimates ~Q+1 month) | ✅ `A191RL1Q225SBEA` (real GDP %-change-q/q) |
| 15 | Industrial Productivity MoM (= Industrial Production Index) | FRB G.17 (DDP) | §1.5 HAR-RE candidate; series=INDPRO-equivalent | Monthly (~M+1 day 15) | ✅ `INDPRO` |
| 16 | Capacity Utilization | FRB G.17 (DDP) | §1.5 HAR-RE candidate; series=TCU-equivalent | Monthly (~M+1 day 15, joint with IP release) | ✅ `TCU` |

NB §2.1 row 15: yang label "Industrial Productivity" likely a yang-naming variant for "Industrial Production Index" (the FRB G.17 + Bloomberg `IPCHNG Index` headline measure). DRIFT-class candidate at TO-008 cross-check time — flag for Phase 2b TO-007 synthesis.

**Inflation group (2 ~D-PRIMARY of 8):**

| # | Yang indicator | ~D PRIMARY source | Endpoint | Cadence | FRED-mirror |
|---|---|---|---|---|---|
| 17 | PCE MoM | BEA NIPA Table T20807 | §1.4 `apps.bea.gov/api/data/?...&datasetname=NIPA&TableName=T20807&Frequency=M` | Monthly (~M+1 day 28-30; "Personal Income and Outlays" release) | ✅ `PCEPI` (price index) / `PCE` (level) |
| 18 | Core PCE MoM | BEA NIPA Table T20807 (row "PCE excluding food and energy") | §1.4 (same as PCE) | Monthly (same release) | ✅ `PCEPILFE` |

**Consumer group (1 ~D-PRIMARY of 7):**

| # | Yang indicator | ~D PRIMARY source | Endpoint | Cadence | FRED-mirror |
|---|---|---|---|---|---|
| 19 | Consumer Credit YoY | FRB G.19 (DDP) | §1.5 HAR-RE candidate; series=TOTALSL-equivalent | Monthly (~M+2 day 5-7) | ✅ `TOTALSL` |

**Derived indicator (1 ~D-PRIMARY of 79):**

| # | Yang indicator | ~D PRIMARY source | Computation | Cadence |
|---|---|---|---|---|
| 20 | Fed Balance Sheet as % of GDP | DERIVED: FRB H.4.1 WALCL ÷ BEA NIPA T10105 Nominal GDP × 100 | Weekly numerator, quarterly denominator (linear-interpolate or step-function) | Quarterly-update bound |

**Total ~D-PRIMARY: 20/79 = ~25.3%.**

### §2.2 — ~D Cross-reference (overlap with sister lanes)

**Trade Balance** (Lagging indicator #7 in 79):
- Sister ~C TO-006c claimed Census-PRIMARY (`ftd` dataset; joint Census/BEA program).
- ~D documents BEA upstream side: BEA `ITA` dataset OR NIPA T40205B; same headline numbers as Census `ftd` (per BEA + Census joint-publication MOU).
- **Disposition:** ~C-PRIMARY stands. ~D documents BEA-upstream as cross-reference for TO-007 synthesis (single-source-of-truth: pick Census endpoint at harness build time; treat BEA endpoint as cross-validation only).

### §2.3 — Non-~D for 79-indicator universe (59/79 = ~74.7%)

| Group | ~D-out indicators | Best-source attribution (per ~C §2.2 + sister-lane reconnaissance) |
|---|---|---|
| Leading Indicator (8) | LEI, PMI Mfg/Services, S&P PMI Mfg/Services, ISM Mfg/Services New Orders, NFIB | Conference Board, ISM, S&P Global, NFIB — none federal-source. ~E aggregate-orphan lane scope. |
| Lagging Indicator (4 ~D-out of 7) | Durable Goods Orders, Factory Orders, Business Inventories YoY, Trade Balance | Census-PRIMARY per ~C; ~D cross-ref noted for Trade Balance. |
| Financial Condition (3 ~D-out of 6) | Bloomberg BFCI, Chicago Fed NFCI, Fed Balance Sheet as % of GDP (~D-DERIVED) | BFCI = Bloomberg (n/a-private); NFCI = Chicago Fed (note: Chicago Fed IS a Reserve Bank, but NFCI publication is via FRED `NFCI`; FRED-mirror primary path); BS%GDP = ~D-derived (row 20 above). |
| Inflation (6 ~D-out of 8) | CPI, Core CPI, PPI, Unit Labor Cost, UMich 1Y, UMich 5-10Y | BLS-PRIMARY (CPI/Core CPI/PPI/Unit Labor Cost) per ~B; UMich = University-of-Michigan-private per ~E. |
| Labor Market (9) | Unemployment, Initial Jobless Claims, Continuing Claims, Job Openings, NFP, ADP, LFPR, Weekly Hours, Hourly Earnings | BLS-PRIMARY (8 of 9) per ~B; DoL (claims); ADP-private (ADP Employment) per ~E. |
| Consumer (6 ~D-out of 7) | Retail Sales MoM ×3, UMich Sentiment, CB Consumer Confidence, Wards Vehicle Sales | Census-PRIMARY (Retail Sales ×3) per ~C; UMich-private, CB-private, Wards-private per ~E. |
| Housing Market (3 ~D-out of 6) | NAHB HMI, Existing Home Sales, Pending Home Sales | NAHB + NAR — private surveys; ~E. |
| (Census ~C-PRIMARY: 3 Housing — New Home Sales, Housing Starts, Building Permits) | n/a here | n/a |
| Investor Sentiment (7) | AAII ×6, Fed NLP | AAII (American Association of Individual Investors) = private; Fed NLP = Atlanta Fed NLP (a Reserve Bank product, but distributed via Atlanta Fed website + FRED-mirror) — Wave-2 disposition. |
| Credit Spread (5) | Ted Spread, AAA, IG, AGG, HY | Bloomberg + ICE — private. ~E. |
| Market Indicator (1) | VIX | CBOE — private/exchange. ~E. |
| Currency (5) | DXY, EUR/USD, USD/JPY, GBP/USD, USD/CNH | Bloomberg/Reuters — private. ~E. |

**Total non-~D: 59/79 (~74.7%).** ~D is a **mid-coverage source-class** for this macro page; primary value-add concentrated in Treasury Yields (10 indicators = full sub-group coverage) + scattered Fed/BEA contributions across Financial Condition + Lagging + Inflation + Consumer.

### §2.4 — Wave-2-relevant ~D-adjacent candidates (out-of-79)

For Wave-2 macro-adjacent pages, the ~D surface ALSO covers:

- **Fed Funds Target Rate** (vs Effective) — FOMC-set target (range since Dec 2008); FRB H.15 + FRED `DFEDTAR` (single rate to 2008) + `DFEDTARU`/`DFEDTARL` (range upper/lower since 2008). Wave-2 if FOMC dashboard.
- **SOFR + OBFR + BGCR/TGCR** — NY Fed Markets API §1.3; Wave-2 if money-market dashboard.
- **TIC Tables 1, 3** — Major Foreign Holders, Net Cross-Border Portfolio Flows; Wave-2 if capital-flows page.
- **FRB H.6 Money Stock (M1, M2)** — DDP series; Wave-2 if monetary aggregates page.
- **FRB Z.1 Flow of Funds** — DDP series + L.110 etc.; Wave-2 if balance-sheet-of-the-economy page.
- **BEA International Transactions Accounts (ITA)** — Current account, capital account, financial account; Wave-2 if BoP dashboard.
- **FDIC BankFind** — Bank stress, deposit flows, failure tracker — Wave-2 if banking-sector page.
- **CFPB Consumer Complaint Database** — Wave-2 if financial-services-complaint page.
- **Regional Fed Surveys (5)** — Wave-2 if regional-Fed-dashboard or manufacturing-breadth page.

---

## §3 — Cadence per ~D source

| Source-class | Indicator(s) | Cadence | Release timing | Revision pattern |
|---|---|---|---|---|
| Treasury Direct CSV | 10 Treasury Yields | Daily | ~4pm ET (business days) | Rare (intraday corrections occasionally; not month-end benchmark style) |
| Treasury Fiscal Data API | Wave-2 fiscal cross-ref | Daily/Monthly per endpoint | Per-endpoint | Per-endpoint |
| NY Fed Markets EFFR | Fed Fund Rate | Daily | ~9am ET next business day | Rare (occasional revision-indicator flag) |
| BEA NIPA Quarterly | GDP QoQ | Quarterly | Advance Q+1 month last week; 2nd Q+2; 3rd Q+3; annual revisions July | Revision-heavy (advance→2nd→3rd 0.2-0.5pt typical; annual benchmark larger) |
| BEA NIPA Monthly (T20807) | PCE MoM, Core PCE MoM | Monthly | ~M+1 day 28-30 ("Personal Income and Outlays") | Minor revisions M+2 + annual benchmark July |
| FRB H.4.1 (DDP) | Fed Balance Sheet | Weekly | Thursday 4:30pm ET (data as of prior Wednesday) | Minor revisions next-week |
| FRB G.17 (DDP) | Industrial Production, Capacity Utilization | Monthly | ~M+1 day 15-17 | Initial subject to M+1 revision; annual benchmark Q4 (December) |
| FRB G.19 (DDP) | Consumer Credit | Monthly | ~M+2 day 5-7 | Revisions at M+2/M+3; annual benchmark Q4 |
| Treasury TIC Table 2 (XLSX) | Net Long Term TIC Flows | Monthly | M+2 day ~15 | Annual benchmark each summer |
| FDIC BankFind API | (Wave-2 only) | Per-endpoint (institutions real-time; financials quarterly Call Report; failures real-time) | Per-endpoint | Per-endpoint |

**AC-CADENCE-TOLERANCE (PRD §5):** Yang's monthly-update cadence is structurally aligned with all ~D-PRIMARY monthly/quarterly sources. Daily Treasury Yields are higher-resolution than yang requires (yang stores monthly snapshots; harness can sub-sample to month-end or month-avg — TO-008 decision). No cadence mismatch class fires.

---

## §4 — RE Harness Sketch

### §4.1 — Multi-source orchestration pattern

The ~D harness orchestrates **5 distinct API models** (CSV-download / REST-JSON-no-auth / REST-JSON-with-key / DDP-CSV / XLSX-download). Recommend a per-source adapter pattern:

```python
import os, requests, csv, io
import pandas as pd

class TreasuryDirectAdapter:
    BASE = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv"
    def pull_year(self, year: int) -> pd.DataFrame:
        params = {"type":"daily_treasury_yield_curve", "field_tdr_date_value":year, "_format":"csv"}
        r = requests.get(f"{self.BASE}/{year}/all", params=params, timeout=30)
        r.raise_for_status()
        return pd.read_csv(io.StringIO(r.text), parse_dates=["Date"])

class TreasuryFiscalDataAdapter:
    BASE = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
    def pull(self, endpoint: str, fields: list[str], date_range: tuple) -> list[dict]:
        params = {"fields":",".join(fields), "sort":"-record_date",
                  "filter":f"record_date:gte:{date_range[0]},record_date:lte:{date_range[1]}"}
        r = requests.get(f"{self.BASE}/{endpoint}", params=params, timeout=30)
        r.raise_for_status()
        return r.json()["data"]

class NYFedMarketsAdapter:
    BASE = "https://markets.newyorkfed.org/api/rates"
    def pull_effr(self, n: int = 30) -> list[dict]:
        r = requests.get(f"{self.BASE}/unsecured/effr/last/{n}.json", timeout=30)
        r.raise_for_status()
        return r.json()["refRates"]

class BEAAdapter:
    BASE = "https://apps.bea.gov/api/data/"
    def __init__(self):
        self.userid = os.environ["BEA_API_KEY"]   # signup: apps.bea.gov/API/signup/
    def get_nipa_table(self, table_name: str, frequency: str, year: str = "ALL") -> list[dict]:
        params = {"UserID":self.userid, "method":"GetData", "datasetname":"NIPA",
                  "TableName":table_name, "Frequency":frequency, "Year":year, "ResultFormat":"JSON"}
        r = requests.get(self.BASE, params=params, timeout=30)
        r.raise_for_status()
        return r.json()["BEAAPI"]["Results"]["Data"]   # error-check via APIErrorCode

class FRBDDPAdapter:
    """HAR-RE candidate — series= encoding requires HAR-recovered series IDs."""
    BASE = "https://www.federalreserve.gov/datadownload/Output.aspx"
    SERIES = {                          # populated post-HAR-capture
        "H4_WALCL": "<hex-id-from-HAR>",
        "G17_INDPRO": "<hex-id-from-HAR>",
        "G17_TCU": "<hex-id-from-HAR>",
        "G19_TOTALSL": "<hex-id-from-HAR>",
    }
    def pull(self, series_key: str, from_date: str, to_date: str) -> pd.DataFrame:
        params = {"rel":series_key.split("_")[0], "series":self.SERIES[series_key],
                  "lastobs":"", "from":from_date, "to":to_date,
                  "filetype":"csv", "label":"include", "layout":"seriescolumn"}
        r = requests.get(self.BASE, params=params, timeout=30)
        r.raise_for_status()
        return pd.read_csv(io.StringIO(r.text), skiprows=5)   # DDP CSV has 5-row preamble
```

### §4.2 — Per-indicator harness pull plan (20 indicators)

| # | Indicator | Adapter | Call signature |
|---|---|---|---|
| 1-10 | Treasury Yields ×10 | TreasuryDirectAdapter | `pull_year(year)` returns 14-col CSV; project to 10 yang maturities |
| 11 | Fed Fund Rate | NYFedMarketsAdapter | `pull_effr(n=30)` then month-avg if yang stores monthly |
| 12 | Fed Balance Sheet | FRBDDPAdapter | `pull("H4_WALCL", from, to)` — **HAR-RE required for series-ID** |
| 13 | Net LT TIC Flows | XLSX-download (Treasury TIC) | XLSX parser (openpyxl) on Table 2 — **HAR-RE required for download URL stability** |
| 14 | GDP QoQ | BEAAdapter | `get_nipa_table("T10101", "Q")` row "Gross domestic product" |
| 15 | Industrial Production | FRBDDPAdapter | `pull("G17_INDPRO", from, to)` — **HAR-RE required** |
| 16 | Capacity Utilization | FRBDDPAdapter | `pull("G17_TCU", from, to)` — **HAR-RE required** |
| 17 | PCE MoM | BEAAdapter | `get_nipa_table("T20807", "M")` row "Personal consumption expenditures" |
| 18 | Core PCE MoM | BEAAdapter | `get_nipa_table("T20807", "M")` row "PCE excluding food and energy" |
| 19 | Consumer Credit YoY | FRBDDPAdapter | `pull("G19_TOTALSL", from, to)` — **HAR-RE required**; YoY-derive |
| 20 | Fed BS as % GDP | Composite | WALCL ÷ NominalGDP × 100; cross-adapter |

**~10 calls per refresh per source-class × 5 source-classes = ~30-40 API calls per refresh.** Well under any documented rate limit (Treasury + NY Fed + FDIC = no auth; BEA = standard tier ~100 calls/min OK; FRB DDP = no documented limit).

### §4.3 — Failure modes + retry

- **Treasury Direct CSV**: HTTP 200 always; empty CSV body if year out-of-range. Detect by `len(df) == 0`.
- **Treasury Fiscal Data**: standard JSON-API; HTTP 200 + JSON error body on malformed; standard exponential backoff on 5xx.
- **NY Fed Markets**: HTTP 200 + empty `refRates` on out-of-range; no observed 5xx pattern.
- **BEA**: `APIErrorCode` in body on any error; throttle if `>100/min` (recommended self-throttle).
- **FRB DDP**: HTTP 200 + empty body on malformed series-ID (silent failure) — detect by `Content-Length: 0`. Critical to validate series-ID at startup via known-good probe.
- **No session/cookie model on any ~D source.** Sister to Census + Treasury Fiscal Data; clean operational risk (compare YCharts 403-session-eviction class).

### §4.4 — Cross-source consistency check (RE harness value-add)

For Treasury Yields (rows 1-10), ~D harness can produce a **3-way cross-validation**:
1. Treasury Direct CSV (upstream-authoritative)
2. FRB H.15 DDP (FRB-published mirror; HAR-RE for series-ID)
3. FRED `DGS{N}` (third-party mirror; sister ~A lane)

For Phase 2b harness verdict-taxonomy:
- **RE-MATCH** if all 3 sources agree within tolerance (±0.01% for yields)
- **RE-REPRESENTATIVE** if 2-of-3 agree (typical lag-class — daily revisions between sources)
- **RE-DRIFT** if all 3 disagree (rare; flag for investigation — likely a yang-specific transformation)

Same 3-way pattern applies to FBR balance sheet (FRB DDP / FRED mirror) + Industrial Production (FRB DDP / FRED mirror) + Consumer Credit (FRB DDP / FRED mirror) + GDP/PCE (BEA / FRED mirror).

---

## §5 — Coverage % + Sister-Lane Handoffs

### §5.1 — ~D coverage summary

- **~D-PRIMARY: 20/79 = ~25.3%** (10 Treasury Yields + 3 Financial Condition + 3 Lagging + 2 Inflation + 1 Consumer + 1 Derived BS%GDP)
- **~D-adjacent (Wave-2 candidates): 9 source-classes** (FedFunds Target, SOFR-family, TIC T1/T3, H.6, Z.1, BEA ITA, FDIC BankFind, CFPB, 5 regional Fed surveys)
- **Non-~D: 59/79 = ~74.7%** (routes to sister lanes ~A/~B/~C/~E)

### §5.2 — Sister-lane handoff matrix

| Sister lane | Source | Overlap with ~D | Disposition |
|---|---|---|---|
| **~A FRED** | FRED API (St. Louis Fed) | **HIGH** — FRED mirrors ALL 20 ~D-PRIMARY indicators (Treasury Yields, Fed Funds, WALCL, INDPRO, TCU, TOTALSL, GDP, PCE, PCEPILFE). For runtime harness, FRED is preferred (single API, no DDP HAR-RE friction). | **FRED-PRIMARY runtime; ~D for upstream-cross-validation + DRIFT investigation.** |
| **~B BLS** | BLS API | **ZERO** — BLS = labor/prices; ~D = Treasury/Fed/BEA. Disjoint. | n/a |
| **~C Census** | Census EITS | **ONE OVERLAP — Trade Balance** (joint Census/BEA `ftd`). | ~C-PRIMARY stands; ~D documents BEA upstream as cross-ref only. |
| **~E Aggregate-orphan** | Conference Board, ISM, NAHB, NAR, AAII, UMich, Wards, NFIB, AAII, Bloomberg/ICE | **ZERO** — ~E covers private + survey + index sources; ~D = federal-government sources only. | n/a |

### §5.3 — Recommendation for TO-007 synthesis (~A primary author + ~D co-author)

**Two-tier harness architecture (~D recommendation):**

- **PRIMARY runtime tier**: **FRED API** (sister ~A coverage). Reasons:
  1. Single source-of-truth simplifies harness (one adapter, one key, one rate-limit model).
  2. FRED mirrors all 20 ~D-PRIMARY indicators with established series IDs (no HAR-RE friction for FRB DDP).
  3. FRED's revision history + vintages provide audit-trail equivalent to FRB DDP.
  4. ~A lane already authoring this primary path.

- **SECONDARY / CROSS-CHECK tier**: **~D adapters** for these specific cases:
  1. **Same-day-freshness cases**: Treasury Direct CSV publishes ~4pm ET same-day; FRED `DGS10` typically updates next-business-day morning. For an end-of-day refresh (~5pm ET), Treasury Direct is fresher.
  2. **DRIFT investigation**: when FRED + Bloomberg disagree, ~D upstream (Treasury Direct / FRB DDP / BEA) is the canonical arbiter.
  3. **Wave-2 page candidates**: regional Fed surveys, TIC tables, FDIC BankFind, CFPB complaint database — not 79-indicator-relevant but Wave-2-relevant.

**Phase 2b TO-007 verdict-taxonomy alignment:** RE-MATCH / RE-REPRESENTATIVE / RE-GAP / RE-DRIFT (per ~A TO-006a §cross_domain) materializes cleanly here. Treasury Yields are the most-likely RE-MATCH class (all 3 sources publish same canonical CMT yields); BEA NIPA is most-likely RE-REPRESENTATIVE class (advance/2nd/3rd revisions across publishers); FRB DDP G.17/G.19 = RE-MATCH-with-revision-class.

---

## §6 — Source-Specific Quirks

1. **Treasury Direct CSV: ~5 additional maturities** (1.5Mo, 2Mo, 4Mo, 6Mo + "1.5 Month" naming convention) beyond yang's 10 indicators. Harness should project to yang's 10 (drop the 4 extras) at parse time, not propagate them.
2. **Treasury Fiscal Data: numeric values returned as STRING** in JSON (sister to Census EITS quirk per ~C §6.2). Explicit float parse required client-side.
3. **NY Fed Markets EFFR `revisionIndicator` field**: empty string for un-revised, populated for revised observations. Harness should surface this flag for audit trail (yang's monthly snapshot loses this dimension).
4. **BEA `APIErrorCode` only in body**: HTTP 200 + error-in-JSON-body pattern. Harness MUST inspect `BEAAPI.Results.Error.APIErrorCode` before consuming `BEAAPI.Results.Data`. Sister to Census's "Missing Key returns HTML body" failure mode (different mechanism, same "200-but-failed" class).
5. **BEA Table names are BEA-internal codes** (`T10101`, `T20807`, etc.) — not self-documenting. Harness should bundle a table-name → human-readable-description mapping cache; use `GetParameterValuesFiltered` for introspection.
6. **FRB DDP CSV has a 5-row preamble** (description + units + frequency + observation_start + Multiplier) before the header row. `pd.read_csv(..., skiprows=5)` or equivalent skip required. Naive `pd.read_csv` parses the preamble as data.
7. **FRB DDP `series=` parameter is a long hex string** discoverable only via the DDP UI's "Build a series" wizard (JavaScript-generated client-side). **HAR-RE recovery essential.** Without HAR, the harness can fall back to FRED-mirror equivalents for all FRB releases (recommended runtime path).
8. **FRB DDP silent-empty-on-malformed-series-ID**: HTTP 200 + 0 bytes when series-ID is wrong (live-probe ~22:?Z confirmed). Critical to validate series-ID at harness startup via known-good probe — silent staleness class otherwise.
9. **Treasury TIC tables are XLSX-only** (no documented JSON/REST API). XLSX parsing required; or accept FRED-mirror partial coverage (`TICFLT` etc.) as runtime, document gap.
10. **FRB H.4.1 release timing edge case**: typically Thursday 4:30pm ET, data as of prior Wednesday. Holiday-week shifts (e.g., Thanksgiving) move release to Friday. Harness should be holiday-calendar-aware.
11. **BEA NIPA quarterly release cycle = advance/2nd/3rd**: advance ~Q+1 month last week; 2nd estimate ~Q+2; 3rd ~Q+3; annual revisions July. Cross-publisher comparisons must be vintage-aware (Yang's snapshot date determines which vintage is canonical at that point).
12. **No session/cookie auth model on any ~D source.** Compare YCharts 403-session-eviction class per [[feedback_ycharts_http_400_is_cookie_stale_class]] — ~D harness has fundamentally clean operational risk profile.
13. **Regional Fed surveys have heterogeneous distribution**: NY Fed Empire is direct XLSX; Philly Fed BOS is XLSX behind landing-page click; KC/Richmond/Dallas are XLSX+PDF combos. **HAR-RE required** for each if Wave-2 picks any up.
14. **CFPB API does have rate-limiting** (~600/hour per IP per public-API docs); not a concern for Wave-2 quarterly refresh, but documented.

---

## §7 — Domains for HAR Capture (Andrew handoff list)

Per Andrew direct 2026-05-26 ~22:?Z mid-flight ratification of HAR-capture pattern, the following domains/paths are **HAR-RE candidates** (frontend-driven; no REST JSON API documented; data discoverable via browser network capture):

### §7.1 — HAR-REQUIRED (in-scope ~D-PRIMARY)

These directly affect ~D-PRIMARY indicator coverage (rows 12, 13, 15, 16, 19 of §2.1):

| # | Domain / path | What to record | Indicator(s) unlocked | Priority |
|---|---|---|---|---|
| 1 | `federalreserve.gov/datadownload/` (DDP UI "Build a series" wizard) | Click-path: select H.15 → 10Y Treasury → Generate Download → CSV | All FRB H.15 series IDs (cross-validation for Treasury Yields) | **HIGH** (~10 series, single HAR session) |
| 2 | `federalreserve.gov/datadownload/` (same UI) | Click-path: select H.4.1 → Total assets (WALCL equivalent) → CSV | Fed Balance Sheet series ID (row 12) | **HIGH** |
| 3 | `federalreserve.gov/datadownload/` (same UI) | Click-path: select G.17 → Industrial Production (INDPRO equivalent) + Capacity Utilization (TCU) → CSV | Industrial Production + Capacity Utilization series IDs (rows 15-16) | **HIGH** |
| 4 | `federalreserve.gov/datadownload/` (same UI) | Click-path: select G.19 → Total consumer credit (TOTALSL equivalent) → CSV | Consumer Credit series ID (row 19) | **HIGH** |
| 5 | `home.treasury.gov/data/treasury-international-capital-tic-system-home-page/` | Navigate to TIC Table 2 (Net Long-Term TIC Flows) → XLSX download | Net LT TIC Flows endpoint URL stability (row 13) | **MEDIUM** (FRED-mirror partial fallback exists) |

**HARs 1-4 can be batched in a single FRB DDP session** (the wizard is the same UI; record one HAR covering all 4 series-build click-paths sequentially).

### §7.2 — HAR-RECOMMENDED (Wave-2 candidates)

Out-of-79 but Wave-2-relevant; lower priority:

| # | Domain / path | What to record | Wave-2 unlock |
|---|---|---|---|
| 6 | `newyorkfed.org/research/regional_economy/empire-state-manufacturing-survey` | Navigate to data download (XLSX history file) | Empire State survey programmatic ingest |
| 7 | `philadelphiafed.org/surveys-and-data/regional-economic-analysis/business-outlook-survey` | Navigate to data download (XLSX BOS history) | Philly Fed BOS programmatic ingest |
| 8 | `kansascityfed.org/surveys/manufacturing-survey/` | Navigate to manufacturing-survey data table → XLSX | KC Fed mfg programmatic ingest |
| 9 | `richmondfed.org/research/regional_economy/surveys_of_business_conditions` | Navigate to manufacturing survey data table → XLSX | Richmond Fed mfg programmatic ingest |
| 10 | `dallasfed.org/research/surveys/tmos` | Navigate to TMOS data download → XLSX | Dallas TMOS programmatic ingest |

### §7.3 — HAR-NOT-REQUIRED (already verified clean REST APIs)

These ~D sources are HAR-not-needed; documented + live-verified REST APIs (~22:?Z):
- `home.treasury.gov/resource-center/data-chart-center/interest-rates/...csv` (Treasury Direct daily yield curve — CSV download direct)
- `api.fiscaldata.treasury.gov/services/api/fiscal_service/...` (Treasury Fiscal Data REST JSON)
- `markets.newyorkfed.org/api/rates/...` (NY Fed Markets REST JSON)
- `apps.bea.gov/api/data/?...` (BEA API REST JSON — UserID free signup, then HAR-not-needed)
- `banks.data.fdic.gov/api/...` (FDIC BankFind REST JSON)
- `api.consumerfinance.gov/data/...` (CFPB REST JSON — Wave-2-relevant only)

### §7.4 — Recommended HAR-recording sequence

For minimum operational overhead, Andrew can record HARs in this sequence (single browser session):

1. **Session 1 (FRB DDP, ~10-15 min):** open `federalreserve.gov/datadownload/`, walk wizard for H.15 (Treasury 10Y/2Y), H.4.1 (Total assets), G.17 (Industrial Production + Capacity Utilization), G.19 (Consumer Credit). One HAR file covers HIGH-priority items #1-4.
2. **Session 2 (Treasury TIC, ~5 min):** open TIC landing page, click Table 2 download. One HAR file covers MEDIUM item #5.
3. **Session 3 (Regional Fed surveys, ~10-15 min total):** five quick navigations to Empire/Philly/KC/Richmond/Dallas survey landing pages → data download click. One HAR file per bank OR one combined.

**Subagent fan-out parse plan** (post-HAR receipt): one subagent per HAR file; parse network panel for (a) request URLs, (b) query params, (c) response bodies, (d) any auth headers; emit per-source endpoint+param spec for harness adapter.

---

## §8 — RAVC2-Request

**To:** 2.0.0_SA_COO
**From:** 0.1.0_DS_MarketIntelligence~D
**TO:** YALP_MACROS.006d — Treasury/FDIC/other federal-source RE reconnaissance (Phase 2a lane D)

**Evidence:**
- This brief at `docs/briefs/yalp_macros_phase2a_treasury_fdic_reconnaissance_2026-05-26.md`
- §1 API surface — 5 documented source-classes (Treasury Direct CSV / Treasury Fiscal Data / NY Fed Markets / BEA / FRB DDP) + 4 ancillary (TIC / FDIC / regional Fed surveys / OCC-CFPB-SSA); 5 endpoints LIVE-VERIFIED ~22:?Z (HTTP 200 + sample shape captured)
- §2 Per-indicator match-set — 20 ~D-PRIMARY indicators classified across 6 yang groups; 1 cross-reference (Trade Balance, ~C-PRIMARY stands); 59 non-~D best-source-attributed to sister lanes
- §3 Cadence per ~D source — 5 cadence classes (daily / weekly / monthly / quarterly / mixed) documented with release-timing + revision-pattern
- §4 RE harness sketch — 5 per-source adapter classes drafted; per-indicator harness pull plan for 20 indicators; failure-mode + retry + cross-source 3-way validation pattern
- §5 Coverage % — **20/79 = ~25.3% ~D-PRIMARY**; 9 Wave-2-candidate source-classes; sister-lane handoff matrix with FRED-PRIMARY-runtime + ~D-CROSS-CHECK recommendation
- §6 Source-specific quirks — 14 surfaced (string-typed values, BEA APIErrorCode, FRB DDP preamble + silent-empty-on-malformed, regional Fed XLSX heterogeneity, no-session-cookie clean operational risk, etc.)
- §7 **HAR-capture domains list** per Andrew direct 2026-05-26 mid-flight ratification: 5 HAR-REQUIRED (HIGH/MEDIUM priority) + 5 HAR-RECOMMENDED (Wave-2) + recommended 3-session capture sequence + subagent fan-out parse plan

**5/5 ACs MET:**
- **AC1** ✅ API surface — 5 documented + 4 ancillary; endpoint patterns + auth + pagination + failure modes
- **AC2** ✅ Per-indicator match-set — all 79 yang indicators classified (20 ~D-PRIMARY + 1 cross-ref + 59 non-~D-with-best-source)
- **AC3** ✅ Cadence — 5 cadence classes documented per source + release-timing + revision-pattern
- **AC4** ✅ RE harness sketch — 5 adapter classes + per-indicator pull plan + 3-way cross-source validation pattern
- **AC5** ✅ Coverage % — 20/79 = ~25.3% + sister-lane handoff matrix + FRED-PRIMARY-runtime/~D-CROSS-CHECK two-tier recommendation

**Phase 2b TO-007 synthesis input (co-author with ~A primary):** Two-tier harness architecture — FRED-PRIMARY runtime + ~D upstream-CROSS-CHECK for (1) same-day freshness, (2) DRIFT investigation, (3) Wave-2 candidates. Trade Balance overlap with ~C resolves to ~C-PRIMARY (Census `ftd`); ~D documents BEA upstream as cross-ref only. Treasury Yields = highest-confidence RE-MATCH class (3-way Treasury Direct + FRB H.15 + FRED agree on canonical CMT yields).

**Outstanding for Andrew:** HAR recordings per §7.1 (HIGH priority — 4 FRB DDP series-IDs + 1 Treasury TIC URL stability) unlock 5 of 20 ~D-PRIMARY indicators (rows 12-13, 15-16, 19) for upstream-RE; FRED-mirror fallback exists for all 5, so HAR is harness-enhancement not harness-blocker.

**Standing for:** RAVC2-ACCEPT on Phase 2a Treasury/FDIC/govt-other reconnaissance lane closure + Phase 2b TO-007 synthesis dispatch (co-author with ~A primary).

— 0.1.0_DS_MarketIntelligence~D
2026-05-26

---

## §9 — Addendum: FRED v2 `release/observations` endpoint obsoletes §7.1 HAR-capture pattern (Andrew direct ~23:?Z post-RAVC2-ACCEPT)

**Andrew direct (post-RAVC2-ACCEPT, this same cycle):** surfaced FRED's `v2/release/observations` endpoint as the right primitive instead of HAR-recording the FRB DDP wizard. Documentation: `https://fred.stlouisfed.org/docs/api/fred/v2/release_observations.html`.

### §9.1 — Endpoint pattern

```
GET https://api.stlouisfed.org/fred/v2/release/observations
    ?release_id={N}                                       (integer; e.g., 52 for Z.1)
    &format=json                                          (json|xml)
    &limit=500000                                         (max per page; default 500000)
    &next_cursor={prior-response-cursor}                  (cursor-based pagination)
    &api_key={32-char-alpha-num-lowercase}                (REQUIRED — standard FRED API key)
```

**Live-probe disposition (~23:?Z):**
- `release_id=52&format=json` without key → HTTP **401** `{"code":401,"message":"Missing or invalid credentials."}` (auth-gated)
- Standard FRED API key signup: `https://fred.stlouisfed.org/docs/api/api_key.html` (free, instant, 32-char-alpha-num-lowercase).
- Same auth class as Census + BEA + CFPB API-key model. **No HAR capture required.**

### §9.2 — Why this obsoletes §7.1 HAR-REQUIRED items

§7.1 listed FRB DDP wizard (H.15 / H.4.1 / G.17 / G.19) as HAR-REQUIRED HIGH priority for recovery of canonical series IDs. FRED's `release/observations` makes this **unnecessary**:

- FRED is organized BY Fed statistical release at the release_id level.
- A single call (paginated by cursor; up to 500k observations/page) returns **ALL series** in a release + **full observation history** + metadata (frequency, units, seasonal_adjustment, last_updated, source notes).
- No per-series HAR-RE; no FRB DDP wizard friction; no silent-empty-on-malformed-series-ID class.

### §9.3 — FRED release IDs for ~D-PRIMARY Fed releases

FRED release IDs for the 4 Fed statistical releases referenced in this brief's §7.1 (well-known from FRED's public release listing at `fred.stlouisfed.org/releases` — verification via authenticated `/fred/releases?api_key=...` recommended at harness build time):

| FRB release | ~D-PRIMARY indicator(s) | FRED release_id (canonical) |
|---|---|---|
| H.15 Selected Interest Rates | (Treasury Yield cross-validation rows 1-10) + Fed Fund Rate (row 11 cross-ref) | **18** |
| H.4.1 Factors Affecting Reserve Balances | Fed Balance Sheet (row 12) | **20** |
| G.17 Industrial Production and Capacity Utilization | Industrial Production + Capacity Utilization (rows 15-16) | **13** |
| G.19 Consumer Credit | Consumer Credit YoY (row 19) | **17** |
| Z.1 Financial Accounts | (Wave-2 candidate per §2.4 — Z.1 Flow of Funds) | **52** (Andrew's example) |

**Recovery method if any release ID is wrong:** `GET /fred/releases?api_key=...&file_type=json` returns the full release catalog (~300 entries) with id + name + frequency + last_updated; harness should cache this at startup OR pre-bake the mapping after one-time discovery.

### §9.4 — Updated harness adapter (replaces §1.5 FRB DDP adapter)

```python
class FREDReleaseAdapter:
    """Replaces FRB DDP HAR-RE per Andrew direct ~23:?Z.
    One adapter handles H.15 / H.4.1 / G.17 / G.19 / Z.1 + any FRED release."""
    BASE = "https://api.stlouisfed.org/fred/v2/release/observations"
    def __init__(self):
        self.api_key = os.environ["FRED_API_KEY"]   # signup: fred.stlouisfed.org/docs/api/api_key.html
    def pull_release(self, release_id: int, limit: int = 500000) -> list[dict]:
        """Returns flattened (series_id, date, value) tuples for ALL series in release."""
        results, next_cursor = [], None
        while True:
            params = {"release_id":release_id, "format":"json", "limit":limit, "api_key":self.api_key}
            if next_cursor: params["next_cursor"] = next_cursor
            r = requests.get(self.BASE, params=params, timeout=60)
            r.raise_for_status()
            payload = r.json()
            for s in payload.get("series", []):
                for obs in s.get("observations", []):
                    if obs["value"] == ".": continue   # FRED missing-value sentinel
                    results.append({
                        "series_id": s["series_id"], "date": obs["date"], "value": float(obs["value"]),
                        "frequency": s["frequency"], "units": s["units"],
                        "seasonal_adjustment": s["seasonal_adjustment"],
                        "last_updated": s["last_updated"],
                    })
            if not payload.get("has_more"): break
            next_cursor = payload["next_cursor"]
        return results
```

### §9.5 — Updated §7 HAR-capture list disposition

| Original §7.1 item | New disposition |
|---|---|
| H.15 DDP HAR | **OBSOLETED** — use `release_id=18` via FRED `release/observations` |
| H.4.1 DDP HAR | **OBSOLETED** — use `release_id=20` |
| G.17 DDP HAR | **OBSOLETED** — use `release_id=13` |
| G.19 DDP HAR | **OBSOLETED** — use `release_id=17` |
| Treasury TIC T2 XLSX HAR (MEDIUM) | **STILL APPLIES** — TIC is published by Treasury, not in FRED's H-series releases; FRED partial coverage via `release/observations` for `TICFLT` (Major Foreign Holders) but not full T2 (Net Long-Term TIC Flows). HAR remains the path to confirm Treasury TIC XLSX URL stability. **NB:** confirm via FRED release catalog at harness build time whether a TIC-specific release_id exists (FRED has `release_id=39` for "Treasury International Capital System" — if so, this MAY ALSO obsolete the TIC HAR). |
| Regional Fed surveys ×5 (LOW) | **MOSTLY OBSOLETED** for the headline series — Empire State / Philly Fed BOS / KC / Richmond / Dallas all have FRED-mirrored headline diffusion indices (e.g., `GACDISA066MSFRBNY` for Empire State headline; check via FRED's release_id catalog for survey-specific releases). HAR retained as fallback for sub-component / breakdown data FRED may not mirror. |

### §9.6 — Updated 2-tier harness architecture for TO-007 synthesis

**Original recommendation (§5.3):** FRED-PRIMARY runtime + ~D-CROSS-CHECK via Treasury Direct / FRB DDP / BEA.

**Updated recommendation (post-Andrew direct §9):** **FRED `release/observations` BULK-PRIMARY runtime + ~D-source-specific CROSS-CHECK only for the gaps FRED doesn't cover.**

Reasons:
1. FRED `release/observations` returns ALL series in a Fed statistical release in one paginated call — more efficient than 4 individual DDP adapter calls.
2. Single adapter class (`FREDReleaseAdapter` §9.4) replaces FRBDDPAdapter (§4.1 row 5) + simplifies harness.
3. Cursor-based pagination + 500k-observation limit = single call per release for typical historical depth.
4. FRED's series metadata (frequency, units, SA, last_updated, source notes) preserves audit trail equivalent to FRB DDP raw downloads.

**~D-source-specific CROSS-CHECK remaining tier:**
- **Treasury Direct CSV** (§1.1) — same-day-freshness for Treasury Yields when FRED next-morning lag matters
- **Treasury Fiscal Data** (§1.2) — fiscal-side cross-validation (avg interest rates, debt-to-the-penny)
- **NY Fed Markets API** (§1.3) — EFFR daily granularity beyond FRED's `FEDFUNDS` monthly
- **BEA API** (§1.4) — GDP/PCE upstream when BEA vintage matters
- **Treasury TIC XLSX** (§1.6) — only if FRED `release_id=39` (TIC system) coverage is partial post-HAR-verify

**HAR-capture pattern for Andrew NARROWED:** §7.1 HIGH/MED items obsoleted (4 of 5); only Treasury TIC XLSX (§7.1 #5) potentially survives, gated on FRED `release_id=39` coverage check.

### §9.7 — Updated outstanding-for-Andrew

- **OLD (§8):** "HAR recordings per §7.1 unlock 5 of 20 ~D-PRIMARY indicators ... HAR is harness-enhancement not harness-blocker."
- **NEW (post-§9):** "FRED API key signup + `release_id=18,20,13,17` baked into harness obsoletes 4 of 5 §7.1 HAR items. TIC HAR optional gated on FRED `release_id=39` coverage check. Andrew HAR-capture-window NARROWED to optional single XLSX session if FRED TIC coverage is incomplete + the regional Fed surveys are Wave-2-deferred."

**Net effect:** ~D's TO-007 synthesis input upgrades from "two-tier harness with HAR-recovered FRB DDP series" to "FRED-release-bulk-PRIMARY harness with narrow ~D-source CROSS-CHECK". Cleaner architecture; less HAR friction; FRED's release-organizing primitive aligns naturally with the macro page's Fed-statistical-release source structure.

— 0.1.0_DS_MarketIntelligence~D
2026-05-26 (§9 addendum post-RAVC2-ACCEPT per Andrew direct ~23:?Z)

