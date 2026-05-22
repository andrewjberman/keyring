# YALP_MDSRC.C2 — WS-2 MP-01/02/03 Build Plan (benchmark-leg YCharts pull)

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` — PRD v0.3 §7 Phase 2C |
| Task Order | `YALP_MDSRC.C2` — co-owned (0.1.0_DS lead / WS-1; 0.2.0_DS co-owner / WS-2) |
| Author | `0.2.0_DS_PortfolioAnalytics` (WS-2 co-owner) |
| Date | 2026-05-22 |
| Scope of this brief | The MP-01/02/03 benchmark-leg pull — the first (build-ready) WS-2 leg per the COO GO sequencing |
| Build inputs consumed | C3 input spec §3.3 (`mdsrc-ws2-c2-input-spec-20260520`), A3 P3 mapping TSV (`mdsrc-ycharts-internal-api-mapping-20260520.tsv`), A3 internal-API spec, the dc01d4b8a ticker map |
| Freeze status | FREEZE-AWARE — this plan + the pull module are BUILT + structurally validated now; NO live YCharts execution until the dedicated seat lands |

---

## 1. What MP-01/02/03 needs

The generator `yang-model-portfolio-benchmarks` (`infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py`) produces three S3 artifacts — the WS-2 hybrid surfaces:

| Surface | S3 artifact | Benchmark leg this brief sources |
|---|---|---|
| MP-01 | `benchmark_returns.json` | index + ETF benchmark returns |
| MP-02 | `model_portfolio_benchmarks.json` | comprehensive index + ETF benchmark table |
| MP-03 | `model_portfolio_timeseries.json` | full-history benchmark series + RFR |

All three consume the **same input families**. The `model` return leg is WS-3 (SmartX, TO-B1) — out of scope. The benchmark leg is **9 distinct public market-data series**, verified against the generator source 2026-05-22:

- `INDEX_COMPOSITIONS` / `ETF_COMPOSITIONS` / `MODEL_RFR_TENOR` (generator lines 107-133) confirm the C3 §3.3 blend weights **exactly** — no drift since C3 (2026-05-20).

## 2. The 9 input series

### 2a. Index-blend constituents (3) — generator reads `data.pkl -> return_daily`

| # | portal_name | bbg_ticker | ycharts_symbol | fidelity (portal_1Y vs yc_1Y) | endpoint | status |
|---|---|---|---|---|---|---|
| 1 | Bloomberg 0-1 Year Treasury | `I22917US Index` | **UNPINNED** | n/a | `/charts/general_data.json` | SYMBOL-DISCOVERY (see §4) |
| 2 | Bloomberg Aggregate | `LBUSTRUU Index` | `^BBUSATR` | CLOSE (gap 0.3 pt) | `/charts/general_data.json` | READY |
| 3 | MSCI ACWI | `MXWD Index` | `^MSACWI` | CLOSE (gap 1.1 pt) | `/charts/general_data.json` | READY |

### 2b. ETF-blend constituents (3) — generator reads pre-blended `{Model} Term ETF`

| # | ETF | ycharts_symbol | endpoint | status |
|---|---|---|---|---|
| 4 | VGSH (Vanguard Short-Term Treasury ETF) | `VGSH` (ETF ticker = YCharts symbol, entity-agnostic per A3 §1) | `/charts/fund_data.json` | READY |
| 5 | AGG (iShares Core US Aggregate Bond ETF) | `AGG` | `/charts/fund_data.json` | READY |
| 6 | ACWI (iShares MSCI ACWI ETF) | `ACWI` | `/charts/fund_data.json` | READY |

### 2c. Risk-free-rate tenors (3) — generator reads `data.pkl -> price_monthly` Treasury yields

| # | RFR tenor | used by model | endpoint | status |
|---|---|---|---|---|
| 7 | 1Y Treasury yield | UST, ST | `/charts/general_data.json` (YIELD metric) | CROSS-DOMAIN — WS-1 (see §4) |
| 8 | 5Y Treasury yield | INT | `/charts/general_data.json` (YIELD metric) | CROSS-DOMAIN — WS-1 |
| 9 | 10Y Treasury yield | LTC, LTA | `/charts/general_data.json` (YIELD metric) | CROSS-DOMAIN — WS-1 |

## 3. Endpoint call shapes (per A3 P3)

**Indices + RFR yields — `/charts/general_data.json` GET:**
- `securities=id:{yc_symbol},include:true,,` ; `metrics=id:price,include:true,,` (RFR: a Treasury-yield metric — exact `internal_name` to confirm against `all_calc_menu`) ; `xAxis=time` ; `startDate` / `endDate` ; `resampleFrequency` (daily for indices, monthly for RFR).
- JSON path to value: `chart_data[].raw_data[[ts_ms, value]]`.

**ETFs — `/charts/fund_data.json` GET:**
- `securities=id:{ETF},include:true,,` ; `calcs=id:level,include:true,,` (a calc is REQUIRED — securities-only returns 400) ; `format=indexed`.
- JSON path to value: `chart_data[][].raw_data[[ts_ms, value]]`.

Both authenticate via the TO-C1 credential pipeline through 0.1.0_DS's shared internal-API client (one module, two sections — agreed seam). No parallel auth.

## 4. Re-blend logic (Opal computation unchanged — TO `do_not`)

C2 pulls the 9 raw constituent series; the Opal generator's existing blend math is untouched. The C2 pull module re-blends the constituents into the `{Model} Term Benchmark` / `{Model} Term ETF` series the generator currently reads pre-blended, per the generator constants (verified 2026-05-22):

```
INDEX:  UST 100% Bloomberg 0-1Y Treasury
        ST  85% Agg / 15% ACWI      INT 40% Agg / 60% ACWI
        LTC 15% Agg / 85% ACWI      LTA 15% Agg / 85% ACWI
ETF:    UST 100% VGSH
        ST  85% AGG / 15% ACWI      INT 40% AGG / 60% ACWI
        LTC 15% AGG / 85% ACWI      LTA 15% AGG / 85% ACWI
RFR:    UST 1Y | ST 1Y | INT 5Y | LTC 10Y | LTA 10Y  (price_monthly, fwd-filled to daily)
```

Blend is a weighted sum of daily decimal returns. The re-blend is a pull-module transform that reproduces the pre-blended series shape — it is NOT a change to the generator's downstream computation.

## 5. Open items (WS-2 co-owner to close)

| # | Item | Owner | Plan |
|---|---|---|---|
| O1 | Bloomberg 0-1 Year Treasury — no YCharts symbol pinned (A3 P4 "still-wide" maturity-band residue) | 0.2.0_DS | YCharts securities-search for the 0-1Y / short-Treasury index variant + a per-symbol fidelity check vs `portal_1Y=3.66`. Bounded symbol-discovery, not a data gap (A3 P4). |
| O2 | RFR 1Y/5Y/10Y Treasury yields are WS-1 YIELD-domain series | 0.2.0_DS + 0.1.0_DS | Cross-domain handoff — the RFR yield symbols belong in WS-1's crosswalk; coordinate so MP re-blend consumes WS-1's pinned yield symbols rather than re-pinning. Flagged to 0.1.0_DS. |
| O3 | RFR Treasury-yield metric `internal_name` unconfirmed | 0.2.0_DS | Confirm against `static.ycharts.com/.../all_calc_menu` (same UNVERIFIED-COLS pattern as WS1-VAL-01). |
| O4 | ETF `level` calc vs total-return basis — generator consumes returns; confirm `format=indexed` level series differences to daily total return | 0.2.0_DS | Structural check during build; per-symbol fidelity at first live run. |

None of O1-O4 blocks the freeze-aware build — they are symbol/metric-pinning items closed by structural validation now + a fidelity check at first live run.

## 6. Build sequence + freeze-aware validation

1. **Module section** — build the MP-01/02/03 WS-2 leg into the shared C2 pull module (one module, two sections) once 0.1.0_DS posts the shared internal-API client interface signature. The MP leg = a `fetch 9 series -> re-blend -> emit the pre-blended benchmark shape` function.
2. **Structural validation (no live YCharts):** unit-test the re-blend math against synthetic constituent series (weights sum to 1.0; UST single-constituent passthrough; output shape matches the generator's expected `{Model} Term Benchmark` series); assert the endpoint call shapes against the A3 P3 param spec; mock the client responses.
3. **Compiler mandate** — Phase 1 `comp-routes behaviors` + `comp-pipescript io yang-model-portfolio-benchmarks` (expect non-node -> source-read fallback per C3 §2); Phase 2 `.tools/ds-commit-gate.sh` on every `.py`; Phase 3 `comp-blast` on the changed producer.
4. **Live execution deferred** to the dedicated-seat unfreeze — same dormant-build pattern as C1.

## 7. Coordination

- **0.1.0_DS (WS-1 lead):** seam corrected — MP-01/02/03 is WS-2 (mine); MP-04 is WS-1. Awaiting the shared internal-API client skeleton + interface signature. RFR yield symbols (O2) handed to WS-1's crosswalk.
- **TO-B1 (SmartX):** the `model` return leg of MP-01/02/03 is dual-sourced — coordinate the `model_portfolio_*` artifact shape per PRD §5.3 when B1's model leg lands.
- **RAVC2 to 2.0.0_SA_COO** (no CC CTO per Andrew directive). This brief is phase artifact 1; next is the FT-02/03 and Correlation leg plans.
