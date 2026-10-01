# Deploy Completion Record
**Date opened:** 2026-10-01T00:14:11.628489+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T001946Z
**Deploy:** MDPF_TAXSMA TX-i-2: the egress publisher role's read of the one Tax control key (mdpf-publisher-taxsma-control-read-policy); opal-assets root, 1 create, nothing else
**Authored by:** 4.0.0_SA_CRO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | fresh saved plan of infra/aws/terraform/opal-assets from the shared tree | Plan 1/0/0 = aws_iam_role_policy.mdpf_egress_publisher_taxsma_control; baseline before the edit: No changes | Saved plan 00:1xZ from the shared tree (file content = bf643a0530; vendored terraform 1.9.8): Plan 1 to add, 0 to change, 0 to destroy = aws_iam_role_policy.mdpf_egress_publisher_taxsma_control named mdpf-publisher-taxsma-control-read-policy. Baseline plan 22:1xZ before the edit: No changes. | CLOSED 20261001T001658Z |
| D1 | activation | safe-apply of the saved plan | apply complete 1 added; re-plan No changes | safe-apply 00:16:59Z of the saved plan (vendored terraform 1.9.8; naming plan limb WARN 119 graded, 0 REFUSE; tag-authz SKIP, no default_tags in this root): Apply complete, 1 added 0 changed 0 destroyed -- opal-assets-mdpf-egress-publisher-role:mdpf-publisher-taxsma-control-read-policy. Re-plan 00:17Z: No changes. | CLOSED 20261001T001945Z |
| V1 | verify | the publisher role's grants | control key GetObject allowed; taxsma_assets, dispositions, workbook, secret denied; existing served-write and Gold grants unchanged | SIMULATED, NOT EXERCISED (the role trusts only Lambda). iam simulate-principal-policy 2026-10-01T00:18Z, 10 rows, one resource per call, the 49financial bucket policy passed as the resource policy: 10 of 10 as expected. Control key GetObject allowed; control PutObject, another opal-data-mdpf key, workbook Bronze/Silver, the capability secret implicitDeny; 49financial taxsma_assets and dispositions explicitDeny (the fence); positive controls -- existing canonical Gold read and served platinum put -- allowed. get-role-policy: one statement, s3:GetObject on the exact control key; inline policies on the role 3. EXERCISE owed at the first publisher run with the rollout switch ON (TX-r-3). | CLOSED 20261001T001945Z |

## Log

- 20261001T001411Z OPENED by 4.0.0_SA_CRO with 3 leg(s)
- 20261001T001658Z LEG P1 closed: Saved plan 00:1xZ from the shared tree (file content = bf643a0530; vendored terraform 1.9.8): Plan 1 to add, 0 to change
- 20261001T001945Z LEG D1 closed: safe-apply 00:16:59Z of the saved plan (vendored terraform 1.9.8; naming plan limb WARN 119 graded, 0 REFUSE; tag-authz 
- 20261001T001945Z LEG V1 closed: SIMULATED, NOT EXERCISED (the role trusts only Lambda). iam simulate-principal-policy 2026-10-01T00:18Z, 10 rows, one re
- 20261001T001946Z CLOSED -- all 3 legs proven
