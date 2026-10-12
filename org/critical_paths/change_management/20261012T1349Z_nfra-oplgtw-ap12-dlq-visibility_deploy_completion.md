# Deploy Completion Record
**Date opened:** 2026-10-12T13:49:14.286741+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-12: grant sqs:ChangeMessageVisibility on opal-assets-silver-dlq (ONE action, ONE queue, on the shared policy opal-assets-silver-dlq-access attached to 7 roles) and re-deploy the schwab converter at the OG-ap-11 build. CAUSE: row Z-S97 -- OG-ap-11's per-family drain deployed correctly and could not RUN without this action, and was rolled back under A2. Halves signed: COO @031aec9026, CTO @2a3205e69d. BLAST RADIUS AS SIGNED: all 7 roles (etf, smartx, orion, schwab, bd49finsurance, eclipse, blackdiamond) gain the one action on the one queue; each already holds sqs:DeleteMessage there, which can destroy a received message, while the new action can only re-time one; the other 6 roles' deployed code never calls it; the queue has NO RedrivePolicy, so a repeatedly-returned message stays until its owner deletes it or the 14-day retention expires.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | commit carrying the one-action policy edit on aws_iam_policy.silver_dlq_access plus the comment and description, and the pin moved back to the OG-ap-11 build commit a11240c01c | commit hash |  | OPEN |
| L2 | activation | safe-apply -target=aws_iam_policy.silver_dlq_access: plan reads exactly 0 to add, 1 to change, 0 to destroy on that one address and the document diff is the single action plus the description | saved-plan summary plus apply result |  | OPEN |
| L3 | verify | live simulate-principal-policy for opal-assets-silver-schwab-role on sqs:ChangeMessageVisibility against the DLQ ARN reads allowed, run as ONE resource-arn in its own invocation | simulate output |  | OPEN |
| L4 | activation | safe-apply -target the schwab function to re-deploy the OG-ap-11 build: plan reads 1 to change, the code fields plus OPAL_BUILD_COMMIT b3e481b261 -> a11240c01c | saved-plan summary plus apply result |  | OPEN |
| L5 | verify | live read-back of opal-assets-silver-schwab: CodeSha256 equals the OG-ap-11 build YeLmNn/Tkz+HYVVrCS/PeE+mISSAnH/8ilUUxPEnCmk=, State Active, LastUpdateStatus Successful, and a 0-diff re-plan | get-function-configuration output |  | OPEN |

## Log

- 20261012T134914Z OPENED by 0.7.0_AE_CloudOps~Z with 5 leg(s)
