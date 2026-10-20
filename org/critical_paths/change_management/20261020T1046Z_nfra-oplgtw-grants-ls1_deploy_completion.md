# Deploy Completion Record
**Date opened:** 2026-10-20T10:46:58.835878+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ls-1 Phase B: narrow the silver s3:ListBucket list of gateway-family-depth-read-policy to the eight sources (one list, one statement, a strict narrowing); IAM only, no deploy, no downtime; halves signed at ask 7472e5c143d2 and .tf blob 42fee26095
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| apply | activation | one targeted safe-apply of aws_iam_role_policy.gw_family_depth_read, plan re-read 0 to add 1 to change 0 to destroy | proof: the apply output counts in W/LS_APPLY.txt |  | OPEN |
| live-read-back | verify | get-role-policy shows exactly four statements with only per-source silver patterns; simulate-principal-policy on the live role: source prefix allowed, bloomberg gateway yahoo NOT allowed, root list with delimiter allowed and without NOT allowed, unchanged statements allowed, PutRule and PutObject NOT allowed | proof: W/LS_APPLIED.json |  | OPEN |
| family-depth-host-read | verify | the family_depth read once on the host from the deployed tree under the hard guard as the instance role answers the same families and denominator as W/FWD20_DRIVEN_READ.json | proof: W/LS_HOST_READ.json |  | OPEN |

## Log

- 20261020T104658Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
