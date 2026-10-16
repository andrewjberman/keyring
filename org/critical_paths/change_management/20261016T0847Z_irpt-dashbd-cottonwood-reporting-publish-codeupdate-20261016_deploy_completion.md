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
| L1 | git | tree commit and the sha256 of each pinned file; packet blob, sha256 and both halves; marker scan over every live worktree; live reads equal to the packet section 3 | the printed reads | applier 0.7.0_AE_CloudOps~DB2; tree HEAD 0080ca8f04 on wk-IRPT_DASHBD-DB2-b291 cut from box/dell2 (carries re-pin edf7999ebe ancestor true, order @860feb475b, COO half @d20bc88608, CTO half @ed74d5520d); packet git blob c64ed6f7ea594e7cc0a70cfe6f0a7b4dd458d083 equals the CTO half's blob, sha256 77f0af99d2bb28cd49344df6cf63494e8185f04d6cc8fff65bf9c4f1f2d501b0 equal; COO half SIGNED (REVISION 1) and CTO half SIGNED, both on that sha256; the eight pins re-read, 8 of 8 equal (iam.tf 0008681b0b01, lambda.tf 4b06e81c4119, locals.tf fb2e7936b6d0, main.tf 5b49dd311dbf, schedule.tf fc5867c7af69, handler.py ed630f8859de, publisher.py 3d32ffb84ea0, series contract 42fc230550fe); marker scan over 74 live worktrees (git grep at HEAD of .open_deploys for the root, the function name and the platinum reporting prefix), positive control on a known marker token hit 41 worktrees: the only hits are 4 ANLREQ worker worktrees (wk-irpt-anlreq-230 to 233) holding a STALE COPY of the first pair's sentinel irpt-dashbd-cottonwood-reporting-publish-20261016, a ledger CLOSED on trunk (change_management entry closed 20261016T071926Z @6650d1aac6, no sentinel at box/dell2 HEAD, the packet section 3 states it closed); named, never closed; no OPEN entry on this surface (reading of gate (c): a copy of a closed entry is not an open change); live: function present CodeSha256 HDgIzQoXMyUNBxeyqgLXcplD1c01QwVsASRoMJbd4hk= 1024 MB timeout 900 one layer no reserved concurrency no environment; artifact key one version 9s6sk2dVtf6Ygi2JOGUxtwuiSNXCfKDa (140472 bytes); no schedule named irpt-cot-reporting-publish*; scheduler role and policy absent (NoSuchEntity); target prefix 1878 objects (the CLI printed pages 1000 and 878); both buckets versioning Enabled | CLOSED 20261016T084819Z |
| L2 | s3-prefix | BUILD_ONLY zip equal to the packet build line, import smoke rc 0, then a NEW VERSION of the artifact key; built equals landed | zip sha256, smoke rc, VersionId | BUILD_ONLY sha256 GagDGBNGmPsmYaJR1B7qG/TvaPdQU3LiVAh6c+wt6jo= equals the packet's section 2 value (hex 19a803181346..., 13 members: handler.py and 12 staged); import smoke rc 0 from a different working directory with a discriminating negative control (a missing module rc 1); real upload landed a NEW version 4wX9zhqX6x4x73i1vX1ADsXfv1LyDzRA of the existing key (142653 bytes, write VERIFIED, sha256 metadata match), the first pair's version 9s6sk2dVtf6Ygi2JOGUxtwuiSNXCfKDa kept (2 versions, the new one latest); landed bytes sha256 equal the built zip; source map changed in the entry's artifact_sha256 field only | CLOSED 20261016T085036Z |
| L3 | tf-lambda | fmt -check, init, validate, saved plan EXACTLY 3 add / 1 change / 0 destroy by address with the function change by code attributes only, naming gate 0 REFUSE, ONE safe-apply, replan No changes, read-backs, stamp | plan line, apply line, replan line, read-backs |  | OPEN |
| L4 | verify | Act 3 ONE synchronous dry-run event payload empty; writes nothing; memory at most 717 MB; unreported days equal the report-build list | the event result and the LIST unchanged |  | OPEN |
| L5 | verify | Act 4 ONE-ACCOUNT republish at the same two keys; ten checks true; prior versions kept | the event result, the LIST unchanged, the checks |  | OPEN |
| L6 | verify | Act 5 the FULL republish and the Act 6 S104 read; objects equal 2 x published; ten sampled accounts pass; claim and calendar counts equal published | the event result, the LIST count, the counts |  | OPEN |

## Log

- 20261016T084742Z OPENED by 0.7.0_AE_CloudOps~DB2 with 6 leg(s)
- 20261016T084819Z LEG L1 closed: applier 0.7.0_AE_CloudOps~DB2; tree HEAD 0080ca8f04 on wk-IRPT_DASHBD-DB2-b291 cut from box/dell2 (carries re-pin edf799
- 20261016T085036Z LEG L2 closed: BUILD_ONLY sha256 GagDGBNGmPsmYaJR1B7qG/TvaPdQU3LiVAh6c+wt6jo= equals the packet's section 2 value (hex 19a803181346...,
