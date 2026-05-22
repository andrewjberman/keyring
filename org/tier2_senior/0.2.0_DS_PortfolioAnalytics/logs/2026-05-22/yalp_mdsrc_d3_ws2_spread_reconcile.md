# Session Log -- YALP_MDSRC.D3 WS-2 leg (FT-02/03 spread reconcile + RSI basis)

| Field | Value |
|---|---|
| Agent | 0.2.0_DS_PortfolioAnalytics |
| Date | 2026-05-22 |
| TO | YALP_MDSRC.D3 -- all-surface confirmation closure; co-owned, WS-2 leg (0.2.0_DS) |
| Status | Phase A COMPLETE -- FT-02/03 reconcile verdict + fix committed; RSI basis verdict handed off. Phase B (live re-pull) gated on YCharts seat. |

## Scope (WS-2 leg)

1. FT-02/03 factor-spread definition reconcile -- `ws2_factor_tilts_pull` spread
   arithmetic vs Yang `model_portfolio_regression_analysis.ipynb` section 8.
2. RSI basis check -- C2 used `rsi_14`; confirm the correct portal basis.
3. Any WS-2 hybrid-leg residual from D2 still uncertain -> terminal verdict.

Phase A = analysis + dormant-source edits, NO YCharts call. Phase B = the live
re-pull to evidence the verdicts end-to-end, gated on the shared Menachem seat
(0.1.0_DS holds it for the WS-1 WU1 MSCI round).

## Item 1 -- FT-02/03 factor-spread reconcile: VERDICT

**Construct: CONFIRMED-MATCH.** `ws2_factor_tilts_pull.compute_factor_spreads`
computes `spread_t = return(leg A)_t - return(leg B)_t`, daily, on the dates
present in both legs, missing-date dropped. Yang section 8
`calculate_factor_spreads` (notebook cell 22) computes `returns_df[t1] -
returns_df[t2]` -- the identical construct: a 1-day return difference, common
dates (pandas NaN-align), no rolling, no cumulative.

**D2's diagnosis is FALSIFIED.** The D2 brief called `factor_spread` "a
different, larger-scale construct (rolling/cumulative spread, not a 1-day
return-diff)." It is not -- it is the same 1-day return-diff. D2 saw a ~100x
scale gap and mis-attributed it.

**The real gap: a 100x UNIT divergence (decimal vs percent).**
- Yang section 8 builds `factor_spreads` from `etf_returns['return']`, the
  Bloomberg field `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` (notebook cell 3 `dc_return`),
  which is reported in PERCENT units. Confirmed by cell 14
  `calculate_model_returns_with_drift`: it divides `{ticker}_return` by 100 to
  use the value as a decimal multiplier -> the column is percent-unit.
- model.pkl `factor_spread` (notebook cell 35 export) is therefore percent-unit.
  Empirically confirmed -- `.runtime/model_20260405.pkl` `factor_spread`
  (1319 rows x 6 cols, daily 2020-12-31..2026-04-02): per-factor daily std
  ~0.29-0.99, |extremes| ~1.2-8.6. Those are percent (a daily equity-vs-FI
  spread of std ~1.0); as decimals they would be ~100% daily moves -- impossible.
- The generator `yang-generate-factor-tilts` (`extract_factor_spreads` /
  `extract_time_series`) applies NO scaling -- `round(float(value), 4)`
  passthrough -- so the portal JSON is percent-unit.
- `ws2_factor_tilts_pull` builds spreads from `daily_returns_from_levels`
  (`level_t/level_{t-1} - 1`), which yields DECIMAL simple returns. The module
  emitted decimal-unit spreads.

D2's "YCharts ~+/-0.006 vs model.pkl ~+/-0.1-0.6" is exactly this: +/-0.006
decimal = +/-0.6 percent, squarely inside the model.pkl +/-0.1-0.6 percent range.

**RECONCILE APPLIED (commit 47871c033).** `compute_factor_spreads` now scales
the spread by `SPREAD_PCT_SCALE = 100.0` -> percent-unit output, a unit-faithful
drop-in for model.pkl/factor_spread. The shared `daily_returns_from_levels`
(imported by the MP-benchmark module too) is UNCHANGED -- the percent scaling is
local to the FT module's `compute_factor_spreads`, which is the FT module's
responsibility to match its consumer's unit. Structural self-test updated
(Equity-vs-FI 3-date check now asserts percent: 1.5 / -1.4 / 2.9) and passes.

Terminal verdict: **CONFIRMED-MATCH (construct), unit reconciled.** Phase B will
evidence the end-to-end value match on a live re-pull.

## Item 2 -- RSI basis check: VERDICT

**The correct portal RSI basis is RSI-30D (30-day).** Citation: Yang's original
Market Overview build `docs/reference/yang-original-scripts/market_indices_data_pull.ipynb`
cell 10 -- the Bloomberg field map has `'rsi': 'RSI_30D'`. The portal Market
Overview RSI (RSIBars / RSIModal, surfaces WS1-MO-02/03) is fed from yang
`data_pkl` `rsi` = Bloomberg `RSI_30D`; no generator re-derives it.

**The C2 module `ws1_surface_pull.py` has `RSI_COLUMNS = ["rsi_14"]`** -- a
14-day RSI (YCharts default). Wrong window. The WS-1 audit brief called `rsi_14`
"index-applicable / Covered" -- a catalog-applicability check, not a
window-match check.

RSI surfaces WS1-MO-02/03 + `ws1_surface_pull.py` are the WS-1 module section,
so the `RSI_COLUMNS` re-map belongs in 0.1.0_DS's WS-1 work (handed off by MCP
2026-05-22 21:59Z). Sub-tasks for it: discover a YCharts 30-day RSI metric on
the seat -> CONFIRMED-MATCH; or, if none, derive RSI-30D from the 30-day price
window -> CONFIRMED-DERIVED. Not Bloomberg-only either way.

## Item 3 -- WS-2 hybrid-leg residual triage

| WS-2 leg | D2 finding | D3 terminal verdict |
|---|---|---|
| MP-01/02/03 ETF legs | MATCH 5/5 to-the-cent | CONFIRMED-MATCH (terminal) |
| MP-01/02/03 index legs | MINOR 0.004-0.030pp | Phase B: per-symbol fidelity check. 0-1Y Treasury `^BBUTB13MTR` -> CONFIRMED-REPRESENTATIVE (V1A rep-index); `^BBUSATR`/`^MSACWI` legs -> tighten to CONFIRMED-MATCH or document residual. |
| FT-02/03 | DIVERGENCE (flagged in-flight) | Resolved -- see Item 1. CONFIRMED-MATCH, unit reconciled. |
| ERP / Risk-Premium | UNRESOLVED on YCharts | CONFIRMED-BLOOMBERG-ONLY -- forward-P/E leg: `I:SP500PND`/`PNM` are trailing not NTM-forward (38.9% divergence), no forward-P/E entity on YCharts; COO hybrid ruling holds the leg on Bloomberg-pkl. Terminal. |

## Files Modified

| File | Change |
|------|--------|
| infra/aws/lambda/ycharts-market-data-pull/ws2_factor_tilts_pull.py | `compute_factor_spreads` scales spread by `SPREAD_PCT_SCALE=100.0` -> percent units, matching Yang s8 / model.pkl factor_spread. Docstrings + module comment + meta note updated; structural self-test percent-unit expectations updated. Commit 47871c033. |

## Compiler Tools

| Tool | Result |
|------|--------|
| (none applicable) | D3 edits dormant Lambda-module source (`ws2_factor_tilts_pull.py`) and runs it ad-hoc; it touches no gold/silver/bronze script, no portal component, no route, no IAM surface, no Terraform -- same determination as the D3 TO `<compiler_tools_mandate>` note. The reconcile discipline is code+notebook+empirical-pkl tracing; verdicts are citation-grounded per the TO context. |
| `.tools/ds-commit-gate.sh` | PASS (exit 0) -- py_compile + ds-precommit-check + ruff on `ws2_factor_tilts_pull.py` before commit. |

## Next Steps

- [0.1.0_DS_MarketIntelligence] RSI re-map in `ws1_surface_pull.py` (WS-1 lane) -- discover the YCharts 30-day RSI metric or derive RSI-30D; verdict basis = RSI-30D per this log.
- [0.1.0_DS_MarketIntelligence] Signal seat-FREE after the WS-1 WU1 MSCI round -> my Phase B re-pull.
- [0.2.0_DS] Phase B: live re-pull of the 10 FT-02/03 constituents (`pull_factor_tilt_inputs`) on the Menachem seat -> evidence the percent-unit spreads match model.pkl/factor_spread on matched dates; MP index-leg per-symbol fidelity check.
- [0.2.0_DS] Draft the WS-2 confirmed-table section for the joint D3 brief; send to 0.1.0_DS for assembly.
- [2.0.0_SA_COO] Joint D3 RAVC2 (one-sender pattern) once WS-1 + WS-2 legs both land.
