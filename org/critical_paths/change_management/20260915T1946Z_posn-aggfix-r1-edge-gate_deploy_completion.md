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
| L1 | git | branch carries index.mjs + aggregate_gate.mjs | commit hash |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts portal-auth/auth-validator-edge.zip | sha256 + VersionId |  | OPEN |
| L3 | verify | plan targeted to the function and the distribution | 0 add 2 change 0 destroy |  | OPEN |
| L4 | activation | safe-apply | apply summary + published version |  | OPEN |
| L5 | verify | 0-diff re-plan and LIVE association version N of N | No changes + association read |  | OPEN |
| L6 | verify | live tier arms on both URLs and the control | statuses per class |  | OPEN |
| L7 | git | record-terraform-deploy | commit hash |  | OPEN |

## Log

- 20260915T194613Z OPENED by 0.9.0_WK_POSN_AGGFIX~2 with 7 leg(s)
