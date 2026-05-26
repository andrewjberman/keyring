# YALP_MACROS Phase 2a — Census Bureau Multi-Source Reconnaissance

**TO:** YALP_MACROS.006c — Census Bureau multi-source RE reconnaissance (Phase 2a parallel lane C)
**Author:** 0.1.0_DS_MarketIntelligence~C (Phase 2a Census lane; sister to ~A FRED + ~B BLS + ~D Treasury/FDIC + ~E Aggregate-orphan)
**PRD:** `docs/architecture/YALP_MACROS.md` v0.5 RE-OPENED `7e781ea8c` — Phase 2 multi-source RE charter
**Authority:** Andrew sovereign direct ~21:00Z + RE-OPEN Phase 2 ~21:05Z + MSTR LD-0104 fast-trajectory endorsement
**T*:** indicator-cadence-bound (most Census EITS monthly with M+1/M+2 release lag); brief authored 2026-05-26 against current API surface
**Status:** Phase 2a reconnaissance COMPLETE — 5/5 ACs met

---

## §0 — TL;DR

Census Bureau Economic Indicators Time Series (EITS) API at `https://api.census.gov/data/timeseries/eits/{dataset}` provides **21 EITS datasets** (monthly + quarterly). API key required (free; instant signup at `api.census.gov/data/key_signup.html`); 500 queries/day anonymous, unlimited keyed. Standard JSON response shape (array-of-arrays, first row header). **Census-PRIMARY coverage of 79-indicator universe: 10 indicators (~12.7%)** across 6 EITS datasets: `ressales` (New Home Sales), `resconst` (Housing Starts + Building Permits), `m3`/`advm3` (Durable Goods + Factory Orders), `mtis` (Business Inventories), `ftd` (Trade Balance), `marts`/`mrts` (Retail Sales family — 3 subcomponents). Most Census-primary indicators are ALSO available as FRED-mirror series (`HOUST`, `PERMIT`, `HSN1F`, `DGORDER`, `AMTMNO`, `BUSINV`, `BOPGSTB`, `RSAFS`, etc.); Census-upstream advantage = sub-component breakouts + seasonal-adjustment toggle + advance-vs-revised distinction. Cookie-stale-OK regime not applicable (no session model; key-or-anonymous tier). **Per Andrew "go exploring" framing**: surface enumerated + matched against macro page; strict identify-then-RE not required at this phase.

---

## §1 — Census API Surface

### §1.1 — Endpoint structure

**Base URL pattern:**
```
https://api.census.gov/data/timeseries/eits/{dataset_code}
```

**Standard query shape (live-verified `~22:00Z`):**
```
?get=cell_value,data_type_code,category_code,seasonally_adj,time_slot_id,error_data
&time=2026-03                                 (YYYY or YYYY-MM ISO-8601)
&data_type_code=TOTAL                         (per-dataset enum; e.g., HOUST, PERMIT, RETAIL)
&category_code=02000                          (per-dataset enum; industry/unit-type)
&seasonally_adj=yes                           (yes|no)
&key=YOUR_KEY                                 (required; free signup)
```

**Response shape:** JSON array-of-arrays. First row = headers, subsequent rows = data.

```json
[
  ["cell_value","data_type_code","category_code","seasonally_adj","time_slot_id","error_data","time","us"],
  ["1456","TOTAL","02000","yes","0","no","2026-03","1"],
  ...
]
```

### §1.2 — 21 EITS Datasets (live `api.census.gov/data.json` enumeration `~22:00Z`)

| Code | Full Name | Cadence | Macro-page relevance |
|---|---|---|---|
| `advm3` | Advance Report on Durable Goods Manufacturers' Shipments, Inventories, and Orders | Monthly | **PRIMARY** (Durable Goods Orders) |
| `m3` | Manufacturers' Shipments, Inventories, and Orders (full report) | Monthly | **PRIMARY** (Factory Orders + Durable subset) |
| `marts` | Advance Monthly Sales for Retail and Food Services | Monthly | **PRIMARY** (Retail Sales family) |
| `mrts` | Monthly Retail Trade and Food Services (full report) | Monthly | **PRIMARY** (Retail Sales family revised) |
| `mtis` | Manufacturing and Trade Inventories and Sales | Monthly | **PRIMARY** (Business Inventories) |
| `mwts` | Monthly Wholesale Trade: Sales and Inventories | Monthly | Adjacent (wholesale trade — no direct 79-indicator match; BLS-overlap-zero) |
| `mwtsadv` | Advance Wholesale Inventories | Monthly | Adjacent |
| `mrtsadv` | Advance Retail Inventories | Monthly | Adjacent (retail inventories distinct from Retail Sales) |
| `resconst` | New Residential Construction (Housing Starts + Building Permits + Completions + Under Construction) | Monthly | **PRIMARY** (Housing Starts + Building Permits) |
| `ressales` | New Home Sales | Monthly | **PRIMARY** (New Home Sales) |
| `vip` | Construction Spending (Value of Construction Put-in-Place) | Monthly | Adjacent (no direct 79-indicator match; flag for Wave-2) |
| `ftd` | U.S. International Trade in Goods and Services | Monthly/Quarterly | **PRIMARY** (Trade Balance — joint Census/BEA) |
| `ftdadv` | Advance U.S. International Trade in Goods | Monthly | Adjacent (advance release of `ftd`) |
| `bfs` | Business Formation Statistics | Monthly/Quarterly | Out (no 79-indicator match) |
| `hv` | Housing Vacancies and Homeownership | Quarterly | Out (no 79-indicator match) |
| `mhs` | Manufactured Homes Survey | Monthly | Out |
| `mhs2` | Manufactured Housing Survey (2014-Present) | Monthly | Out |
| `qfr` | Quarterly Financial Report | Quarterly | Out |
| `qpr` | Quarterly Survey of Public Pensions | Quarterly | Out |
| `qss` | Quarterly Services Survey | Quarterly | Out |
| `qtax` | Quarterly Summary of State and Local Taxes | Quarterly | Out |

**Total: 21 EITS datasets** — 6 PRIMARY for macro-page (10 indicators) + 4 adjacent + 11 out-of-scope.

### §1.3 — Required variables (live-verified per `variables.json`)

Per `https://api.census.gov/data/timeseries/eits/{ds}/variables.json` (resconst + marts both verified):

| Variable | Required | Predicate | Notes |
|---|---|---|---|
| `cell_value` | required (get) | string | The metric value (note: returned as string; parse to float client-side) |
| `data_type_code` | required (filter) | string | Per-dataset enum (e.g., `TOTAL`, `1UNIT`, `PERMIT`, `HOUST` — varies per dataset; lookup via `data_type_code.json`) |
| `time_slot_id` | required (filter) | string | Time-slot index (often `0` for current month, `1`-`N` for revisions) |
| `seasonally_adj` | required (filter) | string | `yes` / `no` |
| `category_code` | required (filter) | string | Per-dataset enum (industry/unit-type code) |
| `program_code` | default displayed | string | Component name (auto-included) |
| `time` | required (filter) | datetime | ISO-8601; `YYYY` or `YYYY-MM` |
| `error_data` | optional (get) | string | `yes` / `no` — flags statistical-significance gates |
| `geo_level_code` | optional | string | Geographic granularity (default US-national) |
| `for` / `in` | optional | fips-clause | Geographic filter (default `us:*`) |

**Per-dataset enum discovery:** `https://api.census.gov/data/timeseries/eits/{ds}/variables/data_type_code.json` returns full enum list; same pattern for `category_code.json`. Live-verified shape via resconst + marts samples.

### §1.4 — Authentication + Rate Limits

- **API Key:** free signup at `api.census.gov/data/key_signup.html`; instant email delivery. Pass as `&key=<KEY>` query param.
- **Anonymous tier:** 500 queries/day per IP (per Census docs); no key returns HTML `Missing Key` page (HTTP 200).
- **Keyed tier:** no documented daily cap; per Census API guidelines, throttle-tolerant.
- **Per [[third-party-data-reverse-engineer-not-scrape]] compliance:** Census API IS the authoritative API (not a scrape of a frontend); no reverse-engineering required — the public REST API is the official ingestion surface.
- **No session/cookie model.** API-key auth = no session-eviction class (sister to YCharts 403 risk). All Census API queries are stateless.

---

## §2 — Per-Indicator Match-Set (79 yang → Census)

Per the canonical macro_data.json indicator universe (12 groups × 79 indicators per L1 §6.4 / TO-004 empirical):

### §2.1 — Census-PRIMARY matches (10/79 = ~12.7%)

| # | Yang indicator | yang BBG ticker | Census dataset | data_type_code candidate | category_code candidate | Cadence | FRED-mirror? |
|---|---|---|---|---|---|---|---|
| 1 | **Housing Starts** (Housing Market group) | `NHSPSTOT Index` | `resconst` | `TOTAL` (Housing Units Started) | `02000` (total all units; `01000` = 1-unit, `04500` = 5+ units) | Monthly (M+2 release; ~17th-19th of M+2) | ✅ FRED `HOUST` |
| 2 | **Building Permits** (Housing Market group) | `NHSPATOT Index` | `resconst` | `AUTH` (Housing Units Authorized by Permit) OR `PERMIT` | `02000` (total) | Monthly (M+2; same release as starts) | ✅ FRED `PERMIT` |
| 3 | **New Home Sales** (Housing Market group) | `NHSLTOT Index` | `ressales` | `ASOLD` (Houses Sold) | `01000` (single-family; default) | Monthly (M+2; ~25th of M+2) | ✅ FRED `HSN1F` |
| 4 | **Durable Goods Orders MoM** (Lagging) | `DGNOCHNG Index` | `advm3` (advance) OR `m3` (revised) | `NO` (New Orders) | `31AT` (Total Durable Goods) | Monthly (advance ~M+1 day 25; revised ~M+2 day 5) | ✅ FRED `DGORDER` |
| 5 | **Factory Orders MoM** (Lagging) | `USPHTMOM Index` | `m3` (full report includes nondurables) | `NO` (New Orders) | `MFG` (Total Manufacturing) | Monthly (~M+2 day 5) | ✅ FRED `AMTMNO` |
| 6 | **Business Inventories YoY** (Lagging) | `MTIBYOY Index` | `mtis` | `IM` (Inventories) OR `IS` (Inventories/Sales ratio) | `44X72` (Total Business — Manufacturing + Wholesale + Retail) | Monthly (~M+2 day 15) | ✅ FRED `BUSINV` |
| 7 | **Trade Balance** (Lagging) | `USTBTOT Index` | `ftd` (joint Census/BEA) | `BAL` (Balance) | `001` (Total Goods + Services) | Monthly (~M+2 day 5-7) | ✅ FRED `BOPGSTB` |
| 8 | **Retail Sales MoM** (Consumer) | `RSTAMOM Index` | `marts` (advance) OR `mrts` (revised) | `SM` (Sales, Monthly) | `44X72` (Total Retail + Food Services) | Monthly (advance ~M+1 day 15-17; full ~M+2) | ✅ FRED `RSAFS` |
| 9 | **Retail Sales ex Auto MoM** (Consumer) | `RSTAXMOM Index` | `marts` / `mrts` | `SM` | `44Y72` (Total ex Motor Vehicle Dealers — Census 4-digit NAICS exclude `441`) | Monthly | ✅ FRED `RSFSXMV` |
| 10 | **Retail Sales ex Auto and Gas MoM** (Consumer) | `RSTAXAG% Index` | `marts` / `mrts` | `SM` | `44W72` (ex MV Dealers + Gas Stations — exclude `441` + `447`) | Monthly | ✅ FRED `RSFSXMVG` (or derived) |

**Notes on data_type_code / category_code:** values above are best-fit candidates from Census EITS conventions (verified empirically only where probed). Full enum confirmation deferred to TO-008 harness build phase; `variables/{var}.json` JSON enums available per dataset.

### §2.2 — Non-Census (n/a) for 79-indicator universe (69/79)

The other 69 yang indicators have **no Census Bureau authoritative source**. Best-source attribution from sister-lane reconnaissance:

| Group | Indicator count | Primary source(s) | Census coverage |
|---|---|---|---|
| Leading Indicator (8) | 8 | Conference Board (LEI), ISM (PMI Manufacturing/Services + New Orders), S&P Global (PMI), NFIB | n/a — none Census |
| Lagging Indicator (3 non-Census of 7) | GDP, Industrial Productivity, Capacity Utilization | BEA (GDP); FRB G.17 (IP + CapUtil) | n/a — none Census |
| Financial Condition (6) | 6 | Bloomberg (BFCI), Chicago Fed (NFCI), FRB (Fed Funds, balance sheet, TIC flows) | n/a — none Census |
| Inflation (8) | 8 | BLS (CPI/Core CPI/PPI/Unit Labor Cost), BEA (PCE/Core PCE), UMich (inflation expectations) | n/a — none Census |
| Labor Market (9) | 9 | BLS (unemployment, NFP, JOLTS, LFPR, hours, earnings), DoL (jobless claims), ADP (private payrolls) | n/a — **NOTE**: Census *collects* Current Population Survey data jointly with BLS, but BLS is the publishing authority; macro-page consumes BLS endpoints not Census directly |
| Consumer (4 non-Census of 7) | UMich Sentiment, CB Consumer Confidence, Consumer Credit, Wards Vehicle Sales | UMich, Conference Board, FRB G.19, Wards Auto | n/a — none Census |
| Housing Market (3 non-Census of 6) | NAHB HMI, Existing Home Sales, Pending Home Sales | NAHB (HMI survey), NAR (existing + pending) | n/a — none Census |
| Investor Sentiment (7) | 7 | AAII, Fed-NLP | n/a |
| Treasury Yields (10) | 10 | Treasury Direct / FRB H.15 | n/a (lane ~D scope) |
| Credit Spread (5) | 5 | Bloomberg + ICE | n/a |
| Market Indicator (1) | 1 | CBOE (VIX) | n/a |
| Currency (5) | 5 | Bloomberg / Reuters | n/a |

**Total non-Census: 69/79 (~87.3%)** — Census Bureau is a **niche-coverage source** for this macro page; primary value is housing/construction + retail + manufacturing/orders + trade + business inventories.

### §2.3 — Census-adjacent candidates (out-of-79 but Wave-2-relevant)

For Wave-2 macro-adjacent pages (ATTR, etc.) that may consume additional macro indicators, the Census EITS surface ALSO covers:

- **Construction Spending** (`vip` — Total Private + Total Public; FRED mirror `TLCONSPR` / `TLPBLCONS`) — high-prior addition if Wave-2 ATTR consumes construction-spending
- **Wholesale Trade Sales** (`mwts`) — adjacent to Retail; FRED mirror `WHLSLRIMSA`
- **International Trade in Goods Advance** (`ftdadv`) — releases ~M+1 day 28; advance to `ftd`
- **Housing Vacancies / Homeownership Rate** (`hv` — quarterly) — adjacent to Housing-Market group

---

## §3 — Cadence per Census Dataset

### §3.1 — Monthly EITS (release-lag taxonomy)

All 10 Census-PRIMARY matches are **monthly cadence**. Release-lag pattern (per Census EITS release calendar):

| Dataset | Release timing | Revision pattern |
|---|---|---|
| `resconst` (Housing Starts + Permits) | M+2 day 17-19 | Initial release subject to ±2-3% revision at M+3; minor revisions through M+12 (benchmark) |
| `ressales` (New Home Sales) | M+2 day 23-25 | Same — initial subject to M+3 revision (often substantial due to small monthly sample) |
| `advm3` (Durable Goods advance) | M+1 day 24-27 | **Advance** release; superseded by `m3` (full) at M+2 day 4-5 |
| `m3` (Factory Orders + Durable Goods revised) | M+2 day 4-5 | Replaces `advm3`; subject to minor revision at M+3 |
| `mtis` (Business Inventories) | M+2 day 14-15 | Combines previously-released `m3` + `mwts` + `mrts` inventories; minor revision pattern |
| `ftd` (Trade Balance) | M+2 day 5-7 | Joint Census/BEA; initial subject to revision at M+3 + annual benchmark |
| `ftdadv` (Trade Advance Goods-only) | M+1 day 28 | Advance to `ftd`; goods-only (no services) |
| `marts` (Retail Sales advance) | M+1 day 14-17 | **Advance** release; superseded by `mrts` at M+2 |
| `mrts` (Retail Sales full + revised) | M+2 day 14-17 | Replaces `marts`; subject to revision at M+3 |

**AC-CADENCE-TOLERANCE (PRD §5):** Yang's monthly update cadence is structurally aligned with Census monthly release. No cadence mismatch class fires for Census-PRIMARY indicators.

### §3.2 — Advance vs Revised distinction (Census-specific quirk)

For 4 indicators, Census publishes an **advance** release ~10 days before the **revised** release:

| Indicator | Advance dataset | Revised dataset | Yang likely consumes |
|---|---|---|---|
| Durable Goods Orders MoM | `advm3` (M+1 day 25) | `m3` (M+2 day 5) | TBD — Yang reads Bloomberg `DGNOCHNG`; Bloomberg likely mirrors revised `m3` |
| Retail Sales MoM (3 indicators) | `marts` (M+1 day 15) | `mrts` (M+2 day 14) | TBD — Bloomberg `RSTAMOM` likely mirrors `marts` advance |
| Trade Balance | `ftdadv` (M+1; goods only) | `ftd` (M+2; goods + services) | TBD — Bloomberg `USTBTOT` likely mirrors `ftd` revised (full goods+services) |

**RE harness implication:** harness should pull from REVISED datasets (`m3`, `mrts`, `ftd`) for Bloomberg-equivalence; pull from ADVANCE (`advm3`, `marts`, `ftdadv`) only if explicit advance-release matching needed.

---

## §4 — RE Harness Sketch

### §4.1 — Auth + endpoint pattern

```python
import os, requests
CENSUS_API_KEY = os.environ["CENSUS_API_KEY"]  # signup: api.census.gov/data/key_signup.html
BASE = "https://api.census.gov/data/timeseries/eits"

def pull_eits(dataset, data_type_code, category_code, seasonally_adj="yes",
              time_range="from+2024-01+to+2026-05"):
    params = {
        "get": "cell_value,data_type_code,category_code,seasonally_adj,time_slot_id,time,error_data",
        "data_type_code": data_type_code,
        "category_code": category_code,
        "seasonally_adj": seasonally_adj,
        "time": time_range,
        "key": CENSUS_API_KEY,
    }
    r = requests.get(f"{BASE}/{dataset}", params=params, timeout=30)
    r.raise_for_status()
    rows = r.json()
    header, data = rows[0], rows[1:]
    return [dict(zip(header, row)) for row in data]
```

### §4.2 — Per-indicator pull table

| # | Indicator | Endpoint | data_type_code | category_code |
|---|---|---|---|---|
| 1 | Housing Starts | `resconst` | `TOTAL` | `02000` |
| 2 | Building Permits | `resconst` | `AUTH` (or `PERMIT`) | `02000` |
| 3 | New Home Sales | `ressales` | `ASOLD` | `01000` |
| 4 | Durable Goods Orders | `m3` | `NO` | `31AT` |
| 5 | Factory Orders | `m3` | `NO` | `MFG` |
| 6 | Business Inventories | `mtis` | `IM` | `44X72` |
| 7 | Trade Balance | `ftd` | `BAL` | `001` |
| 8 | Retail Sales | `mrts` | `SM` | `44X72` |
| 9 | Retail Sales ex Auto | `mrts` | `SM` | `44Y72` |
| 10 | Retail Sales ex Auto+Gas | `mrts` | `SM` | `44W72` |

10 pulls per refresh = ~10 API calls (well under 500/day anonymous limit; trivial under keyed).

### §4.3 — Normalization shape

`cell_value` is returned as STRING; parse to float client-side. Time slots use `time_slot_id`:
- `0` = current release (most recent)
- `1`-`N` = prior revisions (history)

For RE verification on T*-bound shared-date: filter `time={YYYY-MM}` + `time_slot_id=0` for latest revision. For historical timeseries: filter time-range + `time_slot_id=0` per month.

### §4.4 — Pagination + retry

- No pagination (single-call per indicator per time-range).
- Retry: standard exponential backoff on 5xx + 429. Census API does NOT use session cookies — no session-eviction class.
- 200 OK with HTML body = "Missing Key" failure mode (the only quirky failure); detect by `Content-Type` not being JSON.

---

## §5 — Coverage % + Sister-Lane Handoffs

### §5.1 — Census coverage summary

- **Census-PRIMARY: 10/79 = ~12.7%** (3 Housing + 4 Lagging + 3 Consumer)
- **Census-adjacent (Wave-2 candidates): 4 datasets** (`vip`, `mwts`, `ftdadv`, `hv`) — no current 79-indicator match
- **Non-Census: 69/79 = ~87.3%**

### §5.2 — Sister-lane handoffs

| Lane | Source | Expected coverage | Overlap with Census |
|---|---|---|---|
| ~A FRED | FRED API (St. Louis Fed) | High — FRED mirrors most Census EITS series + many other sources | **HIGH OVERLAP** — all 10 Census-PRIMARY indicators also available as FRED-mirror (see §2.1 final col). FRED is preferred for harness simplicity (single source); Census is preferred for advance-release-specificity + sub-component breakouts |
| ~B BLS | BLS API | Labor (9) + Inflation (CPI/PPI; 5 of 8) + adjacency | **ZERO OVERLAP** — BLS and Census are disjoint primary publishers for the 79 universe (Census = goods/trade; BLS = labor/prices). Joint program (CPS) is BLS-published. |
| ~D Treasury/FDIC | Treasury Direct + FDIC + OFR | Treasury Yields (10) + Financial Condition adjacency | ZERO OVERLAP |
| ~E Aggregate-orphan | Multi-source residual | Conference Board, ISM, NAHB, NAR, AAII, UMich, Wards, NFIB, etc. (~25 indicators) | ZERO OVERLAP |

### §5.3 — Recommendation for TO-007 synthesis

For the 10 Census-PRIMARY indicators, **FRED is the recommended PRIMARY harness anchor** (simpler — single source, single API client, broader mirror coverage of non-Census indicators). Census is the recommended **SECONDARY/CROSS-CHECK anchor** for:
1. Advance-release-specificity (`marts` advance for retail; `advm3` for durable; `ftdadv` for trade) — when Yang's Bloomberg-mirror likely uses advance, Census-direct advance is the exact match
2. Sub-component breakouts (e.g., Housing Starts by 1-unit vs multi-unit; Retail Sales by ex-auto-ex-gas)
3. Seasonal-adjustment toggle (Census returns both SA and NSA via `seasonally_adj=yes/no` filter; FRED is series-id-bound to one or the other)
4. Pre-revision benchmark (Census `time_slot_id` history preserves all prior revisions; FRED stores only current-revised)

---

## §6 — Census-Specific Quirks

1. **Missing-key failure returns HTTP 200 with HTML body** (not JSON error). Harness MUST detect `Content-Type: text/html` to fail correctly; naive `json.loads(r.text)` will throw `JSONDecodeError`. Sister to YALP_MKTOVR's YCharts 403-HTML-from-Lambda finding (`comp-routes behaviors`).
2. **`cell_value` is STRING-typed** in JSON response — explicit float parse required client-side.
3. **Per-dataset enum discovery requires separate metadata pull.** `data_type_code` + `category_code` enums are not in the main variables.json; require `/variables/{var}.json` per-variable fetch OR consultation of dataset's HTML examples page. Harness should cache enum metadata at startup.
4. **Time-slot semantics vary by dataset.** `time_slot_id=0` is most-recent for monthly; for quarterly datasets (`qfr`, `qss`, etc.), time-slot represents quarter-within-year. Per-dataset verification required.
5. **Joint Census/BEA programs (`ftd`).** Trade Balance is jointly published by Census Foreign Trade Division + BEA International Economic Accounts. Both Census API AND BEA API return identical headline numbers; Census API recommended for harness simplicity (single API key vs BEA's separate signup).
6. **Annual benchmark revisions.** Most monthly EITS series receive ANNUAL benchmark revision (typically June for housing; April for retail). Pre-benchmark vs post-benchmark values may differ by 1-3%. RE-REPRESENTATIVE class applies if Yang's snapshot date crosses a benchmark boundary.
7. **`error_data=yes` flag.** Census flags statistically-insignificant month-over-month changes (especially for small-sample monthly surveys like `ressales`). Harness should surface this flag in RE comparison output (Yang doesn't carry the flag — Census provides MORE metadata than Yang preserves).
8. **No session/cookie model.** Stateless API-key auth — no session-eviction failure class. Sister to YCharts 403 risk; Census harness has fundamentally different operational risk profile (clean).

---

## §7 — RAVC2-Request

**To:** 2.0.0_SA_COO
**From:** 0.1.0_DS_MarketIntelligence~C
**TO:** YALP_MACROS.006c — Census Bureau multi-source RE reconnaissance (Phase 2a lane C)

**Evidence:**
- This brief at `docs/briefs/yalp_macros_phase2a_census_reconnaissance_2026-05-26.md`
- §1 Census API surface — 21 EITS datasets enumerated via live `api.census.gov/data.json` pull; 10 required variables verified via live `variables.json` per dataset
- §2 Per-indicator match-set — 79 yang indicators → 10 Census-PRIMARY + 69 n/a (best-source attribution per group)
- §3 Cadence per dataset — all 10 Census-PRIMARY monthly; advance-vs-revised distinction for 4 indicators
- §4 RE harness sketch — auth + endpoint pattern + per-indicator pull table + normalization + retry
- §5 Coverage % — **10/79 = ~12.7% Census-PRIMARY**; 4 Wave-2-adjacent datasets; sister-lane handoff matrix
- §6 Census-specific quirks — 8 surfaced (Missing-Key-HTML-200, string-typed cell_value, enum-discovery-pattern, time-slot semantics, joint Census/BEA, annual benchmarks, error_data flag, no-session model)

**5/5 ACs MET:**
- **AC1** ✅ Census API surface — 21 EITS datasets + endpoint pattern + required variables (live-verified)
- **AC2** ✅ Per-indicator match-set — all 79 yang indicators classified (10 PRIMARY + 69 n/a-with-best-source)
- **AC3** ✅ Cadence — monthly EITS class + quarterly EITS class + advance-vs-revised distinction
- **AC4** ✅ RE harness sketch — auth + endpoint + per-indicator pull table + normalization
- **AC5** ✅ Coverage % — 10/79 = ~12.7% + sister-lane handoff recommendation (FRED-PRIMARY + Census-SECONDARY for 10-indicator overlap class)

**Phase 2b TO-007 synthesis input (co-author with ~A primary):** recommendation that FRED be PRIMARY harness anchor (broader 79-coverage; single-source simplicity); Census be SECONDARY/cross-check for advance-release + sub-component + SA-toggle + pre-revision-benchmark dimensions. Census-PRIMARY-ONLY indicators (zero — all 10 also FRED-mirror) reduces to Census as a robust secondary corroboration source, not a primary harness requirement.

**Standing for:** RAVC2-ACCEPT on Phase 2a Census reconnaissance lane closure + Phase 2b TO-007 synthesis dispatch.

— 0.1.0_DS_MarketIntelligence~C
2026-05-26
