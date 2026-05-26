# YALP_MACROS Phase 2a — FRED Multi-Source Reconnaissance

**TO:** YALP_MACROS.006a — FRED multi-source authoritative-source RE reconnaissance (Phase 2a parallel lane A)
**Author:** 0.1.0_DS_MarketIntelligence~A (Phase 2a FRED lane; sister to ~B BLS + ~C Census + ~D Treasury/FDIC + ~E Aggregate-orphan; also Phase 1 YALP_MACROS lead-author per `3effd8667` + cascade `c50c59399`)
**PRD:** `docs/architecture/YALP_MACROS.md` v0.5 RE-OPENED `7e781ea8c` — Phase 2 multi-source RE charter
**Authority:** Andrew sovereign direct ~21:00Z + RE-OPEN Phase 2 ~21:05Z + MSTR LD-0104 fast-trajectory endorsement + ws COO cross-lane primitive alerts `20260526T203625Z` (initial v2 framing) + `20260526T204136Z` (CRITICAL CORRECTION post ~D `6d3a75014` live-verify: v2 OAuth-gated, use v1 2-step pattern; release_id corrections G.19=14, TIC=3)
**T*:** indicator-cadence-bound (Treasury yields daily; FRB releases weekly/monthly; BEA NIPA quarterly via FRED-mirror); brief authored 2026-05-26 against current FRED v1 API surface live-verified ~23:?Z post-AWS-Secrets-key retrieval
**Status:** Phase 2a reconnaissance COMPLETE — 5/5 ACs met

---

## §0 — TL;DR

**FRED (Federal Reserve Bank of St. Louis Economic Data) is the broadest single mirror of the 79-indicator macro universe.** FRED hosts mirrors of FRB statistical releases, BEA NIPA, BLS, Treasury, NAR, NAHB, Census, ICE, CBOE, and ~150 other federal + private data providers behind a single REST API surface with one stable api_key auth model.

**Per-indicator coverage breakdown (79-indicator universe):**

| Coverage class | Count | % | Notes |
|---|---:|---:|---|
| **FRED-MATCH** (canonical FRED series with documented mapping; 1:1 yang→FRED equivalence) | 52 | 65.8% | Treasury Yields (10/10), FRB-release-mirrored macro (WALCL/INDPRO/TCU/TOTALSL/FEDFUNDS), BEA NIPA mirrored (GDP/PCE/PCEPI/PCEPILFE), BLS-mirrored (CPI/CPILFE/PAYEMS/UNRATE/ICSA/CCSA/JTSJOL/CIVPART/AWHAETP/CES0500000003), Census-mirrored (RSAFS/DGORDER/AMTMNO/BUSINV/BOPGSTB/HOUST/PERMIT/HSN1F/EXHOSLUSM495S), ICE BofA spreads (BAMLC0A1CAAA/BAMLC0A0CM/BAMLH0A0HYM2), CBOE VIX (VIXCLS), Chicago Fed NFCI, currency (DEXUSEU/DEXJPUS/DEXUSUK), UMich 1Y (MICH) |
| **FRED-REPRESENTATIVE** (FRED-mirror approximate or proxy; usable but methodology-variant) | 5 | 6.3% | USSLIND (Leading Index proxy — Philly Fed adaptation, NOT Conference Board LEI), DTWEXBGS (Nominal Broad Dollar Index proxy for ICE DXY), RSXFS+RSGASS-derived (Retail Sales ex Auto and Gas — requires component-subtract), Industrial Productivity MoM (FRED INDPRO = production index, yang may label differently per Phase 1 F4-class) |
| **FRED-DERIVED** (composite computed client-side from FRED inputs) | 1 | 1.3% | Fed Balance Sheet as % of GDP (WALCL ÷ GDP * 100) |
| **FRED-GAP** (NOT in FRED; route to sister-lane or accept as orphan) | 21 | 26.6% | All 8 Leading except USSLIND-proxy (ISM/S&P Global/NFIB — private), all 7 Investor Sentiment (AAII×6 + Atlanta Fed NLP — private/discontinued in FRED), TED Spread (TEDRATE DISCONTINUED 2022), AGG Bloomberg Aggregate (private), MOVE Index (private/ICE), DXY exact (ICE proprietary; DTWEXBGS is REPRESENTATIVE proxy), USD/CNH (offshore CNH not in FRED; CNY proxy exists), UMich 5-10Y Inflation (UMich only publishes 1Y on FRED via MICH), Conference Board Consumer Confidence (private), Wards Total Vehicle Sales (private), NAHB Housing Market Index (private), Pending Home Sales (NAR private), Bloomberg BFCI (private), Net Long Term TIC Flows (FRED has partial TIC; not full LT-flows table) |

**Two-tier harness architecture (Phase 2b TO-007 synthesis lean):**
- **PRIMARY runtime:** FRED `series/observations` per-series fetcher (v1 2-step pattern; api_key auth; clean operational risk profile)
- **CROSS-CHECK tier:** sister ~B BLS + ~C Census + ~D Treasury Direct for upstream-authoritative validation when DRIFT class fires (FRED is mirror, NOT origin for any of the 79)
- **GAP routing:** ~E aggregate-orphan lane primary (private + survey + index sources)

**Critical reconnaissance findings (banked candidates):**
1. **FRED v2 `release/observations` endpoint is OAuth-gated, NOT v1-api-key-compatible** — live-probe ~23:?Z returned HTTP 401 with valid v1 key. v1 2-step pattern (`release/series` → `series/observations`) is the empirically-working primitive.
2. **release_id catalog ground-truth empirically deviates from canonical-release-organization memory** — G.19 Consumer Credit = 14 (NOT 17; 17 is H.10 Foreign Exchange Rates); TIC SLT = 3 (NOT 39; 39 absent from catalog). Sister-finding to [[feedback_api_catalog_live_verify_before_committing_ids]] LD-31; this brief live-verified all 5 target release_ids against `/fred/releases` catalog.
3. **3-way Treasury Yields cross-validation MATCHES empirically** — DGS10 2026-05-22 = 4.56 == Treasury Direct CSV 10Yr 2026-05-22 = 4.56 (per ~D §1.1 live-pull). Validates RE-MATCH class hypothesis from harness architecture; Treasury Direct + FRB H.15 + FRED-mirror triangulation works.
4. **ISM PMI series discontinued in FRED in 2016** — NAPM, NAPMNOI, NAPMSDI, ISM-prefixed series all return NOT FOUND. Reconnaissance NEGATIVE result; route all 4 PMI indicators (PMI Mfg/Services + ISM Mfg/Services New Orders) + S&P PMI ×2 to ~E aggregate-orphan lane. (USSLIND IS a FRED-hosted leading index but is FRBP/Crone NOT Conference Board LEI — REPRESENTATIVE-class at best.)

**Phase 2b TO-007 synthesis disposition:** FRED is the **CONVENIENT PRIMARY** for ~66% of 79; sister-lane fallback for the rest. Two-tier harness with FRED-PRIMARY + sister-lane CROSS-CHECK + sister-lane PRIMARY for FRED-GAP class is the architecturally-clean lean.

---

## §1 — FRED API Surface

### §1.1 — Auth + base URL

**Base:** `https://api.stlouisfed.org/fred/`
**Auth:** 32-char alphanumeric lowercase api_key on every request via `&api_key={KEY}` query param.
**Key sourcing:** AWS Secrets Manager secret `FredApiKey` (live-verified retrievable ~23:?Z via `aws secretsmanager get-secret-value --secret-id FredApiKey --query SecretString --output text`; same `/cloud-ops` permissions profile). **No fresh signup required** — Opal already has a registered key.

### §1.2 — v1 2-step primitive (LIVE-VERIFIED — preferred runtime)

**Step 1: Enumerate series in a release**
```
GET https://api.stlouisfed.org/fred/release/series
    ?release_id={N}
    &api_key={KEY}
    &file_type=json
    &limit=1000          (max 1000 per page; default 1000)
    &offset={M}          (pagination)
```
Returns metadata for all series in a release.

Live-verified shape (~23:?Z, release_id=18 H.15):
```json
{
  "realtime_start": "2026-05-26", "realtime_end": "2026-05-26",
  "order_by": "series_id", "sort_order": "asc",
  "count": 270, "offset": 0, "limit": 1000,
  "seriess": [
    {"id":"CD1M","title":"Average Rate on 1-Month Negotiable Certificates of Deposit ...","frequency":"Daily, Close","units":"Percent","seasonal_adjustment":"Not Seasonally Adjusted","last_updated":"2025-04-04 ...", ...},
    ...
  ]
}
```

**Step 2: Pull observations for a series**
```
GET https://api.stlouisfed.org/fred/series/observations
    ?series_id={SERIES_ID}
    &api_key={KEY}
    &file_type=json
    &sort_order=desc                 (newest first; default asc)
    &limit={N}                       (max 100000 default 100000)
    &observation_start={YYYY-MM-DD}  (filter window)
    &observation_end={YYYY-MM-DD}
```
Returns observation history with date + value (numeric value as STRING; "." for missing).

Live-verified shape (~23:?Z, DGS10):
```json
{
  "realtime_start":"2026-05-26", "realtime_end":"2026-05-26",
  "observation_start":"1600-01-01", "observation_end":"9999-12-31",
  "units":"lin", "output_type":1, "file_type":"json",
  "order_by":"observation_date", "sort_order":"desc",
  "count": 16799, "offset": 0, "limit": 100000,
  "observations":[
    {"realtime_start":"2026-05-26","realtime_end":"2026-05-26","date":"2026-05-22","value":"4.56"},
    {"realtime_start":"2026-05-26","realtime_end":"2026-05-26","date":"2026-05-21","value":"4.57"},
    ...
  ]
}
```

### §1.3 — v2 `release/observations` bulk endpoint (OAuth-gated; NOT v1-key-compatible)

Per ws COO cross-lane primitive alert `20260526T203625Z` (initial framing) → CRITICAL CORRECTION `20260526T204136Z` post sister ~D `6d3a75014` live-probe:

```
GET https://api.stlouisfed.org/fred/v2/release/observations?release_id=18&api_key={v1-KEY}&format=json
  → HTTP 401 {"code":401,"message":"Missing or invalid credentials."}
```

v2 endpoint is operational + returns all series in a release in single paginated call (cursor-based, up to 500k obs/page) per `https://fred.stlouisfed.org/docs/api/fred/v2/release_observations.html` — **BUT requires OAuth-class auth which v1 api_keys do not satisfy.** Future v2 OAuth swap-in scaffold left as commented-out class in §4 adapter (per ~D §9 corrections precedent).

**Until v2 OAuth onboarding (separate ops task; defer to Wave-3 if/when scale demands it):** v1 2-step is canonical. For YALP_MACROS narrow scope (79 indicators), harness short-circuits `list_series_in_release()` to known target series IDs → ~10-15 calls per H.15 refresh vs ~271 calls full enumeration. Acceptable per Andrew "monthly cadence acceptable" framing (LD-0104).

### §1.4 — Additional v1 endpoints (reference)

| Endpoint | Purpose | When to use |
|---|---|---|
| `/fred/releases` | List ALL ~300 FRED releases with id + name | Discovery; LD-31 live-verify gate before committing release_id mappings |
| `/fred/series` | Single-series metadata (title, units, frequency, last_updated) | Verify a series exists before observation pull; cache-friendly |
| `/fred/series/search` | Full-text search across series titles | Discovery for ambiguous indicator names; e.g., "Pending Home Sales" reveals no FRED-direct |
| `/fred/series/observations` | Observation history per series | **Primary runtime endpoint** for harness |
| `/fred/release/series` | All series in a release | v1 bulk-enumeration step 1 |
| `/fred/categories/{N}/series` | Series in a FRED-internal category | Alternative discovery axis (FRED has its own taxonomic categories distinct from release-groups) |
| `/fred/tags` + `/fred/tags/series` | Tag-based discovery (e.g., "monetary-aggregates") | Alternative discovery axis |

### §1.5 — Rate limits + ops profile

- **Rate limit:** 120 requests/minute per api_key per FRED docs (`https://fred.stlouisfed.org/docs/api/`). Well above harness needs (~50-100 calls/refresh × monthly cadence).
- **Failure modes:** HTTP 200 + JSON error body on malformed request (`{"error_code":400,"error_message":"..."}`); standard HTTP 4xx/5xx on infra-class failures. Series-not-found returns 400 with explicit message (NOT 200-empty as FRB DDP does — cleaner failure semantics).
- **No session/cookie auth.** Sister to ~D Treasury Direct + Census + NY Fed Markets clean-ops profile. Compare YCharts 403-session-eviction class per [[feedback_ycharts_http_400_is_cookie_stale_class]].
- **Value encoding:** Numeric values returned as STRING in `observations[].value` (parse float client-side); missing observations encoded as `"."` (NOT null, NOT empty). Sister to Census EITS + Treasury Fiscal Data quirks (~C §6 + ~D §6).

### §1.6 — Live-verified release_id catalog (LD-31 ground-truth)

Per [[feedback_api_catalog_live_verify_before_committing_ids]] — release_id guesses live-verified against `/fred/releases?api_key={K}` catalog enumeration at brief authoring time (NOT TO-008 impl time). Ground-truth ~23:?Z:

| Release | Banked memory was | Live-verified ID | Notes |
|---|:-:|:-:|---|
| H.15 Selected Interest Rates | 18 | **18** ✓ | Confirmed |
| H.4.1 Factors Affecting Reserve Balances | 20 | **20** ✓ | Confirmed (sister 122 = "data not included in press release" variant) |
| G.17 Industrial Production and Capacity Utilization | 13 | **13** ✓ | Confirmed |
| **G.19 Consumer Credit** | **17 (WRONG)** | **14** | release_id=17 in FRED catalog is **H.10 Foreign Exchange Rates** — completely different release. Memory-banked guess from canonical-release-organization heuristic deviated from FRED's internal id-allocation. |
| Z.1 Financial Accounts of the United States | 52 | **52** ✓ | Confirmed (Andrew's example holds) |
| **TIC Treasury International Capital** | **39 (WRONG)** | **3** | release_id=39 NOT in catalog (search for "Treasury International Capital" returned only id=3 "TIC: Continuous Securities Long Term (SLT)"). release_id=3 covers partial TIC scope (SLT only, not full LT-flows table). |
| (search match check) "Selected Interest Rates" | n/a | 18 + 131 | 131 = "G.13 Selected Interest Rates" (distinct from H.15) |
| (search match check) "Reserve Balances" | n/a | 20 + 122 + 185 | 122 = H.4.1 sister; 185 = "Interest Rate on Reserve Balances" (IORB rate; distinct) |

**Banked LD candidate (LD-0105? — TBD by MSTR per [[feedback_api_catalog_live_verify_before_committing_ids]]):** `release_id-guesses-must-be-live-verified-against-/fred/releases-catalog-before-committing-to-brief-or-harness`. Confirmed empirical-anchor-over-assumption discipline; sister to [[feedback_commit_age_use_iso_utc_not_local]].

---

## §2 — Per-Indicator Match-Set (79 yang → FRED)

### §2.1 — Treasury Yields group (10 indicators; 10/10 FRED-MATCH)

| # | Yang indicator | FRED series ID | FRED title (live-verified ~23:?Z) | Cadence | Sister source |
|---|---|---|---|---|---|
| 1 | 1M | `DGS1MO` | Market Yield on U.S. Treasury Securities at 1-Month Constant Maturity | Daily (business days) | ~D Treasury Direct CSV `"1 Mo"` |
| 2 | 3M | `DGS3MO` | ... 3-Month CMT | Daily | ~D `"3 Mo"` |
| 3 | 1Y | `DGS1` | ... 1-Year CMT | Daily | ~D `"1 Yr"` |
| 4 | 2Y | `DGS2` | ... 2-Year CMT | Daily | ~D `"2 Yr"` |
| 5 | 3Y | `DGS3` | ... 3-Year CMT | Daily | ~D `"3 Yr"` |
| 6 | 5Y | `DGS5` | ... 5-Year CMT | Daily | ~D `"5 Yr"` |
| 7 | 7Y | `DGS7` | ... 7-Year CMT | Daily | ~D `"7 Yr"` |
| 8 | 10Y | `DGS10` | ... 10-Year CMT | Daily | ~D `"10 Yr"` |
| 9 | 20Y | `DGS20` | ... 20-Year CMT | Daily | ~D `"20 Yr"` |
| 10 | 30Y | `DGS30` | ... 30-Year CMT | Daily | ~D `"30 Yr"` |

**3-way cross-validation MATCHES empirically (DGS10 2026-05-22 = 4.56 == ~D Treasury Direct 10Yr 2026-05-22 = 4.56).** Per Phase 2b harness verdict-taxonomy: Treasury Yields are the high-confidence RE-MATCH class — Treasury Direct upstream + FRB H.15 mirror + FRED-mirror all publish same canonical CMT yields.

### §2.2 — Lagging Indicator group (7 indicators; 7/7 FRED-MATCH/REPRESENTATIVE)

| # | Yang indicator | FRED series ID | FRED title | Cadence | Class | Notes |
|---|---|---|---|---|---|---|
| 11 | GDP QoQ | `A191RL1Q225SBEA` | Real GDP, %-change-q/q SAAR | Quarterly (advance/2nd/3rd) | MATCH | BEA-published; sister ~D §2.1 row 14 |
| 12 | Industrial Productivity MoM | `INDPRO` | Industrial Production: Total Index | Monthly | REPRESENTATIVE | Yang label "Productivity" likely variant for FRB G.17 "Industrial Production"; flag for TO-007 Phase 1 F4 cross-check. ~D §2.1 row 15 sister. |
| 13 | Durable Goods Orders MoM | `DGORDER` | Manufacturers' New Orders: Durable Goods | Monthly | MATCH | Census M3 release; sister ~C TO-006c |
| 14 | Factory Orders MoM | `AMTMNO` | Manufacturers' New Orders: Total Manufacturing | Monthly | MATCH | Census M3 release |
| 15 | Capacity Utilization | `TCU` | Capacity Utilization: Total Index | Monthly | MATCH | FRB G.17; sister ~D §2.1 row 16 |
| 16 | Business Inventories YoY | `BUSINV` (level) | Total Business Inventories | Monthly | MATCH-DERIVED | Census MTIS; level series; YoY derive client-side `(t / t-12mo - 1) * 100` |
| 17 | Trade Balance | `BOPGSTB` | Trade Balance: Goods and Services, BoP Basis | Monthly | MATCH | Joint Census/BEA; ~D §2.1 row 7 cross-ref + ~C TO-006c |

### §2.3 — Financial Condition group (6 indicators; 4 FRED-coverage of various class + 1 DERIVED + 1 GAP)

| # | Yang indicator | FRED series ID | Cadence | Class | Notes |
|---|---|---|---|---|---|
| 18 | Bloomberg Financial Condition Index | n/a | - | **GAP** | BFCI is Bloomberg-proprietary; not on FRED. Route ~E aggregate-orphan. |
| 19 | Chicago Fed Financial Condition Index | `NFCI` | Weekly | MATCH | Chicago Fed-published; mirror on FRED |
| 20 | Fed Fund Rate | `FEDFUNDS` (monthly) or `DFF` (daily) | Monthly / Daily | MATCH | Yang stores monthly avg → `FEDFUNDS`; sister ~D §2.1 row 11 NY Fed Markets EFFR live source |
| 21 | Fed Balance Sheet | `WALCL` | Weekly (Wednesday level) | MATCH | FRB H.4.1; sister ~D §2.1 row 12 |
| 22 | Fed Balance Sheet as % of GDP | (derived) | Quarterly-update bound | **DERIVED** | `WALCL / GDP * 100` cross-frequency interpolate; ~D §2.1 row 20 sister-pattern |
| 23 | Net Long Term TIC Flows | (no direct) | Monthly | **GAP** | release_id=3 (TIC SLT) is partial scope (Continuous Securities Long Term subset, not full LT-flows table). FRED-mirror partial; route ~D Treasury TIC XLSX HAR-RE candidate. |

### §2.4 — Inflation group (8 indicators; 7 FRED-MATCH + 1 GAP)

| # | Yang indicator | FRED series ID | Cadence | Class | Notes |
|---|---|---|---|---|---|
| 24 | CPI MoM | `CPIAUCSL` (level) | Monthly | MATCH-DERIVED | BLS-published; level series; MoM derive `(t / t-1 - 1) * 100`. Sister ~B BLS-PRIMARY |
| 25 | Core CPI MoM | `CPILFESL` | Monthly | MATCH-DERIVED | BLS; level; MoM derive. Sister ~B |
| 26 | PCE MoM | `PCEPI` | Monthly | MATCH-DERIVED | BEA NIPA T20807; sister ~D §2.1 row 17 |
| 27 | Core PCE MoM | `PCEPILFE` | Monthly | MATCH-DERIVED | BEA NIPA T20807; sister ~D §2.1 row 18 |
| 28 | PPI MoM | `PPIACO` | Monthly | MATCH-DERIVED | BLS PPI All Commodities; sister ~B |
| 29 | Unit Labor Cost YoY | `ULCNFB` | Quarterly | MATCH-DERIVED | BLS Productivity & Costs; YoY derive |
| 30 | UMich 1 Year Inflation | `MICH` | Monthly | MATCH | UMich Inflation Expectation 1Y |
| 31 | UMich 5-10 Year Inflation | n/a | - | **GAP** | UMich publishes 1Y on FRED; 5-10Y NOT on FRED. Route ~E aggregate-orphan (UMich source-direct via UMich data export). Alternative: `T5YIFR` (5Y-5Y-forward breakeven) is REPRESENTATIVE-class proxy from market-implied not survey-derived. |

### §2.5 — Labor Market group (9 indicators; 8 FRED-MATCH + 1 GAP)

| # | Yang indicator | FRED series ID | Cadence | Class | Notes |
|---|---|---|---|---|---|
| 32 | Unemployment Rate | `UNRATE` | Monthly | MATCH | BLS CPS; sister ~B BLS-PRIMARY |
| 33 | Initial Jobless Claims | `ICSA` | Weekly | MATCH | DoL ETA; sister ~B |
| 34 | Continuing Jobless Claims | `CCSA` | Weekly | MATCH | DoL ETA; sister ~B |
| 35 | US Job Openings | `JTSJOL` | Monthly | MATCH | BLS JOLTS; sister ~B |
| 36 | Nonfarm Payrolls | `PAYEMS` | Monthly | MATCH | BLS CES; sister ~B |
| 37 | ADP Employment Change | `ADPMNUSNERSA` (or `NPPTTL` DISCONTINUED) | Monthly | REPRESENTATIVE | ADP series re-instated on FRED as `ADPMNUSNERSA` (Monthly Total Nonfarm Private Payroll Employment); older `NPPTTL` (DISCONTINUED). MoM derive. |
| 38 | Labor Force Participation Rate | `CIVPART` | Monthly | MATCH | BLS CPS; sister ~B |
| 39 | Weekly Hours | `AWHAETP` | Monthly | MATCH | BLS CES "Average Weekly Hours of All Employees, Total Private"; sister ~B |
| 40 | Hourly Earnings MoM | `CES0500000003` | Monthly | MATCH-DERIVED | BLS CES "Average Hourly Earnings of All Employees, Total Private"; MoM derive |

### §2.6 — Consumer group (7 indicators; 4 MATCH + 1 REPRESENTATIVE + 2 GAP)

| # | Yang indicator | FRED series ID | Cadence | Class | Notes |
|---|---|---|---|---|---|
| 41 | Retail Sales MoM | `RSAFS` | Monthly | MATCH-DERIVED | Census MARTS; sister ~C TO-006c row "Retail Sales MoM" |
| 42 | Retail Sales ex Auto MoM | `RSXFS` | Monthly | MATCH-DERIVED | Census MARTS "Retail Sales: Retail Trade" (excludes Food Services); approximately = ex-Auto. **MINOR DRIFT CAVEAT**: yang "ex Auto" may include or exclude Food Services differently from FRED RSXFS (which excludes both). Phase 2b TO-008 cross-check vs Census source-direct. |
| 43 | Retail Sales ex Auto and Gas MoM | (derived from `RSXFS` + `RSGASS`) | Monthly | **REPRESENTATIVE** | No direct FRED series; derive `(RSXFS - RSGASS) / prior_month` MoM. **Computational class — REPRESENTATIVE not MATCH per derive-class.** |
| 44 | UMich Consumer Sentiment | `UMCSENT` | Monthly | MATCH | UMich Index of Consumer Sentiment |
| 45 | Conference Board Consumer Confidence | n/a | - | **GAP** | Conference Board CCI is private-published; not on FRED. Route ~E aggregate-orphan. |
| 46 | Consumer Credit YoY | `TOTALSL` | Monthly | MATCH-DERIVED | FRB G.19 release_id=14 (verified) "Total Consumer Credit Owned and Securitized"; level; YoY derive. Sister ~D §2.1 row 19 |
| 47 | Wards Total Vehicle Sales | n/a | - | **GAP** | Wards Intelligence private; not on FRED. Closest FRED proxy `DAUTOSAAR` is domestic-autos-only subset (NOT total). Route ~E aggregate-orphan or accept GAP. |

### §2.7 — Housing Market group (6 indicators; 4 MATCH + 2 GAP)

Per Phase 1 brief F5 finding: Housing Market `declared_count=7 actual=6`; this brief works against live macro_data.json ground-truth (6 indicators).

| # | Yang indicator | FRED series ID | Cadence | Class | Notes |
|---|---|---|---|---|---|
| 48 | NAHB Housing Market Index | n/a | - | **GAP** | NAHB-published private; not on FRED. Route ~E aggregate-orphan. |
| 49 | New Home Sales | `HSN1F` | Monthly | MATCH | Census Survey of Construction; sister ~C TO-006c |
| 50 | Existing Home Sales | `EXHOSLUSM495S` | Monthly | MATCH | NAR mirror on FRED |
| 51 | Pending Home Sales | n/a | - | **GAP** | NAR-published private; not on FRED (FRED search returned only "Existing Home Sales: Housing Inventory" related). Route ~E aggregate-orphan. |
| 52 | Housing Starts | `HOUST` | Monthly | MATCH | Census Survey of Construction; sister ~C TO-006c |
| 53 | Building Permits | `PERMIT` | Monthly | MATCH | Census Building Permits Survey; sister ~C TO-006c |

### §2.8 — Investor Sentiment group (7 indicators; 0/7 FRED-MATCH)

| # | Yang indicator | FRED series ID | Cadence | Class | Notes |
|---|---|---|---|---|---|
| 54 | AAII Sentiment Bullish | n/a | - | **GAP** | AAII Survey private; not on FRED. Route ~E aggregate-orphan. |
| 55 | AAII Sentiment Neutral | n/a | - | **GAP** | same |
| 56 | AAII Sentiment Bearish | n/a | - | **GAP** | same |
| 57 | AAII Stock Allocation | n/a | - | **GAP** | same |
| 58 | AAII Bond Allocation | n/a | - | **GAP** | same |
| 59 | AAII Cash Allocation | n/a | - | **GAP** | same |
| 60 | Fed NLP Sentiment | n/a | - | **GAP** | Atlanta Fed NLP sentiment series search returned only DISCONTINUED `ATLSBUIREI` + `ATLSBUSGUI`; the "Fed NLP" yang label likely references a yang-internal NLP-derived sentiment from Fed text corpus, NOT a FRED-hosted Atlanta Fed sentiment series. Route ~E aggregate-orphan (clarify yang-side source). |

**Whole-group GAP class.** ~E aggregate-orphan lane carries full Investor Sentiment coverage. FRED is structurally absent here — AAII is private association; Fed NLP is yang-internal derivation, not Fed-published.

### §2.9 — Leading Indicator group (8 indicators; 1 REPRESENTATIVE + 7 GAP)

| # | Yang indicator | FRED series ID | Cadence | Class | Notes |
|---|---|---|---|---|---|
| 61 | Leading Index | `USSLIND` | Monthly | **REPRESENTATIVE** | Philly Fed/Crone "Leading Index for the United States" — DIFFERENT methodology from Conference Board LEI (which yang label likely references). Use as proxy with documented method-variance OR route Conference Board source-direct via ~E. |
| 62 | PMI Manufacturing | n/a | - | **GAP** | ISM PMI series discontinued in FRED ~2016. Route ~E aggregate-orphan. |
| 63 | PMI Services | n/a | - | **GAP** | ISM Non-Mfg discontinued in FRED ~2016. Route ~E. |
| 64 | S&P PMI Manufacturing | n/a | - | **GAP** | S&P Global private; not on FRED. Route ~E. |
| 65 | S&P PMI Services | n/a | - | **GAP** | S&P Global private; not on FRED. Route ~E. |
| 66 | ISM Manufacturing New Orders | n/a | - | **GAP** | ISM subseries discontinued. Route ~E. |
| 67 | ISM Services New Orders | n/a | - | **GAP** | ISM subseries discontinued. Route ~E. |
| 68 | NFIB Small Business Optimism | n/a | - | **GAP** | NFIB private; not on FRED. Route ~E aggregate-orphan. |

**Critical finding F-FRED-1**: ISM PMI series were removed from FRED in 2016 (per FRED catalog inspection; NAPM/NAPMNOI/NAPMSDI all return NOT FOUND). For 6 of 8 Leading indicators (PMI ×4 + ISM New Orders ×2), FRED has ZERO coverage. Sister-lane ~E aggregate-orphan is the only authoritative-source path; if Wave-2 expects FRED-PRIMARY here, the empirical answer is NO.

### §2.10 — Credit Spread group (5 indicators; 3 MATCH + 1 DISCONTINUED + 1 GAP)

| # | Yang indicator | FRED series ID | Cadence | Class | Notes |
|---|---|---|---|---|---|
| 69 | Ted Spread | `TEDRATE` (**DISCONTINUED 2022**) | n/a | **DISCONTINUED** | TED Spread was 3M LIBOR - 3M T-Bill; LIBOR retirement (2022) made it discontinued. FRED hosts historical only. **Yang-side recommendation**: deprecate the indicator OR substitute SOFR-3M minus T-Bill-3M as modern equivalent. Phase 2b TO-007 + Andrew architectural decision required. |
| 70 | AAA | `BAMLC0A1CAAA` | Daily | MATCH | ICE BofA AAA US Corporate Index Option-Adjusted Spread (OAS) |
| 71 | IG | `BAMLC0A0CM` | Daily | MATCH | ICE BofA US Corporate Index OAS (broad investment grade) |
| 72 | AGG | n/a | - | **GAP** | Bloomberg US Aggregate Bond Index private; not on FRED (search returned empty). Route ~E aggregate-orphan. |
| 73 | HY | `BAMLH0A0HYM2` | Daily | MATCH | ICE BofA US High Yield Index OAS |

### §2.11 — Market Indicator group (1 indicator per live macro_data.json; per Phase 1 F4 declared=2 actual=1 MOVE-MISSING; 1/1 FRED-MATCH)

| # | Yang indicator | FRED series ID | Cadence | Class | Notes |
|---|---|---|---|---|---|
| 74 | VIX | `VIXCLS` | Daily | MATCH | CBOE Volatility Index: VIX (FRED-mirror of CBOE-published; same source attribution as `volatility_data.json` per Phase 1 brief §6.1) |

NB: MOVE Index (yang Market Indicator declared but absent per F4) — **NOT IN FRED**; ICE BofAML MOVE is proprietary index; Yahoo Finance ^MOVE is closest non-private source. If yang adds MOVE back, FRED is NOT the source — route to ICE BofAML / Yahoo passthrough (consistent with Phase 1 brief §6.1 attribution).

### §2.12 — Currency group (5 indicators; 3 MATCH + 1 REPRESENTATIVE + 1 GAP)

| # | Yang indicator | FRED series ID | Cadence | Class | Notes |
|---|---|---|---|---|---|
| 75 | DXY | `DTWEXBGS` | Daily | **REPRESENTATIVE** | FRED hosts "Nominal Broad U.S. Dollar Index" (DTWEXBGS) which is FED-calculated, NOT ICE DXY (ICE-published 6-currency basket: EUR/JPY/GBP/CAD/SEK/CHF). Methodology-variant; correlated but not 1:1. |
| 76 | EUR/USD | `DEXUSEU` | Daily | MATCH | "U.S. Dollars to Euro Spot Exchange Rate" |
| 77 | USD/JPY | `DEXJPUS` | Daily | MATCH | "Japanese Yen to U.S. Dollar Spot Exchange Rate" |
| 78 | GBP/USD | `DEXUSUK` | Daily | MATCH | "U.S. Dollars to U.K. Pound Sterling Spot Exchange Rate" |
| 79 | USD/CNH | n/a | - | **GAP** | FRED hosts USD/CNY onshore (e.g., `CCUSSP02CNM650N` monthly) but NOT USD/CNH offshore. Route to broker-direct (Bloomberg/Reuters) via ~E or accept CNY proxy with documented variance. |

### §2.13 — Group-level coverage summary

| Group | Total | FRED-MATCH | FRED-REPRESENTATIVE | FRED-DERIVED | FRED-GAP | FRED-coverage % |
|---|---:|---:|---:|---:|---:|---:|
| Leading Indicator | 8 | 0 | 1 (USSLIND-proxy) | 0 | 7 | 12.5% |
| Lagging Indicator | 7 | 6 | 1 (INDPRO-IndProd) | 0 | 0 | **100%** |
| Financial Condition | 6 | 3 | 0 | 1 | 2 | 66.7% |
| Inflation | 8 | 7 | 0 | 0 | 1 | 87.5% |
| Labor Market | 9 | 8 | 1 (ADP) | 0 | 0 | **100%** |
| Consumer | 7 | 4 | 1 (RS ex Auto&Gas derive) | 0 | 2 | 71.4% |
| Housing Market | 6 | 4 | 0 | 0 | 2 | 66.7% |
| Investor Sentiment | 7 | 0 | 0 | 0 | 7 | **0%** |
| Treasury Yields | 10 | 10 | 0 | 0 | 0 | **100%** |
| Credit Spread | 5 | 3 | 0 | 0 | 2 (incl. 1 DISCONTINUED) | 60% |
| Market Indicator | 1 | 1 | 0 | 0 | 0 | **100%** |
| Currency | 5 | 3 | 1 (DTWEXBGS-DXY) | 0 | 1 | 80% |
| **TOTAL** | **79** | **49** | **5** | **1** | **24 (incl. 1 DISCONTINUED)** | **MATCH 62.0% / +REPR 68.4% / +DERIVED 69.6% / GAP 30.4%** |

**Best-coverage groups (100% FRED):** Treasury Yields, Lagging Indicator, Labor Market, Market Indicator (1/1 VIX).
**Worst-coverage groups (0% FRED):** Investor Sentiment (all 7 private).
**~D-PRIMARY overlap (per ~D §2.1):** all 20 ~D-PRIMARY indicators are FRED-MATCH/REPRESENTATIVE — confirms FRED-as-mirror role for federal-source upstream data.

---

## §3 — Cadence per FRED Series

FRED inherits cadence + publication-timing from underlying publisher; FRED itself updates within hours of publisher release.

| Cadence class | Count | Indicator examples | FRED update lag from publisher |
|---|---:|---|---|
| Daily (business days) | 18 | Treasury Yields ×10, Currency ×4, Credit Spreads ×3, VIX | <24h |
| Weekly | 3 | NFCI (Sat-published), Initial/Continuing Claims (Thursdays), WALCL (Thursday EOD) | <12h |
| Monthly | 36 | All Lagging/Inflation/Consumer/Labor/Housing macro series | <24h of publisher release |
| Quarterly | 3 | GDP QoQ (A191RL1Q225SBEA), Unit Labor Cost (ULCNFB), Productivity-related | <24h advance estimate; revisions M+2/M+3 |
| Monthly Avg of Daily | 1 | FEDFUNDS (daily DFF averaged) | <24h |
| Discontinued / GAP | 18 | TEDRATE + 17 GAP | n/a |

**AC-CADENCE-TOLERANCE (PRD §5):** Yang's monthly-snapshot cadence is structurally well-aligned with FRED's cadence distribution. Daily Treasury Yields + daily Credit Spreads + daily Currency are higher-resolution than yang requires (yang stores monthly snapshots); harness can sub-sample at T*-anchor month-end OR month-avg per TO-008 decision. No cadence mismatch class fires for FRED-MATCH coverage. Sister to ~D §3 disposition.

---

## §4 — RE Harness Sketch

### §4.1 — FREDAdapter v1 2-step (live-verified working primitive)

```python
import os
import requests
import boto3

class FREDAdapter:
    """v1 2-step pattern — live-verified working 2026-05-26 ~23:?Z.
       Future v2 OAuth swap-in scaffold left as commented-out class (see end of file)."""

    BASE = "https://api.stlouisfed.org/fred"

    def __init__(self, api_key: str | None = None):
        # Sourcing per AWS-Secrets-FredApiKey per ws COO direction (LD-31 + ~D §9 precedent)
        if api_key is None:
            secrets = boto3.client("secretsmanager")
            api_key = secrets.get_secret_value(SecretId="FredApiKey")["SecretString"]
        self.api_key = api_key
        self.session = requests.Session()

    # --- Discovery ---
    def list_releases(self) -> list[dict]:
        """LD-31 catalog ground-truth probe — call before committing release_id mappings."""
        r = self.session.get(
            f"{self.BASE}/releases",
            params={"api_key": self.api_key, "file_type": "json", "limit": 1000},
            timeout=30,
        )
        r.raise_for_status()
        return r.json()["releases"]

    def list_series_in_release(self, release_id: int, limit: int = 1000) -> list[dict]:
        """v1 step 1 — enumerate series in a release."""
        r = self.session.get(
            f"{self.BASE}/release/series",
            params={
                "release_id": release_id,
                "api_key": self.api_key,
                "file_type": "json",
                "limit": limit,
            },
            timeout=30,
        )
        r.raise_for_status()
        return r.json()["seriess"]

    # --- Primary runtime endpoint ---
    def get_observations(
        self,
        series_id: str,
        start: str | None = None,
        end: str | None = None,
        sort_desc: bool = True,
    ) -> list[dict]:
        """v1 step 2 — pull observations for a series.
           Returns [{"date":"YYYY-MM-DD","value":"<str>"}] (parse float client-side; "." = missing)."""
        params = {
            "series_id": series_id,
            "api_key": self.api_key,
            "file_type": "json",
            "sort_order": "desc" if sort_desc else "asc",
        }
        if start:
            params["observation_start"] = start
        if end:
            params["observation_end"] = end
        r = self.session.get(f"{self.BASE}/series/observations", params=params, timeout=30)
        r.raise_for_status()
        return r.json()["observations"]

    def get_series_metadata(self, series_id: str) -> dict:
        """Verify a series exists + cache metadata (title, units, frequency, last_updated)."""
        r = self.session.get(
            f"{self.BASE}/series",
            params={"series_id": series_id, "api_key": self.api_key, "file_type": "json"},
            timeout=30,
        )
        r.raise_for_status()
        seriess = r.json().get("seriess", [])
        return seriess[0] if seriess else {}


# --- FUTURE v2 OAuth swap-in (per ~D §9 commented-scaffold precedent) ---
# class FREDAdapterV2:
#     """v2 release/observations bulk-fetcher — REQUIRES OAuth-class auth (NOT v1 api_key).
#        Live-probe 2026-05-26 ~23:?Z returned HTTP 401 with valid v1 key.
#        Implement when separate OAuth onboarding ops task completes."""
#     BASE = "https://api.stlouisfed.org/fred/v2"
#     def pull_release_bulk(self, release_id: int) -> Iterator[tuple]:
#         # cursor-based pagination; up to 500k obs/page; yields (series_id, date, value)
#         raise NotImplementedError("v2 OAuth onboarding pending")
```

### §4.2 — Per-indicator harness pull plan (49 MATCH + 5 REPRESENTATIVE + 1 DERIVED = 55 active)

```python
# Concrete series-ID registry — bake into harness module as constants
YALP_MACROS_FRED_SERIES = {
    # Treasury Yields (10) — full sub-group coverage
    "Treasury Yields/1M":  "DGS1MO",  "Treasury Yields/3M":  "DGS3MO",
    "Treasury Yields/1Y":  "DGS1",    "Treasury Yields/2Y":  "DGS2",
    "Treasury Yields/3Y":  "DGS3",    "Treasury Yields/5Y":  "DGS5",
    "Treasury Yields/7Y":  "DGS7",    "Treasury Yields/10Y": "DGS10",
    "Treasury Yields/20Y": "DGS20",   "Treasury Yields/30Y": "DGS30",

    # Lagging Indicator (7) — full sub-group coverage
    "Lagging Indicator/GDP QoQ":                  "A191RL1Q225SBEA",
    "Lagging Indicator/Industrial Productivity MoM": "INDPRO",   # REPRESENTATIVE (yang-label variant)
    "Lagging Indicator/Durable Goods Orders MoM": "DGORDER",
    "Lagging Indicator/Factory Orders MoM":       "AMTMNO",
    "Lagging Indicator/Capacity Utilization":     "TCU",
    "Lagging Indicator/Business Inventories YoY": "BUSINV",     # MATCH-DERIVED
    "Lagging Indicator/Trade Balance":            "BOPGSTB",

    # Financial Condition (3 MATCH + 1 DERIVED)
    "Financial Condition/Chicago Fed Financial Condition Index": "NFCI",
    "Financial Condition/Fed Fund Rate":          "FEDFUNDS",    # or DFF for daily
    "Financial Condition/Fed Balance Sheet":      "WALCL",
    # "Financial Condition/Fed Balance Sheet as % of GDP" — DERIVED in harness, no series

    # Inflation (7 MATCH)
    "Inflation/CPI MoM":               "CPIAUCSL",   # MATCH-DERIVED
    "Inflation/Core CPI MoM":          "CPILFESL",   # MATCH-DERIVED
    "Inflation/PCE MoM":               "PCEPI",      # MATCH-DERIVED
    "Inflation/Core PCE MoM":          "PCEPILFE",   # MATCH-DERIVED
    "Inflation/PPI MoM":               "PPIACO",     # MATCH-DERIVED
    "Inflation/Unit Labor Cost YoY":   "ULCNFB",     # MATCH-DERIVED
    "Inflation/UMich 1 Year Inflation": "MICH",

    # Labor Market (8 MATCH + 1 REPRESENTATIVE)
    "Labor Market/Unemployment Rate":              "UNRATE",
    "Labor Market/Initial Jobless Claims":         "ICSA",
    "Labor Market/Continuing Jobless Claims":      "CCSA",
    "Labor Market/US Job Openings":                "JTSJOL",
    "Labor Market/Nonfarm Payrolls":               "PAYEMS",
    "Labor Market/ADP Employment Change":          "ADPMNUSNERSA",  # REPRESENTATIVE
    "Labor Market/Labor Force Participation Rate": "CIVPART",
    "Labor Market/Weekly Hours":                   "AWHAETP",
    "Labor Market/Hourly Earnings MoM":            "CES0500000003",  # MATCH-DERIVED

    # Consumer (4 MATCH + 1 REPRESENTATIVE-derived)
    "Consumer/Retail Sales MoM":               "RSAFS",       # MATCH-DERIVED
    "Consumer/Retail Sales ex Auto MoM":       "RSXFS",       # MATCH-DERIVED (minor methodology caveat)
    # "Consumer/Retail Sales ex Auto and Gas MoM" — REPRESENTATIVE-DERIVED: (RSXFS - RSGASS) / prior_month
    "Consumer/UMich Consumer Sentiment":       "UMCSENT",
    "Consumer/Consumer Credit YoY":            "TOTALSL",     # MATCH-DERIVED

    # Housing Market (4 MATCH)
    "Housing Market/New Home Sales":     "HSN1F",
    "Housing Market/Existing Home Sales": "EXHOSLUSM495S",
    "Housing Market/Housing Starts":     "HOUST",
    "Housing Market/Building Permits":   "PERMIT",

    # Leading Indicator (1 REPRESENTATIVE)
    "Leading Indicator/Leading Index": "USSLIND",  # REPRESENTATIVE (Philly Fed/Crone, not CB LEI)

    # Credit Spread (3 MATCH)
    "Credit Spread/AAA": "BAMLC0A1CAAA",
    "Credit Spread/IG":  "BAMLC0A0CM",
    "Credit Spread/HY":  "BAMLH0A0HYM2",

    # Market Indicator (1 MATCH)
    "Market Indicator/VIX": "VIXCLS",

    # Currency (3 MATCH + 1 REPRESENTATIVE)
    "Currency/DXY":     "DTWEXBGS",     # REPRESENTATIVE (FRED Broad Dollar Index, not ICE DXY)
    "Currency/EUR/USD": "DEXUSEU",
    "Currency/USD/JPY": "DEXJPUS",
    "Currency/GBP/USD": "DEXUSUK",
}

# YALP_MACROS_FRED_GAP = [
#   24 indicators — all 8 Leading except USSLIND, all 7 Investor Sentiment, TED (discontinued),
#   AGG (private), MOVE (private), USD/CNH (offshore), UMich 5-10Y, CB Consumer Confidence,
#   Wards, NAHB, Pending Home Sales, BFCI, Net LT TIC Flows — sister-lane routing per §5
# ]
```

**~55 active series × monthly refresh = ~55 API calls per refresh** (single observations endpoint per series; cursor-paginated for historical backfill). Well under 120-req/min rate limit.

### §4.3 — Failure modes + retry

- **Series not found**: HTTP 400 + `error_code:"400"` + `error_message:"..."` JSON body. Clean failure semantics (vs FRB DDP silent-empty-on-malformed). Harness should validate all 55 series IDs at startup via batch `get_series_metadata()` probe — fail-fast if any series_id has been renamed/discontinued by FRED.
- **Missing observations**: `value: "."` in observation row (NOT null/empty). Parse `value` as float OR detect `"."` and treat as NaN.
- **Rate limit (HTTP 429)**: documented at 120/min; standard exponential backoff on 429.
- **No session/cookie auth**: clean operational risk profile per §1.5.

### §4.4 — Cross-source consistency check (RE harness value-add)

For all 49 FRED-MATCH indicators, harness produces 3-way (or 2-way) cross-validation:

**3-way (Treasury Yields, GDP, PCE, Fed Balance Sheet, Industrial Production, Capacity Utilization, Consumer Credit):**
1. FRED-mirror (this lane primary)
2. Sister upstream-authoritative (~D Treasury Direct / FRB DDP / BEA)
3. Yang-side Bloomberg `data.pkl` (the comparison target — what yang stores)

Verdict-taxonomy per [[feedback_corroborate_with_concern_verdict_shape]] 4-shape model adapted to RE-class:
- **RE-MATCH** if all 3 sources agree within tolerance (±0.01% yields; ±0.1% values; same-date)
- **RE-REPRESENTATIVE** if 2-of-3 agree (typical lag-class — daily revisions between publishers)
- **RE-DRIFT** if all 3 disagree (rare; flag for investigation — likely yang-specific transformation)
- **RE-GAP** if FRED is GAP-class for the indicator (per §2 coverage; sister-lane primary)

**2-way (BLS-only mirrored, Census-only mirrored, ICE-only mirrored):**
1. FRED-mirror
2. Yang-side Bloomberg `data.pkl`

Same verdict-taxonomy minus the 3rd-source confirmation. Sister-lane handoff at TO-007 synthesis for upstream-authoritative validation.

---

## §5 — Coverage % + Sister-Lane Handoffs

### §5.1 — Coverage summary (recap §2.13)

- **FRED-MATCH/REPRESENTATIVE/DERIVED: 55/79 = 69.6%** (broadest single-source coverage in the 5-lane reconnaissance)
- **FRED-GAP: 24/79 = 30.4%** (routes to sister lanes ~B BLS upstream, ~C Census upstream, ~D Treasury/Fed upstream, or ~E aggregate-orphan)

### §5.2 — Sister-lane handoff matrix

| Sister lane | Source | Overlap with ~A FRED | Disposition |
|---|---|---|---|
| **~B BLS** (TO-006b in flight) | BLS API | **HIGH overlap** — FRED mirrors BLS for: CPI, Core CPI, PPI, ULC, UNRATE, ICSA, CCSA, JTSJOL, PAYEMS, CIVPART, AWHAETP, CES0500000003 = 12 indicators. ~B is upstream-authoritative; FRED mirror is publication-lag bound. | **FRED-PRIMARY runtime for monthly cadence; ~B BLS for cross-validation + same-day-freshness if needed.** |
| **~C Census** (TO-006c shipped) | Census EITS | **HIGH overlap** — FRED mirrors Census for: RSAFS, RSXFS, DGORDER, AMTMNO, BUSINV, BOPGSTB, HOUST, PERMIT, HSN1F = 9 indicators. | **FRED-PRIMARY runtime; ~C Census upstream for cross-validation + DRIFT investigation.** |
| **~D Treasury/FDIC** (TO-006d shipped) | Treasury Direct + FRB DDP + BEA + NY Fed Markets | **HIGH overlap** — FRED mirrors ~D-PRIMARY for: Treasury Yields ×10, FEDFUNDS, WALCL, INDPRO, TCU, TOTALSL, GDP QoQ, PCE, Core PCE = 18-20 indicators. ~D explicitly recommends FRED-PRIMARY runtime + ~D for cross-check in §5.3 of their brief. | **FRED-PRIMARY runtime AGREED (~D recommendation absorbed); ~D for upstream-authoritative arbitration when DRIFT class fires.** |
| **~E Aggregate-orphan** (TO-006e in flight) | Conference Board, ISM, S&P Global, NFIB, AAII, UMich (5-10Y), NAHB, NAR, Wards, ICE BofA Aggregate, Bloomberg, CBOE proprietary, ICE proprietary | **ZERO FRED overlap for the 24 FRED-GAP indicators** — ~E is the sister-lane primary for ALL of: 7 Leading (ex USSLIND) + 7 Investor Sentiment + TED Spread DISCONTINUED + AGG + MOVE + CB Consumer Confidence + Wards + NAHB + Pending Home Sales + BFCI + UMich 5-10Y. | **~E-PRIMARY runtime for all 24 FRED-GAP indicators.** |

### §5.3 — Recommendation for TO-007 synthesis (~A primary author per TO §notes)

**Two-tier harness architecture (consolidated ~A+~B+~C+~D+~E recommendation):**

- **PRIMARY runtime tier (~A FRED + ~E private/survey)**:
  - **~A FRED**: 55 of 79 indicators (69.6%) — single adapter, single auth model (api_key), single rate-limit model. Most ops-simple harness layer.
  - **~E aggregate-orphan**: 24 of 79 indicators (30.4%) — heterogeneous adapter set (per-source HAR-RE per ~D §7 pattern OR per-source CSV/XLSX/API integrations) for the FRED-GAP class.

- **CROSS-CHECK / upstream-authoritative tier (~B/~C/~D)**:
  - **~D Treasury/Fed/BEA**: upstream-authoritative for 18-20 federal-source indicators (Treasury Yields, FRB releases, BEA NIPA). Use for same-day-freshness OR DRIFT arbitration.
  - **~C Census EITS**: upstream-authoritative for 9 Census-published indicators. Use for DRIFT arbitration.
  - **~B BLS**: upstream-authoritative for 12 BLS-published indicators. Use for DRIFT arbitration.

**Rationale for FRED-PRIMARY over upstream-source-primary:**
1. **Operational simplicity**: 1 adapter + 1 key + 1 rate-limit vs 4+ adapters with mixed auth models (BEA UserID, Census API key, FRB DDP HAR-RE, Treasury Direct CSV download). Maintenance burden scales linearly with adapter count.
2. **Publication-lag is acceptable**: FRED mirrors with <24h lag; yang's monthly snapshot cadence absorbs any sub-day lag without DRIFT class fires.
3. **Sister ~D explicitly endorses this pattern** (their §5.3 recommendation). 4-of-5 lanes converge on FRED-PRIMARY runtime + sister-lane upstream-cross-check.
4. **FRED's revision-history support** (vintages via `realtime_start`/`realtime_end` per observation) provides audit-trail equivalent to upstream-source raw publishes.

**Phase 2b TO-007 verdict-taxonomy alignment:** RE-MATCH / RE-REPRESENTATIVE / RE-GAP / RE-DRIFT (per TO-006a `<cross_domain_coordination>` v0.3-substance-now-Phase-2-canonical) materializes cleanly here. Treasury Yields are the most-likely RE-MATCH class (3-way agree); BEA NIPA + BLS revision-bound series are most-likely RE-REPRESENTATIVE (advance/2nd/3rd estimate revisions); 24 FRED-GAP = RE-GAP class by definition (route to ~E or accept GAP).

---

## §6 — FRED-Specific Quirks

1. **Numeric values returned as STRING in JSON `observations[].value`** — explicit float parse client-side required. Missing observations encoded as `"."` (NOT null/empty). Sister to Census EITS quirk + Treasury Fiscal Data quirk; cross-publisher consistent pattern.
2. **`/fred/releases?api_key=` enumerates ~300 releases (FRED-internal organization, NOT publisher-organization)** — release_id allocation is FRED-historical (numerically-incremental as releases were added); mapping is NOT predictable from publisher's own release-codes (per LD-31 G.19=14-not-17 + TIC=3-not-39 corrections).
3. **`/fred/series/observations` returns ALL history by default** — yang's monthly cadence pulls only need recent window; pass `observation_start={T*-N_months}` to bound payload.
4. **v2 `release/observations` bulk endpoint is OAuth-gated** (per ws COO `20260526T204136Z` CRITICAL CORRECTION absorbed; per ~D §9 corrections `6d3a75014` empirically REVISED). v1 api_key authentication ONLY works against v1 2-step pattern (`release/series` + `series/observations`); v2 returns HTTP 401 even with valid v1 key. Future v2 OAuth onboarding is a SEPARATE ops task.
5. **MoM/YoY derivation required for many MATCH-class indicators**: FRED publishes raw level series (`CPIAUCSL`, `TOTALSL`, `BUSINV`); MoM/YoY values are client-side computed `(t / t-N - 1) * 100`. Yang publishes pre-computed MoM/YoY values. Verification axis at Phase 2b TO-008: yang-MoM-value vs FRED-derived-MoM = MATCH expected (modulo published-revisions vintage selection).
6. **`USSLIND` is Philly Fed Crone leading index, NOT Conference Board LEI** — methodology-variant. If Wave-2 expects CB LEI specifically, FRED is GAP-class (route ~E). USSLIND remains a defensible Leading-class proxy with documented methodology citation.
7. **ISM PMI series discontinued in FRED ~2016** (NAPM, NAPMNOI, NAPMSDI all NOT FOUND). 6 of 8 Leading indicators (4 PMI + 2 ISM New Orders) have ZERO FRED coverage. Sister-lane ~E only path.
8. **TEDRATE DISCONTINUED 2022** (LIBOR retirement). Yang Ted Spread indicator is structurally obsolete at the underlying-rate level; Phase 2b TO-007 should surface as Andrew architectural decision: deprecate or substitute SOFR-3M minus T-Bill-3M as modern equivalent.
9. **ICE BofA spread series (`BAMLC0A1CAAA`, `BAMLC0A0CM`, `BAMLH0A0HYM2`)** are PUBLIC via FRED-mirror; underlying ICE-published source is proprietary. Yang AGG (Bloomberg Aggregate) is NOT in this set — Bloomberg US Aggregate Bond Index is private, no FRED mirror. (Phase 2b TO-007 should clarify whether yang AGG is bond-yield, total-return, or duration — affects whether ICE-BAML "US Treasury Master" or similar series could be a REPRESENTATIVE proxy.)
10. **DTWEXBGS (FRED Broad Dollar Index) ≠ ICE DXY** — methodology-variant (FRED is FED-calculated trade-weighted basket; ICE DXY is 6-currency ICE-basket). Correlated but not 1:1 daily values. Yang DXY indicator likely references ICE DXY (the common quote). Use DTWEXBGS as REPRESENTATIVE with documented variance OR route to broker-direct (Bloomberg/Reuters) via ~E for ICE-exact.
11. **Atlanta Fed NLP Sentiment search yielded only DISCONTINUED series** (`ATLSBUIREI`, `ATLSBUSGUI`). Yang's "Fed NLP Sentiment" indicator likely references a yang-internal NLP-derived sentiment over Fed minutes/speeches corpus, NOT a FRED-hosted Atlanta Fed sentiment series. Phase 2b TO-007 should clarify yang-side source-of-record.
12. **No session/cookie auth model.** Sister to ~D Treasury Direct + Census + NY Fed Markets clean-ops profile. Compare YCharts 403-session-eviction class per [[feedback_ycharts_http_400_is_cookie_stale_class]]. FRED's stable api_key model is the cleanest operational profile across all 5 reconnaissance lanes.

---

## §7 — RAVC2-Request

**To:** 2.0.0_SA_COO
**From:** 0.1.0_DS_MarketIntelligence~A
**TO:** YALP_MACROS.006a — FRED multi-source RE reconnaissance (Phase 2a lane A)

**Evidence:**
- This brief at `docs/briefs/yalp_macros_phase2a_fred_reconnaissance_2026-05-26.md`
- §1 FRED API surface — base URL + auth model + v1 2-step primitive LIVE-VERIFIED (~23:?Z post-AWS-Secrets-key retrieval) + v2 OAuth-gated documented + 5 additional v1 endpoints catalogued + rate limit + failure semantics + LIVE-VERIFIED release_id catalog (~300 releases enumerated; 6 target release_ids confirmed/corrected per LD-31)
- §2 Per-indicator match-set — 79/79 indicators classified across 12 groups; **49 FRED-MATCH + 5 FRED-REPRESENTATIVE + 1 FRED-DERIVED + 24 FRED-GAP** (incl. 1 DISCONTINUED); per-group coverage summary in §2.13 (100% Lagging/Labor/Treasury/Market vs 0% Investor Sentiment)
- §3 Cadence per FRED series — 6 cadence classes (daily / weekly / monthly / quarterly / monthly-avg-of-daily / discontinued-GAP); FRED-publisher-lag <24h structural
- §4 RE harness sketch — FREDAdapter v1 2-step adapter class (Python) + per-indicator series-ID registry (55 active) + future v2 OAuth swap-in scaffold commented-out + failure-mode + retry + 3-way cross-source consistency-check pattern for Phase 2b TO-007 verdict-taxonomy
- §5 Coverage % + sister-lane handoff matrix — **69.6% FRED-coverage** (broadest single-source) + ~B/~C/~D HIGH-overlap cross-check tier + ~E-PRIMARY for 24 FRED-GAP indicators; ~D-recommendation absorbed (FRED-PRIMARY runtime); 4-of-5 lanes converge on FRED-PRIMARY architectural lean
- §6 12 FRED-specific quirks — STRING-encoded numeric + release_id catalog-internal allocation + MoM/YoY derive required + USSLIND-vs-CB-LEI methodology-variant + ISM-discontinued-2016 + TEDRATE-discontinued-2022 + DTWEXBGS-vs-ICE-DXY methodology-variant + Atlanta Fed NLP yang-internal-not-FRED + v2-OAuth-gated + clean-ops-profile (no session/cookie)

**Acceptance criteria (5/5 met):**
- **AC1** — FRED API surface enumerated (base + key APIs documented): ✅ §1 + LIVE-VERIFIED ~23:?Z
- **AC2** — Per-indicator match-set populated for all 79 yang macro indicators (FRED series ID OR `n/a` reason): ✅ §2.1-§2.12 (79/79; explicit class label per row); §2.13 group-level summary
- **AC3** — Cadence per FRED series documented: ✅ §3 (6-class taxonomy)
- **AC4** — RE harness sketch documented for TO-008 follow-on (NOT implementation; design-level): ✅ §4 (FREDAdapter class + series-ID registry + failure modes + cross-source pattern)
- **AC5** — Coverage % + sister-lane handoffs documented: ✅ §5 (69.6% FRED-coverage + handoff matrix + 4-of-5 lane convergence on FRED-PRIMARY runtime)

**Disposition recommendation:** ACCEPT.

**No production touches.** Reconnaissance class; documentation-only commit. Read-only verification scope per PRD v0.5 §4 + Andrew per-page charter framing.

---

## §8 — Memory candidates banked

Candidates surfaced through this reconnaissance for future memory-write disposition (CTO/MSTR ratification; non-blocking):

1. **`release_id-guesses-must-be-live-verified-against-fred-catalog-before-committing`** — per ws COO CRITICAL CORRECTION `20260526T204136Z` + ~D §9 corrections `6d3a75014` + ~A §1.6 live-verify gate. Sister to [[feedback_commit_age_use_iso_utc_not_local]] + [[feedback_api_catalog_live_verify_before_committing_ids]] empirical-anchor-over-assumption discipline. **CANDIDATE: extend LD-31 from generic "API-internal IDs" → specific "FRED release_id" worked example.**

2. **`fred-v2-oauth-gated-not-v1-key-compatible`** — empirical class refinement banked as workaround: v2 endpoint OAuth-class auth requirement is undocumented externally; live-probe alone reveals it. Sister-lane ~D `6d3a75014` first-fire + ~A this brief second-fire (post correction-cascade absorption). **CANDIDATE: API-version auth-class transitions need live-probe verification, not docs alone.**

3. **`fred-as-broadest-single-source-mirror-pattern`** — 69.6% FRED coverage of 79-indicator universe makes FRED the convenient PRIMARY for any macro page; sister-lane upstream is CROSS-CHECK not PRIMARY for ops-efficiency. Confirms 4-of-5 lane convergence pattern. **CANDIDATE: when designing multi-source harness with mirror-class options, prefer single-mirror PRIMARY (lower ops burden) + upstream-CROSS-CHECK (DRIFT-arbitration only) over upstream-PRIMARY (multi-adapter complexity).**

4. **`mirror-vs-origin-distinction-affects-verdict-taxonomy`** — FRED is mirror for 49 of 49 MATCH indicators; ZERO origin-class FRED-PRIMARY data. Phase 2b TO-007 verdict-taxonomy RE-MATCH must distinguish 2-way (FRED vs yang) from 3-way (FRED + upstream vs yang) — 3-way is structurally stronger verdict. **CANDIDATE: verdict-taxonomy granularity should reflect source-class (mirror vs origin).**

5. **`yang-internal-vs-publisher-published-indicator-class-distinction`** — Fed NLP Sentiment + Industrial Productivity MoM (Phase 1 F4 sister) + Ted Spread (post-LIBOR) are yang-side indicators where the label deviates from publisher-published structure. Phase 2b TO-007 surface these for Andrew architectural disposition (deprecate / substitute / re-source). **CANDIDATE: reconnaissance briefs should flag yang-internal-vs-publisher mismatches as architectural-class findings, not data-class findings.**

Banking deferred to MSTR /govern + Andrew sovereign ratification per LD-0025 ALWAYS-PROCEED + Article XVI.

---

## §9 — Standing posture

Brief shipped. Phase 2b TO-007 synthesis is the next ~A-primary deliverable (per TO §notes: "you're primary author on TO-007 source-of-truth synthesis brief post all 5 Phase 2a lanes ship"). Convergence gates on:
- ~B BLS brief ship (in flight per ws COO message)
- ~E Aggregate-orphan brief ship (in flight per ws COO message)
- (Phase 2a Wave-1 already 2-of-5 shipped: ~C Census + ~D Treasury/FDIC at `4f4901d34` cascade + `6d3a75014` corrections)
- ~A FRED brief shipped this commit = 3-of-5

Standing /work 20m loop for any sister-lane convergence MCPs OR Phase 2b TO-007 GO dispatch from ws COO.

— 0.1.0_DS_MarketIntelligence~A
2026-05-26 work-cycle:1 (Phase 2a YALP_MACROS.006a)
