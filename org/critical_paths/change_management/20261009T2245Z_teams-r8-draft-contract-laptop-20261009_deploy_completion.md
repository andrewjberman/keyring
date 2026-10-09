# Deploy Completion Record
**Date opened:** 2026-10-09T22:45:18.060263+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T230921Z
**Deploy:** TO31 NFRA_CTLPLN INBOUND r8 CT-i-14: ONE targeted apply of module.ldo_001 in infra/aws/terraform/transcripts, CODE ONLY, function families teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda; rollback = saved live package op92gM7r... re-applied on the same target
**Authored by:** 0.7.0_AE_CloudOps~CTL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | targeted safe-apply of module.ldo_001 (handler + ingress[0]) in infra/aws/terraform/transcripts | Branch A plan 0 add 2 change 0 destroy, source_code_hash/last_modified only; Apply complete 0 added 2 changed 0 destroyed; CloudTrail UpdateFunctionCode event time per function | Branch A met exactly and machine-verified: targeted plan 0 to add, 2 to change, 0 to destroy on module.ldo_001.aws_lambda_function.handler and .ingress[0]; check_plan.py asserts actions=[update], changed keys subset {source_code_hash,last_modified}, after hash SFSTGBQX3r49t2YXSrN+6t6Ekmz1NrpxkjX09VHLZEM= equal to the built package, no unexpected computed values, no environment change. ONE safe-apply of the SAVED plan with the same target and TF_DATA_DIR (fresh dir outside every git tree; init without -reconfigure): Apply complete 0 added, 2 changed, 0 destroyed at 23:03:19Z. Live LastModified handler 23:03:08Z, ingress 23:03:14Z. DEVIATION REPORTED, not hidden: the root's foreign variable second_reader_trust_principal_arns (no default by design, readers.tf) was passed as the ONE -var at its LIVE value read at the act (role CreateDate 09:55:13Z), the issuer's own A3 method on CA-d-2; TO-31 names no -var, so it is the issuer's to grade. It widened nothing. Hour sent to the issuer at 23:04:44Z before any proof work. | CLOSED 20261009T230719Z |
| L2 | verify | live read-back of both CodeSha256 against the built package + targeted re-plan | both live CodeSha256 equal the built package's sha256_base64; targeted plan -detailed-exitcode exit=0 no changes | Both live CodeSha256 equal the built package's sha256_base64 SFSTGBQX3r49t2YXSrN+6t6Ekmz1NrpxkjX09VHLZEM= (read_evidence after: matches=true; built 32 files, 268046 bytes, sha256 485493181417debe3db766174ab37eeade84926cf536ba719235f4f551cb6443). Targeted re-plan with the same target and the same one -var: exit=0, 'No changes. Your infrastructure matches the configuration.' | CLOSED 20261009T230719Z |
| L3 | verify | five minutes of ingress log lines by event, counts only | ingress_poll lines continue with polls>0 and ingress_step_failed=0, positive control REPORT>0; channel_poll failed is pre-existing | Five minutes 23:03:14Z-23:08:14Z on the ingress log group: 27 lines, positive control REPORT=5 (non-zero, so the filter demonstrably sees lines). ingress_poll=5 and all 5 carry the new fields (chats_read, pages, messages); failed_steps={} so ingress_step_failed=0; mail_poll=1. channel_poll=5 with the failed field set on all 5 -- the PRE-EXISTING condition the order and both halves name ('channel_poll failed=1' is the FIELD's value per poll, not a count of one; the r7 predecessor recorded the same as 'channel_poll failed=5 expected until gateway release'). No function invoked, no test event, text or bus line sent, no message content read. Counts only. | CLOSED 20261009T230921Z |

## Log

- 20261009T224518Z OPENED by 0.7.0_AE_CloudOps~CTL with 3 leg(s)
- 20261009T230719Z LEG L1 closed: Branch A met exactly and machine-verified: targeted plan 0 to add, 2 to change, 0 to destroy on module.ldo_001.aws_lambd
- 20261009T230719Z LEG L2 closed: Both live CodeSha256 equal the built package's sha256_base64 SFSTGBQX3r49t2YXSrN+6t6Ekmz1NrpxkjX09VHLZEM= (read_evidence
- 20261009T230921Z LEG L3 closed: Five minutes 23:03:14Z-23:08:14Z on the ingress log group: 27 lines, positive control REPORT=5 (non-zero, so the filter 
- 20261009T230921Z CLOSED -- all 3 legs proven
