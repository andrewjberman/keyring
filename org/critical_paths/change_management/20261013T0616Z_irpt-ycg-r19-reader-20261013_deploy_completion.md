# Deploy Completion Record
**Date opened:** 2026-10-13T06:16:39.414430+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R19b: irpt-ycharts-generate reader release (uploads.py, template_reader.py) to CodeSha256 bNPCG2Oe..; live NeAB50CN.. / S3 objver _1MrCfPkp..; resident V1 closed green (COO~Y2 msg 6821); pair COO 2140b935 + CTO 6facbbb2d3
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | live CodeSha256 NeAB50CNXWvM5Y6nsba220QmsEiASbVbXcZVRYe4MUM= and S3 latest VersionId _1MrCfPkpVkl7XDAC3NsbLhvIDvHBusc before any write; open-entry denominator over every live worktree | the two reads and the denominator printed |  | OPEN |
| L2 | verify | BEFORE: refusal-path sample status and body sha256, or ABSENT with reason | status and sha256, or ABSENT |  | OPEN |
| L3 | s3-prefix | build at 5d8b0390ed plus RELEASE_MAP_PATCH_R2.diff: CodeSha256 bNPCG2Oe1oQM/ztjggmrdDbdl83CAmUEcPnBFxlj2Rk=, 104 members, differs from live in exactly template_reader.py and uploads.py; then upload, VersionId, read-back sha256 | printed CodeSha256, member diff, new VersionId, read-back equality |  | OPEN |
| L4 | verify | scoped plan -target module.irpt_ycharts_generate.aws_lambda_function.this: 0 add 1 change 0 destroy, attributes last_modified s3_object_version source_code_hash only | plan summary line and attribute list |  | OPEN |
| L5 | activation | .tools/safe-apply.sh on the saved plan | Apply complete 0 added 1 changed 0 destroyed |  | OPEN |
| L6 | verify | AFTER: CodeSha256 bNPCG2Oe.., 104 members with exactly two differing, refusal sample equals BEFORE, env keys and role equal BEFORE; door reads D1-D4 and C1 ABSENT | live CodeSha256 line and diffs |  | OPEN |
| L7 | verify | rollback armed and unused, or ROLLED_BACK; ledger closed | state |  | OPEN |
| L8 | git | RELEASE_MAP_PATCH_R2.diff applied to lambda-source-map.json plus artifact_* and last_deployed_* record; commit | commit hash |  | OPEN |

## Log

- 20261013T061639Z OPENED by 0.7.0_AE_CloudOps~IB2 with 8 leg(s)
