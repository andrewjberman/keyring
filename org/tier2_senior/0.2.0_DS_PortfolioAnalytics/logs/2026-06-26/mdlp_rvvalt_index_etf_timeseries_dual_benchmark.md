# MDLP_RVVALT — Index/ETF benchmark toggle: dual-benchmark daily timeseries (Lambda)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE
**Agent:** 0.2.0_DS_PortfolioAnalytics
**Date:** 2026-06-26 (~14:25Z-15:03Z)
**Commit:** f3cfe6a4a (CLOUD)

## Origin

Andrew-direct via Teams thread w/ Yang Liu (2026-06-26 ~14:25-14:34Z). Yang asked whether the
May upside/downside capture on the Model Portfolios page is benched against the INDEX or the
ETF benchmark, and asked to convert the capture/Sharpe/drawdown charts to respond to the
existing Index/ETF toggle. Andrew observation: "all of those charts are not toggling aside from
return vs volatility, all of them need to be linked to the toggle." Scoped to me: the Lambda
data plane only; Pod2 DE owns FE wiring, Pod2 DT owns deploy (Andrew-direct).

## Diagnosis (source-grounded)

The Model Portfolios "Benchmark" tab has two data paths:
- `benchmarkData` (period returns) carries BOTH `index_benchmark` + `etf_benchmark` -> Return vs
  Volatility scatter + Benchmark Comparison heatmap toggle correctly.
- `getModelPortfolioTimeseries()` -> `json/benchmarks/model_portfolio_timeseries.json` carried a
  SINGLE `benchmark_return`, which `build_timeseries()` populated from `mapping['index_benchmark']`
  ONLY (producer L623, L637-647). The 3 sibling views of the ReturnVolatilityScatter panel
  (Up/Down Capture = RollingCaptureChart, Rolling Sharpe, Max Drawdown) all derive from this
  single series -> they could not toggle.

**Answer to Yang's question (source-confirmed, not inferred):** the May capture was computed vs
the **INDEX** benchmark.

**Feasibility linchpin:** the ETF-blend daily series was ALREADY loaded in `term_returns`
(`mapping['etf_benchmark']`, e.g. "Long Term ETF") — the same source the period/scatter path uses.
`build_timeseries()` simply wasn't carrying it through. So the fix is contained to the producer;
no new upstream data dependency.

## Change made (Lambda — DS scope)

File: `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py`
Function: `build_timeseries()`

- Added `etf_series = term_returns.get(mapping['etf_benchmark'])` + a null-series warning.
- Each timeseries row now emits BOTH `index_benchmark_return` + `etf_benchmark_return` (daily
  decimal fractions).
- `benchmark_return` RETAINED as a back-compat alias == `index_benchmark_return` (prior behavior)
  so the current FE keeps working until DE threads the toggle. Additive, non-breaking.
- Updated build log line + output `series_note`; updated `data_contract.xml` with a new
  `model_portfolio_timeseries.json` shared_source entry documenting the dual-benchmark shape.

New row shape (`json/benchmarks/model_portfolio_timeseries.json`):
`{ date, model_code, model_return, benchmark_return, index_benchmark_return, etf_benchmark_return, rfr }`
`etf_benchmark_return` is null for (model, date) where the ETF series has no value (pre-ETF dates).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `comp-which "which charts wired to index/etf toggle"` | yes | PASS (backstop) | No rich tool for portal-FE wiring Q; routed to manifest backstop -> proceeded to grounded Read/Grep. Coverage gap candidate: a yang-pipeline-fed page wiring tool (banked, prior YALP gap). |
| `comp-pipescript io <producer>` | yes | PASS | Confirmed producer WRITES json/benchmarks/model_portfolio_timeseries.json (+ 2 other keys); additive field change touches no read/write/IAM. NOTE: yang Lambdas not yet in BD-gold DAG (partial AC5) — expected. |
| `python -m py_compile` | yes | PASS | Clean. |

**What worked:** `comp-pipescript io` confirmed the output-key set is unchanged (additive only) —
exactly the signal DT needs that this is a no-IAM, no-key-change deploy. **What failed:** none.
**Gap found:** no comp-tool maps a portal chart -> its benchmark data path / toggle wiring; had to
Read components directly (RollingCaptureChart, ReturnVolatilityScatter, portal-proxy). Banked as
an R&D candidate (consistent with prior YALP yang-pipeline graph-coverage gap).

## MCP traffic

5 sent / handled. Significant: HANDOFF -> Pod2 DE (FE wiring spec) + DEPLOY HANDOFF -> Pod2 DT
(Terraform deploy). Both ACKed cleanly. DT flagged a transient working-tree ` M` on the file;
I verified from the shared CLOUD tree (HEAD commit = f3cfe6a4a, `git status --porcelain` empty,
committed blob contains the new fields) and sent git-evidence — it was benign CRLF normalization
churn. No blockers raised by either lane.

## Files Modified

See commit message: f3cfe6a4a (lambda_function.py build_timeseries; data_contract.xml; new
devops brief). Brief authored: `docs/briefs/devops-brief-model-portfolio-timeseries-index-etf-toggle.md`.

## Briefs Written

| Brief | Purpose | Audience |
|---|---|---|
| `docs/briefs/devops-brief-model-portfolio-timeseries-index-etf-toggle.md` | Root cause + Lambda change + 4-step FE wiring map (file:line) + DT deploy/verify steps | Pod2 DE + DT |

## Current State

- Producer `yang-model-portfolio-benchmarks` `build_timeseries()` emits dual benchmark daily
  returns; committed `f3cfe6a4a` on CLOUD (HEAD has since advanced to ceaa8d3d3 via other agents;
  my commit is in lineage, working tree clean for the file).
- Commit used an audited owned-paths override `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL`
  (infra/aws enumerated AE-only; DS-edits-yang-Lambda lane gap; Andrew-direct scoped this Lambda
  to DS) — logged to org/git-author-override-audit.log.
- NOT YET DEPLOYED. New `etf_benchmark_return` fields materialize only after the next scheduled
  yang-pipeline run regenerates the artifact (DT deploys Lambda via Terraform first; no ad-hoc
  gold run per rule).
- Pod2 DE: FE wiring in progress on portal DEV. Pod2 DT: Lambda deploy in progress.

## Next Steps

1. [0.2.0_DT_PortfolioAnalytics] Deploy yang-model-portfolio-benchmarks via Terraform; tag after
   0-diff; served-verify the dual fields on the next scheduled yang run's artifact.
2. [0.2.0_DE_PortfolioAnalytics] Thread `benchmarkType` into ReturnVolatilityScatter -> the 3
   charts; add the two fields to `ModelTimeseriesPoint`; select field by toggle; ETF labels.
3. [0.2.0_DS_PortfolioAnalytics — me] Available for data-shape follow-ups; verify dual-benchmark
   correctness on the served artifact post-deploy if asked.

## RAVC

- Request: Andrew-direct (adjust the Lambda; report to Pod2 DE/DT when ready).
- Acknowledge: this log + commit f3cfe6a4a + the two handoff MCPs.
- Validate: DE + DT both ACKed; DT reconciliation closed with git evidence.
- Close: DS Lambda leg COMPLETE; overall feature open pending DE FE + DT deploy + served verify.
