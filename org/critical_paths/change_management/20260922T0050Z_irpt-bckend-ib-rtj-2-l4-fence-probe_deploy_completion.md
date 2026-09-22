# Deploy Completion Record
**Date opened:** 2026-09-22T00:50:12.565612+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND.TO-IB-rtj-2 -- the L4 bounded test principal: role irpt-fence-probe-l4-role (lib/opal_naming.py name('irpt',None,'fence-probe','role','l4')) + inline policy irpt-fence-probe-l4-policy = {"Statement":[{"Action":"s3:ListBucket","Effect":"Allow","Resource":["arn:aws:s3:::opal-data-inflection","arn:aws:s3:::opal-data-cottonwood","arn:aws:s3:::opal-313476888478-lambda-artifacts"],"Sid":"ListBucketOnlyThreeBuckets"}],"Version":"2012-10-17"}; trust = sts:AssumeRole by user/Andrew_Berman only. Root infra/aws/terraform/investor-reporting/l4-fence-probe (own state key). NOTHING APPLIES UNTIL the CTO + CRO halves are at HEAD naming packet NEVER_WIDEN_SIGNOFF_PACKET_IB-rtj-2.md. ENDS WITH: plan -destroy (exactly 2 deletions) -> safe-apply apply <destroy plan> -> aws iam get-role returns NoSuchEntity (printed) -> the root's .tf files removed and committed. Closes leg L4 of 20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets if it discriminates (CTO 99312 CALL 1).
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | infra/aws/terraform/investor-reporting/l4-fence-probe: aws_iam_role.l4_fence_probe + aws_iam_role_policy.l4_fence_probe_listbucket | both halves at HEAD naming the packet; saved plan EXACTLY 2 creates; safe-apply rc=0 'Apply complete! Resources: 2 added'; get-role + get-role-policy read back == the packet's policies |  | OPEN |
| L2 | verify | positive arm: control opal-313476888478-lambda-artifacts | list-objects-v2 under the assumed role session SUCCEEDS, wire result printed |  | OPEN |
| L3 | verify | negative arms: opal-data-inflection + opal-data-cottonwood (2 of 2) + attribution control opal-data-assets | each fenced bucket AccessDenied with S3 error context 'explicit deny in a resource-based policy' (CloudTrail if a data-event trail covers them); control bucket AccessDenied 'no identity-based policy allows' |  | OPEN |
| L4 | activation | DESTROY infra/aws/terraform/investor-reporting/l4-fence-probe | saved plan -destroy EXACTLY 2 deletions; safe-apply apply <destroy plan> rc=0 'Resources: 0 added, 0 changed, 2 destroyed' |  | OPEN |
| L5 | verify | role gone + declaration removed | aws iam get-role --role-name irpt-fence-probe-l4-role -> NoSuchEntity, printed verbatim; the root's .tf files deleted and committed |  | OPEN |

## Log

- 20260922T005012Z OPENED by 0.7.0_AE_CloudOps~V with 5 leg(s)
