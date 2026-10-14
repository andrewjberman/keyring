# Deploy Completion Record
**Date opened:** 2026-10-14T06:22:37.583675+00:00
**Status:** OPEN
**Deploy:** COMM_ASSIST r18 CA-j-8: resource policy narrowing the ingress-mark key (aws_secretsmanager_secret_policy.ca_ingress_mark, one Deny statement), NO code, pinned tree 3af44d523b -- secret teams/global/ingress-mark, functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda unchanged (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~CA
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | aws_secretsmanager_secret_policy.ca_ingress_mark created (1/0/0), exactly one Deny GetSecretValue statement excepting teams-global-chat-assist-role | get-resource-policy on teams/global/ingress-mark shows one Deny statement; saved plan JSON |  | OPEN |
| L2 | verify | CAj8-AC1 check_j8_live.py PASS plus a targeted re-plan reading no changes; simulate GetSecretValue allowed for the role and explicitDeny for both Dell users | check output + plan tail |  | OPEN |
| L3 | verify | ingress logs show ingress_poll and mail_poll within 10 minutes and neither function log shows AccessDenied for the mark secret | log-line counts (no message content, secret value never read) |  | OPEN |

## Log

- 20261014T062237Z OPENED by 0.7.0_AE_CloudOps~CA with 3 leg(s)
