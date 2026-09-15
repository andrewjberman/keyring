# Deploy Completion Record
**Date opened:** 2026-09-15T19:46:13.726982+00:00
**Status:** OPEN
**Deploy:** POSN_AGGFIX AF1-s-11: auth-validator-edge refuses the Opal-only aggregate outside Opal
**Authored by:** 0.9.0_WK_POSN_AGGFIX~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | branch carries index.mjs + aggregate_gate.mjs | commit hash | commit 240fe36222 on branch wk-posn_aggfix-1-2 carries infra/aws/lambda-edge/auth-validator-edge/index.mjs (M) + aggregate_gate.mjs (A); git diff --stat 605c03f81f HEAD -- infra/aws/lambda-edge/ = 2 files, 73 insertions (C1-AC5) | CLOSED 20260915T195049Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts portal-auth/auth-validator-edge.zip | sha256 + VersionId | s3://opal-313476888478-lambda-artifacts/portal-auth/auth-validator-edge.zip VersionId zNqzzAOFvq1LnTji4BV2_OymHRfr.bXI content-sha256 fekWqHP2cWuewpfFOnlxa2S5jBhxmKKs8eB4/QccRxs= (head-object after the build, 2026-09-15T19:50:30Z); get-object of that VersionId re-hashed to the same sha256 and its index.mjs carries aggregate_denied x1 and the gate message x1; rollback pair: prior VersionId GUSk3wpLZE2ElK8it6sOBQeIU0VZASNH sha256 wRAHCaKdoJ+wGRe95gu0Yh0jcTEeXTAPahEhQ8sRiic=, function last version 19 | CLOSED 20260915T195510Z |
| L3 | verify | plan targeted to the function and the distribution | 0 add 2 change 0 destroy |  | OPEN |
| L4 | activation | safe-apply | apply summary + published version |  | OPEN |
| L5 | verify | 0-diff re-plan and LIVE association version N of N | No changes + association read |  | OPEN |
| L6 | verify | live tier arms on both URLs and the control | statuses per class |  | OPEN |
| L7 | git | record-terraform-deploy | commit hash |  | OPEN |

## Log

- 20260915T194613Z OPENED by 0.9.0_WK_POSN_AGGFIX~2 with 7 leg(s)
- 20260915T195049Z LEG L1 closed: commit 240fe36222 on branch wk-posn_aggfix-1-2 carries infra/aws/lambda-edge/auth-validator-edge/index.mjs (M) + aggrega
- 20260915T195510Z LEG L2 closed: s3://opal-313476888478-lambda-artifacts/portal-auth/auth-validator-edge.zip VersionId zNqzzAOFvq1LnTji4BV2_OymHRfr.bXI c
