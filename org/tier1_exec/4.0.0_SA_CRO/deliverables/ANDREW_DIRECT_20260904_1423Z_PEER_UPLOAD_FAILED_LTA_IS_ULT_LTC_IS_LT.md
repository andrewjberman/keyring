# ANDREW-DIRECT 2026-09-04 ~14:2xZ-14:4xZ -- Yang's peer-ranking upload failed; LTA is now ULT, LTC is now LT

**Receiving seat:** 4.0.0_SA_CRO~C (Claude terminal, this session)
**Channel:** Claude Code terminal, mid-turn messages, 2026-09-04 (Yang's Teams message 14:23:24Z; Andrew's reply to Yang "Hey Yang, checking into it now" 14:23:57Z)
**Scope:** VERBATIM below. The receiving seat does not adjudicate scope.

## Verbatim

Message 1 (with a screenshot of the portal Data Refresh page showing "Pipeline Failed", 18 steps, Generate JSON Files 0/1):

> Look at Yang's message on MS Teams. Afterwards, check the execution logs for "Data Refresh" pipeline from the opalinvest.dev portal. It would appear Yang's upload of the Peers data failed for some reason.

Message 2:

> LTA is now ULT and LTC is now LT, see if they have that in the fields where previously LTA and LTC were expected/housed.

Yang Liu's Teams message (1:1 chat with Andrew, 2026-09-04T14:23:24Z), verbatim:

> good morning, Andrew. The peer ranking upload seems not to work any more. the source data is in the same format

## What was measured (EXERCISED, this session)

| # | Object | Instrument | Reading |
|---|---|---|---|
| 1 | Step Functions `YangDataPipeline` executions | `list-executions` (40 returned) | `20260904_v1-06273296` FAILED 14:20:27Z; `20260904_v1-3c6fdaa5` FAILED 14:22:12Z; `20260804_v1-74331a80` FAILED 2026-08-04T13:18:16Z (never noticed) |
| 2 | Execution `3c6fdaa5` history (64 events) | `get-execution-history` | only `GeneratePeerPerformance` failed: `LambdaFunctionFailed` x2 (retry once), `ParallelStateFailed`, `PipelineFailed` |
| 3 | `/aws/lambda/yang-generate-peer-performance` stream `2026/09/04/[$LATEST]7f792c1b...` (54 events) | `get-log-events` | 4 invocations, each: `Extracted UST, INT, ST` then `ValueError: ... missing expected models: ['LTA', 'LTC']` at `lambda_function.py:135 validate_peer_output` |
| 4 | Live Lambda config | `get-function-configuration` | `LastModified=2026-06-26T16:50:42Z`, `CodeSha256=uhHb2esvNIC/QAVo1mJ50kVma0Rv5WJdJ5rQXytWUeg=` == the 2026-06-26 guard deploy (yang-v2.4.15, commit 7f77542de). Code unchanged since; the SOURCE changed. |
| 5 | `Models Performance vs Peers 20260731.xlsx` archived 2026-08-03 (exec-a18d45745369, 566,233 B) | openpyxl, Peer Table col AA | R28 `Aggressive growth daily returns` 1Y=18.5667; R29 `Conservative growth daily returns` 1Y=17.2745 -- the run that wrote the served JSON |
| 6 | Same filename re-uploaded 2026-08-04 (exec-8c07d2cebfae, 559,445 B) | openpyxl | R28 `Long term daily returns` 1Y=17.2745; R29 `Ultra long term daily returns` 1Y=18.5667 -- RENAMED, values swapped rows; run FAILED |
| 7 | `Models Performance vs Peers 20260831.xlsx` (today, 558,689 B) | openpyxl | R28 `Long term daily returns` 1Y=15.6316; R29 `Ultra long term daily returns` 1Y=16.6039 |
| 8 | Served `json/peers/peer_performance.json` | `s3 cp` | `generated_at 2026-08-03T13:54:45Z`, `data_as_of 2026-07-31`; LTA 1Y=18.5667, LTC 1Y=17.2745 |
| 9 | Portal FE | `Grep portal/src` | `lib/modelPortfolioColors.ts:226-227` labels LTC='Long Term', LTA='Ultra-Long Term'; `:371-372` aliases `LT: 'LTC'`, `ULT: 'LTA'`; consumer `pages/ModelPortfolios.tsx:571` |

**Answer to message 2:** YES. In the block where LTA/LTC were housed (Peer Table, block 4, header R17 col AA "Return/Risk - Long Term"), the model rows are now R28 `Long term daily returns` and R29 `Ultra long term daily returns`. The 1-Year values tie them: `Long term` == the served LTC number (17.2745) and `Ultra long term` == the served LTA number (18.5667). So LT = old LTC (Conservative growth) and ULT = old LTA (Aggressive growth), as Andrew stated. The rename first appeared in Yang's 2026-08-04 re-upload of the July file, whose run failed unnoticed; the served page stayed on the 2026-08-03 artifact.

**Root cause:** `MODEL_MAP` in `yang-generate-peer-performance/lambda_function.py` recognises `aggressive growth` / `conservative growth` but not `ultra long term` / `long term`, so the parser yields 3 of 5 models and the 2026-06-26 fail-closed guard (`validate_peer_output`) raises. The guard did its job: no partial artifact was written.

## Fix applied LOCAL (uncommitted at time of writing; lane = DT/AE, not CRO)

`infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-generate-peer-performance/lambda_function.py`: `MODEL_MAP` gains `'ultra long term': 'LTA'` (ordered BEFORE `'short term'`, since first-substring-wins) and `'long term': 'LTC'` (LAST, since it is a substring of the others); both label generations accepted so archived files re-run. `MODEL_NAMES` LTC='Long-Term', LTA='Ultra Long-Term'. Internal codes stay LTA/LTC because the FE keys on them and already aliases ULT/LT.

Harness (scratchpad, parser-independent raw-cell oracle for every model's 1Y value), PRE = `git show HEAD:` source, NEW = patched:

```
peers_20260630.xlsx        PRE 5/5 VALID   NEW 5/5 VALID   1Y-vs-raw mismatches: none
peers_20260731_aug3.xlsx   PRE 5/5 VALID   NEW 5/5 VALID   1Y-vs-raw mismatches: none
peers_20260731.xlsx (aug4) PRE 3/5 RAISE   NEW 5/5 VALID   1Y-vs-raw mismatches: none
peers_20260831.xlsx        PRE 3/5 RAISE   NEW 5/5 VALID   1Y-vs-raw mismatches: none
```

PRE reproduces the live failure on the two renamed files (positive control); NEW passes all four.

## Deploy path (NOT executed by this seat)

Build+upload `infra/aws/lambda/ci/build-and-upload.sh` -> `s3://opal-313476888478-lambda-artifacts/yang-pipeline/yang-generate-peer-performance.zip` -> `safe-apply` in `infra/aws/terraform/yang-pipeline` (module `generate_peer_performance`, `lambdas.tf:214`) -> Yang or Andrew clicks Retry Upload on the portal Data Refresh page (the 20260831 file is still in `uploads/`). Change-management ledger entry required at start.
