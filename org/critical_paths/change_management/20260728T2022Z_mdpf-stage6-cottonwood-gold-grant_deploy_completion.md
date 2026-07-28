# Deploy Completion Record
**Date opened:** 2026-07-28T20:22:09.413875+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260728T203131Z
**Deploy:** Stage-6 cottonwood gold grants on mdpf_runner (3 grants: Put+Get on blackdiamond/cottonwood/gold/*, prefix-conditioned ListBucket) -- CTO dispatch 201342Z, AE-base pre-computed 194533Z
**Authored by:** 0.7.0_AE_CloudOps~C
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of iam.tf | commit hash pushed | commit 7d4eeefac (iam.tf + ledger), author 0.7.0_AE_CloudOps~C, pushed to CLOUD | CLOSED 20260728T203131Z |
| L2 | activation | targeted terraform apply -target=aws_iam_role_policy.mdpf_runner | safe-apply output + 0-diff re-plan | safe-apply.sh -target=aws_iam_role_policy.mdpf_runner: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' comp-tagauthz gate SELF-RAN and PASSED, ZERO override (TMPDIR export). Row 10's four resources NOT in plan (Plan: 0 to add, 1 to change, 0 to destroy). | CLOSED 20260728T203131Z |
| L3 | verify | applied truth via aws iam get-role-policy | both Sids present in the LIVE policy document | aws iam get-role-policy mdpf-daily-runner-ec2-role/mdpf-runner-scoped: 25 statements. AssetsCottonwoodGoldWrite Allow [PutObject,GetObject] on opal-data-assets/blackdiamond/cottonwood/gold/*; AssetsCottonwoodGoldList Allow [ListBucket] on opal-data-assets Condition StringLike s3:prefix=[blackdiamond/cottonwood/gold/*]. BOTH P0 Deny statements still LIVE. | CLOSED 20260728T203131Z |
| L4 | verify | 6-control simulate battery T1/T2/T3 allowed + C1/C2/C3 denied, ISOLATED invocations | per-control verdict incl. C3 explicitDeny on json/mdpf serve | 8 ISOLATED invocations, one --resource-arns each. T1 PutObject cottonwood/gold=allowed; T2 GetObject same key=allowed; T3 ListBucket +context cottonwood/gold/=allowed; C2 PutObject cottonwood SILVER=implicitDeny; C3 [STOP] PutObject portal-v2 json/mdpf/global/aggregate-aua-timeseries.json=explicitDeny; C1' ListBucket +context blackdiamond/49financial/gold/=implicitDeny; C4 PutObject 49financial/gold=implicitDeny. PRE-STATE baseline T1/T2=implicitDeny before apply; positive control (separate invocation) gold/mdpf_revamp=allowed; action names validated REAL via accessanalyzer validate-policy. NOTE: dispatch-specified C1 (schwab/08242234/silver) returned ALLOWED -- NON-DISCRIMINATING, granted by pre-existing AssetsRevampListScoped, NOT by my statement; replaced with C1'. | CLOSED 20260728T203131Z |

## Log

- 20260728T202209Z OPENED by 0.7.0_AE_CloudOps~C with 4 leg(s)
- 20260728T203131Z LEG L1 closed: commit 7d4eeefac (iam.tf + ledger), author 0.7.0_AE_CloudOps~C, pushed to CLOUD
- 20260728T203131Z LEG L2 closed: safe-apply.sh -target=aws_iam_role_policy.mdpf_runner: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' com
- 20260728T203131Z LEG L3 closed: aws iam get-role-policy mdpf-daily-runner-ec2-role/mdpf-runner-scoped: 25 statements. AssetsCottonwoodGoldWrite Allow [P
- 20260728T203131Z LEG L4 closed: 8 ISOLATED invocations, one --resource-arns each. T1 PutObject cottonwood/gold=allowed; T2 GetObject same key=allowed; T
- 20260728T203131Z CLOSED -- all 4 legs proven
