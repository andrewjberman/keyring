# Deploy Completion Record
**Date opened:** 2026-10-19T11:48:57.369440+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261019T121225Z
**Deploy:** NFRA_OPLGTW OG-cd-3 Phase B: gateway role family_depth READ grant (1 policy, 4 statements, 1 add, 0 change, 0 destroy), safe-apply targeted, read back from IAM; .tf blob 0f5da21da8d9a68287182a1509b44c6af0a3d75c, ask sha256 b1e10d5e68fd; three halves signed (CTO 673a4582d9 lapsed then re-signed, COO, CVO); GO msg 35947
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | apply gw_family_depth_read then get-role-policy | exactly FOUR Allow statements over events:DescribeRule, s3:GetObject, s3:ListBucket only, the source-root list carrying s3:delimiter StringEquals / | safe-apply targeted (HALT_ACK after the 77 pending messages were reviewed, none a hold): plan at the apply 1 add 0 change 0 destroy, Apply complete 1 added 0 changed 0 destroyed 2026-10-19T12:04Z; .tf blob 0f5da21da8d9a68287182a1509b44c6af0a3d75c; get-role-policy opal-gateway-role/gateway-family-depth-read-policy: exactly 4 Allow statements, actions events:DescribeRule, s3:GetObject, s3:ListBucket only, the source-root list statement carrying s3:delimiter StringEquals /; policy sha256-16 2dd3ee621be1436d; role inline policies 24 -> 25, the other 24 unchanged | CLOSED 20261019T121224Z |
| S1 | verify | simulate-principal-policy on the live role, one resource per call, with controls | DescribeRule, GetObject and the source-root list WITH delimiter allowed; the source-root list with NO delimiter, PutRule and PutObject NOT allowed | simulate-principal-policy on the live role, one resource per call: DescribeRule allowed on a real sweep-rule ARN, GetObject allowed on a real backfill-status key ARN, source-root list (prefix schwab/) WITH delimiter / allowed, NO delimiter implicitDeny, other delimiter implicitDeny; silver list with no delimiter allowed; gold list and no-prefix list implicitDeny; PutRule, PutObject, DeleteObject implicitDeny; W/FD_APPLIED.json | CLOSED 20261019T121224Z |
| C1 | verify | the CT3 census, read-only | top-level prefixes of opal-data-assets beyond the eight roots that hold a silver child, counts and names only, in W/FD_CT3_CENSUS.json | W/FD_CT3_CENSUS.json (read-only list calls from this seats own role, 186 calls): 19 top-level prefixes, 12 beyond the eight sources, 4 hold a silver child under a scope (bloomberg, commonwealth, gateway, yahoo; none directly); msn is not a top-level prefix; 109 silver tables under the eight roots, 35238 date= partition folders and 1 non-date (snapshot_date=). The CTO rule: a non-zero count is reported and statement (a) is narrowed in the OG-ap-50 cycle | CLOSED 20261019T121225Z |
| V1 | verify | targeted re-plan of the one policy | No changes | terraform plan -lock=false targeted at aws_iam_role_policy.gw_family_depth_read after the apply: No changes. Your infrastructure matches the configuration. | CLOSED 20261019T121225Z |

## Log

- 20261019T114857Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 4 leg(s)
- 20261019T121224Z LEG P1 closed: safe-apply targeted (HALT_ACK after the 77 pending messages were reviewed, none a hold): plan at the apply 1 add 0 chang
- 20261019T121224Z LEG S1 closed: simulate-principal-policy on the live role, one resource per call: DescribeRule allowed on a real sweep-rule ARN, GetObj
- 20261019T121225Z LEG C1 closed: W/FD_CT3_CENSUS.json (read-only list calls from this seats own role, 186 calls): 19 top-level prefixes, 12 beyond the ei
- 20261019T121225Z LEG V1 closed: terraform plan -lock=false targeted at aws_iam_role_policy.gw_family_depth_read after the apply: No changes. Your infras
- 20261019T121225Z CLOSED -- all 4 legs proven
