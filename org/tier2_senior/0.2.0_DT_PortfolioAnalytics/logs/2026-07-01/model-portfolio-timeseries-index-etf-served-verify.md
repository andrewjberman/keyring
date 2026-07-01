# model_portfolio_timeseries.json — post-nightly served-verify (yang-v2.4.12 index/etf toggle)
**archetype:** VALIDATE

**Agent:** 0.2.0_DT_PortfolioAnalytics
**Date:** 2026-07-01
**Window:** session start (~16:2xZ) — /watcher + org/XXX.md startup, then closed the one DT-owned open follow-on from 2026-06-26.

## Summary

Closed the post-nightly served-verify that was the standing DT follow-on from the
2026-06-26 yang-v2.4.12 deploy (added `index_benchmark_return` + `etf_benchmark_return`
to each `model_portfolio_timeseries.json` row; `benchmark_return` retained as back-compat
alias == index). 5 days elapsed since deploy -> nightly yang runs have materialized the
change. Ground-truthed against the SERVED artifact (F5, never source/self-report). All
three assertions PASS; verify is SOUND. Backend + FE stack is fully shipped.

## Ground truth (served artifact)

`s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json`
- LastModified: 2026-07-01 16:31:36 GMT  (fresh — today's run)
- generated_at: 2026-07-01T16:31:35Z   data_as_of: 2026-06-30
- 2830 rows across 5 models {INT, LTA, LTC, ST, UST}; row schema =
  {date, model_code, model_return, benchmark_return, index_benchmark_return,
  etf_benchmark_return, rfr}

## Assertions (all PASS)

| # | Assertion | Result |
|---|---|---|
| 1 | Every row carries non-null `index_benchmark_return` + `etf_benchmark_return` | PASS — 0 index nulls, 0 etf nulls / 2830 |
| 2 | Alias invariant: `index_benchmark_return == benchmark_return` | PASS — 0 violations / 2830 |
| 3 | Distinct series: `etf_benchmark_return != index` | PASS — 2806/2830 differ (99.2%); all 5 models distinct on latest date 2026-06-30 |

Per-model latest-date (2026-06-30) index vs etf:
```
INT  index= 0.002973  etf= 0.002858  [DISTINCT]
LTA  index= 0.005925  etf= 0.005685  [DISTINCT]
LTC  index= 0.005925  etf= 0.005685  [DISTINCT]
ST   index=-0.002341  etf=-0.002229  [DISTINCT]
UST  index=-0.000793  etf=-0.000858  [DISTINCT]
```

## Full-stack ship status (verified)

- Backend: yang-v2.4.12 (CodeSha256 CTF3JGXMj4E+VC48PIOaTQygcU9nxpoVO+2Vyfp72Dg=) — LIVE, served data verified above.
- FE: DE commit e5029515 (Index/ETF toggle wired into Up/Down Capture, Rolling Sharpe, Max Drawdown)
  promoted to PROD via merge bee2842f = portal-v2.1.126. Confirmed in portal git log.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| (none — served-data F5 verify) | model_portfolio_timeseries.json | n/a | This is an operational served-artifact content verify (field presence + value assertions on a `json/` served path), not a graph/IAM/routes/freshness inspection any comp-tool models. comp-freshness targets gold\|platinum, not `json/` served proxy artifacts. Grounded directly on the served S3 object per Rule 20 F5 ("verify your OWN change against live/served, never the graph"). |

What worked: direct served-artifact pull is the correct F5 grounding for a delivery/value claim.
What failed: none. Gap: no comp-tool covers "does this served `json/` artifact carry field X with value invariant Y" — that's data-plane/operational by design (graph-presence principle), so off-rail is correct here.

## Blockers

None.

## Current State

- yang-v2.4.12 index/etf timeseries change is LIVE and CONFIRMED MATERIALIZED in the served
  `model_portfolio_timeseries.json` (data_as_of 2026-06-30). Alias invariant + distinct-series
  both hold across all 2830 rows / 5 models. FE toggle shipped to PROD (v2.1.126).
- The MDLP_RVVALT Index/ETF benchmark toggle (Up/Down Capture, Rolling Sharpe, Max Drawdown) has
  both halves proven: producer supplies both series; FE consumes them.

## Next Steps

- [0.2.0_DT or 0.2.0_DE_PortfolioAnalytics] (NON-GATING) PIXEL/Playwright visual spot-check of the
  3 charts toggling Index<->ETF on PROD — whoever frees the shared Playwright profile first.
  Backend + FE both verified present, so this is cosmetic confirmation only.
- [0.7.0_AE_CloudOps] (low-pri cleanup, on record) remove dead distribution id E2LPCXXBLDGWXY from
  the yang invalidate-cloudfront lambda (NoSuchDistribution every run; harmless).
- [2.0.0_SA_COO] (optional) owned-paths DT-enumeration for infra/aws/lambda/ci + owned pipeline TF.
