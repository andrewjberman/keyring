# Deploy Completion Record
**Date opened:** 2026-10-14T01:28:03.199922+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T014556Z
**Deploy:** COMM_ASSIST r17 CA-i-12: replay fix (tenant.py only) onto module.ldo_001, CODE ONLY, pinned build 8a480805e5 -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~CA
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | teams-global-chat-assist-handler-lambda code: new CodeSha256 equal to the built package, replacing lRKObLMbn1kTWSXtohLxZ33HYVq7aBd1o/fjLfaA1Rw=; env unchanged | get-function-configuration CodeSha256 + LastModified + env key names | live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 eH3nihM/lYGRWi/ZgQE7uyWW2bZP0OLh4PXJ2MZSX5s= (was lRKObLMbn1kTWSXtohLxZ33HYVq7aBd1o/fjLfaA1Rw=), LastModified 2026-10-14T01:33:10Z, CodeSize 291779, env keys 14 unchanged -- equals the zip built at pin 8a480805e5; saved r17b/AFTER_handler_config.json | CLOSED 20261014T013428Z |
| L2 | activation | teams-global-chat-assist-ingress-lambda code: new CodeSha256 equal to the built package, replacing lRKObLMbn1kTWSXtohLxZ33HYVq7aBd1o/fjLfaA1Rw=; env unchanged | get-function-configuration CodeSha256 + LastModified + env key names | live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 eH3nihM/lYGRWi/ZgQE7uyWW2bZP0OLh4PXJ2MZSX5s= (was lRKOb...), LastModified 2026-10-14T01:33:04Z, CodeSize 291779, env keys 14 unchanged -- equals the zip built at pin 8a480805e5; saved r17b/AFTER_ingress_config.json | CLOSED 20261014T013428Z |
| L3 | verify | CAi12-AC2 check_i12_live.py PASS plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail | CAi12-AC2 check_i12_live.py RESULT: PASS (one new package on both; served zip hash equals CodeSha256 at 291779 B; four files equal the pin; muse key fingerprint, mail secret and SMS origination as recorded; served code routes muse.reply, accepts a real signature, refuses another key, stamps ldo-001, refuses a payload without version, carries seq, holds the acted-set guard). Targeted re-plan -detailed-exitcode rc=0 'No changes' -- saved r17b/CAi12_REPLAN_AFTER.txt | CLOSED 20261014T013428Z |
| L4 | verify | ingress logs show ingress_poll and mail_poll within 10 minutes of the apply | log-line counts (no message content) | log read 2026-10-14T01:45:33Z, 12m29s after the apply: 13 ingress_poll (last 01:45:19Z), 3 mail_poll (last 01:44:48Z, failed=0 refused=0 sent=0), 0 Traceback/ERROR; counts only, saved r17b/CAi12_L4_log_read.txt | CLOSED 20261014T014556Z |

## Log

- 20261014T012803Z OPENED by 0.7.0_AE_CloudOps~CA with 4 leg(s)
- 20261014T013428Z LEG L1 closed: live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 eH3nihM/lYGRWi/ZgQE7uyWW2bZP0OLh4PXJ
- 20261014T013428Z LEG L2 closed: live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 eH3nihM/lYGRWi/ZgQE7uyWW2bZP0OLh4PXJ
- 20261014T013428Z LEG L3 closed: CAi12-AC2 check_i12_live.py RESULT: PASS (one new package on both; served zip hash equals CodeSha256 at 291779 B; four f
- 20261014T014556Z LEG L4 closed: log read 2026-10-14T01:45:33Z, 12m29s after the apply: 13 ingress_poll (last 01:45:19Z), 3 mail_poll (last 01:44:48Z, fa
- 20261014T014556Z CLOSED -- all 4 legs proven
