# Deploy Completion Record
**Date opened:** 2026-09-11T08:51:36.091691+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T085441Z
**Deploy:** IRPT IB-s-15: 11 scoped routes on portal API 7k3ed8px20 under the EXISTING authorizer naqxlm, with AWS_PROXY integrations to six of this project's Lambdas
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | wk-irpt_bckend-1-2 source commit for the api root (routes.tf, integrations.tf, routes.json) and _scope/global.py | commit hash on the worker branch (LOCAL, never pushed) | bef9b459f3 on wk-irpt_bckend-1-2 (LOCAL; a worker never pushes). 8 files, 953 insertions. The OPEN sentinel and the ledger entry rode THIS commit, before the act. | CLOSED 20260911T085240Z |
| L2 | activation | terraform apply of infra/aws/terraform/investor-reporting/api (state key investor-reporting/api/tfstate) adding 11 routes, 6 integrations and 6 lambda permissions | safe-apply output showing ADDED only, 0 changed and 0 destroyed so the 14 existing scoped routes and the naqxlm authorizer are untouched | safe-apply.sh (HALT-GATE passed; session serial file written before the apply) on infra/aws/terraform/investor-reporting/api -> 'Apply complete! Resources: 23 added, 0 changed, 0 destroyed.' -- 11 routes, 6 AWS_PROXY integrations, 6 narrowed lambda:InvokeFunction permissions. The pre-apply plan read the same before the fact: '23 to add, 0 to change, 0 to destroy'. 0 changed and 0 destroyed: the 14 existing scoped routes and the naqxlm authorizer were not touched. | CLOSED 20260911T085425Z |
| L3 | verify | get-routes on 7k3ed8px20 filtered to the investor-reporting prefix | every route key in routes.json status=DECLARED present with AuthorizerId naqxlm, N of N printed | aws apigatewayv2 get-routes --api-id 7k3ed8px20: 84 routes on the api, 11 under /api/scoped/investor-reporting/, 11 of 11 carrying AuthorizationType CUSTOM with AuthorizerId naqxlm. Every route_key in routes.json with status DECLARED is present live: 11 of 11, 0 missing. The 12th route (holdings) is NO-HANDLER-AT-HEAD and is deliberately not declared. | CLOSED 20260911T085441Z |
| L4 | verify | 0-diff terraform plan on the api root (criterion S15-AC2) | plan No changes | terraform plan -no-color -input=false -lock=false on infra/aws/terraform/investor-reporting/api AFTER the apply -> 'No changes. Your infrastructure matches the configuration.' rc=0. That is criterion S15-AC2. | CLOSED 20260911T085441Z |

## Log

- 20260911T085136Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 4 leg(s)
- 20260911T085240Z LEG L1 closed: bef9b459f3 on wk-irpt_bckend-1-2 (LOCAL; a worker never pushes). 8 files, 953 insertions. The OPEN sentinel and the ledg
- 20260911T085425Z LEG L2 closed: safe-apply.sh (HALT-GATE passed; session serial file written before the apply) on infra/aws/terraform/investor-reporting
- 20260911T085441Z LEG L3 closed: aws apigatewayv2 get-routes --api-id 7k3ed8px20: 84 routes on the api, 11 under /api/scoped/investor-reporting/, 11 of 1
- 20260911T085441Z LEG L4 closed: terraform plan -no-color -input=false -lock=false on infra/aws/terraform/investor-reporting/api AFTER the apply -> 'No c
- 20260911T085441Z CLOSED -- all 4 legs proven
