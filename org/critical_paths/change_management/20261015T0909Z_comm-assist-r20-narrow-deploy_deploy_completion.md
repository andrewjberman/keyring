# Deploy Completion Record
**Date opened:** 2026-10-15T09:09:40.788620+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T093029Z
**Deploy:** COMM_ASSIST r20 CA-l-4: narrower package (registry files 17 to 12, zip 39 to 34 files) onto module.ldo_001, CODE ONLY, mode stays enforce, pinned build 863dc0f739 -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~CA
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | teams-global-chat-assist-handler-lambda code: new CodeSha256 equal to the built 34-file package replacing nQlJW0j/a2nE1om0ZbXm9CTMxAVDXwUQNju62S4xa9k=; env unchanged, mode enforce | get-function-configuration CodeSha256 + LastModified + env key names + mode | live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok= (was nQlJW0j...), LastModified 2026-10-15T09:18:48Z, CodeSize 235445, 34-file package, env keys 15 unchanged, mode enforce -- equals the zip built at pin 863dc0f739; saved r20/AFTER_handler_config.json | CLOSED 20261015T093029Z |
| L2 | activation | teams-global-chat-assist-ingress-lambda code: new CodeSha256 equal to the built 34-file package replacing nQlJW0j...; env unchanged, mode enforce | get-function-configuration CodeSha256 + LastModified + env key names + mode | live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok= (was nQlJW0j...), LastModified 2026-10-15T09:18:55Z, CodeSize 235445, env keys 15 unchanged, mode enforce -- equals the zip built at pin 863dc0f739; saved r20/AFTER_ingress_config.json | CLOSED 20261015T093029Z |
| L3 | verify | CAl4-AC2 check_m4_live.py PASS plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail | CAl4-AC2 check_m4_live.py RESULT: PASS at ~09:20Z (one new package on both, 34 files, 8 contract files equal the pin, 12 served registry files equal the manifest and none of the five dropped files served, mode enforce and 15 key names, secret current version value not read, both roles may read it, two-mail pending_list probe True, 17 probes equal). Targeted re-plan -detailed-exitcode rc=0 No changes -- saved r20/CAl4_REPLAN_AFTER.txt. AC1 M4-EQUIV ok=True dropped=5 foreign=2 probes=17 same=17 and C1 M4-SCAN ok=True before the apply | CLOSED 20261015T093029Z |
| L4 | verify | ingress logs show ingress_poll and mail poll within 10 minutes, no error or AccessDenied in either function log, dead-letter queue counts unchanged from BEFORE (0/0/0) | log-line counts + sqs get-queue-attributes (no message content, secret value never read) | log read 2026-10-15T09:29:38Z, 10m39s after the apply: ingress 11 ingress_poll (last 09:29:19Z), 2 mail_poll (last 09:25:39Z), 0 Traceback/ERROR, 0 AccessDenied; handler log 0 lines, 0 errors. Dead-letter queue ApproximateNumberOfMessages 0, NotVisible 0, Delayed 0 -- UNCHANGED from BEFORE (0/0/0). check_j5_obs after: CLEAN, marks_ok 10, unmarked 0. Counts only, saved r20/CAl4_L4_log_read.txt | CLOSED 20261015T093029Z |

## Log

- 20261015T090940Z OPENED by 0.7.0_AE_CloudOps~CA with 4 leg(s)
- 20261015T093029Z LEG L1 closed: live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mme
- 20261015T093029Z LEG L2 closed: live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mme
- 20261015T093029Z LEG L3 closed: CAl4-AC2 check_m4_live.py RESULT: PASS at ~09:20Z (one new package on both, 34 files, 8 contract files equal the pin, 12
- 20261015T093029Z LEG L4 closed: log read 2026-10-15T09:29:38Z, 10m39s after the apply: ingress 11 ingress_poll (last 09:29:19Z), 2 mail_poll (last 09:25
- 20261015T093029Z CLOSED -- all 4 legs proven
