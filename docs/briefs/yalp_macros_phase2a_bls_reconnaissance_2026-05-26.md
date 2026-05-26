# YALP_MACROS Phase 2a — BLS Multi-Source Reconnaissance

**TO:** YALP_MACROS.006b — BLS multi-source authoritative-source RE reconnaissance (Phase 2a parallel lane B)
**Author:** 0.1.0_DS_MarketIntelligence~B (Phase 2a BLS lane; sister to ~A FRED + ~C Census + ~D Treasury/FDIC + ~E Aggregate-orphan)
**PRD:** `docs/architecture/YALP_MACROS.md` v0.5 RE-OPENED `7e781ea8c` — Phase 2 multi-source RE charter
**Authority:** Andrew sovereign direct ~21:00Z + RE-OPEN Phase 2 ~21:05Z + MSTR LD-0104 fast-trajectory endorsement + ws COO /allocation #110 GO `79417a259` + MSTR SPAWN-WITH-DIRECTION `20260526T210829Z`
**T*:** indicator-cadence-bound (most BLS series monthly with M+1 release lag; jobless-claims-class is DoL NOT BLS); brief authored 2026-05-26 against current BLS Public Data API v2 surface live-verified ~21:?Z anonymous tier
**Status:** Phase 2a reconnaissance COMPLETE — 5/5 ACs met

---

## §0 — TL;DR

**BLS Public Data API v2 (`https://api.bls.gov/publicAPI/v2/timeseries/data/`) is the upstream-authoritative source for 10 of the 79 yang macro indicators (12.7%).** All 10 are FRED-mirrored (FRED is downstream-publication-lag-bound mirror); BLS-direct advantage = same-day-of-publication freshness + footnote-level revision flags (P=preliminary, R=revised) richer than FRED's vintage-encoding. v1 anonymous tier (25 series/query, 10y history, 25 queries/day) is sufficient for reconnaissance; v2 registered (50 series/query, 20y, 500 queries/day, calc-bundle) recommended for production harness — free signup, no AWS-Secrets dependency yet (`BlsApiKey` secret NOT present in Secrets Manager as of brief authoring).

**Per-indicator coverage breakdown (79-indicator universe):**

| Coverage class | Count | % | Notes |
|---|---:|---:|---|
| **BLS-MATCH** (BLS upstream-authoritative; 1:1 yang→BLS equivalence) | 10 | 12.7% | CPI (CUUR0000SA0), Core CPI (CUUR0000SA0L1E), PPI (WPSFD4 modern / WPU00000000 legacy), Unit Labor Cost (PRS85006112), Unemployment Rate (LNS14000000), JOLTS Job Openings (JTS000000000000000JOL), Nonfarm Payrolls (CES0000000001), Labor Force Participation Rate (LNS11300000), Weekly Hours (CES0500000002), Hourly Earnings (CES0500000003) |
| **BLS-REPRESENTATIVE** (BLS-adjacent series; methodology-variant or yang-side may use alt) | 0 | 0% | None for 79-universe — BLS is either upstream-authoritative-MATCH or absent |
| **BLS-GAP** (NOT in BLS; route to sister-lane or accept as orphan) | 69 | 87.3% | All Leading (8) + Lagging GDP/CapUtil/IP/Census-trade-class (7) + Financial Condition (6) + Inflation UMich-1Y/UMich-5-10Y (2) + Labor Market ICSA/CCSA/ADP (3) + Consumer (7) + Housing (6) + Investor Sentiment (7) + Treasury Yields (10) + Credit Spread (5) + Market VIX (1) + Currency (5) |

**Critical reconnaissance findings (banked candidates):**
1. **Jobless Claims (ICSA + CCSA) are NOT BLS — they are DoL ETA (Department of Labor Employment & Training Administration).** Live-probe response: `"Invalid Series for Series ICSA"` + `"Series does not exist for Series CCSA"` in `message[]` array (partial-success — `status:REQUEST_SUCCEEDED` overall + EMPTY `data[]` for the invalid series). Yang's "Initial/Continuing Jobless Claims" indicators route via ~D (Treasury/Fed mirror) or FRED (`ICSA`/`CCSA` series — FRED mirrors DoL ETA, not BLS). Sister-finding to ~A FRED §2.5 row 33/34.
2. **PPI has TWO modern series in BLS** — `WPSFD4` (PPI Final Demand index — 2009-rebased modern headline) vs `WPU00000000` (PPI All Commodities — legacy continuous series). Yang's `PPIACO` mirror in FRED maps to legacy `WPU00000000`. **Modern WPSFD4 is methodology-more-aligned-with-economic-press**; legacy WPU00000000 maintains 1947-present continuity. Phase 2b TO-007 architectural decision: harness should expose BOTH or surface yang-label-vs-publisher-class mismatch.
3. **Seasonal-adjustment is encoded in series_id prefix** — `LN_S_14000000` (Seasonally Adjusted) vs `LN_U_14000000` (Unadjusted). Yang likely consumes SA (Bloomberg `USURTOT Index` = monthly SA UNRATE); harness must lock S-prefix. Sister to FRED's series-id-bound SA-vs-NSA choice (~C §5.3 noted Census exposes both via `seasonally_adj=yes/no` filter — BLS embeds in series_id).
4. **BLS v2 anonymous tier returns partial-success with per-series error messages** — `status: REQUEST_SUCCEEDED` + `message: ["Invalid Series for Series X", ...]` + EMPTY `data[]` for invalid IDs. Harness MUST inspect `message[]` AND per-series `data[]` length, not just top-level status. Sister to Census Missing-Key-HTML-200 failure-mode (~C §6 row 1); different mechanism, same "happy HTTP, look deeper" pattern.

**Two-tier harness disposition (consolidated with ~A/~C/~D recommendations):**
- **PRIMARY runtime tier:** FRED (~A) — broadest single-source mirror (69.6%) — operationally simpler than per-publisher adapters
- **CROSS-CHECK tier for BLS-MATCH indicators (this lane):** BLS-direct for same-day-freshness + footnote-level revision flags when DRIFT class fires
- **GAP routing for 69 BLS-GAP indicators:** sister-lane primaries (~A FRED-PRIMARY for 49/79, ~C Census-overlap, ~D Treasury/Fed-PRIMARY, ~E aggregate-orphan-PRIMARY)

**Phase 2b TO-007 synthesis disposition:** BLS is the **CROSS-CHECK** lane for 10 federal-source labor + price indicators where FRED is the convenient mirror but BLS holds upstream-authoritative status. Two-tier harness with FRED-PRIMARY + BLS-CROSS-CHECK is the architecturally-clean lean (4-of-5 lane convergence per ~A §5.3).

---

## §1 — BLS API Surface

### §1.1 — Auth + base URL

**Base:** `https://api.bls.gov/publicAPI/v{1,2}/timeseries/data/`
**Auth:** v1 = anonymous (no key required); v2 = optional registration key as JSON body field `registrationkey` (free signup at `https://data.bls.gov/registrationEngine/`).
**Key sourcing:** `BlsApiKey` secret NOT yet present in AWS Secrets Manager (verified ~21:?Z `aws secretsmanager describe-secret --secret-id BlsApiKey` → `ResourceNotFoundException`). Production harness should onboard key + secret per `~A` `FredApiKey` precedent (sister to LD-31 + ~D §9 corrections).

**Tier caps (per BLS API documentation, `https://www.bls.gov/developers/api_signature_v2.htm`):**

| Tier | Series/query | History | Queries/day | Calculations | Notes |
|---|:-:|:-:|:-:|:-:|---|
| v1 anonymous | 25 | 10 years | 25 | No | Sufficient for reconnaissance only |
| v2 anonymous | 25 | 10 years | 25 | No | Same caps as v1; v2 endpoint required for POST JSON body |
| **v2 registered (free)** | **50** | **20 years** | **500** | **Yes (net change + percent change auto-computed)** | **Recommended for production harness** |

### §1.2 — v2 POST primitive (LIVE-VERIFIED — preferred runtime)

**Endpoint:**
```
POST https://api.bls.gov/publicAPI/v2/timeseries/data/
Content-Type: application/json

{
  "seriesid": ["LNS14000000", "CUUR0000SA0", "CES0000000001"],
  "startyear": "2024",
  "endyear": "2026",
  "registrationkey": "<KEY>"               (optional; v1/v2-anonymous tier omits)
  "calculations": true                     (v2-registered only; auto net/percent change)
  "annualaverage": true                    (v2-registered only; includes M13 annual avg row)
  "catalog": true                          (v2-registered only; includes series metadata)
  "aspects": true                          (v2-registered only; multi-aspect series)
}
```

**Live-verified shape (~21:?Z anonymous tier, 3-series probe LNS14000000 + CUUR0000SA0 + CES0000000001 startyear=endyear=2026):**

```json
{
  "status": "REQUEST_SUCCEEDED",
  "responseTime": 78,
  "message": [],
  "Results": {
    "series": [
      {
        "seriesID": "LNS14000000",
        "data": [
          {"year":"2026","period":"M04","periodName":"April","latest":"true","value":"4.3","footnotes":[{}]},
          {"year":"2026","period":"M03","periodName":"March","value":"4.3","footnotes":[{}]},
          {"year":"2026","period":"M02","periodName":"February","value":"4.4","footnotes":[{}]},
          {"year":"2026","period":"M01","periodName":"January","value":"4.3","footnotes":[
            {"code":"12","text":"January 2026 estimates were revised to incorporate updated population controls. ..."}
          ]}
        ]
      },
      ...
    ]
  }
}
```

**Response shape notes:**
- `status` always present; `REQUEST_SUCCEEDED` = HTTP-level success (does NOT guarantee per-series success — see §1.5 partial-failure mode)
- `responseTime` = ms (server-side; useful for SLA monitoring)
- `message[]` = top-level errors AND per-series invalid-id warnings (partial-success mode)
- `Results.series[]` = always present even if all series invalid (EMPTY `data[]` per invalid series)
- Per-observation: `year` + `period` (M01-M12 month; M13 annual avg; Q01-Q04 quarter; Q05 annual) + `periodName` (human-readable) + `latest` (only on most-recent obs) + `value` (STRING — parse float client-side) + `footnotes[]` (per-obs flags)
- Footnotes: `P` = preliminary; `R` = revised; numeric codes = per-survey revision-class flags (e.g., `12` for CPS population-control revisions)

### §1.3 — v1 GET primitive (LIVE-VERIFIED — fallback for single-series probes)

```
GET https://api.bls.gov/publicAPI/v1/timeseries/data/{seriesId}
```

Returns same JSON shape as v2 with single-series fixed. Anonymous tier. No POST body required. Useful for harness self-tests + ad-hoc series-id validation. Latest 3 years of data by default.

### §1.4 — Additional v2 endpoints (reference)

| Endpoint | Purpose | When to use |
|---|---|---|
| `/v2/timeseries/data/` | Bulk timeseries pull (1-50 series/request) | **Primary runtime endpoint** for harness |
| `/v1/timeseries/data/{seriesId}` | Single-series pull | Fallback / self-test |
| `/v2/surveys` | List all 73 BLS surveys (`survey_abbreviation` + `survey_name`) | Discovery — enumerated below in §1.6 |
| `/v2/surveys/{abbr}` | Survey metadata (description + URL) | Discovery — per-survey context |
| `/v2/timeseries/popular?survey={abbr}` | Popular series in a survey (top-N most-requested) | Discovery — quick anchor identification for unfamiliar surveys |
| `/v1/timeseries/data/{seriesId}?startyear=&endyear=` | v1 with year range | Backfill within 10y v1 cap |

### §1.5 — Rate limits + failure modes

- **Rate limit:** 25 queries/day anonymous; 500 queries/day v2-registered (`X-RateLimit-Remaining` header surfaces remaining quota — NOT verified empirically; documented in BLS API docs).
- **Partial-success failure:** invalid series IDs returned as EMPTY `data[]` + warning text in top-level `message[]`. **`status` remains `REQUEST_SUCCEEDED` even when all series in a batch are invalid.** Harness MUST inspect `message[]` AND per-series `len(data[])` — top-level status check is structurally insufficient.
  - Live-verified example: `{"seriesid":["ICSA","CCSA"]}` returned `status:REQUEST_SUCCEEDED` + `message:["Invalid Series for Series ICSA","Series does not exist for Series CCSA"]` + 2 EMPTY series objects.
- **Quota-exceeded failure:** when daily query limit hit, `status:REQUEST_NOT_PROCESSED` + `message:["Daily threshold for total number of requests exceeded"]` (per BLS docs; NOT empirically reproduced — would cost quota to verify).
- **Malformed-request failure:** invalid JSON body returns `status:REQUEST_NOT_PROCESSED` + descriptive `message[]`. Per BLS docs.
- **No session/cookie auth.** Sister to ~A FRED + ~C Census + ~D Treasury Direct clean-ops profile. Compare YCharts 403-session-eviction class per [[feedback_ycharts_http_400_is_cookie_stale_class]].
- **Value encoding:** Numeric values returned as STRING in `data[].value` (parse float client-side); missing observations encoded as `"-"` (NOT null, NOT empty per BLS docs — anonymous probe did not surface a `-` example). Sister to FRED (`.`) + Census EITS (string-typed cell_value) + Treasury Fiscal Data quirks.

### §1.6 — Live-verified BLS survey catalog (LD-31 ground-truth)

Per [[feedback_api_catalog_live_verify_before_committing_ids]] — survey + series-id mappings live-verified against `/v2/surveys` + per-series probe at brief authoring time. Ground-truth ~21:?Z anonymous tier.

**Full surveys catalog returned 73 surveys.** Relevant subset for 79-indicator universe:

| Abbr | Survey name | Relevant indicators |
|---|---|---|
| **CU** | Consumer Price Index - All Urban Consumers | **CPI MoM + Core CPI MoM** (CUUR0000SA0 + CUUR0000SA0L1E) |
| **CW** | Consumer Price Index - Urban Wage Earners and Clerical Workers | (alternative CPI for wage-earners; not in 79-universe) |
| **SU** | Consumer Price Index - Chained Consumer Price Index | (alternative chained CPI; SUUR0000SA0 — not in 79-universe) |
| **WP** | Producer Price Index-Commodities | **PPI MoM** (WPSFD4 modern + WPU00000000 legacy) |
| ND/PC | Producer Price Index Industry Data | (industry-level PPI; not in 79-universe) |
| **LN** | Labor Force Statistics from the Current Population Survey | **UNRATE + LFPR** (LNS14000000 + LNS11300000) |
| **CE** | Employment, Hours, and Earnings from the Current Employment Statistics survey (National) | **PAYEMS + Weekly Hours + Hourly Earnings** (CES0000000001 + CES0500000002 + CES0500000003) |
| **JT** | Job Openings and Labor Turnover Survey | **JOLTS Job Openings** (JTS000000000000000JOL) |
| **CI/EC** | Employment Cost Index | (ECI total comp — not in 79-universe; CIU1010000000000A live-verified) |
| **PR** | Major Sector Productivity and Costs | **Unit Labor Cost YoY** (PRS85006112) |
| MP | Major Sector Total Factor Productivity | (TFP; not in 79-universe) |
| EI | Import/Export Price Indexes | (Import/Export inflation; not in 79-universe) |
| CC/CM | Employer Costs for Employee Compensation | (ECEC; not in 79-universe) |
| OE | Occupational Employment and Wage Statistics | (OES; not in 79-universe) |

**Banked LD candidate (per [[feedback_api_catalog_live_verify_before_committing_ids]]):** survey-abbreviation + series_id-construction conventions per BLS are well-documented in BLS Handbook of Methods (`https://www.bls.gov/opub/hom/`); however, **live-probe is still required for series-existence verification** since BLS discontinues series silently (e.g., legacy WPU vs modern WPSFD; LNS14000000 has both -SA and -U variants encoded in 3rd char prefix). Sister to ~A LD-31 release_id corrections (G.19=14, TIC=3); BLS analog = "series_id-must-be-live-verified" not "guessed from survey conventions alone."

---

## §2 — Per-Indicator Match-Set (79 yang → BLS)

### §2.1 — BLS-MATCH (10 indicators; 10/79 = 12.7%)

All series live-verified ~21:?Z via v2 anonymous probe (3-batch enumeration covering 12 candidate series IDs). All 10 returned valid `data[]` with current-year observations.

| # | Yang indicator | yang Bloomberg ticker | BLS series ID | BLS survey | Cadence | FRED-mirror | Class |
|---|---|---|---|---|---|---|---|
| 1 | **CPI MoM** (Inflation) | `CPI YOY Index` (or MoM) | `CUUR0000SA0` | CU (CPI-U) | Monthly (M+1 release ~10th-15th) | ✅ `CPIAUCSL` | **MATCH-DERIVED** (BLS publishes level index; yang MoM = client-side `(t / t-1 - 1) * 100`) |
| 2 | **Core CPI MoM** (Inflation) | `CPI XYOY Index` | `CUUR0000SA0L1E` | CU (CPI-U Less Food & Energy) | Monthly (M+1 same release as headline CPI) | ✅ `CPILFESL` | **MATCH-DERIVED** |
| 3 | **PPI MoM** (Inflation) | `PPI FINL Index` or `PPI CHNG` | `WPSFD4` (modern PPI Final Demand) OR `WPU00000000` (legacy All Commodities) | WP | Monthly (M+1 ~10th-15th) | ✅ `PPIACO` (FRED maps to legacy `WPU00000000`) | **MATCH-DERIVED** (level; MoM derive). **Modern vs legacy class-distinction surfaced as Phase 2b TO-007 architectural finding.** |
| 4 | **Unit Labor Cost YoY** (Inflation) | `USULCYOY Index` | `PRS85006112` | PR (Major Sector Productivity and Costs — Nonfarm Business) | Quarterly (Q+1 ~6 weeks post quarter-end) | ✅ `ULCNFB` | **MATCH** (BLS publishes %chg directly; not derive-required) |
| 5 | **Unemployment Rate** (Labor Market) | `USURTOT Index` | `LNS14000000` | LN (CPS) | Monthly (M+1 ~1st Friday post month) | ✅ `UNRATE` | **MATCH** (BLS publishes rate directly) |
| 6 | **US Job Openings** (Labor Market) | `JOLTTOTL Index` | `JTS000000000000000JOL` | JT (JOLTS) | Monthly (M+2 ~1st Tuesday — 1-month-lag vs other Labor) | ✅ `JTSJOL` | **MATCH** (BLS publishes level in thousands) |
| 7 | **Nonfarm Payrolls** (Labor Market) | `NFP TCH Index` (MoM change) | `CES0000000001` | CE (CES) | Monthly (M+1 ~1st Friday — JOINT release with UNRATE) | ✅ `PAYEMS` | **MATCH-DERIVED** (BLS publishes level in thousands; yang MoM-change = client-side `t - t-1`) |
| 8 | **Labor Force Participation Rate** (Labor Market) | `PRUSTOT Index` | `LNS11300000` | LN (CPS) | Monthly (M+1 same release as UNRATE) | ✅ `CIVPART` | **MATCH** (BLS publishes rate directly) |
| 9 | **Weekly Hours** (Labor Market) | `AHE TOTL Index` or `AWH TOTL` | `CES0500000002` | CE (CES — Total Private Average Weekly Hours of All Employees) | Monthly (M+1 same release as PAYEMS) | ✅ `AWHAETP` | **MATCH** (BLS publishes hours directly) |
| 10 | **Hourly Earnings MoM** (Labor Market) | `AHE CMOM Index` | `CES0500000003` | CE (CES — Total Private Average Hourly Earnings of All Employees) | Monthly (M+1 same release as PAYEMS) | ✅ `CES0500000003` (FRED-mirror preserves BLS id verbatim) | **MATCH-DERIVED** (BLS publishes level $/hour; MoM derive) |

**3-way cross-validation potential (sister-lane convergence):**
- UNRATE: BLS LNS14000000 (upstream) vs FRED UNRATE (mirror) vs yang `USURTOT Index` (Bloomberg) — Phase 2b TO-008 expected RE-MATCH class
- PAYEMS: BLS CES0000000001 (upstream level) vs FRED PAYEMS (mirror) vs yang `NFP TCH Index` (Bloomberg MoM-change) — DERIVE-class verification (BLS level → MoM derive must match Bloomberg headline number)
- CPI: BLS CUUR0000SA0 (upstream level) vs FRED CPIAUCSL (mirror) vs yang `CPI YOY Index` (Bloomberg YoY) — DERIVE-class

### §2.2 — BLS-GAP (69 indicators; 69/79 = 87.3%)

The other 69 yang indicators have **no BLS authoritative source**. Best-source attribution from sister-lane reconnaissance:

| Group | Total | BLS-MATCH | BLS-GAP | Primary alternative source |
|---|---:|---:|---:|---|
| Leading Indicator | 8 | 0 | 8 | Conference Board (LEI), ISM (PMI), S&P Global (PMI), NFIB → ~E aggregate-orphan; FRED USSLIND-proxy (REPRESENTATIVE) for LEI per ~A |
| Lagging Indicator | 7 | 0 | 7 | BEA (GDP, PCE class), FRB (IP, CapUtil), Census (Trade, DG/Factory Orders, BUSINV) → ~A FRED mirror or ~C/~D direct |
| Financial Condition | 6 | 0 | 6 | Chicago Fed (NFCI), FRB (FedFunds, Balance Sheet, TIC) → ~A FRED or ~D direct |
| **Inflation** | 8 | 5 (CPI, Core CPI, PPI, ULC; UMich-1Y is GAP) | 3 | UMich (1Y + 5-10Y inflation expectations), BEA (PCE + Core PCE class). **PCE NOT BLS — PCE is BEA NIPA T20807.** |
| **Labor Market** | 9 | 5 (UNRATE, JTSJOL, PAYEMS, LFPR, Hours, Earnings = 6 actually counting Hours+Earnings as 2) | 3 | DoL ETA (Initial + Continuing Jobless Claims — **NOT BLS**); ADP private (ADP Employment Change). **Jobless Claims live-probed as `Invalid Series` in BLS API.** |
| Consumer | 7 | 0 | 7 | Census (Retail Sales family), UMich (Sentiment), Conference Board (CCI), FRB G.19 (Consumer Credit), Wards (Vehicle Sales) → ~A/~C/~E |
| Housing Market | 6 | 0 | 6 | Census (Housing Starts, Permits, New Home Sales), NAHB (HMI), NAR (Existing + Pending Home Sales) → ~A/~C/~E |
| Investor Sentiment | 7 | 0 | 7 | AAII private (6 series), Atlanta Fed NLP yang-internal-derived → ~E |
| Treasury Yields | 10 | 0 | 10 | Treasury Direct + FRB H.15 → ~D primary, ~A FRED mirror |
| Credit Spread | 5 | 0 | 5 | ICE BofA (AAA, IG, HY), Bloomberg Aggregate (private), TED (discontinued 2022) → ~A FRED mirror or ~E |
| Market Indicator | 1 | 0 | 1 | CBOE (VIX) → ~A FRED mirror |
| Currency | 5 | 0 | 5 | Bloomberg/Reuters/ICE → ~E |

**Total BLS-GAP: 69/79 (87.3%)** — BLS is a **narrow-coverage source** for this macro page; concentrated value in headline labor (5 of 9 Labor Market indicators are BLS-direct) + headline prices (3 of 8 Inflation indicators are BLS-direct, with the other 5 being BEA-PCE-class or UMich-survey-class).

**Recount confirmation:** Labor Market = 9 yang indicators (UNRATE + ICSA + CCSA + JTSJOL + PAYEMS + ADP + CIVPART + Hours + Earnings); BLS-MATCH for 6 of 9 (UNRATE + JTSJOL + PAYEMS + CIVPART + Hours + Earnings = 6 distinct yang labels); BLS-GAP for 3 of 9 (ICSA, CCSA, ADP). Inflation = 8 yang indicators; BLS-MATCH for 4 of 8 (CPI + Core CPI + PPI + ULC); BLS-GAP for 4 of 8 (PCE, Core PCE, UMich 1Y, UMich 5-10Y). 6 + 4 = 10 BLS-MATCH total. ✓ consistent with §2.1 count.

### §2.3 — BLS-adjacent candidates (out-of-79 but Wave-2-relevant)

For Wave-2 macro-adjacent pages that may consume additional macro indicators, the BLS surface ALSO covers:

- **Employment Cost Index (ECI)** — `CIU1010000000000A` (Total Compensation Civilian Workers % change annual) live-verified value `3.4` ~21:?Z. CI/EC surveys. Quarterly cadence. Wave-2 relevance: compensation pressure tracking (alternative to BLS Hourly Earnings monthly).
- **Productivity (Labor + Total Factor)** — `PRS85006092` (Labor Productivity NF Business % change) + MP-survey TFP series. PR + MP surveys. Quarterly cadence. Wave-2 relevance: productivity-cycle macro signal.
- **Import/Export Price Indexes** — `EIUIR` (Import Prices All Commodities) `147.6` + `EIUIQ` (Export Prices) `166.1` live-verified ~21:?Z. EI survey. Monthly cadence. Wave-2 relevance: trade-flow inflation pass-through.
- **Chained CPI** — `SUUR0000SA0` (Chained CPI All Items) `184.499` live-verified. SU survey. Alternative inflation index used by SSA + IRS bracket-indexation; methodology-variant from headline CPI.
- **Manufacturing Payrolls** — `CES0600000001` (Manufacturing Employment level) `21523` live-verified. CE survey supersector "06". Wave-2 relevance: sector-decomposition of NFP.

---

## §3 — Cadence per BLS Series

BLS inherits cadence from each survey's release calendar; BLS publishes data directly (no mirror lag — BLS IS the upstream).

| Cadence class | Count (of 10 BLS-MATCH) | Indicator examples | BLS release timing |
|---|:-:|---|---|
| **Monthly (M+1; ~1st Friday)** | 5 | UNRATE, PAYEMS, LFPR, Weekly Hours, Hourly Earnings | Joint CES + LN release; ~1st Friday post month |
| **Monthly (M+1; ~10th-15th)** | 3 | CPI, Core CPI, PPI | CU + WP releases; ~10th-15th post month |
| **Monthly (M+2; ~1st Tuesday)** | 1 | JOLTS Job Openings | JT release; 1-month-lag vs other labor (4 weeks post month) |
| **Quarterly (Q+1; ~6 weeks post quarter)** | 1 | Unit Labor Cost YoY | PR release; advance + preliminary + final revisions |

**AC-CADENCE-TOLERANCE (PRD §5):** Yang's monthly-snapshot cadence is structurally well-aligned with BLS's monthly cadence (9 of 10 BLS-MATCH). The single quarterly indicator (Unit Labor Cost) updates 4× annually with ~6-week lag; harness should sub-sample at quarter-end OR carry-forward last-published value between quarters. No cadence mismatch class fires for BLS-MATCH coverage. Sister to ~A FRED §3 + ~C Census §3.1 disposition.

**Revision pattern:** BLS uses footnote-level revision flags richer than FRED's `realtime_start`/`realtime_end` vintage encoding. Per `footnotes[]` per-observation:
- `P` (preliminary) — initial release subject to revision
- `R` (revised) — superseded a prior preliminary value
- Numeric codes (e.g., `12`) — survey-specific revision-class (CPS population-control revisions, CES benchmark revisions, etc.)

**Annual benchmark revisions:** CES (Employment, Hours, Earnings) receives annual benchmark revision at February release (covering March prior-year through current data); CPS (Labor Force) receives population-control updates annually at January release. Pre-benchmark vs post-benchmark values may differ by 0.5-2%. RE-REPRESENTATIVE class applies if Yang's snapshot date crosses a benchmark boundary. Sister to ~C §6 Census annual-benchmark pattern.

---

## §4 — RE Harness Sketch

### §4.1 — BLSAdapter v2 POST primitive (live-verified working primitive)

```python
from __future__ import annotations
import os
import requests
import boto3


class BLSAdapter:
    """v2 POST primitive — live-verified working 2026-05-26 ~21:?Z anonymous tier.

    Anonymous tier limits: 25 series/query, 10y history, 25 queries/day.
    Registered tier limits: 50 series/query, 20y history, 500 queries/day, calculations enabled.

    Future v2-registered swap-in: pass `registration_key` from AWS Secrets `BlsApiKey`
    (NOT yet provisioned at brief authoring; recommend onboarding per ~A FredApiKey precedent).
    """

    BASE = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

    def __init__(self, registration_key: str | None = None):
        # Sourcing per AWS-Secrets-BlsApiKey (PENDING ops provisioning)
        if registration_key is None:
            try:
                secrets = boto3.client("secretsmanager")
                registration_key = secrets.get_secret_value(SecretId="BlsApiKey")["SecretString"]
            except Exception:
                # Anonymous-tier fallback (acceptable for development/reconnaissance)
                registration_key = None
        self.registration_key = registration_key
        self.session = requests.Session()

    def get_observations(
        self,
        series_ids: list[str],
        start_year: str,
        end_year: str,
        calculations: bool = False,
        annual_average: bool = False,
    ) -> dict[str, list[dict]]:
        """v2 POST — pull observations for up to 50 series in a single request.

        Returns {series_id: [{year, period, periodName, value, footnotes}, ...]}.
        Parse float client-side from `value` STRING; "-" = missing.
        """
        payload: dict = {
            "seriesid": series_ids,
            "startyear": start_year,
            "endyear": end_year,
        }
        if self.registration_key:
            payload["registrationkey"] = self.registration_key
        if calculations:
            payload["calculations"] = True
        if annual_average:
            payload["annualaverage"] = True

        r = self.session.post(self.BASE, json=payload, timeout=30)
        r.raise_for_status()
        body = r.json()

        # Partial-success defensive check — status:REQUEST_SUCCEEDED does NOT guarantee per-series success
        if body.get("status") != "REQUEST_SUCCEEDED":
            raise RuntimeError(f"BLS request failed: status={body.get('status')} msg={body.get('message')}")

        # Per-series invalid-id warnings are in top-level message[] AND surfaced as EMPTY data[]
        warnings = body.get("message", [])

        result: dict[str, list[dict]] = {}
        for series in body["Results"]["series"]:
            sid = series["seriesID"]
            data = series.get("data", [])
            if not data:
                # Invalid series id — log and skip (caller can detect missing key)
                continue
            result[sid] = data
        return result, warnings

    def list_surveys(self) -> list[dict]:
        """LD-31 catalog ground-truth probe — call before committing series_id mappings."""
        r = self.session.get(
            "https://api.bls.gov/publicAPI/v2/surveys",
            timeout=30,
        )
        r.raise_for_status()
        return r.json()["Results"]["survey"]
```

### §4.2 — Per-indicator harness pull plan (10 BLS-MATCH active)

```python
# Concrete series-ID registry — bake into harness module as constants
YALP_MACROS_BLS_SERIES = {
    # Inflation (4 BLS-MATCH; PCE/UMich are GAP)
    "Inflation/CPI MoM":             ("CUUR0000SA0",     "CU"),  # MATCH-DERIVED (level; MoM derive)
    "Inflation/Core CPI MoM":        ("CUUR0000SA0L1E",  "CU"),  # MATCH-DERIVED
    "Inflation/PPI MoM":             ("WPSFD4",          "WP"),  # MATCH-DERIVED (modern Final Demand). Legacy alt: WPU00000000
    "Inflation/Unit Labor Cost YoY": ("PRS85006112",     "PR"),  # MATCH (BLS publishes %chg directly)

    # Labor Market (6 BLS-MATCH; ICSA/CCSA/ADP are GAP)
    "Labor Market/Unemployment Rate":              ("LNS14000000",                "LN"),  # MATCH
    "Labor Market/US Job Openings":                ("JTS000000000000000JOL",      "JT"),  # MATCH
    "Labor Market/Nonfarm Payrolls":               ("CES0000000001",              "CE"),  # MATCH-DERIVED (level; MoM derive)
    "Labor Market/Labor Force Participation Rate": ("LNS11300000",                "LN"),  # MATCH
    "Labor Market/Weekly Hours":                   ("CES0500000002",              "CE"),  # MATCH
    "Labor Market/Hourly Earnings MoM":            ("CES0500000003",              "CE"),  # MATCH-DERIVED
}

# YALP_MACROS_BLS_GAP = [
#   69 indicators — see §2.2 for sister-lane primary attribution
# ]
```

**~10 active series × monthly refresh = ~1 batched API call per refresh** (single POST with all 10 series in `seriesid[]`; under 25-series anonymous-tier cap; under 50-series registered cap). Trivial under either rate-limit tier (1 query of 25/500 daily quota).

### §4.3 — Failure modes + retry

- **Invalid series ID:** EMPTY `data[]` for that series + warning in top-level `message[]`. Harness MUST validate all 10 series IDs at startup via batch probe — fail-fast if any series_id has been discontinued by BLS (e.g., legacy WPU vs modern WPSFD class-rename precedent).
- **Missing observations:** `value: "-"` (per BLS docs; NOT empirically probed — anonymous probes returned dense data). Parse `value` as float OR detect `"-"` and treat as NaN. Sister to FRED `"."` quirk.
- **Quota-exceeded (HTTP 200 + `status:REQUEST_NOT_PROCESSED`):** standard exponential backoff + daily-quota-aware throttle. Anonymous tier (25/day) is fragile; recommend v2-registered (500/day) for production.
- **Partial-success check is structural requirement:** harness MUST verify both top-level `status` AND per-series `len(data[])`. Top-level-only check will silently swallow invalid series.
- **No session/cookie auth:** clean operational risk profile per §1.5.

### §4.4 — Cross-source consistency check (RE harness value-add)

For all 10 BLS-MATCH indicators, harness produces 3-way cross-validation:

**3-way (all 10 BLS-MATCH):**
1. BLS-direct (this lane upstream)
2. FRED-mirror (~A lane)
3. Yang-side Bloomberg `data.pkl` (the comparison target — what yang stores)

Verdict-taxonomy per [[feedback_corroborate_with_concern_verdict_shape]] 4-shape model adapted to RE-class (mirror sister lane ~A §4.4):
- **RE-MATCH** if all 3 sources agree within tolerance (±0.1% for rates; ±0.5% for index levels; same-month-anchor)
- **RE-REPRESENTATIVE** if 2-of-3 agree (typical lag-class — pre-revision vs post-revision; CES preliminary `P` flag still in flight)
- **RE-DRIFT** if all 3 disagree (rare; flag for investigation — likely yang-specific transformation OR Bloomberg index-rebasing)
- **RE-GAP** if BLS is GAP-class for the indicator (69/79; sister-lane primary per §5)

**Footnote-level revision-flag verification:** for BLS-direct vs FRED-mirror comparisons, BLS surfaces `footnotes[].code` (P=preliminary, R=revised) richer than FRED. RE harness can detect revision-class drift PRE-yang-snapshot — sister-lane finding for Phase 2b TO-008 verification design.

---

## §5 — Coverage % + Sister-Lane Handoffs

### §5.1 — Coverage summary (recap §2)

- **BLS-MATCH: 10/79 = 12.7%** (concentrated in headline Inflation + Labor)
- **BLS-GAP: 69/79 = 87.3%** (routes to sister lanes ~A FRED-PRIMARY, ~C Census-overlap, ~D Treasury/Fed-PRIMARY, ~E aggregate-orphan)

### §5.2 — Sister-lane handoff matrix

| Sister lane | Source | Overlap with ~B BLS | Disposition |
|---|---|---|---|
| **~A FRED** (TO-006a shipped `c50c59399`) | FRED API (St. Louis Fed) | **FULL overlap** — FRED mirrors ALL 10 BLS-MATCH indicators. FRED is downstream-publication-lag-bound (<24h); BLS is upstream-authoritative. Per ~A §5.2: "12 indicators are BLS-mirrored in FRED — FRED-PRIMARY runtime; ~B BLS for cross-validation + same-day-freshness if needed." | **FRED-PRIMARY runtime; BLS-CROSS-CHECK for footnote-level revision flags + same-day-publication freshness.** |
| **~C Census** (TO-006c shipped `ba147dbc5`) | Census EITS | **ZERO overlap** — Census + BLS are disjoint primary publishers for the 79-universe (Census = goods/trade/housing; BLS = labor/prices). Joint CPS program is BLS-published. Per ~C §5.2 explicit. | (no cross-lane action) |
| **~D Treasury/FDIC** (TO-006d shipped `e48480c5e`) | Treasury Direct + FRB DDP + BEA + NY Fed Markets | **ZERO overlap** — ~D covers Treasury Yields + FRB releases + BEA NIPA; BLS covers Labor + Prices. Disjoint. | (no cross-lane action) |
| **~E Aggregate-orphan** (TO-006e in flight) | Conference Board, ISM, S&P Global, NFIB, AAII, UMich, ADP, DoL ETA, NAHB, NAR, Wards, etc. | **ZERO overlap of BLS-MATCH; HIGH overlap of BLS-GAP** — ~E carries 3 of the 9 Labor Market indicators that BLS GAPs (ICSA, CCSA, ADP via DoL ETA / ADP-private adapter sets) + 2 of 8 Inflation (UMich 1Y + 5-10Y). | **~E primary for the 5 BLS-GAP labor/inflation indicators** (Jobless Claims × 2 via DoL ETA; ADP via ADP-private; UMich × 2 via UMich survey). |

### §5.3 — Recommendation for TO-007 synthesis (~A primary co-author with this brief)

**Two-tier harness architecture (consolidated with ~A FRED §5.3 recommendation):**

- **PRIMARY runtime tier:** ~A FRED — broadest single-source mirror (49 of 79 = 62% MATCH + 5 REPRESENTATIVE + 1 DERIVED = 69.6% effective coverage). Single adapter + single api_key + single rate-limit model. Most ops-simple harness layer.
- **CROSS-CHECK tier:** ~B BLS-direct for the 10 BLS-MATCH indicators — same-day-publication freshness + footnote-level revision flags (P=preliminary, R=revised) richer than FRED's `realtime_start`/`realtime_end` vintage encoding.
- **GAP routing:** ~E aggregate-orphan primary for 24 FRED-GAP indicators (per ~A §5.2); ~B is structurally absent here (BLS-GAP for these indicators).

**Rationale for FRED-PRIMARY + BLS-CROSS-CHECK over BLS-PRIMARY for the 10 overlap indicators:**

1. **Operational simplicity per ~A §5.3 rationale point 1**: FRED 1-adapter vs per-publisher adapter set; BLS-direct adds a second adapter for only 10 of 79 indicators.
2. **Publication-lag is acceptable per ~A §5.3 point 2**: FRED mirrors BLS with <24h lag; yang's monthly snapshot cadence absorbs sub-day lag.
3. **BLS-direct unique value = revision-flag granularity** (P/R footnotes per-observation) NOT raw-value-freshness. Use BLS for DRIFT arbitration + revision-aware harness logic, not for everyday pull.
4. **BLS anonymous tier 25-query-daily cap is fragile**; full 79-indicator nightly refresh fits inside but offers no headroom. v2-registered (500/day) production-ready but adds `BlsApiKey` ops onboarding step. FRED ops-profile (single api_key already in AWS Secrets per ~A) is operationally simpler.

**Phase 2b TO-007 verdict-taxonomy alignment:** RE-MATCH / RE-REPRESENTATIVE / RE-GAP / RE-DRIFT (per TO-006a `<cross_domain_coordination>` v0.3-substance-now-Phase-2-canonical) materializes cleanly for the 10 BLS-MATCH overlap. UNRATE + LFPR are most-likely RE-MATCH class (3-way agree: BLS upstream + FRED mirror + Bloomberg consume same monthly snapshot); PAYEMS is most-likely RE-REPRESENTATIVE (preliminary vs revised vintage selection between BLS publication date vs yang-snapshot date); 69 BLS-GAP = RE-GAP class by definition.

**4-of-5 lane convergence on FRED-PRIMARY runtime + sister-lane CROSS-CHECK** confirmed (per ~A §5.3): ~A endorses FRED-PRIMARY + sister-CROSS-CHECK; ~B (this brief) endorses BLS as CROSS-CHECK tier for 10 indicators; ~C explicitly endorses FRED-PRIMARY + Census-SECONDARY for 10 overlap; ~D explicitly endorses FRED-PRIMARY + ~D-CROSS-CHECK for 18-20 federal-source indicators (per ~A §5.2). All 4 shipped Phase 2a lanes converge.

---

## §6 — BLS-Specific Quirks

1. **Partial-success failure mode**: `status:REQUEST_SUCCEEDED` does NOT guarantee per-series success. Invalid series IDs return EMPTY `data[]` + warning text in top-level `message[]`. Harness MUST inspect both. Sister to Census `Missing-Key-HTML-200` (~C §6 row 1) and FRED `400 + error_message JSON` (~A §1.5) — different mechanisms; same "look beyond top-level status" pattern. Live-verified: `{"seriesid":["ICSA","CCSA"]}` returned `status:REQUEST_SUCCEEDED` + 2 invalid-series warnings + 2 EMPTY data arrays.

2. **Seasonal-adjustment encoded in series_id 3rd character**: `LN_S_14000000` (Seasonally Adjusted) vs `LN_U_14000000` (Unadjusted) — same data structure, different series_id. Yang almost certainly consumes SA-prefix variants (Bloomberg's macro page = monthly SA). Sister to ~C Census `seasonally_adj=yes/no` query param (~C §1.3) and FRED series-id-bound SA-vs-NSA choice (~A §1) — three different SA-encoding mechanisms across 3 federal-source APIs.

3. **PPI modern-vs-legacy class-distinction**: `WPSFD4` (PPI Final Demand, 2009-rebased modern headline) vs `WPU00000000` (PPI All Commodities, 1947-present legacy continuity). Yang's `PPIACO` Bloomberg label + FRED-mirror map to legacy `WPU00000000`; press coverage of "PPI" headline number maps to modern `WPSFD4`. **Phase 2b TO-007 architectural-class finding**: harness should surface yang-label-vs-publisher-class mismatch + Andrew decision on which BLS variant is authoritative (related to yang-internal-vs-publisher class per ~A §8 candidate #5).

4. **Footnote-level revision flags richer than FRED**: `data[].footnotes[]` array carries `P` (preliminary), `R` (revised), and survey-specific numeric codes (e.g., `12` for CPS population-control revisions, `5` for CES seasonal-adjustment-method updates). FRED's vintage encoding (`realtime_start`/`realtime_end` per-observation) is structurally equivalent but harder to surface in harness UI. **RE harness value-add**: per-observation revision-class flagging enables PRE-yang-snapshot drift detection (e.g., preliminary `P` value gets revised between BLS publication and yang-snapshot date).

5. **Jobless Claims (ICSA + CCSA) are NOT BLS — they are DoL ETA**: Department of Labor Employment & Training Administration publishes weekly Unemployment Insurance claims data via `https://oui.doleta.gov/`. FRED mirrors as ICSA/CCSA from DoL upstream, NOT BLS. Yang's "Initial/Continuing Jobless Claims" indicators route via ~A FRED-mirror OR ~E DoL-ETA-direct adapter. Live-empirically-confirmed: `"Invalid Series for Series ICSA"` + `"Series does not exist for Series CCSA"` returned from BLS v2 probe ~21:?Z.

6. **CES series_id structure follows CES + supersector(2) + industry(6) + datatype(2) convention**: e.g., `CES0000000001` = supersector "00" (Total Nonfarm) + industry "000000" + datatype "01" (All Employees thousands). `CES0500000003` = supersector "05" (Total Private) + industry "000000" + datatype "03" (Average Hourly Earnings). Datatype "02" = Avg Weekly Hours All Employees; datatype "08" = Avg Weekly Earnings. Yang likely consumes datatype "03" headline labels for Hourly Earnings MoM. Industry-level decomposition (e.g., Manufacturing `CES0600000001`) available for Wave-2 deepening but not in 79-universe.

7. **JOLTS series_id structure follows JTS + seasonal(1) + industry(6) + region(2) + sizeclass(2) + dataelement(3) convention**: e.g., `JTS000000000000000JOL` = seasonal "0" + industry "000000" (all industries) + region "00" + sizeclass "00" + dataelement "JOL" (Job Openings Level thousands). Dataelements: `JOL` (Openings), `HIL` (Hires), `TSL` (Total Separations), `QUL` (Quits), `LDL` (Layoffs), `OTL` (Other Separations). 1-month-cadence-lag vs other Labor (M+2 release vs M+1 for CES/CPS) is the JOLTS-survey-specific quirk.

8. **CU series for CPI uses `CUUR` (NSA U-rban consumers) prefix**: e.g., `CUUR0000SA0` = "CU + UR (Urban) + 0000 (all areas) + SA0 (all items, seasonally-adjusted-class)". The `SA0` suffix is misleading — it does NOT mean Seasonally-Adjusted; it means "All Items" group code. Seasonal adjustment in CPI series is encoded via `CUSR` prefix vs `CUUR` prefix (S vs U at 3rd-char). Yang's `CPIAUCSL` FRED-mirror likely uses NSA `CUUR0000SA0` per FRED's mapping convention. Per Phase 2b TO-008 verification: confirm yang-side SA-vs-NSA selection matches.

9. **v1 vs v2 endpoint differences**: v1 = GET single-series, anonymous-only, JSON response. v2 = POST batch (1-50 series), optional registration key, JSON request body, JSON response. Same response shape across both versions. **v2 POST with `Content-Type: application/json` is REQUIRED** — v2 with `application/x-www-form-urlencoded` returns `status:REQUEST_NOT_PROCESSED`. Sister to FRED v1-key-vs-v2-OAuth class-distinction (~A §1.3 + §6 row 4) — different transition class (BLS v1→v2 is anonymous-tier-or-registered-tier, no auth-class break; FRED v1→v2 is OAuth-class break).

10. **Period encoding M01-M12 + M13 (annual average) + Q01-Q05 (Q05 = annual)**: monthly series carry `period:"M01"` through `M12` with optional `M13` (Q5-style annual average row) when `annualaverage:true` flag set; quarterly series use `Q01`-`Q04` + `Q05`. Harness must filter `period` carefully — naive sort-by-`period` will mix M13 annual rows with M12 December rows.

11. **No session/cookie auth model**: stable api_key (registered tier) or fully anonymous (rate-capped tier); no session-eviction class. Sister to ~A FRED + ~C Census + ~D Treasury Direct + ~D NY Fed Markets clean-ops profile. Compare YCharts 403-session-eviction class per [[feedback_ycharts_http_400_is_cookie_stale_class]] — BLS operational risk profile is fundamentally cleaner than any session-bound API.

12. **BlsApiKey AWS Secrets onboarding pending**: secret not yet provisioned (live-verified ~21:?Z `aws secretsmanager describe-secret --secret-id BlsApiKey` → `ResourceNotFoundException`). Production harness build phase (Phase 2b TO-008) should bundle key signup + Secrets provisioning + Lambda IAM grant per ~A `FredApiKey` precedent. Reconnaissance brief authored against anonymous tier (sufficient for 12 probe queries; would NOT support sustained nightly refresh against 25/day cap).

---

## §7 — RAVC2-Request

**To:** 2.0.0_SA_COO
**From:** 0.1.0_DS_MarketIntelligence~B
**TO:** YALP_MACROS.006b — BLS multi-source RE reconnaissance (Phase 2a lane B)

**Evidence:**
- This brief at `docs/briefs/yalp_macros_phase2a_bls_reconnaissance_2026-05-26.md`
- §1 BLS API surface — base URL + auth model + v2 POST primitive LIVE-VERIFIED (~21:?Z anonymous tier) + v1 GET fallback documented + 4 additional v2 endpoints catalogued + tier-cap table + failure-mode taxonomy + LIVE-VERIFIED BLS surveys catalog (73 surveys enumerated; relevant subset mapped to 79-indicator universe per LD-31 ground-truth discipline)
- §2 Per-indicator match-set — 79/79 indicators classified across 12 groups; **10 BLS-MATCH + 0 BLS-REPRESENTATIVE + 69 BLS-GAP**; per-group coverage summary in §2.2 (5 of 9 Labor Market + 4 of 8 Inflation = 9 of 17 group-overlap rows; 0% for other 10 groups)
- §3 Cadence per BLS series — 4 cadence classes (monthly-M+1-1st-Friday / monthly-M+1-mid-month / monthly-M+2-1st-Tuesday / quarterly-Q+1-six-weeks); revision-flag pattern + annual benchmark pattern documented
- §4 RE harness sketch — BLSAdapter v2 POST adapter class (Python) + per-indicator series-ID registry (10 active) + future v2-registered swap-in scaffold + failure-mode + retry + 3-way cross-source consistency-check pattern for Phase 2b TO-007 verdict-taxonomy
- §5 Coverage % + sister-lane handoff matrix — **12.7% BLS-coverage** (narrow-but-deep upstream-authoritative for headline labor + prices) + ~A FRED-mirror full-overlap (FRED-PRIMARY runtime + BLS-CROSS-CHECK tier disposition) + ~C/~D zero-overlap + ~E primary for 5 BLS-GAP labor/inflation indicators; 4-of-5 lanes converge on FRED-PRIMARY runtime architectural lean
- §6 12 BLS-specific quirks — partial-success-failure-mode + SA-encoded-in-series-id-3rd-char + PPI-modern-vs-legacy + footnote-revision-flags-richer-than-FRED + ICSA/CCSA-not-BLS-but-DoL-ETA + CES-series-id-structure + JOLTS-series-id-structure + CU-CUUR-SA0-misleading + v1-vs-v2-endpoint-differences + period-M01-M13-Q01-Q05 + clean-ops-profile + BlsApiKey-AWS-Secrets-onboarding-pending

**Acceptance criteria (5/5 met) — mirroring YALP_MACROS.006a AC1-AC5 per TO:**
- **AC1** — BLS API surface enumerated (base + key APIs documented): ✅ §1 + LIVE-VERIFIED ~21:?Z (3-batch series probe + surveys catalog enumeration)
- **AC2** — Per-indicator match-set populated for all 79 yang macro indicators (BLS series ID OR `n/a` reason): ✅ §2.1-§2.2 (79/79; explicit class label per row; §2.2 best-source attribution for 69 BLS-GAP); §2.3 Wave-2-adjacent candidates
- **AC3** — Cadence per BLS series documented: ✅ §3 (4-class taxonomy + revision-flag pattern + annual benchmark pattern)
- **AC4** — RE harness sketch documented for TO-008 follow-on (NOT implementation; design-level): ✅ §4 (BLSAdapter class + series-ID registry + failure modes + cross-source pattern)
- **AC5** — Coverage % + sister-lane handoffs documented: ✅ §5 (12.7% BLS-coverage + handoff matrix + 4-of-5 lane convergence on FRED-PRIMARY runtime + BLS-CROSS-CHECK disposition)

**Disposition recommendation:** ACCEPT.

**No production touches.** Reconnaissance class; documentation-only commit. Read-only verification scope per PRD v0.5 §4 + Andrew per-page charter framing. Sister to ~A FRED + ~C Census + ~D Treasury/FDIC briefs' read-only-verification scope.

---

## §8 — Memory candidates banked

Candidates surfaced through this reconnaissance for future memory-write disposition (CTO/MSTR ratification; non-blocking):

1. **`bls-partial-success-failure-mode-requires-per-series-data-length-check`** — `status:REQUEST_SUCCEEDED` does NOT guarantee per-series validity; invalid IDs return EMPTY `data[]` + top-level `message[]` warning. Sister to ~C Census `Missing-Key-HTML-200` + ~A FRED `400 + error_message JSON` — three federal-source APIs with three different "look beyond top-level status" patterns. **CANDIDATE: extend "API status check is structurally insufficient" memory class with BLS-specific partial-success example.**

2. **`bls-vs-doleta-vs-adp-jobless-claims-class-attribution`** — Yang's "Initial/Continuing Jobless Claims" + "ADP Employment Change" are NOT BLS even though they are Labor Market group indicators. Jobless Claims = DoL ETA (Department of Labor Employment & Training Administration); ADP = ADP-private (Automatic Data Processing payroll-processor data). Reconnaissance findings often attribute Labor indicators to BLS by default — empirical class-attribution requires live-probe per [[feedback_api_catalog_live_verify_before_committing_ids]]. **CANDIDATE: extend LD-31 with Labor-Market-publisher-attribution worked example.**

3. **`bls-footnote-revision-flags-richer-than-fred-vintage`** — BLS `footnotes[]` per-observation array carries P/R/numeric-code revision-class flags structurally richer than FRED's `realtime_start`/`realtime_end` vintage encoding. For drift-detection harness use cases, BLS-direct surfaces revision class PRE-yang-snapshot; FRED-vintage requires explicit revision-history pull. **CANDIDATE: when designing revision-aware harness for mirror-vs-origin source pairs, prefer origin-source for revision-class signal even if mirror is operational PRIMARY.** Sister to ~A §8 candidate #3 mirror-vs-origin discipline.

4. **`bls-seasonal-adjustment-encoded-in-series-id-third-character`** — `LN_S_14000000` (SA) vs `LN_U_14000000` (NSA); `CU_S_R0000SA0` (CPI SA) vs `CU_U_R0000SA0` (CPI NSA). Three federal-source APIs encode SA differently: BLS = series_id 3rd char; Census = `seasonally_adj=yes/no` query param; FRED = series-id-bound (one or the other per series id). **CANDIDATE: federal-source SA-encoding-class taxonomy memory** — useful when designing multi-source harness that must consistently consume SA across sources.

5. **`bls-ppi-modern-wpsfd-vs-legacy-wpu-class-distinction`** — `WPSFD4` (PPI Final Demand 2009-rebased modern) vs `WPU00000000` (PPI All Commodities 1947-present legacy continuity). Yang `PPIACO` Bloomberg label maps to legacy; press coverage maps to modern. Sister to ~A §8 candidate #5 yang-internal-vs-publisher-published class. **CANDIDATE: surface as Phase 2b TO-007 architectural-class finding for Andrew disposition** — deprecate legacy / substitute modern / dual-publish.

Banking deferred to MSTR /govern + Andrew sovereign ratification per LD-0025 ALWAYS-PROCEED + Article XVI.

---

## §9 — Standing posture

Brief shipped. Phase 2a Wave-1 now 4-of-5 shipped (~A FRED + ~B BLS this brief + ~C Census + ~D Treasury/FDIC); ~E Aggregate-orphan in flight per ws COO /allocation #110 dispatch path. Phase 2b TO-007 synthesis (co-author with ~A primary) gates on:
- ~E Aggregate-orphan brief ship (in flight per ws COO message; SPAWN-NEEDED status at ws COO /allocation cycle 110)
- (Phase 2a Wave-1 5-of-5 ship)

Standing /work 20m loop for sister-lane convergence MCPs OR Phase 2b TO-007 GO dispatch from ws COO.

— 0.1.0_DS_MarketIntelligence~B
2026-05-26 work-cycle:1 (Phase 2a YALP_MACROS.006b)
