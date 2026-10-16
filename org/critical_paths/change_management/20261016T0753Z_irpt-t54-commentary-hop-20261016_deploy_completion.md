# Deploy Completion Record
**Date opened:** 2026-10-16T07:53:23.936651+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-t54 (AR-tf-76): FWD-4 commentary hop, three artifacts one at a time at HEAD 8da0127c5b: G the inline policy of irpt-commentary-draft-store-role gains S6 and S7; D the draft-store zip (commentary_draft_store.py changed, durable_job.py added; BUILD_ONLY twice, digest recorded before deploy); C the SURGICAL commentary zip (lambda_handler.py replaced); P the driven proof on the synthetic row REQ-d47252fe74634d0c5cdd8067, restored; COO packet blob 8dcbccc512, CTO half msg 9181
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G | verify | irpt-commentary-draft-store-role inline policy S6 and S7 (draft-store root, one resource in place) | simulate battery, plan 0/1/0, safe-apply, re-plan No changes, Sids S1 to S7 | validate Success; unscoped plan read 2 changes (the policy and the Lambda whose 3 attributes are only known-after-apply because the S3 artifact data source is read during apply); SCOPED plan -target the policy: 0 add 1 change 0 destroy, attribute policy only, equal to the simulated document; simulate battery 10 rows + 2 controls OK; safe-apply 0 added 1 changed 0 destroyed; re-plan No changes; Sids S6 S7 S1 to S5 read live | CLOSED 20261016T082516Z |
| P | verify | driven proof on synthetic row REQ-d47252fe74634d0c5cdd8067 plus two negative arms, restored | the answers, the row before and after, the restore read ABSENT |  | OPEN |
| irpt-commentary-draft-store-lambda | tf-lambda | module.irpt_commentary_draft_store.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | BUILD_ONLY twice byte-identical RizVjaXiTEhiTAZxJ1mUCGBv6p78N5N0PtzjE3dfAqI= recorded in the ledger before the deploy; member diff vs live: commentary_draft_store.py changed, durable_job.py added; one upload VersionId 0alBeYtamoL7JpslE4VGeHa4eUbCX7Lf read back byte-identical; scoped plan 0/1/0 (last_modified, s3_object_version, source_code_hash); safe-apply 0 added 1 changed 0 destroyed; re-plan No changes; live CodeSha256 equals the recorded digest, memory 512 timeout 29 unchanged | CLOSED 20261016T084627Z |
| outlook-global-commentary-draft-lambda | tf-lambda | aws_lambda_function.commentary | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261016T075323Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
- 20261016T082516Z LEG G closed: validate Success; unscoped plan read 2 changes (the policy and the Lambda whose 3 attributes are only known-after-apply 
- 20261016T084627Z LEG irpt-commentary-draft-store-lambda closed: BUILD_ONLY twice byte-identical RizVjaXiTEhiTAZxJ1mUCGBv6p78N5N0PtzjE3dfAqI= recorded in the ledger before the deploy; m

## Carried notes (hand-written lines kept across re-renders)

- 20261016T0840Z 0.7.0_AE_CloudOps~AQ2 ARTIFACT 2 DIGEST RECORDED BEFORE THE DEPLOY (CTO condition 2): irpt-commentary-draft-store-lambda BUILD_ONLY twice at detached HEAD c3cc3dd42a, byte-identical, CodeSha256 RizVjaXiTEhiTAZxJ1mUCGBv6p78N5N0PtzjE3dfAqI= (sha256 hex 462cd58da5e24c48624c067127599408606fea9efc3793743edce313775f02a2, 145665 bytes, 17 members); member diff against the live zip cwf6bUEb...: commentary_draft_store.py changed, durable_job.py added, nothing else; submission.py and durable_job.py present; clean-interpreter import OK. Rollback: the fetched live zip cwf6bUEb... (C:/dev/aq2-t54/pre2) and the S3 version aL8XyKRly10MtjXfQZuSL5DiC5lqMdwr.
- 20261016T0850Z 0.7.0_AE_CloudOps~AQ2 ARTIFACT 3 DIGEST RECORDED BEFORE THE DEPLOY: SURGICAL commentary zip (t54_surgical_zip.py, from the fetched live zip hUZY39qN... replacing exactly data/transcripts/scripts/commentary/lambda_handler.py with the git blob at c3cc3dd42a): 905858 bytes, 92 members (equals live), base64 sha256 I/6mirBTU5+JPCUUx6Xrmd1bn1vGAjvZTL75LhOm3HY=. PROOF-i 1 of 1 member byte-equal to the pin blob (sha256 141bb78ccf1a...); PROOF-ii same 92 names in the same order, members that differ from live: 1, exactly lambda_handler.py; PROOF-iii clean python -I import of commentary.lambda_handler, commentary.drafter, commentary.entry rc=0. Clock 08:5xZ Friday: before the 13:00Z Teams pull and the 23:30Z mail pull, clear of every fire. Rollback artifact: the fetched live zip hUZY39qN... (C:/dev/aq2-t54/pre2).
