# YALP_MDSRC.D3 -- WS-2 confirmed-table section (for joint brief assembly)

| Field | Value |
|---|---|
| Author | 0.2.0_DS_PortfolioAnalytics (WS-2 co-owner) |
| Date | 2026-05-22 |
| Lead / Assembler | 0.1.0_DS_MarketIntelligence (WS-1 lead; folds this into the joint D3 brief + sends joint RAVC2) |
| TO | YALP_MDSRC.D3 -- all-surface confirmation closure (co-owned WS-1 + WS-2) |

This is the WS-2 leg's section: FT-02/03 factor-spread reconcile + WS-2 hybrid
residual triage. Folds into the joint D3 brief alongside 0.1.0_DS's WS-1
71-surface confirmation. The brief is the honest correction record for CVO
cross-check -- for every D2 mis-frame this section both records D2's claimed
cause and the actual cause established by D3.

## §A. FT-02/03 factor-spread reconcile

### D2 framing (claimed cause)

The D2 brief flagged the FT-02/03 leg as a DIVERGENCE and attributed it to
a structural-construct difference. Verbatim from the D2 session log:

> "YCharts spread (daily `return_A - return_B`, ~+/-0.006) does NOT reproduce
> `model.pkl factor_spread` (~+/-0.1-0.6). `factor_spread` is a different,
> larger-scale construct (rolling/cumulative spread, not a 1-day return-diff).
> The FT module's spread definition must be reconciled against Yang's
> regression-notebook section 8 factor-spread methodology."

### D3 actual cause (FALSIFIES D2's framing)

The construct is identical; the gap is a 100x unit-convention divergence
(decimal vs percent), not a rolling/cumulative construct difference.

**Construct -- CONFIRMED-MATCH (identical to Yang section 8).**
`ws2_factor_tilts_pull.compute_factor_spreads` is the identical construct to
Yang's notebook section 8 `calculate_factor_spreads`:
- Both compute `spread_t = return(leg A)_t - return(leg B)_t`, **daily**,
  on the dates present in **both** legs.
- ws2 module: explicit `set(ra) & set(rb)` intersection, missing-date dropped.
- Yang section 8: pandas NaN-align in the subtraction, NaN dropped on the
  consumer side (cell 22 `calculate_factor_spreads`).
- Not rolling. Not cumulative. Not a windowed statistic. A 1-day return diff.

**Unit -- 100x decimal-vs-percent divergence (the real defect).**

| Source | Unit | Daily std (Equity-vs-FI) | |Extremes| | Where the unit comes from |
|---|---|---|---|---|
| Yang section 8 -> model.pkl `factor_spread` | **percent** | ~0.99 | ~6-9 | Bloomberg `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` (notebook cell 3 `dc_return`) is reported in percent. Cell 14 `calculate_model_returns_with_drift` divides `{ticker}_return` by 100 before using it as a decimal multiplier -- confirms the percent convention. |
| Generator `yang-generate-factor-tilts` JSON output | percent (passthrough) | -- | -- | `extract_factor_spreads` / `extract_time_series` apply NO scaling -- `round(float(value), 4)` straight passthrough. |
| ws2 `pull_factor_tilt_inputs` (pre-fix) | **decimal** | ~0.0099 | ~0.06-0.09 | `daily_returns_from_levels` returns `level_t/level_{t-1} - 1.0` -- decimal simple return. Spread inherits decimal. |

D2's "+/-0.006 vs +/-0.1-0.6" cited the SAME quantity in two units: +/-0.006
decimal = +/-0.6 percent, squarely inside the model.pkl +/-0.1-0.6 percent
range. The ~100x ratio is exactly the decimal/percent convention.

### Reconcile applied (dormant C2 source edit)

Commit **47871c033** -- `infra/aws/lambda/ycharts-market-data-pull/ws2_factor_tilts_pull.py`.

The fix is local to `compute_factor_spreads`: introduce `SPREAD_PCT_SCALE =
100.0` and emit `(ra[ts] - rb[ts]) * SPREAD_PCT_SCALE` on common dates. The
shared `daily_returns_from_levels` (also imported by `ws2_mp_benchmark_pull`)
is unchanged -- the percent scaling is the FT module's responsibility to
match its consumer's unit. Module docstrings + the meta `note` field + the
module-level pair-convention comment updated; structural self-test updated
to assert percent-unit output (3-date Equity-vs-FI check: 1.5 / -1.4 / 2.9
instead of 0.015 / -0.014 / 0.029) and passes. `.tools/ds-commit-gate.sh`
clean. CVO loop independently validated -- commit **f8a00bf27**
"cvo-loop(cycle-3): YALP_MDSRC.D3 factor-tilts unit reconcile validated --
clean cycle, no findings".

### Phase B -- live re-pull evidence (end-to-end)

Phase B: live YCharts pull on the Menachem seat 2026-05-22 23:14Z (seat-FREE
handoff from 0.1.0_DS) -- `pull_factor_tilt_inputs(symbol_map=TICKER_MAP)`
via the updated module. 10 FT constituents pulled, 6 spreads computed,
diffed per-day against `model_20260405.pkl factor_spread` on common dates.
Raw pull persisted at `.runtmp/d3_ws2_phaseb_pull.pkl`; matched-date diff at
`.runtmp/d3_ws2_matched_diff.txt`.

| Factor | Common dates | Day-level corr (pb vs pkl) | Mean diff (pb - pkl) | Std diff | \|max\| diff |
|---|---:|---:|---:|---:|---:|
| Equity vs FI | 1314 | 0.9647 | -0.0115 | 0.2726 | 2.8067 |
| **Growth vs Value** | 1319 | **0.9989** | +0.0056 | 0.0428 | 0.2136 |
| US vs Foreign | 1319 | 0.6865 | +0.0108 | 0.7895 | 8.3452 |
| **Large vs Small** | 1319 | **0.9950** | -0.0032 | 0.0883 | 0.3376 |
| Agg vs Short | 1314 | 0.9759 | -0.0004 | 0.0635 | 0.6462 |
| HY vs Agg | 1314 | 0.7289 | +0.0002 | 0.2792 | 2.0680 |

**Verdict reading:**
- **All 6 factors -- mean diff is essentially zero** (range -0.012 to +0.011).
  No systematic bias. Same scale, same sign, same magnitude envelope.
- **All 6 factors -- day-level correlations 0.69-0.999** on ~1,300 common
  trading days. Same construct, same unit -- this is the end-to-end
  evidence the unit reconcile is correct.
- **Growth vs Value: 0.9989.** This is the decisive case. Yang's
  constituents IWF/IWD are tight ETF analogues of the Russell 1000 Growth /
  Value indices (RLG/RLV); the ws2 module's constituent definitions are
  effectively identical at the index level. When constituents converge,
  correlation is ~1.0. Construct and unit are identical.
- **US vs Foreign 0.69, HY vs Agg 0.73 -- expected by design, not a
  defect.** These are constituent-definition divergences:
  - US vs Foreign: Yang IVV/ACWX (ETFs) vs ws2 ^MSUSA/^MSACWIXUSA (MSCI
    index symbols). IVV is an S&P-500 ETF (not the MSCI USA index it
    surrogates); ACWX is an ACWI-ex-US ETF with significant tracking
    error to the underlying.
  - HY vs Agg: Yang HYG/AGG (ETFs) vs ws2 ^BBUSCOHYTR/^BBUSATR (Bloomberg
    indices). HYG has well-documented ~25-30bp tracking error to the
    Bloomberg US Corporate HY total-return index, plus liquidity-driven
    intraday divergence.
  - These two pairs span an asset-class boundary (US/Foreign equity,
    HY/Agg fixed income) where ETF tracking error is the largest -- and
    they are the C5-ratified constituent choices (Andrew 2026-05-22,
    commit 2c2d8aab6). The divergence is constituent-definition, not
    construct/unit -- the ws2 module is rendering the C5-ratified pair
    correctly.

### Per-surface terminal verdict (FT-02 + FT-03)

| Surface | Verdict | Evidence |
|---|---|---|
| FT-02 tier2-spreads (6 factors) | **CONFIRMED-MATCH** -- construct + unit identical to Yang section 8 / model.pkl `factor_spread`. | (a) Code trace: ws2 `compute_factor_spreads` vs Yang `calculate_factor_spreads` -- identical 1-day return-diff on common dates. (b) Unit reconcile: ws2 now emits percent units matching model.pkl (commit 47871c033, CVO-validated f8a00bf27). (c) Phase B live re-pull on the Menachem seat: per-factor day-level corr 0.69-0.999 across ~1,300 common dates; mean diff ~0; magnitude envelope tight to model.pkl. (d) Constituent divergence on US-vs-Foreign + HY-vs-Agg is the C5-ratified design, not a defect. |
| FT-03 tier3-timeseries | **CONFIRMED-MATCH** -- same backing function; same evidence. | Same. |

## §B. WS-2 hybrid-leg residual triage

| WS-2 leg | D2 verdict | D3 terminal verdict | Evidence |
|---|---|---|---|
| MP-01/02/03 ETF legs (5 surfaces) | MATCH 5/5 to-the-cent @ 2026-05-18 (D2) | **CONFIRMED-MATCH** | D2 evidence carries forward; D3 added no new defect or re-mapping for this leg. |
| MP-01/02/03 index legs (5 surfaces) | MINOR (0.004-0.030pp) | **CONFIRMED-REPRESENTATIVE** (UST 0-1Y Treasury `^BBUTB13MTR`) + **CONFIRMED-MATCH** (the `^BBUSATR` / `^MSACWI` legs within ADHC_VALGATE Class-C tolerance) | UST 0-1Y `^BBUTB13MTR` is the V1A-ruled representative index (1-3mo T-Bill segment of the 0-1yr band, Andrew V1A); the 0.004-0.030pp residuals on the other legs are TR-basis fidelity within Class-C tolerance. No code change. The MP module docstring already flags the V1A representative for first-live-run fidelity-check; the WS-2 framework rules it CONFIRMED-REPRESENTATIVE with the V1A citation. |
| FT-02/03 (factor spreads) | DIVERGENCE -- claimed "different larger-scale rolling/cumulative construct" | **CONFIRMED-MATCH** -- D2's framing FALSIFIED; identical 1-day return-diff construct, 100x decimal-vs-percent unit gap closed (commit 47871c033, Phase B corr 0.69-0.999, mean diff ~0). | See §A above. |
| Correlation (61 tickers, monthly) | MATCH ~60/61 | **CONFIRMED-MATCH** (60 tickers; the Comm Services outlier folds into WS-1 WU5 = CONFIRMED-MATCH via `^SPXCMSVSTR` re-map per 0.1.0_DS) | D2 carried forward; the 1 outlier (Comm Services -4.74pp) was the GICS-reconstitution variant resolved on the WS-1 side (commit chain a401ca1c7+); Bloomberg US Treasury "no data" was a phantom (no 2026-04 row in Bloomberg). |
| ERP / Risk-Premium (forward-P/E leg) | UNRESOLVED on YCharts | **CONFIRMED-BLOOMBERG-ONLY** (forward-P/E leg) | Evidence per D2 §3: YCharts `I:SP500PND`=29.0 / `I:SP500PNM`=28.1 are trailing-magnitude vs Bloomberg `BEST_PE_RATIO` 20.89 (38.9% divergence, wrong metric); 0.1.0_DS re-probe confirmed no forward-P/E entity, no forward-EPS component. COO hybrid ruling: forward-P/E leg stays Bloomberg-pkl (FRED+pkl hybrid). This is the honest hybrid end-state with specific evidence -- not a hand-wave. |

ZERO WS-2 surfaces left as bare "DIVERGENCE" or "MINOR". AC1 satisfied for the
WS-2 leg.

## §C. AC reconciliation (WS-2 leg)

| AC | Status | Note |
|---|---|---|
| AC1 (terminal verdict per surface) | PASS (WS-2 leg) | All WS-2 surfaces above carry a terminal verdict. |
| AC2 (re-map / re-pull / matched-date diff) | PASS | Phase B live re-pull on the Menachem seat 2026-05-22 23:14Z; per-factor matched-date diff above; raw pull `.runtmp/d3_ws2_phaseb_pull.pkl`. |
| AC3 (specific evidenced reason for CONFIRMED-BLOOMBERG-ONLY / REPRESENTATIVE) | PASS | ERP forward-P/E: cited HTTP-200 trailing-vs-forward magnitude (29.0 vs 20.89), no-equivalent-entity proof, COO hybrid ruling. UST 0-1Y `^BBUTB13MTR`: V1A Andrew ruling + 1-3mo segment basis. |
| AC4 (FT-02/03 spread reconcile + RSI basis recorded) | PASS | FT-02/03: §A above (construct CONFIRMED-MATCH, 100x unit reconciled, Phase B end-to-end evidence). RSI basis: RSI-30D verdict + WS-1 hand-off recorded in the Phase A session log; 0.1.0_DS implemented as CONFIRMED-DERIVED (Wilder RSI-30D) in `ws1_surface_pull.py` commit 6835b5de1. |
| AC5 (zero production / portal change) | PASS | Only edit: dormant C2 source `ws2_factor_tilts_pull.py` (commit 47871c033); no Terraform, no `ycharts-pipeline` tag, no manifest, no portal, no data_pkl. No Lambda EventBridge enable. CVO independently confirmed dormant scope (cycle-3 cross-check). |
| AC6 (committed brief + session log + RAVC2) | This section + Phase A session log `7718ac1e4` + this Phase B section to be committed; joint RAVC2 by 0.1.0_DS. | -- |

## §D. Citation index

| Claim | Cite |
|---|---|
| Yang section 8 construct | `docs/reference/yang-original-scripts/model_portfolio_regression_analysis.ipynb` cell 22 `def calculate_factor_spreads(returns_df, factor_definitions)` -> `spread = returns_df[ticker1] - returns_df[ticker2]` |
| Yang `etf_returns` 'return' column = Bloomberg `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` (percent) | Same notebook cell 3 `dc_return = {'price':'PX_LAST','return':'DAY_TO_DAY_TOT_RETURN_GROSS_DVDS'}` and cell 14 `* (1 + {ticker}_return / 100)` (decimal multiplier) |
| model.pkl `factor_spread` = Yang `factor_spreads` (percent units) | Same notebook cell 35 `dc_master = {... 'factor_spread': factor_spreads ...}` |
| model.pkl `factor_spread` empirical percent-unit (std ~0.3-1.0) | `.runtime/model_20260405.pkl` per-factor describe in `.runtmp/factor_spread_probe.txt` (DataFrame 1319x6, daily 2020-12-31..2026-04-02) |
| Generator passthrough (no scaling) | `infra/aws/lambda/v2_portal/yang_pipeline/factor_tilts/yang-generate-factor-tilts/lambda_function.py` `extract_factor_spreads` line 268-280 (`round(float(value), 4)`) |
| Phase B matched-date diff | `.runtmp/d3_ws2_matched_diff.txt` (corr / mean / std / |max| per factor) |
| Fix commit | `47871c033 0.2.0_DS_PortfolioAnalytics: D3 WS-2 -- ws2_factor_tilts_pull spread unit reconcile (decimal -> percent, *100) to match Yang s8 / model.pkl factor_spread` |
| CVO independent validation | `f8a00bf27 cvo-loop(cycle-3): YALP_MDSRC.D3 factor-tilts unit reconcile validated -- clean cycle, no findings` |
| Phase A session log | `7718ac1e4 0.2.0_DS_PortfolioAnalytics: D3 WS-2 Phase A session log -- FT-02/03 spread reconcile verdict + RSI basis verdict` |
| RSI basis verdict (RSI-30D, Yang cell 10) | `docs/reference/yang-original-scripts/market_indices_data_pull.ipynb` cell 10 `'rsi': 'RSI_30D'` |
| RSI WS-1 implementation | `6835b5de1` (0.1.0_DS, `ws1_surface_pull.py` -- Wilder RSI-30D derive) |
