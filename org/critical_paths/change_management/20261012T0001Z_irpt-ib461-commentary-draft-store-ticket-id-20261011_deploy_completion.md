# Deploy Completion Record
**Date opened:** 2026-10-12T00:01:50.105686+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T001142Z
**Deploy:** IRPT_BCKEND IB-pr-461: APPLY irpt-commentary-draft-store-lambda under the signed pair of IB-pr-460 (COO half 39597f02ec, CTO half 7a2a9182a2, CTO msg 6150). ONE function, ONE member of 16 (commentary_draft_store.py: a first persist that answers OK carries the accepted record ticket_id when it has one). No caller changes. Signed digest cwf6bUEbPvKkpOtbldaTmzaqst08D/L7DFB32RtJP1A=; live before AsKY+KWLZBW54N73z9VdnR7SIKMPd9RDoYS8x4vRkpw= (read by this seat at get-function-configuration, equals the pair); rollback S3 version ToWX4K7J1NpXcwbkf4imLR6Xu0_0aJGn re-read PRESENT and still LATEST of investor-reporting/irpt-commentary-draft-store-lambda.zip, its content-sha256 equal to the live digest. Invoke right read first by simulate-principal-policy for arn:aws:iam::313476888478:user/cloudops-dell2-agent-user: allowed via cloudops-dell-agent-deploy-policy; the function carries NO resource policy (get-policy ResourceNotFoundException), so no hidden deny; NO grant sought. NO DRAFT IS PERSISTED: the member on a real first persist is UNEXERCISED LIVE.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | live CodeSha256 after the apply | equals the signed digest cwf6bUEbPvKkpOtbldaTmzaqst08D/L7DFB32RtJP1A= | get-function-configuration after the apply reads CodeSha256 cwf6bUEbPvKkpOtbldaTmzaqst08D/L7DFB32RtJP1A=, EQUAL to the signed digest, LastModified 2026-10-12T00:06:20.000+0000. The BUILD_ONLY control before any upload printed the same digest with 0 files not found and the import closure satisfied, and the uploaded S3 object was read back by head-object: version aL8XyKRly10MtjXfQZuSL5DiC5lqMdwr, content-sha256 equal to the signed digest. Three reads agree. | CLOSED 20261012T001051Z |
| V2 | verify | the parser-refused shape op=none invoked once before and once after the apply, persisting nothing | both answer bodies identical and both status REFUSED reason INVALID_REQUEST | Two direct invokes of the shape the parser refuses at its first check, one before the apply and one after, persisting nothing. Both answered StatusCode 200, FunctionError null, body exactly status REFUSED reason INVALID_REQUEST, and the two bodies compared byte-identical. The shape was read at this tree before sending: KEYS_BY_OP holds only put and get_ref, so op none is unknown at commentary_draft_store.py:91-92, which is the first check inside parse_request, and store() calls parse_request as its first statement at :158, before _resolve_record. compose_ports only constructs lazy boto3 clients, so nothing is read or written on the refused path. | CLOSED 20261012T001051Z |
| V3 | verify | one get_ref invoke for a request that HAS a draft | answer key names only, sorted, never a ref value; or made=false with why_not_made | NOT MADE, and the reason is a refusal this seat did not work around. The order's own path: if the table read is denied, get_ref.made is false with why_not_made and nothing more is tried. My simulate-principal-policy read dynamodb Query, Scan and GetItem all ALLOWED on the requests table, but the live Scan was refused by KMS: no identity-based policy allows kms:Decrypt on the table CMK for this principal. The table is encrypted with a customer key, so the DynamoDB action allow is not sufficient and the dynamodb-only simulate is not a sound oracle for the read. No grant was sought, no second route was tried, and no Query was attempted after the Scan refusal. Filed as a row. | CLOSED 20261012T001052Z |
| irpt-commentary-draft-store-lambda | tf-lambda | module.irpt_commentary_draft_store.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | safe-apply of a SAVED targeted plan at infra/aws/terraform/investor-reporting/export: Apply complete, 0 added, 1 changed, 0 destroyed; tombstone-gate checked 0 creates against 7 tombstones, CLEAN. The plan held ONE resource, module.irpt_commentary_draft_store.aws_lambda_function.this, and its only non-computed changes were s3_object_version ToWX4K7J1NpXcwbkf4imLR6Xu0_0aJGn to aL8XyKRly10MtjXfQZuSL5DiC5lqMdwr and source_code_hash AsKY+KWL to cwf6bUEb. No other resource line appeared, so plan_resources_other_than_the_function is 0. Never aws lambda update-function-code. | CLOSED 20261012T001051Z |

## Log

- 20261012T000150Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261012T001051Z LEG irpt-commentary-draft-store-lambda closed: safe-apply of a SAVED targeted plan at infra/aws/terraform/investor-reporting/export: Apply complete, 0 added, 1 changed
- 20261012T001051Z LEG V1 closed: get-function-configuration after the apply reads CodeSha256 cwf6bUEbPvKkpOtbldaTmzaqst08D/L7DFB32RtJP1A=, EQUAL to the s
- 20261012T001051Z LEG V2 closed: Two direct invokes of the shape the parser refuses at its first check, one before the apply and one after, persisting no
- 20261012T001052Z LEG V3 closed: NOT MADE, and the reason is a refusal this seat did not work around. The order's own path: if the table read is denied, 
- 20261012T001142Z CLOSED -- all 4 legs proven

---

## CLOSE STATEMENT (the order's step 7, in words)

APPLIED and verified. One function, one member of sixteen: on a first persist that answers OK, the
answer now carries the accepted record's ticket_id when it has one. Nothing else changed, and no caller
does anything different after this release.

**THE MEMBER ON A REAL FIRST PERSIST IS UNEXERCISED LIVE.** No draft was persisted to test this
release, by the CTO half's condition 4. The member will first be exercised by the commentary drafter's
next organic persist for a ticketed request. Nobody should read this entry as evidence that the member
works in the world; it is evidence that the bytes carrying it are live and that the function still
refuses what it refused before.

The two after-reads were direct invokes of a shape the parser refuses at its first check, identical
before and after, persisting nothing. The get_ref after-read was NOT made: the requests-table read was
refused by KMS (no kms:Decrypt on the table's CMK for this principal) even though the DynamoDB-action
simulation read allowed. No grant was sought and nothing further was tried.

Rollback remains available and was re-read: S3 version ToWX4K7J1NpXcwbkf4imLR6Xu0_0aJGn still holds the
pre-release bytes, now the second-newest version of the artifact key.
