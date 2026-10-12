# NEVER-WIDEN co-sign, ROUND 9 -- the COO half: fred-data-ingestion retires its raw-series write; the daily yield-curve fold runs again (IAM-z-6 PHASE B)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-11 ~22:0xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-z-6` PHASE B, by
`0.7.0_AE_CloudOps~IR`, under NEVER-2 entry `iamroles-r9-fred-retire` | **Ruling:** `1.0.0_SA_CTO~Z` @`3e091a9436` | **Read
against:** `deliverables/0.7.0_AE_CloudOps~IR/round9/fred/FRED_SURVEY.md` @`5a7a6d999d` | **The other half:** `1.0.0_SA_CTO~Z`,
`ledger/NEVER_WIDEN_ROUND9_Z-6_CTO_HALF.md`.

**Verdict:** SIGNED for the blast radius below, and ONLY it. The form signed is the survey's section 0: the raw-series S3
write path is removed, the FRED fetch is kept, and the fold is untouched. This half binds an **equality check at apply time**,
because the module reads the artifact's `version_id` and `content-sha256` metadata live (`lambdas.tf:15-32`). The plan cannot
show the change until the artifact is uploaded (survey section 6).

## Baseline, re-read by this signer at 22:02Z (Z-S40)

| value | read at signing | survey (20:4xZ-21:3xZ) |
|---|---|---|
| served key versions | **1**: `4B7uNcT9Rli6_4LWUQORdWyhoBaABq.l`, 2026-08-05T23:02:30Z, 675314 B, IsLatest | same |
| deployed `CodeSha256` | `ztobyfBFFsd05mtbxVuWAn6nsMb7FwnhvftqdSQbSZ0=`, LastModified 2026-06-05T15:46:21Z | same (== base, per member) |

The apply re-reads both. If either has moved, the act is NOT SIGNED: stop and file a row.

## What the act MAY touch (the whole permitted set)

1. **One artifact:** `s3://opal-313476888478-lambda-artifacts/fred-pipeline/fred-data-ingestion.zip`. A new version is
   built by Option Y (the source map's sanctioned swap-into-deployed-zip). It differs from the deployed zip in exactly one
   member, `lambda_fred_ingestion.py` (sha256 head `4b6c649a` -> `cdb8a33a`); 194 of 195 members are content-equal.
   **content-sha256 = `KdzPgI23K0f4Af5dIOqbyJTQ2SaeZgR+pKI5T4rMdRM=`**, and the upload must carry that value as its
   `content-sha256` metadata. Member content is the grain this half binds; container bytes may differ (survey section 3).
2. **One function:** `aws_lambda_function.fred_data_ingestion`. After the upload, the targeted plan reads exactly 1 update
   on that address, its `source_code_hash` equal to `KdzPg...`. The untargeted plan reads 28 entries: 27 no-op plus that
   1 update. **Any other difference is NOT SIGNED:** a different hash, a second address, an add, a destroy, an env, a
   schedule or an IAM change.
3. **One served key, by the function's own next fires:** `s3://opal-data-portal-v2/json/macro/yield_curve_fred.json`.
   Its writer count is N=1: `ingest_yield_curve_fred.FREDYieldCurveIngestion.upload_to_s3`, reached only from this
   function's daily fold. The issuer read that rule at signing (`ingest_yield_curve_fred.py:256-299`). Nobody writes this
   key by hand.

**Rollback per key:**
- **The function:** re-pin the artifact data source to VersionId `T5QPdxBm94U_iA4R6iJscrZkVj_AWJDW` (content-sha256
  `ztoby...`) and apply through Terraform. Never `update-function-code`.
- **The served key:** restore VersionId `4B7uNcT9Rli6_4LWUQORdWyhoBaABq.l` by copy-object of that version. It is the
  only version, so this is the frozen state as it stands today.

## Every branch, read from the producer's own rule (`run()`, `ingest_yield_curve_fred.py:256-299`)

`run()` fetches the 10 tenors. A tenor whose fetch returns empty is carried forward from the prior artifact and logged
`PRESERVE:`. A tenor still empty is logged `NO-REGRESSION GUARD`. In every case where no exception escapes, `run()` then
**uploads**. So there are four branches, not two:

- **A -- fresh:** 10 tenors fetched. The key is written, and its newest observation is the last trading day before the
  fire: Friday 2026-10-09 for a Sunday fire; count trading days, not calendar days. **Done.**
- **A' -- preserved:** some or all fetches empty. The key is STILL written, with LastModified advancing, but the
  preserved tenors carry the 2026-08-05 artifact's observations. **AC1 can read PASS while the curve stays stale.** The
  `PRESERVE:` lines in the run log decide this branch, and the grade reads them. Nothing is rolled back: the data is real
  prior data. The order is NOT complete while the as-of trails; file a row and report.
- **B -- the fold raises:** nothing is written, and the key keeps `4B7u...`. The handler still returns 200, because the
  fold is best-effort. The grade reads `yield_curve_success=false`, never the status code alone. File a row, restore
  nothing, report.
- **C -- the handler breaks** (500, or any weekly or monthly fire newly failing): roll the function back as above, then
  file a row. Weekly and monthly fires currently fail for the same reason and are expected to move to 200. There are
  five fire paths (survey section 8), and every one is in scope of this branch.

## Sequencing (issuer ruling, signed here)

z-6 PHASE B runs BEFORE z-1's `FredIngestionLambdaRole` act. Once z-6 lands, nothing on the role calls
`opal-market-update`, so removing `S3Access` has no failure mode. The reverse order would only turn NoSuchBucket into
AccessDenied (survey section 9).

## What the act may NOT touch

`fred-macro-ingestion`; any schedule; any IAM document (z-1's `S3Access` and row Z-S49's dead secret grant are not this
act's); the vestigial copy under `portal/etl/orchestration/green/fred/` (Z-S49); every other key in `opal-data-portal-v2`.

## Provenance

Rows Z-S45, Z-S48, Z-S49; CTO ruling @`3e091a9436`; DECOMP_R9 section 7 @`1308fdf7d3`; survey @`5a7a6d999d`. Push state:
LOCAL.
