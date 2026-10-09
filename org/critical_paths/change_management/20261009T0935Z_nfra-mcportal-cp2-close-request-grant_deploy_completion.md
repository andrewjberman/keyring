# Deploy Completion Record
**Date opened:** 2026-10-09T09:35:49.057345+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T094436Z
**Deploy:** NFRA_MCPORTAL MP-k-2 (workstream CP2): the gateway role's one close-request PutObject grant on the globgrph requests/ prefix
**Authored by:** 0.7.0_AE_CloudOps~MP
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | opal-gateway-role gains inline policy gateway-mcportal-close-request-write-policy -- safe-apply with the SAVED plan C:/tmp/mp-k2.tfplan, targeted to aws_iam_role_policy.gw_mcportal_close_request_write only (CTO half condition 1: any other plan line is a STOP) | terraform: 1 added, 0 changed, 0 destroyed | APPLIED via .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply C:/tmp/mp-k2.tfplan (the SAVED plan, rc=0). NOT taken from rc: verified against live state and config. (a) terraform state list -> aws_iam_role_policy.gw_mcportal_close_request_write present, grep -c = 1, and MP-x-3's aws_iam_role_policy.gw_mcportal_fabric_read still present and untouched. (b) live IAM read, k2.AC1.sh -> 'actions=s3:PutObject resources=1 problems=0' RESULT: PASS. (c) targeted 0-diff confirmation plan -> 'No changes. Your infrastructure matches the configuration.' CTO half condition 1 met: the saved plan was the only thing applied and it carried exactly the one addition. | CLOSED 20261009T094326Z |
| L2 | verify | read-back: k2.AC1.sh (live get-role-policy) + k2.AC2.sh (6-arm simulate-principal-policy, one --resource-arns per call) | AC1 actions=s3:PutObject resources=1 problems=0; AC2 6 of 6 with the GetObject positive control allowed (CTO half condition 2) | READ-BACK PASS, both checks, with the pre-act negative arm beside the post-act positive one. k2.AC1.sh -> 'actions=s3:PutObject resources=1 problems=0' RESULT: PASS (pre-act the same call returned NoSuchEntity rc=254). k2.AC2.sh -> 'simulation arms matched 6 of 6' RESULT: PASS, one --resource-arns per call, each its own invocation: put request allowed / put list implicitDeny / put result implicitDeny / put activity implicitDeny / delete request implicitDeny / get list (GetObject positive control) allowed. DISCRIMINATING DELTA vs the pre-act control banked at deliverables/0.7.0_AE_CloudOps~MP/MP-k-2_PRE_ACT_CONTROL.md (5 of 6): EXACTLY ONE arm moved, put request implicitDeny -> allowed; the four refusals and the control are unmoved, so the change is attributable to this one statement and not to an instrument that allows everything. CTO half condition 2 met: 6 of 6 with the GetObject control allowed, so the sheet is not an all-implicitDeny instrument fault. No S3 object was written by this seat; the simulation is the exercise per the TO's BOUNDS. | CLOSED 20261009T094352Z |

## Log

- 20261009T093549Z OPENED by 0.7.0_AE_CloudOps~MP with 2 leg(s)
- 20261009T094326Z LEG L1 closed: APPLIED via .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply C:/tmp/mp-k2.tfplan (the SAVED plan, rc=0
- 20261009T094352Z LEG L2 closed: READ-BACK PASS, both checks, with the pre-act negative arm beside the post-act positive one. k2.AC1.sh -> 'actions=s3:Pu
- 20261009T094436Z CLOSED -- all 2 legs proven
