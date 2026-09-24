# Deploy Completion Record
**Date opened:** 2026-09-24T01:50:37.496590+00:00
**Status:** OPEN
**Deploy:** IRPT resident cutover infrastructure half: runner resident policy + host running (plan 04c77cbe / 9b6e6fa98e; CTO GO 99936, Y 99916)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply of the SAVED plan 04c77cbe only (1 create / 1 update / 16 no-op) | apply output line + sha of the apply output |  | OPEN |
| P1 | verify | get-role-policy irpt-ycharts-runner-resident-policy equals the decoded document (6 statements, resource lists equal) | decoded policy diff |  | OPEN |
| I1 | verify | describe-instance-status i-0167fd745ad906a66 running; AutoShutdown=disabled tag present | readback lines |  | OPEN |
| V1 | verify | re-plan ycharts root -detailed-exitcode rc 0; recorder | plan rc line |  | OPEN |
| C1 | verify | cutover receipt with MEASURED booleans (legacy probe off, per-job power cycle off, no other queue consumers, factory installed, enrolled_user_id pinned) | receipt path + sha |  | OPEN |

## Log

- 20260924T015037Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
