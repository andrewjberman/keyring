# MDLP_MONPUB: W8 witness COMPLETE (all 3 legs PASS) + W5 exercised on the LIVE deployed Lambda

**archetype:** VERIFY

**Serial:** `3.0.0_SA_CVO`. Window: 2026-08-03T1745-1755Z.

## W8 -- force_publish rollback plumbing: all three legs witnessed PASS

Per the 172718Z ruling (CTO-ratified), executed by DS on DT's scratch instance
`opal-data-refresh-api-qa-scratch` (identical artifact sha, BUCKET=scratch):

1. **End-to-end handle_rollback (the required entry point):** the re-processing fallback ran
   through the REAL rollback handler and LANDED the stamped manifest on scratch `uploads/` --
   read by me: `force_publish: true` + `rollback_execution_id: exec-fdf49e30710f` INSIDE the
   manifest body, `manifest.json` written LAST (17:44:30Z, after both pkls at :29 -- the
   trigger-ordering contract).
2. **Yang manifest-arm bypass:** requestId ed35ec26...: the logged EVENT shows force_publish
   ONLY inside `event.manifest` -- no top-level key -- so the `:146` manifest arm is what fired
   (the discriminating condition; leg C had covered the `:145` top-level arm). FORCE_PUBLISH
   warning verbatim WITH the rollback id riding in the log per the TO. Scratch flipped
   28B-seed -> 19,221B payload.
3. **Negative control:** requestId 030ed212...: `PublishGuardError` raised in-window at the
   POST-W8 line numbers (`:361/:659` vs pre-W8 `:354/:649` -- incidental proof the NEW artifact
   ran); scratch re-seed byte-unchanged (28B, `2ad52d9f...`). The plumbing did not widen the
   default posture.

**Live serve untouched throughout** (all three production ETags byte-identical to the 16:23:50Z
set, verified by me at 17:52Z). **Disclosed event-side injection accepted:** DS added a `bucket`
field into `event.manifest` for scratch-scoping -- correctly disclosed, and their pre-fire catch
(the default would have pointed a stamped invoke at the LIVE bucket) is exactly the check-before-
mutate discipline; in orchestrated mode the same default correctly targets production.
**Traversal status unchanged:** middle segment SOURCE-GROUNDED-NOT-EXERCISED (live ASL verified),
upgrades at the first genuine rollback.

**Cleanup GO to DS, widened:** delete BOTH fixture-era DynamoDB records -- `exec-w8scratch` AND
`exec-fdf49e30710f` (the rollback-created record is equally a fixture in the real table; my live
W5 exercise surfaced both at the top of the production history list, where they will sit visibly
until cleaned).

## W5 -- rollback picker time-sort: DEPLOYED AND EXERCISED on the live Lambda

- Deployed zip read: full-partition pagination -> `sort(key=startedAt, reverse=True)` -> limit,
  on EXECUTION and SSCN lists plus the combined sort; the W5 comment block records the defect.
- **Exercised live** (direct invoke, history event, limit 25): 25 items returned STRICTLY
  time-ordered descending, and **`exec-5a4149176fb6` (the 07-27 execution that was structurally
  invisible on 07-31) is PRESENT** -- the differential acceptance satisfied on the deployed
  artifact against the production table. The picker now shows the true recency order:
  today's runs, then 07-31, 07-28, 07-23, 07-22...

## Rollback-capability answer (Andrew's question, grounded)

Selection fixed (W5, exercised); restore path guarded + rollback-capable (W2 guard witnessed
complete; W8 plumbing witnessed complete -- the emergency rollback can now carry force_publish
through the fallback chain); edge invalidation on rollback deployed since 08-01 and coverage-
verified; client-cache invalidation (W6) = the remaining open piece, PROD promote in-flight at DT.
