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
| A | activation | safe-apply targeted to the draft-store module, its role, role policy and commentary_draft_store_invoke policy in infra/aws/terraform/investor-reporting/export | EXACTLY those creates with 0 change and 0 destroy; anything else is a STOP. The module owns the function log group per AMENDMENT 2, so no root log group is created |  | OPEN |
| A2 | activation | set irpt-anlreq-x10-v1 ACTIVE in infra/logic/registry/reporting_policies.json with enforcement_ref = the full 40-char hash of the merge carrying the store, a one-row registry commit; rebuild the store zip from that commit; re-apply the function CODE ONLY | the row reads ACTIVE at the applied pin and the rebuilt zip sha256 is recorded here |  | OPEN |
| KEYS | verify | CTO condition: print the transcripts key ARN beside the request_compositions key ARN | they must DIFFER; equal is a STOP |  | OPEN |
| B | activation | safe-apply targeted to the commentary.tf resources the COO half lists in infra/aws/terraform/transcripts | exact creates only: log group, five queues, two queue policies, role, policy, three attachments, KMS grant, function, event-source mapping |  | OPEN |
| SIM | verify | CTO condition: simulate as the commentary role | dynamodb:GetItem and kms:Decrypt on the IRPT table/key DENIED; lambda:InvokeFunction on the reader and the store ALLOWED. A key-policy-only grant reads implicitDeny in the simulator, so the KEY POLICY is read where the simulator is blind -- the TO-RUN-a17 finding this order cites back to me |  | OPEN |
| INVOKE | verify | ONE test invoke with a synthetic analysis_ready for a 49financial test request | report the STAGES only -- no composition, no text, no content in any file or message |  | OPEN |

## Log

- 20261009T161950Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 6 leg(s)
