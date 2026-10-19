# Deploy Completion Record
**Date opened:** 2026-10-19T17:34:00.138327+00:00
**Status:** OPEN
**Deploy:** COMM_ASSIST r22 CA-p-2: mail handler refuses mail Andrew sent (mail_requests.py +17 -5) onto module.ldo_001, CODE ONLY, mode stays enforce, pinned build e6c37673c8 -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~COMM1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | teams-global-chat-assist-handler-lambda code: new CodeSha256 equal to the built 34-file package p4kaI5t0i6vgzAZ0xONR/e8G9iDBU3icKNb3PvUdGEg= replacing RoH5DIiH/lWEutB+Qb3CswFUB402LhOjbx6P5sbk2DE=; env unchanged, mode enforce | get-function-configuration CodeSha256 + LastModified + env key names + mode | live get-function-configuration teams-global-chat-assist-handler-lambda read 2026-10-19T17:44Z: CodeSha256 p4kaI5t0i6vgzAZ0xONR/e8G9iDBU3icKNb3PvUdGEg= (was RoH5DIiH/lWEutB+Qb3CswFUB402LhOjbx6P5sbk2DE=), LastModified 2026-10-19T17:43:55Z, CodeSize 241267, 34-file package built at pin e6c37673c8, env keys 15 same names as BEFORE, mode enforce; saved r22/AFTER_handler_config.json | CLOSED 20261019T175324Z |
| L2 | activation | teams-global-chat-assist-ingress-lambda code: new CodeSha256 equal to the built 34-file package replacing RoH5DIiH/lWEutB+Qb3CswFUB402LhOjbx6P5sbk2DE=; env unchanged, mode enforce | get-function-configuration CodeSha256 + LastModified + env key names + mode | live get-function-configuration teams-global-chat-assist-ingress-lambda read 2026-10-19T17:44Z: CodeSha256 p4kaI5t0i6vgzAZ0xONR/e8G9iDBU3icKNb3PvUdGEg= (was RoH5DIiH/lWEutB+Qb3CswFUB402LhOjbx6P5sbk2DE=), LastModified 2026-10-19T17:43:49Z, CodeSize 241267, env keys 15 same names as BEFORE, mode enforce; saved r22/AFTER_ingress_config.json | CLOSED 20261019T175324Z |
| L3 | verify | CAp2-AC2 check_p2_equiv.py P2-LIVE ok=True plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail | CAp2-AC2 check_p2_equiv.py P2_MODE=live read P2-LIVE ok=True differ=0 foreign=0 probes=17 same=17 p1=6 of 6 at ~17:44Z (saved r22/AC2_AFTER.txt). Targeted re-plan of module.ldo_001 -detailed-exitcode rc=0 'No changes' (r22/CAp2_REPLAN_AFTER.txt). AC1 P2-EQUIV ok=True differ=5 foreign=4 probes=17 same=17 p1=6 of 6 before the apply (r22/AC1_BEFORE.txt). Saved plan graded Branch A (r22/CAp2_PLAN_BRANCH.summary.json). DLQ 0/0/0 before and after. | CLOSED 20261019T175324Z |
| L4 | verify | ingress logs show channel_poll calls at most 20, ingress_poll and mail polled within 10 minutes, no error/AccessDenied/me-without-mail in either function log, dead-letter queue counts unchanged from BEFORE | log-line counts + sqs get-queue-attributes (no message content, secret value never read) |  | OPEN |

## Log

- 20261019T173400Z OPENED by 0.7.0_AE_CloudOps~COMM1 with 4 leg(s)
- 20261019T175324Z LEG L1 closed: live get-function-configuration teams-global-chat-assist-handler-lambda read 2026-10-19T17:44Z: CodeSha256 p4kaI5t0i6vgz
- 20261019T175324Z LEG L2 closed: live get-function-configuration teams-global-chat-assist-ingress-lambda read 2026-10-19T17:44Z: CodeSha256 p4kaI5t0i6vgz
- 20261019T175324Z LEG L3 closed: CAp2-AC2 check_p2_equiv.py P2_MODE=live read P2-LIVE ok=True differ=0 foreign=0 probes=17 same=17 p1=6 of 6 at ~17:44Z (
