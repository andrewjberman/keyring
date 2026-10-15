# Deploy Completion Record
**Date opened:** 2026-10-15T05:38:33.683970+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T060833Z
**Deploy:** COMM_ASSIST r19 CA-k-4: mail object's list of open drafts (mail_requests.py, tenant.py) onto module.ldo_001, CODE ONLY, mode stays enforce, pinned build 93a3f55d25 -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~CA
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | teams-global-chat-assist-handler-lambda code: new CodeSha256 equal to the built package replacing BBiNwhfKGcPciG5+zFa2KCIsJ/kF18g+x4ozNN2EnIA=; env unchanged, mode enforce | get-function-configuration CodeSha256 + LastModified + env key names + mode | live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 nQlJW0j/a2nE1om0ZbXm9CTMxAVDXwUQNju62S4xa9k= (was BBiNwhfK...), LastModified 2026-10-15T05:56:32Z, CodeSize 320236, env keys 15 unchanged, mode enforce -- equals the zip built at pin 93a3f55d25; saved r19/AFTER_handler_config.json | CLOSED 20261015T060832Z |
| L2 | activation | teams-global-chat-assist-ingress-lambda code: new CodeSha256 equal to the built package replacing BBiNwhfK...; env unchanged, mode enforce | get-function-configuration CodeSha256 + LastModified + env key names + mode | live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 nQlJW0j/a2nE1om0ZbXm9CTMxAVDXwUQNju62S4xa9k= (was BBiNwhfK...), LastModified 2026-10-15T05:56:24Z, CodeSize 320236, env keys 15 unchanged, mode enforce -- equals the zip built at pin 93a3f55d25; saved r19/AFTER_ingress_config.json | CLOSED 20261015T060832Z |
| L3 | verify | CAk4-AC2 check_l4_live.py PASS plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail | CAk4-AC2 check_l4_live.py RESULT: PASS at ~05:58Z (one new package on both, 39 served files equal the pin, mode enforce and 15 key names, secret current version value not read, both roles may read it, served code keeps both of two mails in pending_list). Targeted re-plan -detailed-exitcode rc=0 'No changes' -- saved r19/CAk4_REPLAN_AFTER.txt; AC1 K4-EQUIV ok=True 17 of 17 probes before the apply | CLOSED 20261015T060833Z |
| L4 | verify | ingress logs show ingress_poll and mail poll within 10 minutes, no error or AccessDenied in either function log, dead-letter queue counts unchanged from BEFORE (0/0/0) | log-line counts + sqs get-queue-attributes (no message content, secret value never read) | log read 2026-10-15T06:07:34Z, 11m after the apply: ingress 11 ingress_poll (last 06:07:19Z), 2 mail_poll (last 06:05:21Z), 0 Traceback/ERROR, 0 AccessDenied; handler log 0 lines, 0 errors. Dead-letter queue ApproximateNumberOfMessages 0, NotVisible 0, Delayed 0 -- UNCHANGED from BEFORE (0/0/0). check_j5_obs after: CLEAN, marks_ok 10, unmarked 0. Counts only, saved r19/CAk4_L4_log_read.txt | CLOSED 20261015T060833Z |

## Log

- 20261015T053833Z OPENED by 0.7.0_AE_CloudOps~CA with 4 leg(s)
- 20261015T060832Z LEG L1 closed: live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 nQlJW0j/a2nE1om0ZbXm9CTMxAVDXwUQNju6
- 20261015T060832Z LEG L2 closed: live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 nQlJW0j/a2nE1om0ZbXm9CTMxAVDXwUQNju6
- 20261015T060833Z LEG L3 closed: CAk4-AC2 check_l4_live.py RESULT: PASS at ~05:58Z (one new package on both, 39 served files equal the pin, mode enforce 
- 20261015T060833Z LEG L4 closed: log read 2026-10-15T06:07:34Z, 11m after the apply: ingress 11 ingress_poll (last 06:07:19Z), 2 mail_poll (last 06:05:21
- 20261015T060833Z CLOSED -- all 4 legs proven
