# Deploy Completion Record
**Date opened:** 2026-10-02T05:46:42.043635+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD DB-b-5: apply the reporting-read root (8 new resources; packet blob f44ee4d312, CTO half batch 115)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | re-plan of reporting-read at HEAD | 8 to add, 0 to change, 0 to destroy; trees equal to @81bc2e6f4f | terraform plan -lock=false at CLOUD 221b0b0dc4 (05:4xZ): Plan: 8 to add, 0 to change, 0 to destroy; git diff 81bc2e6f4f..HEAD on reporting-read/ and reporting/ = 0 lines | CLOSED 20261002T055539Z |
| D1 | activation | safe-apply of infra/aws/terraform/investor-reporting/reporting-read | apply complete, 8 added | HALT_ACK=1 .tools/safe-apply.sh apply of the saved plan, 05:52:22Z: Apply complete! Resources: 8 added, 0 changed, 0 destroyed (route id 3smc8xr, integration 904xvoc); halt gate listed 40 routine historic messages, no STOP/HALT | CLOSED 20261002T055540Z |
| V1 | verify | post-apply readback | CodeSha256 dKMqVb..., route on CUSTOM naqxlm, 17 existing routes unchanged, re-plan No changes | get-function-configuration irpt-49f-reporting-read-lambda: CodeSha256 dKMqVbKWyZJV+0txPH16QGwLoC/HfsyGHoOdo1lGuS8= State Active role irpt-49f-reporting-read-role; get-routes 7k3ed8px20: 18 investor-reporting routes, the new key on CUSTOM naqxlm -> integrations/904xvoc, 17 of 17 prior routes unchanged (key, auth type, authorizer; CR-stripped diff); re-plan: No changes | CLOSED 20261002T055540Z |
| N1 | verify | negative control | unauthenticated GET refused by the authorizer; no invocation logged | unauthenticated curl GET https://7k3ed8px20.execute-api.us-east-1.amazonaws.com/api/scoped/investor-reporting/reporting/0010783709/manifest at 05:54Z: http=401 body {"message":"Unauthorized"}; describe-log-streams /aws/lambda/irpt-49f-reporting-read-lambda: 0 streams (no invocation) | CLOSED 20261002T055540Z |
| A1 | verify | workstream F signed-in fetch (FWD-1 real run) | one covered account's series fetched through the route, as-of 2026-09-28 shown |  | OPEN |

## Log

- 20261002T054642Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20261002T055539Z LEG P1 closed: terraform plan -lock=false at CLOUD 221b0b0dc4 (05:4xZ): Plan: 8 to add, 0 to change, 0 to destroy; git diff 81bc2e6f4f.
- 20261002T055540Z LEG D1 closed: HALT_ACK=1 .tools/safe-apply.sh apply of the saved plan, 05:52:22Z: Apply complete! Resources: 8 added, 0 changed, 0 des
- 20261002T055540Z LEG V1 closed: get-function-configuration irpt-49f-reporting-read-lambda: CodeSha256 dKMqVbKWyZJV+0txPH16QGwLoC/HfsyGHoOdo1lGuS8= State
- 20261002T055540Z LEG N1 closed: unauthenticated curl GET https://7k3ed8px20.execute-api.us-east-1.amazonaws.com/api/scoped/investor-reporting/reporting/
