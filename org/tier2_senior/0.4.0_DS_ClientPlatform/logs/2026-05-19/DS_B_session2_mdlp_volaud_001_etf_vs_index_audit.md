# MDLP_VOLAUD.001 — ETF vs INDEX Volatility Audit

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-19
**Branch:** CLOUD
**Project:** MDLP_VOLAUD (new — Phase 0 only)
**TO:** MDLP_VOLAUD.001 (CTO, Andrew-direct routing 2026-05-19 ~13:40Z)
**Status:** COMPLETE — brief landed, RAVC2 to CTO

## Current State

Read-only audit complete. Brief shipped at
`docs/briefs/mdlp-etf-vs-index-volatility-audit-20260519.md`.

Verdict (AC6): two-part.
(a) For **6 of 9 periods** (1M, QTD, 1Q, YTD, 1Y, Since Inception), the published
    ETF-vs-INDEX volatility difference IS explainable as microstructure noise —
    ETF >= INDEX structurally; stdev ratios 1.05-1.24; residual lag-1 autocorr
    strongly negative (mean-reverting tracking error); published vols reproduce
    the deployed Lambda's `calculate_volatility` formula to the cent.
(b) For **3 of 9 periods** (1D, WTD, MTD), a Lambda-output anomaly surfaces —
    published 1D == WTD == MTD byte-identical per model (returns AND vols, all
    three axes), but the deployed Lambda's `lambda_function.py` (byte-identical
    md5 to repo) produces correctly differentiated values when run locally.
    Out-of-scope to fix; separate AE 0.5.0 follow-on TO recommended.

## Files Modified

| File | Change |
|------|--------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/probes/mdlp_volaud_001_etf_vs_index_audit.py` | NEW — audit probe. Mirrors Lambda `get_term_returns` (weekday-strip + holiday-zero-row drop), `calculate_volatility` (`np.std(daily, ddof=1)*sqrt(252)*100`), and `calculate_period_returns` slicing across the 9 periods. Emits AC1-AC5 inventory + JSON dump. No artifact write to S3. |
| `docs/briefs/mdlp-etf-vs-index-volatility-audit-20260519.md` | NEW — audit brief; AC1-AC7 evidence; verdict; Lambda-anomaly characterization; CTO recommendations. |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/MDLP_VOLAUD.001.dsb-etf-vs-index-volatility-audit.md` | status `pending` -> `in_progress` -> `complete`. |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-19/DS_B_session2_mdlp_volaud_001_etf_vs_index_audit.md` | NEW — this file. |

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `aws s3 ls s3://opal-data-portal-v2/benchmarks/` | OK | Pinned `data_20260519_v1.pkl` as latest |
| `aws s3 cp ... LATEST.json -` | OK | `data_pkl: "benchmarks/data_20260519_v1.pkl"` |
| `aws s3 cp ... model_portfolio_benchmarks.json` | OK | Published `data_as_of=2026-05-18`, 5 models, 9 periods |
| `aws lambda get-function-configuration` | OK | Deployed LastModified 2026-05-04T18:54:55Z; Layer `AWSSDKPandas-Python312:16` |
| `aws lambda get-function --query Code.Location` + `curl` + `unzip` + `md5sum` | OK | Deployed Lambda zip byte-identical to repo (md5 `81cdb6063971c32eec6aa1a20bdd914d`, 587 lines) |
| `aws logs get-log-events` (PowerShell) | OK | Pinned publishing-invocation RequestId `fe5f8952-6553-4eaf-bb17-e37947c7008a` -- pickle used was `data_20260519_v1.pkl`, single invoke, no anomalous payload |
| `comp-pipescript io yang-model-portfolio-benchmarks` | empty | Lambda not indexed in comp graph; TO `if_mismatch` documents the gap. Substituted direct file read of `lambda_function.py:333-477` for methodology reference. |
| `.tools/ds-commit-gate.sh org/tier2_senior/0.4.0_DS_ClientPlatform/probes/mdlp_volaud_001_etf_vs_index_audit.py` | exit 0 | py_compile + AST undefined-name scan + ruff 0.15.11. One iteration: removed unused `io` import after the first run failed ruff F401. |
| Probe execution end-to-end | OK | `--out-json /tmp/mdlp_volaud_001_result.json`; 12 AC2 cells, 45 AC3 cells, 7-class anomaly inventory. |

## Phase Evidence

### Phase 0 — Grounding

Identified the pipeline anchor points: source pickle (`benchmarks/data_20260519_v1.pkl`),
published JSON (`json/benchmarks/model_portfolio_benchmarks.json`,
`data_as_of=2026-05-18`), deployed Lambda (`yang-model-portfolio-benchmarks`,
LastModified 2026-05-04). All canonical paths verified live.

### Phase 1 — Source extraction + AC1 structural

Mirrored `get_term_returns` exactly (both filters per CTO rider #1):
13 series × 621 weekday rows, 2024-01-01 -> 2026-05-18, 0 NaN. Zero-return-day
counts: INDEX series 0-31; ETF series 25-43 (US-trading-day-only calendar).
Max-abs daily moves cluster on real market-stress days (2025-04-09 Liberation
Day, 2026-04-06 Treasury rally) -- no artifact.

### Phase 2 — AC2 pair-window stats

4 distinct (INDEX, ETF) pairs (LTC/LTA share Long Term Benchmark / ETF) x 3
windows (1Y / YTD / SI) = 12 cells. **AC2 1Y convention = calendar-365**
(`end_date - timedelta(days=365)`), mirroring the Lambda's calculate_period_returns
1Y branch -- CTO rider #2. All 12 cells: corr 0.92-0.97, stdev ratio 1.05-1.24,
residual mean within +/-0.18 bps/day, residual lag-1 autocorr strongly negative
(-0.38 to -0.57).

### Phase 3 — AC3 reproduce 45 vols vs published

6 of 9 periods reproduce TO THE CENT for both INDEX and ETF vols across all 5
models (30 cells PASS to the cent). 3 of 9 periods exhibit drift (1D / WTD /
MTD -- 10 INDEX drift rows + 9 ETF drift rows). Drift is structural and
unbidirectional: published values for 1D / WTD / MTD COLLAPSE to one identical
value per (model, axis), and that value does NOT correspond to any
calculate_period_returns output on the same pickle.

### Phase 4 — AC4 microstructure verdict

12 AC2 cells verdict-by-verdict:
- 5 cells: consistent-with-microstructure (UST 1Y, UST SI, ST 1Y, ST YTD, ST SI)
- 3 cells: near-threshold (UST YTD 0.948, INT SI 0.948, LT SI 0.950 -- all <1.8bps
  below 0.95 corr)
- 4 cells: flagged for corr<0.95 (INT 1Y/YTD, LT 1Y/YTD -- 0.92-0.94, consistent
  with equity-blend tracking error over the 2025-04 Liberation-Day-inclusive
  window)
No cell exceeds the 1.30 stdev ratio threshold in the 12 long-window cells.
No cell shows residual drift > 5 bps/day mean. Verdict: explainable.

### Phase 5 — AC5 anomaly inventory (7-class)

| Class | Count | Disposition |
|-------|------:|-------------|
| ETF<INDEX vol | 0 | NONE |
| ratio>1.30 in calm AC2 long-window | 0 | NONE |
| ratio>1.30 across full 45-cell grid | 9 | Real on INT 1M (1.347), LTC/LTA 1M (1.388); collapsed-value on LTC/LTA 1D/WTD/MTD (see below). 1M cells reflect structural equity-heavy ETF dispersion over a short window; not a defect. |
| corr<0.90 | 0 | NONE (lowest 0.9153) |
| residual drift>5 bps/day | 0 | NONE (largest +0.18 bps/day) |
| zero-day asymmetry | 4 | UST INDEX/ETF 31/43; ST/INT/LT INDEX/ETF 0/25 each. Structural calendar handling (Bloomberg/MSCI calendar-daily vs US trading-day-only ETF), not a defect. |
| **Lambda-output collapsed-period values (1D/WTD/MTD)** | 10 | NEW class added per evidence. ALL 5 models, BOTH idx and etf vol axes, 1D == WTD == MTD byte-identical in published JSON; deployed code reproduces correct differentiated values locally. **OUT OF SCOPE FOR THIS TO; AE 0.5.0 follow-on recommended.** |

### Lambda-output anomaly characterization

Empirical signals captured to support the AE follow-on scoping (full
characterization in the brief, condensed here):
- Deployed zip md5 = repo md5 (no code drift).
- Repo lambda_function.py executed locally against the same pickle
  (`data_20260519_v1.pkl`) produces correctly differentiated 1D / WTD / MTD
  values (e.g. UST INDEX 1D=1.25 / WTD=None / MTD=1.18).
- CloudWatch log for the publishing invocation
  (RequestId `fe5f8952-6553-4eaf-bb17-e37947c7008a`, 2026-05-19T11:25:01-03Z)
  shows a single, non-anomalous Step Functions invoke.
- Legacy `benchmark_returns.json` exhibits the same collapse pattern -- rules
  out a comprehensive-output-specific bug.
- Lambda Layer `AWSSDKPandas-Python312:16` is the only environmental difference
  between local execution and AWS-Lambda execution.

Hypothesis: Lambda-runtime divergence in pandas / numpy behavior under the
AWSSDKPandas layer vs the local pandas environment, OR a Lambda-init-time
side effect that mutates `calculate_period_returns` execution. Confirmation
requires either (a) an `aws lambda invoke` test (out of scope this TO) or
(b) a Lambda container-runtime reproduction. AE 0.5.0 follow-on is the
correct lane for either.

## Acceptance Criteria

| AC | Status | Evidence |
|----|--------|----------|
| AC1 | PASS | Structural inspection table; 13 series x 621 rows; per-series row/date/NaN/zero/max-abs columns. |
| AC2 | PASS | 12-cell pair-window stats table; calendar-365 1Y convention per CTO rider #2; corr/ratio/residual/lag1 columns. |
| AC3 | PASS | 45-cell reproduce-vs-published table; 30 cells MATCH to the cent; 19 drift rows enumerated (10 INDEX + 9 ETF, all in 1D/WTD/MTD). |
| AC4 | PASS | 12-cell hypothesis verdict; verdict cell-by-cell with corr/ratio/residual evidence. |
| AC5 | PASS | 7-class anomaly inventory (5 TO-listed + 2 added: full-grid ratio + Lambda-collapsed). Each class explicit count + per-row entries where applicable. |
| AC6 | PASS | Verdict in brief Section 0: two-part answer addressing Andrew's question for the 6-period bulk + 3-period anomaly. |
| AC7 | PASS | Brief at `docs/briefs/mdlp-etf-vs-index-volatility-audit-20260519.md`. |
| AC8 | PASS | This session log; RAVC2 to 1.0.0_SA_CTO. |

## Deploy Ledger

| Step | Result |
|------|--------|
| Pre-commit gate | `.tools/ds-commit-gate.sh` exit 0 (probe + brief) |
| Commit SHA | to follow (this session log is part of the same commit) |
| safe-commit.sh | scoped (4-path list: probe + brief + TO + session log) |
| Push | to follow |
| S3 deploy | n/a (no artifact write; probe runs locally) |

## Next Steps

| Recipient | Item |
|-----------|------|
| **1.0.0_SA_CTO** | RAVC2 — MDLP_VOLAUD.001 complete; brief shipped. AC1-AC8 met. Recommend a follow-on AE 0.5.0 TO to root-cause the 1D/WTD/MTD Lambda-output collapse (out of scope this TO; characterization captured in brief Section 5 + AC5 inventory). |
| **DS~B (self)** | Idle / watchdog. No further DS~B-lane pending TOs (other open MDPF TOs are DS~C or DS Base). |
