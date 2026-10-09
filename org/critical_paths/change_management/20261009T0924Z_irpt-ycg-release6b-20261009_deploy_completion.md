# Deploy Completion Record
**Date opened:** 2026-10-09T09:24:31.343551+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND APPLY-Y77 (AMENDMENT 2): irpt-ycharts-generate RELEASE 6b custody, PINNED to 66207bce7d, built tdpterTMfJlWXjnoAQCwil+wN/Jf8Q/yLjGxTk7yUkk=, over live ZA0QJ5Wt/7JcwmuzVfHOeNAdFk6th4H5IEeqQStDYm8= with rollback source S3 version 8rOI5aDff8mlWQQ6YNVy7Is11Pfh8jcn
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| Y0 | verify | step 0 pre-checks in the detached pin worktree /c/dev/y77-pin | live CodeSha256 equals ZA0QJ5Wt..., the rollback source is S3 version 8rOI5aDf..., and the census at the pin reads EXACTLY 3 changed members: acceptance.py, submission.py, contracts/AnalysisSubmissionRequest.schema.json | ALL THREE STEP-0 PRE-CHECKS PASS, measured in the detached pin worktree /c/dev/y77-pin at 66207bce7d (0 uncommitted), which AMENDMENT 2 requires for every build, census, plan and apply step. (a) live CodeSha256 ZA0QJ5Wt/7JcwmuzVfHOeNAdFk6th4H5IEeqQStDYm8= EQUALS the value the amendment names, LastModified 2026-10-09T07:49:20Z -- which is the IB-pr-390 apply, the act this seat earlier established was a TERRAFORM apply and not the banned CLI call, so the state the amendment builds on is the state I measured. (b) the rollback source is S3 version 8rOI5aDff8mlWQQ6YNVy7Is11Pfh8jcn, exactly as named, and its own content-sha256 metadata reads ZA0QJ5Wt..., i.e. that version is self-consistently the one carrying the live bytes rather than a version believed to. (c) the census at the pin against live reads built_members=104 live_members=104 and changed_members=3, and the three ARE the three the amendment names: acceptance.py, submission.py and contracts/AnalysisSubmissionRequest.schema.json -- no fourth member, nothing added, nothing removed. Note what this census is NOT: it is the pin-vs-live comparison, so it also confirms the earlier release-6 pin is superseded; a build at HEAD or at the old pin would not produce this set. | CLOSED 20261009T092452Z |
| Y1 | s3-prefix | build and upload from the pin worktree | the uploaded object downloaded back and its content-sha256 equal to tdpterTMfJlWXjnoAQCwil+wN/Jf8Q/yLjGxTk7yUkk= or STOP |  | OPEN |
| Y2 | activation | ONE safe-apply of the targeted plan | the plan is 1 ADD (the custody policy) plus the function s3_object_version and source_code_hash, and NO layer diff because IB-pr-390 already attached it; ANY other line is a STOP per the CTO condition |  | OPEN |
| Y3 | verify | reads 0 to 5 of the 6b pair section 4 | read 5 is the ticket binding live: one input_id submission with a valid ticket_id is accepted and its record carries it, a malformed one refuses TICKET_REFERENCE; reads 4 and 5 S3 objects recorded as prospect_objects [{key, version_id}] and NOT deleted, their deletes waiting on Andrew word |  | OPEN |
| irpt-ycharts-generate | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T092431Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 5 leg(s)
- 20261009T092452Z LEG Y0 closed: ALL THREE STEP-0 PRE-CHECKS PASS, measured in the detached pin worktree /c/dev/y77-pin at 66207bce7d (0 uncommitted), wh
