# Deploy Completion Record
**Date opened:** 2026-10-11T02:01:56.894653+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T022427Z
**Deploy:** COMM_ASSIST r14 CA-f-1: round-13 package onto module.ldo_001, code only, pinned build 2fd32e12c2 -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~CA
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | teams-global-chat-assist-handler-lambda code: new CodeSha256 equal to the built package, replacing SFSTGBQX3r49t2YXSrN+6t6Ekmz1NrpxkjX09VHLZEM= | get-function-configuration CodeSha256 + LastModified | live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 nIQW+3XvvaFNJQfwX5lrI99XSexESb68Pd1uLldlTgI= (was SFSTGBQX3r49t2YXSrN+6t6Ekmz1NrpxkjX09VHLZEM=), LastModified 2026-10-11T02:16:55.000+0000, CodeSize 269206 -- equals the zip built at pin 2fd32e12c2; saved AFTER_teams-global-chat-assist-handler-lambda_config.json | CLOSED 20261011T022000Z |
| L2 | activation | teams-global-chat-assist-ingress-lambda code: new CodeSha256 equal to the built package, replacing SFSTGBQX3r49t2YXSrN+6t6Ekmz1NrpxkjX09VHLZEM= | get-function-configuration CodeSha256 + LastModified | live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 nIQW+3XvvaFNJQfwX5lrI99XSexESb68Pd1uLldlTgI= (was SFSTGBQX3r49t2YXSrN+6t6Ekmz1NrpxkjX09VHLZEM=), LastModified 2026-10-11T02:17:01.000+0000, CodeSize 269206 -- equals the zip built at pin 2fd32e12c2; saved AFTER_teams-global-chat-assist-ingress-lambda_config.json | CLOSED 20261011T022000Z |
| L3 | verify | CAf1-AC1 d1_live.py PASS plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail | CAf1-AC1 d1_live.py RESULT: PASS (both functions on one new package; served zip hash equals CodeSha256 at 269206 B; both round-13 files byte-equal the pin; served code returns exactly the five party keys against a synthetic registry carrying a sixth). Targeted re-plan -target=module.ldo_001 -detailed-exitcode rc=0 'No changes.' -- saved CAf1_REPLAN_AFTER.txt | CLOSED 20261011T022000Z |
| L4 | verify | CAf1-AC2 d1_errorfield.py PASS within 10 minutes of the apply | check output | CAf1-AC2 d1_errorfield.py RESULT: PASS at 2026-10-11T02:21:56Z, window start = ingress LastModified 02:17:01Z. COUNTS channel_poll=5 failed>0=5 with_error=5 ingress_step_failed[channels]=5 -- readable-and-escalated=True. Base was 60 channel_poll / 60 failed / 0 with error / 0 step_failed. Condition 3's remaining clauses also measured: ingress_poll continues (6 lines, chats_read=2) and mail_poll logged; ingress_step_failed is channels-only, never mail. | CLOSED 20261011T022356Z |

## Log

- 20261011T020156Z OPENED by 0.7.0_AE_CloudOps~CA with 4 leg(s)
- 20261011T022000Z LEG L1 closed: live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 nIQW+3XvvaFNJQfwX5lrI99XSexESb68Pd1u
- 20261011T022000Z LEG L2 closed: live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 nIQW+3XvvaFNJQfwX5lrI99XSexESb68Pd1u
- 20261011T022000Z LEG L3 closed: CAf1-AC1 d1_live.py RESULT: PASS (both functions on one new package; served zip hash equals CodeSha256 at 269206 B; both
- 20261011T022356Z LEG L4 closed: CAf1-AC2 d1_errorfield.py RESULT: PASS at 2026-10-11T02:21:56Z, window start = ingress LastModified 02:17:01Z. COUNTS ch
- 20261011T022427Z CLOSED -- all 4 legs proven
