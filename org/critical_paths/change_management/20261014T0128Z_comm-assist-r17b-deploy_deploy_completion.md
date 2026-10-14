# Deploy Completion Record
**Date opened:** 2026-10-14T01:28:03.199922+00:00
**Status:** OPEN
**Deploy:** COMM_ASSIST r17 CA-i-12: replay fix (tenant.py only) onto module.ldo_001, CODE ONLY, pinned build 8a480805e5 -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~CA
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | teams-global-chat-assist-handler-lambda code: new CodeSha256 equal to the built package, replacing lRKObLMbn1kTWSXtohLxZ33HYVq7aBd1o/fjLfaA1Rw=; env unchanged | get-function-configuration CodeSha256 + LastModified + env key names |  | OPEN |
| L2 | activation | teams-global-chat-assist-ingress-lambda code: new CodeSha256 equal to the built package, replacing lRKObLMbn1kTWSXtohLxZ33HYVq7aBd1o/fjLfaA1Rw=; env unchanged | get-function-configuration CodeSha256 + LastModified + env key names |  | OPEN |
| L3 | verify | CAi12-AC2 check_i12_live.py PASS plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail |  | OPEN |
| L4 | verify | ingress logs show ingress_poll and mail_poll within 10 minutes of the apply | log-line counts (no message content) |  | OPEN |

## Log

- 20261014T012803Z OPENED by 0.7.0_AE_CloudOps~CA with 4 leg(s)
