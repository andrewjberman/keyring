# Deploy Completion Record
**Date opened:** 2026-10-09T09:35:49.057345+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-k-2 (workstream CP2): the gateway role's one close-request PutObject grant on the globgrph requests/ prefix
**Authored by:** 0.7.0_AE_CloudOps~MP
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | opal-gateway-role gains inline policy gateway-mcportal-close-request-write-policy -- safe-apply with the SAVED plan C:/tmp/mp-k2.tfplan, targeted to aws_iam_role_policy.gw_mcportal_close_request_write only (CTO half condition 1: any other plan line is a STOP) | terraform: 1 added, 0 changed, 0 destroyed |  | OPEN |
| L2 | verify | read-back: k2.AC1.sh (live get-role-policy) + k2.AC2.sh (6-arm simulate-principal-policy, one --resource-arns per call) | AC1 actions=s3:PutObject resources=1 problems=0; AC2 6 of 6 with the GetObject positive control allowed (CTO half condition 2) |  | OPEN |

## Log

- 20261009T093549Z OPENED by 0.7.0_AE_CloudOps~MP with 2 leg(s)
