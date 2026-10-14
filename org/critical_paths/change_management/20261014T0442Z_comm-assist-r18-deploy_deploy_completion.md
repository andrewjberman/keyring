# Deploy Completion Record
**Date opened:** 2026-10-14T04:42:55.796676+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T050540Z
**Deploy:** COMM_ASSIST r18 CA-j-3: ingress mark -- secret shell teams/global/ingress-mark, its value out of band, then module.ldo_001 code + INGRESS_MARK_MODE=record + exec-policy Secrets ARN, pinned build 38ce5a7981 -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~CA
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | secret shell teams/global/ingress-mark created (aws_secretsmanager_secret.ca_ingress_mark, 1/0/0, no value) | describe-secret Name + ARN, no version before step 2 | step 1 safe-apply of the saved plan -target=aws_secretsmanager_secret.ca_ingress_mark: 1 added 0 changed 0 destroyed at 2026-10-14T04:48Z; describe-secret Name teams/global/ingress-mark, ARN ...secret:teams/global/ingress-mark-YoDDGm, no version (saved r18/AFTER_step1_describe_secret.json) | CLOSED 20261014T045433Z |
| L2 | activation | secret value put out of band; AWSCURRENT version exists, value never read or printed, generating file deleted | describe-secret VersionIdsToStages shows AWSCURRENT (version id only) | step 2 put-secret-value from a file outside every git tree (value never printed, file deleted, confirmed absent); describe-secret shows one version id bdd58f57-f340-4883-90dd-2e3adf7ec650 staged AWSCURRENT; value never read back (saved r18/AFTER_step2_describe_secret.json) | CLOSED 20261014T045433Z |
| L3 | activation | teams-global-chat-assist-handler-lambda code: new CodeSha256 equal to the built package replacing sWltfUwyJQpANEhbY+KFkszo8ScLKEIi7Lm4qyUNWrM=, plus env key INGRESS_MARK_MODE=record | get-function-configuration CodeSha256 + LastModified + env key names | live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 nX67q2k05fh77lG2gBLsNlp6HLAZeELPq85CJpWCVhA= (was sWltfUwyJQpANEhbY+KFkszo8ScLKEIi7Lm4qyUNWrM=), LastModified 2026-10-14T04:52:10Z, CodeSize 294668, env keys 15 (14 plus INGRESS_MARK_MODE) -- equals the zip built at pin 38ce5a7981; saved r18/AFTER_handler_config.json | CLOSED 20261014T045433Z |
| L4 | activation | teams-global-chat-assist-ingress-lambda code: new CodeSha256 equal to the built package replacing sWltf..., plus env key INGRESS_MARK_MODE=record | get-function-configuration CodeSha256 + LastModified + env key names | live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 nX67q2k05fh77lG2gBLsNlp6HLAZeELPq85CJpWCVhA= (was sWltf...), LastModified 2026-10-14T04:52:16Z, CodeSize 294668, env keys 15 -- equals the zip built at pin 38ce5a7981; saved r18/AFTER_ingress_config.json | CLOSED 20261014T045433Z |
| L5 | activation | aws_iam_policy.exec Secrets statement gains exactly the new secret ARN | saved plan diff plus check_j3_live simulated read per role | saved plan JSON: aws_iam_policy.exec changed only the Secrets statement (secretsmanager:GetSecretValue) Resource, +1 arn:...:secret:teams/global/ingress-mark-YoDDGm, 14 statements before and after; applied 04:51Z; check_j3_live simulate: both roles may read the secret | CLOSED 20261014T045433Z |
| L6 | verify | CAj3-AC2 check_j3_live.py PASS plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail | CAj3-AC2 check_j3_live.py RESULT: PASS (one new package on both; served zip hash equals CodeSha256 at 294668 B; 6 files equal the pin; INGRESS_MARK_MODE=record and other keys as recorded; secret has a current version, value not read; both roles may read it; served code round-trips a mark, refuses a tampered one, parses the modes). Targeted re-plan -detailed-exitcode rc=0 'No changes' -- saved r18/CAj3_REPLAN_AFTER.txt | CLOSED 20261014T045433Z |
| L7 | verify | ingress logs show ingress_poll and mail_poll within 10 minutes of step 3 | log-line counts (no message content) | log read 2026-10-14T05:05:23Z, 13m07s after step 3: 13 ingress_poll (last 05:04:19Z), 2 mail_poll (last 05:01:21Z, failed=0 refused=0 sent=0), 0 Traceback/ERROR, 0 lines naming a secret or access error; counts only, saved r18/CAj3_L7_log_read.txt | CLOSED 20261014T050540Z |

## Log

- 20261014T044255Z OPENED by 0.7.0_AE_CloudOps~CA with 7 leg(s)
- 20261014T045433Z LEG L1 closed: step 1 safe-apply of the saved plan -target=aws_secretsmanager_secret.ca_ingress_mark: 1 added 0 changed 0 destroyed at 
- 20261014T045433Z LEG L2 closed: step 2 put-secret-value from a file outside every git tree (value never printed, file deleted, confirmed absent); descri
- 20261014T045433Z LEG L3 closed: live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 nX67q2k05fh77lG2gBLsNlp6HLAZeELPq85C
- 20261014T045433Z LEG L4 closed: live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 nX67q2k05fh77lG2gBLsNlp6HLAZeELPq85C
- 20261014T045433Z LEG L5 closed: saved plan JSON: aws_iam_policy.exec changed only the Secrets statement (secretsmanager:GetSecretValue) Resource, +1 arn
- 20261014T045433Z LEG L6 closed: CAj3-AC2 check_j3_live.py RESULT: PASS (one new package on both; served zip hash equals CodeSha256 at 294668 B; 6 files 
- 20261014T050540Z LEG L7 closed: log read 2026-10-14T05:05:23Z, 13m07s after step 3: 13 ingress_poll (last 05:04:19Z), 2 mail_poll (last 05:01:21Z, faile
- 20261014T050540Z CLOSED -- all 7 legs proven
