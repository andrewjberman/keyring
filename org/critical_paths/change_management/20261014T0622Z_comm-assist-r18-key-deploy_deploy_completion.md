# Deploy Completion Record
**Date opened:** 2026-10-14T06:22:37.583675+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T065050Z
**Deploy:** COMM_ASSIST r18 CA-j-8: resource policy narrowing the ingress-mark key (aws_secretsmanager_secret_policy.ca_ingress_mark, one Deny statement), NO code, pinned tree 3af44d523b -- secret teams/global/ingress-mark, functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda unchanged (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~CA
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | aws_secretsmanager_secret_policy.ca_ingress_mark created (1/0/0), exactly one Deny GetSecretValue statement excepting teams-global-chat-assist-role | get-resource-policy on teams/global/ingress-mark shows one Deny statement; saved plan JSON | safe-apply of the saved plan -target=aws_secretsmanager_secret_policy.ca_ingress_mark at 2026-10-14T06:38Z: 1 added 0 changed 0 destroyed; live get-resource-policy shows exactly one statement (Deny secretsmanager:GetSecretValue, Principal *, StringNotEquals aws:PrincipalArn = arn:aws:iam::313476888478:role/teams-global-chat-assist-role); BEFORE it returned no ResourcePolicy; saved r18b/AFTER_resource_policy.json and r18b/BEFORE_get_resource_policy.json | CLOSED 20261014T064057Z |
| L2 | verify | CAj8-AC1 check_j8_live.py PASS plus a targeted re-plan reading no changes; simulate GetSecretValue allowed for the role and explicitDeny for both Dell users | check output + plan tail | CAj8-AC1 check_j8_live.py RESULT: PASS at ~06:39Z (one Deny statement; simulated against the LIVE policy the execution role allowed and both Dell users explicitDeny; PutSecretValue/DescribeSecret/PutResourcePolicy allowed for both Dell users; code hash nX67q... and mode record unmoved on both functions; secret version current, value not read). BEFORE-apply simulation with the plan text: role allowed, dell1 and dell2 explicitDeny, no-policy controls allowed for all three (r18b/BEFORE_simulation.txt). Targeted re-plan -detailed-exitcode rc=0 'No changes' -- saved r18b/CAj8_REPLAN_AFTER.txt | CLOSED 20261014T064057Z |
| L3 | verify | ingress logs show ingress_poll and mail_poll within 10 minutes and neither function log shows AccessDenied for the mark secret | log-line counts (no message content, secret value never read) | log read 2026-10-14T06:50:26Z, 12m after the apply: ingress 12 ingress_poll (last 06:50:19Z), 3 mail_poll (last 06:50:23Z, failed=0 refused=0 sent=0), 0 Traceback/ERROR, 0 AccessDenied and 0 ingress-mark lines; handler log group 0 lines (no text arrived, so the key read on a cold container was NOT exercised in the window -- the issuer's first-real-text watch covers it); counts only, saved r18b/CAj8_L3_log_read.txt | CLOSED 20261014T065049Z |

## Log

- 20261014T062237Z OPENED by 0.7.0_AE_CloudOps~CA with 3 leg(s)
- 20261014T064057Z LEG L1 closed: safe-apply of the saved plan -target=aws_secretsmanager_secret_policy.ca_ingress_mark at 2026-10-14T06:38Z: 1 added 0 ch
- 20261014T064057Z LEG L2 closed: CAj8-AC1 check_j8_live.py RESULT: PASS at ~06:39Z (one Deny statement; simulated against the LIVE policy the execution r
- 20261014T065049Z LEG L3 closed: log read 2026-10-14T06:50:26Z, 12m after the apply: ingress 12 ingress_poll (last 06:50:19Z), 3 mail_poll (last 06:50:23
- 20261014T065050Z CLOSED -- all 3 legs proven
