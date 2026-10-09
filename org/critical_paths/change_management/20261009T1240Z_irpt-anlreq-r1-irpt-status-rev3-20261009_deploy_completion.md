# Deploy Completion Record
**Date opened:** 2026-10-09T12:40:13.559987+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ APPLY-Y1 REVISION 3 (AMENDMENT 2): irpt-status registry fix for REQ-5e4149d2, PINNED to 5240156380, built t6OJTCcm, over live BjUZjt2oq8GPJSibq4vD/0m8/LfdN0GF3THwCaBMVOM= which is also the ROLLBACK. The per-member diff is exactly infra/logic/registry/reporting_policies.json, 1 of 49 -- the CTO stop rule (msg 3262). Supersedes rev2 (CLOSED, its deploy complete and its reads 3-5 deferred to the laptop per row IRPT_ANLREQ-D2-S8)
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 0 at the new pin, all limbs re-measured myself rather than taken from the issuer report | 5240156380 is an ancestor of origin/box/dell2 with a DISCRIMINATING control; the per-member diff is exactly reporting_policies.json; the _authz unguarded-route census passes at the pin; live equals the named rollback BjUZjt2o | STEP 0 CLEARS, every limb measured by this seat rather than taken from the issuer report. (a) merge-base --is-ancestor 5240156380 origin/box/dell2 returns rc 0, origin tip 47dd74455f, and the control DISCRIMINATES: origin/box/dell1 is NOT an ancestor. (b) THE CTO STOP RULE (msg 3262) IS MET: release-census at the pin reads built_members=49 live_members=49 changed_members=1, and the one changed member is exactly infra/logic/registry/reporting_policies.json (built 1479826b5764, live 2bd3520dd386). I ran this BEFORE the pin reached origin, because it is a local property of the pin and would have killed revision 3 before anyone waited on a push. (c) the _authz unguarded-route census at the pin reads 9 passed. (d) live irpt-status CodeSha256 is BjUZjt2oq8GPJSibq4vD/0m8/LfdN0GF3THwCaBMVOM=, exactly the rollback AMENDMENT 2 names -- so the rollback target is the state actually running, not an assumed one. Worktree /c/dev/anl-r1-pin3, detached at the pin. | CLOSED 20261009T124051Z |
| L2 | s3-prefix | build and upload irpt-status from the new pin worktree /c/dev/anl-r1-pin3 | the uploaded sha256 is t6OJTCcm... or STOP, and symbol_closure on the object downloaded back BY VERSION reads missing=0 or STOP | UPLOADED, both stop conditions met ON THE UPLOADED BYTES. build-and-upload.sh run from the detached pin worktree /c/dev/anl-r1-pin3 at 5240156380 (0 uncommitted). Build printed t6OJTCcmOnWGVl8iglcvfGoYb3PbPJqJYqsSgJBpGdI=, the AMENDMENT 2 declared value. Read back INDEPENDENTLY: new object version mkD1gV_CByQfMVGbNzf6E7EKsUUlKdXb, 356127 bytes, and the sha256 RECOMPUTED FROM THE RETURNED BYTES is t6OJTCcm..., EQUAL to both the declared value and the object own content-sha256 metadata -- three agreeing sources rather than one. Rollback source retained: version 7loKTWdSAUPR6Rqk.XhqBufmwP9VHXfy at BjUZjt2o, which is the live state. SECOND CONDITION, the CTO symbol closure on those same downloaded bytes rather than a local rebuild: modules=37 pairs=115 missing=0 optional_fallbacks=0, PASS -- it grades the bytes the Lambda will load. | CLOSED 20261009T124212Z |
| L3 | activation | ONE ops safe-apply from the repo root with -chdir | code-only: s3_object_version and source_code_hash and the computed last_modified, nothing else -- any other line is a STOP; no api change this revision, since the route already exists from rev2 |  | OPEN |
| L4 | verify | after-reads 1, 2, 6 and 7 | live == t6OJTCcm and the re-plan 0; the /original route still exists EXACTLY ONCE; read 6 = REQ-5e4149d2 served, which 2.0.0_SA_COO~G2 is copied on for the YCDGEN FWD-1 grade |  | OPEN |
| irpt-status | tf-lambda | module.irpt_status.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T124013Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 5 leg(s)
- 20261009T124051Z LEG L1 closed: STEP 0 CLEARS, every limb measured by this seat rather than taken from the issuer report. (a) merge-base --is-ancestor 5
- 20261009T124212Z LEG L2 closed: UPLOADED, both stop conditions met ON THE UPLOADED BYTES. build-and-upload.sh run from the detached pin worktree /c/dev/
