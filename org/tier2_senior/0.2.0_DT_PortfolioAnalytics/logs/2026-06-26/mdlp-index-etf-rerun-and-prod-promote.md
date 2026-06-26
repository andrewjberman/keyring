# MDLP index/etf — Andrew-direct manual rerun + portal PROD promote (portal-v2.1.126)
**archetype:** DEPLOY

**Agent:** 0.2.0_DT_PortfolioAnalytics
**Date:** 2026-06-26
**Window:** 15:13Z -> 15:36Z (delta after the yang-v2.4.12 deploy log); ~12 MCP messages, 1 lambda rerun, 1 portal PROD promote

## Summary

Continuation of the MDLP_RVVALT Index/ETF toggle ship. After the yang-v2.4.12 backend deploy,
Andrew-direct: get the functionality live for FE users immediately. Surfaced that a lambda
rerun alone wouldn't do it (DATA != user-facing functionality without DE's FE threading);
Andrew chose "refresh data + fast-track DE". Executed: manual lambda rerun (data live), then
the full DT-lane portal DEV->PROD promote of DE's FE wiring. Feature is LIVE end-to-end for
internal/Opal users.

## What happened

1. **Premise correction.** Andrew asked to "just rerun the lambda." Flagged via AskUserQuestion
   that the 3 charts (Up/Down Capture, Rolling Sharpe, Max Drawdown) read the old single
   `benchmark_return` and won't toggle until DE threads the new fields through the FE -- so the
   rerun is necessary-but-not-sufficient. Andrew chose refresh-data + fast-track-DE.
2. **Manual lambda rerun** (Andrew-direct override of the hold-for-next-upload line):
   `aws lambda invoke yang-model-portfolio-benchmarks {}` (CLI v1, no --cli-binary-format) ->
   orchestrated branch, latest data.pkl. 200, no error, 5 models, 2790 rows. Regenerated all 3
   benchmark outputs incl. model_portfolio_timeseries.json with new fields.
3. **Artifact verify (S3 source-of-truth):** row keys now date/model_code/model_return/
   benchmark_return/index_benchmark_return/etf_benchmark_return/rfr; data_as_of 2026-06-18
   (SAME vintage as prior -> no cross-artifact skew); alias holds, etf distinct.
4. **CF invalidation:** invoked yang-invalidate-cloudfront -> live dist EVTSA9VEHNZVH InProgress.
   [2nd id E2LPCXXBLDGWXY = dead distribution, NoSuchDistribution, pre-existing harmless --
   flagged for AE cleanup.]
5. **DS independent data verify PASSED** on live artifact (0/2790 alias mismatch, etf distinct
   2767/2790, zero nulls, magnitudes sane). DS patched cosmetic series_note (b8874661f, NO
   redeploy -- rides next change).
6. **DE FE already shipped in parallel** (e5029515 on DEV, VALGATE PASS, tsc/eslint 0); DE
   verified chart math toggles on live data (index vs etf differ on all 3; model-only drawdown
   toggle-invariant). DE GO'd the promote with the pixel-screenshot leg honestly flagged as
   deferred (browser locked), non-gating.
7. **Portal DEV->PROD promote** (canonical /prod-deploy): freeze notified+ACK'd by COO; PROD
   re-asserted from origin; ephemeral worktree + foreground bun install (420 pkgs); merge
   --no-ff origin/DEV; parity gate EMPTY; push -> CI. Tag verified peeled.

## Deployment Sequence + Verification (actual output)

```
Lambda rerun:    StatusCode 200, FunctionError None, model_count 5, timeseries_row_count 2790
Artifact verify: alias_ok=True (index==benchmark_return), distinct=True (etf!=index); data_as_of 2026-06-18
PROD merge:      bee2842f3b9cf7c2ed340442cb9e7e964ffd7c01 (parity git diff origin/DEV HEAD = EMPTY)
VALGATE/tsc:     D-1 PASS (no api/endpoints changed); tsc -b --noEmit OK at push
CI:              run 28248041838  status=completed  conclusion=success
Tag:             portal-v2.1.126 ^{commit} = bee2842f (== origin/PROD head, peeled-verified)
Workspace ptr:   46248a804 on CLOUD (portal -> e5029515 DEV; live PROD bee2842f)
Teardown:        worktree git-deregistered (worktree list = main tree only, DEV); .runtmp dir persists (Win long-path, inert)
Rollback base:   206f4a60
```

## Compiler Tools

No comp-tool runs in THIS delta -- the Rule-20 pre-infra graph check (comp-blast
yang-model-portfolio-benchmarks) was logged in the paired yang-v2.4.12 deploy entry
(yang-mdlp-benchmarks-index-etf-deploy.md); this window is the data-rerun + portal promote,
which are operational deploy steps (aws invoke, gh/git, /prod-deploy) with no comp-tool surface.

## Blockers

None.

## Current State

- LIVE: Index/ETF benchmark toggle on Model Portfolios (Up/Down Capture + Rolling Sharpe + Max
  Drawdown), behind SHOW_BENCHMARK_TOGGLE (internal/Opal only; external = ETF default).
- Backend: yang-v2.4.12 lambda live; served json/benchmarks/model_portfolio_timeseries.json
  carries index_benchmark_return + etf_benchmark_return (data_as_of 2026-06-18). DS-verified.
- Portal: PROD bee2842f / tag portal-v2.1.126, CI success. Workspace pointer 46248a804 on CLOUD.
  Main portal tree on DEV (never left).

## Next Steps

- [0.2.0_DE or 0.2.0_DT] PIXEL screenshot spot-check of the 3 charts toggling on PROD --
  non-gating, whoever frees the shared Playwright profile first (currently locked).
- [0.7.0_AE_CloudOps] (low-pri cleanup) remove dead distribution id E2LPCXXBLDGWXY from the
  yang invalidate-cloudfront lambda (NoSuchDistribution every run; harmless).
- [2.0.0_SA_COO] (optional) owned-paths DT-enumeration for infra/aws/lambda + owned pipeline TF
  (flagged earlier this session).
