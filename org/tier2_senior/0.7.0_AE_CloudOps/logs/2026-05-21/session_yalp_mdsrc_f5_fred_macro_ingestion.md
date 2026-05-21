# AE 0.7.0 Session Log -- 2026-05-21 -- YALP_MDSRC.F5: fred-macro-ingestion Lambda commit + deploy

**Agent:** 0.7.0_AE_CloudOps (base lane)
**Status:** YALP_MDSRC.F5 COMPLETE -- fred-macro-ingestion deployed; macro_data_fred.json produced with 51 indicators.

---

## TL;DR

F5 is the AE deploy half of F4 (0.2.0_DS~A authored + verified the 51-indicator
FRED macro pull `ingest_fred_macro.py`). F5 committed it and deployed it as a
NEW Lambda `fred-macro-ingestion` in the existing `fred-pipeline` Terraform
module. Standard new-Lambda deploy -- Rule-1-clean natively (never
console-deployed, so no F2-style import path). One triggered run produced
`json/macro/macro_data_fred.json` with all 51 indicators. `fred-pipeline-v1.1.0`.

## Function identity (AC1)

`fred-macro-ingestion` -- a DISTINCT new function, not a variant of the existing
`fred-data-ingestion`. Separate concerns confirmed: separate 51-indicator pull
(vs the existing 8-indicator + yield-curve set), separate artifact
(`macro_data_fred.json` vs `macro_data.json`/`yield_curve_fred.json`), its own
EventBridge schedule, its own IAM role. No name collision.

## Source-directory decision (F2 coordination)

F4 placed `ingest_fred_macro.py` in `infra/aws/lambda/fred-data-ingestion/`
alongside the existing `lambda_fred_ingestion.py` + `ingest_yield_curve_fred.py`.
F5 moved it to its OWN source dir `infra/aws/lambda/fred-macro-ingestion/`.

Reason: `build-and-upload.sh`'s ADHC_DRIFTD.002 parity check requires
`source_dir == one function's complete file set` -- it ERRORs when a source dir
holds files not listed in that function's source-map `files[]`. The shared dir
would have forced a `BAU_PARITY_SKIP=1` override on every build (cultural
workaround vs structural fix). A clean own-dir is the structural resolution and
is pure relocation, not re-authoring. The two FRED Lambdas still share the same
TF MODULE (`fred-pipeline`) as the F5 TO requires -- only the source dirs split.

`fred-data-ingestion` is unaffected -- it does not use `build-and-upload.sh`
(it is the COO-signed-off Option-Y vendored-deps build per F2).

## Dual-source-of-truth check (F2 cross_domain_coordination heads-up)

The F5 TO flagged a possible main-repo-copy vs portal-ETL-copy split for the
FRED Lambda family. Checked: `ingest_fred_macro.py` is a NEW F4-authored file
that exists ONLY in the main repo (`infra/aws/lambda/`) -- there is no
portal-ETL copy. Single source of truth, clean. (The dual-copy situation that
F2 reconciled applied to `ingest_yield_curve_fred.py`, not the macro pull.)

## Deps layer (Rule 3)

`ingest_fred_macro.py` needs `numpy` + `requests` (boto3 is in the Lambda
runtime). Phase-0 question -- new layer or reuse? Resolved by inspecting the
existing layer zips: `pandas-pyarrow-requests-layer:1` (py3.11) carries
importable `numpy` (via pandas) AND `requests` (verified: both have
`__init__.py` in the layer zip). Reused it -- no new layer build. Rule 3
satisfied (use an existing layer; no `pip install -t .`).

## Deploy (AC2)

- Code: `infra/aws/lambda/fred-macro-ingestion/ingest_fred_macro.py` committed
  `90aebdf9f` (safe-commit).
- Terraform (`fred-pipeline` module, committed `d67494cef`):
  - `lambdas.tf` -- `aws_lambda_function.fred_macro_ingestion` (py3.11,
    256MB/120s, x86_64, handler `ingest_fred_macro.lambda_handler`,
    `pandas-pyarrow-requests-layer:1`) + log group (14d retention).
  - `iam.tf` -- new TF-managed `FredMacroIngestionLambdaRole`: basic execution
    (CloudWatch Logs) + `secretsmanager:GetSecretValue` on `opal/external-apis`
    + `s3:PutObject` on the ONE key `macro_data_fred.json` (no wildcard).
  - `eventbridge.tf` -- `fred-macro-ingestion-daily` rule `cron(30 23 * * ? *)`
    (23:30 UTC, 30 min after `fred-ingestion-daily`).
- `lambda-source-map.json` -- `fred-macro-ingestion` entry (Rule 4); artifact
  fields populated by `build-and-upload.sh` (`468d02bf9`).
- Build: standard `build-and-upload.sh fred-pipeline fred-macro-ingestion` --
  single-file source, deps in the layer (no vendored-deps Option-Y needed,
  unlike F2's fred-data-ingestion). SHA256 `I+IbWj9JKUE+3HE2+K5qL/40xxCis7lonABrJ6E0z5M=`.
- Apply: `safe-apply.sh` (HALTGT checkpoint clean -- empty inbox). **9 added /
  0 changed / 0 destroyed.** 0-diff replan: "No changes." F2's existing
  fred-data-ingestion resources untouched (0 changed).
- `record-terraform-deploy.sh` -> `f295f4fc0`; tag `fred-pipeline-v1.1.0`;
  pushed `origin/CLOUD --follow-tags`.

## Verification (AC3)

One run triggered (`aws lambda invoke`, empty payload = full run). StatusCode
200; handler return `indicator_count: 51`, `output_key
json/macro/macro_data_fred.json`. S3 artifact pulled + parsed:
**51 indicators across 9 groups** (Lagging 7 / Financial Condition 4 /
Inflation 7 / Labor Market 8 / Consumer 6 / Housing 5 / Treasury Yields 10 /
Market Indicator 1 / Currency 3 -- every group's `count` matches actual).
`data_as_of 2026-05-01`, LastModified 2026-05-21 13:57Z, 72944 bytes. The
`fred-macro-ingestion-daily` EventBridge schedule keeps it fresh going forward.

## Compiler Tools (AC4)

| Phase | Tool | Result |
|-------|------|--------|
| 1 (before deploy) | `comp-iam service fred-macro-ingestion` | "No service matching" -- not a comp-graph node (a newly-TF'd Lambda; consistent with the F2 finding for fred-data-ingestion). `FredMacroIngestionLambdaRole` IS recognized from the committed `iam.tf`. IAM verified by direct read of the script's boto3 calls instead: `secretsmanager.get_secret_value` -> `secretsmanager:GetSecretValue` granted; `s3.put_object` -> `s3:PutObject` on macro_data_fred.json granted; CloudWatch Logs -> basic-execution granted. No gap. |
| 2 (before commit) | `.tools/ds-commit-gate.sh ingest_fred_macro.py` | exit 0 (py_compile + ds-precommit-check + ruff py39) -- re-confirmed F4's gate-clean result at commit time. |
| 3 (after deploy) | 0-diff plan + deployed-SHA match | `terraform plan` post-apply = "No changes." Deployed `CodeSha256 I+IbWj9JKUE+3HE2+K5qL/40xxCis7lonABrJ6E0z5M=` == build SHA == source-map `artifact_sha256` -- MATCH (the Lambda equivalent of `comp-pipescript deployed` MATCH; `comp-pipescript deployed` itself is an EC2-gold-runner tool, N/A for a Lambda). |

## Current State

| Item | Status |
|------|--------|
| YALP_MDSRC.F5 | COMPLETE -- fred-macro-ingestion deployed; macro_data_fred.json 51 indicators; RAVC2 to COO + CC CTO + CC DS~A |
| Tag | fred-pipeline-v1.1.0 |
| YALP_MDSRC.C1 | queued -- COO dispatches on the F5 report |
| YALP_MDSRC.SEC1 | background/P3 -- Phase-0 grep-scan ran; pick up only in non-chain windows |

## Commits this session (F5)

| Commit | Scope |
|--------|-------|
| `90aebdf9f` | ingest_fred_macro.py (moved to own source dir, committed) |
| `d67494cef` | fred-pipeline TF -- function + IAM role + EventBridge + source-map entry |
| `468d02bf9` | source-map artifact fields (build-and-upload.sh) |
| `f295f4fc0` | record-terraform-deploy.sh -- CHANGELOG + last_deployed |
| tag | `fred-pipeline-v1.1.0` |

## v0.4 carry-forward (out of F5 scope, surfaced by F4)

- The FRED-vs-Bloomberg-residue MERGE (whether `macro_data_fred.json` merges
  into `macro_data.json`) -- a v0.4 integration decision. F5 ships the separate
  artifact as built; no dual-writer.
- Indicator overlap between `ingest_fred_macro.py` (51) and the existing
  `lambda_fred_ingestion.py` (8) -- v0.4 FRED-architecture consolidation.
- `macro_data.json` Fed Balance Sheet unit mislabel (raw $M under unit "B") in
  `yang-generate-macro` -- F4 finding F4-3; F5's FRED value is correct $B.
