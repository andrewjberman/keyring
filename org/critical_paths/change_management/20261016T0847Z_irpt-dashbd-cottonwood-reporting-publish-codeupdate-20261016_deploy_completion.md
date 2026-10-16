# Deploy Completion Record
**Date opened:** 2026-10-16T08:47:42.481954+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-291: APPLY the second signed Cottonwood series-publish pair (packet sha256 77f0af99d2bb, COO half @d20bc88608, CTO half @ed74d5520d); APPLIER 0.7.0_AE_CloudOps~DB2: build and upload a NEW VERSION of the irpt-cot-reporting-publish-lambda bundle (writer 0.3.0), plan EXACTLY 3 add / 1 change / 0 destroy on reporting-publish-iso (scheduler role, scheduler policy, DISABLED daily schedule; function CODE attributes only), ONE safe-apply, then a DRY-RUN event, a ONE-ACCOUNT republish, the FULL republish of the 939 series and the S104 read, all under irpt/cottonwood/platinum/reporting/; NO enable, NO delete; ledger stays OPEN
**Authored by:** 0.7.0_AE_CloudOps~DB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | tree commit and the sha256 of each pinned file; packet blob, sha256 and both halves; marker scan over every live worktree; live reads equal to the packet section 3 | the printed reads |  | OPEN |
| L2 | s3-prefix | BUILD_ONLY zip equal to the packet build line, import smoke rc 0, then a NEW VERSION of the artifact key; built equals landed | zip sha256, smoke rc, VersionId |  | OPEN |
| L3 | tf-lambda | fmt -check, init, validate, saved plan EXACTLY 3 add / 1 change / 0 destroy by address with the function change by code attributes only, naming gate 0 REFUSE, ONE safe-apply, replan No changes, read-backs, stamp | plan line, apply line, replan line, read-backs |  | OPEN |
| L4 | verify | Act 3 ONE synchronous dry-run event payload empty; writes nothing; memory at most 717 MB; unreported days equal the report-build list | the event result and the LIST unchanged |  | OPEN |
| L5 | verify | Act 4 ONE-ACCOUNT republish at the same two keys; ten checks true; prior versions kept | the event result, the LIST unchanged, the checks |  | OPEN |
| L6 | verify | Act 5 the FULL republish and the Act 6 S104 read; objects equal 2 x published; ten sampled accounts pass; claim and calendar counts equal published | the event result, the LIST count, the counts |  | OPEN |

## Log

- 20261016T084742Z OPENED by 0.7.0_AE_CloudOps~DB2 with 6 leg(s)
