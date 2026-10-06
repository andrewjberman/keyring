# Deploy Completion Record
**Date opened:** 2026-10-06T19:46:51.249630+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 76 AMGT-az-5: the code redeploy carrying az-2 (top_band, input_provenance) and az-4 (the cold read cut) on opal-amgt-scoped-api. ONE artifact built from a DETACHED worktree at EXACTLY de48559928, never at-or-after; CONTENT-DIFF vs deployed D29LJCXh is CHANGED 7 + ADDED 1 and any other file is a STOP; ONE code-only safe-apply graded UNTARGETED (memory_size stays 1769, no IAM, no schedule, no grant); then ONE snapshot event {amgt_scheduled_action: refresh_freshness_snapshot} so the /freshness snapshot is written by the new code. COO half @6c06cabc3f, CTO half @9c5a2a4b61 conditions 1-5. Pins: r74 c55 and r75 c59 run on this redeploy. Snapshot rollback is a copy-object of the prior VersionId, NEVER an S3 delete; code rollback is the prior artifact through the module via one code-only safe-apply.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | base re-read live + .open_deploys union over every live worktree | CodeSha256 D29LJCXhOStZ51JD4TTt2Jk0QUVDUbXDouXRTUS1ULI= and MemorySize 1769 unchanged at start; per-tree denominator printed over all live worktrees with every RESAPP sentinel shown world-done by completion entry + ancestry with a discriminating positive control | Live base read 2026-10-06T19:4xZ by lambda get-function-configuration: CodeSha256 D29LJCXhOStZ51JD4TTt2Jk0QUVDUbXDouXRTUS1ULI=, MemorySize 1769, python3.11, LastModified 2026-10-06T11:28:32Z, CodeSize 41960001 -- equals both halves' stated base. .open_deploys union swept over 65 live worktrees (git worktree list --porcelain, then git -C <wt> ls-tree -r HEAD): 61 DISTINCT entries. Shared-tree HEAD carries 17 and NONE is amgt-resapp; the on-disk ls -a read agrees. The three RESAPP sentinels in the union are world-done: amgt-resapp-r56-af6-price-cutover.json (og-rb9..16, og-rel9..16, 14 stale trees), amgt-resapp-r73-aw7.json (wk-dsgn-amgtv1-104 @8b14110481), amgt-resapp-r74-ax5.json (wk-oplgtw-15-r20 @a6e1127031) -- each absent on the shared tree at HEAD (probe discriminating: positive control leadpanel-price-producer-schedule.json reads 1 on the same probe) and each carrying a shared-tree completion entry (20261001T0626Z af6, 20261006T0337Z aw7, 20261006T0714Z ax5). Ancestry: the deployed D29LJCXh was built at ab28d0ba01, merge-base --is-ancestor ab28d0ba01 CLOUD passes while the reverse fails (control discriminates), and ab28d0ba01 is an ancestor of the build pin de48559928, so the pin is strictly LATER than the deployed artifact. 0 unresolved. | CLOSED 20261006T194722Z |
| L1 | verify | CODE LEG build from a DETACHED worktree at EXACTLY de48559928, CONTENT-DIFF vs deployed D29LJCXh | exactly CHANGED lib/research/api/scoped_amgt.py + lib/research/api/monthly_chatter.py + lib/research/api/names_read.py + lib/research/coverage/pool_reader.py + lib/trading_calendar.py + infra/logic/registry/reporting_policies.json + infra/logic/registry/systems.json, ADDED lib/research/api/top_band.py, REMOVED none; files 372 IDENTICAL 364 CHANGED 7 ADDED 1; size under the 262144000 ceiling; any file outside that table is a STOP |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + ContentLength re-read by head-object |  | OPEN |
| L3 | activation | opal-amgt-scoped-api code-only safe-apply on infra/aws/terraform/harvest/, plan graded UNTARGETED, then leadpanel_cold_warm.py --label after | full untargeted plan show -json: exactly 1 update (the function code), 0 destroy, 0 IAM, 0 schedule, 0 grant in THIS plan; memory_size 1769; live CodeSha256 differs from D29LJCXh AND equals the artifact built at de48559928 (an unchanged hash is a 0-diff deploy and a STOP); leadpanel after output and the cold AMGT_PHASE table captured |  | OPEN |
| L4 | activation | ONE direct invoke with exactly {amgt_scheduled_action: refresh_freshness_snapshot} so the snapshot is written by the new code | exactly one invoke; the snapshot stamp read after it; rollback for the object is a copy-object of the prior VersionId, never a delete |  | OPEN |
| L5 | verify | AC1 (r76 c62/c63 + r75 c59) and AC2 (r75 c57/c58/c61, r74 c53/c55/c56, r71 c38) on the DEPLOYED function | every criterion SERVED YES with exit=0; c62/c63 flip FAIL to YES; c59 YES with rows EQUAL after the event; no regression on the AC2 set; any NO is the rollback trigger |  | OPEN |

## Log

- 20261006T194651Z OPENED by 0.7.0_AE_CloudOps~A with 6 leg(s)
- 20261006T194722Z LEG L0 closed: Live base read 2026-10-06T19:4xZ by lambda get-function-configuration: CodeSha256 D29LJCXhOStZ51JD4TTt2Jk0QUVDUbXDouXRTU
