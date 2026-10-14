# Deploy Completion Record
**Date opened:** 2026-10-14T12:11:45.490730+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R29a: release 29 leg L2, irpt-status at expected CodeSha256 yNpw441TP5aMGYuZqkHQAPjAiQJDEPk7q8kFeDiIRIg= (status.py, CORRECTION_WORDS gains SHARES_PRICE_SOURCE_NOT_COMPOSED, code only); signed pair COO blob 5e8b3cbd95 + CTO half @abbfe49feb; rollback VersionId V_g2PtX08Ktkbo5XYohrB5pHDFctjzZE; resident (L4) and irpt-ycharts-generate (L3) not in this order
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | COO half hash 5e8b3cbd95; CTO half signed on that blob; diff hash 33b9de71; markers over every worktree, 0 live open entries naming irpt-status; R0b live CodeSha256 MIVrDbv+... and S3 latest version V_g2PtX08... equal and object hash equal | printed reads |  | OPEN |
| L2 | s3-prefix | throwaway worktree detached at d39886e4aa, guard printed, diff applied, BUILD_ONLY digest yNpw441T..., then upload of one new version, read back sha256 c8da70e38d53... | digest equal, VersionId, sha256 equal |  | OPEN |
| L3 | verify | scoped plan -target=module.irpt_status.aws_lambda_function.this: 0 add 1 change 0 destroy, attributes last_modified s3_object_version source_code_hash only | plan summary line |  | OPEN |
| L4 | activation | .tools/safe-apply.sh on the saved plan | apply line |  | OPEN |
| L5 | verify | S1 CodeSha256 yNpw441T..., S2 49 members only status.py differs, S3 credential-less envelope equal to before | printed reads |  | OPEN |
| L6 | git | map record: status.py row of the diff plus artifact_* and last_deployed_* in lambda-source-map.json, committed | commit hash |  | OPEN |

## Log

- 20261014T121145Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 6 leg(s)
