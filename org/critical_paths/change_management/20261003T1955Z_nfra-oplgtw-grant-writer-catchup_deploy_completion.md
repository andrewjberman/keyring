# Deploy Completion Record
**Date opened:** 2026-10-03T19:55:46.164388+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261003T201244Z
**Deploy:** NFRA_OPLGTW OG-gw-2: mcportal-grant-writer-lambda code redeployed from the closure of gateway ref af2d762970 (targeted terraform apply, aws_lambda_function.mcportal_grant_writer only)
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~26
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| apply | tf-lambda | aws_lambda_function.mcportal_grant_writer targeted safe-apply of the saved plan | safe-apply output line (Apply complete: 0 added, 1 changed, 0 destroyed); plan was one in-place update, code hash only, environment unchanged | safe-apply 2026-10-03T20:07Z rc=0 on the saved targeted plan (one in-place update of aws_lambda_function.mcportal_grant_writer; changing attrs last_modified, source_code_hash nhz+dwJs -> ZyYCPPyP; environment before==after 3 keys; resources 4, non-no-op 1): 'aws_lambda_function.mcportal_grant_writer: Modifications complete after 6s' / 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.'; comp-tagauthz gate PASSED; W2 re-read before (CodeSha256 nhz+dwJs, manifest af2d762970) | CLOSED 20261003T201243Z |
| read-back | verify | deployed zip == staged closure; environment hashes == GW2_ENV_BEFORE.json; State/LastUpdateStatus Active/Successful | gw2.AC1 RESULT PASS; env hashes equal 3 of 3; get-function-configuration Active/Successful; CloudWatch ERROR count if invoked | 20:09Z gw2.AC1: files deployed 11 staged 11 same 11 diff 0 only-deployed 0 only-staged 0 RESULT: PASS; env keys before 3 now 3, value hashes equal 3 of 3 vs GW2_ENV_BEFORE.json; get-function-configuration CodeSha256 ZyYCPPyP... State Active LastUpdateStatus Successful; CloudWatch: 0 events, 0 ERROR since 20:07Z, Invocations datapoints 0 (not invoked); layer count 1 | CLOSED 20261003T201243Z |
| rollback-proven | verify | saved deployed zip 9e1cfe77 (54650 bytes) outside repo; rollback = same targeted safe-apply from .build/staged extracted from it | PHASE A rollback plan equal-and-opposite hash pair (ANNOUNCE_OG-gw-2.md step 6) and verify PASS, or rolled back and re-verified | saved deployed zip 54650 bytes sha256 9e1cfe77..df732 outside the repo; PHASE A rollback plan No changes with config hash == live nhz+dwJs; POST-APPLY 20:1xZ rollback plan (.build/staged = extracted saved zip, same targeted plan, same variable feed, NOT applied): rc 2, one in-place update of the function, changing attrs last_modified + source_code_hash only, ZyYCPPyP -> nhz+dwJs, environment unchanged, non-no-op 1 of 4; not executed, not needed (read-back PASS) | CLOSED 20261003T201243Z |

## Log

- 20261003T195546Z OPENED by 0.9.0_WK_NFRA_OPLGTW~26 with 3 leg(s)
- 20261003T201243Z LEG apply closed: safe-apply 2026-10-03T20:07Z rc=0 on the saved targeted plan (one in-place update of aws_lambda_function.mcportal_grant_
- 20261003T201243Z LEG read-back closed: 20:09Z gw2.AC1: files deployed 11 staged 11 same 11 diff 0 only-deployed 0 only-staged 0 RESULT: PASS; env keys before 3
- 20261003T201243Z LEG rollback-proven closed: saved deployed zip 54650 bytes sha256 9e1cfe77..df732 outside the repo; PHASE A rollback plan No changes with config has
- 20261003T201244Z CLOSED -- all 3 legs proven
