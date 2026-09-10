# Deploy Completion Record
**Date opened:** 2026-09-10T03:47:51.476797+00:00
**Status:** OPEN
**Deploy:** ETFS_GUARDRAIL.TO-EG-s-20 -- THE SEND PATH MADE CORRECT AND TEST-SAFE: the terminal-send guard fixed at BOTH sites (the live guard at lambda_function.py:435 and the terminal_qa rehearsal at :516, rows W1-S25/W1-S29/S11) plus a test-invocation recipient path that cannot reach aj@opalinvest.com (Andrew-direct 2026-09-10 ~02:5xZ), Terraform-deployed under safe-apply from a SAVED PLAN FILE. NO SEND AND NO ORCHESTRATOR INVOKE IS FIRED BY THIS ORDER. Served function: etfs-reports-orchestrator, PRE-STATE CodeSha256 M5Dopbky3W1f1j97cqAB403Kh7IofIv/p0fCtRg7W80= LastModified 2026-09-10T01:16:14.000+0000 CodeSize 10193 (read live 2026-09-10). ROLLBACK: git show ea47e92a72:infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py (sha256 dc05ea90c94dc41e21a92b63a69a3bc3f278dbc878c11324e35b56a295241fd8, 28504 B, BYTE-EQUAL to the deployed zip member) re-applied and re-deployed by the same targeted safe-apply. NEVER-WIDEN HALVES: COO = the L6 round-3 issuance ea47e92a72 which cut this cell and its paths block; CTO = PRD v0.5 @7ba9b976b0 (FWD-10 superseding FWD-7). NO SERVED OUTPUT MOVES under this order -- no S3 key is written, moved or deleted, so the never-widen trigger is not reached; the halves are named because the face requires them. NEVER-9: never a bare terraform apply, never aws lambda update-function-code.
**Authored by:** 0.9.0_WK_ETFS_GUARDRAIL~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the two-site guard fix (_normalize_unresolved at :435 and in terminal_qa) + the test-safe recipient path (_resolve_recipients/_drop_forbidden/TEST_FORBIDDEN_RECIPIENTS) + new pytest arms built from the PRODUCER's output, committed on wk-etfs_guardrail-3-4 BEFORE the apply | commit hash + python -m pytest infra/aws/lambda/etfs-reports-orchestrator/test_terminal_send.py -q count >= 7, plus the same NEW arms run against the PRE-FIX blob and FAILING |  | OPEN |
| L2 | activation | aws_lambda_function.orchestrator -- TARGETED terraform plan -out=<planfile> then HALT_ACK=1 .tools/safe-apply.sh on that SAVED PLAN FILE (.tools/terraform.exe v1.9.8) | the targeted plan reads exactly 0 to add, 1 to change, 0 to destroy on that one resource; the apply's own 1 changed line; the pre-apply plan transcript PRESERVED in the deliverables |  | OPEN |
| L3 | verify | DEPLOYED == BUILT -- the served CodeSha256 after the apply against the base64 sha256 of the zip Terraform built, and a 0-diff targeted re-plan | served CodeSha256 == built zip base64 sha256 (both printed) + terraform plan -detailed-exitcode -target=aws_lambda_function.orchestrator rc=0 No changes |  | OPEN |
| L4 | verify | BOTH DEFECT SITES fixed in the DEPLOYED bytes -- the guard and the terminal_qa rehearsal quoted post-fix with their line numbers, plus a census over the deployed source for remaining reads of the absent key | both post-fix lines quoted from the zip member with line numbers + the census denominator with a CODE-band count of 0 + the guard evaluated TRUTHY against the real served coverage_unresolved.json beside the pre-fix expression evaluating to [] |  | OPEN |
| L5 | verify | THE RECIPIENT PROPERTY both directions, resolved from the DEPLOYED bytes | a TEST invocation's resolved list contains no aj@opalinvest.com across every adversarial override (denominator printed) AND a SCHEDULED invocation's list is unchanged and still contains BOTH -- both lists printed |  | OPEN |

## Log

- 20260910T034751Z OPENED by 0.9.0_WK_ETFS_GUARDRAIL~4 with 5 leg(s)
