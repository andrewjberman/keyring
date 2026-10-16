# Deploy Completion Record
**Date opened:** 2026-10-16T22:03:45.759687+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T222916Z
**Deploy:** COMM_ASSIST r21 CA-n-2: channel poller reads replies in older threads (channel_mentions.py +83 -8) onto module.ldo_001, CODE ONLY, mode stays enforce, pinned build 1aa63bde67 -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~COMM1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | teams-global-chat-assist-handler-lambda code: new CodeSha256 equal to the built 34-file package replacing gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok=; env unchanged, mode enforce | get-function-configuration CodeSha256 + LastModified + env key names + mode | live get-function-configuration teams-global-chat-assist-handler-lambda read 2026-10-16T22:14Z: CodeSha256 RoH5DIiH/lWEutB+Qb3CswFUB402LhOjbx6P5sbk2DE= (was gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok=), LastModified 2026-10-16T22:13:25Z, CodeSize 238923, 34-file package built at pin 1aa63bde67, env keys 15 same names as BEFORE, mode enforce; saved r21/AFTER_handler_config.json | CLOSED 20261016T222915Z |
| L2 | activation | teams-global-chat-assist-ingress-lambda code: new CodeSha256 equal to the built 34-file package replacing gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok=; env unchanged, mode enforce | get-function-configuration CodeSha256 + LastModified + env key names + mode | live get-function-configuration teams-global-chat-assist-ingress-lambda read 2026-10-16T22:14Z: CodeSha256 RoH5DIiH/lWEutB+Qb3CswFUB402LhOjbx6P5sbk2DE= (was gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok=), LastModified 2026-10-16T22:13:31Z, CodeSize 238923, env keys 15 same names as BEFORE, mode enforce; saved r21/AFTER_ingress_config.json | CLOSED 20261016T222916Z |
| L3 | verify | CAn2-AC2 check_n2_equiv.py N2-LIVE ok=True plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail | CAn2-AC2 check_n2_equiv.py N2_MODE=live read N2-LIVE ok=True differ=0 foreign=0 probes=17 same=17 n1=8 of 8 at ~22:14Z (saved r21/AC2_AFTER.txt). Targeted re-plan of module.ldo_001 -detailed-exitcode rc=0 'No changes' (saved r21/CAn2_REPLAN_AFTER.txt). AC1 N2-EQUIV ok=True differ=4 foreign=3 probes=17 same=17 n1=8 of 8 before the apply (r21/AC1_BEFORE.txt) | CLOSED 20261016T222916Z |
| L4 | verify | ingress logs show channel_poll calls at most 20, ingress_poll and mail polled within 10 minutes, no error or AccessDenied in either function log, dead-letter queue counts unchanged from BEFORE | log-line counts + sqs get-queue-attributes (no message content, secret value never read) | log read 2026-10-16T22:26Z, 13m after the apply: ingress 13 channel_poll (calls 0, 6 or 12, max 12 of 20; failed 0 on all 13), 13 ingress_poll, 2 mail_poll (22:17:21, 22:22:21; failed 0, refused 0); 0 Traceback/ERROR/AccessDenied; handler log 0 events. DLQ ApproximateNumberOfMessages 0, NotVisible 0, Delayed 0 -- UNCHANGED from BEFORE (0/0/0). Counts only, saved r21/CAn2_L4_log_read.txt, r21/L4_dlq_at_10min.json | CLOSED 20261016T222916Z |

## Log

- 20261016T220345Z OPENED by 0.7.0_AE_CloudOps~COMM1 with 4 leg(s)
- 20261016T222915Z LEG L1 closed: live get-function-configuration teams-global-chat-assist-handler-lambda read 2026-10-16T22:14Z: CodeSha256 RoH5DIiH/lWEu
- 20261016T222916Z LEG L2 closed: live get-function-configuration teams-global-chat-assist-ingress-lambda read 2026-10-16T22:14Z: CodeSha256 RoH5DIiH/lWEu
- 20261016T222916Z LEG L3 closed: CAn2-AC2 check_n2_equiv.py N2_MODE=live read N2-LIVE ok=True differ=0 foreign=0 probes=17 same=17 n1=8 of 8 at ~22:14Z (
- 20261016T222916Z LEG L4 closed: log read 2026-10-16T22:26Z, 13m after the apply: ingress 13 channel_poll (calls 0, 6 or 12, max 12 of 20; failed 0 on al
- 20261016T222916Z CLOSED -- all 4 legs proven
