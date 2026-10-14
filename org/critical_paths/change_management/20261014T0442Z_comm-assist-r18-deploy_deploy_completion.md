# Deploy Completion Record
**Date opened:** 2026-10-14T04:42:55.796676+00:00
**Status:** OPEN
**Deploy:** COMM_ASSIST r18 CA-j-3: ingress mark -- secret shell teams/global/ingress-mark, its value out of band, then module.ldo_001 code + INGRESS_MARK_MODE=record + exec-policy Secrets ARN, pinned build 38ce5a7981 -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~CA
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | secret shell teams/global/ingress-mark created (aws_secretsmanager_secret.ca_ingress_mark, 1/0/0, no value) | describe-secret Name + ARN, no version before step 2 |  | OPEN |
| L2 | activation | secret value put out of band; AWSCURRENT version exists, value never read or printed, generating file deleted | describe-secret VersionIdsToStages shows AWSCURRENT (version id only) |  | OPEN |
| L3 | activation | teams-global-chat-assist-handler-lambda code: new CodeSha256 equal to the built package replacing sWltfUwyJQpANEhbY+KFkszo8ScLKEIi7Lm4qyUNWrM=, plus env key INGRESS_MARK_MODE=record | get-function-configuration CodeSha256 + LastModified + env key names |  | OPEN |
| L4 | activation | teams-global-chat-assist-ingress-lambda code: new CodeSha256 equal to the built package replacing sWltf..., plus env key INGRESS_MARK_MODE=record | get-function-configuration CodeSha256 + LastModified + env key names |  | OPEN |
| L5 | activation | aws_iam_policy.exec Secrets statement gains exactly the new secret ARN | saved plan diff plus check_j3_live simulated read per role |  | OPEN |
| L6 | verify | CAj3-AC2 check_j3_live.py PASS plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail |  | OPEN |
| L7 | verify | ingress logs show ingress_poll and mail_poll within 10 minutes of step 3 | log-line counts (no message content) |  | OPEN |

## Log

- 20261014T044255Z OPENED by 0.7.0_AE_CloudOps~CA with 7 leg(s)
