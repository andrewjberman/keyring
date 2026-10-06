# The stale-benchmark guard on `yang-model-portfolio-benchmarks` -- never-widen half (COO), `2.0.0_SA_COO~Z`, 2026-10-06 ~14:0xZ

**Route:** track 1 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_INDEX_BENCHMARK_FIX_ROUTE_20261006.md` @5e0c045e8d. It is
Andrew-direct singular priority (msg 30062). This seat was seated as owner by `0.0.0_AB_MSTR~Z` (msg 30084).

**Executor:** `0.7.0_AE_CloudOps~RV`, as a SEAT act.
- Its lane `YANG_PIPELINE_DEPLOY` owns both paths, read at HEAD with `owned-paths-validate.check_agent`: True for AE~RV, and False
  for this seat as the negative control.
- Its only order, ETFS_RIVALS RIV-iam-1, reads `complete`.
- No tree project carries this fix (`org/projects/OPAL_BBGTML.json` reads `status: closed`), so no task order is minted. This pair
  is the bound.

## THE ACT (three legs, in this order, under ONE NEVER-2 entry)

1. **Code leg.** In `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py`, in the
   model loop (~`:222-284`), apply a per-series recency guard:
   - For each model's `index_benchmark` and `etf_benchmark` series, read its LAST non-null bar.
   - If that bar is BEFORE `end_date` (`data_as_of`), the series returns `None` for EVERY period, with volatility `None` and the
     spread `None`. A window is never silently shortened.
   - Add `benchmark_last_date: {"index": "<YYYY-MM-DD>", "etf": "<YYYY-MM-DD>"}` to each model in the comprehensive output, and the
     same per model in the legacy output if that format carries per-model objects.
   - Model rows are untouched. The daily timeseries is untouched.
   - A plant test beside the function (the same directory, `test_stale_benchmark_guard.py`) covers three cases: a series ending
     before `data_as_of` serves null on all 10 periods with its last date; a series ending AT `data_as_of` still computes; model
     values are unchanged.
2. **Deploy leg.** Terraform only (`infra/aws/terraform/yang-pipeline/`, the function's existing module), through `safe-apply`, never
   `update-function-code`.
   - Build the artifact the module's existing path builds, from a commit that carries ONLY the code leg's two files.
   - Grade the plan UNTARGETED. It shows exactly this function's code change; any other resource is a STOP.
3. **Re-serve leg.** ONE invoke of the deployed function on the CURRENT data PKL (the key `LATEST.json` names, data_as_of
   2026-10-05), in the shape of the S3 or Step Functions event it already takes, WITHOUT `force_publish`.
   - The monotonic publish guard passes, because the incoming data_as_of equals the served one.
   - The function writes its three keys (below).

## THE BASE, read live at signing (13:5xZ) -- the rollback per key

| object | value | rollback |
|---|---|---|
| function CodeSha256 | `dHTjheKzauUziiPc6Jkwn7Ys+C36Xb5KS0aAWPh7Th8=`, python3.12, 512 MB, LastModified 2026-08-04T19:44:48Z | prior artifact through the module, one safe-apply |
| `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json` | 19,190 B, 2026-10-06T12:31:21Z, VersionId `9NuMvtEAPll77jLbwgGKki5y7oVS9U8M`, data_as_of 2026-10-05 | re-put the bytes of that version (copy-object from the VersionId), never a delete |
| `.../json/benchmarks/benchmark_returns.json` | 12,505 B, same time, VersionId `JJStBVZG4cRu0XHd5axb_EVvVvnHHx.S` | re-put that version's bytes |
| `.../json/benchmarks/model_portfolio_timeseries.json` | 768,530 B, same time, VersionId `QeBEvgycTlhaOGyt3x1QfhlcvhlRcrek` | re-put that version's bytes |

**Served at the base:** all 5 models' index benchmark is null on 1D/WTD/MTD/QTD; the ETF benchmark is null on the same four periods
for UST, ST, LT and ULT (INT's ETF is current). The other six periods (1M, 1Q, YTD, 1Y, Since Inception, TTW) of those nine series are
POPULATED, compounded only through 2026-09-29 against a model through 2026-10-05: the wrong numbers this guard stops.

## WRITERS OF WHAT MOVES (NEVER-1)

- **The three served keys: N = 1 code writer,** this function. The CHANGELOG records the retired `yang-generate-benchmark-returns`
  Lambda as removed (MDLP_VOLAUD.003), so this function is the single source.
  - It is reached by three triggers: the YangDataPipeline Step Function, the S3 `benchmarks/*.pkl` trigger, and the /data-refresh
    channel. All three run the SAME code after the deploy.
  - This act's manual invoke (leg 3) is a fourth entry onto the same code, on the same PKL the scheduled path last used. It creates
    no new data state: same data_as_of, same inputs.
- **The function's code: N = 1 writer,** this act.

## EXPECTED OUTCOMES (both branches), read from the producer's own rule

| check | before | expected after | if not |
|---|---|---|---|
| the 9 stale series (index UST, ST, INT, LT, ULT; ETF UST, ST, LT, ULT): null cells | 4 periods each | **10 of 10 periods null**, `benchmark_last_date` 2026-09-29 | rollback: prior artifact, then re-put the three keys' base versions |
| INT's ETF benchmark | values on 10 periods | **byte-equal values**, `benchmark_last_date` 2026-10-05 | rollback (the guard nulled a current series) |
| every model's `model` value and volatility, all 10 periods | values | **equal** | rollback |
| the timeseries | 768,530 B | equal except `generated_at` | rollback of the key |
| plant test | -- | 3 of 3 pass | STOP before the deploy leg |

**When the CIX owner fixes the source (track 2)** and the PKL reaches data_as_of, the guard serves numbers again, with no code change.
That is track 3's proof, not this act's.

## SIGNED

`2.0.0_SA_COO~Z`, 2026-10-06 ~14:0xZ. The CTO half is owed by `1.0.0_SA_CTO~Z` (its ruling's track 1 names it).
