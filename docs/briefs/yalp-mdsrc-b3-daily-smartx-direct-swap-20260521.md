# YALP_MDSRC.B3 — daily-SmartX-direct upgrade: the swap

| | |
|---|---|
| **Author** | 0.4.0_DS_ClientPlatform |
| **Date** | 2026-05-21 |
| **TO** | YALP_MDSRC.B3 (`org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/YALP_MDSRC.B3.ds-b1-daily-smartx-direct-upgrade.md`, committed `1b0ec1d12`) |
| **Status** | Phase 0 + Phase 1 complete, locally verified. Code-ready for the AE B3-deploy-half. |
| **Predecessor** | YALP_MDSRC.B1 (v1 shipped + e2e-verified 2026-05-21) |

---

## 1. What B3 does

B1 v1 shipped a correct *labeled hybrid*: the 7 monthly+ periods of `model_portfolio_benchmarks.json`'s `model` return were SmartX-realized; the daily periods (1D/WTD) and `model_portfolio_timeseries.json`'s `model_return` stayed yang model-*design* returns (`model.pkl`). That hybrid existed only because B1 Phase 0 believed SmartX had no daily model-return series.

B3 retires that estimation leg. `/api/3.1/models/{id}/performance?grouping=daily` is a genuine daily flow-adjusted SmartX model-return series. B3 swaps the daily leg to it: **the `model` return is now SmartX-realized end to end.** `model.pkl` is retained as the Q4 proprietary design view — it no longer sources performance.

## 2. Phase 0 — endpoint generalization (PASS)

`/api/3.1/models/{id}/performance?grouping=daily` validated across **all 5 portal models** (B1 Phase 0 had verified only ST):

| Model | Records | Range | Genuine daily? |
|---|---|---|---|
| ST / LTA / INT / LTC | 431 | 2024-09-03 → 2026-05-20 | yes |
| UST | 326 | 2025-02-03 → 2026-05-20 (later inception) | yes |

Genuine-daily proof — the A4/A5 sweep-artifact check: inter-record gap distribution `{1d:334, 2d:7, 3d:80, 4d:9}` (UST `{1d:254, 2d:4, 3d:59, 4d:8}`). Modal gap 1 day; 3-day gaps = weekends, 2/4-day = holidays. Trading-day cadence, **not** uniform-7d weekly-resampled-mislabeled. `summary.isFullRange` true on 100% of records; all series fresh to T-1; `pnl.percent` ranges plausible per model risk (UST -0.26%..0.31% tiny; LTA -5.5%..7.0% widest). Endpoint generalizes — no partial-scope carve-out needed.

## 3. Phase 1 — the swap

### 3.1 SmartX pull (`data/smartx/scripts/pull_smartx_model_monthly_performance.py`)

Extended (B1 monthly logic untouched — zero regression to B1 v1's monthly sidecar). Added `fetch_model_daily` / `build_daily_sidecar` / `crosscheck_daily_vs_monthly`. The Lambda now emits **two** sidecars:

- `_smartx_model_monthly.json` (B1) — the 7 monthly+ periods.
- `_smartx_model_daily.json` (B3, new) — `{schema, generated_at, as_of_date, source, cadence, return_units, model_source_label, models:[{code, model_id, first_date, last_date, record_count, daily:[{date, return_pct, is_full_range}]}]}`. `return_pct` is per-day flow-adjusted return in **percent** (SmartX `pnl.percent` is a decimal fraction → ×100, to match the yang pipeline's percent convention). Record date is `range.end` (the day the return is realized as-of).

**Units verified empirically, not assumed.** `crosscheck_daily_vs_monthly` compounds each model's daily series over the last complete calendar month and compares to the monthly sidecar's 1M — two independent SmartX endpoints. Result, dry-run 2026-05-21: ST/LTA/INT/LTC/UST all **delta = 0.00** (1.11/6.77/4.61/6.18/0.42% on both sides). The daily endpoint's `pnl.percent` units and sign are confirmed correct, and the two SmartX sources agree to the cent.

### 3.2 Producer (`infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py`)

- New `load_smartx_daily_sidecar` + `smartx_daily_period_return` (1D = last record; WTD = compound from Monday of the latest week).
- The period loop: 1D/WTD now sourced from the daily sidecar (`model_source=smartx_realized`); monthly+ unchanged.
- `build_timeseries` now takes the daily sidecar — `model_return` is SmartX-direct.
- Graceful fallback: either sidecar absent → the periods it would supply fall back to yang (`model_source=yang_design`); the producer never hard-fails on a late pull.

### 3.3 Local end-to-end verification (PASS)

Full producer run locally (real `data_20260519_v1.pkl` + live monthly sidecar + locally-built daily sidecar, S3 monkeypatched):

- `model_portfolio_benchmarks.json` — all 9 periods `smartx_realized` for all 5 models. 1D values match the daily sidecar's last record to 2 dp (UST 0.15 / ST 0.37 / INT 0.78 / LTC 0.98 / LTA 1.07).
- `model_portfolio_timeseries.json` — 2050 rows, every row `model_source=smartx_realized`, `model_return` SmartX-direct.

## 4. Artifact-contract deltas (AC5 — for downstream)

1. **`model_portfolio_benchmarks.json`** — 1D/WTD `model_source` flips `yang_design` → `smartx_realized`; the 1D/WTD `model` *values* change (SmartX-realized vs yang-design) and the spreads recompute. `model_source_note` updated. Additive only; no field added/removed.

2. **`model_portfolio_timeseries.json`** — three changes:
   - **New per-row field `model_source`** (additive; consumers ignoring it are unaffected).
   - **Front-truncation.** `model_return` now spans SmartX coverage, which begins after `inception_date` (2024-04-30): ST/LTA/INT/LTC start **2024-09-03** (~4 months lost at the front); **UST starts 2025-02-03 — ~9 months lost** vs inception. The yang return_daily prior to those dates was `model.pkl` design returns — B3 retires them rather than mislabel design as realized.
   - **Trailing model-only rows.** When the SmartX series (T-1 fresh) leads the yang `data.pkl` date, the last 1–2 rows carry `model_return` but `benchmark_return`/`rfr` null (yang has no benchmark for those days). Intermittent — appears only when `data.pkl` lags SmartX; nulls are schema-legal.

3. **New sidecar** `s3://opal-data-portal-v2/json/benchmarks/_smartx_model_daily.json` (internal producer input; not a portal-served artifact).

**Consumer-coordination flag:** deltas 2 (front-truncation, esp. UST ~9mo; trailing model-only rows) affect the `model_portfolio_timeseries.json` consumer — rolling Sharpe + drawdown (MDLP_RVVALT). The producer change is correct as built; whether that consumer wants the early history preserved or the trailing model-only rows trimmed is a consumer-side decision flagged to COO, not resolved unilaterally here.

## 5. Compiler-tools / gate checks

- `.tools/ds-commit-gate.sh` — both files clean (py_compile + ds-precommit-check + ruff py39).
- Phase 0 generalization probe — PASS (§2).
- Daily-vs-monthly fidelity cross-check — delta 0.00 ×5 (§3.1).
- Local producer integration test — PASS (§3.3).

## 6. AE B3-deploy-half

Same DS-author / AE-deploy split as B1/B2. Files for the AE to commit + deploy:
- `data/smartx/scripts/pull_smartx_model_monthly_performance.py` (smartx pull Lambda — now emits 2 sidecars).
- `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py` (the producer).

Deploy order (mirror B2): deploy the pull Lambda first + invoke once so `_smartx_model_daily.json` exists, *then* deploy the producer — no transient window where the producer reads a missing daily sidecar (graceful fallback covers it regardless, but ordering avoids a one-run yang-design 1D/WTD). IAM: the daily sidecar is the same bucket as the monthly — no new permission. On deploy, B1's e2e harness pattern extends naturally to a B3 verification.
