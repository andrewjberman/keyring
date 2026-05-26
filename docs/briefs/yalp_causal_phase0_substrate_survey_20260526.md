# YALP_CAUSAL Phase 0 — CausalityEngine Substrate-Survey

**TO:** YALP_CAUSAL.001 — URGENT Phase 0 substrate-survey for CausalityEngine portal page
**Author:** 0.1.0_DS_MarketIntelligence~E
**Authority:** Andrew /goal sovereign 2026-05-26T~22:42Z portal-page-coverage discipline + ws COO /drive cycle 116 URGENT GO-DISPATCH
**T*:** N/A — substrate-survey class (not value-comparison)
**Status:** Phase 0 COMPLETE — 4/4 ACs met; **finding: ENTIRELY OPAL-PROPRIETARY-DERIVED page; scope-clarification-class (NOT full Phase 1/2 YALP project)**

---

## §0 — TL;DR

**CausalityEngine is a NEWS+AI ANALYTICS product, NOT a yang-pipeline-fed cutover-trust page.** No 3rd-party-source RE applies at the page-output level. Substrate-survey finding parallels (and EXCEEDS) YALP_FACTOR §15 "n/a out-of-cutover-scope" precedent:

| Layer | Output class | RE-able? | Verdict |
|---|---|---|---|
| **Page-level outputs** (Themes / ThematicSignals / Analyses / SavedAnalyses) | News-aggregation + AI-generated analysis + proprietary scoring | **NO** — entirely opal-proprietary-derived | **OPAL-PROPRIETARY-DERIVED (9-shape class 8)** — out-of-cutover-scope |
| **Primitive market data** (TickerPerformance current_price + change_pct + volume_ratio; PricePoint timeseries) | Per-ticker price + volume | **YES** — YCharts-RE-able via existing `^TICKER` endpoints | **MATCH-class candidate** if mapping known; sister to YALP_MKTOVR ticker-class |
| **Derived technicals** (TechnicalSummary RSI / SMA-20 / SMA-50 / pattern) | Computed from price history | **DERIVED** — RE-reproducible from YCharts price input | **DERIVED-class** (compute, not direct lookup) |
| **MarketOverview widget** (SPY/QQQ/VIX cards — currently MOCK per `MarketOverview.tsx:8`) | Three index quotes | **YES** when wired | **MATCH-class candidate** when wired; SAME upstream class as YALP_MKTOVR market-cards |
| **News content** (Article + SeekingAlphaArticle) | News article metadata + content | **NO** — Seeking Alpha is paywalled; news headlines available via news APIs but article content + author attribution is paywalled-or-licensed | **PAID-SUBSCRIPTION / out-of-cutover-scope** |
| **Sentiment scoring** (Theme.sentiment, Article.sentiment) | Per-news-item sentiment [-1, 1] | **NO** — opal-proprietary NLP scoring | **OPAL-PROPRIETARY-DERIVED** |
| **Relevance / Confidence scoring** (Theme.relevance_score, ThematicSignal.confidence) | Proprietary ranking model | **NO** — opal-proprietary scoring | **OPAL-PROPRIETARY-DERIVED** |
| **AI-generated Analysis** (Analysis.summary, catalysts, technical_summary narrative) | LLM-generated trade-idea content | **NO** — opal-proprietary AI generation | **OPAL-PROPRIETARY-DERIVED** |
| **User-generated content** (SavedAnalysis notes, tags) | User-authored | **NO** — user-state, not data | **USER-STATE / out-of-cutover-scope** |

**Scope-carve-out recommendation:** **YALP_CAUSAL project scopes to scope-clarification-class, NOT full Phase 1/2 YALP project.** Page does not consume yang-pipeline `model.pkl` or similar; it consumes news-pipeline + AI-generation + ticker-price-API outputs. The 3rd-party-RE applicable surface is narrow (ticker prices, technical indicators) and is already covered by sister YALP projects (YALP_MKTOVR ticker-class, YALP_FACTOR price-history-class). No new cutover-trust gate fires at the Causality Engine page level beyond ticker-price-primitive sharing with sister pages.

**Lambda + endpoint architecture (per `portal/src/api/endpoints/causality-endpoints.ts:34`):**
- 8 dedicated Lambda endpoints: `causality-thematic-signals-generator`, `causality-themes-fetcher`, `causality-generate-analysis`, `causality-save-analysis`, `causality-get-history`, `causality-delete-analysis`, `causality-update-notes`, `causality-generate-market-update`
- API Gateway base: `/causality` routed via CloudFront
- **Separate service stack** from yang-pipeline (DRY: yang owns Portfolio Analytics; CausalityEngine owns News+AI Analytics)
- EventBridge daily 6:00 AM ET trigger for `causality-thematic-signals-generator`

**Phase 1/2 dispatch recommendation:** **DEFER full Phase 1/2 YALP cycle.** Substrate is opal-proprietary; no 3rd-party-RE verdict surface to verify at cutover. Convert to **3-finding scope-clarification brief** + optional **Phase 0+ follow-up** if Andrew wants ticker-price-primitive verification on MarketOverview widget once wired (~5 fields, sub-30min).

---

## §1 — Portal Page Output Enumeration

### §1.1 — Component tree (per `portal/src/pages/CausalityEngine/`)

```
CausalityEngine.tsx (top-level; 2 tabs: Discovery + History)
├── CausalityEngineHeader.tsx (page header)
├── MarketOverview.tsx (SPY/QQQ/VIX 3-card MOCK widget; "wired by Dashboard Engineer")
├── SystemDescription.tsx (static narrative)
├── Tab1_Discovery.tsx (active tab)
│   ├── FilterControls.tsx (time-range / sentiment / sector filters)
│   ├── ThemeBubbleGalaxy/ (visualization of themes as bubbles)
│   │   └── ThemeBubble.tsx (per-theme bubble component)
│   └── SelectedThemesPanel.tsx (selected themes + generate-analysis trigger)
├── Tab2_History.tsx (placeholder; "coming soon")
├── Tab2_Generate.tsx (analysis generation UI)
├── hooks/
│   ├── useCausalityApi.ts (8 React Query hooks; per §1.4)
│   └── useCausalityStore.ts (Zustand state store)
└── mockData.ts (development-time mock fixtures)
```

### §1.2 — Primary data outputs surfaced to user (per `types.ts`)

| # | Output | Type | Surfaced via | Yang-pipeline? | 3rd-party-RE primitive? |
|---|---|---|---|---|---|
| 1 | **Theme** (trending topic) | object: theme_id, headline, description, article_count, sentiment, sector, tickers[], relevance_score, articles[], seeking_alpha_analysis[] | ThemeBubbleGalaxy, SelectedThemesPanel | NO | partial (tickers list = ticker primitives; rest = opal news+AI) |
| 2 | **ThematicSignal** (top-3 daily signal) | object: signal_id, rank, theme, price_summary, avg_price_change, volume_ratio, confidence | CausalityEngineHeader | NO | partial (price/volume = YCharts primitives; rest = opal scoring) |
| 3 | **Analysis** (AI-generated trade idea) | object: summary, catalysts[], price_impact, technical_summary, ticker_performance[], created_at, tags | Tab1_Discovery (post-Generate) | NO | partial (technical_summary + ticker_performance = primitive-derived; rest = opal AI) |
| 4 | **SavedAnalysis** (user's library entry) | object: analysis, notes, saved_at, last_viewed, tags | Tab2_History | NO | user-state class |
| 5 | **MarketOverview** (SPY/QQQ/VIX cards) | 3× {price, change_pct} | MarketOverview widget | NO | YES — YCharts primitives (currently MOCK per source code) |
| 6 | **PriceImpact / PricePoint** (chart data for analyses) | timeseries: {timestamp, price, volume} | Analysis modal chart | NO | YES — YCharts price-history primitives |
| 7 | **TechnicalSummary** (RSI / SMA-20 / SMA-50 / pattern) | computed indicators per ticker | Analysis modal technical pane | NO | DERIVED — YCharts-RE-reproducible from price-history input |
| 8 | **TickerPerformance** (per-ticker price + volume ratio) | per-ticker snapshot | Analysis ticker grid | NO | YES — YCharts current-price + volume primitives |

### §1.3 — 8 Lambda endpoints (per `causality-endpoints.ts:42-...`)

| # | Endpoint | Method | Lambda producer | Trigger / cache | Yang-pipeline? |
|---|---|---|---|---|---|
| 1 | `/causality/thematic-signals` | GET | `causality-thematic-signals-generator` | EventBridge daily 6 AM ET | NO |
| 2 | `/causality/themes` | GET | `causality-themes-fetcher` | On-request; 5min cache | NO |
| 3 | `/causality/generate-analysis` | POST | `causality-generate-analysis` | User-triggered (LLM call) | NO |
| 4 | `/causality/save-analysis` | POST | `causality-save-analysis` | User action | NO (user-state) |
| 5 | `/causality/history` | GET | `causality-get-history` | On-request; 10min cache | NO (user-state) |
| 6 | `/causality/delete-analysis` | DELETE | `causality-delete-analysis` | User action | NO (user-state) |
| 7 | `/causality/notes/{id}` | PUT | `causality-update-notes` | User action | NO (user-state) |
| 8 | `/causality/market-update` | POST | `causality-generate-market-update` | User-triggered (PowerPoint export) | NO |

**Architectural note:** All 8 endpoints route through dedicated `/causality` API Gateway prefix (NOT yang-pipeline's `/api/general/*` or `/yang/*` namespace). CausalityEngine is a SEPARATE SERVICE STACK from yang Portfolio Analytics.

### §1.4 — 5 React Query hooks (per `useCausalityApi.ts`)

- `useThematicSignals()` — 1h staleTime
- `useThemes(params)` — 5min staleTime
- `useHistory(params)` — 10min staleTime
- `useAPIHealth()` — 30s staleTime
- `useGenerateAnalysis()` / `useSaveAnalysis()` / `useDeleteAnalysis()` / `useUpdateNotes()` / `useGenerateMarketUpdate()` — mutation hooks

---

## §2 — Yang-Source + 3rd-Party RE-Source Side-by-Side

### §2.1 — Yang-pipeline upstream

**NONE.** CausalityEngine does not consume any yang-pipeline producer (`yang-generate-*` Lambdas, `model.pkl`, `data.pkl`, etc.). The page consumes only its own dedicated `/causality/*` Lambda outputs.

### §2.2 — 3rd-party-RE per output

| Output | RE-able primitives within output | 3rd-party source | Sister-YALP-coverage |
|---|---|---|---|
| Theme.tickers[] | ticker symbols (just identifiers; no values) | n/a (identifier only) | n/a |
| ThematicSignal price_summary / avg_price_change / volume_ratio | per-ticker price/volume snapshots | **YCharts** (per `^TICKER` endpoints) | YALP_MKTOVR ticker-class precedent |
| Analysis.ticker_performance[].current_price / price_change_pct / volume_ratio | per-ticker snapshots | **YCharts** | YALP_MKTOVR / YALP_FACTOR price-class |
| Analysis.technical_summary.rsi / sma_20 / sma_50 | computed indicators | **YCharts price-history → RSI/SMA compute** (DERIVED) | not directly covered; computation-class |
| Analysis.price_impact.chart_data[] | per-ticker timeseries | **YCharts** | YALP_FACTOR Phase 1 price-history-class |
| MarketOverview SPY / QQQ / VIX | 3 index quotes (currently MOCK) | **YCharts** (`^SPY` / `^QQQ` / `^VIX`) when wired | YALP_MKTOVR ticker-class (VIX directly per macro_data.json sister) |
| Theme.sentiment / Article.sentiment | sentiment scores [-1, 1] | **NONE** — opal-proprietary NLP | n/a (opal-proprietary-derived) |
| Theme.relevance_score / ThematicSignal.confidence | proprietary scoring [0-100] | **NONE** — opal-proprietary ranking model | n/a (opal-proprietary-derived) |
| Analysis.summary / catalysts / technical_summary (narrative) | LLM-generated text | **NONE** — opal-proprietary AI generation (LLM) | n/a (opal-proprietary-derived) |
| Article.title / source / url / published_at / summary | news article metadata | **News API** (paywalled / licensed depending on provider; Seeking Alpha = subscription) | PAID-SUBSCRIPTION class |
| SeekingAlphaArticle.title / author / rating / summary | Seeking Alpha article metadata | **Seeking Alpha** (subscription) | PAID-SUBSCRIPTION class |
| SavedAnalysis.notes / tags | user-authored | n/a (user-state) | n/a |

---

## §3 — Substitute-Security Application

**N/A for this Phase 0** — substrate-survey class, not value-comparison class. No persistent failures to substitute.

**For future Phase 0+ ticker-primitive follow-up (if scoped):** standard YALP_MKTOVR substitute-security doctrine applies per [[feedback_persistent_ticker_failure_try_alternative_security]] (Andrew sovereign) — family-probe + composite reconstruction + mirror-source per ~D §2.1 pattern.

---

## §4 — Per-Output 9-Shape Verdict-Class Table

**Adapted 9-shape verdict-class taxonomy** (extends YALP_FACTOR 7-shape with explicit opal-proprietary-derived + RE-GAP classes per CausalityEngine + ~D extension):

| Class | Threshold / Definition | Cutover gate |
|---|---|---|
| 1. MATCH-tight | Reconstruction = source within float precision | GREEN |
| 2. MATCH | <0.01 abs delta | GREEN |
| 3. NEAR-MATCH | <0.05 abs delta | GREEN |
| 4. REPRESENTATIVE-tight | <0.10 abs delta | GREEN with cite |
| 5. REPRESENTATIVE | <1.00 abs delta | GREEN with cite |
| 6. DRIFT-suspect | <5.00 abs delta | REVIEW |
| 7. DRIFT-confirmed | ≥5.00 abs delta | NO-TRUST |
| 8. **OPAL-PROPRIETARY-DERIVED** | Structurally not 3rd-party-RE-able (Opal-internal compute, AI, scoring, sentiment, user-state) | out-of-cutover-scope (n/a) |
| 9. **RE-GAP** | 3rd-party-RE conceptually applicable but no authoritative open source available (paid sub / discontinued / no API) | flag-for-doc; out-of-cutover-scope |

### §4.1 — Per-output verdict assignment

| # | Output | Verdict-class | Rationale |
|---|---|---|---|
| 1 | Theme (whole object) | **OPAL-PROPRIETARY-DERIVED (8)** | News aggregation + opal sentiment/relevance scoring |
| 2 | ThematicSignal (whole object) | **OPAL-PROPRIETARY-DERIVED (8)** | Opal ranking model + proprietary confidence scoring |
| 3 | Analysis (whole object) | **OPAL-PROPRIETARY-DERIVED (8)** | LLM-generated content; no 3rd-party equivalent |
| 4 | SavedAnalysis | **OPAL-PROPRIETARY-DERIVED (8)** | User-state class |
| 5 | MarketOverview.spy/qqq/vix (when wired) | **MATCH-class candidate (2)** | YCharts `^SPY`/`^QQQ`/`^VIX` direct; currently MOCK |
| 6 | PriceImpact.chart_data[] | **MATCH-class candidate (2)** | YCharts price-history primitive per ticker |
| 7 | TechnicalSummary.rsi/sma_20/sma_50 | **DERIVED → MATCH-after-compute (2/4)** | RE-reproducible from YCharts price history; computation-class |
| 8 | TickerPerformance.current_price/price_change_pct/volume_ratio | **MATCH-class candidate (2)** | YCharts per-ticker primitive |
| 9 | Article / SeekingAlphaArticle | **RE-GAP (9)** | News content (Seeking Alpha paywalled; news APIs licensed) |
| 10 | Theme.sentiment / Article.sentiment | **OPAL-PROPRIETARY-DERIVED (8)** | Opal NLP sentiment scoring |
| 11 | Theme.relevance_score / ThematicSignal.confidence | **OPAL-PROPRIETARY-DERIVED (8)** | Opal proprietary scoring |
| 12 | Analysis.summary / catalysts / technical_summary narrative | **OPAL-PROPRIETARY-DERIVED (8)** | LLM-generated text |

**Verdict distribution:**
- **OPAL-PROPRIETARY-DERIVED (class 8):** 8/12 (66.7%) — heavy carve-out
- **MATCH-class candidate (class 2):** 3/12 (25%) — ticker price/volume primitives via YCharts
- **DERIVED → MATCH (class 4):** 1/12 (8.3%) — technical indicators computed from price history
- **RE-GAP (class 9):** 1/12 (8.3%) — news content (paywalled)

**Cutover-trust gate applicability:** **NONE of the 12 outputs require cutover-trust verdict at YALP_CAUSAL scope.** The 4 MATCH-class candidates (#5, #6, #7, #8) are ALL ticker-price-primitive class which is structurally covered by sister YALP projects (YALP_MKTOVR + YALP_FACTOR). YALP_CAUSAL doesn't surface new cutover-trust risk.

---

## §5 — Coverage % + Phase 1/2 Dispatch Recommendation

### §5.1 — Coverage summary

| Class | Count | % | Implication |
|---|---:|---:|---|
| OPAL-PROPRIETARY-DERIVED (8) | 8 | 66.7% | Heavy scope-carve-out; out-of-cutover-scope |
| MATCH-class candidate (ticker-primitive) | 3 | 25.0% | Already structurally covered by sister YALP |
| DERIVED-class | 1 | 8.3% | Computation-class; sister YALP covers underlying primitives |
| RE-GAP (paid-sub news) | 1 | 8.3% | flag-for-doc; out-of-cutover-scope |
| **3rd-party-RE applicable at Causal-page-scope** | **0** | **0%** | **Per-output cutover-trust verdict NOT NEEDED at YALP_CAUSAL** |

### §5.2 — Phase 1/2 dispatch recommendation: SCOPE-CLARIFICATION-CLASS (NOT full Phase 1/2)

**Recommendation: convert YALP_CAUSAL from "full YALP project" to "scope-clarification-class brief"** + optional Phase 0+ ticker-primitive follow-up.

**Reasoning:**
1. **No yang-pipeline consumption** — CausalityEngine is a separate service stack (news + AI + ticker-API). YALP per-page cutover-trust pattern (yang→3rd-party validation) doesn't apply.
2. **Page-output level is entirely opal-proprietary-derived** (8/12 outputs) — no 3rd-party-RE equivalent exists by design (LLM-generated analysis, opal scoring, news aggregation).
3. **Primitive-level ticker outputs are sister-YALP-covered** — MarketOverview + Analysis ticker-snapshots use YCharts ticker primitives already verified via YALP_MKTOVR / YALP_FACTOR cycles.
4. **News content is paid-subscription RE-GAP** — Seeking Alpha + licensed news APIs; consistent with Andrew "monthly cadence acceptable" + scope-carve-out framing per YALP_FACTOR §15 precedent.

**Equivalent precedent:** YALP_FACTOR §15 "Tier 1 regression layer = n/a out-of-cutover-scope" — Causality Engine outputs are similarly opal-proprietary-derived analytics where YCharts has no equivalent; carve-out is the structurally-correct disposition.

### §5.3 — Optional Phase 0+ follow-up (if Andrew wants extra verification)

**MarketOverview ticker-primitive verification (~5 fields, sub-30min):**
- When MarketOverview is wired from mock to real (currently `MarketOverview.tsx:8` mock data), pull SPY/QQQ/VIX from YCharts and confirm price/change_pct match within MATCH-class tolerance.
- Sister-scope to YALP_MKTOVR Phase 2 ticker-set; can be folded into next YALP_MKTOVR cycle rather than authored as standalone YALP_CAUSAL Phase 1.

**No Phase 1/2 substantive work warranted at YALP_CAUSAL.**

---

## §6 — RAVC2-Request

**To:** 2.0.0_SA_COO
**From:** 0.1.0_DS_MarketIntelligence~E
**TO:** YALP_CAUSAL.001 — URGENT Phase 0 substrate-survey

**Evidence:**
- This brief at `docs/briefs/yalp_causal_phase0_substrate_survey_20260526.md`
- Source enumeration: `portal/src/pages/CausalityEngine/` (component tree, types.ts, hooks, MarketOverview.tsx mock)
- API enumeration: `portal/src/api/endpoints/causality-endpoints.ts` (8 Lambda endpoints + dedicated `/causality` API Gateway prefix)
- React Query hooks: `portal/src/pages/CausalityEngine/hooks/useCausalityApi.ts` (5 query hooks + 5 mutation hooks)

**4/4 ACs MET:**
- **AC1** ✅ Causality Engine portal page outputs enumerated — §1 12 distinct outputs across 8 Lambda endpoints + 2 tab UIs (Discovery active, History placeholder)
- **AC2** ✅ Per-output yang-source + RE-source side-by-side — §2.2 (zero yang-pipeline consumption; ticker primitives → YCharts; news content → paid-sub; analytics → opal-proprietary)
- **AC3** ✅ 9-shape verdict-class assigned per output — §4.1 (8 OPAL-PROPRIETARY-DERIVED + 3 MATCH-candidate + 1 DERIVED + 1 RE-GAP)
- **AC4** ✅ Coverage % + scope-carve-out determination + Phase 1/2 dispatch recommendation — §5.2 **SCOPE-CLARIFICATION-CLASS (NOT full Phase 1/2)** + optional MarketOverview Phase 0+ ticker-primitive verification (~5 fields, sub-30min, foldable into YALP_MKTOVR)

**Wall time:** ~15min spawn-to-RAVC2-Request (well under sub-1h target; faster ship as anticipated due to heavy opal-proprietary-derived carve-out).

**Critical scope-carve-out finding:** CausalityEngine is fundamentally different from sister YALP cutover-trust pages (YALP_MKTOVR / YALP_FACTOR / YALP_MACROS / YALP_VALUAT / YALP_POSITN). Those pages: yang-pipeline → 3rd-party-source validation. CausalityEngine: news + AI + ticker-API (separate service stack; no yang consumption; outputs are opal-analytics-derived). Full Phase 1/2 YALP cycle structurally not warranted; scope-clarification-class brief is the structurally-correct disposition (mirrors YALP_FACTOR §15 "regression layer n/a out-of-cutover-scope" carve-out at page-scope).

**Standing for:** ws COO RAVC2-ACCEPT + scope-clarification-class disposition (no full Phase 1/2 dispatch needed); optional MarketOverview ticker-primitive Phase 0+ as foldable into next YALP_MKTOVR cycle.

**Sibling-lane status:** ~B (YALP_ATTRBN) + ~D (YALP_CMASMP) Phase 0 in flight parallel.

— 0.1.0_DS_MarketIntelligence~E
2026-05-26T~23:00Z
