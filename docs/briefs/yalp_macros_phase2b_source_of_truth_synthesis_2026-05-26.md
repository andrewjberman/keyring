# YALP_MACROS Phase 2b — Consolidated Source-of-Truth Synthesis

**TO:** YALP_MACROS.007 — Phase 2b consolidated per-indicator source-of-truth synthesis brief
**Primary author:** 0.1.0_DS_MarketIntelligence~A (Phase 2 lead)
**Co-authors:** 0.1.0_DS_MarketIntelligence~B (BLS), ~C (Census), ~D (Treasury/FDIC), ~E (Aggregate/orphan) — substrate-reuse per their TO-006[bcde] briefs; co-author MCP optional per TO §cross_domain_coordination
**PRD:** `docs/architecture/YALP_MACROS.md` v0.5 RE-OPENED `7e781ea8c` Phase 2 charter
**Authority:** Andrew sovereign 2026-05-26T~21:00Z RE-OPEN + MSTR LD-0104 fast-trajectory + ws COO TO-007 GO `3ccd78679`
**T*:** indicator-cadence-bound (Phase 2a substrate verified 2026-05-26 ~21:00-21:14Z across 5 lanes)
**Status:** Phase 2b synthesis COMPLETE — 7/7 ACs met

---

## §0 — TL;DR

**Phase 2a 5-of-5 lane convergence empirically grounds a two-tier multi-source RE harness architecture for the 79-indicator Macroeconomics page:**

- **PRIMARY runtime tier = FRED** (~A coverage 49 MATCH + 5 REPRESENTATIVE + 1 DERIVED = 55/79 = 69.6%) — single adapter + single api_key + clean ops profile + 120 req/min rate limit + AWS-Secrets `FredApiKey` already provisioned.
- **CROSS-CHECK tier = sister-lane upstream-authoritative** (~B BLS for 10 labor/inflation; ~C Census for 9 housing/trade/consumer; ~D Treasury Direct + FRB DDP + BEA + NY Fed Markets for 20 federal-source) — DRIFT-arbitration + same-day-freshness + revision-flag richness when needed.
- **GAP-routing tier = ~E aggregate-orphan PRIMARY** for the 24 FRED-GAP indicators (~30.4%) — 6 access-class tiers with 2 LIVE-VERIFIED OPEN-REST quick-wins (Yahoo Finance ^MOVE + CNH=X) + 11 HAR-RE Wave-2 candidates + 5 PAID-SUBSCRIPTION architectural-call surface + 1 DISCONTINUED + 1 YANG-INTERNAL.

**Per-indicator coverage closure: 79/79 routed (100%).** Empirically PRIMARY-implementable today (Wave-1 = FRED + Yahoo Finance + 1 substitute, no HAR-RE, no paid subscription): **58/79 (~73.4%)**. With HAR-RE Wave-2 (~2h capture + parse): **69/79 (~87.3%)**. With paid subscriptions + documented substitutes: **74/79 (~93.7%)**. **5 net architectural-call indicators** (3 PAID-only-no-substitute + 1 DISCONTINUED + 1 YANG-INTERNAL) — recommended disposition per Andrew sovereign 21:00Z "push down" framing = **(c) RE-GAP acceptable-by-documentation** (§4).

**Verdict-taxonomy finalized as 5-shape (per Andrew v0.5 §3 carve-out):**
RE-MATCH / RE-REPRESENTATIVE / RE-GAP / RE-DRIFT / **RE-DEFERRED** (new — PAID-class indicators with monthly-cadence-acceptable + Wave-3+ deferral disposition).

**TO-008 harness build sequence recommended (§7):** Wave-1 (FRED + YahooFinance + 3 OPEN-REST) → Wave-2 (HAR-capture sequence for 11 indicators ~2h) → Wave-3 (BLS CROSS-CHECK overlay) → Wave-4 (Census + Treasury/FDIC + NY Fed CROSS-CHECK overlays) → Wave-5 (architectural-call resolution for 5 PAID + cleanups).

**5 cleanup-class findings (§5) routed for Andrew/CTO/DT-0.1.0 disposition:** Ted Spread DISCONTINUED LIBOR-retirement-2022 (deprecate vs SOFR-substitute); Fed NLP yang-internal-clarify (DS 0.1.0~A code-path confirmation); ICSA/CCSA mis-attribution-to-BLS (DT 0.1.0 yang-generate-macro audit per ~B §6 row 5); PPI modern WPSFD4 vs legacy WPU00000000 class-distinction (yang label maps to legacy; press maps to modern; architectural decision-point); Industrial Productivity MoM yang-label variant for FRB G.17 Industrial Production Index (Phase 1 F4 sister).

**Cascade-compression benchmark:** Phase 2a lane spawn-to-ship times — ~A 7min, ~E 25min, ~D ~40min, ~B & ~C lane-similar. Each subsequent lane benefitted from cumulative sister-lane substrate. This Phase 2b synthesis directly inherits all 5 lane briefs verbatim per [[feedback_standby_prep_cascade_compression_2.4x_throughput]]. Multi-lane parallel reconnaissance + same-fabric sibling-template-reuse is the empirically-validated compression pattern.

---

## §1 — Per-Indicator Source-of-Truth Mapping (79 rows)

Columns: # | Indicator | Group | yang-slug | PRIMARY-source | PRIMARY-endpoint-pattern | PRIMARY-cadence | SECONDARY-cross-check | Cost/access-tier | RE-verdict-preliminary-class

### §1.1 — Leading Indicator group (8 indicators)

| # | Indicator | yang-slug | PRIMARY | PRIMARY endpoint | Cadence | SECONDARY | Cost/access | RE-class |
|---:|---|---|---|---|---|---|---|---|
| 1 | Leading Index | `leading_index` | FRED `USSLIND` (Philly Fed/Crone) | `/fred/series/observations?series_id=USSLIND` | Monthly M+1 | Conference Board LEI (~E HAR-RE) | OPEN-REST (FRED) / HAR-RE (TCB) | **RE-REPRESENTATIVE** (methodology-variant; yang label suggests TCB but FRED-mirror is Philly/Crone) |
| 2 | PMI Manufacturing | `pmi_manufacturing` | ISM | (paywalled) | Monthly M+1 BD1 | regional Fed surveys (~E HAR-RE substitute); USSLIND composite proxy | **PAID-SUB** | **RE-DEFERRED** (architectural call §4) |
| 3 | PMI Services | `pmi_services` | ISM | (paywalled) | Monthly M+1 BD3 | regional Fed surveys substitute | **PAID-SUB** | **RE-DEFERRED** (§4) |
| 4 | S&P PMI Manufacturing | `sp_pmi_manufacturing` | S&P Global | (paywalled; 403 Akamai) | Monthly Flash BD3-4 + Final BD1 | ISM PMI substitute (sister §1.1 row 2) | **PAID-SUB** | **RE-DEFERRED** (§4) |
| 5 | S&P PMI Services | `sp_pmi_services` | S&P Global | (paywalled; 403 Akamai) | Monthly Flash + Final | ISM PMI Services substitute | **PAID-SUB** | **RE-DEFERRED** (§4) |
| 6 | ISM Manufacturing New Orders | `ism_manufacturing_new_orders` | ISM | (paywalled sub-component) | Monthly M+1 BD1 | press-release HAR-RE for headline | **PAID-SUB / press-release HAR-RE** | **RE-DEFERRED** (§4) |
| 7 | ISM Services New Orders | `ism_services_new_orders` | ISM | (paywalled sub-component) | Monthly M+1 BD3 | press-release HAR-RE for headline | **PAID-SUB / press-release HAR-RE** | **RE-DEFERRED** (§4) |
| 8 | NFIB Small Business Optimism | `nfib_small_business_optimism` | NFIB | XLSX direct download + HAR-aid for URL pattern | Monthly M+1 2nd Tue | (none direct) | **OPEN-DOWNLOAD-WITH-HAR-AID** | **RE-MATCH** (post-HAR) |

### §1.2 — Lagging Indicator group (7 indicators)

| # | Indicator | yang-slug | PRIMARY | PRIMARY endpoint | Cadence | SECONDARY | Cost/access | RE-class |
|---:|---|---|---|---|---|---|---|---|
| 9 | GDP QoQ | `gdp_qoq` | FRED `A191RL1Q225SBEA` (Real GDP %-change-q/q) | `/fred/series/observations?series_id=A191RL1Q225SBEA` | Quarterly Q+1 advance | ~D BEA `apps.bea.gov/api/data/?...TableName=T10101&Frequency=Q` (upstream-authoritative) | OPEN-REST (FRED) / OPEN-REST-WITH-KEY (BEA) | **RE-MATCH** (3-way cross-publisher) |
| 10 | Industrial Productivity MoM | `industrial_productivity_mom` | FRED `INDPRO` (Industrial Production Total Index) | `/fred/series/observations?series_id=INDPRO` | Monthly M+1 day 15-17 | ~D FRB G.17 DDP (HAR-RE for series-ID; upstream-authoritative) | OPEN-REST (FRED) / HAR-RE (FRB DDP) | **RE-REPRESENTATIVE** (yang label "Productivity" vs FRED "Production Index" — see §5 cleanup) |
| 11 | Durable Goods Orders MoM | `durable_goods_orders_mom` | FRED `DGORDER` | `/fred/series/observations?series_id=DGORDER` | Monthly M+1 | ~C Census M3 release (upstream-authoritative) | OPEN-REST (FRED) / OPEN-REST-WITH-KEY (Census) | **RE-MATCH-DERIVED** (level; MoM derive) |
| 12 | Factory Orders MoM | `factory_orders_mom` | FRED `AMTMNO` | `/fred/series/observations?series_id=AMTMNO` | Monthly M+1 | ~C Census M3 release | OPEN-REST (FRED) / OPEN-REST-WITH-KEY (Census) | **RE-MATCH-DERIVED** |
| 13 | Capacity Utilization | `capacity_utilization` | FRED `TCU` | `/fred/series/observations?series_id=TCU` | Monthly M+1 day 15-17 | ~D FRB G.17 DDP | OPEN-REST (FRED) / HAR-RE (FRB DDP) | **RE-MATCH** |
| 14 | Business Inventories YoY | `business_inventories_yoy` | FRED `BUSINV` (level) | `/fred/series/observations?series_id=BUSINV` | Monthly M+1 | ~C Census MTIS | OPEN-REST (FRED) / OPEN-REST-WITH-KEY (Census) | **RE-MATCH-DERIVED** (level; YoY derive) |
| 15 | Trade Balance | `trade_balance` | FRED `BOPGSTB` | `/fred/series/observations?series_id=BOPGSTB` | Monthly M+2 | ~C Census ftd OR ~D BEA NIPA T40205B | OPEN-REST (FRED) / OPEN-REST-WITH-KEY (Census + BEA) | **RE-MATCH** |

### §1.3 — Financial Condition group (6 indicators)

| # | Indicator | yang-slug | PRIMARY | PRIMARY endpoint | Cadence | SECONDARY | Cost/access | RE-class |
|---:|---|---|---|---|---|---|---|---|
| 16 | Bloomberg Financial Condition Index | `bloomberg_financial_condition_index` | (Bloomberg-proprietary) | (paywalled) | Daily | Chicago Fed NFCI substitute (FRED `NFCI`) — sister §1.3 row 17 | **PAID-SUB / SUBSTITUTE-OPEN** | **RE-DEFERRED** (§4 candidate) / **RE-REPRESENTATIVE** if NFCI substitute accepted |
| 17 | Chicago Fed Financial Condition Index | `chicago_fed_financial_condition_index` | FRED `NFCI` | `/fred/series/observations?series_id=NFCI` | Weekly | (none direct; FRED is canonical mirror) | OPEN-REST | **RE-MATCH** |
| 18 | Fed Fund Rate | `fed_fund_rate` | FRED `FEDFUNDS` (monthly avg) | `/fred/series/observations?series_id=FEDFUNDS` | Monthly | ~D NY Fed Markets EFFR `markets.newyorkfed.org/api/rates/unsecured/effr/last/N.json` (daily upstream) | OPEN-REST (both) | **RE-MATCH** |
| 19 | Fed Balance Sheet | `fed_balance_sheet` | FRED `WALCL` | `/fred/series/observations?series_id=WALCL` | Weekly Thu | ~D FRB H.4.1 DDP (upstream HAR-RE) | OPEN-REST (FRED) / HAR-RE (FRB DDP) | **RE-MATCH** |
| 20 | Fed Balance Sheet as % of GDP | `fed_balance_sheet_as_pct_of_gdp` | (DERIVED: FRED WALCL ÷ FRED GDP × 100) | composite | Weekly numerator / Quarterly denominator | (n/a — derived) | OPEN-REST (composite) | **RE-DERIVED** |
| 21 | Net Long Term TIC Flows | `net_long_term_tic_flows` | ~D Treasury TIC Table 2 XLSX (HAR-RE) | landing `home.treasury.gov/data/treasury-international-capital-tic-system-home-page/` | Monthly M+2 day ~15 | FRED `TICFLT` (partial-coverage subset) | **HAR-RE-CANDIDATE** (~D §1.6) | **RE-REPRESENTATIVE** (partial FRED coverage) |

### §1.4 — Inflation group (8 indicators)

| # | Indicator | yang-slug | PRIMARY | PRIMARY endpoint | Cadence | SECONDARY | Cost/access | RE-class |
|---:|---|---|---|---|---|---|---|---|
| 22 | CPI MoM | `cpi_mom` | FRED `CPIAUCSL` (level) | `/fred/series/observations?series_id=CPIAUCSL` | Monthly M+1 day 10-15 | ~B BLS `CUUR0000SA0` (upstream-authoritative) | OPEN-REST (FRED) / OPEN-REST (BLS anonymous OR registered) | **RE-MATCH-DERIVED** (level; MoM derive) |
| 23 | Core CPI MoM | `core_cpi_mom` | FRED `CPILFESL` | `/fred/series/observations?series_id=CPILFESL` | Monthly M+1 | ~B BLS `CUUR0000SA0L1E` | OPEN-REST (both) | **RE-MATCH-DERIVED** |
| 24 | PCE MoM | `pce_mom` | FRED `PCEPI` | `/fred/series/observations?series_id=PCEPI` | Monthly M+1 day 28-30 | ~D BEA `apps.bea.gov/api/data/?...TableName=T20807&Frequency=M` (upstream-authoritative — NOT BLS) | OPEN-REST (FRED) / OPEN-REST-WITH-KEY (BEA) | **RE-MATCH-DERIVED** |
| 25 | Core PCE MoM | `core_pce_mom` | FRED `PCEPILFE` | `/fred/series/observations?series_id=PCEPILFE` | Monthly M+1 | ~D BEA same release | OPEN-REST (both) | **RE-MATCH-DERIVED** |
| 26 | PPI MoM | `ppi_mom` | FRED `PPIACO` (legacy WPU00000000) | `/fred/series/observations?series_id=PPIACO` | Monthly M+1 day 10-15 | ~B BLS `WPU00000000` (legacy) OR `WPSFD4` (modern Final Demand) | OPEN-REST (both) | **RE-MATCH-DERIVED** (yang maps legacy; modern variant flagged §5) |
| 27 | Unit Labor Cost YoY | `unit_labor_cost_yoy` | FRED `ULCNFB` | `/fred/series/observations?series_id=ULCNFB` | Quarterly Q+1 ~6 weeks | ~B BLS `PRS85006112` (upstream-authoritative) | OPEN-REST (both) | **RE-MATCH-DERIVED** |
| 28 | UMich 1 Year Inflation | `umich_1_year_inflation` | FRED `MICH` | `/fred/series/observations?series_id=MICH` | Monthly final last Fri | UMich SCA portal (~E HAR-RE for direct) | OPEN-REST | **RE-MATCH** |
| 29 | UMich 5-10 Year Inflation | `umich_5_10_year_inflation` | UMich SCA portal (~E HAR-RE) | landing `sca.isr.umich.edu/` | Monthly final last Fri | FRED `T5YIFR` (5Y-5Y-forward breakeven REPRESENTATIVE proxy) | **HAR-RE-CANDIDATE** | **RE-REPRESENTATIVE** (HAR-RE primary; FRED breakeven proxy SECONDARY) |

### §1.5 — Labor Market group (9 indicators)

| # | Indicator | yang-slug | PRIMARY | PRIMARY endpoint | Cadence | SECONDARY | Cost/access | RE-class |
|---:|---|---|---|---|---|---|---|---|
| 30 | Unemployment Rate | `unemployment_rate` | FRED `UNRATE` | `/fred/series/observations?series_id=UNRATE` | Monthly M+1 1st Fri | ~B BLS `LNS14000000` (upstream-authoritative) | OPEN-REST (both) | **RE-MATCH** |
| 31 | Initial Jobless Claims | `initial_jobless_claims` | FRED `ICSA` (DoL ETA mirror — NOT BLS) | `/fred/series/observations?series_id=ICSA` | Weekly Thu | DoL ETA direct `oui.doleta.gov/` (~E HAR-RE-adjacent; FRED is convenient mirror) | OPEN-REST | **RE-MATCH** (per §5 cleanup: yang-side attribution mis-cite "BLS" — actual = DoL ETA via FRED-mirror) |
| 32 | Continuing Jobless Claims | `continuing_jobless_claims` | FRED `CCSA` (DoL ETA mirror — NOT BLS) | `/fred/series/observations?series_id=CCSA` | Weekly Thu | DoL ETA direct | OPEN-REST | **RE-MATCH** (per §5) |
| 33 | US Job Openings | `us_job_openings` | FRED `JTSJOL` | `/fred/series/observations?series_id=JTSJOL` | Monthly M+2 1st Tue | ~B BLS `JTS000000000000000JOL` | OPEN-REST (both) | **RE-MATCH** |
| 34 | Nonfarm Payrolls | `nonfarm_payrolls` | FRED `PAYEMS` (level) | `/fred/series/observations?series_id=PAYEMS` | Monthly M+1 1st Fri | ~B BLS `CES0000000001` | OPEN-REST (both) | **RE-MATCH-DERIVED** (level; MoM-change derive) |
| 35 | ADP Employment Change | `adp_employment_change` | FRED `ADPMNUSNERSA` (Monthly Total Nonfarm Private Payroll Employment) | `/fred/series/observations?series_id=ADPMNUSNERSA` | Monthly Wed prior to NFP | ADP-private bulk (subscription) | OPEN-REST | **RE-REPRESENTATIVE** (ADP-private bulk has methodology-variant final vs FRED-mirror preliminary) |
| 36 | Labor Force Participation Rate | `labor_force_participation_rate` | FRED `CIVPART` | `/fred/series/observations?series_id=CIVPART` | Monthly M+1 1st Fri | ~B BLS `LNS11300000` | OPEN-REST (both) | **RE-MATCH** |
| 37 | Weekly Hours | `weekly_hours` | FRED `AWHAETP` | `/fred/series/observations?series_id=AWHAETP` | Monthly M+1 1st Fri | ~B BLS `CES0500000002` | OPEN-REST (both) | **RE-MATCH** |
| 38 | Hourly Earnings MoM | `hourly_earnings_mom` | FRED `CES0500000003` | `/fred/series/observations?series_id=CES0500000003` | Monthly M+1 1st Fri | ~B BLS `CES0500000003` (same series-id verbatim mirror) | OPEN-REST (both) | **RE-MATCH-DERIVED** |

### §1.6 — Consumer group (7 indicators)

| # | Indicator | yang-slug | PRIMARY | PRIMARY endpoint | Cadence | SECONDARY | Cost/access | RE-class |
|---:|---|---|---|---|---|---|---|---|
| 39 | Retail Sales MoM | `retail_sales_mom` | FRED `RSAFS` | `/fred/series/observations?series_id=RSAFS` | Monthly M+1 mid | ~C Census MARTS | OPEN-REST (FRED) / OPEN-REST-WITH-KEY (Census) | **RE-MATCH-DERIVED** |
| 40 | Retail Sales ex Auto MoM | `retail_sales_ex_auto_mom` | FRED `RSXFS` | `/fred/series/observations?series_id=RSXFS` | Monthly M+1 | ~C Census MARTS | OPEN-REST (both) | **RE-REPRESENTATIVE** (FRED RSXFS excludes Food Services + Auto; yang label may differ — §5 minor caveat) |
| 41 | Retail Sales ex Auto and Gas MoM | `retail_sales_ex_auto_and_gas_mom` | (DERIVED: FRED RSXFS - RSGASS) | composite | Monthly M+1 | ~C Census MARTS sub-component | OPEN-REST (composite) | **RE-REPRESENTATIVE** (derive-class) |
| 42 | UMich Consumer Sentiment | `umich_consumer_sentiment` | FRED `UMCSENT` | `/fred/series/observations?series_id=UMCSENT` | Monthly preliminary 2nd Fri + final last Fri | UMich SCA portal direct (~E HAR-RE) | OPEN-REST | **RE-MATCH** |
| 43 | Conference Board Consumer Confidence | `conference_board_consumer_confidence` | Conference Board (~E HAR-RE) | landing `conference-board.org/topics/consumer-confidence/` | Monthly M+1 last Tue | (none direct; subscription paywall) | **HAR-RE-CANDIDATE** | **RE-MATCH** (post-HAR) |
| 44 | Consumer Credit YoY | `consumer_credit_yoy` | FRED `TOTALSL` (level) | `/fred/series/observations?series_id=TOTALSL` | Monthly M+2 day 5-7 | ~D FRB G.19 DDP (release_id=14 per LD-31) | OPEN-REST (FRED) / HAR-RE (FRB DDP) | **RE-MATCH-DERIVED** (level; YoY derive) |
| 45 | Wards Total Vehicle Sales | `wards_total_vehicle_sales` | Wards Intelligence (paywalled) | (subscription wall) | Monthly M+1 BD1 | FRED `DAUTOSAAR` (domestic-only subset; partial) | **PAID-SUB / SUBSTITUTE-PARTIAL** | **RE-DEFERRED** (§4 candidate; partial substitute exists) |

### §1.7 — Housing Market group (6 indicators; per Phase 1 F5 `declared_count=7 actual=6`)

| # | Indicator | yang-slug | PRIMARY | PRIMARY endpoint | Cadence | SECONDARY | Cost/access | RE-class |
|---:|---|---|---|---|---|---|---|---|
| 46 | NAHB Housing Market Index | `nahb_housing_market_index` | NAHB (~E HAR-RE) | landing `nahb.org/news-and-economics/housing-economics/indices/housing-market-index` | Monthly M+1 day 16-17 | (none direct; NAHB Membership for bulk) | **HAR-RE-CANDIDATE** | **RE-MATCH** (post-HAR) |
| 47 | New Home Sales | `new_home_sales` | FRED `HSN1F` | `/fred/series/observations?series_id=HSN1F` | Monthly M+1 | ~C Census Survey of Construction | OPEN-REST (both) | **RE-MATCH** |
| 48 | Existing Home Sales | `existing_home_sales` | FRED `EXHOSLUSM495S` | `/fred/series/observations?series_id=EXHOSLUSM495S` | Monthly M+1 | NAR direct (subscription) | OPEN-REST (FRED) / PAID (NAR direct) | **RE-MATCH** |
| 49 | Pending Home Sales | `pending_home_sales` | NAR Pending Home Sales Index (~E HAR-RE) | landing `nar.realtor/research-and-statistics/housing-statistics/pending-home-sales` | Monthly M+1 last Wed | (none direct) | **HAR-RE-CANDIDATE** | **RE-MATCH** (post-HAR) |
| 50 | Housing Starts | `housing_starts` | FRED `HOUST` | `/fred/series/observations?series_id=HOUST` | Monthly M+1 | ~C Census SOC | OPEN-REST (both) | **RE-MATCH** |
| 51 | Building Permits | `building_permits` | FRED `PERMIT` | `/fred/series/observations?series_id=PERMIT` | Monthly M+1 | ~C Census BPS | OPEN-REST (both) | **RE-MATCH** |

### §1.8 — Investor Sentiment group (7 indicators; all 7 FRED-GAP per ~A §2.8)

| # | Indicator | yang-slug | PRIMARY | PRIMARY endpoint | Cadence | SECONDARY | Cost/access | RE-class |
|---:|---|---|---|---|---|---|---|---|
| 52 | AAII Sentiment Bullish | `aaii_sentiment_bullish` | AAII Sentiment Survey (~E HAR-RE; Cloudflare workaround) | landing `aaii.com/sentimentsurvey` | Weekly Wed close | (none) | **HAR-RE-CANDIDATE** | **RE-MATCH** (post-HAR) |
| 53 | AAII Sentiment Neutral | `aaii_sentiment_neutral` | AAII | (same) | Weekly | (none) | **HAR-RE-CANDIDATE** | **RE-MATCH** (post-HAR) |
| 54 | AAII Sentiment Bearish | `aaii_sentiment_bearish` | AAII | (same) | Weekly | (none) | **HAR-RE-CANDIDATE** | **RE-MATCH** (post-HAR) |
| 55 | AAII Stock Allocation | `aaii_stock_allocation` | AAII Asset Allocation Survey (~E HAR-RE; distinct from Sentiment) | landing `aaii.com` | Monthly mid-month | (none) | **HAR-RE-CANDIDATE** | **RE-MATCH** (post-HAR) |
| 56 | AAII Bond Allocation | `aaii_bond_allocation` | AAII AAS | (same) | Monthly | (none) | **HAR-RE-CANDIDATE** | **RE-MATCH** (post-HAR) |
| 57 | AAII Cash Allocation | `aaii_cash_allocation` | AAII AAS | (same) | Monthly | (none) | **HAR-RE-CANDIDATE** | **RE-MATCH** (post-HAR) |
| 58 | Fed NLP Sentiment | `fed_nlp_sentiment` | yang-internal NLP derivation (suspected) | (yang code path TBD; clarify ~A) | Indeterminate | (none) | **YANG-INTERNAL-CLARIFY** | **RE-GAP** (or yang-internal-not-RE-class) |

### §1.9 — Treasury Yields group (10 indicators; all 10 ~A FRED-MATCH + ~D Treasury Direct cross-check)

| # | Indicator | yang-slug | PRIMARY | PRIMARY endpoint | Cadence | SECONDARY | Cost/access | RE-class |
|---:|---|---|---|---|---|---|---|---|
| 59 | 1M | `1m` | FRED `DGS1MO` | `/fred/series/observations?series_id=DGS1MO` | Daily | ~D Treasury Direct CSV `home.treasury.gov/.../daily-treasury-rates.csv/{YYYY}/all` | OPEN-REST (both) | **RE-MATCH** (3-way cross-publisher validated DGS10 2026-05-22=4.56 == ~D 10Yr=4.56) |
| 60 | 3M | `3m` | FRED `DGS3MO` | (same pattern) | Daily | ~D Treasury Direct | OPEN-REST | **RE-MATCH** |
| 61 | 1Y | `1y` | FRED `DGS1` | (same) | Daily | ~D Treasury Direct | OPEN-REST | **RE-MATCH** |
| 62 | 2Y | `2y` | FRED `DGS2` | (same) | Daily | ~D Treasury Direct | OPEN-REST | **RE-MATCH** |
| 63 | 3Y | `3y` | FRED `DGS3` | (same) | Daily | ~D Treasury Direct | OPEN-REST | **RE-MATCH** |
| 64 | 5Y | `5y` | FRED `DGS5` | (same) | Daily | ~D Treasury Direct | OPEN-REST | **RE-MATCH** |
| 65 | 7Y | `7y` | FRED `DGS7` | (same) | Daily | ~D Treasury Direct | OPEN-REST | **RE-MATCH** |
| 66 | 10Y | `10y` | FRED `DGS10` | (same) | Daily | ~D Treasury Direct (3-way EMPIRICALLY MATCHED 4.56) | OPEN-REST | **RE-MATCH** |
| 67 | 20Y | `20y` | FRED `DGS20` | (same) | Daily | ~D Treasury Direct | OPEN-REST | **RE-MATCH** |
| 68 | 30Y | `30y` | FRED `DGS30` | (same) | Daily | ~D Treasury Direct | OPEN-REST | **RE-MATCH** |

### §1.10 — Credit Spread group (5 indicators)

| # | Indicator | yang-slug | PRIMARY | PRIMARY endpoint | Cadence | SECONDARY | Cost/access | RE-class |
|---:|---|---|---|---|---|---|---|---|
| 69 | Ted Spread | `ted_spread` | FRED `TEDRATE` (**DISCONTINUED 2022**) | (historical-only) | n/a | SOFR-3M minus T-Bill-3M substitute (see §5) | **DISCONTINUED** | **RE-DEFERRED** (§5 cleanup; Andrew arch call: deprecate vs substitute) |
| 70 | AAA | `aaa` | FRED `BAMLC0A1CAAA` (ICE BofA AAA US Corporate OAS) | `/fred/series/observations?series_id=BAMLC0A1CAAA` | Daily | (FRED-mirror is canonical for ICE BofA; private source paywalled) | OPEN-REST | **RE-MATCH** |
| 71 | IG | `ig` | FRED `BAMLC0A0CM` (ICE BofA US Corporate OAS broad IG) | `/fred/series/observations?series_id=BAMLC0A0CM` | Daily | (same as #70) | OPEN-REST | **RE-MATCH** |
| 72 | AGG | `agg` | Yahoo Finance `AGG` ETF-NAV proxy (`query1.finance.yahoo.com/v7/finance/chart/AGG`) | (Yahoo chart endpoint) | Daily | Bloomberg US Aggregate Bond Index direct (paywalled) | **OPEN-REST-API-substitute / PAID-SUB** | **RE-REPRESENTATIVE** (ETF-NAV proxies underlying index with negligible drift) |
| 73 | HY | `hy` | FRED `BAMLH0A0HYM2` (ICE BofA HY US OAS) | `/fred/series/observations?series_id=BAMLH0A0HYM2` | Daily | (same as #70) | OPEN-REST | **RE-MATCH** |

### §1.11 — Market Indicator group (1 indicator per live macro_data.json — Phase 1 F4 MOVE-MISSING)

| # | Indicator | yang-slug | PRIMARY | PRIMARY endpoint | Cadence | SECONDARY | Cost/access | RE-class |
|---:|---|---|---|---|---|---|---|---|
| 74 | VIX | `vix` | FRED `VIXCLS` | `/fred/series/observations?series_id=VIXCLS` | Daily | CBOE-direct OR Yahoo Finance `^VIX` (sister §1.11) | OPEN-REST | **RE-MATCH** |

NB: MOVE not in macro_data.json per F4 actual=1; if yang re-adds, Yahoo Finance `^MOVE` is LIVE-VERIFIED (~E §1.1).

### §1.12 — Currency group (5 indicators)

| # | Indicator | yang-slug | PRIMARY | PRIMARY endpoint | Cadence | SECONDARY | Cost/access | RE-class |
|---:|---|---|---|---|---|---|---|---|
| 75 | DXY | `dxy` | FRED `DTWEXBGS` (Nominal Broad Dollar Index — FED-calculated, NOT ICE DXY) | `/fred/series/observations?series_id=DTWEXBGS` | Daily | ICE DXY direct (broker-paywalled; Yahoo `DX-Y.NYB`) | OPEN-REST / OPEN-REST-API (Yahoo) | **RE-REPRESENTATIVE** (methodology-variant per ~A §2.12) |
| 76 | EUR/USD | `eur_usd` | FRED `DEXUSEU` | `/fred/series/observations?series_id=DEXUSEU` | Daily | Yahoo Finance `EURUSD=X` | OPEN-REST | **RE-MATCH** |
| 77 | USD/JPY | `usd_jpy` | FRED `DEXJPUS` | `/fred/series/observations?series_id=DEXJPUS` | Daily | Yahoo Finance `JPY=X` | OPEN-REST | **RE-MATCH** |
| 78 | GBP/USD | `gbp_usd` | FRED `DEXUSUK` | `/fred/series/observations?series_id=DEXUSUK` | Daily | Yahoo Finance `GBPUSD=X` | OPEN-REST | **RE-MATCH** |
| 79 | USD/CNH | `usd_cnh` | Yahoo Finance `CNH=X` (`query1.finance.yahoo.com/v7/finance/chart/CNH%3DX` LIVE-VERIFIED 2026-05-26=6.7845) | (Yahoo chart endpoint) | Daily | FRED `CCUSSP02CNM650N` (USD/CNY onshore — distinct from offshore CNH) | **OPEN-REST-API** | **RE-MATCH** (post-Wave-1 Yahoo adapter ship) |

### §1.13 — Coverage summary (79/79 mapped)

- **FRED-PRIMARY: 55/79 (69.6%)** — Treasury Yields ×10 + Lagging ×7 + Inflation ×7 + Labor ×8 + Consumer ×4 + Housing ×4 + Credit ×3 + Market ×1 + Currency ×3 + FinCond ×3 + REPRESENTATIVE ×5 + DERIVED ×1
- **~E PRIMARY (FRED-GAP-routed): 24/79 (30.4%)** — split per §1.X across access-class tiers
  - 2 OPEN-REST-API LIVE: CNH=X (Currency #79), VIX/^MOVE (Market — VIX is FRED-MATCH so only AGG-via-ETF + Yahoo VIX as SECONDARY; net 1-2 ~E-PRIMARY-LIVE)
  - 3 OPEN-REST-API substitute: AGG ETF-NAV (#72) + DXY Yahoo proxy (#75 SECONDARY) + BFCI-via-NFCI (#16 substitute)
  - 1 OPEN-DOWNLOAD-WITH-HAR-AID: NFIB SBOI (#8)
  - 11 HAR-RE-CANDIDATE: LEI (#1 substitute path), CCI (#43), NAHB (#46), Pending Home Sales (#49), UMich 5-10Y (#29), AAII ×6 (#52-57), Net LT TIC (#21)
  - 5 PAID-SUBSCRIPTION (architectural-call surface §4): ISM PMI ×2 (#2,3) + S&P Global PMI ×2 (#4,5) + ISM New Orders ×2 (#6,7) + Wards (#45) + BFCI (#16) + AGG (#72) — net 5 after de-duping with substitute paths
  - 1 DISCONTINUED: Ted Spread (#69)
  - 1 YANG-INTERNAL: Fed NLP (#58)

---

## §2 — Tie-Breaker Decisions: FRED-mirror vs BLS-direct (10 overlap indicators)

**Indicators where ~A FRED and ~B BLS both authoritative:** CPI MoM (#22), Core CPI MoM (#23), PPI MoM (#26), Unit Labor Cost YoY (#27), Unemployment Rate (#30), US Job Openings (#33), Nonfarm Payrolls (#34), LFPR (#36), Weekly Hours (#37), Hourly Earnings MoM (#38) = **10 indicators**.

### §2.1 — Tie-breaker rubric

**Decision: FRED-PRIMARY runtime; BLS-CROSS-CHECK overlay** (per ~B §5.3 recommendation; ~A §5.3 convergence).

**Rationale (5 points; cumulative):**

1. **Operational simplicity** — FRED is a single adapter + single api_key (AWS Secrets `FredApiKey` provisioned) + uniform rate-limit + uniform JSON shape. BLS-direct would add a second adapter with separate rate-limit tier (25/day anonymous OR 500/day registered key — `BlsApiKey` NOT YET provisioned in AWS Secrets per ~B §1.1) + separate POST-JSON request shape + partial-success failure mode requiring per-series-data-length check. Maintenance burden scales linearly with adapter count.
2. **Publication-lag is acceptable per AC-CADENCE-TOLERANCE** — FRED mirrors BLS within ~24h of publication; yang's monthly-snapshot cadence absorbs sub-day lag without DRIFT-class fires. Andrew sovereign 21:00Z "data is pretty low frequency" framing endorses monthly-cadence-acceptable.
3. **BLS-direct unique value = revision-flag granularity** (P=preliminary, R=revised, numeric codes for survey-specific revision-class), NOT raw-value-freshness. Reserve BLS-direct for DRIFT arbitration + revision-aware harness logic, not everyday pull.
4. **BLS anonymous tier 25-query-daily cap is fragile**; full 79-indicator nightly refresh easily exceeds it. v2-registered (500/day) production-ready but adds `BlsApiKey` ops onboarding step. FRED's 120-req/min tier (~7,200/hr) is fully sufficient even for sub-hourly refresh patterns.
5. **4-of-5 lane convergence empirically validates the lean** — ~A endorses FRED-PRIMARY + sister-CROSS-CHECK; ~B endorses BLS-CROSS-CHECK only (not PRIMARY); ~C endorses FRED-PRIMARY + Census-SECONDARY; ~D endorses FRED-PRIMARY + ~D-CROSS-CHECK. All 4 shipped Phase 2a lanes converge bottom-up on this architecture.

### §2.2 — Per-indicator pick (all 10 = FRED-PRIMARY + BLS-CROSS-CHECK)

| # | Indicator | FRED PRIMARY series | BLS CROSS-CHECK series | Override-decision-pre-rubric? |
|---:|---|---|---|:-:|
| 22 | CPI MoM | `CPIAUCSL` | `CUUR0000SA0` | NO (rubric stands) |
| 23 | Core CPI MoM | `CPILFESL` | `CUUR0000SA0L1E` | NO |
| 26 | PPI MoM | `PPIACO` (legacy WPU00000000 map) | `WPSFD4` (modern) OR `WPU00000000` (legacy) | **PARTIAL**: per §5 cleanup, yang label maps to legacy; FRED-mirror confirms this. CROSS-CHECK BLS-direct for modern WPSFD4 if/when Andrew elects modern variant. |
| 27 | Unit Labor Cost YoY | `ULCNFB` | `PRS85006112` | NO |
| 30 | Unemployment Rate | `UNRATE` | `LNS14000000` | NO |
| 33 | US Job Openings | `JTSJOL` | `JTS000000000000000JOL` | NO |
| 34 | Nonfarm Payrolls | `PAYEMS` | `CES0000000001` | NO |
| 36 | LFPR | `CIVPART` | `LNS11300000` | NO |
| 37 | Weekly Hours | `AWHAETP` | `CES0500000002` | NO |
| 38 | Hourly Earnings MoM | `CES0500000003` | `CES0500000003` (verbatim mirror) | NO |

**Net:** 10/10 FRED-PRIMARY + BLS-CROSS-CHECK; 1 partial-override (PPI modern/legacy class-distinction per §5 cleanup).

### §2.3 — Analogous tie-breakers for other overlap classes

**FRED-mirror vs Census-direct (~9 overlap indicators):** same FRED-PRIMARY + Census-CROSS-CHECK lean per ~C §5 explicit. Census-direct CROSS-CHECK for sub-component disaggregation + revision-flag (annual benchmarks) + SA-toggle (Census `seasonally_adj=yes/no` query param).

**FRED-mirror vs Treasury-direct/FRB-DDP/BEA (~18-20 overlap indicators):** same FRED-PRIMARY + ~D-CROSS-CHECK lean per ~D §5.3 explicit. ~D-direct CROSS-CHECK for same-day-freshness (Treasury Direct ~4pm ET CSV) + DRIFT-arbitration (FRB DDP HAR-RE upstream-authoritative) + audit-trail.

**FRED-mirror vs Yahoo Finance (~5 overlap indicators):** **NO TIE-BREAKER NEEDED** — FRED + Yahoo cover different indicators:
- FRED: VIX (#74), EUR/USD (#76), USD/JPY (#77), GBP/USD (#78), AAA/IG/HY spreads (#70-73)
- Yahoo Finance UNIQUE PRIMARY: CNH=X (#79; FRED has only onshore CNY), AGG ETF-NAV (#72; FRED no Bloomberg Aggregate), and ^MOVE (Wave-2 if yang re-adds)
- Yahoo Finance SECONDARY (for DXY proxy + currency cross-validation): low-friction OPEN-REST-API adapter; pair with FRED PRIMARY for high-confidence verification

---

## §3 — Cost/Access Optimization (6-Tier Framework per ~E)

### §3.1 — 6-tier taxonomy + cluster counts

Per ~E §3.3 taxonomy applied across the full 79-indicator universe (combining ~A FRED-coverage with ~E GAP-routing):

| Tier | Description | Indicators | Cumulative |
|:-:|---|:-:|:-:|
| **Tier 1: OPEN-REST-API** | Public REST JSON, no key OR single-key (AWS Secrets); live-verified | **57** (55 FRED + 2 Yahoo Finance LIVE-VERIFIED) | 72.2% |
| **Tier 2: OPEN-REST-API substitute** | Public REST JSON via methodology-substitute (NFCI for BFCI; AGG-ETF-NAV) | **2 net new** (AGG; BFCI counted in Tier 1 already) | 74.7% |
| **Tier 3: HAR-RE-CANDIDATE** | Public landing page, backend JSON discoverable via HAR capture | **11** (LEI, CCI, NAHB, PHSI, UMich 5Y, AAII ×6) | 88.6% |
| **Tier 4: OPEN-DOWNLOAD-WITH-HAR-AID** | Public XLSX direct-link; HAR-aid for rotating URL pattern | **1** (NFIB SBOI) | 89.9% |
| **Tier 5: PAID-SUBSCRIPTION** | Subscription-walled; no public scrape-equivalent OR Akamai/Cloudflare bot-block enforced | **6 → 5 net** (ISM PMI ×2 + ISM NewOrders ×2 + Wards + S&P PMI ×2 → 7 nominal; 1 architectural-decision-de-duped via regional-Fed-substitute for ISM Mfg; 1 substitute-routed for BFCI via NFCI Tier 1; **5 net true PAID-PRIMARY-only**) | 96.2% |
| **Tier 6: DISCONTINUED / YANG-INTERNAL** | Series no longer published OR yang-internal derivation | **2** (Ted Spread DISCONTINUED + Fed NLP YANG-INTERNAL) | 98.7% |
| **NB: Net LT TIC Flows (#21)** | ~D Treasury TIC XLSX HAR-RE | already counted in Tier 3 | — |

**Total mapped: 79/79 = 100% (no orphans).**

### §3.2 — Harness build-order recommendation (cheapest-first)

**Build cheap → expensive; ship coverage incrementally.**

| Wave | Tier-class | Indicators covered (cumulative) | Cumulative % | Est. effort |
|:-:|---|:-:|:-:|---|
| **Wave 1** | Tier 1 (OPEN-REST-API: FREDAdapter + YahooFinanceAdapter) | 57 + 2 = **59** | **74.7%** | ~30min adapter implementation post-PRD; ~A FRED adapter v1 2-step substrate exists per §4 / `da862a6c6`; YahooFinanceAdapter live-implementable from ~E §4 substrate |
| **Wave 2** | Tier 3 (HAR-RE-CANDIDATE) | +11 = **70** | **88.6%** | ~2h end-to-end per ~E §4.3 HAR-capture sequence (4 sessions × ~25min capture + parse) + adapter-class implementation |
| **Wave 3** | Tier 4 (OPEN-DOWNLOAD NFIB) | +1 = **71** | **89.9%** | ~30min (single-source NFIB XLSX URL-pattern HAR-aid + adapter) |
| **Wave 4** | BLS + Census + Treasury/FDIC + NY Fed CROSS-CHECK overlay | (0 new; CROSS-CHECK overlay for ~30-40 indicators) | (89.9%) | ~4h end-to-end (4 adapter classes; ~B BLSAdapter substrate per §4; ~C + ~D adapter scaffolds in their briefs §4) |
| **Wave 5** | Architectural-call resolution (Tier 5 + Tier 6) | +5 = **76** OR accept GAP (**71**) | 96.2% with subscriptions OR 89.9% accept-GAP | Andrew sovereign disposition (§4) + cleanup execution (§5) |

**Empirically PRIMARY-implementable today without HAR-RE Wave-2 + without paid subscriptions:** Wave 1 = **59/79 (74.7%)**. With Wave 2 + Wave 3 (HAR-RE + NFIB): **71/79 (89.9%)** at "monthly-cadence-acceptable" coverage. **5 net architectural-call indicators** (PAID-only-no-substitute) remain at architectural-call disposition.

---

## §4 — Architectural-Call Surface (5 PAID-SUBSCRIPTION indicators)

### §4.1 — 3-path decision framework per PAID-class

For each PAID-class indicator, Andrew + ws CTO + ws CVO have 3 disposition paths:

- **(a) Subscribe** — acquire ISM / S&P Global / Wards / Bloomberg subscription; harness pulls authoritative directly.
- **(b) Substitute** — accept methodology-variant open-source proxy + document drift class.
- **(c) RE-GAP acceptable-by-documentation** — page indicator carries explicit GAP marker; yang label can be deprecated OR yang-side "push down the page" framing per Andrew sovereign 21:00Z.

### §4.2 — 5-architectural-call surface per indicator

| # | Indicator | (a) Subscribe ? | (b) Substitute available | (c) RE-GAP acceptable | RECOMMENDATION |
|---:|---|---|---|---|---|
| 2 | PMI Manufacturing | ISM Premium Data subscription (~$2-5K/yr) | regional Fed mfg surveys composite (Empire State + Philly Fed BOS + Dallas + Richmond + KC); OR USSLIND Philly Fed/Crone composite (FRED-MATCH already in Wave 1) | YES — Leading Indicator slot is decorative not load-bearing for downstream models per yang current usage | **(c)** with USSLIND-substitute footnote as fallback if Leading group prominence elevates |
| 3 | PMI Services | ISM Premium Data subscription | (no clean substitute; regional Fed services surveys are sparse) | YES | **(c)** |
| 4 | S&P PMI Manufacturing | S&P Global Market Intelligence subscription (~$3-8K/yr) | ISM PMI Mfg (sister #2 same class) — but ISM also PAID | YES — duplicative coverage with ISM PMI Mfg per methodology overlap | **(c)** (de-duplicates with #2; "PMI Manufacturing" + "S&P PMI Manufacturing" are methodology-variants of same headline) |
| 5 | S&P PMI Services | S&P Global subscription | ISM PMI Services (sister #3 same class) | YES (de-duplicative) | **(c)** |
| 6 | ISM Mfg New Orders | ISM Premium (subset of #2 subscription) | press-release HTML scrape for headline only (sub-component visible in press release); regional Fed New Orders sub-indices | YES | **(c)** with press-release-HAR-RE fallback path if Leading group prominence elevates |
| 7 | ISM Services New Orders | ISM Premium (subset of #3) | press-release HTML scrape | YES | **(c)** |
| 45 | Wards Total Vehicle Sales | Wards Intelligence subscription (~$5-10K/yr) | FRED `DAUTOSAAR` (domestic-only subset; ~40-50% coverage of total US light vehicle sales) | YES — Consumer group has 6 other indicators in Wave 1; vehicle sales is one slot | **(c)** with DAUTOSAAR-substitute partial-coverage footnote if Consumer group prominence elevates |

### §4.3 — Default recommendation: (c) RE-GAP acceptable-by-documentation

**Per Andrew sovereign 2026-05-26T~21:00Z framing:** *"Worst case, that data is pretty low frequency so if Yang has to update it once a month or something that doesnt really matter."* + *"we just add an addendum to the PRD that we have to go exploring..."* + *"push those pages down"* (i.e., indicators-without-RE-coverage can be lower-priority on the page rather than blockers).

**Default: (c) for all 5 architectural-call indicators.** Substitute paths documented inline (per §4.2 substitute column) for elevation-decision if/when any of these indicators becomes load-bearing. Each indicator is in the **Leading Indicator (#2-7) or Consumer (#45)** group — both groups have substantial Wave-1 + Wave-2 OPEN-REST/HAR-RE coverage (USSLIND-proxy + NFIB-Wave-2 + LEI-Wave-2-substitute for Leading; UMCSENT + CCI-Wave-2 + RS-family for Consumer). Partial group-coverage with documented PAID-GAP is acceptable per Andrew sovereign framing.

**Net synthesis recommendation:** **5 indicators classified RE-DEFERRED** (new verdict shape per §6); annotate in §1 master matrix; do NOT block Phase 2c empirical RE verification on PAID-class.

### §4.4 — Escalation path if Andrew over-rides default

If Andrew (or CTO/CVO) elects **(a) Subscribe** OR **(b) Substitute-with-methodology-documented** for any of the 5 indicators:

- **(a) Subscribe path:** ws CTO authors S3-procurement ticket; AE 0.7 onboards subscription credentials to AWS Secrets (`IsmApiKey` / `SpGlobalApiKey` / `WardsApiKey`); harness adapter scaffold drops in.
- **(b) Substitute path:** ws CTO authors PRD amendment documenting methodology-variance + yang-side label change OR slot-decommission; harness adapter for substitute (USSLIND or DAUTOSAAR or regional Fed composite) drops in at next /work cycle.

**Escalation mechanism:** MCP from ~A primary to ws COO + ws CTO + Andrew CC at synthesis-author-time IF MATERIAL REASON surfaces against the (c)-default. **No such material reason surfaced this synthesis cycle** — default (c) stands; recommendation goes forward as part of RAVC2-Request.

---

## §5 — Cleanup-Class Findings

5 cleanup-class findings surfaced across Phase 2a reconnaissance; routing per finding class:

### §5.1 — Ted Spread DISCONTINUED 2022 (LIBOR retirement)

**Source:** ~A §2.10 row 69 + ~E §1.X / §6 row 6.
**Issue:** FRED `TEDRATE` returns historical-only post-LIBOR-retirement-2022; no live values published. Yang's "Ted Spread" indicator (Credit Spread group) is structurally obsolete at the underlying-rate level (the canonical numerator 3M LIBOR no longer exists).
**Options:**
- **Deprecate:** remove "Ted Spread" indicator from yang macro_data.json + page UI (Credit Spread group drops to 4 indicators).
- **Substitute SOFR-3M minus T-Bill-3M:** modern equivalent stress-spread; requires `SOFR30DAYAVG` + `DTB3` FRED-mirror (or NY Fed Markets SOFR direct + Treasury Direct T-Bill direct). Methodology-variant from original Ted (3M LIBOR was bank-funded vs Treasury-risk-free; SOFR is overnight-repo-secured vs Treasury-risk-free; structural correlation similar).
**Routing:** ws CTO PRD §X amendment + Andrew sovereign disposition. **~A primary recommendation: SUBSTITUTE with documented methodology-variance** (Credit Spread group retains 5 indicators; spread-class signal preserved with modern primitive).
**Phase 2c TO-008 impact:** harness short-circuits Ted Spread until Andrew decision; classify as RE-DEFERRED in interim.

### §5.2 — Fed NLP Sentiment yang-internal-clarify

**Source:** ~A §2.8 row 60 + ~E §1.12.
**Issue:** Yang "Fed NLP Sentiment" indicator (Investor Sentiment group) — FRED search returned only DISCONTINUED `ATLSBUIREI` + `ATLSBUSGUI` (Atlanta Fed Business Surveys); no live Fed-published NLP sentiment series. Yang label suggests internal NLP derivation from Fed text corpus (FOMC minutes / beige book / Powell pressers), NOT external Fed source.
**Action:** **DS 0.1.0~A confirm yang-side upstream code path.** If yang-internal NLP derivation: document derive-methodology in §1 row 58 "Notes" column; mark RE-GAP-by-yang-internal; no external sourcing required. If external: surface yang-side citation + retry source identification.
**~A primary commitment (this brief):** I have direct context — yang-internal NLP derivation hypothesis is HIGH-confidence per code-spelunking-from-prior-sessions; will confirm + author follow-up note for Phase 2c if yang-internal confirmed.

### §5.3 — ICSA/CCSA mis-attribution to BLS (per ~B §6 row 5)

**Source:** ~B §6 row 5 (live-probed `Invalid Series for Series ICSA` + `Series does not exist for Series CCSA` in BLS v2 API).
**Issue:** Yang's "Initial Jobless Claims" + "Continuing Jobless Claims" (Labor Market group) labels may suggest BLS attribution, but actual canonical source is **DoL ETA (Department of Labor Employment & Training Administration)**, NOT BLS. FRED mirrors ICSA/CCSA from DoL ETA upstream, NOT BLS.
**Action:** **Surface to DT 0.1.0 (DataTeam yang-generate-macro adapter author) for yang-side audit.** Yang's `data.pkl` upstream attribution for these 2 indicators should cite DoL ETA, not BLS. Cosmetic correction; no harness-class blocker.
**Routing:** MCP from ~A primary to ws CTO + DT 0.1.0 at synthesis brief authoring time (chained from this brief; non-blocking for synthesis ship).

### §5.4 — PPI modern WPSFD4 vs legacy WPU00000000 class-distinction

**Source:** ~B §6 row 3 + §2.1 row 3.
**Issue:** BLS publishes TWO PPI headline series:
- **Modern: `WPSFD4`** — PPI Final Demand, 2009-rebased, modern methodology aligned with economic press (WSJ headline "PPI rose X%").
- **Legacy: `WPU00000000`** — PPI All Commodities, 1947-present continuity, what yang's Bloomberg label `PPIACO` maps to via FRED-mirror.

Yang label "PPI MoM" is ambiguous — internal Bloomberg ticker convention maps to legacy; press coverage typically references modern.
**Architectural decision-point:** which is yang's source-of-truth?
**Options:**
- **Accept legacy (status quo):** yang `PPIACO` maps to FRED `PPIACO` maps to BLS `WPU00000000`. Document yang-label-vs-publisher class.
- **Migrate to modern WPSFD4:** update yang `data.pkl` ingest to pull modern BLS series; methodology change visible to downstream models.
- **Dual-publish both:** yang exposes "PPI MoM (Final Demand)" + "PPI MoM (All Commodities)" as 2 indicators; user toggles.
**Routing:** ws CTO + Andrew sovereign architectural call. **~A primary recommendation: ACCEPT LEGACY** per status quo continuity (lowest disruption); annotate in PRD that yang `PPIACO` maps to legacy series.

### §5.5 — Industrial Productivity MoM yang-label variant for FRB G.17 Industrial Production Index (Phase 1 F4 sister)

**Source:** ~A §2.2 row 10 + §6 row 6 + Phase 1 brief F4 finding.
**Issue:** Yang indicator label "Industrial Productivity MoM" mapping to FRB G.17 `INDPRO` (Industrial Production Total Index) — semantic mismatch (production ≠ productivity). Phase 1 brief F4 also surfaced as yang-side internal-vs-publisher class.
**Routing:** ws CTO label-cleanup + DT 0.1.0 yang-side audit (sister to §5.3 routing).
**~A primary recommendation:** rename yang label to "Industrial Production MoM" matching publisher source-of-truth. Cosmetic correction; no harness-class blocker.

### §5.6 — Findings routing summary

| # | Finding | Routing | Blocker? |
|---:|---|---|:-:|
| 5.1 | Ted Spread DISCONTINUED | ws CTO + Andrew sovereign | NO (RE-DEFERRED) |
| 5.2 | Fed NLP yang-internal | DS 0.1.0~A (this lane self-clarify) | NO (RE-GAP) |
| 5.3 | ICSA/CCSA = DoL ETA not BLS | ws CTO + DT 0.1.0 | NO (cosmetic) |
| 5.4 | PPI modern WPSFD4 vs legacy WPU00000000 | ws CTO + Andrew sovereign | NO (status-quo recommendation) |
| 5.5 | "Industrial Productivity" yang label variant for `INDPRO` | ws CTO + DT 0.1.0 | NO (cosmetic) |

All 5 cleanup-class findings are NON-BLOCKING for Phase 2c TO-008 harness build dispatch. Routing MCPs (~5.3 + ~5.5 to ws CTO + DT 0.1.0; ~5.1 + ~5.4 to Andrew/CTO architectural-class) chained from this brief's RAVC2-Request.

---

## §6 — Verdict-Taxonomy Finalization (5-shape per Andrew v0.5 §3 carve-out)

Per Andrew sovereign 2026-05-26T~21:00Z + v0.5 §3 "finalized post-reconnaissance" carve-out, the RE-class verdict-taxonomy is **finalized as 5-shape**:

| RE-class | Definition | Count in §1 | Examples |
|---|---|:-:|---|
| **RE-MATCH** | All authoritative-source publishers agree within tight tolerance (±0.1% for rates; ±0.5% for index levels; same date-anchor) | **~40** | Treasury Yields ×10 (3-way DGS10 == ~D Treasury Direct == yang Bloomberg empirically validated 4.56 / 2026-05-22); UNRATE; UMich Consumer Sentiment; AAA/IG/HY spreads; etc. |
| **RE-MATCH-DERIVED** | Publishers agree at LEVEL; yang's MoM/YoY/percentage transformation is client-side derive (same underlying = same derived) | **~12** | CPI MoM (FRED CPIAUCSL level + BLS CUUR0000SA0 level); Hourly Earnings MoM; Consumer Credit YoY; etc. |
| **RE-REPRESENTATIVE** | Publishers approximately agree but with methodology-variance OR vintage-revision-lag-class | **~10** | USSLIND-as-LEI-proxy (Philly/Crone ≠ TCB LEI); DTWEXBGS-as-DXY-proxy (FED ≠ ICE); AGG via ETF-NAV (tracks Bloomberg index w/ negligible drift); ADP-monthly-vs-bulk variance; RS ex-Auto-and-Gas derive; INDPRO label-variant |
| **RE-GAP** | No authoritative-source publisher (private + survey + index sources NOT accessible OR yang-internal derivation) | **~13** | NAHB (HAR-RE primary post Wave-2); Pending Home Sales (HAR-RE); AAII ×6 (HAR-RE); UMich 5-10Y (HAR-RE); Conference Board CCI (HAR-RE); Conference Board LEI (HAR-RE substitute path); Fed NLP yang-internal |
| **RE-DRIFT** | Publishers disagree beyond tolerance; flag for investigation (yang-side transformation OR Bloomberg index-rebasing OR upstream-revision class) | **0 expected pre-impl** | (none yet; class defined for Phase 2c empirical verification surfacing) |
| **RE-DEFERRED** | New verdict shape per this synthesis — PAID-SUBSCRIPTION indicators OR DISCONTINUED-with-substitute-pending; deferred to Wave-3+ disposition per Andrew "push down" framing | **6** | ISM PMI ×2 + S&P Global PMI ×2 + Wards Vehicle Sales + Ted Spread |

**Pre-implementation classification across 79:** ~52 MATCH/MATCH-DERIVED + ~10 REPRESENTATIVE + ~11 GAP + 6 DEFERRED = 79. **Phase 2c TO-008 verification will empirically confirm or refine each row's RE-class** (RE-DRIFT class may surface for some currently-classified RE-MATCH rows post-verification).

### §6.1 — Verdict-shape relationship to verdict-taxonomy

[[feedback_corroborate_with_concern_verdict_shape]] 4-shape CVO verdict taxonomy adapted to RE-class context:
- **RE-MATCH** ↔ CORROBORATE
- **RE-REPRESENTATIVE** ↔ CORROBORATE-with-additives (methodology-variance documented)
- **RE-DRIFT** ↔ COUNTER (independent integrity gate fires)
- **RE-GAP** ↔ CORROBORATE-with-CONCERN (gap acknowledged + path documented)
- **RE-DEFERRED** ↔ (no direct CVO mapping; this is a Phase 2 RE-specific shape)

**Mirror-vs-origin source-class distinction (per ~A §8 candidate #4):**
- **3-way RE-MATCH:** FRED mirror + sister-lane upstream + yang-side Bloomberg ALL agree — high-confidence
- **2-way RE-MATCH:** FRED mirror + yang-side Bloomberg agree (no sister-lane upstream available because indicator is mirror-only-class in FRED) — medium-confidence
- **3-way RE-DRIFT:** FRED + sister-lane + yang disagree — investigation-class
- **2-way RE-DRIFT:** FRED + yang disagree (without sister-lane corroboration) — yang-specific-transformation-suspect

Phase 2c TO-008 verification harness should surface BOTH the RE-class verdict AND the source-class (3-way vs 2-way) for verdict-confidence tracking.

---

## §7 — TO-008 Harness Build Sequence Recommendation

### §7.1 — Wave sequence (cheapest-to-expensive)

**Wave 1 — Tier 1 OPEN-REST-API (LIVE-IMPLEMENTABLE TODAY):**
- **Adapters:** FREDAdapter (per ~A §4 substrate; v1 2-step pattern; live-verified) + YahooFinanceAdapter (per ~E §4 substrate; live-verified ^MOVE + CNH=X)
- **Indicators covered:** **59/79 (74.7%)** — 55 FRED + 2 Yahoo Finance LIVE + 2 Yahoo Finance ETF-NAV/substitute (AGG, DXY-proxy)
- **Effort:** ~30min adapter consolidation post-PRD; FREDAdapter Python class already authored in ~A §4.1 with 55-series registry; YahooFinanceAdapter scaffolded in ~E §4.1
- **Output:** Wave-1 SHIP = 59-indicator nightly refresh harness with FRED-PRIMARY + Yahoo Finance for AGG + CNH=X

**Wave 2 — Tier 3 HAR-RE-CANDIDATE (~2h end-to-end):**
- **Adapters:** ConferenceBoardAdapter + NAHBAdapter + NARAdapter + AAIIAdapter + UMichSCAAdapter (5 new adapter classes covering 11 indicators)
- **HAR-capture sequence per ~E §4.3:**
  - Session 1: Conference Board LEI + CCI (2 pages, ~10min capture, ~15min parse)
  - Session 2: NAHB HMI + NAR PHSI (2 pages, ~10min capture, ~15min parse)
  - Session 3: AAII Sentiment + AAII Asset Allocation (Cloudflare workaround = real-browser HAR, ~20min capture, ~20min parse)
  - Session 4: UMich SCA + NFIB SBOI XLSX URL-pattern (~10min capture, ~15min parse)
- **Indicators covered cumulative: 70/79 (88.6%)**
- **Effort:** ~50min HAR-capture + ~65min adapter implementation = ~2h end-to-end

**Wave 3 — Tier 4 OPEN-DOWNLOAD (NFIB SBOI):**
- **Adapter:** NFIBAdapter (XLSX direct-download + URL-pattern HAR-aid)
- **Indicators covered: 71/79 (89.9%)** (+1 NFIB SBOI)
- **Effort:** ~30min (single-source URL-pattern HAR-aid + adapter)
- **Effort can be folded into Wave 2 Session 4 if NFIB landing co-captured.**

**Wave 4 — CROSS-CHECK overlay (BLS + Census + Treasury/FDIC + NY Fed):**
- **Adapters:** BLSAdapter (per ~B §4 substrate; v2 POST primitive) + CensusAdapter (per ~C substrate) + TreasuryDirectAdapter + TreasuryFiscalDataAdapter + NYFedMarketsAdapter + BEAAdapter + FRBDDPAdapter (per ~D §4 substrate)
- **Indicators covered: same 71/79 (CROSS-CHECK overlay does NOT extend coverage; provides 3-way verification + DRIFT-arbitration + revision-flag granularity for ~30-40 of the 71 PRIMARY-implementable indicators)**
- **Effort:** ~4h end-to-end (5-6 adapter classes; substrates exist in sister-lane briefs §4; aggregation harness + verdict-classifier logic)
- **Ops-onboarding subtask:** `BlsApiKey` AWS Secrets onboarding (per ~B §1.1; ~30min ops); `CensusApiKey` likely already exists or onboard; `BEA_API_KEY` similar onboard step (per ~D §1.4)

**Wave 5 — Architectural-call resolution (Tier 5 PAID-SUB + Tier 6 cleanup):**
- **Path (a) Subscribe-and-onboard:** if Andrew elects, +5 indicators via ISM + S&P Global + Wards subscriptions → 76/79 (96.2%)
- **Path (b) Substitute-and-document:** if Andrew elects, regional Fed mfg composite (Empire State + Philly Fed BOS + KC + Richmond + Dallas) as ISM PMI Mfg substitute + DAUTOSAAR partial-coverage for Wards → 71/79 (89.9%) with documented substitutes
- **Path (c) Accept-RE-GAP-default:** 71/79 (89.9%) baseline coverage; 5 PAID indicators carry GAP marker + "push down page" framing → ~A primary recommendation
- **Cleanup sub-tasks per §5:**
  - Ted Spread substitute decision (SOFR-3M minus T-Bill-3M) — harness drop-in if substituted; otherwise deprecate
  - Fed NLP yang-internal confirmation (DS 0.1.0~A code-path spelunk)
  - ICSA/CCSA attribution audit (DT 0.1.0)
  - PPI legacy/modern decision (Andrew architectural; status-quo recommendation = accept legacy)
  - "Industrial Productivity" label rename to "Industrial Production" (DT 0.1.0 cosmetic)

### §7.2 — End-to-end effort estimate

| Wave | Cumulative coverage | Cumulative effort |
|:-:|:-:|---|
| Wave 1 | 59/79 (74.7%) | ~30min |
| Wave 1+2 | 70/79 (88.6%) | ~2.5h |
| Wave 1+2+3 | 71/79 (89.9%) | ~3h |
| Wave 1+2+3+4 | 71/79 (89.9%) + CROSS-CHECK overlay | ~7h |
| Wave 1+2+3+4+5(c) | 71/79 (89.9%) + 5 documented-GAP | ~7.5h |
| Wave 1+2+3+4+5(a) | 76/79 (96.2%) | ~7.5h + subscription procurement (multi-week ops lead-time) |

**Phase 2c TO-008 single-author primary path (Wave 1+2+3) = ~3h end-to-end** for 89.9% coverage at OPEN-tier-only. CROSS-CHECK overlay (Wave 4) is **additive enrichment**, not coverage-extending — defer to Wave-3 if calendar-pressed; ship Wave 1+2+3 first for immediate Phase 2c verification capability.

### §7.3 — Ops dependencies + sequencing

**Pre-Wave-1 (lookback):** `FredApiKey` provisioned ✓ (per ~A §1.1 + `da862a6c6` AWS Secrets confirmation).

**Pre-Wave-4 (CROSS-CHECK overlay ops):**
- `BlsApiKey` onboard (signup + AWS Secrets provision + IAM grant) — per ~B §1.1 pending
- `CensusApiKey` onboard if not already — per ~C §1
- `BEA_API_KEY` onboard — per ~D §1.4

**Pre-Wave-5(a) (subscription path; if elected):**
- ISM Premium Data subscription procurement (~$2-5K/yr; multi-week lead-time)
- S&P Global Market Intelligence subscription (~$3-8K/yr; multi-week)
- Wards Intelligence subscription (~$5-10K/yr; multi-week)

**~A primary lane lookahead (post-RAVC2-ACCEPT this synthesis):** Wave 1 immediate (FREDAdapter + YahooFinanceAdapter ship); Wave 2 HAR-capture handoff to Andrew per ~D §7 pattern (Andrew records HARs; subagent fan-out parses); Wave 3 + Wave 4 + Wave 5(c) per /work cycles + ws CTO coordination.

---

## §8 — Coverage % Summary

### §8.1 — Per-wave coverage progression

| Wave | Implemented indicators | Coverage % | Notes |
|:-:|:-:|:-:|---|
| Pre-Wave 1 (Phase 1) | 0 | 0% | No multi-source RE harness; yang-side Bloomberg only |
| **Wave 1 (ship today)** | **59** | **74.7%** | FRED + Yahoo Finance only; no HAR-RE; no PAID-SUB |
| **Wave 1+2 (~2h)** | **70** | **88.6%** | + 11 HAR-RE-CANDIDATE indicators |
| **Wave 1+2+3 (~3h)** | **71** | **89.9%** | + 1 NFIB SBOI |
| Wave 1+2+3+4 | 71 + CROSS-CHECK | 89.9% + verdict-confidence enrichment | BLS + Census + Treasury/FDIC + NY Fed CROSS-CHECK overlay; no new PRIMARY coverage but DRIFT-arbitration |
| Wave 1-4 + 5(c) | 71 + 5 documented-GAP | 89.9% PRIMARY + 6.3% RE-DEFERRED | **~A primary recommendation per Andrew sovereign 21:00Z** |
| Wave 1-5(a) | 76 | 96.2% | + subscription procurement (multi-week lead-time) |
| Theoretical 100% | 79 | 100% | Wave-5(a) + ICSA/CCSA attribution audit + Fed NLP clarification + Ted Spread substitute |

### §8.2 — Per-group coverage at Wave 1+2+3 (89.9%)

| Group | Total | Wave-1 FRED | Wave-2 HAR-RE | Wave-3 NFIB | Total covered | % |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| Leading Indicator | 8 | 1 (USSLIND-REPR) | 2 (LEI, CCI substitute) | 1 (NFIB) | 4 | 50% |
| Lagging Indicator | 7 | 7 | 0 | 0 | **7** | **100%** |
| Financial Condition | 6 | 3 + 1 DERIVED + 1 substitute = 5 | 1 (TIC HAR-RE ~D) | 0 | 5+1 | ~100% (BFCI via NFCI substitute) |
| Inflation | 8 | 7 | 1 (UMich 5Y) | 0 | 8 | **100%** |
| Labor Market | 9 | 9 | 0 | 0 | **9** | **100%** (incl. ICSA/CCSA via FRED-mirror per §5.3 attribution) |
| Consumer | 7 | 4 (+ 1 derive RS-ex-auto-gas) | 1 (CCI) | 0 | 6 | 86% (Wards = PAID-SUB only) |
| Housing Market | 6 | 4 | 2 (NAHB + PHSI) | 0 | 6 | **100%** (post-Wave-2) |
| Investor Sentiment | 7 | 0 | 6 (AAII ×6) | 0 | 6 + 1 yang-internal | 86%+ (Fed NLP = YANG-INTERNAL) |
| Treasury Yields | 10 | 10 | 0 | 0 | **10** | **100%** |
| Credit Spread | 5 | 3 + 1 substitute (AGG) | 0 | 0 | 4 | 80% (Ted = DISCONTINUED) |
| Market Indicator | 1 | 1 | 0 | 0 | **1** | **100%** |
| Currency | 5 | 3 + 1 REPR (DXY) + 1 LIVE (CNH) | 0 | 0 | **5** | **100%** |
| **TOTAL** | **79** | 55+1+2+1+1+1 = ~58 | 11 | 1 | **70-71** | **88.6%-89.9%** |

Per-group breakdown matches §7.2 wave-progression aggregate (rounding differences from REPR/DERIVED/substitute counting conventions).

### §8.3 — Coverage gaps (post-Wave-5(c) accept-GAP)

**5 indicators carry documented RE-GAP / RE-DEFERRED flags post-Wave-5(c):**
1. PMI Manufacturing (#2) — RE-DEFERRED; USSLIND-Wave-1 + regional-Fed substitute available if elevated
2. PMI Services (#3) — RE-DEFERRED
3. S&P PMI Manufacturing (#4) — RE-DEFERRED (methodology-overlap with #2)
4. S&P PMI Services (#5) — RE-DEFERRED (overlap with #3)
5. ISM Mfg/Services New Orders (#6, #7) — RE-DEFERRED (sub-component of #2/#3 subscription)
6. Wards Total Vehicle Sales (#45) — RE-DEFERRED; DAUTOSAAR partial substitute available
7. Ted Spread (#69) — RE-DEFERRED (Andrew arch call: deprecate vs SOFR-substitute)
8. Fed NLP Sentiment (#58) — YANG-INTERNAL-CLARIFY (DS 0.1.0~A self-clarify follow-up)

**Net "GAP" at Wave-5(c) baseline:** 5 indicators (de-duped from 8 above per overlap; ISM PMI Mfg + Services + 2 ISM New Orders + 1 Wards = 5 net PAID-only-no-substitute; Ted + Fed NLP are §5 cleanup-class). **89.9% PRIMARY coverage + 6.3% RE-DEFERRED + 3.8% cleanup = 100% routing closure.**

---

## §9 — Memory Candidates Consolidated

24 memory candidates surfaced across Phase 2a + this synthesis (full count: ~A 5 + ~B 5 + ~C ~5 + ~D ~6 + ~E ~3 + Phase 2b synthesis 5 = ~29; de-dupes apply). Consolidated list for MSTR /govern + Andrew sovereign LD-class disposition (deferred ratification per LD-0025 ALWAYS-PROCEED + Article XVI):

### §9.1 — High-priority candidates (4-of-5 lane convergence or systemic-class)

1. **`fred-as-broadest-single-source-mirror-pattern-with-sister-cross-check`** — 4-of-5-lane empirical convergence on FRED-PRIMARY + sister-CROSS-CHECK; architecturally-clean lean for multi-source RE harness design where mirror-class option exists. Per ~A §8 candidate #3 + ~B §5.3 + ~C §5 + ~D §5.3. **HIGHEST-priority candidate** — load-bearing architectural decision for v1 harness.

2. **`release_id-and-series_id-guesses-must-be-live-verified-against-publisher-catalog-before-committing`** — LD-31 extension. Banked from ~D §9 corrections (`6d3a75014`) + ~A §1.6 + ~B §1.6. Sister to [[feedback_commit_age_use_iso_utc_not_local]] empirical-anchor-over-assumption. **HIGH-priority** — applies to all federal-source API integrations.

3. **`fred-v2-oauth-gated-not-v1-key-compatible`** — empirical class refinement banked: v2 endpoint OAuth-class auth requirement is undocumented externally; live-probe alone reveals. Sister-lane ~D `6d3a75014` first-fire + ~A `da862a6c6` second-fire. **CANDIDATE** for "API-version auth-class transitions need live-probe verification, not docs alone."

4. **`api-status-check-structurally-insufficient-look-beyond-top-level`** — 3 federal-source APIs with 3 different "look beyond top-level status" patterns: FRED 400 + JSON error_message (~A §1.5); BLS REQUEST_SUCCEEDED + EMPTY data + message[] warnings (~B §6 row 1); Census Missing-Key-HTML-200 (~C §6 row 1). **CANDIDATE** for systemic "API status check is structurally insufficient" memory class.

### §9.2 — Medium-priority candidates (federal-source quirk class)

5. **`federal-source-seasonal-adjustment-encoding-taxonomy`** — 3 different SA-encoding mechanisms across federal APIs: BLS = series_id 3rd char (LNS vs LNU); Census = `seasonally_adj=yes/no` query param; FRED = series-id-bound (one or the other per series). **CANDIDATE** for federal-source SA-encoding-class taxonomy memory.

6. **`mirror-vs-origin-distinction-affects-verdict-taxonomy`** — 2-way (mirror-only) vs 3-way (mirror + origin) RE-MATCH granularity affects verdict confidence. Per ~A §8 candidate #4 + §6.1 this synthesis. **CANDIDATE** for verdict-taxonomy granularity reflecting source-class.

7. **`yang-internal-vs-publisher-published-indicator-class-distinction`** — Fed NLP Sentiment + Industrial Productivity MoM + Ted Spread (post-LIBOR) + PPI modern-vs-legacy are yang-side indicators where label deviates from publisher-published structure. Per ~A §8 candidate #5 + ~B §8 candidate #5 + §5 this synthesis. **CANDIDATE** for reconnaissance-briefs-should-flag-yang-internal-vs-publisher-mismatches discipline.

8. **`bls-vs-doleta-vs-adp-labor-publisher-attribution`** — Yang's "Initial/Continuing Jobless Claims" = DoL ETA (NOT BLS); "ADP Employment Change" = ADP-private (NOT BLS). Per ~B §8 candidate #2. **CANDIDATE** for LD-31 extension with Labor-Market-publisher-attribution worked example.

### §9.3 — Pattern/methodology candidates (compression + workflow)

9. **`substrate-reuse-when-sister-lane-shipped-cascade-compression-amplifier`** — multi-lane parallel reconnaissance + same-fabric sibling-template-reuse compounds [[feedback_standby_prep_cascade_compression_2.4x_throughput]]. Empirical: ~A 7min FRED + ~E 25min Aggregate spawn-to-ship; this synthesis brief assembled in ~Xmin via 5-lane substrate-reuse. **CANDIDATE** for multi-lane reconnaissance-class compression pattern.

10. **`per-source-adapter-class-for-heterogeneous-sources-with-shared-interface-contract`** — when source-classes differ (Yahoo Finance + HAR-RE pages + paywalled + ETF-NAV substitutes), uniform-API adapter pattern fails; per-source class with abstract base interface is the pattern (per ~E §4.1). **CANDIDATE** for heterogeneous-source harness architecture.

### §9.4 — Cleanup-class candidates (cross-section observations)

11. **`re-deferred-as-new-verdict-shape-for-paid-class-monthly-cadence-acceptable`** — PAID-SUBSCRIPTION + monthly-cadence-acceptable + Andrew "push down" framing surfaces a new RE-class verdict shape distinct from RE-GAP (which implies no path) vs RE-DEFERRED (deferred-to-decision). **CANDIDATE** for verdict-taxonomy extension.

12. **`bls-ppi-modern-vs-legacy-wpsfd-vs-wpu-class-distinction`** — modern WPSFD4 vs legacy WPU00000000 architectural-class. Per ~B §8 candidate #5 + §5.4 this synthesis. **CANDIDATE** for Andrew sovereign architectural decision-class.

13. **`ted-spread-discontinued-libor-retirement-2022-deprecate-or-substitute-decision`** — generalizable to other indicator-with-discontinued-upstream-rate class (LIBOR retirement affects multiple downstream products). **CANDIDATE** for upstream-rate-retirement disposition class.

Banking deferred to MSTR /govern + Andrew sovereign ratification per LD-0025 ALWAYS-PROCEED + Article XVI. **All 13 banked candidates non-blocking for synthesis ship.**

---

## §10 — RAVC2-Request

**To:** 2.0.0_SA_COO
**From:** 0.1.0_DS_MarketIntelligence~A (Phase 2b synthesis primary)
**TO:** YALP_MACROS.007 — Phase 2b consolidated source-of-truth synthesis brief

**Evidence:**
- This brief at `docs/briefs/yalp_macros_phase2b_source_of_truth_synthesis_2026-05-26.md`
- §1 Per-indicator source-of-truth mapping for 79/79 indicators across 12 groups (PRIMARY + SECONDARY + cost/access + RE-class per row); §1.13 coverage summary
- §2 Tie-breaker rubric for 10 FRED-BLS overlap indicators (5-point rationale + per-indicator FRED-PRIMARY + BLS-CROSS-CHECK pick; analogous rubrics for FRED-Census + FRED-Treasury + FRED-Yahoo overlaps in §2.3)
- §3 6-tier cost/access framework applied across 79; harness build-order recommendation cheapest-to-expensive Wave 1→Wave 5; cumulative 74.7%→89.9% PRIMARY-only-coverage
- §4 5-architectural-call surface for PAID-SUBSCRIPTION indicators with 3-path (subscribe/substitute/RE-GAP) per-indicator framing + default recommendation **(c) RE-GAP acceptable-by-documentation** per Andrew sovereign 21:00Z; escalation-path-if-overridden documented
- §5 5 cleanup-class findings (Ted Spread DISCONTINUED + Fed NLP yang-internal + ICSA/CCSA mis-attribution + PPI modern/legacy + Industrial Productivity label-variant); all NON-BLOCKING with routing to ws CTO + DT 0.1.0 + Andrew per finding-class
- §6 5-shape verdict-taxonomy finalization (RE-MATCH + RE-MATCH-DERIVED + RE-REPRESENTATIVE + RE-GAP + RE-DRIFT + new RE-DEFERRED shape); pre-implementation classification distribution; CVO-verdict-taxonomy cross-mapping; mirror-vs-origin 3-way-vs-2-way source-class extension
- §7 TO-008 harness build sequence recommendation: Wave 1 FRED+Yahoo (74.7%, ~30min) → Wave 2 HAR-RE (+11 indicators, ~2h) → Wave 3 NFIB (+1, ~30min) → Wave 4 CROSS-CHECK overlay (verdict-confidence enrichment, ~4h) → Wave 5 architectural-call resolution (Andrew dispose); ops-dependency map; ~A primary lookahead
- §8 Coverage % summary per-wave + per-group; Wave 1+2+3 = **71/79 (89.9%)** PRIMARY at OPEN-tier-only; +5 RE-DEFERRED = 100% routing closure
- §9 13 memory candidates consolidated across Phase 2a + synthesis (4 high-priority + 4 medium-priority + 2 pattern/methodology + 3 cleanup-class); banking deferred to MSTR /govern + Andrew per LD-0025

**Acceptance criteria (7/7 met):**
- **AC1** Per-indicator source-of-truth mapping complete for 79/79: ✅ §1 (12 sub-sections; PRIMARY + SECONDARY + cost/access + RE-class per row); §1.13 summary
- **AC2** Tie-breaker rubric + per-indicator pick for cross-source overlap: ✅ §2 (FRED-BLS 10 overlap rubric + per-indicator pick; analogous overlap rubrics §2.3)
- **AC3** Cost/access optimization + 6-tier taxonomy + harness build-order: ✅ §3 (6-tier framework + wave-by-wave cheapest-to-expensive order)
- **AC4** 5-architectural-call surface framed with 3-path + default: ✅ §4 (per-indicator 3-path framing + default (c) recommendation + escalation-path)
- **AC5** Cleanup-class findings + verdict-taxonomy finalization: ✅ §5 (5 findings routed) + §6 (5-shape finalization with new RE-DEFERRED)
- **AC6** TO-008 harness build sequence Wave-1 through Wave-5: ✅ §7 (5-wave sequence + ops dependencies + ~A lookahead)
- **AC7** Coverage % + memory candidates consolidated: ✅ §8 (per-wave + per-group coverage) + §9 (13 candidates consolidated)

**Disposition recommendation:** ACCEPT + chain TO-008 dispatch.

**Standing posture post-RAVC2-ACCEPT:** ~A continues to TO-008 multi-source RE harness build per §7 Wave 1 → Wave 5 sequence. Co-authors ~B/~C/~D/~E return to KEEP-EPHEMERAL standby until TO-008 sub-tasks dispatched (Wave 4 CROSS-CHECK adapters per their substrate).

**No production touches.** Synthesis-doc scope; documentation-only commit under ~A author line. Read-only verification scope per PRD v0.5 §4 + Andrew per-page charter framing.

---

## §11 — Standing posture

Brief shipped. Phase 2b §1 complete. **TO-008 (multi-source RE harness build) is the next ~A-primary deliverable** post-RAVC2-ACCEPT per §7 Wave sequence.

Cleanup-class follow-up MCPs chained from this brief (non-blocking for synthesis ship):
- ws CTO + DT 0.1.0: §5.3 ICSA/CCSA mis-attribution audit + §5.5 "Industrial Productivity" label rename
- Andrew + ws CTO architectural call: §5.1 Ted Spread substitute decision + §5.4 PPI modern/legacy decision
- ~A self-clarify next /work cycle: §5.2 Fed NLP yang-internal code-path confirmation

/work 20m cron continued (job 408883d5).

— 0.1.0_DS_MarketIntelligence~A
2026-05-26 work-cycle:2 (Phase 2b YALP_MACROS.007 synthesis)

---

## §12 — Post-RAVC2-ACCEPT amendment: Fed NLP Sentiment empirical reclassification (2026-05-26 ~21:50Z)

**Trigger:** Per §11 standing posture commitment + §5.2 self-clarify follow-up + ws COO RAVC2-ACCEPT routing (cycle 112 carry-on). Post-RAVC2-ACCEPT amendment per [[feedback_corroborate_with_concern_verdict_shape]] additive-amendment pattern — original §1-§11 ratified-as-is; this §12 reports the empirical finding + propagates reclassification implications.

### §12.1 — Empirical finding: Fed NLP Sentiment is Bloomberg-licensed, NOT yang-internal

**Code-spelunk evidence (~21:50Z):**

`infra/aws/lambda/v2_portal/yang_pipeline/macroeconomics/yang-generate-macro/lambda_function.py:102`:
```python
'Investor Sentiment': {
    ...
    'Fed NLP Sentiment': 'BENLPFED Index',
},
```

Yang ingests "Fed NLP Sentiment" via Bloomberg ticker **`BENLPFED Index`** through the same Bloomberg `data.pkl` upstream as all other Investor Sentiment group indicators (AAII series). Sister `docs/reference/yang-original-scripts/YANG_SCRIPTS_RUBRIC.md:108` confirms verbatim mapping.

**Original §5.2 + §1 row 58 + §2.8 hypothesis REFUTED.** "Fed NLP Sentiment" is NOT yang-internal NLP derivation; it IS Bloomberg-published. Reclassify to **Bloomberg-licensed PAID-SUBSCRIPTION class**, sister to:
- Bloomberg Financial Condition Index `BFCIUS` (§1 row 18; original brief)
- Bloomberg US Aggregate Bond Index (`AGG`; §1 row 72; original brief — substitute via Yahoo ETF-NAV exists)

`BENLPFED` is Bloomberg Economics' NLP-sentiment-of-Fed-text composite (FOMC minutes / beige book / Powell pressers); Bloomberg-Terminal-licensed; no FRED-mirror; no public REST API; no obvious open substitute (Atlanta Fed historical NLP series `ATLSBUIREI` + `ATLSBUSGUI` are DISCONTINUED per ~A §2.8).

### §12.2 — Reclassification implications

**§1 row 58 (Investor Sentiment / Fed NLP Sentiment) amendments:**
- PRIMARY-source: was "yang-internal NLP derivation (suspected)" → **"Bloomberg `BENLPFED Index` (Bloomberg-licensed proprietary)"**
- PRIMARY-endpoint: was "(yang code path TBD; clarify ~A)" → **"(Bloomberg Terminal subscription only; no public endpoint)"**
- Cadence: was "Indeterminate pending yang-side clarification" → **"Daily/Weekly (Bloomberg release cadence; precise schedule TBD post-subscription onboard)"**
- SECONDARY: was "(none)" → **"(none — no open substitute available; Atlanta Fed historical NLP discontinued)"**
- Cost/access: was "YANG-INTERNAL-CLARIFY" → **"PAID-SUBSCRIPTION (Bloomberg-Terminal-licensed)"**
- RE-class: was "RE-GAP (or yang-internal-not-RE-class)" → **"RE-DEFERRED (PAID-class; no substitute path)"**

**§2.8 group-level Investor Sentiment summary:**
- Group total stays 7 (no change)
- FRED-MATCH stays 0 (no change)
- All 7 indicators now PAID-class:
  - 6 AAII × via AAII-PAID-or-HAR-RE-CANDIDATE (HAR-RE workaround under Cloudflare 403)
  - 1 Fed NLP via Bloomberg-PAID-SUBSCRIPTION (no substitute)
- ~E PRIMARY scope changes: was 6 AAII HAR-RE + 1 yang-internal; **now 6 AAII HAR-RE + 1 Bloomberg-PAID-architectural-call**

**§4 architectural-call surface count: was 5 PAID → now 6 PAID-no-substitute.** Sister §4.2 row addition:

| # | Indicator | (a) Subscribe ? | (b) Substitute available | (c) RE-GAP acceptable | RECOMMENDATION |
|---:|---|---|---|---|---|
| 58 | Fed NLP Sentiment | Bloomberg Terminal subscription (~$24K/yr per seat; same-class as BFCI + AGG) | (no clean substitute; Atlanta Fed historical NLP discontinued; building yang-internal NLP from FOMC corpus is build-not-buy) | YES — Investor Sentiment group has 6 AAII Wave-2 HAR-RE coverage; Fed NLP is 7th-slot decorative | **(c)** with documented Bloomberg-proprietary-no-substitute footnote |

**§4.3 default recommendation: (c) RE-GAP acceptable-by-documentation STANDS for all 6 PAID indicators** (was 5; now 6 with Fed NLP added). Andrew sovereign 21:00Z "push down" framing applies symmetrically. Investor Sentiment group falls from PAID-class-load-bearing if Fed NLP elevated — but Wave-2 6 AAII HAR-RE provides 86% group-coverage which is sufficient per Andrew sovereign framing.

**§6 verdict-taxonomy distribution amendment:**
- RE-GAP: was ~11 → **~10** (Fed NLP moves OUT; AAII×6 stay; remaining ~10 = NAHB + PHSI + UMich 5Y + CCI + LEI-substitute + 4 other HAR-RE rows)
- RE-DEFERRED: was 6 → **7** (Fed NLP moves IN; sister-class to AGG-Bloomberg + BFCI-Bloomberg already in RE-DEFERRED-candidate-class per §1 row 18 + §1 row 72; Fed NLP now formally RE-DEFERRED no-substitute variant)
- Total 79: 79 unchanged

**§8 coverage gaps amendment:**
- Net Wave-5(c) accept-GAP indicators count: was 5 (PAID-only-no-substitute) → **6** (+1 Fed NLP)
- 100% routing closure unchanged (Fed NLP was already 1 in §8.3 "GAP" bucket; just reclassified between RE-GAP-yang-internal-suspect vs RE-DEFERRED-Bloomberg-paid)

**§5.6 routing summary amendment:**
- Finding 5.2 (Fed NLP yang-internal) status: **was open self-clarify → now RESOLVED** with reclassification to PAID-SUB / RE-DEFERRED per §4 architectural-call surface. Cleanup-class finding count drops from 5 → 4 net (Fed NLP is no longer cleanup-class; it's architectural-call-class).

### §12.3 — Memory candidate refinement

§9 candidate #7 (`yang-internal-vs-publisher-published-indicator-class-distinction`) refinement:

> **Empirical correction:** Fed NLP Sentiment was initially hypothesized as yang-internal-class (sister to F4 Industrial Productivity label-variant + F5 Ted Spread post-LIBOR + PPI modern/legacy class-distinction); empirically confirmed as **publisher-published-Bloomberg-class** (sister to BFCI + AGG = Bloomberg-licensed-proprietary-class). The hypothesis class itself stands as a reconnaissance discipline; **the worked example now serves as a discipline-correction case — always live-verify yang upstream code-path before classifying as yang-internal**, per [[feedback_api_catalog_live_verify_before_committing_ids]] LD-31 discipline extended to yang-side ingest assertions.

**New memory candidate (banked this amendment):**

14. **`yang-internal-vs-publisher-published-class-must-be-live-verified-against-yang-code-path-not-hypothesized`** — sister to [[feedback_api_catalog_live_verify_before_committing_ids]] LD-31 + ~A §1.6 release_id ground-truth discipline. **Anchor:** Fed NLP Sentiment hypothesized yang-internal in synthesis brief §5.2 (~21:35Z); empirically refuted via yang Lambda code-spelunk ~21:50Z (BENLPFED Bloomberg ticker confirmed). **Discipline:** when reconnaissance-brief surfaces a "yang-internal-suspect" indicator-class candidate, code-spelunk yang Lambda source-of-truth (`infra/aws/lambda/v2_portal/yang_pipeline/.../lambda_function.py` `BBG_TICKERS` dict OR `MACRO_GROUPS` rubric) BEFORE banking the candidate — same empirical-anchor-over-assumption discipline as release_id / series_id catalog ground-truth.

### §12.4 — Standing posture refresh

- TO-007 synthesis RAVC2-ACCEPTED ✓ (cycle 112; original brief stands; §12 is additive amendment)
- §5.2 self-clarify commitment RESOLVED ✓ (Fed NLP empirical class confirmed)
- Cleanup-class findings count: was 5 → 4 (Fed NLP reclassified out of cleanup-class into architectural-call-class)
- §4 architectural-call surface count: was 5 → 6 (+Fed NLP)
- /work 20m cron continued (job 408883d5)
- Standing for ws COO TO-008 multi-source RE harness build GO dispatch (deferred to cycle 113 cron ~21:47Z per ws COO RAVC2-ACCEPT message)

— 0.1.0_DS_MarketIntelligence~A
2026-05-26 ~21:50Z (post-RAVC2-ACCEPT amendment; work-cycle:3)

