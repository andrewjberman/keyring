# Deploy Completion Record
**Date opened:** 2026-10-20T10:46:58.835878+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T110238Z
**Deploy:** NFRA_OPLGTW OG-ls-1 Phase B: narrow the silver s3:ListBucket list of gateway-family-depth-read-policy to the eight sources (one list, one statement, a strict narrowing); IAM only, no deploy, no downtime; halves signed at ask 7472e5c143d2 and .tf blob 42fee26095
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| apply | activation | one targeted safe-apply of aws_iam_role_policy.gw_family_depth_read, plan re-read 0 to add 1 to change 0 to destroy | proof: the apply output counts in W/LS_APPLY.txt | one safe-apply of the saved targeted plan: Plan 0 to add 1 to change 0 to destroy; Apply complete 0 added 1 changed 0 destroyed (W/LS_APPLY.txt); .tf blob 42fee26095 as signed | CLOSED 20261020T110238Z |
| live-read-back | verify | get-role-policy shows exactly four statements with only per-source silver patterns; simulate-principal-policy on the live role: source prefix allowed, bloomberg gateway yahoo NOT allowed, root list with delimiter allowed and without NOT allowed, unchanged statements allowed, PutRule and PutObject NOT allowed | proof: W/LS_APPLIED.json | get-role-policy: four statements, sixteen per-source silver patterns, hash prefix c67f734cff (was 2dd3ee621b); simulate-principal-policy on the live role 11 of 11 as expected (W/LS_LIVE.json, W/LS_APPLIED.json) | CLOSED 20261020T110238Z |
| family-depth-host-read | verify | the family_depth read once on the host from the deployed tree under the hard guard as the instance role answers the same families and denominator as W/FWD20_DRIVEN_READ.json | proof: W/LS_HOST_READ.json | family_depth read once on the host from the deployed tree (marker 13917ef993) under the cgroup hard guard as the instance role: 13 of 13 families, 59 values, claims and boto3 operation counts equal W/FWD20_DRIVEN_READ.json, 0 writes (W/LS_HOST_READ.json) | CLOSED 20261020T110238Z |

## Log

- 20261020T104658Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261020T110238Z LEG apply closed: one safe-apply of the saved targeted plan: Plan 0 to add 1 to change 0 to destroy; Apply complete 0 added 1 changed 0 de
- 20261020T110238Z LEG live-read-back closed: get-role-policy: four statements, sixteen per-source silver patterns, hash prefix c67f734cff (was 2dd3ee621b); simulate-
- 20261020T110238Z LEG family-depth-host-read closed: family_depth read once on the host from the deployed tree (marker 13917ef993) under the cgroup hard guard as the instanc
- 20261020T110238Z CLOSED -- all 3 legs proven
