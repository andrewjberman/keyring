# Deploy Completion Record
**Date opened:** 2026-10-09T16:19:50.883404+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-t1 (AMENDMENT 2 @080a66522c, resumed on T2 msg 3594): the FIRST apply of the commentary DRAFT store (IRPT export root) then the commentary Lambda (transcripts root), in the pair's order A -> A2 -> B. PIN f616e46440a2, which carries BOTH 87909ea558 (the staged_from build fix, without which step A cannot build) and 36b0bc0423 (the D2-S50 log-group fix, without which step 1 half-lands on ResourceAlreadyExistsException). STORE ZIP sha256 xyROb11eaQHbVx7KqF7lQAauPL2VOPKv7v8t9QqXJc8= from BUILD_ONLY, 0 files-not-found. BAU_PARITY_SKIP=1 is RULED in TO-AR-t-12 AMENDMENT 8: the seven unregistered siblings in the shared source_dir are outside the store's import closure -- cited here as the order requires, not taken as my own judgement. PRE-STATE READ: irpt-commentary-draft-store-lambda is ResourceNotFoundException (step A creates it) while irpt-commentary-composition-read-lambda is live at ZZmWOFSA and irpt-commentary-composition-invoke-policy EXISTS, which is step 0's IB-pr-391 condition -- one absent and one present, so the read discriminates
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | activation | safe-apply targeted to the draft-store module, its role, role policy and commentary_draft_store_invoke policy in infra/aws/terraform/investor-reporting/export | EXACTLY those creates with 0 change and 0 destroy; anything else is a STOP. The module owns the function log group per AMENDMENT 2, so no root log group is created | STEP A LANDED EXACTLY AS PLANNED: Apply complete, 5 added, 0 changed, 0 destroyed, matching the committed plan text @02d22dfc5c. The five are aws_iam_policy.commentary_draft_store_invoke, aws_iam_role.commentary_draft_store, aws_iam_role_policy.commentary_draft_store, module.irpt_commentary_draft_store.aws_cloudwatch_log_group.lambda and module.irpt_commentary_draft_store.aws_lambda_function.this; module...data.aws_s3_object.artifact was READ during apply, a data source rather than a create. THE DECISIVE PRE-APPLY READ WAS THE LOG GROUP OWNER, NOT THE COUNT: the plan carried ZERO root-level aws_cloudwatch_log_group resources and exactly ONE module-level one at retention_in_days 14. A ROOT log group would have meant the pin lacked 36b0bc0423 and that this step was about to half-land on ResourceAlreadyExistsException, so that read is what proved the pin rather than the number of creates. LIVE VERIFICATION after the apply: irpt-commentary-draft-store-lambda CodeSha256 xyROb11eaQHbVx7KqF7lQAauPL2VOPKv7v8t9QqXJc8= EQUALS the built and uploaded value; runtime python3.12, memory 512, timeout 29, handler commentary_draft_store.lambda_handler, role irpt-commentary-draft-store-role created 16:26:14Z; the invoke policy exists at v1 with AttachmentCount 0; log group /aws/lambda/irpt-commentary-draft-store-lambda at 14-day retention. PRE-STATE was measured and discriminating: the function read ResourceNotFoundException before this step while the IB-pr-391 reader read live at ZZmWOFSA, so one absent and one present from the same instrument. | CLOSED 20261009T163614Z |
| A2 | activation | set irpt-anlreq-x10-v1 ACTIVE in infra/logic/registry/reporting_policies.json with enforcement_ref = the full 40-char hash of the merge carrying the store, a one-row registry commit; rebuild the store zip from that commit; re-apply the function CODE ONLY | the row reads ACTIVE at the applied pin and the rebuilt zip sha256 is recorded here |  | OPEN |
| KEYS | verify | CTO condition: print the transcripts key ARN beside the request_compositions key ARN | they must DIFFER; equal is a STOP |  | OPEN |
| B | activation | safe-apply targeted to the commentary.tf resources the COO half lists in infra/aws/terraform/transcripts | exact creates only: log group, five queues, two queue policies, role, policy, three attachments, KMS grant, function, event-source mapping |  | OPEN |
| SIM | verify | CTO condition: simulate as the commentary role | dynamodb:GetItem and kms:Decrypt on the IRPT table/key DENIED; lambda:InvokeFunction on the reader and the store ALLOWED. A key-policy-only grant reads implicitDeny in the simulator, so the KEY POLICY is read where the simulator is blind -- the TO-RUN-a17 finding this order cites back to me |  | OPEN |
| INVOKE | verify | ONE test invoke with a synthetic analysis_ready for a 49financial test request | report the STAGES only -- no composition, no text, no content in any file or message |  | OPEN |

## Log

- 20261009T161950Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 6 leg(s)
- 20261009T163614Z LEG A closed: STEP A LANDED EXACTLY AS PLANNED: Apply complete, 5 added, 0 changed, 0 destroyed, matching the committed plan text @02d

## A2 HELD at the registry edit -- 2026-10-09 ~16:4xZ

Leg A is CLOSED and nothing is half-landed: the store function, its role, role policy, invoke policy
and the module log group are live and verified, and the function will simply not be ENFORCED until
the registry row goes ACTIVE.

WHAT IS HELD. A2 step 1 of 4 is a one-row edit to infra/logic/registry/reporting_policies.json,
setting irpt-anlreq-x10-v1 to state ACTIVE with enforcement_ref
81c60ba22cade51a05af42f15f44a98356b16ac1. The edit was made, measured at +2 -2 with every byte
outside that row object asserted unchanged, and then REFUSED by the owned-paths gate:

    lane=IRPT_COMPLETION_REGISTRY (CTO grantor IRPT-M-REGISTRY-01 under Andrew session delegation)
    permitted_agents: 4.0.0_SA_CRO, ~A, ~B, ~C, ~D, 2.0.0_SA_COO~M, 2.0.0_SA_COO~M2
    agent=0.7.0_AE_CloudOps~DELL2 not in permitted_agents

The order TO-APPLY-t1 names that exact file in its own <paths> grant. So the order authorises a write
that a CTO exact-file grant withholds. A task order cannot widen a CTO lane grant, so the gate is
right and the paths block is the thing in error. I did not use the audited override: that escape is
for a lane AUTHORSHIP line, not for writing another lane's reserved file, and the file note adds
that an IRPT member-scope change needs an explicit equality proof and naming-owner review.

I REVERTED the edit rather than leave it uncommitted in a shared tree, so nothing of mine sits in a
file I may not write. The row reads PENDING_ENFORCEMENT with enforcement_ref null, exactly as before
I touched it.

THE HASH IS VERIFIED, so whoever lands it needs no further diagnosis. 2.0.0_SA_COO~T2 ruled
81c60ba22c and I checked it against the DEPLOYED bytes rather than the word: deployed
commentary_draft_store.py is 14137 bytes at sha256 6ad7ac7211c9ed3f, equal to that file at
81c60ba22c and DIFFERENT from my own earlier proposal 77adb5a035 (13255 bytes, 38ff1027d41af866),
which predates the I7 validator the store gained at 20a62c3c6c. repository.py and retention.py are
byte-identical at both refs and in the deployed zip, so 81c60ba22c carries the whole enforcing
closure as deployed. 20a62c3c6c is an ancestor of it; it is a 2-parent merge.

UN-PARKS WHEN 2.0.0_SA_COO~M2 (the dell2-seated permitted agent) lands the two-field edit and sends
its commit. A2 steps 2-4 then follow from that commit: rebuild the store zip FROM it, re-apply the
function code only, record the rebuilt sha256 here, and read the row ACTIVE at the applied pin.
