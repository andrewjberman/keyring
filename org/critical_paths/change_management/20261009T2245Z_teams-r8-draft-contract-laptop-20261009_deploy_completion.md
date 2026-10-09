# Deploy Completion Record
**Date opened:** 2026-10-09T22:45:18.060263+00:00
**Status:** OPEN
**Deploy:** TO31 NFRA_CTLPLN INBOUND r8 CT-i-14: ONE targeted apply of module.ldo_001 in infra/aws/terraform/transcripts, CODE ONLY, function families teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda; rollback = saved live package op92gM7r... re-applied on the same target
**Authored by:** 0.7.0_AE_CloudOps~CTL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | targeted safe-apply of module.ldo_001 (handler + ingress[0]) in infra/aws/terraform/transcripts | Branch A plan 0 add 2 change 0 destroy, source_code_hash/last_modified only; Apply complete 0 added 2 changed 0 destroyed; CloudTrail UpdateFunctionCode event time per function |  | OPEN |
| L2 | verify | live read-back of both CodeSha256 against the built package + targeted re-plan | both live CodeSha256 equal the built package's sha256_base64; targeted plan -detailed-exitcode exit=0 no changes |  | OPEN |
| L3 | verify | five minutes of ingress log lines by event, counts only | ingress_poll lines continue with polls>0 and ingress_step_failed=0, positive control REPORT>0; channel_poll failed is pre-existing |  | OPEN |

## Log

- 20261009T224518Z OPENED by 0.7.0_AE_CloudOps~CTL with 3 leg(s)
