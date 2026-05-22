# Session Log — YALP_MDSRC.D2 WS-2 YCharts-vs-Bloomberg comparison

| Field | Value |
|---|---|
| Agent | 0.2.0_DS_PortfolioAnalytics |
| Date | 2026-05-22 |
| TO | YALP_MDSRC.D2 — YCharts-vs-Bloomberg parallel comparison, co-owned (WS-2 = 0.2.0_DS) |
| Status | WS-2 run COMPLETE — 4 surfaces diffed live; 3 module fixes committed; joint-brief §3 in flight |

## Scope

D2 = the comparison/validation half of the original D1 (cutover carved out to a future
project). Run the C2 YCharts pull live against the Menachem session, diff each WS-2 surface
vs the current Bloomberg portal data on matched dates. Read + compare ONLY — zero
production/AWS/portal change.

## Matched-date method

- **Daily-surface anchor: 2026-05-18.** The portal `data_pkl` (`data_20260519_v1.pkl`) and
  the portal `all-returns.json` both last-settle at 2026-05-18 (the `20260519` filename is the
  file-write date). Converged independently with 0.1.0_DS.
- **Correlation (monthly) anchor: 2026-04 month-end** — the last settled monthly observation.
- Bloomberg `return` field = `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` (total return, per Yang's
  notebook `dc_fields_all`).

## Per-surface results (ADHC_VALGATE Class-C)

| Surface | Verdict | Evidence |
|---|---|---|
| MP-01/02/03 ETF legs | **MATCH** 5/5 to-the-cent | UST/ST/INT/LTC/LTA Term ETF — YCharts re-blend == Bloomberg `return_daily` @ 2026-05-18 exactly. Validates the pull + re-blend + matched-date method. |
| MP-01/02/03 index legs | MINOR divergence | 0.004-0.030 pp vs Bloomberg `{Model} Term Benchmark`. Cause: the representative-index residual (`^BBUTB13MTR` for the UST 0-1Y leg) + the CLOSE-not-EXACT fidelity of `^BBUSATR`/`^MSACWI`. Expected, documented — not a defect. |
| Correlation | **MATCH** ~60/61 | YCharts monthly returns vs Bloomberg `return_monthly` @ 2026-04 agree within ~0.13 pp (a small consistent ~0.07 pp offset — minor TR/PR-basis or month-end-alignment). Outliers: Communication Services -4.74 pp (known S5COMM cross-vendor index-definition divergence — corroborates the WS-1 finding); Bloomberg US Treasury no-data (no 2026-04 row in Bloomberg `return_monthly` — a phantom like bare `Crude Oil`). |
| FT-02/03 | **DIVERGENCE — finding** | YCharts spread (daily `return_A - return_B`, ~+/-0.006) does NOT reproduce `model.pkl factor_spread` (~+/-0.1-0.6). `factor_spread` is a different, larger-scale construct (rolling/cumulative spread, not a 1-day return-diff). The FT module's spread definition must be reconciled against Yang's regression-notebook §8 factor-spread methodology. |
| ERP / Risk-Premium | **UNRESOLVED on YCharts** | The S&P 500 forward P/E is not YCharts-sourceable. `I:SP500PND`=29.0 / `I:SP500PNM`=28.1 are trailing-magnitude vs Bloomberg NTM-forward (`BEST_PE_RATIO`) 20.89 — 38.9% divergence, wrong metric. 0.1.0_DS re-probe: no forward-P/E entity, no forward-EPS component. Forward-P/E leg stays Bloomberg-pkl (FRED+pkl hybrid). COO ruling pending. |

## Module fixes committed (all surfaced by D2's first live run)

| Fix | Commit | Detail |
|---|---|---|
| Correlation — gmtime crash guard | `fb053a108` | `_year_month` crashed on an out-of-range live YCharts ts (OSError on Windows); now returns None and the point is skipped. |
| Correlation — entity-kind calc | `fb053a108` | commodity SECURITIES (`GOLD`/`WTI`) need `fund_data(calc=price)`; module hardcoded `calc=level` -> 400. New `_calc_for()` — `^`/`I:` -> level, bare -> price. |
| ERP — revert I:SP500PND wire | `bc139cdd6` | the C2 ERP wire (`06e0e82c8`) to `I:SP500PND` is the wrong metric; reverted. `pull_erp_inputs` no longer pulls a forward P/E; the leg stays pkl. |

All three: synthetic self-tests could not reach these (they need live YCharts data) — D2's first live run is exactly what caught them. Self-tests updated, Rule 14 gate clean on each.

## RAVC state

- WS-2 findings RAVC'd to COO progressively (ERP 175831Z; will RAVC the full set with the joint brief).
- Joint D2 brief: `docs/briefs/mdsrc-d2-ycharts-bloomberg-comparison-20260522.md` — §2 WS-1 committed by 0.1.0_DS (`fc3b19641`); §3 WS-2 = my next deliverable.

## Next Steps

- [0.2.0_DS] Draft §3 (WS-2) of the joint comparison brief with the per-surface diffs above.
- [0.2.0_DS] Read Yang's `model_portfolio_regression_analysis.ipynb` §8 — pin the factor-spread definition; reconcile the FT module's spread arithmetic (COO directive: flag any divergence of the `ws2_*.py` modules vs Yang's original logic).
- [0.1.0_DS] Joint-brief assembly + joint RAVC2 to COO once §3 lands.
- [COO] Rule the ERP forward-P/E hybrid disposition (forward-P/E leg stays Bloomberg-pkl).
- [COO] Finding B carried — generator `MARKET_OVERVIEW_INDICES` bare `Crude Oil` alignment -> D1 TO.
