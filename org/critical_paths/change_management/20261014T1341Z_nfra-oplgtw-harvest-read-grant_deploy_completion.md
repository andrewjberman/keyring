# Deploy Completion Record
**Date opened:** 2026-10-14T13:41:35.084378+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T134955Z
**Deploy:** NFRA_OPLGTW OG-hv-2 ACT 1: the harvest read grant on gateway-global-internal-reader-role (3 halves signed, C1-C3)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the targeted plan immediately before the apply reads 1 to add, 0 to change, 0 to destroy (C3) | the Plan: line from the saved plan file the apply consumes | The saved plan the apply consumed (scratchpad hv2_act1.tfplan, 258526 bytes) reads: 'Plan: 1 to add, 0 to change, 0 to destroy.' and terraform show of that file lists exactly ONE resource, aws_iam_role_policy.int_reader_harvest_read. C3 satisfied at the act, not from an earlier plan. | CLOSED 20261014T134955Z |
| L2 | activation | safe-apply lands ONLY aws_iam_role_policy.int_reader_harvest_read; the role carries gateway-global-harvest-read-policy | the apply output plus get-role-policy read-back of the one name, and the pre-existing internal-reader policy unchanged | safe-apply rc=0, 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.' Read-back: list-role-policies on gateway-global-internal-reader-role returns 2 inline (gateway-global-harvest-read-policy added, gateway-global-internal-reader-policy untouched, 0 attached managed). get-role-policy on the new name: Statement 1 s3:GetObject over 24 object ARNs (24 distinct opal-data-harvest prefixes), Statement 2 s3:ListBucket on the bucket with 48 s3:prefix condition values; no other action. The pre-existing policy still reads exactly s3:GetObject on opal-data-portal-v2/json/* and /platinum/*. NOTE: safe-apply seat-gates ran in WARN mode and printed CROSSBOX-DEPLOY verdict=STOP on an OPEN-CALL hit (org/devices/state/sitez/open_calls.json row sitez-20261009T173038Z-21c5 names root infra/aws/terraform/opal-gateway); under ENFORCE it would have stopped this apply. | CLOSED 20261014T134955Z |
| L3 | verify | the internal reader role reads the served prefixes and nothing else | three isolated simulate-principal-policy calls (packs allowed, wsj/harvest allowed, zzz-not-served implicitDeny) written to W/HV2_IAM_SIM.json | W/HV2_IAM_SIM.json, verdict PASS: packs/1299_HK_Equity/input_ledger.json allowed, wsj/harvest/bronze/article/...20261002T061945Z.html allowed, zzz-not-served/x.json implicitDeny (STAYS, which is the branch that bounds the act), and the same-principal positive control opal-data-portal-v2/json/x.json still allowed. ONE --resource-arns per invocation; head-bucket opal-data-harvest rc=0 so no allowed is the false-ALLOW mode. All three read implicitDeny before the grant. | CLOSED 20261014T134955Z |

## Log

- 20261014T134135Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
- 20261014T134955Z LEG L1 closed: The saved plan the apply consumed (scratchpad hv2_act1.tfplan, 258526 bytes) reads: 'Plan: 1 to add, 0 to change, 0 to d
- 20261014T134955Z LEG L2 closed: safe-apply rc=0, 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.' Read-back: list-role-policies on gateway-
- 20261014T134955Z LEG L3 closed: W/HV2_IAM_SIM.json, verdict PASS: packs/1299_HK_Equity/input_ledger.json allowed, wsj/harvest/bronze/article/...20261002
- 20261014T134955Z CLOSED -- all 3 legs proven
