# Deploy Completion Record
**Date opened:** 2026-10-02T11:20:16.903104+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 62 AMGT-al-1 act (B) (URGENT, FREEZE 12:30Z): track B code-only redeploy of opal-amgt-scoped-api at a2ff06d1a1, carrying al-2 -- the timeline day route's silver read runs under an 18 s deadline from handler start and on the deadline serves mentions with headline null plus one plain headline_reason as a 200, instead of a sandbox kill. Under the never-widen pair COO a12291728f / CTO 57dfa6bd84 (ruling 5a @e041af6102). Base CodeSha256 E+FAZF0f63S5LxRWs4l3mCfOZgKc3erezTkjxCoVcBY=, rollback artifact VersionId YSqlUTOWHwV6H7LePjd1pr9DKomiDo5U, MemorySize stays 10240 (act (A)'s value, untouched)
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | build + upload ONE artifact to s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip from a worktree at a2ff06d1a1 | CONTENT-DIFF graded independently of the build script's summary line: EXACTLY CHANGED 1 with the set equal to [lib/research/api/scoped_amgt.py], ADDED 0, REMOVED 0, set equality both ways, packaged denominator printed, fabricated-path control; the base CodeSha256 re-read LIVE immediately before the build as a mechanical abort; prior and new S3 VersionId read back from S3 |  | OPEN |
| L2 | activation | ONE code-only safe-apply on infra/aws/terraform/harvest, applied from the SAVED plan | the plan read BEFORE applying shows ONE in-place update with ONLY source_code_hash, s3_object_version and last_modified moving; memory_size MUST NOT appear as a changed attribute (it stays 10240 from act (A)); any IAM, route, gateway, alias or destroy change is a STOP; prior and new CodeSha256 plus MemorySize read back from LIVE state, not from the apply rc |  | OPEN |
| L3 | verify | timeline_b.py --what post --pre round62/AL2_CONTROLS_PRE.json (CTO condition 2) | 3 of 3 concurrent cold BA day invokes answer 200, and BOTH control days (BA 2026-09-30 and 2026-10-01) are byte-equal to the pre at body_sha256 6c25fff80da9be93.. and 69ecb7a884a83585.. -- a non-200 on any cold run or a moved control byte is the ROLLBACK trigger; HTTP 200 alone is never the grade |  | OPEN |
| L4 | verify | pytest lib/research/api/tests/test_timeline_silver_deadline.py -- the planted slow read (CTO condition 2) | 3 passed: the deadline branch is exercised against a planted slow silver read and returns 200 with mentions and the reason rather than a timeout, which is the only arm that proves the NEW branch works rather than merely that the old path still does |  | OPEN |

## Log

- 20261002T112016Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
