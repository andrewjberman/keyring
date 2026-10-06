# Deploy Completion Record
**Date opened:** 2026-10-06T11:06:58.799273+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 75 AMGT-ay-5: code at EXACTLY ab28d0ba01 carrying ay-1..ay-4 (CHANGED 3 + ADDED 3), the snapshot-key GRANT, ONE name()-named SCHEDULE (cron 30 12 ? * MON-FRI *, UTC) invoking the existing function, and the FIRST FIRE writing the snapshot. CTO conditions 1-7 @452acb4e68, COO half @265f85f8fe, carrying ROUND_ANALYSIS.round74 ADDENDUM 1 @82afef1fd8 option (b). Build is EXACTLY the pin, never 'at or after' -- the issuer wrote that in because round 74's ax-5 stopped on a file another project changed after the pin. Grant and schedule legs are graded on an UNTARGETED plan, which is round 74's row Z-S357 adopted as practice. No S3 delete in any branch; the snapshot rollback is a re-put of a computed view or the route's own fallback.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | gating reads: base live, worktree union, the snapshot key's absence, the grant's base arm, the schedule's name() output, and comp-schedule | CodeSha256 0MZWPl7nGZzFI53w+vsKdS7hQpcxu4Mrd5wEMWWZQpA= and MemorySize 1769 unchanged; per-tree denominator with 0 unresolved; snapshot key 404 with a positive control on its prefix tree; PutObject and GetObject on the snapshot key and PutObject on a sibling key all implicitDeny, each one resource ARN per call, with a separately-invoked positive control reading allowed; name() output recorded and grade() CONFORMANT; comp-schedule run to completion with GATES ARMED 0 |  | OPEN |
| L1 | verify | CODE LEG build at EXACTLY ab28d0ba01 from a detached worktree, CONTENT-DIFF vs deployed 0MZWPl7n | exactly CHANGED lib/research/api/scoped_amgt.py + lib/research/api/monthly_chatter.py + lib/research/print/render_pack.py, ADDED lib/research/api/names_read.py + lib/research/api/segment_labels.py + lib/research/freshness/snapshot.py, REMOVED none; size under 262144000 B; the pin is resolved by CONTENT and the build commit is the pin itself, not a descendant |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + ContentLength + content-sha256, re-read by head-object |  | OPEN |
| L3 | activation | opal-amgt-scoped-api code-only safe-apply, then leadpanel_cold_warm.py --label after and the cold invokes' AMGT_PHASE lines | live CodeSha256 = the new build with MemorySize 1769; leadpanel after output and the phase table captured into deliverables |  | OPEN |
| L4 | activation | GRANT + SCHEDULE legs, graded on an UNTARGETED plan per CTO condition 2 | the untargeted plan shows exactly the one added policy statement on the snapshot key, the schedule, its scheduler role and the code update, and NOTHING else non-no-op; the schedule's name is name() output amgt-global-freshness-snapshot-daily (grade CONFORMANT), cron(30 12 ? * MON-FRI *) UTC state ENABLED, input exactly {"amgt_scheduled_action": "refresh_freshness_snapshot"}, target the EXISTING function, its role holding lambda:InvokeFunction on that one function only; AFTER: PutObject and GetObject on the snapshot key read allowed while PutObject on a sibling key under amgt/harvest/state/ STAYS implicitDeny |  | OPEN |
| L5 | verify | FIRST FIRE: one direct invoke with the schedule's own event, writing the first snapshot | the snapshot object exists with its stamp and ETag read back by head-object; the stamp moves; an HTTP GET never writes (the plant test); no S3 delete in any branch |  | OPEN |
| L6 | verify | AC1 c57/c58/c59(C1-C3)/c61 deployed, AC2 the r71-r74 regression set including the c55 pin | each criterion SERVED YES with exit=0; c59 C1 rows EQUAL to the computed view and C2/C3 a cold or post-hold GET under about 2 s; r74 c53/c55/c56, r73 c48-c50 and r71 c38 unchanged |  | OPEN |

## Log

- 20261006T110658Z OPENED by 0.7.0_AE_CloudOps~A with 7 leg(s)
