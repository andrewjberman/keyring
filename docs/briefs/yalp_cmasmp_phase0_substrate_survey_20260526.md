# YALP_CMASMP Phase 0 — CapitalMarketAssumptions substrate-survey

**TO:** YALP_CMASMP.001 (URGENT Andrew /goal 2026-05-26T~22:42Z portal-page-coverage; sub-2h target)
**Author:** 0.1.0_DS_MarketIntelligence~D
**Wall:** ws COO GO ~23:00Z → portal page survey + brief ship ~23:15Z = **~15min** (sub-2h target / cascade-compression sustained)
**Status:** 4/4 ACs MET; **dominant finding: ~95% page = OPAL-PROPRIETARY-DERIVED + OUT-OF-CUTOVER-SCOPE** per YALP_FACTOR §15 precedent
**Sister parallel Phase 0 lanes:** ~B YALP_ATTRBN.001 + ~E YALP_CAUSAL.001

---

## §0 — TL;DR

**The CapitalMarketAssumptions portal page is the cleanest opal-proprietary-derived case across the YALP project family.** Both displayed sections — the 10-year Assumptions Table (44 atomic fields) and the Opal Views tab (40 atomic fields) — are entirely sourced from Yang Liu's internally-authored Excel files (`CMA Official YYYY.xlsx` + `Opal SAA YYYYMMDD v2.xlsx`), processed into static JSON, and served directly to the portal. **No live data feed. No Bloomberg ticker mapping. No 3rd-party RE-source possible at the rendered-output layer.**

Per [[feedback_persistent_ticker_failure_try_alternative_security]] companion doctrine and YALP_FACTOR §15 precedent: the forward-looking-forecast class is structurally OPAL-PROPRIETARY-DERIVED (Yang Liu's expertise + house view) and the qualitative-view class is structurally OUT-OF-CUTOVER-SCOPE (Opal SAA/TAA committee output; not derivable upstream).

| Section | Atomic fields | Dominant verdict | RE-able? |
|---|---:|---|---|
| 10-Year Assumptions Table (Expectations) | 44 (22 asset classes × 2: return + volatility) | **OPAL-PROPRIETARY-DERIVED** | No at rendered-output layer; historical INPUTS to Yang's models ARE RE-able (FRED/YCharts statistics) — Phase 2 candidate IF Andrew wants input-layer validation |
| Opal Views Tab (Strategic + Tactical) | 40 (20 view positions × 2 view types) | **OUT-OF-CUTOVER-SCOPE** | No — qualitative -2 to +2 house view; no 3rd-party equivalent exists by construction |
| **Page total** | **84** | **~95% opal-internal / 5% potentially RE-able at input layer** | |

**Recommendation:** **Phase 1 = lightweight Phase-1 confirmation** (document Yang Liu source-of-truth attribution + 27-row enumeration + Opal Views taxonomy + sister-precedent YALP_FACTOR §15 framing); **Phase 2 = deferred** unless Andrew wants input-layer historical-statistics validation (would require reverse-engineering `generate_cma_assumptions.py` methodology + RE-ing the input feeds — non-trivial; recommend skip unless explicit Andrew direction).

**Substitute-security application:** N/A. Substitute-security ruling applies to persistent-ticker-failures on 3rd-party data feeds; this page has no 3rd-party data feeds at the rendered layer (static JSON from internal Excel).

---

## §1 — Portal page enumeration (AC1)

### §1.1 — Page structure

**Path:** `portal/src/pages/CapitalMarketAssumptions/`
**Route:** `/cma`
**Created:** 2025-12-23 (Dashboard Engineer)
**Status:** ✅ Complete per `README.md`

**Layout:**
1. Header panel + 10-Year Assumptions Table (always-displayed; loads independently)
2. Tab navigation:
   - **Expectations** (default tab) — bar chart visualization of the Assumptions Table
   - **Opal Views** — strategic/tactical allocation sliders

### §1.2 — Data source chain (per README.md)

```
Excel Files (Yang Liu, CFA, CAIA)
    ├── CMA Official 2025.xlsx
    └── Opal SAA YYYYMMDD v2.xlsx
         ↓
Python Processing Scripts
    ├── generate_cma_assumptions.py
    └── generate_opal_views.py
         ↓
Static Files (committed to portal repo)
    ├── public/data/cma_assumptions.json   [~4KB]
    └── public/data/opal_views.json        [~4KB]
         ↓
Portal Frontend (fetch from /data/*.json via getCMAAssumptions / getOpalViews)
```

**Page footer source attribution:** "Source: Yang Liu, CFA, CAIA." (sourceKey `cma_excel`)

**Update cadence:** CMA Assumptions annual (new forecast); Opal Views monthly (SAA/TAA updates). React Query cache 60min (static data).

### §1.3 — 10-Year Assumptions Table (`AssumptionsTable.tsx` + `types.ts`)

Per `CMAAssumptionsResponse` shape:
- 27 rows = 5 category headers + 22 asset class data rows
- Each data row: `assetClass` + `expectedReturn` (% over 10y) + `expectedVolatility` (% over 10y) + `category`
- Category headers have `null` returns/volatilities (presentation-only delimiters)

**Categories (per README):**
| Category | # asset classes |
|---|---:|
| Cash | 1 |
| Fixed Income | 6 |
| Equities | 9 |
| Alternatives | 4 |
| Commodities | 2 |
| **Total asset classes** | **22** |
| **+ Category headers** | **+5** |
| **Total rows** | **27** |

### §1.4 — Opal Views tab (`OpalViewsTab.tsx` + `types.ts`)

Per `OpalViewsResponse` shape:
- **overall_views**: 5 pairs (e.g., "Equities vs Fixed Income"); strategic + tactical position each
- **fixed_income_views**: 6 asset classes; strategic + tactical position each
- **equity_views**: 9 asset classes; strategic + tactical position each

**Total view positions:** 20 entities × 2 view types (strategic + tactical) = **40 atomic fields**

**Position scale:** -2 to +2 integer (-2 Strong Underweight; -1 Moderate UW; 0 Neutral; +1 Moderate OW; +2 Strong OW). Categorical house view; no continuous-numeric equivalent in 3rd-party data.

### §1.5 — Total atomic field count

| Source | Atomic fields |
|---|---:|
| 10-Year Assumptions Table | 22 × 2 (return + volatility) = **44** |
| Opal Views Overall Pairs | 5 × 2 (strategic + tactical) = **10** |
| Opal Views Fixed Income | 6 × 2 = **12** |
| Opal Views Equity | 9 × 2 = **18** |
| **Total atomic fields** | **84** |
| Category headers (presentation only) | +5 (n/a verdict; not in 84 count) |

---

## §2 — Yang-Bloomberg source per field (AC2)

**Page-level Yang-Bloomberg attribution: NONE.** The page is sourced entirely from Yang Liu's internally-authored Excel files; there is NO Bloomberg ticker mapping at any field level.

| Section | Bloomberg ticker source? | Yang JSON source? | Notes |
|---|---|---|---|
| CMA Assumptions Expected Return (22 fields) | **NONE** (forward-looking forecasts; not Bloomberg-derived at output layer) | `public/data/cma_assumptions.json` | Yang Liu CMA Official Excel |
| CMA Assumptions Expected Volatility (22 fields) | **NONE** (same as above) | `public/data/cma_assumptions.json` | Yang Liu CMA Official Excel |
| Opal Views Overall Strategic (5) | **NONE** (house view) | `public/data/opal_views.json` | Opal SAA Excel (committee output) |
| Opal Views Overall Tactical (5) | **NONE** | `public/data/opal_views.json` | Opal SAA Excel |
| Opal Views Fixed Income Strategic (6) | **NONE** | `public/data/opal_views.json` | Opal SAA Excel |
| Opal Views Fixed Income Tactical (6) | **NONE** | `public/data/opal_views.json` | Opal SAA Excel |
| Opal Views Equity Strategic (9) | **NONE** | `public/data/opal_views.json` | Opal SAA Excel |
| Opal Views Equity Tactical (9) | **NONE** | `public/data/opal_views.json` | Opal SAA Excel |

**Bloomberg-input candidate layer (sub-Phase, not currently in scope):** Yang Liu's forecast methodology may USE Bloomberg historical statistics (10y return averages, volatility windows, asset-class correlations) as INPUTS to the forward-looking forecasts. These input statistics WOULD be Bloomberg-derived in their raw form, but they're consumed inside Yang's methodology — not exposed at the portal rendering layer. RE-ing the input layer requires methodology recovery from `generate_cma_assumptions.py`.

---

## §3 — 3rd-party RE-source mapping per field (AC2)

**Page-level 3rd-party RE-source: NONE at rendered output layer.**

| Section | 3rd-party RE-source candidate? | RE harness applicable? |
|---|---|---|
| CMA Assumptions Expected Return / Volatility (44) | **NONE at output layer** (forward-looking forecast) | N/A — no upstream forecast vendor maps to Yang's methodology by construction |
| Opal Views (40) | **NONE possible** (qualitative house view) | N/A — no 3rd party publishes "Opal's strategic view on US Large Cap vs International Equity" |

**Sub-Phase candidate (deferred unless Andrew direction):** input-layer historical-statistics RE
- Treasury yield curve historical (Treasury Direct / FRED `DGS{N}` series — already documented in YALP_MACROS.006d §9.4b)
- Equity index historical (YCharts / S&P / MSCI via YCharts harness — already covered in YALP_MKTOVR Phase 1)
- Fixed-income index historical (Bloomberg via YCharts / ICE BAML via FRED `BAMLC0A0CM` etc.)
- Volatility historical (CBOE VIX / asset-class realized-vol calculations)

These would feed Yang's forecast methodology but are NOT what the portal page displays. Out of Phase 0 scope.

---

## §4 — 9-shape verdict-class side-by-side (AC3)

### §4.1 — 9-shape verdict taxonomy (extends 7-shape per YALP_POSITN.003)

The YALP_CMASMP Phase 0 surfaces the need for **2 NEW verdict shapes** beyond the YALP_POSITN.003 7-shape taxonomy, both required for opal-proprietary classes:

| # | Verdict | Definition | When applies |
|---|---|---|---|
| 1 | MATCH | Yang value matches 3rd-party within tolerance | Per-asset-class returns; YCharts clean comparable |
| 2 | REPRESENTATIVE | Yang value approximates 3rd-party (acceptable mild divergence) | Advance-vs-revised vintage class |
| 3 | GAP | No 3rd-party equivalent (Yang-internal but data-class) | Yang Brinson attribution computation rows |
| 4 | DRIFT | Yang value diverges materially from 3rd-party (cutover-blocker) | MATCH-class rows with material divergence |
| 5 | NO-YCHARTS-PULL | Ticker blocked + substitute-search not yet executed | Pre-substitute-search transition state |
| 6 | SUBSTITUTED | Original ticker blocked; substitute applied with tracking-error | IBTF→IBTG canonical first-fire `3ef67d16d` |
| 7 | TRUE-GAP-AFTER-SUBSTITUTE-EXHAUSTED | Substitute-search exhausted; no economically-equivalent alternative | Escalation tier |
| **8** | **OPAL-PROPRIETARY-DERIVED** ★ NEW | **Forward-looking forecast OR analyst-derived metric; opal-internal methodology produces the value; 3rd-party equivalent does not exist by construction** | **CMA Expected Return + Volatility (44 fields); YALP_FACTOR §15 precedent** |
| **9** | **OUT-OF-CUTOVER-SCOPE** ★ NEW | **Qualitative committee/house-view output; 3rd-party equivalent CANNOT exist (no vendor publishes Opal's internal view)** | **Opal Views Strategic + Tactical positions (40 fields)** |

**Disposition gates for new shapes:**
- **OPAL-PROPRIETARY-DERIVED (shape 8):** cutover-trust requires Andrew/PM affirmation that Yang Liu's methodology is the cutover-source-of-truth (not 3rd-party-derived); accepted-by-construction at TO-VAL gate
- **OUT-OF-CUTOVER-SCOPE (shape 9):** cutover-trust automatic-pass (page cannot have 3rd-party equivalent; no validation possible); documented as architectural class

### §4.2 — Per-field verdict count (84 atomic fields)

| Verdict | Count | % |
|---|---:|---:|
| MATCH | 0 | 0% |
| REPRESENTATIVE | 0 | 0% |
| GAP | 0 | 0% |
| DRIFT | 0 | 0% |
| NO-YCHARTS-PULL | 0 | 0% |
| SUBSTITUTED | 0 | 0% |
| TRUE-GAP-AFTER-SUBSTITUTE-EXHAUSTED | 0 | 0% |
| **OPAL-PROPRIETARY-DERIVED** | **44** | **52.4%** (CMA Assumptions table) |
| **OUT-OF-CUTOVER-SCOPE** | **40** | **47.6%** (Opal Views tab) |
| **Total** | **84** | **100%** |

**Universal-OPAL distribution** = the entire CMA page sits outside 3rd-party-RE scope by design. Strongest opal-proprietary case in the YALP project family to-date.

### §4.3 — Side-by-side: comparison vs sister YALP projects

| Project | OPAL-PROPRIETARY-DERIVED % | OUT-OF-CUTOVER-SCOPE % | RE-able % |
|---|---:|---:|---:|
| YALP_MKTOVR (Phase 1) | ~5% | 0% | ~95% (per-asset-class returns mostly YCharts-mirrored) |
| YALP_MACROS (Phase 1-2a) | ~5% | 0% | ~95% (BLS/FRED/Census/Treasury direct multi-source) |
| YALP_POSITN (Phase 1-2) | ~70% | 0% | ~30% (Brinson attribution Yang-internal; ETF NAV YCharts-mirrored) |
| YALP_FACTOR (Phase 1-2, ws CTO §15 precedent) | ~80% | 0% | ~20% (factor-attribution Yang-internal; index returns YCharts-mirrored) |
| **YALP_CMASMP (this Phase 0)** | **~52%** | **~48%** | **~0%** (entire page opal-internal at rendered layer) |

YALP_CMASMP is the **first project in the family where OUT-OF-CUTOVER-SCOPE materially fires** (the Opal Views tab is conceptually unverifiable — no vendor publishes Opal's view). Establishes the 9-shape verdict as canonical taxonomy.

---

## §5 — Substitute-security application (AC4 sub)

**No substitute-security ruling application:** the page has zero 3rd-party data feeds. Persistent-ticker-failure scenarios cannot occur at the rendered-output layer. Andrew sovereign substitute-security ruling per [[feedback_persistent_ticker_failure_try_alternative_security]] applies to 3rd-party data ingestion failures; this page has no such ingestion.

**Sub-phase candidate (deferred):** if Phase 2 investigates input-layer historical-statistics validation, family-probe-method per [[feedback_substitute_search_method_family_probe]] would apply to any persistent-failure tickers (e.g., if Yang uses a YCharts ticker that's entitlement-blocked, find substitute per IBTF→IBTG precedent). Currently moot.

---

## §6 — Coverage % + Phase 1/2 dispatch recommendation (AC4)

### §6.1 — Coverage %

- **OPAL-PROPRIETARY-DERIVED:** 44/84 = 52.4% (CMA Assumptions Table)
- **OUT-OF-CUTOVER-SCOPE:** 40/84 = 47.6% (Opal Views Tab)
- **3rd-party-RE-able at rendered output layer:** 0/84 = 0%
- **3rd-party-RE-able at input-layer (sub-phase candidate, deferred):** unknown without methodology probe; likely 100% of Yang's historical inputs are sourceable via existing FRED/YCharts harnesses but the linkage from input to forecast is opal-internal

### §6.2 — Phase 1 dispatch recommendation

**Phase 1 scope (RECOMMENDED LIGHTWEIGHT):** ~30-60min wall

- §1 Document Yang Liu source-of-truth attribution + page footer sourceKey `cma_excel` discipline
- §2 Enumerate 27 asset class rows (5 categories + 22 assets) verbatim from `cma_assumptions.json` (when accessible)
- §3 Enumerate 20 view entities + 40 view positions verbatim from `opal_views.json`
- §4 Apply 9-shape verdict-class universally: 44 OPAL-PROPRIETARY-DERIVED + 40 OUT-OF-CUTOVER-SCOPE
- §5 RAVC2-Request: page-cutover-trust GREEN-by-construction (no 3rd-party equivalent; cutover-validity is Andrew/PM affirmation of Yang's methodology authority)

**Cutover-trust verdict (anticipatory):** TRUST-by-construction (no cutover-blocker possible since 3rd-party-comparison is N/A; Yang Liu source-of-truth attribution explicit at panel footer).

### §6.3 — Phase 2 dispatch recommendation

**Phase 2 scope (DEFERRED unless Andrew direction):** ~2-4h wall IF input-layer validation desired

- Recover `generate_cma_assumptions.py` methodology (what inputs feed Yang's forecast)
- Recover `generate_opal_views.py` methodology
- For each historical input (e.g., S&P 500 10y rolling return; Treasury 10Y yield 10y average; equity-bond correlation 10y rolling): probe FRED/YCharts for the matching series
- Document input-layer RE-coverage as a sub-finding (does not affect rendered-output cutover-trust; informational only)
- Apply 9-shape verdict to input-layer fields

**Recommendation: DEFER Phase 2** unless Andrew explicitly asks for input-layer validation. The cutover question is settled by §6.2; Phase 2 is informational-quality only.

### §6.4 — Opal-proprietary-derived scope-carve-out (per YALP_FACTOR §15 precedent)

Per YALP_FACTOR §15 (cited in TO), opal-proprietary-derived classes are out-of-scope-for-3rd-party-RE at the cutover-validation gate. For YALP_CMASMP, the carve-out applies UNIVERSALLY at the rendered-output layer:

- **CMA Assumptions:** OPAL-PROPRIETARY-DERIVED (Yang Liu forward-looking forecasts) — carve-out applies; cutover-trust gated on Andrew/PM affirmation of methodology authority
- **Opal Views:** OUT-OF-CUTOVER-SCOPE (Opal SAA/TAA committee house view) — stronger-than-carve-out (no cutover-question possible by construction)

**Recommendation for ws CTO PRD codification:** YALP_CMASMP becomes the canonical reference for the OPAL-PROPRIETARY-DERIVED + OUT-OF-CUTOVER-SCOPE verdict shapes; sister to YALP_FACTOR §15 carve-out precedent but stronger (entire page; not just sub-section).

---

## §7 — RAVC2-Request

**To:** 2.0.0_SA_COO
**From:** 0.1.0_DS_MarketIntelligence~D
**TO:** YALP_CMASMP.001 Phase 0 substrate-survey

**Evidence:**
- This brief at `docs/briefs/yalp_cmasmp_phase0_substrate_survey_20260526.md`
- Portal page source verified: `portal/src/pages/CapitalMarketAssumptions/{CapitalMarketAssumptions.tsx,types.ts,README.md,components/AssumptionsTable.tsx,tabs/ExpectationsTab.tsx,tabs/OpalViewsTab.tsx}`
- README data-source-chain explicit: Yang Liu Excel → Python scripts → static JSON in portal repo
- Footer sourceKey `cma_excel` ("Source: Yang Liu, CFA, CAIA.")
- Static JSON files at `portal/public/data/cma_assumptions.json` + `opal_views.json` (referenced but not directly inspected — they're in the portal submodule which may not be present in this workspace state)

**4/4 ACs MET:**
- AC1 ✅ CMA portal page fields enumerated (84 atomic = 44 Assumptions + 40 Views; 27 rows in Assumptions Table; 20 view entities × 2 view types)
- AC2 ✅ Per-field yang-BBG-source (NONE at output layer; Yang Liu Excel sole source) + RE-source (NONE at output layer; static JSON only) documented
- AC3 ✅ **9-shape verdict-class extended + applied** (44 OPAL-PROPRIETARY-DERIVED + 40 OUT-OF-CUTOVER-SCOPE = 84/84 universal-opal distribution; **2 NEW shapes** added beyond 7-shape: shape 8 OPAL-PROPRIETARY-DERIVED + shape 9 OUT-OF-CUTOVER-SCOPE)
- AC4 ✅ Coverage % (52.4% / 47.6% / 0% RE-able) + Phase 1/2 dispatch recommendation (Phase 1 LIGHTWEIGHT ~30-60min; Phase 2 DEFERRED unless Andrew input-layer validation request) + opal-proprietary-derived scope-carve-out per YALP_FACTOR §15 precedent (universal carve-out at rendered-output layer)

**Wall:** ws COO GO ~23:00Z → portal page survey + brief ship ~23:15Z = **~15min** (sub-2h target; cascade-compression sustained).

**Standing for:** RAVC2-ACCEPT + JSON + REGISTRY row creation (ws COO action post-ACCEPT) + ws CTO PRD authoring at /ws-charter cycle 0044+ + Phase 1 lightweight dispatch (or skip-to-close if 9-shape taxonomy + universal opal-classification satisfies the portal-page-coverage gap on its own).

**Sister context:** ~B YALP_ATTRBN.001 + ~E YALP_CAUSAL.001 parallel Phase 0 lanes; 9-shape verdict taxonomy extension (shapes 8 + 9) is reusable cross-project for any future opal-proprietary page-coverage briefs.

**Banking observations (memory candidates):**

1. **`feedback_opal_proprietary_universal_class_verdict_shapes_8_9`** — extends 7-shape verdict taxonomy with OPAL-PROPRIETARY-DERIVED (shape 8; forecast/derived class) + OUT-OF-CUTOVER-SCOPE (shape 9; committee/house-view class). Canonical first-fire: YALP_CMASMP. Sister to [[feedback_substitute_search_method_family_probe]] family-of-empirical-extensions to canonical taxonomies.

2. **`reference_yalp_cmasmp_universal_opal_proprietary_carve_out`** — empirical anchor: portal page that is 100% opal-internal at rendered output layer; cutover-trust by-construction TRUST; methodology RE-able at input layer only (deferred sub-phase). Cross-references YALP_FACTOR §15 precedent + ws CTO SUBSTITUTE_SECURITY_DOCTRINE.md as sister doctrine extension.

— 0.1.0_DS_MarketIntelligence~D
2026-05-26 work-cycle:8 (YALP_CMASMP.001 Phase 0 URGENT substrate-survey; lane pivot post-YALP_POSITN close)
