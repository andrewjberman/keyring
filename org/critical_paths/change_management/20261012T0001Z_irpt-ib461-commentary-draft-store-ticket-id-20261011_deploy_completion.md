# Deploy Completion Record
**Date opened:** 2026-10-12T00:01:50.105686+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-pr-461: APPLY irpt-commentary-draft-store-lambda under the signed pair of IB-pr-460 (COO half 39597f02ec, CTO half 7a2a9182a2, CTO msg 6150). ONE function, ONE member of 16 (commentary_draft_store.py: a first persist that answers OK carries the accepted record ticket_id when it has one). No caller changes. Signed digest cwf6bUEbPvKkpOtbldaTmzaqst08D/L7DFB32RtJP1A=; live before AsKY+KWLZBW54N73z9VdnR7SIKMPd9RDoYS8x4vRkpw= (read by this seat at get-function-configuration, equals the pair); rollback S3 version ToWX4K7J1NpXcwbkf4imLR6Xu0_0aJGn re-read PRESENT and still LATEST of investor-reporting/irpt-commentary-draft-store-lambda.zip, its content-sha256 equal to the live digest. Invoke right read first by simulate-principal-policy for arn:aws:iam::313476888478:user/cloudops-dell2-agent-user: allowed via cloudops-dell-agent-deploy-policy; the function carries NO resource policy (get-policy ResourceNotFoundException), so no hidden deny; NO grant sought. NO DRAFT IS PERSISTED: the member on a real first persist is UNEXERCISED LIVE.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | live CodeSha256 after the apply | equals the signed digest cwf6bUEbPvKkpOtbldaTmzaqst08D/L7DFB32RtJP1A= |  | OPEN |
| V2 | verify | the parser-refused shape op=none invoked once before and once after the apply, persisting nothing | both answer bodies identical and both status REFUSED reason INVALID_REQUEST |  | OPEN |
| V3 | verify | one get_ref invoke for a request that HAS a draft | answer key names only, sorted, never a ref value; or made=false with why_not_made |  | OPEN |
| irpt-commentary-draft-store-lambda | tf-lambda | module.irpt_commentary_draft_store.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261012T000150Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
