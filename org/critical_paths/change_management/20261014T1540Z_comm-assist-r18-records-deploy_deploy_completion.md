# Deploy Completion Record
**Date opened:** 2026-10-14T15:40:40.855923+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T155846Z
**Deploy:** COMM_ASSIST r18 CA-j-14: assistant mention record + mail log (channel_mentions.py, mail_requests.py, folder_records.py) onto module.ldo_001, CODE ONLY, mode stays enforce, pinned build 0774100edc -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~CA
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | teams-global-chat-assist-handler-lambda code: new CodeSha256 equal to the built package replacing /amW90t7TNsAAcx8Ap0t/eD7Jgk1HAOXJHCv8t8Mkho=; env unchanged, mode enforce | get-function-configuration CodeSha256 + LastModified + env key names + mode | live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 BBiNwhfKGcPciG5+zFa2KCIsJ/kF18g+x4ozNN2EnIA= (was /amW90t7TNsAAcx8Ap0t/eD7Jgk1HAOXJHCv8t8Mkho=), LastModified 2026-10-14T15:46:59Z, CodeSize 297733, env keys 15 unchanged, mode enforce -- equals the zip built at pin 0774100edc; saved r18e/AFTER_handler_config.json | CLOSED 20261014T154847Z |
| L2 | activation | teams-global-chat-assist-ingress-lambda code: new CodeSha256 equal to the built package replacing /amW90t7...; env unchanged, mode enforce | get-function-configuration CodeSha256 + LastModified + env key names + mode | live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 BBiNwhfKGcPciG5+zFa2KCIsJ/kF18g+x4ozNN2EnIA= (was /amW90t7...), LastModified 2026-10-14T15:47:05Z, CodeSize 297733, env keys 15 unchanged, mode enforce -- equals the zip built at pin 0774100edc; saved r18e/AFTER_ingress_config.json | CLOSED 20261014T154847Z |
| L3 | verify | CAj14-AC2 check_k3_live.py PASS plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail | CAj14-AC2 check_k3_live.py RESULT: PASS at ~15:48Z (one new package on both; served zip hash equals CodeSha256 at 297733 B; 8 files equal the pin; INGRESS_MARK_MODE=enforce and other keys as recorded; secret current version, value not read; both roles may read it; served code: mark checks, snippet_clean, mention_record, mail_record all True). Targeted re-plan -detailed-exitcode rc=0 'No changes' -- saved r18e/CAj14_REPLAN_AFTER.txt | CLOSED 20261014T154847Z |
| L4 | verify | ingress logs show ingress_poll and mail_poll within 10 minutes, no error or AccessDenied in either function log, and the dead-letter queue counts unchanged from BEFORE | log-line counts + sqs get-queue-attributes (no message content, secret value never read) | log read 2026-10-14T15:58:21Z, 11m16s after the apply: ingress 11 ingress_poll (last 15:57:18Z), 2 mail_poll (last 15:56:48Z: listed=3 fetched=1 sent=1 refused=0 failed=0), 0 Traceback/ERROR, 0 AccessDenied and 0 ingress-mark lines; handler log 7 lines: 1 ldo_event (1165 ms) and 1 mail_considered with body_no_andrew=1 at 15:56:41Z, i.e. one real mail event ran through the new code and was not texted, so the mail-log writer (texted branch only) did NOT run; 0 errors. Dead-letter queue ApproximateNumberOfMessages 0, NotVisible 0, Delayed 0 -- UNCHANGED from BEFORE (0/0/0). check_j5_obs after: CLEAN, marks_ok 9, unmarked 0, probes=1 probe_unmarked=1. Counts only, saved r18e/CAj14_L4_log_read.txt | CLOSED 20261014T155845Z |

## Log

- 20261014T154040Z OPENED by 0.7.0_AE_CloudOps~CA with 4 leg(s)
- 20261014T154847Z LEG L1 closed: live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 BBiNwhfKGcPciG5+zFa2KCIsJ/kF18g+x4oz
- 20261014T154847Z LEG L2 closed: live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 BBiNwhfKGcPciG5+zFa2KCIsJ/kF18g+x4oz
- 20261014T154847Z LEG L3 closed: CAj14-AC2 check_k3_live.py RESULT: PASS at ~15:48Z (one new package on both; served zip hash equals CodeSha256 at 297733
- 20261014T155845Z LEG L4 closed: log read 2026-10-14T15:58:21Z, 11m16s after the apply: ingress 11 ingress_poll (last 15:57:18Z), 2 mail_poll (last 15:56
- 20261014T155846Z CLOSED -- all 4 legs proven
