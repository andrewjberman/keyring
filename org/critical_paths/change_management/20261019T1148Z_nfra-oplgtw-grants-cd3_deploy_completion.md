# Deploy Completion Record
**Date opened:** 2026-10-19T11:48:57.369440+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-cd-3 Phase B: gateway role family_depth READ grant (1 policy, 4 statements, 1 add, 0 change, 0 destroy), safe-apply targeted, read back from IAM; .tf blob 0f5da21da8d9a68287182a1509b44c6af0a3d75c, ask sha256 b1e10d5e68fd; three halves signed (CTO 673a4582d9 lapsed then re-signed, COO, CVO); GO msg 35947
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | apply gw_family_depth_read then get-role-policy | exactly FOUR Allow statements over events:DescribeRule, s3:GetObject, s3:ListBucket only, the source-root list carrying s3:delimiter StringEquals / |  | OPEN |
| S1 | verify | simulate-principal-policy on the live role, one resource per call, with controls | DescribeRule, GetObject and the source-root list WITH delimiter allowed; the source-root list with NO delimiter, PutRule and PutObject NOT allowed |  | OPEN |
| C1 | verify | the CT3 census, read-only | top-level prefixes of opal-data-assets beyond the eight roots that hold a silver child, counts and names only, in W/FD_CT3_CENSUS.json |  | OPEN |
| V1 | verify | targeted re-plan of the one policy | No changes |  | OPEN |

## Log

- 20261019T114857Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 4 leg(s)
