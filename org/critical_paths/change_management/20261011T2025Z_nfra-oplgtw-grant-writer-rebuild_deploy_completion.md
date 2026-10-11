# Deploy Completion Record
**Date opened:** 2026-10-11T20:25:19.806677+00:00
**Status:** OPEN
**Deploy:** OG-ap-9: rebuild mcportal-grant-writer-lambda from the live release so calendar_months grants stop being refused (row W42-S1)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the prior recorded and the targeted pre-apply plan captured with its exit code | prior CodeSha256 plus the prior package downloaded and hash-verified against it; W/ap9_plan_target.txt and .rc read 0 to add, 1 to change, 0 to destroy at rc=0, that address only, source_code_hash only |  | OPEN |
| L2 | activation | safe-apply of the same -target and -var from the detached box/sitez-HEAD worktree; never aws lambda update-function-code | apply completes and the live CodeSha256 moves off the prior |  | OPEN |
| L3 | verify | targeted re-plan after the apply, and W/ap9_build.json | W/ap9_replan.txt and .rc read 0/0/0 at rc=0; ap9_build.json carries the post-apply live CodeSha256 |  | OPEN |
| L4 | verify | the SESSION-FREE parse read-back (COO half condition B), each package using its OWN parse_scope | W/ap9_parse.json: deployed_accepts_13 true AND prior_accepts_13 false -- the prior package is the negative control and must REFUSE the 13-month scope |  | OPEN |
| L5 | git | lambda-source-map.json's grant-writer entry updated to the deployed build (deploy rule 4) | the commit carrying that edit |  | OPEN |

## Log

- 20261011T202519Z OPENED by 0.7.0_AE_CloudOps~Z with 5 leg(s)
