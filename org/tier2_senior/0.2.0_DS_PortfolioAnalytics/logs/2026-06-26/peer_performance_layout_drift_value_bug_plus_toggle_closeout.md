# Peer-performance layout-drift value bug (Andrew-caught) + Index/ETF toggle close-out

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE
**Agent:** 0.2.0_DS_PortfolioAnalytics
**Date:** 2026-06-26 (~15:03Z-16:50Z)
**Commits:** b8874661f, d4ae41b84, b72df1095, 7f77542de
**Window:** since last log 61f878a87

## Summary

Two threads. (1) Closed out the Index/ETF benchmark toggle (data verify PASS, served).
(2) Andrew flagged the /Peers numbers looked "completely wrong" -> root-caused + fixed a
TWO-LAYER silent source-layout-drift bug in yang-generate-peer-performance, deployed
(yang-v2.4.13/v2.4.14), verified end-to-end against RAW Excel cells, and added a
fail-closed structural guard.

## Index/ETF toggle close-out (carried from prior log)

- b8874661f: fixed series_note metadata cosmetic lag (handler literal still described old
  row shape) flagged by DT during model_portfolio_timeseries rerun.
- Served-data verify on regenerated json/benchmarks/model_portfolio_timeseries.json (DT
  Andrew-direct manual rerun): alias invariant 0 mismatches/2790, etf distinct 2767/2790,
  ZERO nulls (etf full-history from inception), magnitude/sign sane, INT 06-18 idx=0.004437
  etf=0.008608 matched. DE FE (e5029515) + behavioral verify tie to DS numbers. DS leg CLOSED.

## Peer-performance bug (the main event)

**Layer 1 (d4ae41b84):** parse_peer_excel hardcoded section start-cols [0,20]; wide 06-18
source shifted 2nd block to col 26 -> ST/LTC/LTA silently dropped (served had only INT+UST).
Fix = scan for every 'Return/Risk' header column. Mechanism SOURCE-CONFIRMED by reproduction
on the archived wide file (data-refresh/archive/exec-ef9c2e9f2b37/...20260618.xlsx): pre-fix
parser -> ['INT','UST'] == served exactly; fixed -> 5 models. Also found + flagged a dangling
manifest pointer (uploads/20260618 archived out); DT restored it.

**Layer 2 (b72df1095) -- Andrew's catch:** even after 5 models appeared, VALUES were
systematically wrong. The wide workbook added leading 1 Day + MTD periods (3 cols each:
Stat/Rank/Percentile), shifting every period column +6. The hardcoded stat offsets
[1,4,7,10,13,16] read the WRONG period for every cell -- a clean N->N-2 shift (served '1Y'
was the 1-Quarter column; Since Inception never read). Proven: served '1Q'(0.3729)==correct
'1M', served 'YTD'(0.8146)==correct 'QTD'. Fix = build_period_stat_cols() maps each period to
its Statistic column by HEADER LABEL (layout-agnostic). Validated correct on wide source (all
5x6 + SI populated, monotonic-with-horizon) and backward-compatible on narrow 202512 layout
(leads with 1 Month -> same columns the old offsets found, no regression).

**False-green lesson (banked, shared with DE/DT):** the earlier "INT 1Y=6.3888 exact match"
was a FALSE-GREEN -- the verify target was computed by the SAME buggy offset code, so local
parser and served agreed with each other, not ground truth. The redo anchored verification to
RAW Excel cells (located each '<period> Statistic' header column in the .xlsx directly, read
the model-row cell), independent of any parser. Served 30/30 model values matched raw cells.

**Layer 3 (7f77542de) -- preventive:** added validate_peer_output() fail-closed guard --
raises at generation (no artifact written) if an expected model is dropped or a period column
can't be header-resolved. Both today's bugs were silent; this makes the next layout drift a
loud generation failure. Tested: passes on good data, raises on dropped-model +
header-not-found-period. Preventive (output unchanged); rides next deploy.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `comp-which` | yes | backstop | No rich tool for portal-chart-wiring / Excel-parser-structure Qs; proceeded to grounded Read/raw-cell inspection. Gap banked (prior YALP yang-pipeline graph-coverage gap). |
| `comp-pipescript io` (prior turn) | reused | PASS | producer output keys (incl peer_performance.json) unchanged across edits; additive/no-IAM. |
| `python -m py_compile` | 4x | PASS | clean on every commit (b8874661f, d4ae41b84, b72df1095, 7f77542de). |
| direct S3 + openpyxl/pandas cell inspection | many | PASS | THE decisive tool here -- raw-cell ground truth (parser-independent) for both mechanism repro and served verify. |

**What worked:** raw-cell ground-truth comparison caught what count/presence checks missed and
broke the false-green cycle. **What failed:** my own earlier served verify (model_count==5,
fully-populated) passed a structurally-complete-but-semantically-wrong artifact -- presence !=
value-correctness. **Gap found:** (a) no comp-tool maps a portal chart -> its data path/toggle
wiring, nor an Excel producer -> its source-cell structure; (b) the verify discipline gap (don't
derive a numeric verify target from the same code path) -- now banked across the pod.

## MCP traffic

~16 sent/handled across the window. Significant: 2x peer deploy handoffs -> DT (d4ae41b84,
b72df1095) with rerun-source constraints; grounding-gap exchange with DE (archive wide-source
key + dangling-pointer); independent served-verify PASS reports; FE FYIs to DE (no FE change --
period keys unchanged). All RAVC loops closed.

## Files Modified

See commit messages: b8874661f, d4ae41b84, b72df1095, 7f77542de (all
infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-generate-peer-performance/lambda_function.py
except b8874661f = yang-model-portfolio-benchmarks). Brief from prior turn:
docs/briefs/devops-brief-model-portfolio-timeseries-index-etf-toggle.md.

## Current State

- Peer-performance: LIVE on yang-v2.4.14 (CodeSha256 qhjMKxByTyspQpCJY9zz3KiM0YYTwdh46k7s95l+Z1A=).
  Served json/peers/peer_performance.json (generated 16:40:37Z, data_as_of 06-18): 5 models x 6
  periods, 30/30 values match raw source cells, SI populated, risk-ordering sane. Guard 7f77542de
  committed (CLOUD), NOT yet deployed (preventive, rides next deploy).
- Index/ETF toggle: model_portfolio_timeseries dual-benchmark live (yang-v2.4.12); FE e5029515 on DEV.
- All 4 commits used GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL (yang-Lambda DS lane gap,
  Andrew-direct 2026-06-26) -- audited to org/git-author-override-audit.log.

## Next Steps

1. [0.2.0_DT_PortfolioAnalytics] Deploy guard 7f77542de on next peer-performance deploy (preventive).
2. [0.2.0_DE_PortfolioAnalytics] /Peers visual re-smoke on corrected values (INT 1Y ~14.43, SI non-null) -- DONE/CLOSED per DE VERIFY PASS.
3. [0.2.0_DS_PortfolioAnalytics -- me] Available. Consider folding the raw-cell value-verify +
   header-resolution check into a reusable producer QA pattern for other Excel-fed yang Lambdas.

## RAVC

- Request: Andrew-direct -- "peer numbers look completely wrong, reassess document structure."
- Acknowledge: this log + commits + the diagnosis report to Andrew.
- Validate: independent served verify 30/30 vs RAW Excel cells (parser-independent); DE + DT concur.
- Close: peer-performance VALUE bug CLOSED end-to-end; guard committed; Index/ETF toggle data-side CLOSED.
