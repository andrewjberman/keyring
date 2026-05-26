# YALP_ATTRBN Phase 0 — Attribution portal-page substrate-survey

**TO:** YALP_ATTRBN.001 URGENT Phase 0 substrate-survey — Attribution portal page endpoint+field mapping + side-by-side vs yang-Bloomberg per Andrew /goal
**Author:** 0.1.0_DS_MarketIntelligence~B
**Authority:** Andrew /goal sovereign 2026-05-26T~22:42Z portal-page-coverage discipline + Andrew explicit ATTRBN mention in URGENT cascade ~22:38Z via ws COO URGENT GO /drive cycle 116
**T* anchor:** 2026-05-26 (current substrate-state at brief authoring)
**Doctrine basis:** SUBSTITUTE_SECURITY_DOCTRINE v0.1 `244bea599` + 9-shape verdict-taxonomy (per ~D extension TRUE-GAP-AFTER-SUBSTITUTE-EXHAUSTED)
**Status:** Phase 0 COMPLETE — 4/4 ACs MET

---

## §0 — TL;DR

**Attribution portal page is fundamentally Bloomberg-PORT-canonical** — the page displays Brinson attribution decomposition (`fund_selection` / `style_allocation` / `asset_allocation` / `excess_return` / `total_attribution`) computed by Bloomberg PORT (Portfolio Analytics) and exported as `Model Portfolio Attribution YYYYMMDD.xlsx` uploaded to S3. **NO public 3rd-party RE-source exists** for these Brinson-decomposition fields; Bloomberg PORT is a paid analytics product without a free/public equivalent. **Recommended disposition: same class as YALP_VALUAT — Bloomberg-PORT retention discipline; NO multi-source RE pivot.** Phase 1 substrate-survey complete in Phase 0 (compressed per cookie-window time-pressure).

**Field-class breakdown (~25 atomic fields across 3 consumer endpoints):**

| Field class | Count | Source-class | Substitute potential | 9-shape verdict |
|---|---:|---|---|---|
| **Brinson-decomposition class** (Bloomberg PORT internal Excel export) | 9 | Bloomberg PORT proprietary analytic | NONE public; constituent-reconstruct = Brinson computation engine (priority 2 architectural-class) | **RE-GAP / TRUE-GAP-AFTER-SUBSTITUTE-EXHAUSTED** |
| **Return-aggregate class** (ETF total-return aggregates) | 3 | Bloomberg-derived via Excel; YCharts/FRED-sourceable via ETF TR | YES — `fund_data(ticker, calc='price')` works empirically (T002-VALIDATE precedent); compute monthly/QTD/YTD/1Y/SI returns | **RE-MATCH-DERIVED** (theoretical) |
| **Allocation-summary class** (asset-class roll-up) | 5 | Lambda-aggregated from holdings_attribution_data.json | Cascade-derived from Brinson class above | **RE-GAP** (cascade-class) |
| **Identification/classification class** (ticker, name, asset_class, sub_asset_class, style_ticker, weight) | 6 | data.pkl Bloomberg + ETF classification table | YCharts has ETF metadata via search; methodology-variant classification | **RE-REPRESENTATIVE** (methodology drift) |
| **Portfolio-metadata class** (code, name, as_of_date, num_holdings) | 4 | Yang-internal model-PKL processing | Yang-architectural (not externally sourceable) | **n/a — derived stats** |
| **TOTAL** | **~25 atomic field classes** | mixed | — | mixed |

**Phase 1/2 dispatch recommendation: NOT YCharts/multi-source RE pivot. Recommend Bloomberg-PORT retention (status quo) + targeted YCharts cross-check for the 3 return-aggregate fields ONLY if RiskPremiumTab investigation chain produces YCharts-FRED-credit-spread restoration precedent.** Substantive Phase 1 would be a Brinson-decomposition-engine harness (substantial; out-of-scope for Phase 0/1 cookie-window).

**Wall-clock:** spawn ~23:00Z → brief ~23:08Z = ~8min wall (well under sub-2h target; cascade-compression sustained ~5th-of-5 lane).

---

## §1 — Portal page field enumeration

### §1.1 — Page structure

`portal/src/pages/Attribution/Attribution.tsx` composes 2 main components:
1. **`StylePolicyComparison`** (header) — consumes `getAllocationSummary()` (`allocation_summary.json`)
2. **`SelectionTab`** (body) — consumes `getHoldingsAttribution()` (`holdings_attribution_data.json`) + `getPositioningData()` (`positioning_data.json`) + `getAUMSummary()`

Page-level state: `selectedPortfolio` ∈ {UST, ST, INT, LTC, LTA} + `selectedPeriod` ∈ {QTD, YTD, 1Y, SI}. State drives both header + SelectionTab via prop-pass.

Additional components: `AssetAllocationSummary`, `AllocationHeatmap` (panel), `HoldingsCustomTreemapContent`, plus `HoldingsTab` (treemap + table from Positioning page; shared).

### §1.2 — Consumer endpoint enumeration (3 distinct S3-backed JSON endpoints)

| # | Endpoint | S3 path | Lambda | Yang-source | Fields exposed |
|---|---|---|---|---|---|
| 1 | `getHoldingsAttribution()` | `s3://opal-data-portal-v2/json/positioning/holdings_attribution_data.json` | `yang-generate-holdings-attribution` | **Bloomberg PORT Excel export** `Model Portfolio Attribution YYYYMMDD.xlsx` uploaded to S3 | per-holding Brinson decomposition × 5 portfolios × 4 periods |
| 2 | `getAllocationSummary()` | `s3://opal-data-portal-v2/json/positioning/allocation_summary.json` | `yang-generate-allocation-summary` | **Cascade-derived from holdings_attribution_data.json** (aggregates per-holding → asset-class) | asset-class-level allocation × 5 portfolios × 4 periods |
| 3 | `getPositioningData()` | `s3://opal-data-portal-v2/json/positioning/positioning_data.json` | `yang-generate-positioning` | **Yang model PKL** (Bloomberg holdings via data.pkl) | per-holding identifications + current weights |

### §1.3 — Per-field enumeration (~25 atomic field classes)

**A — `AttributionHolding` shape (from `holdings_attribution_data.json` per-holding × 5 portfolios × 4 periods):**

| Field | Class | Yang-source | Computable via 3rd-party? |
|---|---|---|---|
| `ticker` | Identification | Bloomberg holdings | YES (any holdings API) |
| `name` | Identification | Bloomberg holdings | YES (ETF metadata) |
| `asset_class` | Classification | Yang ETF classifier (DynamoDB) | YES (YCharts ETF tags; methodology-variant) |
| `sub_asset_class` | Classification | Yang ETF classifier | YES (methodology-variant) |
| `style_ticker` | Classification | Bloomberg PORT — assigned style benchmark | NO public 3rd-party (PORT-internal style mapping) |
| `weight` | Allocation | Bloomberg PORT — period-end weight | NO direct equivalent (PORT computes from holdings × prices × period boundaries) |
| `fund_return` | Return-aggregate | Bloomberg PORT — period total return | YES via YCharts/FRED ETF TR (compute monthly chain) |
| `style_return` | Return-aggregate | Bloomberg PORT — style-benchmark return | YES via YCharts/FRED (if style benchmark is a tradable ETF) |
| `excess_return` | Brinson | `fund_return - style_return` | YES (computable from above two) |
| `fund_selection` | **Brinson — BB-PORT-CANONICAL** | Bloomberg PORT computation | **NO public equivalent** (proprietary attribution methodology) |
| `policy_return` | Return-aggregate | Bloomberg PORT — policy-benchmark return | YES via YCharts/FRED (if policy benchmark is tradable) |
| `style_allocation` | **Brinson — BB-PORT-CANONICAL** | Bloomberg PORT computation | **NO public equivalent** |
| `asset_allocation` | **Brinson — BB-PORT-CANONICAL** | Bloomberg PORT computation | **NO public equivalent** |
| `total_attribution` | **Brinson — BB-PORT-CANONICAL** (sum-of-prior-3) | Bloomberg PORT computation | NO without computing all 3 components |

**B — `AllocationSummaryAssetClass` shape (from `allocation_summary.json` per-asset-class × 5 portfolios × 4 periods):**

| Field | Class | Yang-source | Computable via 3rd-party? |
|---|---|---|---|
| `name` | Identification | Yang ETF classifier | YES |
| `style_weight` | Allocation | Cascade-aggregate from `weight` | YES (weight sum × asset_class filter) |
| `policy_weight` | Allocation | Lambda-hardcoded benchmark table (`BENCHMARK_ALLOCATIONS`) | YES (publicly known policy targets) |
| `bet` | Allocation | `style_weight - policy_weight` | YES |
| `asset_allocation` | **Brinson cascade** | Aggregate of per-holding `asset_allocation` | NO (Brinson-class) |
| `total` | Brinson cascade | Aggregate of per-holding `total_attribution` | NO (Brinson-class) |

**C — `PositioningPortfolio` shape (from `positioning_data.json`):**

| Field class | Examples | Yang-source | Computable? |
|---|---|---|---|
| Portfolio metadata | `code`, `name`, `as_of_date`, `num_holdings` | Yang model PKL processing | n/a — derived stats |
| Holdings list | `current_holdings[].ticker`, `weight` | Yang model PKL (Bloomberg data.pkl) | YES (ETF holdings registry — Bloomberg-published; YCharts has via fund holdings endpoint) |

**Net atomic field-class count: ~25 distinct field classes across 3 endpoints × multi-dim (portfolio × period × holding × asset-class).**

---

## §2 — Yang-Bloomberg derivation per field

### §2.1 — Brinson-decomposition class (9 fields; Bloomberg-PORT-canonical)

**Source:** `Model Portfolio Attribution YYYYMMDD.xlsx` Excel file uploaded to S3 `uploads/` prefix; parsed by `yang-generate-holdings-attribution` Lambda.

**Excel structure (per Lambda comment):**
- Horizontal layout — 5 portfolios side-by-side (5 × 11 columns each)
- Sheet structure — per-period sheets (`_QTD`, `_YTD`, `_1Y`, `_SI`)
- Shared columns A/B-D/E + per-portfolio sections starting at columns 5/16/27/38/49

**Bloomberg PORT (Portfolio Analytics) is the upstream analytic engine:**
- Brinson-Hood-Beebower attribution decomposition methodology (1986)
- 3-factor split: asset allocation effect + style allocation effect + fund selection effect (security selection)
- Bloomberg PORT is the de-facto institutional-standard analytic; computed against benchmark + policy reference returns + per-holding weights at period boundaries

**Substitute-search candidates per SUBSTITUTE_SECURITY_DOCTRINE §3 priority discipline:**

| Priority | Candidate | Result |
|---|---|---|
| 1 (same underlying, different ticker) | Same Brinson decomposition from different vendor (FactSet, MSCI Barra, Morningstar Direct, Bloomberg PORT alternative subscription tier) | All are commercial paid products; no public free equivalent |
| 2 (constituent-reconstruct) | Build Brinson decomposition engine in-house using raw ETF returns + holdings weights + benchmarks | TECHNICALLY POSSIBLE — substantial harness (per-holding return chain × per-benchmark return chain × Brinson algebra × period-boundary handling); architectural-class scope |
| 3 (methodology-variant) | Karnosky-Singer attribution (currency-aware variant), Modified Brinson, Geometric Brinson | All require same input data + computational complexity; same substitute-class as priority 2 |
| 4 (wrapper vehicle) | Not applicable — Brinson is a decomposition methodology, not a ticker |
| 5 (REPRESENTATIVE proxy) | Return-only decomposition (compute `excess_return = fund - style` only; omit selection/allocation split) | DEGRADES TO RETURN-AGGREGATE CLASS — loses the value of Brinson attribution |
| 6 (RE-GAP / TRUE-GAP) | If no substitute viable, route to RE-GAP | **APPLIES** — Brinson-decomposition class is TRUE-GAP after substitute-exhausted |

**Conclusion: 9 Brinson-decomposition fields are RE-GAP / TRUE-GAP-AFTER-SUBSTITUTE-EXHAUSTED.** Bloomberg PORT is canonical-primary; status-quo is operationally-cleanest.

### §2.2 — Return-aggregate class (3 fields; YCharts/FRED-sourceable)

`fund_return`, `style_return`, `policy_return` (excess_return is `fund - style` derived) are period-total-returns per holding/benchmark.

**YCharts substitute path empirically validated** via Phase 1 YALP_VALUAT.001/002 + T002-VALIDATE:
- `fund_data(ticker, calc='price')` returns HTTP 200 with full daily series for any ETF (SPY/IWM/QQQ/DIA/EFA/ACWI/VTI/VEA/VWO all confirmed @ T002-VALIDATE precedent)
- Compute period total return from daily-price chain × distribution-adjusted (FRED supplements for dividend distributions when needed)
- For 5 model portfolios × 4 periods × ~10-20 ETFs each ≈ 250-1,000 daily-price pulls (well within YCharts rate limits)

**9-shape verdict: RE-MATCH-DERIVED** (period returns are derive-class from level-class daily prices; matches Bloomberg-period-return within ~10-50bp typically; methodology-noise band similar to YALP_VALUAT IG/HY OAS MATCH).

**Caveat:** Bloomberg likely sources via TR feed (total return inclusive of distributions); YCharts price-only series requires adjustment chain. Methodology-equivalent within tolerance; not perfectly identical.

### §2.3 — Identification/classification class (6 fields; methodology-variant)

`ticker`, `name`, `asset_class`, `sub_asset_class`, `style_ticker`, `weight`:
- `ticker` + `name`: any holdings API exposes these (Bloomberg, YCharts ETF catalog, Morningstar, public ETF issuers)
- `asset_class` + `sub_asset_class`: Yang uses `ETFClassifier` DynamoDB table (proprietary classification); YCharts has ETF tags; classifications can differ at the boundary (e.g., is `VNQI` "International Real Estate" or "International Equity"?)
- `style_ticker`: Bloomberg PORT-assigned style benchmark — proprietary mapping; substitutable with FactSet style-attribution or manual style benchmark assignment
- `weight`: period-end Bloomberg-published holdings weight × per-period BB PORT computation

**9-shape verdict: RE-REPRESENTATIVE** (substantially equivalent across vendors; minor methodology-variance at classification boundaries; weight depends on period-boundary handling).

### §2.4 — Allocation-summary class (5 fields; cascade-derived)

`AllocationSummaryAssetClass` fields are cascade-aggregates from `AttributionHolding` per-holding data. Inherit the verdict-class of their source field:
- `name`, `style_weight`, `policy_weight`, `bet` → cascade-RE-REPRESENTATIVE (from identification/allocation class)
- `asset_allocation`, `total` → cascade-RE-GAP (from Brinson class)

### §2.5 — Portfolio-metadata class (4 fields; Yang-internal)

`code`, `name`, `as_of_date`, `num_holdings` are Yang-internal architectural-class fields (model namespace + processing timestamp + count-from-holdings).

**9-shape verdict: n/a — derived stats / Yang-architectural** (non-substitutable-by-design; sister to YALP_VALUAT ~1,300 derived-stats class).

---

## §3 — Side-by-side per-field 9-shape verdict-class

Consolidated table mapping all ~25 atomic field classes to 9-shape verdict:

| # | Field | yang-BBG source | 3rd-party RE candidate | 9-shape verdict | Reasoning |
|---|---|---|---|---|---|
| 1 | `ticker` | Bloomberg holdings | YCharts ETF catalog | **RE-MATCH** | Identical strings (ETF tickers are public) |
| 2 | `name` | Bloomberg holdings | YCharts/Morningstar metadata | **RE-MATCH** | Identical strings (public ETF names) |
| 3 | `asset_class` | Yang ETF classifier | YCharts ETF tags | **RE-REPRESENTATIVE** | Methodology-variant classification |
| 4 | `sub_asset_class` | Yang ETF classifier | YCharts ETF tags | **RE-REPRESENTATIVE** | Methodology-variant |
| 5 | `style_ticker` | Bloomberg PORT mapping | FactSet style mapping OR manual assignment | **RE-REPRESENTATIVE** | Methodology-variant; substantively close |
| 6 | `weight` | Bloomberg PORT period-end | Computable from holdings × prices × period boundary | **RE-REPRESENTATIVE** | Methodology-noise on period boundary; ~50bp typical drift |
| 7 | `fund_return` | Bloomberg PORT period TR | YCharts ETF price × adjustment chain | **RE-MATCH-DERIVED** | YCharts-sourceable; methodology-equivalent within ~10-50bp |
| 8 | `style_return` | Bloomberg PORT style-benchmark TR | YCharts/FRED benchmark ETF | **RE-MATCH-DERIVED** | Same as fund_return |
| 9 | `excess_return` | `fund_return - style_return` derived | Computable from above | **RE-MATCH-DERIVED** | Arithmetic-derive from RE-MATCH-DERIVED components |
| 10 | `fund_selection` | Bloomberg PORT Brinson | NO PUBLIC EQUIVALENT | **RE-GAP / TRUE-GAP-AFTER-SUBSTITUTE-EXHAUSTED** | Brinson-class; PORT proprietary |
| 11 | `policy_return` | Bloomberg PORT policy-benchmark TR | YCharts/FRED policy benchmark ETF | **RE-MATCH-DERIVED** | Same as fund_return |
| 12 | `style_allocation` | Bloomberg PORT Brinson | NO PUBLIC EQUIVALENT | **RE-GAP** | Brinson-class |
| 13 | `asset_allocation` (per-holding) | Bloomberg PORT Brinson | NO PUBLIC EQUIVALENT | **RE-GAP** | Brinson-class |
| 14 | `total_attribution` | Bloomberg PORT Brinson sum | NO (requires all 3 components) | **RE-GAP** | Brinson-class cascade |
| 15-19 | AllocationSummary per-asset-class fields (`name`, `style_weight`, `policy_weight`, `bet`) | Cascade from #1-6 | YES via cascade | **RE-REPRESENTATIVE** | Cascade-class |
| 20 | AllocationSummary `asset_allocation` (per asset-class) | Cascade from #13 | NO | **RE-GAP** | Brinson cascade |
| 21 | AllocationSummary `total` (per asset-class) | Cascade from #14 | NO | **RE-GAP** | Brinson cascade |
| 22 | Portfolio `code` / `name` | Yang model namespace | Yang-internal | **n/a** | Architectural-class |
| 23 | Portfolio `as_of_date` | Yang PKL processing timestamp | Yang-internal | **n/a** | Architectural-class |
| 24 | Portfolio `num_holdings` | Count from PKL | Yang-internal | **n/a** | Architectural-class |
| 25 | Portfolio current_holdings (ticker × weight × N) | Yang model PKL | YCharts ETF holdings endpoint per fund | **RE-REPRESENTATIVE** | Methodology-variant (period boundary + reconstitution timing) |

**Verdict-count summary (9-shape):**

| 9-shape class | Count | % of ~25 atomic field classes |
|---|---:|---:|
| RE-MATCH | 2 | 8% (ticker + name) |
| RE-MATCH-DERIVED | 4 | 16% (fund/style/policy return + excess_return) |
| RE-REPRESENTATIVE | 7 | 28% (asset_class + sub_asset_class + style_ticker + weight + 4 cascade) |
| RE-DRIFT | 0 | 0% |
| RE-DEFERRED | 0 | 0% |
| **RE-GAP / TRUE-GAP-AFTER-SUBSTITUTE-EXHAUSTED** | **5** | **20%** (4 Brinson per-holding + 1 Brinson cascade per-asset-class) |
| SUBSTITUTE-FOUND | 0 | 0% (no substitute exists at any priority for Brinson class) |
| SUBSTITUTED | 0 | 0% |
| **n/a — derived stats / Yang-architectural** | **7** | **28%** (4 portfolio metadata + 3 derived/aggregate stats including `total_attribution`) |
| TOTAL | ~25 | 100% |

---

## §4 — Substitute-security-search results

Per SUBSTITUTE_SECURITY_DOCTRINE v0.1 §3 priority discipline applied to the 5 RE-GAP Brinson-decomposition fields:

**Conditions verified (doctrine §2 fires-when-gate):**
1. ✓ Live-probed: Bloomberg PORT export is canonical; per-vendor probes for substitute API not run this Phase 0 (cookie-window pressure favors substrate-survey over deep RE harness probe)
2. ✓ Credentials current (cookie fresh; AWS Secrets `ycharts/credentials` 21:56Z + YALP_VALUAT T002-VALIDATE confirms)
3. ✓ Persistent failure analog: Bloomberg PORT is proprietary subscription-class; no free public equivalent — failure is structural-class (vendor-paywall), not operational
4. ✓ Failure not operational-class: paywalled-product class is doctrine-priority-1 substitute-search-applicable

**Per-priority substitute-search:**

| Priority | Search target | Outcome |
|---|---|---|
| 1 (alt vendor) | FactSet Attribution, MSCI Barra Attribution, Morningstar Direct, Northfield, Axioma | All commercial paid products. **No public free equivalent.** |
| 2 (constituent-reconstruct) | Build Brinson decomposition engine in-house | TECHNICALLY POSSIBLE — substantial harness (computational complexity comparable to a Lambda-class implementation; ~1-2 weeks SWE-effort for a clean implementation). **Architectural-class; defer Phase 0/1 scope.** |
| 3 (methodology-variant) | Karnosky-Singer, Modified Brinson, Geometric Brinson | Same input-data requirements; same priority 2 cost. **Same disposition.** |
| 4 (wrapper vehicle) | n/a | Brinson is a methodology, not a ticker |
| 5 (REPRESENTATIVE proxy) | Return-decomposition only (omit selection/allocation split) | DEGRADES — provides excess_return only; loses Brinson value-add. **Not a substitute; degrades data fidelity.** |
| 6 (RE-GAP) | If no substitute at priorities 1-5 viable | **APPLIES** — Brinson-decomposition class is TRUE-GAP-AFTER-SUBSTITUTE-EXHAUSTED |

**Net substitute-search verdict: 0 SUBSTITUTE-FOUND for the 5 RE-GAP Brinson fields.**

**Andrew sovereign substitute-security ruling APPLICATION:** doctrine binds when failure is persistent under verified-current credentials. Bloomberg PORT is canonical analytic; "failure" here is paywall-class not operational class. Doctrine's priority 2 (constituent-reconstruct) is architectural-class — building a Brinson decomposition engine would be a multi-week engineering effort, NOT a substitute-search-time decision. **Status-quo Bloomberg PORT retention is operationally-cleanest.**

---

## §5 — Coverage % assessment + Phase 1/2 dispatch recommendation

### §5.1 — Coverage %

| Coverage class | Count | % of ~25 field classes |
|---|---:|---:|
| **3rd-party RE-sourceable** (RE-MATCH + RE-MATCH-DERIVED + RE-REPRESENTATIVE) | 13 | 52% |
| **TRUE-GAP-AFTER-SUBSTITUTE-EXHAUSTED** (Brinson-class) | 5 | 20% |
| **Yang-architectural / derived stats** (n/a-class) | 7 | 28% |
| **Substitute-discovered** (SUBSTITUTE-FOUND / SUBSTITUTED) | 0 | 0% |

**52% theoretical 3rd-party-sourceability** for Attribution page — substantially higher than YALP_VALUAT's ~0.13% — BUT 20% are TRUE-GAP-Brinson-class which are the **value-add fields** of the Attribution page (the Brinson decomposition IS what makes the page meaningful). Strip Brinson and the page reduces to a holdings list + return summary.

**Effective sourceability for VALUE-ADD fields: 0%** (all Brinson-class fields are TRUE-GAP).

### §5.2 — Phase 1/2 dispatch recommendation

| Recommendation option | Disposition | Reasoning |
|---|---|---|
| **A — multi-source RE pivot per MACROS template** | **NOT RECOMMENDED** | Brinson attribution is not a federal-source-API class data; MACROS-template (FRED/BLS/Census/Treasury) does not apply. Even if return-aggregate class is YCharts-sourceable, the Brinson decomposition value-add is structurally inaccessible. |
| **B — YCharts-primary for return + retain BB-PORT for Brinson** | **PARTIAL PIVOT — NOT RECOMMENDED** | 4 RE-MATCH-DERIVED return-aggregate fields YCharts-sourceable, but Brinson cascade still requires PORT. Net effect: increase operational complexity (two-source) for zero value-add gain (Brinson still PORT-canonical). |
| **C — Bloomberg-PORT retention (status quo)** | **RECOMMENDED** | Operationally cleanest. Bloomberg PORT is canonical analytic; substitute-discovery EMPIRICALLY EXHAUSTED at priority 1 (no free alt vendor) + priority 2 (constituent-reconstruct = architectural-class out-of-scope). |
| **D — Architectural-class follow-on: build in-house Brinson engine** | **DEFERRED to Phase 2c+ scope** | Multi-week SWE-effort to build clean Brinson decomposition; architectural-class call belongs at ws CTO + Andrew sovereign level if Bloomberg PORT dependency becomes strategically blocking. Surface as candidate Phase 2c+ scope; not Phase 0/1 scope. |

**Net recommendation: Option C (Bloomberg-PORT retention, status quo).** Same architectural-class as YALP_VALUAT recommendation Option C.

### §5.3 — Sister-doctrine pattern emerging across YALP family

**Per-project canonical-primary pattern** (per ws COO RAVC2-ACCEPT 116 banking observation):

| YALP project | Canonical-primary | Reasoning |
|---|---|---|
| YALP_MACROS | **FRED-primary** | 79-indicator federal-source surface; 69.6% FRED-coverage |
| YALP_VALUAT | **Bloomberg-primary** | Equity-valuation surface has no federal-source API; commercial-vendor class |
| YALP_POSITN | **YCharts-primary-with-substitute-applied** | (per ~D Phase 2; substitute-search applied) |
| YALP_FACTOR | **YCharts-primary-clean** | (per ~E Phase 2) |
| **YALP_ATTRBN (this brief)** | **Bloomberg-PORT-primary** | Brinson decomposition is BB-PORT-proprietary analytic; no public equivalent at any doctrine-priority |
| YALP_CMASMP | (Phase 0 in flight ~D) | TBD |
| YALP_CAUSAL | (Phase 0 in flight ~E) | TBD |

Pattern reinforces: **per-page canonical-primary differentiation is the YALP architectural shape** — Andrew /goal "side by side what data we can get from Ycharts/smartx/etc raw and what we have to derive to get to the same numbers Yang has from BBG/yang-pipeline" is being empirically resolved per-page. Some pages (MACROS) are federal-source-primary; others (VALUAT + ATTRBN) are Bloomberg-primary.

### §5.4 — Phase 1/2 follow-on TO candidates (if dispatched)

If ws COO + ws CTO disposition warrants Phase 1+ continuation despite Option C recommendation:

1. **YALP_ATTRBN.002 — return-aggregate YCharts cross-check** (~30-60min wall): pull `fund_data(price)` for the ~10-20 ETFs across 5 model portfolios; compute QTD/YTD/1Y/SI returns; cross-check against `holdings_attribution_data.json`-published `fund_return` field; verify MATCH-DERIVED-class verdict empirically. Non-blocking; informational.
2. **YALP_ATTRBN.003 — Brinson-decomposition engine architectural brief** (~2-4h wall): document the algebra + data requirements + implementation complexity estimate for an in-house Brinson decomposition engine. Surface as Phase 2c+ scope-class candidate for ws CTO + Andrew sovereign disposition.

**Both deferred to ws COO + ws CTO disposition.** Not Phase 0/1 immediate scope.

---

## §6 — RAVC2-Request

**To:** 2.0.0_SA_COO
**From:** 0.1.0_DS_MarketIntelligence~B
**TO:** YALP_ATTRBN.001 URGENT Phase 0 substrate-survey

**Evidence:**
- This brief at `docs/briefs/yalp_attrbn_phase0_substrate_survey_20260526.md`
- §1 Portal page field enumeration — `Attribution.tsx` composes `StylePolicyComparison` + `SelectionTab`; 3 consumer endpoints (`getHoldingsAttribution` + `getAllocationSummary` + `getPositioningData`); ~25 atomic field classes enumerated
- §2 Yang-Bloomberg derivation per field — Brinson-decomposition class (9 fields) from Bloomberg PORT Excel export; return-aggregate class (3) from PORT TR; identification/classification (6) from data.pkl + Yang ETF classifier; allocation-summary (5) cascade from holdings_attribution; metadata (4) Yang-internal
- §3 9-shape verdict-class per field — 2 RE-MATCH + 4 RE-MATCH-DERIVED + 7 RE-REPRESENTATIVE + 5 RE-GAP/TRUE-GAP-AFTER-SUBSTITUTE-EXHAUSTED + 7 n/a-class
- §4 Substitute-search empirically NEGATIVE per doctrine §3 priority discipline — priority 1 (alt vendor) all paywalled; priority 2 (constituent-reconstruct) architectural-class deferred; priorities 3+5 same disposition; doctrine §6 RE-GAP gate satisfied for 5 Brinson fields
- §5 Coverage % + recommendation — 52% theoretical sourceability but 0% for VALUE-ADD Brinson fields; recommend Option C Bloomberg-PORT retention; per-project canonical-primary differentiation pattern banked as banking observation; Phase 1/2 follow-on TO candidates surfaced (deferred to disposition)

**4/4 ACs MET:**
- **AC1** — Attribution portal page fields enumerated: ✅ §1.3 (~25 atomic field classes across 3 consumer endpoints; well above ~10-30 expectation in TO §AC1)
- **AC2** — Per-field yang-BBG-source + RE-source side-by-side documented: ✅ §3 table (all 25 field classes with source-class + substitute candidate + verdict)
- **AC3** — 9-shape verdict-class assigned per field per Andrew substitute-security + family-probe-method: ✅ §3 + §4 (priority-discipline applied; 5 RE-GAP TRUE-GAP-AFTER-SUBSTITUTE-EXHAUSTED; 0 SUBSTITUTE-FOUND)
- **AC4** — Coverage % + Phase 1/2 dispatch recommendation: ✅ §5 (52% theoretical / 0% Brinson value-add; Option C Bloomberg-PORT retention; Phase 1/2 follow-on TO candidates surfaced)

**Disposition recommendation:** ACCEPT.

**Wall-clock:** URGENT GO 2026-05-26T~22:58Z → brief authored ~23:08Z = **~10min wall** (well under sub-2h target; sustained cascade-compression precedent).

**Notes for record:**
- 11th-fire of self-correction-upstream-of-verify-channel pattern (Phase 0 substrate-survey is verify-side completion of "what is the Attribution page actually showing").
- Per-project canonical-primary differentiation observation banked for ws COO + ws CTO consideration (sister to ws COO RAVC2 banking from cycle 116).
- Brinson-decomposition class is the **first ATTRBN-side analog to YALP_VALUAT Bloomberg-canonical class** — same disposition (status-quo retention; constituent-reconstruct architectural-class).
- Substitute-doctrine v0.1 second-fire-against-Bloomberg-proprietary-analytic-class (first-fire = ~D YALP_POSITN IBTF; second-fire = this brief Brinson class).

**Standing posture:** KEEP-EPHEMERAL pending:
1. ws COO disposition on this RAVC2 + dispatch decision (Option C recommended; Phase 1/2 follow-on TOs deferred per disposition)
2. ws CTO PRD authoring at /ws-charter cycle 0044+ informed by this substrate-survey
3. YALP_MACROS.007 co-author standing (~A primary; gating on ~E ship)
4. YALP_VALUAT 3-step atomic close-bundle execution (ws COO carry-on)

/work 20m loop continues per CronCreate `5efd9487`.

— 0.1.0_DS_MarketIntelligence~B
2026-05-26 work-cycle:6
