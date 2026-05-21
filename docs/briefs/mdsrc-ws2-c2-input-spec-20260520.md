# YALP_MDSRC.C3 — WS-2 Hybrid-Surface Input-Series Spec (C2 build-input)

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` |
| Task Order | `YALP_MDSRC.C3` — WS-2 hybrid-surface input-series spec |
| Author | `0.2.0_DS_PortfolioAnalytics` |
| Date | 2026-05-20 |
| Audience | `2.0.0_SA_COO` (RAVC2) — CC `1.0.0_SA_CTO`; consumed by `YALP_MDSRC.C2` |
| Status | COMPLETE — audit/spec deliverable; no code change |
| Companion data | `mdsrc-ws2-c2-input-spec-20260520.tsv` — the machine-readable consolidated input-series table |

---

## 1. Purpose

C3 pre-stages the **input-series requirements** for the WS-2 hybrid surfaces so that, when
A3's YCharts internal-API mapping lands, C2's build starts from a finished requirements list
rather than serializing a fresh enumeration. C3 is the **requirement side** (what input each
yang generator consumes); A3 is the **endpoint side** (where it comes from on the YCharts
internal API); they meet at C2.

Scope: the 6 WS-2 hybrid surfaces — `correlation`, factor spreads `FT-02`/`FT-03`, and the
Model Portfolios benchmark legs `MP-01`/`MP-02`/`MP-03`. A3-independent and Q1-independent —
this enumerates what the generators **already** consume.

---

## 2. Method

| Step | Result |
|---|---|
| `comp-pipescript io` on the 3 generators | All three (`yang-generate-correlation`, `yang-generate-factor-tilts`, `yang-model-portfolio-benchmarks`) returned **"Unknown script" — not comp-graph nodes** (consistent with PRD §5: the yang generators are off the comp-pipescript graph). `<if_mismatch>` fallback taken — direct source read. |
| Source read | All 3 generator `lambda_function.py` read in full — input keys, filters, the index/security lists, cadence, units. |
| Crosswalk cross-reference | Each input series matched to `docs/briefs/mdsrc-ycharts-ticker-map-20260520.csv` (the dc01d4b8a 71-row crosswalk: `portal_name -> bbg_ticker`, `ycharts_symbol_draft` still pending A3). |

**Join key (coordinated with 0.1.0_DS / A3):** each input series is keyed on its
**`portal_name`** (the `index_name` string the yang generator consumes) and carries the
crosswalk **`bbg_ticker`** as the stable cross-reference. The `ycharts_symbol` column is
A3's to fill — C3 marks each row known / pending-A3.

---

## 3. Per-surface input-series requirements

### 3.1 Correlation (`yang-generate-correlation` -> `json/correlations/correlation_data.json`)

**Input:** `data.pkl -> return_monthly` DataFrame; the generator filters `index_name` to a
hard-coded **63-index** list (`MARKET_OVERVIEW_INDICES`), reads the `return` column per
`index_name` per `date`. **Cadence: monthly. Units: monthly total return (decimal/percent
per the pivot).** Feeds the pairwise Pearson correlation matrices for 5 periods
(1M/3M/6M/1Y/2Y — windowed as 21/63/126/252/504 *of the monthly rows*).

The 63 indices are the input series. **59 of 63 map cleanly** to the crosswalk by
`portal_name`. **4 are flagged** (not in the dc01d4b8a crosswalk, or ambiguous):

| Correlation input | Issue | Action |
|---|---|---|
| `Bloomberg US Treasury` | No crosswalk row | A3 lookup + crosswalk extension |
| `Bloomberg 1-3 Year Treasury` | Crosswalk has `Bloomberg 1-3 Year Gov/Credit` (a *different* index — Gov/Credit, not Treasury) | A3 lookup; do NOT silently map to Gov/Credit |
| `Bloomberg 7-10 Year Treasury` | No crosswalk row | A3 lookup + crosswalk extension |
| `Crude Oil` | Crosswalk has `Crude Oil Brent` (`CO1 Comdty`) AND `Crude Oil WTI` (`CL1 Comdty`) — generator uses bare `Crude Oil` | Resolve which variant the `return_monthly` series is (likely WTI); A3/Yang-source confirm |

The other 59 (`S&P 500`, `MSCI *`, `Russell *`, the 11 GICS sectors, `Bloomberg Aggregate /
US Corporate / High Yield / Municipal / 20+ Year Treasury`, `Gold / Silver / Natural Gas /
Copper`, etc.) all have a crosswalk `bbg_ticker`; their `ycharts_symbol` is pending A3.

> Note on entity scope: correlation reads **indices only** (the 63-name list), all monthly.
> No ETF or per-security input. The full 63-row enumeration is in the companion TSV.

### 3.2 Factor Spreads — FT-02 / FT-03 (`yang-generate-factor-tilts`)

**Input:** `model.pkl` — keys `summary`, `factor_spread`, `regression`. FT-02
(`tier2-spreads.json`) and FT-03 (`tier3-timeseries.json` — the `timeSeries` block) are both
driven by the **`factor_spread` DataFrame**: 6 named columns, one per Opal factor pair.
**Cadence: daily** (the generator slices `.tail(504)` trading days). **Units: factor-spread
value (decimal).**

| FT factor-spread column | Likely constituent legs (INFERENCE — see flag) |
|---|---|
| `Equity vs FI` | an equity index minus a fixed-income index (e.g. MSCI ACWI / S&P 500 vs Bloomberg Aggregate) |
| `Growth vs Value` | Growth index minus Value index (e.g. Russell 1000 Growth vs Russell 1000 Value) |
| `US vs Foreign` | US index minus ex-US index (e.g. MSCI USA vs MSCI ACWI ex US / EAFE) |
| `Large vs Small` | large-cap minus small-cap (e.g. Russell 1000 vs Russell 2000) |
| `Agg vs Short` | aggregate-duration minus short-duration bond index |
| `HY vs Agg` | high-yield minus aggregate bond index |

**CRITICAL FLAG for C2:** `factor_spread` is a **pre-computed** series in `model.pkl` — the
generator consumes the finished spread, it does **not** expose the constituent index of each
leg. The constituent-leg table above is **inference from the factor names, not confirmed by
the generator.** To source FT-02/FT-03 from the YCharts internal API, C2 needs the **exact
index pair behind each of the 6 spreads** — and that definition lives in **Yang's upstream
factor-construction workflow**, not in any yang Lambda. **C3 cannot enumerate the FT-02/03
input to ticker level from the generator alone — this requires a Yang-source consult** (or A3
recovering it from a YCharts factor endpoint, if one exists). FT-02/03 are recorded in the
companion TSV as `requirement=6 factor-spread series`, `constituent_legs=PENDING Yang-source`.

(FT-01 `tier1-snapshot.json` — the regression snapshot — is `proprietary` per the WS-2 audit,
not a hybrid surface, and is out of C3 scope.)

### 3.3 Model Portfolios benchmark legs — MP-01 / MP-02 / MP-03 (`yang-model-portfolio-benchmarks`)

**Input:** `data.pkl -> return_daily`, filtered to `index_name` containing `"Term"` +
`data.pkl -> price_monthly` for the risk-free rate. **Cadence: daily** (returns) / **monthly**
(rfr, forward-filled). The generator consumes **pre-blended** benchmark series; the blend
weights are documented in the generator's own `INDEX_COMPOSITIONS` / `ETF_COMPOSITIONS` dicts.

The **WS-2 (benchmark) leg** of MP-01 (`benchmark_returns.json`), MP-02
(`model_portfolio_benchmarks.json`), MP-03 (`model_portfolio_timeseries.json`) consumes three
input families (the `model` return leg is WS-3, not C3 scope):

**(a) Index-benchmark blends** — generator reads pre-blended `{Model} Term Benchmark` series;
C2 reconstruction path = pull the **3 distinct constituent indices** from YCharts and re-blend
per the documented weights:

| Constituent index | Used in blend | Crosswalk bbg_ticker | YCharts |
|---|---|---|---|
| `Bloomberg 0-1 Year Treasury` | UST (100%) | `I22917US Index` | pending A3 |
| `Bloomberg Aggregate` | ST 85% / INT 40% / LTC 15% / LTA 15% | `LBUSTRUU Index` | pending A3 |
| `MSCI ACWI` | ST 15% / INT 60% / LTC 85% / LTA 85% | `MXWD Index` | pending A3 |

**(b) ETF-benchmark blends** — generator reads pre-blended `{Model} Term ETF` series; C2
reconstruction path = pull the **3 constituent ETFs** and re-blend:

| Constituent ETF | Used in blend | YCharts |
|---|---|---|
| `VGSH` (Vanguard Short-Term Treasury ETF) | UST (100%) | ETF ticker — direct YCharts lookup; not in the index crosswalk |
| `AGG` (iShares Core US Aggregate Bond ETF) | ST 85% / INT 40% / LTC 15% / LTA 15% | ETF ticker — direct YCharts lookup |
| `ACWI` (iShares MSCI ACWI ETF) | ST 15% / INT 60% / LTC 85% / LTA 85% | ETF ticker — direct YCharts lookup |

**(c) Risk-free rate** — `price_monthly` Treasury yields, **3 tenors**: `1Y` (UST/ST),
`5Y` (INT), `10Y` (LTC/LTA). Data class YIELD; monthly, forward-filled to daily. These are
WS-1-domain market-data series — flag the cross-domain handoff to WS-1's crosswalk; C2 pulls
them as YIELD series.

**Blend weights (for C2 re-blend) — from the generator's own constants:**
```
INDEX:  UST 100% Bloomberg 0-1Y Treasury | ST 85% Agg / 15% ACWI | INT 40% Agg / 60% ACWI |
        LTC 15% Agg / 85% ACWI | LTA 15% Agg / 85% ACWI
ETF:    UST 100% VGSH | ST 85% AGG / 15% ACWI | INT 40% AGG / 60% ACWI |
        LTC 15% AGG / 85% ACWI | LTA 15% AGG / 85% ACWI
RFR:    UST 1Y | ST 1Y | INT 5Y | LTC 10Y | LTA 10Y
```

**Net MP-01/02/03 distinct input series: 3 indices + 3 ETFs + 3 RFR tenors = 9** (plus the
WS-3 model-return leg, out of scope). All 9 are public market data — the cleanest C2 targets
in the WS-2 hybrid set.

---

## 4. Consolidated requirements summary

| Surface | Generator | Input families | Distinct input series | Crosswalk-mapped | Flagged for A3 / Yang-source |
|---|---|---|---|---|---|
| Correlation | yang-generate-correlation | `return_monthly` indices | 63 indices (monthly) | 59 | 4 (3 Treasury gaps + Crude Oil ambiguity) |
| FT-02 / FT-03 | yang-generate-factor-tilts | `model.pkl factor_spread` | 6 factor-spread series (daily) | 0 — pre-computed | 6 — constituent index pairs need a Yang-source consult |
| MP-01 / MP-02 / MP-03 | yang-model-portfolio-benchmarks | index blends + ETF blends + RFR | 9 (3 idx + 3 ETF + 3 RFR tenor) | 3 indices in crosswalk; 3 ETFs direct; 3 RFR = WS-1 YIELD | 0 hard gaps; ETF + RFR are non-index lookups |

Full row-level enumeration: companion TSV `mdsrc-ws2-c2-input-spec-20260520.tsv`.

**Three findings C2 / A3 must carry:**
1. **Correlation has 3 genuine crosswalk gaps** — `Bloomberg US Treasury`,
   `Bloomberg 1-3 Year Treasury`, `Bloomberg 7-10 Year Treasury` are not in the dc01d4b8a
   crosswalk; `Bloomberg 1-3 Year Treasury` must NOT be silently mapped to the crosswalk's
   `Bloomberg 1-3 Year Gov/Credit` (different index). The crosswalk needs 3 added rows.
2. **FT-02/03 cannot be ticker-enumerated from the yang generator** — `factor_spread` is
   pre-computed in `model.pkl`. C2's YCharts pull for the factor spreads is **blocked on a
   Yang-source consult** (or an A3 finding) that gives the exact index pair behind each of
   the 6 Opal factor spreads. This is the one WS-2 hybrid surface C3 cannot fully spec from
   the generators — flagged explicitly so C2 is not surprised.
3. **MP-01/02/03 is the cleanest C2 target** — 9 public series (3 indices crosswalk-mapped,
   3 ETFs direct, 3 RFR tenors), with the re-blend weights already in the generator source.
   C2 pulls constituents + re-blends; no proprietary dependency on the benchmark leg.

---

## 5. Compiler Tools

| Phase | `<run>` | Result | vs `<expect>` |
|---|---|---|---|
| 1 | `comp-pipescript io yang-generate-correlation / yang-generate-factor-tilts / yang-model-portfolio-benchmarks` | All 3 = "Unknown script — not a comp-graph node" | `<if_mismatch>` fallback — direct source read of all 3 generators, documented (§2, §3) |
| 2 | none (spec doc, no code) | No `.py` authored | MATCH — documented-none |
| 3 | none (the per-surface table is self-validation) | §3/§4 + companion TSV checked vs AC1-AC3 | MATCH — documented-none |

`comp-pipescript` runs auto-logged to `org/compiler-tools-log.md` via `.comp-graph/.agent_context`
(TO_ID `YALP_MDSRC.C3`).

---

## 6. Handoff

- **To C2** (`YALP_MDSRC.C2`, 0.1.0_DS + 0.2.0_DS co-owned): this spec + the companion TSV
  are the WS-2 input requirements. MP-01/02/03 is build-ready (9 public series + re-blend
  weights). Correlation is build-ready for 59/63; 4 need the §4-finding-1 resolution. FT-02/03
  is **blocked** on the §4-finding-2 Yang-source consult — recommend C2 sequences FT-02/03
  last or splits it out.
- **To A3** (`YALP_MDSRC.A3`, 0.1.0_DS): the input rows are keyed on `portal_name` + carry
  `bbg_ticker`; A3 fills `ycharts_symbol`. The 3 correlation Treasury gaps + the Crude Oil
  variant need an A3 internal-API lookup. Surface IDs aligned (correlation / FT-02 / FT-03 /
  MP-01 / MP-02 / MP-03) per the C3<->A3 coordination MCP.
- **Yang-source consult needed** (flag to COO): the 6 factor-spread constituent definitions
  (§3.2). Recommend COO route a one-question consult to AE 0.5.0 (yang-pipeline owner) or
  Yang directly.

## 7. Acceptance criteria

| AC | Status |
|---|---|
| AC1 — every WS-2 hybrid surface's input series enumerated (ticker/symbol, what it feeds, cadence, units, source) | MET — §3, companion TSV |
| AC2 — each input cross-referenced to the YCharts crosswalk; pending-A3 rows flagged | MET — §3.1/§3.3, §4; FT-02/03 flagged as needing Yang-source (§3.2) |
| AC3 — committed machine-readable spec pushed to origin/CLOUD + session log + RAVC2 | brief + companion TSV committed + pushed; session log; RAVC2 to COO CC CTO |
