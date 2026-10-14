# Deploy Completion Record
**Date opened:** 2026-10-14T15:00:33.788360+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T151852Z
**Deploy:** COMM_ASSIST r18 CA-j-5: flip INGRESS_MARK_MODE record -> enforce (environment only, one key) on module.ldo_001, pinned tree 8c5e0b278e (local branch enforce-pin-j5, not on the trunk) -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~CA
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | teams-global-chat-assist-handler-lambda environment INGRESS_MARK_MODE record -> enforce; CodeSha256 unchanged (/amW90t7...) | get-function-configuration CodeSha256 + LastModified + env key names + the mode value | live get-function-configuration teams-global-chat-assist-handler-lambda: INGRESS_MARK_MODE record -> enforce, LastModified 2026-10-14T15:07:01Z, CodeSha256 /amW90t7TNsAAcx8Ap0t/eD7Jgk1HAOXJHCv8t8Mkho= UNCHANGED, CodeSize 295126, env keys 15 (names unchanged); saved r18d/AFTER_handler_config.json | CLOSED 20261014T150901Z |
| L2 | activation | teams-global-chat-assist-ingress-lambda environment INGRESS_MARK_MODE record -> enforce; CodeSha256 unchanged (/amW90t7...) | get-function-configuration CodeSha256 + LastModified + env key names + the mode value | live get-function-configuration teams-global-chat-assist-ingress-lambda: INGRESS_MARK_MODE record -> enforce, LastModified 2026-10-14T15:07:01Z, CodeSha256 /amW90t7TNsAAcx8Ap0t/eD7Jgk1HAOXJHCv8t8Mkho= UNCHANGED, CodeSize 295126, env keys 15; saved r18d/AFTER_ingress_config.json | CLOSED 20261014T150901Z |
| L3 | verify | CAj5-AC2 check_j5_live.py PASS plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail | CAj5-AC2 check_j5_live.py RESULT: PASS at ~15:08Z (one Deny statement; role allowed, both Dell users explicitDeny; management acts open; code unchanged, mode enforce in both, secret version current, value not read). Targeted re-plan -detailed-exitcode rc=0 'No changes' -- saved r18d/CAj5_REPLAN_AFTER.txt | CLOSED 20261014T150901Z |
| L4 | verify | ingress logs show ingress_poll and mail_poll within 10 minutes of the apply and no error or AccessDenied in either function log | log-line counts (no message content, secret value never read) | log read 2026-10-14T15:18:28Z, 11m27s after the apply: ingress 12 ingress_poll (last 15:18:19Z), 2 mail_poll (last 15:13:46Z, failed=0 refused=0 sent=0), 0 Traceback/ERROR, 0 AccessDenied and 0 ingress-mark lines; handler log 5 lines incl. 1 ldo_event at 15:09:49Z (the issuer's forged probe, not this seat's), 0 errors; check_j5_obs after the flip: CLEAN, 8 marks_ok, unmarked=0 on real objects, probes=1 probe_unmarked=1; counts only, saved r18d/CAj5_L4_log_read.txt | CLOSED 20261014T151851Z |

## Log

- 20261014T150033Z OPENED by 0.7.0_AE_CloudOps~CA with 4 leg(s)
- 20261014T150901Z LEG L1 closed: live get-function-configuration teams-global-chat-assist-handler-lambda: INGRESS_MARK_MODE record -> enforce, LastModifi
- 20261014T150901Z LEG L2 closed: live get-function-configuration teams-global-chat-assist-ingress-lambda: INGRESS_MARK_MODE record -> enforce, LastModifi
- 20261014T150901Z LEG L3 closed: CAj5-AC2 check_j5_live.py RESULT: PASS at ~15:08Z (one Deny statement; role allowed, both Dell users explicitDeny; manag
- 20261014T151851Z LEG L4 closed: log read 2026-10-14T15:18:28Z, 11m27s after the apply: ingress 12 ingress_poll (last 15:18:19Z), 2 mail_poll (last 15:13
- 20261014T151852Z CLOSED -- all 4 legs proven
