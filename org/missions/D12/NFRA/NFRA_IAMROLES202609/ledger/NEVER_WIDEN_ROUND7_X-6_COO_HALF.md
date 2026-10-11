# NEVER-WIDEN co-sign, ROUND 7 -- the COO half: deploy smartx-pipeline's three drifted Lambda versions + the ratified output nulls (IAM-x-6 PHASE B, E4 act)

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-11 ~12:4xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-x-6` PHASE B: ONE
untargeted apply of `infra/aws/terraform/smartx-pipeline` by `0.7.0_AE_CloudOps~IR`, under a NEVER-2 entry | **Ruling:**
`1.0.0_SA_CTO~Z` @`20c0a85d55` (DEPLOY all three) | **Read against:**
`deliverables/0.7.0_AE_CloudOps~IR/round7/smartx_deploy/SMARTX_DEPLOY_SURVEY.md` @`3fade2bc55` | **The other half:**
`1.0.0_SA_CTO~Z`, `ledger/NEVER_WIDEN_ROUND7_X-6_CTO_HALF.md`.

**Verdict:** SIGNED for the blast radius below, and ONLY it. **What this half binds is an EQUALITY CHECK at apply time, not
a saved plan file** (the assignee's ask, msg 33272). The module reads `s3_object_version` from the live latest object
(row Z-S41), so a re-upload between survey and apply moves the after-values.

## What the act MAY touch (the whole permitted set), as values

| function | `s3_object_version` before -> after | `source_code_hash` before -> after | running code changes? |
|---|---|---|---|
| `aws_lambda_function.assets_daily_pull` | `XmkW9C_XX1J_6sREU2VZ2naPbfmRQa7O` -> `QNIiMQgfRzxG_KrI_6mVxJDjJbZFOnsd` | unchanged `4Iw0TWcez71pRQoUK0GXPxGMOAsVMIgMBIGhk+JRk8k=` | NO (pointer only) |
| `aws_lambda_function.jwt_refresher` | `lRZrP4cIcsSbeYBd8SIB6_W8No75LiDw` -> `HAmOeAkTP0mT6304E9OvUVTpk_GhC8hh` | unchanged `MCsLEpIgbLtNDTbSDke9CnlBCmxEhN5slexYv2FIjSc=` | NO (pointer only) |
| `aws_lambda_function.rest_pull` | `Way7ManCnOWA8bAdT8YIAzZ0ncPu4ino` -> `g_1WqvOSlrPbM1uf8nFcy0uG9SB4xXwb` | `SnPiO8B8AxABQOxJ2wfoPDFaCxaVeGmcDsVPv0JrzaE=` -> `lM6cnuZTetkFwkGmxQqBFslExfqwGp+WhqFYOYM81xE=` | YES: one docstring line in smartx_jwt_reader.py (CTO's diff, committed source 46d0b98aef) |
| outputs `autostart_lambda_arn`, `autostart_role_arn`, `eventbridge_rule_arn` | -> null (deleted) | -- | the Andrew-ratified removal (a3b36fd877 / @874b52729c) completed |

Rollback per function: a Terraform update back to the BEFORE object version (pin the data source's `version_id`, then
apply). Never `aws lambda update-function-code`.

## The equality check (binding at PHASE B, step 4)

Re-plan at apply time (the saved file may be used only if it still exists AND re-grades identically). The plan must read
`0 to add, 3 to change, 0 to destroy`, with exactly the three addresses above, each `s3_object_version` and
`source_code_hash` EQUAL to the table's after-values, and exactly 3 output deletes. **Any difference** (a moved after-value
from a re-upload, a fourth address, an add or destroy, an output beyond the three) is NOT SIGNED: the act stops and files a
row.

## What the act may NOT touch

Every other address in `smartx-pipeline` (47 resource_changes in the survey, 44 no-op); no IAM; no add, no destroy. The
module's live-latest design gap (Z-S41) is not fixed here.

## Both branches of every outcome named

- **Plan equal to the table -> apply; afterwards live `CodeSha256` equals the after `source_code_hash` for all three (two
  unchanged, rest_pull now `lM6cn...`), the module re-plans 0/0/0, and ONE scheduled `smartx-rest-pull` invocation reads
  SUCCEEDED on the log plane:** Branch A, done. **rest_pull failing after the change, or any CodeSha256 off the table:**
  Branch B. Roll back rest_pull to `Way7...` through Terraform, then file a row.
- **Plan not equal to the table:** no apply. File a row with the new values. A re-survey and a fresh pair are owed.

## Provenance

CTO ruling @`20c0a85d55`; x-3 table @`c951e42cae`; DECOMP_R7 section 10 @`935b63a027`; survey @`3fade2bc55`; rows Z-S21,
Z-S41. Push state: LOCAL.
