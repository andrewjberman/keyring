# Deploy Completion Record
**Date opened:** 2026-09-11T08:51:36.091691+00:00
**Status:** OPEN
**Deploy:** IRPT IB-s-15: 11 scoped routes on portal API 7k3ed8px20 under the EXISTING authorizer naqxlm, with AWS_PROXY integrations to six of this project's Lambdas
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | wk-irpt_bckend-1-2 source commit for the api root (routes.tf, integrations.tf, routes.json) and _scope/global.py | commit hash on the worker branch (LOCAL, never pushed) |  | OPEN |
| L2 | activation | terraform apply of infra/aws/terraform/investor-reporting/api (state key investor-reporting/api/tfstate) adding 11 routes, 6 integrations and 6 lambda permissions | safe-apply output showing ADDED only, 0 changed and 0 destroyed so the 14 existing scoped routes and the naqxlm authorizer are untouched |  | OPEN |
| L3 | verify | get-routes on 7k3ed8px20 filtered to the investor-reporting prefix | every route key in routes.json status=DECLARED present with AuthorizerId naqxlm, N of N printed |  | OPEN |
| L4 | verify | 0-diff terraform plan on the api root (criterion S15-AC2) | plan No changes |  | OPEN |

## Log

- 20260911T085136Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 4 leg(s)
