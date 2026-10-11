# Deploy Completion Record
**Date opened:** 2026-10-11T07:21:37.657334+00:00
**Status:** OPEN
**Deploy:** NFRA_TRNSPT.TO-APPLY-mp23 AMENDMENT 1: re-apply aws_lambda_function.mail_pull (outlook-global-transcripts-pull-lambda) CODE ONLY onto the package the Teams pull already runs, so all three functions of root infra/aws/terraform/transcripts read ONE CodeSha256. NO REBUILD -- the tree is AHEAD of the zip (TR-tt-23 @5374271f5c changed teams/pull.py), so a build.sh anywhere in this act is a STOP; the bytes are the EXISTING dist/transcripts-pull.zip at AI4UQD0ME+ABza1X0BrBjGjpqjN7f2fc0Cdxb88aA/I=. ONE FUNCTION MOVES: outlook-global-transcripts-pull-lambda VGIq85Xxm5KVLCnv16BASS63RsPMHScMEwZJP5SuMNY= -> AI4UQD0ME+ABza1X0BrBjGjpqjN7f2fc0Cdxb88aA/I=. TWO MUST NOT MOVE, both already on AI4UQD0M... with LastModified unchanged: teams-global-transcripts-pull-lambda and outlook-global-commentary-draft-lambda. Disarms row NFRA_TRNSPT-D2-S22 read (1). Pair: COO packet @b73b89ddbd (half in section 8), CTO half @f4ec64d888 section 3. Rollback (Branch B): place the KEPT deployed zip (VGIq85Xx..., fetched from get-function and hash-proven) at the root's zip path, re-apply the same target, proof CodeSha256 back at VGIq85Xx..., then put the root zip back at the path and re-hash so the Teams pull's build input is intact.
**Authored by:** 0.7.0_AE_CloudOps~TR2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | KEEP the mail pull's current package for rollback: fetch the deployed zip from get-function's code location, store it OUTSIDE the repo, hash it | the fetched file's base64 sha256 reading VGIq85Xxm5KVLCnv16BASS63RsPMHScMEwZJP5SuMNY=, EQUAL to the live CodeSha256, which proves the kept file is the running build and not merely a file of the right name |  | OPEN |
| L2 | activation | safe-apply in infra/aws/terraform/transcripts TARGETED at aws_lambda_function.mail_pull ONLY, code only, no rebuild | the local zip hash bound to the Teams pull's live digest BEFORE the plan; a plan of 0 to add, 1 to change, 0 to destroy whose one resource is aws_lambda_function.mail_pull and whose only changed argument is source_code_hash, with memory_size, timeout, handler, environment and layer unchanged and no reader resource; then the three functions on ONE CodeSha256, the other two LastModified unchanged, and the mail pull at MemorySize 1024 and Timeout 600 |  | OPEN |
| L3 | verify | ONE invoke of outlook-global-transcripts-pull-lambda, graded against the packet's section 4 | no errorMessage, exactly one MAIL-PULL-FIRE line carrying window_days=7 and list_refusals=0, and no [ERROR]; any admitted-and-landed message reported with its counts before the close; list_refusals above 0 or any [ERROR] is Branch B |  | OPEN |

## Log

- 20261011T072137Z OPENED by 0.7.0_AE_CloudOps~TR2 with 3 leg(s)
