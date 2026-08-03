# ST Model Portfolio data-refresh incident -- root cause found, LIVE-VERIFIED, currently serving stale data

**archetype:** DIAGNOSE

**Serial:** `0.7.0_AE_CloudOps~F` -- fresh lane, no prior context. Window: 2026-08-03T14:00Z-1445Z.

---

## Summary

**No TO/inbox message from MSTR describing this incident had landed as of investigation start** (checked
lane inbox, base inbox, fabric-wide `find -newermt "2026-08-03"`, and MSTR's own `get_agent_status` --
all empty/no match). Rather than wait, I grounded the incident directly against live AWS state, since
the launch brief ("this morning's data-refresh UX + missing-manifest silent-fallback defect, ST Model
Portfolio incident") was specific enough to search for.

**Found it, and it is still live right now.** The portal's Model Portfolios benchmark surface
(`json/benchmarks/model_portfolio_benchmarks.json`, served to ST/UST/INT/LTC/LTA) is currently showing
`"data_as_of": "2026-07-27"` -- a **regressed, 3-trading-day-stale** read, even though **2026-07-30** data
had already been correctly generated earlier this same morning. Zero errors, zero alarms, all three
governing Step Function executions reported `SUCCEEDED`.

---

## Mechanism, grounded end to end (source + live AWS state, not inference)

**Lambda:** `yang-model-portfolio-benchmarks`
(`infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py`),
orchestrated by the `YangDataPipeline` Step Function
(`arn:aws:states:us-east-1:313476888478:stateMachine:YangDataPipeline`).

### Part A -- the loud crash (real bug, correctly surfaced, not the silent part)

Four executions this morning (`get-execution-history`, live AWS):

| Execution | Start (UTC) | Target date | Result |
|---|---|---|---|
| `5149226b` | 12:07:43Z | 2026-07-31 | **FAILED** |
| `90b7d18b` | 12:10:21Z | 2026-07-31 | **FAILED** |
| `7c0e975d` | 12:53:47Z | 2026-07-31 | **FAILED** |
| `a629706a` | 12:57:08Z | 2026-07-31 | **FAILED** |

All four targeted **2026-07-31** (the correct T-1 for today, a Monday). All four failed with the
identical `LambdaFunctionFailed` event:
```
ValueError: cannot reindex on an axis with duplicate labels
  lambda_function.py:324 in lambda_handler -> build_rfr_daily(data_pkl, end_date, tenor=t)
  lambda_function.py:600 in build_rfr_daily -> rfr_monthly['rfr_daily'].reindex(daily_index).ffill()
```
Read at source (`lambda_function.py:588-604`): `build_rfr_daily()` filters `data_pkl['price_monthly']`
by `index_name == tenor`, `set_index('date')`, then `.reindex(daily_index)`. Pandas raises exactly this
`ValueError` when the date index has **duplicate values** -- i.e. the 2026-07-31 `data.pkl` upload
contains 2+ rows for the same (tenor, date) in `price_monthly`. This is an upstream data-quality defect
in that day's raw upload, not a code logic bug, and the pipeline correctly reported it as `FAILED` --
**this half is not the silent-fallback defect**, it's a loud, correct failure.

### Part B -- the silent regression (this IS the defect)

After the four 07-31 failures, three more executions ran, apparently reprocessing **older, previously-known-good**
uploads (grounded on each execution's own `executionStartedEventDetails.input`, live AWS):

| Execution | Start (UTC) | Manifest files | Target date | Result |
|---|---|---|---|---|
| `2394c6bf` | 13:10:16Z | `data_pkl` + `model_pkl` | **2026-07-30** | SUCCEEDED -- ran `GenerateModelPortfolioBenchmarks`, no failure |
| `ba852138` | 13:22:25Z | `attribution_excel` only | 2026-07-31 | SUCCEEDED -- PKL branch not touched (`SkipBothPKLs`, by design -- no PKLs in this manifest) |
| `0d669fd1` | 13:27:12Z | `data_pkl` + `model_pkl` | **2026-07-27** | SUCCEEDED -- ran `GenerateModelPortfolioBenchmarks`, no failure |
| `19c95ca2` | 13:54:36Z | `peer_excel` only | 2026-07-31 | SUCCEEDED -- PKL branch skipped again |

**`0d669fd1` (07-27) ran *after* `2394c6bf` (07-30) and both wrote through the same publish path with
no date-ordering check.** `yang-model-portfolio-benchmarks` has no guard comparing the incoming
`data_as_of_date` against the currently-served date before publishing -- it just writes. Last-writer-wins,
and the last full-PKL writer carried an **older** date than the one already being served.

**Live-verified consequence** (checked directly against the served artifact, not against a log or a
report):
```
$ aws s3api head-object --bucket opal-data-portal-v2 --key json/benchmarks/model_portfolio_benchmarks.json
LastModified: Mon, 03 Aug 2026 13:29:12 GMT   (matches the 0d669fd1 / 07-27 run, not the later 07-30 run)

$ aws s3 cp s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json -
"generated_at": "2026-08-03T13:29:11Z",
"data_as_of": "2026-07-27",   <-- currently served to every ST/UST/INT/LTC/LTA reader, right now
```
**As of this log, the portal is serving July 27th model-portfolio benchmark data as current** -- a
regression from the 07-30 data that had already correctly landed 17 minutes earlier the same morning,
and 3 trading days behind the actual T-1 target (07-31) that never successfully completed.

### Part C -- why nobody would see any of this from the DataRefresh UX

`infra/aws/lambda/data_refresh/lambda_function.py`, `handle_status()` (the endpoint backing the portal's
DataRefresh progress/history view). Its execution-history parser (`:862-880`) only recognizes
`TaskStateEntered` / `TaskStateExited` / `TaskFailed` / `ExecutionFailed` event types when building the
`steps` array shown to the user. **Live-verified in the actual `get-execution-history` output for
`5149226b`:** the manifest-check skip branches (`SkipDataPKL`, `SkipModelPKL`, `SkipBothPKLs`, and the
Excel-check skips) all emit `PassStateEntered` / `PassStateExited` -- a type this parser never checks.
`STATE_LABELS` (`:730-770`) also has no entries for any `Skip*` state name. **A skip branch is therefore
structurally invisible to the DataRefresh status/history UI** -- not merely unlabeled, absent from the
`steps` array entirely. Combined with Part B, an operator watching the DataRefresh page today would see
a run of `SUCCEEDED` executions with no indication that (a) three of them silently skipped the PKL branch
entirely, or (b) the one that didn't skip just regressed the served date backward.

---

## Characterization vs. the launch brief

This matches "missing-manifest silent-fallback defect (ST Model Portfolio incident)" precisely, with one
refinement: the fallback isn't literally "manifest file absent" -- it's **"the manifest's date is older
than what's already served, and nothing checks."** The manifest is present and well-formed in every
case; the gap is a missing **monotonicity guard** on the publish path, compounded by a UX blind spot that
can't surface a skip even when one is the correct, intended behavior.

---

## Compiler Tools

- `comp-which` triggered on a raw `infra/aws/lambda` grep (`build_rfr_daily`); no comp-tool models a
  function-body search across Lambda source trees, so re-ran with an inline `# rail-checked:` marker
  (Rule 21 exception path) -- logged.
- No `comp-iam`/`comp-blast`/`comp-pipescript` run: this was read-only investigation (AWS CLI reads +
  source grep/read), no infra/data/code change made.

---

## What I did NOT do

- **Did not modify or redeploy `yang-model-portfolio-benchmarks`.** I don't own this pipeline (commit
  history shows `0.2.0_DS_PortfolioAnalytics` / `0.2.0_DT_PortfolioAnalytics` own it) and a live
  client-facing production data path is not mine to unilaterally patch from an investigation lane.
- **Did not re-trigger the pipeline.** Re-uploading a corrected 07-31 `data.pkl` (deduped) or re-running
  with the already-good 07-30 file would very likely restore correct state, but that is a
  production-data action belonging to the pipeline owner, not an ad-hoc AE move.
- **Did not build any alarm/monitor/SES.** Standing moratorium (CLAUDE.md, Andrew-direct 2026-07-28).
  This is a report + escalation, not new detection machinery.

---

## Next Steps

1. **[0.0.0_AB_MSTR / 1.0.0_SA_CTO / 2.0.0_SA_COO]** Escalating this finding now via MCP (same turn).
   Recommend: (a) DS/DT_PortfolioAnalytics re-publish from the already-known-good 2026-07-30 data
   immediately to stop serving the 07-27 regression, pending a real fix for the duplicate-labels defect
   in the 07-31 upload; (b) a monotonic date-guard on `yang-model-portfolio-benchmarks`' publish path
   (reject/warn on `data_as_of_date` older than currently-served) -- an actual fix, not a monitor; (c) the
   `data_refresh` Lambda's `handle_status()` history parser gets `PassStateEntered`/`PassStateExited`
   handling + `STATE_LABELS` entries for every `Skip*` state, so a skip is visible in the DataRefresh UX
   instead of silently absent.
2. **[0.2.0_DS_PortfolioAnalytics / 0.2.0_DT_PortfolioAnalytics]** Owning pod for
   `yang-model-portfolio-benchmarks` -- notified by MCP; not currently registered/live, message queued.
3. **[Andrew]** None yet -- this is a fresh finding, routing up the chain first per escalation discipline.

---

## MCP traffic

Sending now: MSTR (tasking authority for this investigation) + CTO + COO (broadcast, per finding
severity: live production surface currently serving regressed data) + DS_PortfolioAnalytics +
DT_PortfolioAnalytics (owning pod, queued).
