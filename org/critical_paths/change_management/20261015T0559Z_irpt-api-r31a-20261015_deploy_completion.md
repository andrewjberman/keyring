# Deploy Completion Record
**Date opened:** 2026-10-15T05:59:00.808797+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R31A: release 31 leg A -- ONE gateway route through the api Terraform root: GET /api/scoped/investor-reporting/analysis/requests/{requestId}/commentary-pdf on API 7k3ed8px20, target the irpt-status integration, CUSTOM authorizer naqxlm (widening W8); plan gate exactly 1 to add, 0 to change, 0 to destroy at that one address; signed Addendum 1 (COO blob 322dbb2410, CTO msg 8088); runs after leg L (closed); rollback is Terraform only: the contract row status off DECLARED, plan 0/0/1, safe-apply, never delete-route
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P | verify | R0s: contract blob printed; terraform init (existing backend) and plan -lock=false to a saved plan reads exactly 1 add 0 change 0 destroy at the one address aws_apigatewayv2_route.irpt[GET .../commentary-pdf]; every resource line printed; live route list read whole (count and no key ending /commentary-pdf; the irpt-status integration id) | plan lines and route count |  | OPEN |
| A | activation | .tools/safe-apply.sh on the saved plan | apply line |  | OPEN |
| V | verify | A1 get-routes: the route present, target the irpt-status integration, authorizer naqxlm, CUSTOM, count 122; A2 replan No changes; A3 credential-less GET equals the control and says non-discriminating; A4 report pdf route as before | printed reads and A_AFTER_R31A.txt |  | OPEN |

## Log

- 20261015T055900Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
