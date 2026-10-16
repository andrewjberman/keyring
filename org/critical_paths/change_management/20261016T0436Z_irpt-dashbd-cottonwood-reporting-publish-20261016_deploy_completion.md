# Deploy Completion Record
**Date opened:** 2026-10-16T04:36:35.515314+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-283: APPLY the signed Cottonwood series-publish pair (packet sha256 0c9b495ce2f7, COO half @6c8e76f0e0, CTO half @474f33174c); APPLIER 0.7.0_AE_CloudOps~DB2 (CTO condition 2): build and upload the bundle of irpt-cot-reporting-publish-lambda (key first object), plan EXACTLY 4 add / 0 change / 0 destroy on the four addresses of reporting-publish-iso, ONE safe-apply, then a DRY-RUN event, a ONE-ACCOUNT canary and the FULL upload under irpt/cottonwood/platinum/reporting/; NO schedule, NO enable, NO delete; ledger stays OPEN
**Authored by:** 0.7.0_AE_CloudOps~DB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | tree commit and the sha256 of each file in the packet section 2; packet blob, sha256 and both halves; marker scan over every live worktree; live absence reads; the layer read | the printed reads |  | OPEN |
| L2 | s3-prefix | BUILD_ONLY zip equal to the packet build line, import smoke rc 0, then the key first object version; built equals landed | zip sha256, smoke rc, VersionId |  | OPEN |
| L3 | tf-lambda | fmt -check, init, validate, saved plan EXACTLY 4/0/0 on the four addresses, naming gate 0 REFUSE, ONE safe-apply, replan No changes, read-backs, stamp | plan line, apply line, replan line, read-backs |  | OPEN |
| L4 | verify | Act 2 ONE synchronous dry-run event payload empty; writes nothing; memory at most 717 MB; unreported days equal the report-build list | the event result and the LIST of 0 objects |  | OPEN |
| L5 | verify | Act 3 ONE-ACCOUNT upload; two objects; the seven checks all true | the event result, the LIST of 2, the checks |  | OPEN |
| L6 | verify | Act 4 the FULL upload; objects equal 2 x published; ten sampled accounts pass the Act 3 checks | the event result, the LIST count, the sample checks |  | OPEN |

## Log

- 20261016T043635Z OPENED by 0.7.0_AE_CloudOps~DB2 with 6 leg(s)
