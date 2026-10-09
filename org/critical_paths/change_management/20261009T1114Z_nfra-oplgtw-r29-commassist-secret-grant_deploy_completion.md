# Deploy Completion Record
**Date opened:** 2026-10-09T11:14:14.755679+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T112215Z
**Deploy:** OG-ap-3 step 2: one ARN added to gateway-read-secrets-policy for gateway/mail/commassist-bearer (policy only)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| POL | activation | aws_iam_role_policy.gw_gateway_read_secrets | targeted safe-apply from a saved plan; expect 0 add / 1 change / 0 destroy, the role policy only -- any other row is a STOP | safe-apply from a SAVED targeted plan at ~11:18Z -> 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' rc=0; comp-tagauthz PASSED, tombstone-gate CLEAN (0 creates / 7 tombstones). Plan graded from show -json by DECOMPOSING the policy document, not by diffing it as a string: 2 resource_changes, exactly 1 non-no-op, statements 1 -> 1, Effect Allow unchanged, Action ['secretsmanager:GetSecretValue'] unchanged, Condition None unchanged, resources 4 -> 5 with ADDED exactly ['...gateway/mail/commassist-bearer-cPYbR3'] and REMOVED []. That decomposition matters because 0/1/0 would read identically had an ARN been dropped or the action widened -- the whole policy is one opaque attribute in the plan. The added ARN's suffix -cPYbR3 equals the ARN the create returned, so the grant names the secret that was actually made. | CLOSED 20261009T112214Z |
| RB | verify | opal-gateway-role | read the policy back: 5 resources, the commassist ARN present, the prior 4 intact, one statement and one action unchanged | Live iam get-role-policy read-back: 1 statement, Effect Allow, Action ['secretsmanager:GetSecretValue'], Condition None, and 5 resources with the denominator printed. commassist present TRUE; all FOUR prior ARNs individually confirmed retained by name (gateway/transcripts/bearer, gateway/mail/bearer, gateway/principals/rosters, gateway/teams/bearer) rather than inferred from the count -- a count of 5 would also hold if one prior had been swapped for the new one. Post-apply targeted re-plan reads 'No changes. Your infrastructure matches the configuration.' The secret itself: gateway/mail/commassist-bearer, VersionId 5c368b4d-d6e8-4366-8988-92f4eb4b8fcd, AWSCURRENT, rotation disabled, 64 hex characters (32 bytes of entropy). Its VALUE was generated inside one process and passed to boto3 in memory -- never argv, a file, a log, TF state or a commit -- and get_secret_value was never called, so the read-back is describe-only. gateway/mail/bearer AWSCURRENT was not written. | CLOSED 20261009T112214Z |

## Log

- 20261009T111414Z OPENED by 0.7.0_AE_CloudOps~Z with 2 leg(s)
- 20261009T112214Z LEG POL closed: safe-apply from a SAVED targeted plan at ~11:18Z -> 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' rc=0; 
- 20261009T112214Z LEG RB closed: Live iam get-role-policy read-back: 1 statement, Effect Allow, Action ['secretsmanager:GetSecretValue'], Condition None,
- 20261009T112215Z CLOSED -- all 2 legs proven
