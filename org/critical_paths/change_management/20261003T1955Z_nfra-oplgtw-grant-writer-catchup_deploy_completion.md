# Deploy Completion Record
**Date opened:** 2026-10-03T19:55:46.164388+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-gw-2: mcportal-grant-writer-lambda code redeployed from the closure of gateway ref af2d762970 (targeted terraform apply, aws_lambda_function.mcportal_grant_writer only)
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~26
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| apply | tf-lambda | aws_lambda_function.mcportal_grant_writer targeted safe-apply of the saved plan | safe-apply output line (Apply complete: 0 added, 1 changed, 0 destroyed); plan was one in-place update, code hash only, environment unchanged |  | OPEN |
| read-back | verify | deployed zip == staged closure; environment hashes == GW2_ENV_BEFORE.json; State/LastUpdateStatus Active/Successful | gw2.AC1 RESULT PASS; env hashes equal 3 of 3; get-function-configuration Active/Successful; CloudWatch ERROR count if invoked |  | OPEN |
| rollback-proven | verify | saved deployed zip 9e1cfe77 (54650 bytes) outside repo; rollback = same targeted safe-apply from .build/staged extracted from it | PHASE A rollback plan equal-and-opposite hash pair (ANNOUNCE_OG-gw-2.md step 6) and verify PASS, or rolled back and re-verified |  | OPEN |

## Log

- 20261003T195546Z OPENED by 0.9.0_WK_NFRA_OPLGTW~26 with 3 leg(s)
