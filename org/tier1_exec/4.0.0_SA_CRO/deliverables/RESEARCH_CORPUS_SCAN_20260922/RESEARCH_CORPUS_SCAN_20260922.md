# THE ASSET MANAGEMENT RESEARCH CORPUS, SCANNED: report classes, their skeletons, the model typecast, and the sector idiosyncrasies

**Seat:** `4.0.0_SA_CRO~F`. **Date:** 2026-09-22 ~17:5xZ-18:3xZ. **Authority:** Andrew-direct at this terminal ~17:5xZ, verbatim in
`../ANDREW_DIRECT_20260922_17xxZ_CLAUDE_ANALYSIS_LAYER_PLATINUM_DESIGN.md` (seventh message): *"scan through those earnings reports
and look for those idiocyncrasies per sector/business type (e.g. banks, or insurance companies, particularly) ... on 'Model' we
want to typecast 'Model' formats (what ratios are they using) and how on a sector-level ... For securities that already existed
in the database, we need a continuation of how the reports were generated."*
**Corpus:** `OneDrive - Opal Capital/Shared - Documents/Asset Management/Research/`, synced locally, read in place (cloud
placeholders hydrated on read; nothing copied into the repo, nothing sent anywhere). Raw extraction records beside this file
(six JSON files); every figure below is from them.

```
  DENOMINATORS
    name folders           93 (0 loose files at the root)
    files                  351 = 184 .pdf + 78 .xlsx + 71 .docx + 17 .png + 1 .html; 305.7 MB
    Word reports read      71 of 71 .docx (headings + full text; 0 errors)
    report PDFs read       52 (the ones with NO .docx twin, name-filtered to research packs / earnings updates / one-pagers;
                              company source PDFs -- releases, 10-Ks, RNS, transcripts, presentations -- were NOT read)
    workbooks read         78 of 78 .xlsx (sheet names; Model / Overview / CSC cell strings and formulas)
    sector label found     77 of 93 names, from the team's OWN "Sector" header cell or line (2 of the 77 are extraction
                              glitches reading "Location:" -- Costco, Rio Tinto -- and count as UNRESOLVED, so 75 usable)
    fund named             59 of 93 names (IDVZ 43, PFOE 18, DIVZ 3; some name two)
```

---

## 1. FOUR DOCUMENT CLASSES, and the skeleton each one keeps

**Class A -- the RESEARCH PACK / RESEARCH NOTE (initiation).** 23 Word + ~25 PDF-only. Skeleton, in the order the files keep it:
1. **Header block**: Ticker, Name, Sector, Location, Currency, Fiscal Yr, PE NTM, ADTV, and a "TL & SE" balance snapshot;
2. **Financial Summary** table (the one-pager's Model sheet pasted: 2016A ... 2028E);
3. **RECOMMENDATION** -- a fund and a position size (*"Initiate ~2% position in IDVZ"*, *"Candidate for DIVZ"*, *"~1% position in
   IDVZ"*, *"PASS risk reward doesn't justify current valuation"*);
4. **segments** (revenue by segment, with %);
5. **INVESTMENT THESIS** (bulleted pillars, each a bold lead + a paragraph);
6. **RISKS AND CONSIDERATIONS** (same shape); often **OTHER POSITIVES / OTHER NEGATIVES**;
7. **MANAGEMENT / BOARD** (CEO first, tenure, prior roles);
8. **charts**: COMMON STOCK COMPARISON (the CSC table), HISTORICAL VALUATION / VALUATION 10 YEARS / 20 YEARS (P/E, EV/EBITDA
   history), TRADING MULTIPLES VS PEERS, PRICE CHART; plus sector-specific pages (Copa: FLEET PLAN, OPERATIONAL DATA; Michelin:
   OPERATING MARGINS, REVENUE-BASED MARKET SHARE; Shopify: REVENUE GROWTH PROFILE; Singtel: SUM-OF-THE-PARTS).
Median 1,174 words (Word class); PDF-only packs run 18-34 pages.

**Class B -- the EARNINGS UPDATE (quarterly).** 40 Word + ~20 PDF-only. Two authors, two funds, ONE skeleton:
1. **RECOMMENDATION: MAINTAIN x% POSITION IN <fund>** + a one-paragraph "why" (33 of 71 Word files carry an explicit size; 49 name
   a fund) -- *this is the "why we own this" carrier Andrew asked for, and it is where the DELTA belongs*;
2. **Headline results / Qn Summary** (beat or miss, the numbers);
3. **Geographic highlights** and **Segment highlights** (the PDF author's fixed pair; the Word author writes them as named
   sections per business);
4. **Guidance** (updated vs prior);
5. **Headwinds and risks** (PDF author) / **Reasons for stock price reaction** (Word author);
6. **Broker commentary / Broker perspectives and ratings** (41 of 71 files mention brokers; 42 consensus/estimates);
7. **PERFORMANCE VS FUND** (relative performance since purchase);
8. **EARNINGS ESTIMATE PROGRESSION** (the consensus EPS revision chart);
9. **TRADING HISTORY** (the fund's buys and sells in the name);
10. sometimes **COMMON STOCK COMPARISON**.
Median 649 words. Dividend is mentioned in 51 of 71 files, guidance in 37, capex in 15, net debt in 21.

**Class C -- the word-capped SHORT FORM.** 8 Word files: *Company Overview (250) / Investment Thesis 250 / Investment
Considerations 100 / Management-Board 80* -- the numbers are word budgets. A template for a one-screen read.

**Class D -- the STOCK-MOVE UPDATE.** 3 files (AZN, Nokia, Intuit): a single page on a price move, *"Investment thesis unchanged"*.

**A fifth thing that is not a report:** the JD.com, KDDI, MUFG, SMFG and Tokyo Marine "Research Pack Template" files still carry
`[PASTE EXCEL OUTPUT]` and `[COMPANY NAME] [TICKER]` -- the blank template itself, which is useful: it is the team's own
statement of the Class A skeleton.

---

## 2. THE MODEL TYPECAST -- what ratios, and whether they change by sector

**Two generations of the one-pager workbook**, both present:
- 2025 "International Dividend One Pagers": sheets `Overview` + `CSC` (+ CapIQ cache), 21 workbooks;
- 2026 "ONE PAGER" / "FactSet Based ONE PAGER": sheets `Model` (37) and/or `Model NEW VERSION` (24) + `Charts` (24) + `CSC` (56 of 78
  workbooks carry a CSC sheet) + a balance-sheet or EPS-history side sheet.

**The field set is ONE template, sector-agnostic.** Of 60 workbooks with model content, **58 carry the same Bloomberg mnemonic
core**: `PX_LAST, EQY_SH_OUT_TOT_MULT_SH, NET_DEBT, EQY_FREE_FLOAT_PCT, EQY_RAW_BETA, BEST_DIV_YLD, BS_CASH_NEAR_CASH_ITEM,
BS_TOTAL_LIABILITIES, SALES_REV_TURN, BEST_SALES, IS_ADJUSTED_GROSS_PROFIT, IS_ADJUSTED_OPERATING_INCOME, BEST_EBIT, EBITDA_ADJUSTED,
BEST_EBITDA, BEST_NET_INCOME, BEST_CAPEX, CF_FREE_CASH_FLOW, BEST_ESTIMATE_FCF, IS_COMP_EPS_ADJUSTED, BEST_EPS, BEST_BPS,
IS_SH_FOR_DILUTED_EPS, NET_INCOME, EQY_DPS, BEST_DPS` (+ `PE_RATIO` 50, `IS_DIL_EPS_CONT_OPS` 46). **35** carry the extended
ratio set: `PX_TO_BOOK_RATIO, PX_TO_FREE_CASH_FLOW, GROSS_MARGIN, OPER_MARGIN, EBITDA_TO_REVENUE, RETURN_COM_EQY, RETURN_ON_ASSET,
RETURN_ON_CAP, RETURN_ON_INV_CAPITAL, RETURN_ON_TANGIBLE_ASSETS, CUR_MKT_CAP, EQY_SH_OUT_REAL`. **23** are the FactSet-based
variant with the same lines under FactSet codes (`FF_SALES, FF_GROSS_INC, FF_EPS, FF_BPS, FF_BPS_TANG, FF_DPS, FF_ROA, FF_ROE,
FF_NET_DEBT, FF_DEBT, FF_CASH_ST, FF_FREE_CF, FF_STK_PURCH_CF, FE_ESTIMATE, FG_FACTSET_SECTOR`).

**The row labels are the same across sectors** (workbooks carrying each, of 60): `ROE 60, FCF 60, DPS 60, P/E 60, P/B 60, EBIT 60,
EBITDA 60, Rev 59, y/y Growth 58, EPS 58, BVPS 58, ROA 58, Div Yield 58, Net Debt 58, Enterprise Value 58, Upside Case / Base
Case / Downside Case 58, Multiple 58, Return 58, Opal Case Assumptions 58, FCF Margin 57, FCF Yield 57, Revenue/Sh 39, RoTA 34,
EV/Sales Range 43, P/E Range 24, P/B Range 23, FCF Yield Range 23, EV/EBITDA Range 23`. The **Opal Case Assumptions** block
(REVENUE GROWTH and EARNINGS MARGIN, each with MIN / MAX / AVERAGE / MEDIAN over history) drives three cases as EPS x multiple ->
price -> return. This is the house's forward-view mechanism, present in 58 workbooks.

**Sector departures inside the workbooks are RARE and small** -- two measured: Nubank's Model adds `BS_TIER1_COM_EQUITY_RATIO` and
`BS_TOT_LOAN`; Telefonica Brazil's adds `APRU` (sic). No other bank or insurer workbook (HSBC, ICICI, MUFG, Tokyo Marine, Zurich,
BB Seguridade) departs from the template; they are the 2025 Overview+CSC generation with the generic lines.

**So the typecast finding is:** the MODEL is one shape for every sector, and the sector lives in the REPORT TEXT and the CHARTS,
not in the sheet. A sector template for the analysis layer is therefore (i) the generic model lines for everyone, plus (ii) a
sector KPI list that the one-pager never carried and the prose always did, plus (iii) the sector's chart pages.

---

## 3. THE SECTOR IDIOSYNCRASIES, from the prose (Word text census over 71 files)

| business type | names in corpus (measured "Sector" or the folder's business) | the sections and KPIs the team's reports actually use |
|---|---|---|
| **Banks** | BNP Paribas, China Construction Bank, HSBC, ICICI, Intesa Sanpaolo, MUFG, SMFG, UBS, Nubank (9) | CCB: *Headline numbers, Revenue mix, NIM, Asset quality and returns, Dividend*; Intesa: *Revenue Drivers, Operational Efficiency, Asset Quality, Capital Position, Shareholder Remuneration*; HSBC: *Financial Results, Segment Performance, Asset Quality and Costs, Capital Returns, Updated Guidance*; UBS: *Divisional Performance (GWM, IB), Capital Management and Integration, Swiss Government Capital Requirements, Current Capital Position*. Terms: CET1 in 5 files, cost of risk / provisions 6, ROE/ROTE 7, cost/income 3, NIM 1 (by name; "margin" language elsewhere). **KPI set: NII and fee mix, NIM, cost/income, cost of risk and asset quality (NPL, coverage), CET1, RoTE, capital returns (dividend + buyback), divisional P&L.** |
| **Insurers** | BB Seguridade, Tokyo Marine, Zurich (3) | BB Seguridade: *Key Segment Performance by line -- Brasilseg (insurance), Brasilprev (pension), BB Corretora (brokerage), Brasilcap (premium bonds) -- then Dividends and Guidance*. Terms: premiums 25 files (the word is common), combined ratio 2. **KPI set: premiums written by line, combined ratio, investment result, reserves, dividend payout, solvency.** |
| **Oil, gas, energy** | BP, Petrobras, TotalEnergies, Halliburton, Schlumberger, Valero (6) | Petrobras: *Net Income, Adjusted EBITDA, Production, Dividends, Debt and Cash Flow* + a production-history workbook 2006-2030; TotalEnergies: *Production, Capital Returns and Investments, PRODUCTION (kboe/d) chart*; BP: *Operational Headwinds, Strategic Priorities*. Production terms in 12 files. **KPI set: production (kboe/d), realised price, adjusted EBITDA, capex, net debt / gearing, shareholder distributions.** |
| **Telecoms** | America Movil, KPN, Orange, Telefonica Brazil, Singtel, KDDI (6) | KPN: *Segment Performance, Guidance Revision*; Telefonica: *Key Financial Metrics, Operational Performance* (+ a company results spreadsheet with mobile operating figures); Singtel: *SUM-OF-THE-PARTS*. ARPU 3 files, churn 5. **KPI set: service revenue growth, ARPU, churn / net adds, EBITDA margin, capex/sales, FCF, dividend; SOTP for holdcos.** |
| **Consumer staples / non-durables** | Nestle, Unilever, Reckitt, KMB, Clorox, BAT, Imperial, Coca-Cola Femsa, Walmex, Celsius, Monster, Nike (12) | Reckitt: *Profitability and Margins, Cash Flow and Returns, Segment and Category Performance (Emerging Markets, North America, Europe), Category Performance, Full-Year Guidance*; BAT: *Revenue, Adjusted Profit from Operations, Adjusted Diluted EPS, Operating Margin, Category and Regional Performance, New Categories, Combustibles*; Imperial: *Rev Vol Price Distribution* sheet. Volume/price terms in 42 files, organic growth 4. **KPI set: organic growth split volume vs price/mix, category and region, gross and operating margin, FCF conversion, dividend and buyback; tobacco: volume decline vs price, NGP.** |
| **Pharma / health** | AstraZeneca, GSK, Sanofi, Roche, Novartis, LLY, Idexx, ISRG, Zoetis, UNH (10) | GSK: *Segment Results (Vaccines, Specialty, General Medicines, Oncology), Accelerate Growth program, Nuvalent Acquisition, Guidance, Shareholder returns*; Roche: *Headline numbers, Diagnostics, Pipeline, Guidance and dividend*; AZN: *Business Segment and Product Performance, 2026 Guidance and 2030 Ambition*; EPS-history reconciliation workbooks (AZN, GSK, Sanofi business vs IFRS EPS). **KPI set: product and therapy-area growth, pipeline and approvals, core vs reported EPS (the reconciliation), margin, guidance and long-dated ambition.** |
| **Software / tech services** | SAP, Adobe, Cadence, Synopsys, Intuit, ServiceNow, Workday, Netflix, Spotify, MSCI, Shopify, GOOGL (12, PFOE-heavy) | PDF author's fixed skeleton: *Headline results, Geographic highlights, Segment highlights, Headwinds and risks, Guidance*; SAP research pack: *Revenue Visibility and Resilience, Capital Returns, IMPACT OF ARTIFICIAL INTELLIGENCE, The Dominant Platform Scenario*. ARR/RPO/backlog 3 files, GMV 3. **KPI set: cloud/subscription revenue and ARR, RPO/backlog, operating margin, FCF margin, net revenue retention where disclosed.** |
| **Industrials / transport** | CN Rail, Copa, OMA airports, ICTSI, Boeing, HEICO, Uber, Bunzl, Michelin, Tokyo Electron, TSMC, ASML, Hon Hai (13) | Copa: *MOAT, 2026 DYNAMICS, OPERATIONAL DATA, FLEET PLAN, CPA owns most of its planes*; ICTSI: *Throughput Volume, EBITDA and Margins*; CN: *Operational crisis 2021-22, 20-year P/E, 20-year EV/EBITDA*. **KPI set: operating metrics (RPK/ASK/load factor; throughput TEU; operating ratio), unit economics, capex cycle, long valuation history.** |
| **Utilities** | Enel, Iberdrola, National Grid, SSE, RWE, Manila Electric (6) | Enel: *Earnings and Income, Operational Drivers, Regional Offsets, Debt and Investment*; Manila: *Segment Performance, Dividends, Reasons for Market Reaction* + regulatory work flagged in the recommendation. **KPI set: regulated asset base / networks vs generation, EBITDA by business, net debt, capex plan, regulatory and tariff events, dividend.** |
| **Materials** | Rio Tinto (1) | *Production growth, Cap Ex cycle, Segment EBITDA (Iron Ore, Copper, Aluminium & Lithium), Strategic Outlook*. **KPI set: volumes and realised prices by commodity, unit costs, segment EBITDA, capex.** |

**Two vocabularies in the "Sector" header, the same seam `lib/research/peers/taxonomy.py` already names:** the FactSet-based
workbooks print FactSet/RBICS sectors (*Technology Services 10, Consumer Non-Durables 7, Health Technology 6, Electronic
Technology 4, Finance 4, Commercial Services 3 ...*) and the Bloomberg-based ones print GICS (*Information Technology 3,
Consumer Discretionary 2, Communication Services 3, Consumer Staples 4, Financials 5, Health Care 2, Utilities 4, Energy 3 ...*).
A sector template keyed on either alone misses half the corpus; the engine's `GICS11_TO_SCANNER13_v1` map is the bridge.

**The two funds write differently and the layer must know which fund a name is in:** IDVZ reports (43 names; Word; the
international-dividend PM) carry RECOMMENDATION + TRADING HISTORY + PERFORMANCE VS FUND and dividend language in nearly every
file; PFOE reports (18 names; PDF; the US-growth PM) carry the fixed five-section skeleton and *"Fund: PFOE"* in the header.
DIVZ appears 3 times as a candidate fund. The fund is a field of the report, not of the security.

---

## 4. WHAT "CONTINUATION" MEANS FOR A NAME THE TEAM HAS ALREADY WRITTEN UP

For 59 of 93 names the corpus holds the fund, the position size, the thesis pillars (Class A), the prior recommendation and its
reasoning (Class B), and the estimate-progression and performance-vs-fund charts. The continuation contract is therefore
measurable per name: (i) the same fund and the last stated position size are the report's opening line, and the layer writes
the DELTA against them; (ii) the thesis pillars of the last research pack are the axes the update reassesses, each marked
intact / strengthened / weakened, cited; (iii) the KPI set the prior reports used for this name (section 3) is the KPI set
the update reports, before any generic line; (iv) the charts the prior reports carried are the charts the export carries.
For the 34 names with no fund on file, the layer starts from the sector template and says so.

---

## 5. WHAT THIS SCAN DID NOT DO

- It did not read the company source PDFs (releases, RNS, 10-Ks, transcripts, presentations), the 17 PNG charts or the HTML.
- It did not read the report PDFs beyond page 6 for headings, and it did not OCR anything.
- It classified names into business types by the team's own Sector cell where present and by the folder's business otherwise;
  16 names have no Sector cell and 2 read a glitch -- those rows are marked in `research_sector_fund_map.json`.
- It counted KPI terms by regex over Word text only (the PDF-only reports' text is not in the census), so the term counts are
  lower bounds for the corpus.
- It did not measure the section order inside the PDF-only earnings updates beyond their page-1 to page-6 headings.
- It did not open the `_CIQHiddenCacheSheet` / `__FDSCACHE__` caches (vendor data caches; nothing extracted from them).
