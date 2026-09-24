# Deploy Completion Record
**Date opened:** 2026-09-24T05:10:03.566175+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T052514Z
**Deploy:** irpt-directory-search option-B keep-warm: one rule, three concurrent targets (replaces the scheduler) + served.py warm hold @9cf6a63d6f (CRO e1476853c9, CTO GO 100264)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | directory root: rule + 3 targets + permission created, scheduler + role + policy destroyed, function updated | safe-apply of saved plan ea0921b91e 5/1/3, readback CodeSha256 o9Qu0Jm7 | safe-apply (tools terraform 1.9.8, backend worktree directory root) of saved plan ea0921b91e 5/1/3: Apply complete 5 added / 1 changed / 3 destroyed rc=0 at 05:16:16Z, log 787c78abe1bb5f31; readback CodeSha256 o9Qu0Jm7jidtrlBeGWD9d2ZsxROK3NXcQTEOUOMvGus= LastModified 05:16:11Z Active Successful memory 1769 | CLOSED 20260924T052152Z |
| V1 | verify | directory root re-plan + function readback | 0-diff re-plan, LastUpdateStatus Successful, describe-rule ENABLED with 3 targets | re-plan -detailed-exitcode rc=0 No changes at 05:18Z; describe-rule irpt-directory-keepwarm-5min ENABLED rate(5 minutes); list-targets-by-rule 3 targets slot-1/2/3 each input irpt_warm true, hold 500 ms; scheduler get-schedule irpt-directory-keepwarm-5min returns nothing (destroyed) | CLOSED 20260924T052153Z |
| R1 | git | deploy recorder | record-terraform-deploy commit | record-terraform-deploy.sh investor-reporting --function irpt-directory-search: commit d79dac8675 on irpt-p-publish-20260923 (after merge 11bcbbf6d5 of the backend head 9f360e8f3b) | CLOSED 20260924T052312Z |
| W1 | verify | CloudWatch /aws/lambda/irpt-directory-search irpt_warm lines | three lines slots 1/2/3 in three distinct logStreamNames on one tick | CloudWatch filter irpt_warm on /aws/lambda/irpt-directory-search since 05:16Z, read 05:24:11Z: 6 lines over two ticks (05:16:47 and 05:21:47), each tick slots 1/2/3, in THREE distinct logStreamNames (..89d7cd9a8a6837, ..e4ab28ce9557cd, ..2b646152c70a73), hold_ms 500 -- the CTO's receipt criterion met on both ticks | CLOSED 20260924T052514Z |

## Log

- 20260924T051003Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260924T052152Z LEG A1 closed: safe-apply (tools terraform 1.9.8, backend worktree directory root) of saved plan ea0921b91e 5/1/3: Apply complete 5 add
- 20260924T052153Z LEG V1 closed: re-plan -detailed-exitcode rc=0 No changes at 05:18Z; describe-rule irpt-directory-keepwarm-5min ENABLED rate(5 minutes)
- 20260924T052312Z LEG R1 closed: record-terraform-deploy.sh investor-reporting --function irpt-directory-search: commit d79dac8675 on irpt-p-publish-2026
- 20260924T052514Z LEG W1 closed: CloudWatch filter irpt_warm on /aws/lambda/irpt-directory-search since 05:16Z, read 05:24:11Z: 6 lines over two ticks (0
- 20260924T052514Z CLOSED -- all 4 legs proven
