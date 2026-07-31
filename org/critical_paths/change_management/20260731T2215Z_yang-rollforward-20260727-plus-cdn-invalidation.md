# DEPLOY-COMPLETION LEDGER -- Yang roll-forward to 2026-07-27 vintage + CloudFront invalidation

**Opened:** 2026-07-31 ~22:15Z (deploy-start) · **Owner:** `1.0.0_SA_CTO`
**Authority:** Andrew-direct, this session -- *"Make sure that the 7-27 data gets updated and cloudfront
invalidated. Goal is not done until you run smoke on the benchmark tab and see the 7-27 vintage data
published."*
**Status:** CLOSED 2026-07-31 ~22:30Z -- all four steps landed and verified. Goal met.

## Why

At 21:46:51Z a rollback (`rollback-b72b5ecd2641`, restoredBy andrew@opalinvest.com) restored the
**2026-07-22** vintage (`exec-ead9d176deb1`). The S3 restore SUCCEEDED -- all 99 files, verified by
timestamp. **The CloudFront invalidation did not**, because
`infra/aws/lambda/data_refresh/lambda_function.py:1251` hardcodes `Items: ['/api/public/*']`, a prefix
that has matched **zero** CloudFront behaviors since the 2026-02-25 rename to `/api/general/`
(positive control: api/public = 0 behaviors, api/general = 6). The benchmark heatmap is served at
`/api/general/benchmarks/*` -> `json/benchmarks/*`, so the CDN kept serving pre-rollback content.

Target state is NOT the 7/22 vintage: Andrew wants **2026-07-27** live.

## Plan

1. Version-based roll-forward to `exec-5a4149176fb6` (dataAsOfDate **2026-07-27**, SUCCEEDED,
   canRollback=true, manifest `data-refresh/archive/fa8dd6bb-1531-4bc4-a03f-32e1daa2a255/outputs-manifest.json`,
   99 outputs, inputs `data 20260727 v1.pkl` + `model 20260727 v1.pkl`).
2. Invalidate the paths ACTUALLY served: `/api/general/*` on distribution `EVTSA9VEHNZVH`
   (the Lambda's own invalidation is a known no-op -- do not rely on it).
3. Smoke the benchmark tab and confirm the 7/27 vintage renders.

## ACCEPTANCE ORACLE (set BEFORE execution, so it cannot be fitted afterward)

`json/benchmarks/model_portfolio_benchmarks.json` must land at:
- **versionId** `WQW0FW7NVF40_p6E3AfysjCiMDtZqvcF`
- **etag** `a8cb00d8f9fe97b6e11c176bbe8bca63`
- **size** `19221`

Discriminating: the currently-live 7/22 object is **19212** bytes, a different size and etag.
A restore that leaves 19212 in place is a FAILURE regardless of what any status field says.

## Steps + evidence

| # | step | status | evidence |
|---|---|---|---|
| 1 | roll-forward to exec-5a4149176fb6 | **DONE** | Lambda invoke rc=200, `method: version-based`, `filesRestored: 99`, `executionId: exec-5a4149176fb6` |
| 2 | verify S3 etag/size vs oracle | **DONE, 4/4** | see table below -- all four benchmark outputs etag+size match the manifest EXACTLY; negative control passed (19212 -> 19221) |
| 3 | invalidate `/api/general/*` | **DONE** | invalidation `I2BY1873P4GBS08F99UAFENF6K`, Status **Completed**, dist `EVTSA9VEHNZVH` |
| 4 | smoke benchmark tab, 7/27 vintage visible | **DONE, both oracles** | wire + render, see below |

### Step 2 evidence -- oracle set BEFORE execution, 4/4 MATCH

| key | etag | size |
|---|---|---|
| `json/benchmarks/benchmark_returns.json` | `9ed4d8f1…` | 12541 |
| `json/benchmarks/etf_returns.json` | `f05dfeb9…` | 1278 |
| `json/benchmarks/model_portfolio_benchmarks.json` | `a8cb00d8…` | **19221** |
| `json/benchmarks/model_portfolio_timeseries.json` | `b7fb9f3e…` | 708434 |

**Negative control held:** the 7/22 object was 19212 bytes; it is gone. A no-op restore would
have left 19212 and FAILED this check.

### Step 4 evidence -- TWO INDEPENDENT ORACLES, both required, both passed

Runner: `portal/.runtmp/bench_vintage_smoke.mjs` (puppeteer-core over CDP, **real login** as
michael@opalinvest.com against live `https://opalinvest.dev`).

**WIRE** -- what CloudFront actually delivered to an authenticated client:
```
/api/general/benchmarks/model_portfolio_benchmarks.json  200  data_as_of "2026-07-27"  models 5
/api/general/benchmarks/etf_returns.json                 200  data_as_of "2026-07-27"
x-cache: Miss from cloudfront          <- the invalidation took; edge refetched from origin
```
**RENDER** -- Benchmark tab, `portal/.runtmp/bench_vintage/benchmark_tab.png`: BENCHMARK COMPARISON
fully populated (MODEL/BENCHMARK/SPREAD x 5 model portfolios x 10 periods), panel footer reads
**"July 27th, 2026, 5:00p ET"**. `hasNoData: false`.

>> **A FIRST SMOKE ATTEMPT WAS DISCARDED AS AN INVALID MEASUREMENT, NOT RECORDED AS A FAILURE.**
`scripts/ui-smoke.mjs --origin` STUBS `/auth/refresh` with a fake `ui-smoke-token`
(`ui-smoke.mjs:67,96`), which `auth-validator-edge` rejects on a real origin -- so every authed
call 401s and the tab renders "No benchmark data available" REGARDLESS of vintage. **That
instrument cannot distinguish 7/27 from 7/22 and must never be used to score this claim.** It is
built for local dev with fixtures. The authenticated runner above is the valid oracle. <<

## Residual -- NOT closed by this entry

The `/api/public/*` invalidation defect is **still live and was reproduced during this very
change**: the Lambda's own invalidation on my roll-forward was `I1PN50A9GWENFSGJB86H0UCSOH`,
paths `["/api/public/*"]` -- a second confirmed no-op. **Every rollback remains broken at the CDN
step until `lambda_function.py:1251` is fixed.** My manual `/api/general/*` invalidation is what
made this one land, and a manual step is not a fix. Routes to `0.7.0_AE_CloudOps` (infra/aws/ is
outside the CTO lane).

## Notes

- The `/api/public/*` defect is NOT fixed by this entry -- it is a code change in `infra/aws/`, which is
  outside the CTO lane and routes to `0.7.0_AE_CloudOps`. Captured separately.
- This is a served-output move. Authority is Andrew-direct (sovereign), recorded above.
