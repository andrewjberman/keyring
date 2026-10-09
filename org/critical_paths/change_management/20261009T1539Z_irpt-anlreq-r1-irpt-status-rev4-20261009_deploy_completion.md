# Deploy Completion Record
**Date opened:** 2026-10-09T15:39:05.728267+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ APPLY-Y1 REVISION 4 (AMENDMENT 4 @3ec9aa43c8): irpt-status third apply -- the research revision now derives from the PACKAGED registry, fail closed. PINNED to 287b105600, built VC/r14kaXm6FqaZOOFm3fT+8qngsyGI5Yr7U+DgYx64=, over live t6OJTCcmOnWGVl8iglcvfGoYb3PbPJqJYqsSgJBpGdI= which is also the ROLLBACK. R0 MET: the uploaded-zip diff against the LIVE function artifact is EXACTLY status_installed.py -- 49 members both sides, 1 changed, 0 added, 0 removed. Built in a DETACHED worktree at the pin because a shared-root build is a STOP. Both halves signed (CTO msg 3569). Only an R2 failure rolls back
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | the uploaded-zip member diff against the live function artifact | EXACTLY status_installed.py changed, nothing added or removed, or STOP | R0 MET, measured member-by-member rather than by size. The LIVE side was taken from the FUNCTION own code location via get_function, NOT from the S3 key -- the upload had just overwritten that key, so reading the key would have compared the new zip with itself and passed vacuously. live CodeSha256 t6OJTCcmOnWGVl8iglcvfGoYb3PbPJqJYqsSgJBpGdI= equals the rollback the amendment names, so the pre-apply state is the declared one. Uploaded version bkc32xOeK.GxnczvzmSsIxtHDxzpnewu, sha256 VC/r14kaXm6FqaZOOFm3fT+8qngsyGI5Yr7U+DgYx64= equal to the declared build. DIFF: 49 members on each side, changed 1, added 0, removed 0, and the single changed member is status_installed.py. Member-by-member matters because two zips can differ in size without a member changing and a member can change without the size moving. Record: deliverables/irpt_anlreq_r1/Y1_REV4_R0_zip_diff.json. | CLOSED 20261009T154002Z |
| L1 | s3-prefix | build and upload from the detached worktree /c/dev/anl-r1-pin4 at 287b105600 | uploaded sha256 equals VC/r14ka or STOP; a shared-root build is itself a STOP | UPLOADED from the DETACHED worktree /c/dev/anl-r1-pin4 at 287b105600, which the amendment requires -- a shared-root build is itself a STOP, and the shared root also carries other seats work. The worktree read 0 uncommitted files overall and 0 under infra/aws/lambda, which is the build script own gate. Build printed VC/r14kaXm6FqaZOOFm3fT+8qngsyGI5Yr7U+DgYx64=, 356569 bytes, and the object write was VERIFIED by the script against its sha256 metadata; I then re-read it independently by version id and recomputed the sha256 from the returned bytes, which agrees. Three sources therefore agree rather than one: the build line, the object metadata, and the bytes. | CLOSED 20261009T154003Z |
| L2 | activation | ONE ops safe-apply from the repo root with -chdir | code-only: s3_object_version, source_code_hash and the computed last_modified, nothing else; any other line is a STOP |  | OPEN |
| R2 | verify | the after-reads | live equals VC/r14ka and the re-plan 0; the /original route still exactly once; the research revision derives from the packaged registry. Only an R2 failure rolls back, to t6OJTCcm |  | OPEN |
| irpt-status | tf-lambda | module.irpt_status.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T153905Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 5 leg(s)
- 20261009T154002Z LEG R0 closed: R0 MET, measured member-by-member rather than by size. The LIVE side was taken from the FUNCTION own code location via g
- 20261009T154003Z LEG L1 closed: UPLOADED from the DETACHED worktree /c/dev/anl-r1-pin4 at 287b105600, which the amendment requires -- a shared-root buil
