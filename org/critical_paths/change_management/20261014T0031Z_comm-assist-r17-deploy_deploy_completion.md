# Deploy Completion Record
**Date opened:** 2026-10-14T00:31:56.277347+00:00
**Status:** OPEN
**Deploy:** COMM_ASSIST r17 CA-i-4: round-17 package onto module.ldo_001, code plus ONE environment value (MUSE_ANSWER_PUBKEY), pinned build b19849b51c -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~CA
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | teams-global-chat-assist-handler-lambda code: new CodeSha256 equal to the built package, replacing nIQW+3XvvaFNJQfwX5lrI99XSexESb68Pd1uLldlTgI=, plus env key MUSE_ANSWER_PUBKEY | get-function-configuration CodeSha256 + LastModified + env key names |  | OPEN |
| L2 | activation | teams-global-chat-assist-ingress-lambda code: new CodeSha256 equal to the built package, replacing nIQW+3XvvaFNJQfwX5lrI99XSexESb68Pd1uLldlTgI=, plus env key MUSE_ANSWER_PUBKEY | get-function-configuration CodeSha256 + LastModified + env key names |  | OPEN |
| L3 | verify | CAi4-AC2 check_i4_live.py PASS plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail |  | OPEN |
| L4 | verify | ingress logs show ingress_poll and mail step polled within 10 minutes of the apply | log-line counts (no message content) |  | OPEN |

## Log

- 20261014T003156Z OPENED by 0.7.0_AE_CloudOps~CA with 4 leg(s)
