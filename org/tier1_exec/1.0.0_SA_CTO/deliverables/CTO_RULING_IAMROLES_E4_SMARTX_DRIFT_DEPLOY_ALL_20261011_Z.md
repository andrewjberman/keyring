# CTO RULING -- NFRA_IAMROLES202609 E4 (row Z-S21): smartx-pipeline drift -- DEPLOY all three, outputs ride

**By:** `1.0.0_SA_CTO~Z`, 2026-10-11 ~11:3xZ. **On:** `2.0.0_SA_COO~ZI` msg 33257; table
`deliverables/0.7.0_AE_CloudOps~IR/round7/smartx_drift/SMARTX_DRIFT_TABLE.md` @c951e42cae (round-6 analysis Addendum 1).

## Ruling

| item | ruling | basis |
|---|---|---|
| `assets_daily_pull`, `jwt_refresher` | **DEPLOY** (the table's recommendation) | the new S3 version is byte-identical to the running one (same ETag and size); the apply moves a pointer and runs the same code |
| `rest_pull` | **DEPLOY, which overturns the table's HOLD** | this seat's own read, below: the 2-byte difference is a comment, and its source IS committed |
| the three null outputs | **ride the apply** | their deletion was Andrew-ratified (a3b36fd877 / @874b52729c); the nulls complete that removal |

### `rest_pull`, read by this seat (artifacts downloaded and unzipped in a scratch directory, never run)

- `list-object-versions` on `opal-313476888478-lambda-artifacts/smartx-pipeline/smartx-rest-pull.zip`: 12 versions. The
  6,610-byte version (`Way7...`, 2026-06-05) is the one that runs. **The 6,608-byte content first appeared on 2026-07-23,
  not 2026-08-19**, and was re-uploaded 5 times up to the current `g_1W...`.
- File-by-file diff, running vs latest: `lambda_function.py` and `pull_smartx_models_rest.py` are identical. In
  `smartx_jwt_reader.py`, line 3 of the module docstring changes from `data/orion/manual_api/jwt_freshness.py` to
  `data/inf/manual_api/jwt_freshness.py`. **No executable line differs.**
- That line is the repo's source: `infra/aws/lambda/smartx_rest_pull/smartx_jwt_reader.py:3` at HEAD, last changed by
  **46d0b98aef** (2026-06-11, `NFRA_DTAFLP.P1-AE ... data/orion->data/inf` path sweep). The table's "no commit produced them"
  is corrected: the commit exists, and it is the source map's own `last_deployed_commit`. The map's `artifact_sha256`
  is the correct "after" value. Only the deploy never ran.

## The act

ONE apply of `infra/aws/terraform/smartx-pipeline`, by `0.7.0_AE_CloudOps~IR`, under a NEVER-2 entry and a never-widen pair
cut by the issuer. Its plan must read exactly `0 to add, 3 to change, 0 to destroy`, consisting of:
- the three functions' `s3_object_version` (and `rest_pull`'s `source_code_hash`) moving to the versions the table names;
- the three output nulls.

Anything else stops the act. After the apply:
- live `CodeSha256` equals the plan's after-value for all three;
- one scheduled invocation of `smartx-rest-pull` succeeds (read on the log plane);
- the module re-plans 0/0/0.

Rollback per function is `update` back to the prior object version through Terraform (pin the data source's
`version_id` to the old version, apply), never `update-function-code`.

## Carried, not ruled here

The table's design point stands. The module reads `s3_object_version` from the LIVE latest object, so any re-upload
re-opens the drift with no commit behind it. Pinning the version, or deriving it from the build, is the module owner's
choice, and **no project owns `smartx-pipeline`**. The issuer records it as an INERT row naming that gap. It is not
cut in this project.

-- 1.0.0_SA_CTO~Z
