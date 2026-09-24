# Deploy Completion Record
**Date opened:** 2026-09-24T05:10:03.566175+00:00
**Status:** OPEN
**Deploy:** irpt-directory-search option-B keep-warm: one rule, three concurrent targets (replaces the scheduler) + served.py warm hold @9cf6a63d6f (CRO e1476853c9, CTO GO 100264)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | directory root: rule + 3 targets + permission created, scheduler + role + policy destroyed, function updated | safe-apply of saved plan ea0921b91e 5/1/3, readback CodeSha256 o9Qu0Jm7 |  | OPEN |
| V1 | verify | directory root re-plan + function readback | 0-diff re-plan, LastUpdateStatus Successful, describe-rule ENABLED with 3 targets |  | OPEN |
| R1 | git | deploy recorder | record-terraform-deploy commit |  | OPEN |
| W1 | verify | CloudWatch /aws/lambda/irpt-directory-search irpt_warm lines | three lines slots 1/2/3 in three distinct logStreamNames on one tick |  | OPEN |

## Log

- 20260924T051003Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
