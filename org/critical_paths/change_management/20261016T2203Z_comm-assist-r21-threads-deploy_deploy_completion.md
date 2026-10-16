# Deploy Completion Record
**Date opened:** 2026-10-16T22:03:45.759687+00:00
**Status:** OPEN
**Deploy:** COMM_ASSIST r21 CA-n-2: channel poller reads replies in older threads (channel_mentions.py +83 -8) onto module.ldo_001, CODE ONLY, mode stays enforce, pinned build 1aa63bde67 -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~COMM1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | teams-global-chat-assist-handler-lambda code: new CodeSha256 equal to the built 34-file package replacing gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok=; env unchanged, mode enforce | get-function-configuration CodeSha256 + LastModified + env key names + mode |  | OPEN |
| L2 | activation | teams-global-chat-assist-ingress-lambda code: new CodeSha256 equal to the built 34-file package replacing gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok=; env unchanged, mode enforce | get-function-configuration CodeSha256 + LastModified + env key names + mode |  | OPEN |
| L3 | verify | CAn2-AC2 check_n2_equiv.py N2-LIVE ok=True plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail |  | OPEN |
| L4 | verify | ingress logs show channel_poll calls at most 20, ingress_poll and mail polled within 10 minutes, no error or AccessDenied in either function log, dead-letter queue counts unchanged from BEFORE | log-line counts + sqs get-queue-attributes (no message content, secret value never read) |  | OPEN |

## Log

- 20261016T220345Z OPENED by 0.7.0_AE_CloudOps~COMM1 with 4 leg(s)
