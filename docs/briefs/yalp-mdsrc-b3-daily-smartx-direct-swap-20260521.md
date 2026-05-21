# YALP_MDSRC.B3 — daily-SmartX-direct upgrade: the swap

| | |
|---|---|
| **Author** | 0.4.0_DS_ClientPlatform |
| **Date** | 2026-05-21 |
| **TO** | YALP_MDSRC.B3 (`org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/YALP_MDSRC.B3.ds-b1-daily-smartx-direct-upgrade.md`, committed `1b0ec1d12`) |
| **Status** | Phase 0 + Phase 1 complete (incl. the CTO additive rework). Locally verified. Code-ready for the AE B4 deploy-half. |
| **Predecessor** | YALP_MDSRC.B1 (v1 shipped + e2e-verified 2026-05-21) |

---

## 1. What B3 does

B1 v1 shipped a correct *labeled hybrid*: the 7 monthly+ periods of `model_portfolio_benchmarks.json`'s `model` return were SmartX-realized; the daily periods (1D/WTD) and `model_portfolio_timeseries.json`'s `model_return` stayed yang model-*design* returns (`model.pkl`). That hybrid existed only because B1 Phase 0 believed SmartX had no daily model-return series.

B3 retires that estimation leg. `/api/3.1/models/{id}/performance?grouping=daily` is a genuine daily flow-adjusted SmartX model-return series. B3 brings the daily axis to it. `model.pkl` is retained as the Q4 proprietary design view.

## 2. Phase 0 — endpoint generalization (PASS)

`/api/3.1/models/{id}/performance?grouping=daily` validated across **all 5 portal models** (B1 Phase 0 had verified only ST):

| Model | Records | Range | Genuine daily? |
|---|---|---|---|
| ST / LTA / INT / LTC | 431 | 2024-09-03 → 2026-05-20 | yes |
| UST | 326 | 2025-02-03 → 2026-05-20 (later inception) | yes |

Genuine-daily proof — the A4/A5 sweep-artifact check: inter-record gap distribution `{1d:334, 2d:7, 3d:80, 4d:9}` (UST `{1d:254, 2d:4, 3d:59, 4d:8}`). Modal gap 1 day; 3-day gaps = weekends, 2/4-day = holidays. Trading-day cadence, **not** uniform-7d weekly-resampled-mislabeled. `summary.isFullRange` true on 100% of records; all series fresh to T-1; `pnl.percent` ranges plausible per model risk. Endpoint generalizes.

## 3. Phase 1 — the swap

### 3.1 SmartX pull (`data/smartx/scripts/pull_smartx_model_monthly_performance.py`)

Extended (B1 monthly logic untouched — zero regression to B1 v1's monthly sidecar). Added `fetch_model_daily` / `build_daily_sidecar` / `crosscheck_daily_vs_monthly`. The Lambda now emits **two** sidecars:

- `_smartx_model_monthly.json` (B1) — the 7 monthly+ periods.
- `_smartx_model_daily.json` (B3, new) — the per-trading-day flow-adjusted series. `return_pct` is per-day return in **percent** (SmartX `pnl.percent` is a decimal fraction → ×100, to match the yang pipeline's percent convention). Record date is `range.end`.

**Units verified empirically.** `crosscheck_daily_vs_monthly` compounds each model's daily series over the last complete month and compares to the monthly sidecar's 1M. Result: ST/LTA/INT/LTC/UST all **delta = 0.00** — the daily endpoint's `pnl.percent` units and sign are confirmed correct, and the two SmartX sources agree to the cent.

### 3.2 Producer (`infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py`)

- New `load_smartx_daily_sidecar` + `smartx_daily_period_return`.
- **`model_portfolio_benchmarks.json`** — 1D/WTD now sourced from the daily sidecar (`model_source=smartx_realized`); monthly+ unchanged. The `model` return is SmartX-realized for all 9 periods.
- **`model_portfolio_timeseries.json`** — **additive** (see §3.3). `build_timeseries` is left unchanged (full-history design series); a new `build_timeseries_realized` emits the SmartX-direct series alongside.
- Graceful fallback: either sidecar absent → the affected periods fall back to yang; the producer never hard-fails on a late pull.

### 3.3 The CTO additive rework + Phase-0 consumer enumeration

B3-as-first-built did a *truncating replace* of `model_portfolio_timeseries.json`'s `model_return` — the series began at SmartX coverage (UST ~9mo shorter than inception). The consumer-coordination flag raised on that delta was escalated; **CTO ruled (2026-05-21) the timeseries change must be ADDITIVE, not a truncating replace** — a truncating replace silently regresses MDLP_RVVALT (rolling Sharpe / max drawdown), a shipped client-facing feature, and for UST makes a trailing-window rolling Sharpe uncomputable. The pre-coverage history is the `model.pkl` *design*-return view, which Q4 explicitly retains as legitimate — so retaining it (not truncating) is correct.

**Consumer enumeration (rework Phase 0).** `model_portfolio_timeseries.json` is consumed by exactly one fetch — `getModelPortfolioTimeseries()` (`portal/src/api/portal-proxy.ts:722`), called once from `ReturnVolatilityScatter.tsx`, feeding the four MDLP_RVVALT components (`RollingSharpeChart`, `MaxDrawdownChart`, `RollingCaptureChart`, `ReturnVolatilityScatter`). All read only the `timeseries` array via the `ModelTimeseriesResponse` type — no other top-level field. No sibling consumer; the TS type system makes this airtight.

**Additive design.** `model_portfolio_timeseries.json` now carries two parallel series:
- `timeseries` — the full-history model-**design** return series (`model.pkl`-derived, from `inception_date`). **Left byte-identical** to the pre-B3 producer output; MDLP_RVVALT reads this → zero regression.
- `timeseries_realized` — the **SmartX-direct realized** series, present over SmartX coverage only.

Both row schemas are `{date, model_code, model_return, benchmark_return, rfr}`. Which series the rolling metrics ultimately use (design vs realized) is a v0.4 Q8 product decision CTO is surfacing to Andrew; until then the design series stays authoritative for MDLP_RVVALT.

### 3.4 Local end-to-end verification (PASS)

Full producer run locally (real `data_20260519_v1.pkl` + live monthly sidecar + locally-built daily sidecar, S3 monkeypatched):

- `model_portfolio_benchmarks.json` — all 9 periods `smartx_realized` for all 5 models; 1D values match the daily sidecar's last record to 2 dp.
- `model_portfolio_timeseries.json` — `timeseries` (2675 rows) **byte-identical to the pre-B3 live artifact** (zero regression confirmed empirically, not asserted); `timeseries_realized` 2050 rows across all 5 models; design row schema unchanged.

## 4. Artifact-contract deltas (AC5 — for downstream)

1. **`model_portfolio_benchmarks.json`** — 1D/WTD `model_source` flips `yang_design` → `smartx_realized`; the 1D/WTD `model` *values* change (SmartX-realized) and spreads recompute. `model_source_note` updated. Additive only; no field added/removed.

2. **`model_portfolio_timeseries.json`** — **purely additive, zero regression:**
   - `timeseries` (the existing array MDLP_RVVALT reads) is **unchanged** — byte-identical to pre-B3.
   - **New top-level key `timeseries_realized`** — the SmartX-direct realized series; invisible to current TS consumers (not in the `ModelTimeseriesResponse` interface).
   - Top-level `series_note` added; the interim `model_source_note` was removed before ever shipping.

3. **New sidecar** `s3://opal-data-portal-v2/json/benchmarks/_smartx_model_daily.json` (internal producer input; not portal-served).

No consumer-coordination risk remains — the additive rework eliminates it.

## 5. Compiler-tools / gate checks

- `.tools/ds-commit-gate.sh` — both files clean (py_compile + ds-precommit-check + ruff py39).
- Phase 0 endpoint generalization — PASS (§2).
- Daily-vs-monthly fidelity cross-check — delta 0.00 ×5 (§3.1).
- Rework consumer enumeration — MDLP_RVVALT sole consumer, confirmed (§3.3).
- Local additive-rework integration test — PASS, `timeseries` byte-identical to pre-B3 (§3.4).

## 6. AE B4 deploy-half

Files for the AE to commit + deploy (AE-lane; in the shared working tree, uncommitted):
- `data/smartx/scripts/pull_smartx_model_monthly_performance.py` — the smartx pull Lambda. **Purely additive** (adds a 2nd sidecar); deployable independently, no rework dependency.
- `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py` — the producer (additive rework applied).

Deploy order (mirror B2): deploy the pull Lambda first + invoke once so `_smartx_model_daily.json` exists, *then* deploy the producer. IAM: the daily sidecar is the same bucket as the monthly — no new permission.
