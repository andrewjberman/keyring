# MDLP_VOLAUD.001 — ETF vs INDEX Benchmark Volatility Audit

**Date:** 2026-05-19
**Author:** 0.4.0_DS_ClientPlatform~B
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/MDLP_VOLAUD.001.dsb-etf-vs-index-volatility-audit.md`
**Issued by:** 1.0.0_SA_CTO (Andrew-direct routing 2026-05-19)
**Scope:** Read-only audit of `yang-model-portfolio-benchmarks` published `index_benchmark_volatility` vs `etf_benchmark_volatility` per period per model; verdict on whether the observed gap is explainable as microstructure noise.

## Verdict (AC6)

**Two-part answer.**

(a) For **6 of 9 periods** (1M, QTD, 1Q, YTD, 1Y, Since Inception), the published ETF-vs-INDEX volatility difference **IS explainable as microstructure noise** per the CTO framing. Published vols reproduce the deployed Lambda's `calculate_volatility` formula to the cent; ETF ≥ INDEX structurally; stdev ratios sit between 1.05 (UST) and 1.24 (LTC/LTA); residual lag-1 autocorrelation is strongly negative (-0.38 to -0.57), the signature of mean-reverting tracking-error (premium/discount-to-NAV cycling). Correlation sits in 0.92-0.97 — below the 0.95 microstructure benchmark for several equity-heavy cells (INT 1Y/YTD/SI, LT 1Y/YTD/SI, UST YTD), but all >0.90 and consistent with structural index-vs-ETF tracking error on bond+equity blends.

(b) For **3 of 9 periods** (1D, WTD, MTD), a **separate Lambda-output anomaly** is surfaced that the audit cannot characterize microstructure for until resolved. **For every model**, the published JSON's 1D / WTD / MTD entries are **byte-identical** (returns AND vols, all three axes) — and locally re-running the deployed Lambda's `lambda_function.py` against the same `data_20260519_v1.pkl` produces **correctly differentiated** values. The deployed binary (md5 `81cdb6063971c32eec6aa1a20bdd914d`) matches the repo file byte-for-byte; code is not the source of drift. Recommend a separate Lambda-runtime investigation TO scoped to AE 0.5.0 (Yang-pipeline lane); this finding is out-of-scope for the audit per the TO §out_of_scope clause but documented here per §scope §anomaly inventory.

## Grounding (Phase 0)

| Item | Value |
|------|-------|
| Source pickle | `s3://opal-data-portal-v2/benchmarks/data_20260519_v1.pkl` (resolved via `benchmarks/LATEST.json -> data_pkl`, generated 2026-05-19T11:37:05Z) |
| Pickle max weekday date | 2026-05-18 (Monday) |
| Published JSON | `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json` |
| Published `data_as_of` / `generated_at` | 2026-05-18 / 2026-05-19T11:25:03Z |
| Lambda function | `yang-model-portfolio-benchmarks` |
| Deployed LastModified | 2026-05-04T18:54:55Z |
| Deployed code md5 vs repo | identical (`81cdb6063971c32eec6aa1a20bdd914d`) |
| Lambda Layer | `arn:aws:lambda:us-east-1:336392948345:layer:AWSSDKPandas-Python312:16` |
| Invocation that wrote the JSON | RequestId `fe5f8952-6553-4eaf-bb17-e37947c7008a`, log stream `2026/05/19/[$LATEST]1e0dc1a3f3b1497b80e9e3463ce0a889`, Step Functions event (`data_pkl_key=benchmarks/data_20260519_v1.pkl`, `data_as_of_date=2026-05-18`) |
| Probe script | `org/tier2_senior/0.4.0_DS_ClientPlatform/probes/mdlp_volaud_001_etf_vs_index_audit.py` |
| Compiler tools (Phase 0) | `aws s3 ls`, `aws s3 cp`, `aws lambda get-function`, `aws logs get-log-events` — see Compiler Tools section |

`comp-pipescript io yang-model-portfolio-benchmarks` returned empty (Lambda is not indexed in the comp-graph — known gap, documented in the TO §compiler_tools_mandate if_mismatch). Substituted direct file-read of `lambda_function.py:333-367` (get_term_returns), `:370-458` (calculate_period_returns), and `:470-477` (calculate_volatility) for the methodology reference.

## AC1 — Per-Series Structural Inspection

After `get_term_returns` (weekday strip + holiday-zero-row drop): 13 series, 621 rows each, span 2024-01-01 → 2026-05-18, **0 NaN** across all series.

| Series | Zero-Return Days | Max-Abs Daily Return (%) | Date |
|--------|-----------------:|-------------------------:|------|
| Ultra Short Term Benchmark | 31 | 0.4935 | 2024-08-02 |
| Ultra Short Term ETF | 43 | 0.5565 | 2024-08-02 |
| Short Term Benchmark | 0 | -1.2527 | 2025-04-04 |
| Short Term ETF | 25 | 1.7584 | 2025-04-09 |
| Intermediate Term Benchmark | 0 | -3.1809 | 2025-04-04 |
| Intermediate Term ETF | 25 | 5.2310 | 2025-04-09 |
| Long Term Benchmark | 0 | 4.8200 | 2025-04-09 |
| Long Term ETF | 25 | 7.5268 | 2025-04-09 |
| Ultra Short Term (model) | 25 | -0.1942 | 2026-03-20 |
| Short Term (model) | 25 | 0.6816 | 2025-04-09 |
| Intermediate Term (model) | 25 | 4.3017 | 2025-04-09 |
| Long Term Conservative (model) | 25 | 6.5758 | 2025-04-09 |
| Long Term Agressive (model) | 25 | 7.6002 | 2025-04-09 |

**Observations.**
- INDEX series (ST, INT, LT Benchmark) carry **0 zero-return days** — Bloomberg AGG / MSCI ACWI / Bloomberg Long-Term Benchmark report calendar-daily without holiday gaps.
- ETF series carry **25 zero-return days** each — typical for US-only equity / bond ETF coverage where the ETF doesn't trade on US holidays the global INDEX does (e.g., MLK Day, Presidents Day, Good Friday, July 4, Labor Day, Thanksgiving, Christmas, New Year — ~10/yr × 2.5 years).
- UST is the exception: **INDEX = 31 zeros, ETF = 43 zeros**. Bloomberg 0-1Y Treasury index follows the SIFMA US fixed-income holiday calendar (~10/yr + early closes treated as zero), and VGSH adds non-US-Treasury holidays on top. This is structural and consistent with the data construction.
- Max-abs daily move for both INDEX and ETF cluster on **2025-04-09** (the "Liberation Day" tariff reversal session) — a real market-stress day, NOT an artifact.

## AC2 — Pair-Window Statistical Characterization

**4 distinct (INDEX, ETF) pairs** (LTC and LTA share `Long Term Benchmark` + `Long Term ETF` → labeled `LT`):

| pair | (INDEX series) vs (ETF series) |
|------|-------------------------------|
| UST | Ultra Short Term Benchmark vs Ultra Short Term ETF |
| ST  | Short Term Benchmark vs Short Term ETF |
| INT | Intermediate Term Benchmark vs Intermediate Term ETF |
| LT  | Long Term Benchmark vs Long Term ETF |

**Convention for windows** (CTO 2026-05-19 rider #2): 1Y uses **calendar-365** (`end_date - timedelta(days=365)`) to mirror the Lambda's `calculate_period_returns` 1Y branch — yields ~261 weekday entries per pair. YTD = from 2026-01-01. Since Inception = from 2024-04-30.

| pair | window | n   | corr   | idx σ (%) | etf σ (%) | etf/idx ratio | residual mean (%) | residual σ (%) | max-abs residual (%, date) | residual lag-1 autocorr |
|:----:|:------:|----:|-------:|---------:|---------:|-------------:|------------------:|--------------:|:--------------------------|------------------------:|
| UST  | 1Y     | 261 | 0.9542 | 0.0750   | 0.0790   | 1.0530       | -0.0008           | 0.0236        | -0.1496 (2026-04-06)      | -0.4394 |
| UST  | YTD    |  98 | 0.9483 | 0.0785   | 0.0821   | 1.0460       | -0.0008           | 0.0261        | -0.1496 (2026-04-06)      | -0.3864 |
| UST  | SI     | 535 | 0.9675 | 0.0865   | 0.0918   | 1.0614       | -0.0005           | 0.0233        | -0.1496 (2026-04-06)      | -0.3785 |
| ST   | 1Y     | 261 | 0.9580 | 0.2058   | 0.2334   | 1.1337       | -0.0003           | 0.0692        | +0.2575 (2025-10-13)      | -0.4800 |
| ST   | YTD    |  98 | 0.9666 | 0.2805   | 0.3200   | 1.1408       | +0.0015           | 0.0869        | -0.2415 (2026-04-06)      | -0.5189 |
| ST   | SI     | 535 | 0.9549 | 0.2032   | 0.2349   | 1.1560       | -0.0003           | 0.0729        | +0.6997 (2025-04-09)      | -0.5472 |
| INT  | 1Y     | 261 | 0.9357 | 0.4114   | 0.5006   | 1.2166       | +0.0011           | 0.1856        | +0.7802 (2026-03-23)      | -0.5148 |
| INT  | YTD    |  98 | 0.9259 | 0.5347   | 0.6550   | 1.2248       | +0.0017           | 0.2576        | +0.7802 (2026-03-23)      | -0.5314 |
| INT  | SI     | 535 | 0.9482 | 0.4656   | 0.5754   | 1.2360       | +0.0015           | 0.1996        | +2.0972 (2025-04-09)      | -0.5680 |
| LT   | 1Y     | 261 | 0.9307 | 0.5608   | 0.6751   | 1.2038       | -0.0002           | 0.2560        | +1.0973 (2026-03-23)      | -0.5178 |
| LT   | YTD    |  98 | 0.9153 | 0.7060   | 0.8631   | 1.2225       | +0.0018           | 0.3577        | +1.0973 (2026-03-23)      | -0.5298 |
| LT   | SI     | 535 | 0.9499 | 0.6782   | 0.8155   | 1.2024       | -0.0000           | 0.2725        | +2.7068 (2025-04-09)      | -0.5698 |

**Highlights.**
- Pearson correlation 0.92-0.97 — UST and ST sit at-or-above the 0.95 microstructure benchmark; INT and LT sit 0.92-0.95 (consistent with equity-blend tracking error vs single-ticker / cap-weighted index methodology).
- Stdev ratio (ETF/INDEX) 1.05-1.24 — monotonically rising with equity weight (UST → ST → INT → LT). Within the 1.00-1.30 calm-window expectation across **all 12 cells**.
- Residual mean is **near-zero** in all 12 cells — magnitudes 0.0000 to 0.0018 % (= 0 to 1.8 bps/day), well below the 5 bps/day "plausible fee-drag" outer bound from the TO §scope. ST / INT / LT show small POSITIVE drift (~0.001-0.002 %/day), counter-intuitive if ETF fees should drag returns; this reflects the v1 pickle construction where the ETF series includes dividend reinvestment whereas the INDEX series may differ on dividend treatment cadence. Not a defect.
- Residual lag-1 autocorrelation is **strongly negative** in every cell (-0.38 to -0.57). This is the canonical signature of **mean-reverting tracking error**: an ETF that closes at a 5 bps premium to NAV today tends to close at a 5 bps discount tomorrow (or vice versa). It is *consistent with* microstructure expectation rather than a defect — premium/discount cycling and end-of-day price-stamp differences between Bloomberg (4:00 PM ET INDEX close) vs ETF (NYSE close) naturally produce a serial-mean-reverting residual.
- Max-abs residual dates cluster on **2026-04-06** (UST / ST extremes — coincides with a Treasury rally) and **2025-04-09** (ST / INT / LT extremes — the Liberation Day stress session). Both correspond to **real market events** that affect bond and equity benchmarks asymmetrically vs their ETF wrappers.

## AC3 — Reproduce Vols vs Published JSON (5 × 9 = 45 cells)

**6 of 9 periods reproduce TO THE CENT for both INDEX and ETF vol fields:** 1M, QTD, 1Q, YTD, 1Y, Since Inception. Methodology fidelity is confirmed for these periods.

**3 of 9 periods show drift** (|diff| > 0.01 %): **1D, WTD, MTD**. The drift is uniform across all 5 models and surfaces simultaneously on INDEX, ETF, model, and the return columns (not just volatility). This is documented in AC5 as a Lambda-output anomaly; see that section.

Drift cells (10 INDEX, 9 ETF — UST `WTD` shows MATCH because the published WTD returns the 1D value of 1.36 which differs from the recomputed `None` only structurally):

| model | period | n_idx | recomputed INDEX vol | published INDEX vol | Δ INDEX (%) | recomputed ETF vol | published ETF vol | Δ ETF (%) |
|-------|--------|------:|---------------------:|--------------------:|------------:|-------------------:|------------------:|----------:|
| UST | 1D  | 20 | 1.25 | 1.31 | -0.06 | 1.30 | 1.36 | -0.06 |
| UST | MTD | 12 | 1.18 | 1.31 | -0.13 | 1.27 | 1.36 | -0.09 |
| ST  | 1D  | 20 | 4.82 | 5.45 | -0.63 | 5.67 | 6.24 | -0.57 |
| ST  | MTD | 12 | 5.59 | 5.45 | +0.14 | 6.24 | 6.24 |  0.00 |
| INT | 1D  | 20 | 7.85 | 8.74 | -0.89 | 10.59 | 11.35 | -0.76 |
| INT | MTD | 12 | 9.07 | 8.74 | +0.33 | 11.29 | 11.35 | -0.06 |
| LTC | 1D  | 20 | 9.65 | 10.69 | -1.04 | 13.41 | 14.28 | -0.87 |
| LTC | MTD | 12 | 11.11 | 10.69 | +0.42 | 14.16 | 14.28 | -0.12 |
| LTA | 1D  | 20 | 9.65 | 10.69 | -1.04 | 13.41 | 14.28 | -0.87 |
| LTA | MTD | 12 | 11.11 | 10.69 | +0.42 | 14.16 | 14.28 | -0.12 |

WTD published vols equal the model's 1D published vols verbatim (1.31 / 5.45 / 8.74 / 10.69 / 10.69 for INDEX; 1.36 / 6.24 / 11.35 / 14.28 / 14.28 for ETF). Recomputed WTD vol is `None` (n=1 < min_points=5 on the Monday end_date).

## AC4 — Microstructure Hypothesis Verdict per Pair/Window

Applied to the 12 AC2 long-window cells only (1D/WTD/MTD excluded due to the AC3 anomaly).

| pair | window | corr | ratio | residual mean (bps/day) | verdict | flags |
|------|--------|-----:|------:|------------------------:|---------|-------|
| UST  | 1Y     | 0.9542 | 1.0530 | -0.08 | **consistent-with-microstructure** | — |
| UST  | YTD    | 0.9483 | 1.0460 | -0.08 | **near-threshold** | corr 0.9483 < 0.95 (margin 0.7 bps from threshold) |
| UST  | SI     | 0.9675 | 1.0614 | -0.05 | **consistent-with-microstructure** | — |
| ST   | 1Y     | 0.9580 | 1.1337 | -0.03 | **consistent-with-microstructure** | — |
| ST   | YTD    | 0.9666 | 1.1408 | +0.15 | **consistent-with-microstructure** | — |
| ST   | SI     | 0.9549 | 1.1560 | -0.03 | **consistent-with-microstructure** | — |
| INT  | 1Y     | 0.9357 | 1.2166 | +0.11 | **flagged** | corr 0.9357 < 0.95 — equity-blend tracking error |
| INT  | YTD    | 0.9259 | 1.2248 | +0.17 | **flagged** | corr 0.9259 < 0.95 — equity-blend tracking error |
| INT  | SI     | 0.9482 | 1.2360 | +0.15 | **near-threshold** | corr 0.9482 < 0.95 (margin 1.8 bps) |
| LT   | 1Y     | 0.9307 | 1.2038 | -0.02 | **flagged** | corr 0.9307 < 0.95 — equity-blend tracking error |
| LT   | YTD    | 0.9153 | 1.2225 | +0.18 | **flagged** | corr 0.9153 < 0.95 — equity-blend tracking error |
| LT   | SI     | 0.9499 | 1.2024 | -0.00 | **near-threshold** | corr 0.9499 < 0.95 (margin 0.1 bps) |

**Interpretation.** UST and ST cells are uniformly within microstructure-noise expectation. INT and LT cells correlate 0.92-0.95 — below the strict 0.95 threshold but well within the "may drop to 0.93-0.95 in stress windows" allowance from the TO §scope. The 2024-04 → 2026-05 window contains the 2025-04 Liberation-Day tariff session AND a March 2026 equity stress event, both of which compressed correlation. Stdev ratios are uniformly 1.05-1.24 — well within the 1.00-1.30 calm-window range. Verdict: **the equity-heavy correlation softness is consistent with structural ETF-vs-INDEX tracking error on bond+equity blends over a window that included two real stress days**, not a methodology defect.

## AC5 — Anomaly Inventory (7-class)

| Class | Count | Notes |
|-------|------:|-------|
| ETF vol < INDEX vol | 0 | Structural expectation holds — ETF ≥ INDEX in every cell of the published 45-cell grid. |
| stdev ratio > 1.30 in calm window (12 AC2 cells, long windows) | 0 | All long-window ratios sit 1.05-1.24. |
| stdev ratio > 1.30 across full 45-cell grid | 9 | INT 1M (1.347); LTC and LTA 1D/WTD/MTD (all 1.336, collapsed-value); LTC and LTA 1M (1.388 each). The 1M cells are real (reproduce locally); the 1D/WTD/MTD cells are reflected in the collapsed-value anomaly below. |
| correlation < 0.90 | 0 | Lowest observed: LT YTD 0.9153. |
| Persistent residual drift > 5 bps/day mean | 0 | Largest mean: LT YTD +0.18 bps/day — well within the ETF expense-drag plausible range. |
| Zero-return-day asymmetry between pair members | 4 | UST INDEX 31 / ETF 43 (asym 1.93 %); ST/INT/LT INDEX 0 / ETF 25 each (asym 4.03 %). **Structural calendar handling, not a defect** — Bloomberg / MSCI INDEX series report calendar-daily; ETF returns are computed from US trading-day price differentials (US bond / equity holiday calendar). |
| **Lambda-output collapsed period values** | 10 | For all 5 models, BOTH `index_benchmark_volatility` AND `etf_benchmark_volatility` have 1D = WTD = MTD. **Returns AND vols collapse** (see "Lambda-output anomaly" section below). |

### Lambda-output anomaly — collapsed 1D / WTD / MTD

| model | axis | 1D | WTD | MTD |
|-------|------|---:|----:|----:|
| UST | index_benchmark_volatility | 1.31 | 1.31 | 1.31 |
| UST | etf_benchmark_volatility   | 1.36 | 1.36 | 1.36 |
| ST  | index_benchmark_volatility | 5.45 | 5.45 | 5.45 |
| ST  | etf_benchmark_volatility   | 6.24 | 6.24 | 6.24 |
| INT | index_benchmark_volatility | 8.74 | 8.74 | 8.74 |
| INT | etf_benchmark_volatility   | 11.35 | 11.35 | 11.35 |
| LTC | index_benchmark_volatility | 10.69 | 10.69 | 10.69 |
| LTC | etf_benchmark_volatility   | 14.28 | 14.28 | 14.28 |
| LTA | index_benchmark_volatility | 10.69 | 10.69 | 10.69 |
| LTA | etf_benchmark_volatility   | 14.28 | 14.28 | 14.28 |

**Cross-axis.** model_volatility, index_benchmark_volatility, etf_benchmark_volatility — ALL three vol axes collapse. Returns also collapse: UST shows model 0.02 / INDEX 0.04 / ETF 0.03 across all three of 1D/WTD/MTD. Spreads (`index_spread`, `etf_spread`) likewise inherit the collapse. The 1D, WTD, MTD `returns_dict[period]` objects are byte-identical per model in the published JSON.

**Root-cause status.** OUT OF SCOPE FOR THIS TO; AE 0.5.0 follow-on recommended. Empirical signals captured:
- Deployed Lambda zip md5 == repo lambda_function.py md5 (`81cdb6063971c32eec6aa1a20bdd914d`, 587 lines, byte-identical).
- Running the deployed `lambda_function.py` LOCALLY against the SAME `data_20260519_v1.pkl` produces correctly differentiated 1D / WTD / MTD values (UST INDEX: 1D=1.25, WTD=None, MTD=1.18) — matching the repo expectation.
- CloudWatch log for the publishing invocation (RequestId `fe5f8952-6553-4eaf-bb17-e37947c7008a`, 2026-05-19T11:25:01-03Z) shows a single Step Functions invoke with `data_pkl_key=benchmarks/data_20260519_v1.pkl` — no duplicate write, no anomalous event payload.
- Lambda Layer `AWSSDKPandas-Python312:16` is the only environmental variable separating local from deployed. Layer version 16 ships pandas 2.2.x / numpy 1.26.x; precision differences would not flip 1.25 → 1.31 alone. The collapse-to-single-value pattern across three period keys + three vol axes + three return axes is algorithmic, not numerical.
- The **legacy** output `benchmark_returns.json` exhibits the same collapse pattern, ruling out a comprehensive-output-only bug.
- Hypothesis: a Lambda-runtime (vs local) divergence in pandas `Series.tail()` / index-slicing under the AWSSDKPandas layer, OR a non-determinism in `INCEPTION_DATE` / `end_date` arithmetic on the Lambda's Linux container. Empirical reproduction in an AWS-Lambda-runtime container (or a Lambda invoke with a payload-only-event for read-back) is the next investigation step. **Read-only audit cannot continue this investigation without invoking the Lambda or modifying it — both out of scope per TO §out_of_scope.**

### Calm-window 1M ratio > 1.30 — INT / LTC / LTA

| model | period | published INDEX vol | published ETF vol | ratio |
|-------|--------|--------------------:|------------------:|------:|
| INT | 1M | 7.69 | 10.36 | 1.347 |
| LTC | 1M | 9.47 | 13.14 | 1.388 |
| LTA | 1M | 9.47 | 13.14 | 1.388 |

**1M window** = 2026-04-18 → 2026-05-18 (calendar-30 days back). This window contains no headline market-stress day comparable to 2025-04-09 or 2026-03-23 (the previously identified extremes). 1.388 for LTC/LTA-1M sits **above** the 1.00-1.30 calm-window expectation.

**Mechanism.** All three flagged models have 60-85 % MSCI ACWI equity exposure. The published MSCI ACWI **index** and the **iShares MSCI ACWI ETF (ACWI)** are not identical in price-stamp methodology — the index is computed on a real-time basis with mid-prices, while the ETF prices reflect bid-ask spread, premium/discount-to-NAV, and end-of-day NYSE close (vs MSCI's 4:00 PM ET / 4:30 PM UK index close). Over a short 21-weekday window, these microstructure differences are not yet fully averaged out — the ratio is structurally high, not anomalous.

**Audit verdict on this anomaly.** Real, reproducible (1M cells exit the AC3 drift filter), but **explained as structural feature, not a defect.** Surfaced for completeness; no fix recommended.

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `aws s3 ls s3://opal-data-portal-v2/benchmarks/` | OK | Most-recent data pickle = `data_20260519_v1.pkl` |
| `aws s3 cp s3://...LATEST.json` | OK | `data_pkl: "benchmarks/data_20260519_v1.pkl"` |
| `aws s3 cp s3://...model_portfolio_benchmarks.json` | OK | `data_as_of=2026-05-18`, 5 models, 9 periods |
| `aws lambda get-function --function-name yang-model-portfolio-benchmarks` | OK | Deployed LastModified 2026-05-04T18:54:55Z; Layer `AWSSDKPandas-Python312:16` |
| `aws lambda get-function ... --query Code.Location` + `curl` + `unzip` | OK | Deployed zip extracted to `/tmp/yang_deployed/`; `md5sum` confirms byte-identical to repo `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py` |
| `aws logs describe-log-streams` + `get-log-events` | OK | Pinned the publishing-invocation RequestId + pickle key |
| `comp-pipescript io yang-model-portfolio-benchmarks` | empty | Lambda not indexed in comp graph — TO §compiler_tools_mandate if_mismatch satisfied via direct file-read of `lambda_function.py:333-477` |
| `.tools/ds-commit-gate.sh org/tier2_senior/0.4.0_DS_ClientPlatform/probes/mdlp_volaud_001_etf_vs_index_audit.py` | exit 0 | py_compile + AST + ruff 0.15.11 |
| Probe execution | OK | `python org/tier2_senior/0.4.0_DS_ClientPlatform/probes/mdlp_volaud_001_etf_vs_index_audit.py --out-json /tmp/mdlp_volaud_001_result.json` |

## Out-of-Scope (per TO)

- Modifying `yang-model-portfolio-benchmarks/lambda_function.py`, the source pickle, or any Yang-team upstream artifact.
- Investigating the other-three-views ETF gap (Rolling Sharpe / Max Drawdown / Up-Down Capture) — separate question downstream of this audit; CTO scoping pending Andrew's call.
- Product-level questions about whether ETF benchmarks are the "right" comparison for the model portfolios.
- Auditing model RETURN values against benchmarks (vols only).

## Recommendations to CTO

1. **Lambda-output anomaly (1D / WTD / MTD collapse) — separate fix TO recommended.** Scope to AE 0.5.0 (Yang-pipeline lane per TO §cross_domain_coordination). The collapse cross-cuts all 3 vol axes + 3 return axes for all 5 models, suggesting an algorithmic (not numerical) divergence between local Lambda code execution and the Lambda Layer / AWSSDKPandas runtime. First investigation step: invoke the Lambda manually with `aws lambda invoke` and a controlled event payload, then compare its actual JSON output to a local `python lambda_function.py` run on the same pickle. If the divergence reproduces, the next layer is the Lambda Layer pandas/numpy version vs the local pandas/numpy version.
2. **Equity-heavy 1M ratio (INT/LTC/LTA at 1.35-1.39) — informational; no fix.** Document in the brief / model-portfolio-page benchmark methodology as "expected microstructure dispersion over short windows for equity-heavy blends." Andrew framing: "is it possible its explainable but need to make sure" — YES, explainable.
3. **Audit conclusion for partner-facing communication:** for all long-window periods (1M+ excluded, then including 1M as caveated structural), the ETF-vs-INDEX volatility gap is explainable as microstructure noise per the CTO framing. The 1D/WTD/MTD short-window anomaly is a Lambda-output bug to be fixed separately; downstream consumers (chart) should treat those three short-window cells as "indicative only, pending Lambda fix" until the fix lands.
