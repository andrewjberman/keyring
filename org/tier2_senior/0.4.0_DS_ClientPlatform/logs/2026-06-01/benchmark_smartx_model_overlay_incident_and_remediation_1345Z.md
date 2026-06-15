# Session Log — Benchmark Comparison: SmartX model-overlay incident, root-cause + remediation

- **Agent:** 0.4.0_DS_ClientPlatform
- **Date:** 2026-06-01 (~13:00–13:50Z)
- **Trigger:** Andrew direct — "explain what is going on between the 1m and MTD numbers and why they are so divergent" on the portal **Benchmark Comparison** tab (Model Portfolios), as-of 2026-05-29 (Friday).
- **Disposition:** Root-caused. Code revert authored (DS) + deployed by AE (live artifact flipped to `yang_design` at 2026-06-01T13:49:07Z). **Three infra remediation items remain — AE-owned (see §7).**
- **Severity:** Investor-facing portal data shown incorrectly (model column inflated, spreads fabricated as outperformance). Data-only; no pipeline outage.

---

## 1. Executive summary

The Benchmark Comparison tab renders three rows per sleeve — **Model**, **Benchmark**, **Spread** — for periods 1D/WTD/MTD/1M/QTD/1Q/YTD/1Y/SI. All three rows are supposed to be **Yang-PKL-derived** (`data.pkl → return_daily`, one consistent trailing/to-date window method, ending on the as-of date).

Between 2026-05-21 and 2026-05-22, project **YALP_MDSRC (tasks B1/B2/B3/B4)** modified the producer Lambda so the **Model** row was **overwritten with SmartX realized monthly/daily performance** instead of being Yang-computed. The Benchmark and Spread rows stayed Yang. This introduced two independent defects:

1. **Window-semantics defect (most visible on 1M).** SmartX's sidecar defines `1M` as **"the last *complete* calendar month"** (= all of April, as-of late May) and `MTD` as the partial current month. Yang's 1M is a **trailing ~30-calendar-day window** ending on the as-of date. So the 1M column was placing the **model's April** next to the **benchmark's trailing-month (≈ May)** — different time periods — which fabricated green "outperformance" on the equity-heavy sleeves. The SmartX `1M` value is also **frozen** (it never changes as new days arrive) because it always points at the prior completed month.
2. **Source-mix defect (all periods).** Even where windows nominally matched, the model leg was SmartX *realized managed-account* performance (monthly-bucket compounded, as-of possibly leading the benchmark by days) while the benchmark leg was Yang *design-index* return (daily compounded). The Spread became a cross-source subtraction on every period.

**The Benchmark rows (both index and ETF) were never wrong.** A separate red herring during investigation: a benchmark MTD-vs-1M gap of >100 bps that initially looked impossible for an as-of of 5/29. It is **legitimate** — it is exactly one extra trading day (**April 30**) that the trailing-1-month window includes and MTD excludes, and April 30 was a strong up-day. The tab was being viewed in **ETF benchmark mode** (`etf_benchmark`), for which April 30 was an especially large day (see §5).

**Fix:** revert the Model leg to Yang for all periods; remove all SmartX sidecar machinery from the Lambda. Done in code; deployed by AE (live `model_source=yang_design`). Remaining: neutralize the latent EC2 dual-writer of the same artifact, deactivate the now-orphaned SmartX sidecar producers, and invalidate CloudFront so the portal stops serving the cached pre-fix copy.

---

## 2. The bug, in code

**Producer Lambda:** `yang-model-portfolio-benchmarks`
- Source: `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py`
- TF resource: `module.model_portfolio_benchmarks.aws_lambda_function.this`
- Artifact: `s3://<lambda-artifacts>/yang-pipeline/yang-model-portfolio-benchmarks.zip`
- Source-map entry: `infra/aws/lambda/ci/lambda-source-map.json` (line ~1209)

**Introducing commits (project YALP_MDSRC):**
| Commit | Date | Author | What |
|---|---|---|---|
| `84128c245` | 2026-05-21 | 0.7.0_AE_CloudOps~A | B2 — "dual-input producer (B1 Artifact 2)": load SmartX monthly sidecar, override model for monthly+ periods (1M/MTD/QTD/1Q/YTD/1Y/SI) |
| `9f6357634` | 2026-05-22 | 0.7.0_AE_CloudOps | B3/B4 — extend override to 1D/WTD from a SmartX daily sidecar; add additive `timeseries_realized` series |

**Override mechanism (pre-revert, in the period loop):** the Lambda computed the Yang value via `calculate_period_returns()`, then discarded it and substituted the SmartX value:
```python
model_source = 'yang_design'
if period in SMARTX_PERIODS:                       # 1M/MTD/QTD/1Q/YTD/1Y/SI
    sx_ret = smartx_sidecar.get(model_code, {}).get(period)
    if sx_ret is not None:
        model_ret = sx_ret                          # <-- yang value thrown away
        model_source = 'smartx_realized'
elif period in SMARTX_DAILY_PERIODS:               # 1D/WTD
    sx_daily_ret = smartx_daily_period_return(smartx_daily.get(model_code), period)
    if sx_daily_ret is not None:
        model_ret = sx_daily_ret
        model_source = 'smartx_realized'
```

**SmartX sidecar period definitions** (producer `data/smartx/scripts/pull_smartx_model_monthly_performance.py`, `compute_periods()`), the source of the window-semantics defect:
```python
out["MTD"] = vals[-1]              # latest PARTIAL month  (e.g. May)
out["1M"]  = vals[-2]              # last COMPLETE month   (e.g. April)   <-- the outlier
out["QTD"] = compound(curr-quarter months incl. partial)
out["1Q"]  = compound(vals[-3:])  # trailing 3 months incl. partial
out["YTD"] = compound(curr-year months incl. partial)
out["1Y"]  = compound(vals[-12:]) # trailing 12 incl. partial
```
Note the incoherence: **only `1M` excludes the partial current month**; every other period includes it. `1Q` is Mar+Apr+May(partial), NOT Feb+Mar+Apr. This is a latent defect inside the sidecar producer regardless of the overlay.

---

## 3. Affected data sources, artifacts, Lambdas, EC2, schedulers (full inventory)

**S3 bucket:** `opal-data-portal-v2` (us-east-1). Versioning: **Enabled** (used for forensics, see §5).

| Artifact (S3 key) | Producer | Consumed by | Status |
|---|---|---|---|
| `json/benchmarks/benchmark_returns.json` (legacy: model/benchmark/spread; benchmark = index) | `yang-model-portfolio-benchmarks` Lambda | portal `getBenchmarkReturns()` | **Fixed** — regenerated 13:49Z, `model_source=yang_design` |
| `json/benchmarks/model_portfolio_benchmarks.json` (comprehensive: model + **index_benchmark** + **etf_benchmark** + spreads) | same Lambda | portal `getModelPortfolioBenchmarks()` — **this is what the Benchmark Comparison tab reads; ETF mode shows `etf_benchmark`** | **Fixed** — regenerated 13:49Z, `model_source=yang_design` |
| `json/benchmarks/model_portfolio_timeseries.json` (`timeseries` design series; previously also additive `timeseries_realized`) | same Lambda | portal rolling Sharpe / max-drawdown (MDLP_RVVALT) reads `timeseries` (Yang, unchanged) | **Fixed** — `timeseries_realized` removed; `timeseries` byte-identical Yang |
| `json/benchmarks/_smartx_model_monthly.json` (B1 monthly sidecar) | `smartx-model-monthly-pull` Lambda (see below) | **Nothing** after revert | **Orphaned producer still running — DEACTIVATE** |
| `json/benchmarks/_smartx_model_daily.json` (B3 daily sidecar) | SmartX daily-direct producer (AE to confirm exact resource) | **Nothing** after revert | **Orphaned producer — DEACTIVATE** |
| `benchmarks/data_YYYYMMDD_v1.pkl` / `benchmarks/LATEST.json` | Yang upload pipeline | the benchmark Lambda (source of truth) | unaffected; current = `data_20260531_v1.pkl`, as-of 2026-05-29 |

**Lambda (primary):** `yang-model-portfolio-benchmarks` — triggered by Step Functions (`YangDataPipeline`) and/or S3 `ObjectCreated` on `benchmarks/*.pkl`. `lambda_handler` supports both event shapes.

**Orphaned SmartX sidecar producer (B1):**
- Lambda `smartx-model-monthly-pull` — TF: `infra/aws/terraform/smartx-pipeline/model-perf-pull.tf`
- Handler: `pull_smartx_model_monthly_performance.lambda_handler` (src `data/smartx/scripts/pull_smartx_model_monthly_performance.py`)
- Schedule: `aws_scheduler_schedule.model_monthly_pull` name `smartx-model-monthly-pull-daily`, `cron(35 9 * * ? *)` America/New_York (09:35 ET daily)
- Writes `_smartx_model_monthly.json` — now consumed by nothing.

**Latent dual-writer (separate risk class — NOT a SmartX leak, but can clobber the fix):**
- `infra/aws/ec2/smartx-exporter/smartx-workspace/scripts/generate_benchmark_performance.py`
- Writes the **same key** `json/benchmarks/benchmark_returns.json` in bucket `opal-data-portal-v2`, from **Yang PKL** (`return_daily`), with its **own** calendar-day period math (`calculate_period_return(df, end_date, days_back)`).
- Lives on the `smartx-exporter` EC2 (`infra/aws/ec2/EC2_MANIFEST.json` → `smartx-exporter`).
- **No EventBridge/cron/autostart reference to it was found** (it is not in `run-all-portfolios.sh`). It appears dormant, but it is a present script that could be invoked and would silently overwrite the Lambda's `benchmark_returns.json` (and crucially it does **not** write `model_portfolio_benchmarks.json`, so a partial clobber would desync the two artifacts).

**Portal consumption note:** the portal consumes **neither** `model_source` **nor** `timeseries_realized` (grep-confirmed across `portal/src`). The revert is therefore FE-transparent — only the numbers correct themselves; no schema break. The Benchmark Comparison tab toggles `benchmarkType` index|etf and reads `model_portfolio_benchmarks.json` (`index_benchmark` / `etf_benchmark`).

---

## 4. The fix (code) — committed scope

File: `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py` (net diff +36 / −224).

- Removed the per-period SmartX override → `model_ret` stays the `calculate_period_returns()` Yang value; `model_source='yang_design'` on every period.
- Removed `load_smartx_sidecar`, `load_smartx_daily_sidecar`, `smartx_daily_period_return`, `build_timeseries_realized`, the `timeseries_realized` output key, and the `SMARTX_*` constants.
- `timeseries` (Yang, read by MDLP_RVVALT) left untouched → zero regression there.
- Gate: `python -m py_compile` PASS; `ruff check --target-version py39` PASS.

**Lane note:** `infra/aws/**` is the AE_CloudOps owned-path lane; `safe-commit.sh` correctly blocked DS from committing. Change was routed to `0.7.0_AE_CloudOps` via `[DEPLOY-REQUEST]` (broker msg `20260601T133513Z`). AE ACK'd and deployed; the live artifacts (generated `2026-06-01T13:49:07Z`) confirm `model_source=yang_design`, so the **Model leg is corrected in PROD**.

---

## 5. Evidence / forensic trail (numbers)

**The QTD = 1M ⊕ MTD identity proved the model's 1M was April** (pre-fix INT model values): `(1+4.61%)×(1+1.71%) = 1.0640 = QTD` ⇒ 1M=April, MTD=May, QTD=Apr+May.

**S3 object-version forensics** (`benchmark_returns.json`, versioning enabled): no regeneration occurred between 2026-05-26 13:43 and 2026-05-31 21:45 (artifact live 5 days). The pre-revert version (5/31 21:45, `model_source=smartx_realized`) had LTA model 1M=6.77 (frozen April); the SmartX model 1M was identical (6.77) across the 5/21, 5/22, 5/26, 5/31 versions — confirming the "frozen last-complete-month" behaviour.

**The screenshot Andrew saw was the ETF benchmark**, confirmed by exact match against `model_portfolio_benchmarks.json` `etf_benchmark`:

| | screenshot | index_bench | etf_bench |
|---|---|---|---|
| ST MTD | 0.94 | 1.03 | **0.94** |
| ST 1M | 1.30 | 1.27 | **1.30** |
| LTA MTD | 3.96 | 4.46 | **3.96** |
| LTA 1M | 5.41 | 5.29 | **5.41** |

**The benchmark MTD-vs-1M gap is one day (April 30), legitimate** (recomputed from `data_20260531_v1.pkl`):

| ETF benchmark | MTD (May1–29) | 1M (Apr30–May29) | Gap | = April 30 single day |
|---|---|---|---|---|
| INT (60% eq) | 2.88 | 3.93 | +1.05 | +1.022% |
| LTA (85% eq) | 3.96 | 5.41 | +1.45 | +1.389% |
(Index benchmark April 30 was smaller, +0.59% INT / +0.79% LT — an ETF-vs-index tracking difference on that day. More equity weight ⇒ bigger April 30 ⇒ bigger gap. Not an error.)

**Corrected model (post-revert, Yang, same trailing window) — live artifact 13:49Z:**

| Sleeve | Model 1M (was full-April) | Model 1M (now trailing) | index_bench 1M | etf_bench 1M |
|---|---|---|---|---|
| ST | 1.11 | 0.73 | 1.27 | 1.30 |
| INT | 4.61 | 2.95 | 3.84 | 3.93 |
| LTC | 6.18 | 3.85 | 5.29 | 5.41 |
| LTA | 6.77 | 4.08 | 5.29 | 5.41 |

The fabricated green 1M spreads now flip negative (e.g. LTA 1M spread vs ETF: +1.36 🟢 → −1.33 🔴), consistent with MTD/QTD/1Q and with reality (the models trailed the benchmark recently / through April).

---

## 6. Why the portal still showed the bug (cache)

The pre-fix screenshot is **older than the artifact that was in S3 when investigation began** (screenshot ST etf-bench MTD 0.94 / as-of ≈5/28 vs S3's as-of 5/29 values). CloudFront was serving a **cached** copy. Distribution **`EVTSA9VEHNZVH`** ("opalinvest.dev portal distribution", aliases `opalinvest.dev`/`www.opalinvest.dev`) has a `json_tiered_5min` cache policy on the JSON origin, but the served object predated S3 — so an explicit invalidation is required to guarantee the fresh artifact reaches users.

- Origin serving these JSONs: `S3-opal-data-portal-v2-json` → bucket `opal-data-portal-v2`.
- Portal fetch path (from `portal/src/api/portal-proxy.ts`): `/api/general/benchmarks/benchmark_returns.json` and `/api/general/benchmarks/model_portfolio_benchmarks.json`.

---

## 7. AE ACTION ITEMS (owned by 0.7.0_AE_CloudOps)

> The Model-leg fix is already deployed (live `yang_design` @ 13:49Z). These items make it durable and visible.

**A. Re-run / confirm the producer Lambda.**
- `yang-model-portfolio-benchmarks` already regenerated all three artifacts at 13:49Z with `model_source=yang_design`. Confirm the deployed code matches the reverted source (DEPLOY-REQUEST `20260601T133513Z`). If any doubt, re-invoke (Step Functions `YangDataPipeline` or a manual invoke against `benchmarks/LATEST.json` → `data_20260531_v1.pkl`) and verify 0-diff plan first per CLAUDE.md Rule 1–6.

**B. Neutralize the EC2 dual-writer.**
- `infra/aws/ec2/smartx-exporter/smartx-workspace/scripts/generate_benchmark_performance.py` writes the same `benchmark_returns.json`. Confirm it is **not** invoked by any cron/autostart/SSM on the `smartx-exporter` instance; then disable/remove it (or repoint it away from the live key) so it can never clobber the Lambda output. Record in `EC2_MANIFEST.json`. (It is Yang-sourced, not a SmartX leak — but it carries its own period math and only writes the legacy file, so a clobber would also desync legacy vs comprehensive.)

**C. Deactivate the orphaned SmartX sidecar producers.**
- Disable `aws_scheduler_schedule.smartx-model-monthly-pull-daily` (cron 09:35 ET) — Lambda `smartx-model-monthly-pull`, TF `infra/aws/terraform/smartx-pipeline/model-perf-pull.tf`. Writes `_smartx_model_monthly.json`, now consumed by nothing.
- Identify + disable the **B3 daily** producer writing `_smartx_model_daily.json` (sibling resource). 
- Both via Terraform (set schedule disabled / remove resource), commit → plan → apply → 0-diff per deployment rules. (Leaving them running is harmless to the artifact but wastes a SmartX seat and leaves a re-wire footgun; the `compute_periods` window incoherence in §2 lives in that producer.)

**D. Invalidate CloudFront.**
- Distribution **`EVTSA9VEHNZVH`**. Invalidate the benchmark JSON paths so the portal stops serving the cached pre-fix copy:
  - `/api/general/benchmarks/benchmark_returns.json`
  - `/api/general/benchmarks/model_portfolio_benchmarks.json`
  - (broad-safe: `/api/general/benchmarks/*` and `/json/benchmarks/*`)
- Confirm exact behavior path-pattern mapping in `infra/aws/terraform/portal-auth/cloudfront-distribution.tf` before invalidating.

**E. Verify end-to-end (post-invalidation).**
- Reload the Benchmark Comparison tab (ETF mode) and confirm: model 1M = trailing-window Yang value (e.g. LTA 4.08, not 6.77); 1M spreads consistent (negative) with MTD/QTD/1Q; benchmark unchanged (ETF LTA MTD 3.96 / 1M 5.41 — correct, April-30 one-day gap).

---

## 8. Notes for the record

- **The 100+ bps benchmark MTD-vs-1M gap is correct and should not be "fixed."** It is one strong trading day (April 30) included in the trailing-month window but excluded from MTD. Documented here so it is not re-flagged as a defect.
- **`1M` semantics divergence was unique to the model leg.** Index/ETF benchmarks always used Yang's trailing window consistently across periods. After revert, model and benchmark share the same window on every period.
- If a deliberate "last completed calendar month" column is ever wanted, it must be applied to **both** legs (model and benchmark) with the same month — not as a one-sided model overlay.

## Compiler Tools

| Tool | Run? | Result |
|---|---|---|
| comp-pipescript io/deployed/postdeps | N/A | Not a `data/*/scripts/{gold,silver,bronze}` edit — the change is to an `infra/aws/lambda` Lambda (AE lane). No gold-script IO map applies. |
| comp-validate | N/A | No gold artifact produced; forensic + Lambda-source change. |
| comp-transform schema-check | N/A | No portal component edited; FE-transparent (portal reads neither `model_source` nor `timeseries_realized`). |
| ds-commit-gate (py_compile / ruff py39) | **Yes** | PASS / PASS on the edited `lambda_function.py`. |

(Forensic data-investigation + infra-Lambda revert; standard comp-pipescript/comp-validate gold gates do not apply. py_compile + ruff run per CLAUDE.md Rule 14.)
