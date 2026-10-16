# Deploy Completion Record
**Date opened:** 2026-10-16T12:19:55.965695+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-298: APPLY the signed 49 Financial series-publish pair (packet sha256 29b7df738efc, COO half @023604d076, CTO half @582155d0b7); APPLIER 0.7.0_AE_CloudOps~DB2: build and upload a NEW VERSION of the irpt-49f-reporting-publish-lambda bundle (publisher 0.4.0), plan EXACTLY 0 add / 1 change / 0 destroy (the function by CODE attributes only), ONE safe-apply NOT BEFORE 13:00Z and never 12:05Z to 13:00Z, the absent-days check, a one-shard DRY RUN, a ONE-ACCOUNT republish and the FULL republish of the 6949 series, all under irpt/49financial/platinum/reporting/; schedule ENABLED and untouched; NO delete; ledger stays OPEN
**Authored by:** 0.7.0_AE_CloudOps~DB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | tree commit and the sha256 of each pinned file; packet blob, sha256 and both halves; marker scan over every live worktree; live reads equal to the packet section 3 | the printed reads |  | OPEN |
| L2 | s3-prefix | BUILD_ONLY zip equal to the packet build line, import smoke rc 0, then a NEW VERSION of the artifact key; built equals landed | zip sha256, smoke rc, VersionId |  | OPEN |
| L3 | tf-lambda | fmt -check, init, validate, saved plan EXACTLY 0 add / 1 change / 0 destroy on the function by code attributes only, naming gate 0 REFUSE, ONE safe-apply at or after 13:00Z, replan No changes, read-backs, stamp | plan line, apply line, replan line, read-backs |  | OPEN |
| L4 | verify | the absent-days check, then Act 3 ONE synchronous one-shard dry run; writes nothing; memory at most 819 MB, duration at most 240000 ms; no refusal | the absent-days set and the event result, the LIST unchanged |  | OPEN |
| L5 | verify | Act 4 ONE-ACCOUNT republish at the same two keys; ten checks true; prior versions kept | the event result, the LIST unchanged, the checks |  | OPEN |
| L6 | verify | Act 5 the FULL republish (7 shard invocations) and the receipt; series and manifests equal published, other unchanged; ten sampled accounts pass; pair, calendar and version counts equal published | the shard REPORT lines, the LIST counts, the counts |  | OPEN |

## Log

- 20261016T121955Z OPENED by 0.7.0_AE_CloudOps~DB2 with 6 leg(s)
