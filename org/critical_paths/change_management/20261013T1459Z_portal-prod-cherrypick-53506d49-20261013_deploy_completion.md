# Deploy Completion Record
**Date opened:** 2026-10-13T14:59:49.674223+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261013T151315Z
**Deploy:** Portal PROD: cherry-pick 53506d49 (firmAccess.ts generated FIRM_ALLOWED_PATHS block, comments only, sets unchanged) alone onto PROD via /prod-deploy; Andrew-direct 2026-10-13 ~14:3xZ call 2(a)
**Authored by:** 0.2.0_DT_PortfolioAnalytics~PD
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal origin/PROD cherry-pick of 53506d49 | PROD head sha pushed (ls-remote read) and diff vs prior PROD limited to src/lib/firmAccess.ts | origin/PROD 37aa1247 -> 15c97549 (git ls-remote read 15c97549); cherry-pick -x of 53506d49 alone; git diff --stat vs 37aa1247 = src/lib/firmAccess.ts only (35+/33-); typecheck rc=0; FIRM_ALLOWED_PATHS sets equal old vs new (4 firms, 35 page pairs); rollback = git revert 15c97549 on PROD | CLOSED 20261013T151314Z |
| L2 | verify | deploy.yml CI on that sha | gh run view conclusion success, all workflows by headSha, tag peeled to PROD head | Deploy to Production run 38419297038 on 15c97549 completed success (only workflow on that sha, denominator 1); tag portal-v2.1.212 peels to 15c97549 = PROD head | CLOSED 20261013T151315Z |

## Log

- 20261013T145949Z OPENED by 0.2.0_DT_PortfolioAnalytics~PD with 2 leg(s)
- 20261013T151314Z LEG L1 closed: origin/PROD 37aa1247 -> 15c97549 (git ls-remote read 15c97549); cherry-pick -x of 53506d49 alone; git diff --stat vs 37a
- 20261013T151315Z LEG L2 closed: Deploy to Production run 38419297038 on 15c97549 completed success (only workflow on that sha, denominator 1); tag porta
- 20261013T151315Z CLOSED -- all 2 legs proven
