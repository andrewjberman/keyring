# Deploy Completion Record
**Date opened:** 2026-09-12T08:44:00.248094+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rt-6: the absence oracle -- redeploy irpt-directory-refresh with list-established absence and the conditioned ListBucket grant, then re-drive the production fire
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-directory-refresh.zip | VersionId + content-sha256 equal to the rebuilt zip |  | OPEN |
| L2 | activation | terraform apply: the conditioned ListBucket statement + the new function code | safe-apply rc=0, no destroy line |  | OPEN |
| L3 | verify | served CodeSha256 == built, post-apply plan No changes, and simulate-principal-policy shows ListBucket allowed under the prefix condition | three-way hash + plan + simulation |  | OPEN |
| L4 | activation | re-drive the production fire for 2026-09-11 across three firms | the three manifests present with build_dispatch SSM and a real command id each |  | OPEN |

## Log

- 20260912T084400Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 4 leg(s)
