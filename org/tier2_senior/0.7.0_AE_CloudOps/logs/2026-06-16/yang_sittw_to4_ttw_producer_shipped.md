# YANG_SITTW.TO-4 -- WS-2 producer TTW (10 trading-day) SHIPPED, both Lambdas live

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE, COORDINATE

**Agent:** 0.7.0_AE_CloudOps - **Date:** 2026-06-16 - **Window:** ~1845Z -> 1917Z
**TO:** YANG_SITTW.TO-4 (Andrew-direct UP-FIRST) -> **COMPLETE**. Gates 2 DE FE legs (TO-2 0.1.0_DE, TO-3 0.4.0_DE).

## Summary

Emitted an additive `TTW` period (PRD v0.2 §5: trailing 10 TRADING sessions, trading-day-counted)
into BOTH WS-2 producer Lambdas, never-widen-safe. Live in all 3 served artifacts. The §5 trap
(producer A computes returns by CALENDAR days) was avoided by a trading-day-counted path, NOT a
PERIOD_CALENDAR_DAYS entry. Additivity proven twice: Phase-2 old-vs-new on real input, Phase-3
served-vs-independent-recompute. Both DE FE legs unblocked + deploy-sequenced (producer-before-FE).
Interleaved with the NFRA_GCONTR combined peers+aum load (separately shipped this window).

## What shipped (code 22c14d5ec)

- **(A) opal-market-overview-tiered-generator** -> all-returns.json: NEW `calculate_trailing_sessions_return()`
  compounds the daily total-return field over the last 10 ROWS (trading-day-counted). NOT a
  PERIOD_CALENDAR_DAYS entry (§5 trap avoided). `calculate_period_return` + every existing period
  byte-untouched. +`from __future__ import annotations` (ruff FA100; runtime-safe). Decimal unit.
- **(B) yang-model-portfolio-benchmarks** -> model_portfolio_benchmarks.json + benchmark_returns.json:
  periods list append 'TTW' (at END, existing indices unchanged) + elif TTW: series.tail(10) -> generic
  compound_returns + calculate_volatility (identical methodology). model+index+ETF + spreads + vols.
  etf_returns.json untouched. Percent-rounded-2 unit. A and B compound exactly 10 daily returns -> §5-identical.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| ds-commit-gate | both Lambda .py | PASS | A needed +future-import for ruff FA100 (typing.Optional); B clean |
| comp-iam service | market-overview-tiered-generator + yang-model-portfolio-benchmarks | PASS | 0 new boto3 / 0 new perms -> iam.tf UNCHANGED (A's 2 ops show UNKNOWN = pre-existing static-resolve gap on opal-portal-lambda-role, not a TO-4 regression) |
| comp-blast | all-returns.json + model_portfolio_benchmarks.json | PASS (lower-bound) | edges = producer only; FE consumers are dynamic reads -> grepped portal directly |
| portal consumer grep | ALL_PERIODS / period_returns / .strict | PASS | whitelist key-lookup consumers (open Record<string,number>, no all-key iter, no strict schema) -> additive-safe. A's FE (PerformanceHeatMap/ExecutiveSummary) ALREADY whitelist TTW awaiting the key |
| build-and-upload.sh | market-overview + yang-pipeline (single-fn) | PASS | deterministic zip + content-sha256; source-map updated |
| terraform plan/safe-apply | both pipelines | PASS | 0/1/0 each; 0-diff re-plan; live CodeSha256 == zip sha256 (jfjSJDQ.../DLYgGbEN...) |

**What worked:** the old-vs-new-on-real-input additive-diff (Phase-2) isolated my change from data drift
-- the only clean proof of "existing values byte-unchanged". **Gap found:** AWS CLI here is v1 ->
`--cli-binary-format` (v2-only) broke the first invoke; dropped it. terraform needs sandbox-disabled
for network egress (aws CLI does not).

## Deployment Sequence + Verification (AE)

```
code 22c14d5ec (both Lambdas) -> ds-commit-gate PASS -> push CLOUD
PRE-DEPLOY: Phase-1 comp-iam/comp-blast PASS; Phase-2 additive-diff (old HEAD vs working tree on REAL input):
  A 3 tickers (weekend_rows=0 = trading-days-only) + B 15 model x leg -> only TTW added, existing byte-identical, TTW==independent 10-session.
A: build-and-upload market-overview (jfjSJDQ...) -> source-map commit b24430bf5 -> tf plan 0/1/0 -> safe-apply apply 0/1/0 (HALTGT clear) -> 0-diff -> live CodeSha256=jfjSJDQ... -> invoke -> all-returns.json @19:09:47Z
  Phase-3: 71/71 non-null TTW; existing periods intact; served TTW==DynamoDB 10-session (5/5, 0 mismatch). PASS.
B: build-and-upload yang-pipeline (DLYgGbEN...) -> source-map commit b17f2fecf -> tf plan 0/1/0 -> safe-apply apply 0/1/0 -> 0-diff -> live CodeSha256=DLYgGbEN... -> invoke -> model_portfolio_benchmarks.json + benchmark_returns.json @19:14:37Z
  Phase-3: periods ends 'TTW'; every model TTW{model+index+ETF+spreads+3 vols}; existing intact; served TTW==data.pkl 10-session (15/15 + 5/5 spread, 0 mismatch). PASS.
Tags: market-overview-v1.11.4 + yang-pipeline-v1.4.2 (Rule 6).
```

## MCP traffic

~8 sent: DE-2 (0.1.0_DE) producer-live ping (A); DE-3 (0.4.0_DE) producer-live ping (B); RAVC2-A + RAVC2-B/TO-4-complete to COO. Received: COO GO TO-4; COO RAVC-accept leg A.

## Blockers

None. Both DE FE legs are HANDOFFS (not blockers): 0.1.0_DE's FE already whitelists TTW -> renders now;
0.4.0_DE adds 'TTW' to BenchmarkHeatmap/ReturnVolatilityScatter ALL_PERIODS to render. Producer-before-FE
satisfied -> their promote is safe.

## Current State

- all-returns.json (s3://opal-data-portal-v2/json-tiered/market-overview/summary/): additive `TTW` (decimal)
  live, 71/71 tickers. opal-market-overview-tiered-generator @ CodeSha256 jfjSJDQ..., tag market-overview-v1.11.4.
- model_portfolio_benchmarks.json + benchmark_returns.json (s3://opal-data-portal-v2/json/benchmarks/):
  additive `TTW` (percent) live, 5 models, model+index+ETF+spreads+vols. yang-model-portfolio-benchmarks @
  CodeSha256 DLYgGbEN..., tag yang-pipeline-v1.4.2. etf_returns.json / model_portfolio_timeseries.json: TTW N/A (timeseries regenerated, no TTW key needed).
- Source 22c14d5ec; source-maps b24430bf5 + b17f2fecf. Ledger 20260616T1901Z CLOSED.

## Next Steps

- [0.1.0_DE_MarketIntelligence] TO-2: land/verify FE TTW column (already whitelisted) + promote (producer live).
- [0.4.0_DE_ClientPlatform] TO-3: add 'TTW' to BenchmarkHeatmap + ReturnVolatilityScatter ALL_PERIODS + map -> render + promote.
- [DT] promote ordering: producers are live, FE promotes safe (no all-N/A column).
