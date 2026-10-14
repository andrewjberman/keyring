# Deploy Completion Record
**Date opened:** 2026-10-14T01:45:34.260138+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R28a unit L2: irpt-status ops/status.py (CORRECTION_WORDS gains TICKER_KEPT_BY_HISTORY, TICKER_CHECK_FAILED, TICKER_NOT_CHECKED; words only) to CodeSha256 MIVrDbv+..; pair COO blob e9bb20d7fe + CTO half @d3adae2fc8
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | COO half hash e9bb20d7fe; census over every live worktree (open entries naming irpt-status or opal-ticket-api); R0b live CodeSha256, key latest version and object hash; R0d fresh turned_back 0; A3 before envelope | reads printed |  | OPEN |
| L2 | s3-prefix | detached worktree at a4b7c48fad (core.longpaths), guard printed, repin diff da4e88d212 applied uncommitted, BUILD_ONLY digest equals MIVrDbv+.., then upload, read back equals the staged zip 30856b0dbbfe | digest, VersionId, readback |  | OPEN |
| L3 | verify | scoped plan -target=module.irpt_status.aws_lambda_function.this: 0 add 1 change 0 destroy, last_modified s3_object_version source_code_hash only | plan summary and attributes |  | OPEN |
| L4 | activation | safe-apply on the saved plan | Apply complete 0/1/0 |  | OPEN |
| L5 | verify | S1 CodeSha256 MIVrDbv+..; S2 49 members, only status.py differs from 2_5Slkao1..; S3 credential-less refusal envelope equals A3 before | S1-S3 |  | OPEN |
| L6 | git | status.py row of the repin diff plus artifact_* and last_deployed_* applied to the trunk map in own worktree; commit | commit hash |  | OPEN |

## Log

- 20261014T014534Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 6 leg(s)
