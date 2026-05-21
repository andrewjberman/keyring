# AE 0.7.0 Session Log -- 2026-05-21 -- YALP_MDSRC.F2: fred-pipeline IaC + yield-curve staleness fix

**Agent:** 0.7.0_AE_CloudOps (base lane)
**Status:** YALP_MDSRC.F2 COMPLETE -- yield_curve_fred.json refreshing; fred-data-ingestion now IaC-managed.

---

## TL;DR

`yield_curve_fred.json` (the Macroeconomics yield-curve drill-down) was ~4 months
stale because the yield-curve ingest had no deployed runner or schedule. F2:
folded the yield-curve ingest into the `fred-data-ingestion` Lambda's daily
path, and -- per the CTO Rule-1 ruling -- brought that console-deployed Lambda
into IaC via a new `fred-pipeline` Terraform module + a scoped import.
yield_curve_fred.json now `data_as_of 2026-05-21`, on a live daily schedule.

## P0 -- diagnosis

`yield_curve_fred.json` is produced only by `ingest_yield_curve_fred.py`, a
standalone script with no deployed Lambda and no EventBridge schedule. It ran
manually until 2026-01-15, then stopped. The deployed `fred-data-ingestion`
Lambda (8 other indicators) never touched it. Also surfaced: the fred Lambda
family had NO IaC at all -- a Rule-1 gap.

## P1 -- CTO-ruled mechanism

- **Code-fold:** `lambda_fred_ingestion.py`'s `frequency=='daily'` path now
  imports `FREDYieldCurveIngestion` and runs it best-effort (a yield-curve
  failure is logged, does not fail the FRED ingest). `ingest_yield_curve_fred.py`
  brought into the main-repo Lambda source dir (emoji stripped, future-import
  added). Canonical copy confirmed by SHA256 vs the deployed zip.
- **IaC:** new `infra/aws/terraform/fred-pipeline/` module (COO Option-A GO) --
  the `fred-data-ingestion` function + 5 EventBridge rules/targets/permissions,
  authored to match the verified deployed config exactly.
- **Build:** Option Y (COO-signed-off) -- the standard build-and-upload.sh
  cannot build a vendored-deps zip; instead downloaded the deployed zip,
  swapped only the 2 code-fold .py, re-zipped, uploaded. Deps byte-identical.
- **Import:** 17 resources imported into `fred-pipeline/tfstate`. Import plan:
  0 add / 7 change / 0 destroy -- the only non-tag change was the function code
  artifact (the code-fold delta); the rest module tags. One TF authoring error
  caught pre-surface + fixed (log-group retention 30 -> 0 to match deployed).
  Surfaced to COO+CTO; unified GO Option (a) -- apply with the module tags.
- Applied: 0 add / 7 change / 0 destroy; 0-diff replan clean. `fred-pipeline-v1.0.0`.

## P1 follow-on -- the AccessDenied (AC2 verify caught it)

The AC2 daily-run verify exposed an AccessDenied: the yield-curve fold writes
`opal-data-portal-v2/json/macro/yield_curve_fred.json`, but
`FredIngestionLambdaRole`'s pre-existing grant only covered the original
Lambda's `opal-market-update/fred/*`. The best-effort try/except contained it
(the FRED ingest still succeeded). Surfaced to COO+CTO; unified GO for a 1-key
least-privilege grant: `aws_iam_role_policy.fred_ingestion_yield_curve_write` --
`s3:PutObject` on exactly the one artifact ARN, no wildcard. Applied 1-add /
0-diff. `fred-pipeline-v1.0.1`.

## P2 -- verification

Re-triggered the daily `fred-data-ingestion` run: StatusCode 200, success:true,
3 FRED series, **yield_curve: {success:true, series_count:10}**. S3:
`yield_curve_fred.json` -- `data_as_of 2026-05-21`, `generated_at
2026-05-21T13:26:14Z` (fresh today; was frozen 2026-01-15). AccessDenied gone.
The `fred-ingestion-daily` EventBridge schedule keeps it fresh going forward.
Independent verification: ~A's harness (`docs/briefs/f2f3_fred_deploy_verify.py`)
signalled apply-complete -- ~A RAVC2s the verdict.

## Lane coordination

A concurrent `0.7.0_AE_CloudOps~A` lane started during a base rate-limit and
briefly began F3. Coordinated: ~A stood down (4/4 confirm -- no terraform, no
git, no fred-pipeline files), COO formally ruled base owns F2/F3/F5/C1 + ~A
barred from terraform (verification-harness only). ~A had erroneously
deleted+restored `fed_balance_sheet_as_pct_of_gdp.json` -- independently
verified intact (clean delete-marker-removal restore, no content rewrite).

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-iam gaps` (post iam.tf change) | 2 gaps, both the pre-existing unrelated `mdpf-daily-trigger` finding; 0 new gaps from the F2 grant. |
| `comp-iam service fred-data-ingestion` | "No service matching" -- not a comp-graph node (newly TF'd Lambda; documented, consistent with prior fred/inf-runner findings). |
| `ds-commit-gate.sh` | exit 0 on the 2 .py (lambda_fred_ingestion.py + ingest_yield_curve_fred.py). |
| Import plan | the STOP-on-drift artifact -- 0 add/0 destroy, sole non-tag change = code-fold delta; surfaced before apply. |

## Current State

| Item | Status |
|------|--------|
| YALP_MDSRC.F2 | COMPLETE -- yield_curve_fred.json fresh; fred-data-ingestion IaC-managed; RAVC2 to COO+CTO |
| Tags | fred-pipeline-v1.0.0 (import) + fred-pipeline-v1.0.1 (IAM grant) |
| YALP_MDSRC.F5 | clear to dispatch (F2 functionally complete) |
| YALP_MDSRC.C1 | queued after F5 |
| YALP_MDSRC.SEC1 | background/P3-tier (Andrew deprioritized -- free API keys); Phase-0 grep-scan was running; pick up only in non-chain windows |

## Commits this session (F2)

| Commit | Scope |
|--------|-------|
| `b0e05c363` | fred-pipeline TF module (function + schedules + IMPORT_COMMANDS.sh) |
| `fae806585` | yield-curve code-fold into lambda_fred_ingestion.py |
| `70652b005` | source-map entry + retention match + provider lock (apply commit) |
| `0aa486bee` | the 1-key IAM grant (yield-curve S3 write) |
| record-deploy | `92f8f0d07` (v1.0.0) + `09bf342ab` (v1.0.1) |
| (this commit) | F2 closeout -- TO complete + session log |
